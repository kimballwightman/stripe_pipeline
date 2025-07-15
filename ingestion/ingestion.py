"""
Main ingestion script for loading Stripe data into BigQuery.
"""

import os
import json
import logging
import logging.config
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path
import pandas as pd
from google.cloud import bigquery
from google.cloud.exceptions import NotFound
import structlog

from config import (
    PROJECT_ID, DATASET, LOCATION, DATA_INPUT_PATH, 
    RAW_TABLE_SCHEMAS, LOGGING_CONFIG, ENVIRONMENT
)

# Configure logging
logging.config.dictConfig(LOGGING_CONFIG)
logger = structlog.get_logger(__name__)

class StripeDataIngestion:
    """Handles ingestion of Stripe data into BigQuery."""
    
    def __init__(self, project_id: str = PROJECT_ID, dataset_id: str = DATASET, 
                 location: str = LOCATION):
        """Initialize the ingestion client."""
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.location = location
        self.client = bigquery.Client(project=project_id)
        self.dataset_ref = self.client.dataset(dataset_id)
        
        logger.info(
            "Initialized ingestion client",
            project_id=project_id,
            dataset_id=dataset_id,
            location=location,
            environment=ENVIRONMENT
        )
    
    def create_dataset_if_not_exists(self) -> None:
        """Create the dataset if it doesn't exist."""
        try:
            self.client.get_dataset(self.dataset_ref)
            logger.info("Dataset already exists", dataset_id=self.dataset_id)
        except NotFound:
            dataset = bigquery.Dataset(self.dataset_ref)
            dataset.location = self.location
            dataset.description = f"Stripe data for {ENVIRONMENT} environment"
            
            # Set labels for environment tracking
            dataset.labels = {
                "environment": ENVIRONMENT.lower(),
                "project": "stripe_analytics",
                "created_by": "ingestion_pipeline"
            }
            
            dataset = self.client.create_dataset(dataset, timeout=30)
            logger.info("Created dataset", dataset_id=self.dataset_id)
    
    def create_table_if_not_exists(self, table_name: str, schema: List[Dict[str, Any]]) -> None:
        """Create a table if it doesn't exist."""
        table_ref = self.dataset_ref.table(table_name)
        
        try:
            self.client.get_table(table_ref)
            logger.info("Table already exists", table_name=table_name)
        except NotFound:
            # Convert schema to BigQuery format
            bq_schema = []
            for field in schema:
                field_type = field["type"]
                field_mode = field["mode"]
                
                bq_field = bigquery.SchemaField(
                    name=field["name"],
                    field_type=field_type,
                    mode=field_mode
                )
                bq_schema.append(bq_field)
            
            table = bigquery.Table(table_ref, schema=bq_schema)
            table.description = f"Raw Stripe {table_name} data"
            
            # Set table labels
            table.labels = {
                "environment": ENVIRONMENT.lower(),
                "data_source": "stripe",
                "table_type": "raw"
            }
            
            table = self.client.create_table(table, timeout=30)
            logger.info("Created table", table_name=table_name, num_columns=len(bq_schema))
    
    def load_json_file(self, file_path: str) -> List[Dict[str, Any]]:
        """Load data from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            if isinstance(data, list):
                return data
            else:
                return [data]  # Wrap single object in list
                
        except Exception as e:
            logger.error("Failed to load JSON file", file_path=file_path, error=str(e))
            raise
    
    def prepare_data_for_bq(self, data: List[Dict[str, Any]], table_name: str) -> List[Dict[str, Any]]:
        """Prepare data for BigQuery ingestion by adding metadata and handling types."""
        current_time = datetime.utcnow()
        
        prepared_data = []
        for record in data:
            # Create a copy to avoid modifying original
            prepared_record = record.copy()
            
            # Add ingestion metadata
            prepared_record['_ingested_at'] = current_time
            prepared_record['_updated_at'] = current_time
            
            # Convert Unix timestamps to datetime objects
            timestamp_fields = ['created', 'updated', 'trial_start', 'trial_end', 
                              'current_period_start', 'current_period_end', 
                              'canceled_at', 'ended_at', 'start_date', 'cancel_at',
                              'due_date', 'effective_at', 'period_start', 'period_end',
                              'paid_at', 'next_payment_attempt', 'webhooks_delivered_at',
                              'billing_cycle_anchor', 'subscription_proration_date',
                              'date', 'voided_at']
            
            for field in timestamp_fields:
                if field in prepared_record and prepared_record[field] is not None:
                    try:
                        if isinstance(prepared_record[field], (int, float)):
                            prepared_record[field] = datetime.fromtimestamp(prepared_record[field])
                        elif isinstance(prepared_record[field], str):
                            # Handle ISO format strings
                            prepared_record[field] = datetime.fromisoformat(prepared_record[field].replace('Z', '+00:00'))
                    except (ValueError, TypeError) as e:
                        logger.warning(
                            "Failed to convert timestamp", 
                            field=field, 
                            value=prepared_record[field], 
                            error=str(e)
                        )
                        prepared_record[field] = None
            
            # Ensure JSON fields are properly serialized
            json_fields = ['metadata', 'address', 'shipping', 'invoice_settings', 
                          'automatic_tax', 'billing_thresholds', 'cancellation_details',
                          'default_tax_rates', 'discount', 'invoice_settings', 'items',
                          'pause_collection', 'payment_settings', 'pending_invoice_item_interval',
                          'pending_update', 'transfer_data', 'trial_settings', 'card',
                          'billing_details', 'us_bank_account', 'destination_details',
                          'next_action', 'evidence', 'evidence_details', 'payment_method_details',
                          'fraud_details', 'outcome', 'refunds', 'source', 'custom_fields',
                          'customer_address', 'customer_shipping', 'customer_tax_ids',
                          'discounts', 'from_invoice', 'issuer', 'last_finalization_error',
                          'lines', 'payment_settings', 'rendering', 'rendering_options',
                          'shipping_cost', 'shipping_details', 'status_transitions',
                          'subscription_details', 'total_discount_amounts', 'total_tax_amounts',
                          'features', 'package_dimensions', 'currency_options', 'custom_unit_amount',
                          'recurring', 'tiers', 'transform_quantity', 'balance_transactions',
                          'discount_amounts', 'tax_amounts', 'period', 'price', 'tax_rates',
                          'verification', 'account_tax_ids']
            
            for field in json_fields:
                if field in prepared_record and prepared_record[field] is not None:
                    if not isinstance(prepared_record[field], str):
                        prepared_record[field] = json.dumps(prepared_record[field])
            
            prepared_data.append(prepared_record)
        
        return prepared_data
    
    def load_data_to_table(self, table_name: str, data: List[Dict[str, Any]], 
                          write_disposition: str = "WRITE_TRUNCATE") -> None:
        """Load data into a BigQuery table."""
        if not data:
            logger.warning("No data to load", table_name=table_name)
            return
        
        table_ref = self.dataset_ref.table(table_name)
        
        # Configure the load job
        job_config = bigquery.LoadJobConfig(
            write_disposition=write_disposition,
            source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
            ignore_unknown_values=True,
            max_bad_records=10,
            autodetect=False  # Use predefined schema
        )
        
        # Convert data to NDJSON format
        ndjson_data = "\n".join([json.dumps(record) for record in data])
        
        try:
            job = self.client.load_table_from_json(
                data, table_ref, job_config=job_config
            )
            job.result()  # Wait for the job to complete
            
            logger.info(
                "Successfully loaded data to table",
                table_name=table_name,
                rows_loaded=len(data),
                job_id=job.job_id
            )
            
        except Exception as e:
            logger.error(
                "Failed to load data to table",
                table_name=table_name,
                error=str(e),
                job_id=job.job_id if 'job' in locals() else None
            )
            raise
    
    def ingest_stripe_data(self, data_path: str = DATA_INPUT_PATH, 
                          write_disposition: str = "WRITE_TRUNCATE") -> Dict[str, int]:
        """Ingest all Stripe data files into BigQuery."""
        logger.info("Starting Stripe data ingestion", data_path=data_path)
        
        # Create dataset if it doesn't exist
        self.create_dataset_if_not_exists()
        
        ingestion_stats = {}
        data_path_obj = Path(data_path)
        
        # Process each data type
        for table_name, schema in RAW_TABLE_SCHEMAS.items():
            file_path = data_path_obj / f"{table_name}.json"
            
            if not file_path.exists():
                logger.warning("Data file not found", file_path=str(file_path))
                ingestion_stats[table_name] = 0
                continue
            
            try:
                # Create table if it doesn't exist
                self.create_table_if_not_exists(table_name, schema)
                
                # Load and prepare data
                raw_data = self.load_json_file(str(file_path))
                prepared_data = self.prepare_data_for_bq(raw_data, table_name)
                
                # Load data to BigQuery
                self.load_data_to_table(table_name, prepared_data, write_disposition)
                
                ingestion_stats[table_name] = len(prepared_data)
                
            except Exception as e:
                logger.error(
                    "Failed to ingest data for table",
                    table_name=table_name,
                    error=str(e)
                )
                ingestion_stats[table_name] = -1  # Indicate failure
        
        logger.info("Completed Stripe data ingestion", stats=ingestion_stats)
        return ingestion_stats
    
    def validate_ingestion(self) -> Dict[str, Any]:
        """Validate the ingested data by running basic checks."""
        logger.info("Starting ingestion validation")
        
        validation_results = {}
        
        for table_name in RAW_TABLE_SCHEMAS.keys():
            table_ref = self.dataset_ref.table(table_name)
            
            try:
                # Check if table exists
                table = self.client.get_table(table_ref)
                
                # Get row count
                query = f"SELECT COUNT(*) as row_count FROM `{self.project_id}.{self.dataset_id}.{table_name}`"
                row_count_result = self.client.query(query).result()
                row_count = list(row_count_result)[0].row_count
                
                # Check for recent data
                query = f"""
                SELECT 
                    MIN(_ingested_at) as min_ingested_at,
                    MAX(_ingested_at) as max_ingested_at,
                    COUNT(DISTINCT id) as unique_records
                FROM `{self.project_id}.{self.dataset_id}.{table_name}`
                """
                
                metadata_result = self.client.query(query).result()
                metadata = list(metadata_result)[0]
                
                validation_results[table_name] = {
                    "exists": True,
                    "row_count": row_count,
                    "unique_records": metadata.unique_records,
                    "min_ingested_at": metadata.min_ingested_at,
                    "max_ingested_at": metadata.max_ingested_at,
                    "schema_fields": len(table.schema)
                }
                
            except NotFound:
                validation_results[table_name] = {
                    "exists": False,
                    "error": "Table not found"
                }
            except Exception as e:
                validation_results[table_name] = {
                    "exists": True,
                    "error": str(e)
                }
        
        logger.info("Completed ingestion validation", results=validation_results)
        return validation_results


def main():
    """Main function to run the ingestion process."""
    ingestion = StripeDataIngestion()
    
    try:
        # Run ingestion
        stats = ingestion.ingest_stripe_data()
        
        # Validate ingestion
        validation = ingestion.validate_ingestion()
        
        # Print summary
        print("\n" + "="*50)
        print("INGESTION SUMMARY")
        print("="*50)
        
        for table_name, count in stats.items():
            status = "✅ SUCCESS" if count >= 0 else "❌ FAILED"
            print(f"{table_name}: {count} rows {status}")
        
        print("\n" + "="*50)
        print("VALIDATION SUMMARY")
        print("="*50)
        
        for table_name, result in validation.items():
            if result.get("exists", False) and "error" not in result:
                print(f"{table_name}: {result['row_count']} rows, {result['unique_records']} unique")
            else:
                print(f"{table_name}: ❌ {result.get('error', 'Unknown error')}")
        
    except Exception as e:
        logger.error("Ingestion failed", error=str(e))
        raise


if __name__ == "__main__":
    main() 