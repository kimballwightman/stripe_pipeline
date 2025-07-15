"""
Stripe Data Pipeline DAG
Orchestrates data generation, ingestion, and dbt transformation
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago
import os
import sys

# Add paths to sys.path for imports
sys.path.append('/opt/airflow/generate_stripe_data')
sys.path.append('/opt/airflow/ingestion')

# Default arguments for the DAG
default_args = {
    'owner': 'analytics_team',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG definition
dag = DAG(
    'stripe_data_pipeline',
    default_args=default_args,
    description='End-to-end Stripe data pipeline: generation → ingestion → dbt transformation',
    schedule_interval=timedelta(days=1),  # Run daily
    catchup=False,
    max_active_runs=1,
    tags=['stripe', 'analytics', 'dbt', 'data_pipeline'],
)

def generate_stripe_data(**context):
    """Generate Stripe data using the data generator."""
    from main import StripeDataGenerator
    
    # Get environment
    environment = os.getenv('ENVIRONMENT', 'development')
    
    # Initialize generator with appropriate settings
    generator = StripeDataGenerator(
        simulate_api_requests=True,
        enable_rate_limiting=True,
        enable_random_errors=False,
        error_rate=0.01,
        use_real_stripe_api=False
    )
    
    # Generate data
    data = generator.generate_all_data()
    
    # Log summary
    total_records = sum(len(v) if isinstance(v, list) else 1 for v in data.values())
    print(f"Generated {total_records} total records in {environment} environment")
    
    return data

def ingest_data_to_bigquery(**context):
    """Ingest generated data into BigQuery."""
    from ingestion import StripeDataIngestion
    
    # Initialize ingestion
    ingestion = StripeDataIngestion()
    
    # Run ingestion
    stats = ingestion.ingest_stripe_data()
    
    # Validate ingestion
    validation = ingestion.validate_ingestion()
    
    # Log results
    total_ingested = sum(count for count in stats.values() if count > 0)
    print(f"Successfully ingested {total_ingested} records")
    
    return {"ingestion_stats": stats, "validation": validation}

def validate_dbt_setup(**context):
    """Validate dbt setup before running transformations."""
    import subprocess
    
    # Check dbt version
    result = subprocess.run(['dbt', '--version'], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"dbt not available: {result.stderr}")
    
    print(f"dbt version: {result.stdout}")
    
    # Check dbt project
    result = subprocess.run(['dbt', 'debug'], 
                          cwd='/opt/airflow/dbt/stripe_analytics', 
                          capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"dbt debug failed: {result.stderr}")
    
    print("dbt setup validation passed")
    return True

# Task definitions
start_task = DummyOperator(
    task_id='start_pipeline',
    dag=dag,
)

generate_data_task = PythonOperator(
    task_id='generate_stripe_data',
    python_callable=generate_stripe_data,
    dag=dag,
)

ingest_data_task = PythonOperator(
    task_id='ingest_data_to_bigquery',
    python_callable=ingest_data_to_bigquery,
    dag=dag,
)

validate_dbt_task = PythonOperator(
    task_id='validate_dbt_setup',
    python_callable=validate_dbt_setup,
    dag=dag,
)

# dbt tasks
dbt_deps_task = BashOperator(
    task_id='dbt_deps',
    bash_command='cd /opt/airflow/dbt/stripe_analytics && dbt deps',
    dag=dag,
)

dbt_run_staging_task = BashOperator(
    task_id='dbt_run_staging',
    bash_command='cd /opt/airflow/dbt/stripe_analytics && dbt run --select staging',
    dag=dag,
)

dbt_test_staging_task = BashOperator(
    task_id='dbt_test_staging',
    bash_command='cd /opt/airflow/dbt/stripe_analytics && dbt test --select staging',
    dag=dag,
)

dbt_run_dimensions_task = BashOperator(
    task_id='dbt_run_dimensions',
    bash_command='cd /opt/airflow/dbt/stripe_analytics && dbt run --select dimensions',
    dag=dag,
)

dbt_test_dimensions_task = BashOperator(
    task_id='dbt_test_dimensions',
    bash_command='cd /opt/airflow/dbt/stripe_analytics && dbt test --select dimensions',
    dag=dag,
)

dbt_run_facts_task = BashOperator(
    task_id='dbt_run_facts',
    bash_command='cd /opt/airflow/dbt/stripe_analytics && dbt run --select facts',
    dag=dag,
)

dbt_test_facts_task = BashOperator(
    task_id='dbt_test_facts',
    bash_command='cd /opt/airflow/dbt/stripe_analytics && dbt test --select facts',
    dag=dag,
)

dbt_run_marts_task = BashOperator(
    task_id='dbt_run_marts',
    bash_command='cd /opt/airflow/dbt/stripe_analytics && dbt run --select marts',
    dag=dag,
)

dbt_test_marts_task = BashOperator(
    task_id='dbt_test_marts',
    bash_command='cd /opt/airflow/dbt/stripe_analytics && dbt test --select marts',
    dag=dag,
)

dbt_generate_docs_task = BashOperator(
    task_id='dbt_generate_docs',
    bash_command='cd /opt/airflow/dbt/stripe_analytics && dbt docs generate',
    dag=dag,
)

end_task = DummyOperator(
    task_id='end_pipeline',
    dag=dag,
)

# Task dependencies
start_task >> generate_data_task >> ingest_data_task >> validate_dbt_task >> dbt_deps_task

# dbt staging layer
dbt_deps_task >> dbt_run_staging_task >> dbt_test_staging_task

# dbt dimensions layer
dbt_test_staging_task >> dbt_run_dimensions_task >> dbt_test_dimensions_task

# dbt facts layer
dbt_test_dimensions_task >> dbt_run_facts_task >> dbt_test_facts_task

# dbt marts layer
dbt_test_facts_task >> dbt_run_marts_task >> dbt_test_marts_task

# Generate docs and end
dbt_test_marts_task >> dbt_generate_docs_task >> end_task 