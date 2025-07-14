"""
Main orchestration file for Stripe data generation.
Coordinates all generators and provides validation and output functionality.
"""

import os
import random
import datetime
from typing import Dict, List, Any, Tuple
import argparse
import time

# Set random seed for reproducibility
from config import (
    RANDOM_SEED, OUTPUT_DIRECTORY, VALIDATION_THRESHOLDS,
    STRIPE_API_SECRET_KEY, STRIPE_RATE_LIMIT_REQUESTS_PER_SECOND,
    STRIPE_MAX_RETRIES, STRIPE_RETRY_DELAY, PRODUCTS
)
random.seed(RANDOM_SEED)

from product_price_generator import ProductPriceGenerator
from customer_generator import CustomerGenerator
from payment_method_generator import PaymentMethodGenerator
from subscription_generator import SubscriptionGenerator
from invoice_generator import InvoiceGenerator
from refund_dispute_generator import RefundDisputeGenerator
from invoice_item_generator import InvoiceItemGenerator
from credit_note_generator import CreditNoteGenerator
from tax_id_generator import TaxIdGenerator

from utils import (
    save_json, ensure_directory_exists, calculate_summary_stats,
    print_validation_summary, ProgressTracker, APISimulator, datetime_to_timestamp
)

class StripeDataGenerator:
    """Main orchestrator for generating all Stripe data with API simulation."""
    
    def __init__(self, 
                 simulate_api_requests: bool = True,
                 enable_rate_limiting: bool = True,
                 enable_random_errors: bool = False,
                 error_rate: float = 0.01,
                 use_real_stripe_api: bool = False):
        """
        Initialize the data generator with API simulation options.
        
        Args:
            simulate_api_requests: Whether to simulate API request behavior
            enable_rate_limiting: Whether to simulate rate limiting (requires simulate_api_requests=True)
            enable_random_errors: Whether to simulate random API errors
            error_rate: Probability of random errors (0.0 - 1.0)
            use_real_stripe_api: Whether to make real Stripe API calls
        """
        self.simulate_api_requests = simulate_api_requests
        self.use_real_stripe_api = use_real_stripe_api
        self.api_simulator = None
        
        if simulate_api_requests:
            # Calculate delay based on rate limit
            delay_between_requests = 1.0 / STRIPE_RATE_LIMIT_REQUESTS_PER_SECOND if enable_rate_limiting else 0.0
            
            self.api_simulator = APISimulator(
                enable_rate_limiting=enable_rate_limiting,
                enable_random_errors=enable_random_errors,
                error_rate=error_rate,
                delay_between_requests=delay_between_requests,
                use_real_api=use_real_stripe_api,
                stripe_api_key=STRIPE_API_SECRET_KEY if use_real_stripe_api else None
            )
        
        # Initialize generators
        self.product_price_generator = ProductPriceGenerator()
        self.customer_generator = CustomerGenerator()
        self.payment_method_generator = PaymentMethodGenerator()
        self.subscription_generator = None  # Initialized later with dependencies
        self.invoice_generator = None
        self.refund_dispute_generator = None
        self.invoice_item_generator = InvoiceItemGenerator()
        self.credit_note_generator = CreditNoteGenerator()
        self.tax_id_generator = TaxIdGenerator()
        
        # Initialize data storage
        self.generated_data = {}
        self.api_stats = {}
        self.generation_summary = {}
        self.validation_metrics = {}
    
    def _simulate_api_request(self, endpoint: str, method: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulate an API request if API simulation is enabled.
        
        Args:
            endpoint: API endpoint
            method: HTTP method
            payload: Request payload
            
        Returns:
            Dictionary with 'success' boolean and 'data' from API response
        """
        if not self.simulate_api_requests or not self.api_simulator:
            return {"success": True, "data": payload}
        
        response = self.api_simulator.simulate_request(endpoint, method, payload)
        return {
            "success": response.status_code < 400,
            "data": response.data if response.data else payload
        }
    
    def generate_all_data(self) -> Dict[str, Any]:
        """Generate all Stripe data following the proper sequence with API simulation."""
        print("🚀 Starting Stripe data generation...")
        
        # Print configuration
        if self.simulate_api_requests:
            api_mode = "Real Stripe API" if self.use_real_stripe_api else "Simulated API"
            print(f"📡 {api_mode} mode enabled - requests will be rate limited and may fail")
            if self.use_real_stripe_api:
                if STRIPE_API_SECRET_KEY:
                    print("✅ Stripe API key found in environment")
                else:
                    print("❌ ERROR: STRIPE_API_SECRET_KEY not found in environment")
                    print("   Please set this in your .env file for real API calls")
                    return {}
        else:
            print("⚡ Fast mode - no API simulation")
        
        print("=" * 60)
        
        # Step 1: Generate products and prices with API simulation
        print("\n📦 Step 1: Generating products and prices...")
        products_prices = self._generate_products_and_prices_with_api_sim()
        self.generated_data.update(products_prices)
        
        # Step 2: Generate customers with API simulation
        print("\n👥 Step 2: Generating customers...")
        customers = self._generate_customers_with_api_sim()
        self.generated_data["customers"] = customers
        
        # Step 3: Generate payment methods with API simulation
        print("\n💳 Step 3: Generating payment methods...")
        payment_methods = self._generate_payment_methods_with_api_sim(customers)
        self.generated_data["payment_methods"] = payment_methods
        
        # Step 4: Generate subscriptions with API simulation
        print("\n🔄 Step 4: Generating subscriptions...")
        self.subscription_generator = SubscriptionGenerator(
            self.product_price_generator, 
            self.payment_method_generator
        )
        subscriptions, subscription_events = self._generate_subscriptions_with_api_sim(customers)
        self.generated_data["subscriptions"] = subscriptions
        self.generated_data["subscription_events"] = subscription_events
        
        # Step 5: Generate invoices and payments with API simulation
        print("\n🧾 Step 5: Generating invoices and payments...")
        self.invoice_generator = InvoiceGenerator(
            self.product_price_generator,
            self.payment_method_generator
        )
        invoice_data = self._generate_invoices_with_api_sim(subscription_events)
        self.generated_data.update(invoice_data)
        
        # Step 6: Generate refunds and disputes with API simulation
        print("\n💸 Step 6: Generating refunds and disputes...")
        self.refund_dispute_generator = RefundDisputeGenerator()
        refund_dispute_data = self._generate_refunds_disputes_with_api_sim()
        self.generated_data.update(refund_dispute_data)
        
        # Step 7: Generate invoice items with API simulation
        print("\n📋 Step 7: Generating invoice items...")
        invoice_items = self._generate_invoice_items_with_api_sim()
        self.generated_data["invoice_items"] = invoice_items
        
        # Step 8: Generate credit notes with API simulation
        print("\n📝 Step 8: Generating credit notes...")
        credit_notes = self._generate_credit_notes_with_api_sim()
        self.generated_data["credit_notes"] = credit_notes
        
        # Step 9: Generate tax IDs with API simulation
        print("\n🏛️ Step 9: Generating tax IDs...")
        tax_ids = self._generate_tax_ids_with_api_sim()
        self.generated_data["tax_ids"] = tax_ids
        
        # Step 10: Collect API statistics
        if self.simulate_api_requests and self.api_simulator:
            print("\n📊 Step 10: Collecting API simulation statistics...")
            self.api_stats = self.api_simulator.get_stats()
            self.generation_summary = self.api_simulator.get_generation_summary()
            self._print_api_stats()
        
        # Step 11: Validate generated data
        print("\n✅ Step 11: Validating generated data...")
        self.validation_metrics = self._validate_generated_data()
        
        # Step 12: Save all data
        print("\n💾 Step 12: Saving generated data...")
        self._save_all_data()
        
        print("\n🎉 Data generation complete!")
        print("=" * 60)
        
        return self.generated_data
    
    def _generate_products_and_prices_with_api_sim(self) -> Dict[str, List[Dict[str, Any]]]:
        """Generate products and prices with API simulation."""
        products_prices = self.product_price_generator.generate_all()
        
        if not self.simulate_api_requests:
            return products_prices
        
        # Simulate API requests for products and update with real IDs
        print("  📡 Simulating product creation API requests...")
        failed_products = []
        successful_products = []
        
        for product in products_prices["products"]:
            response = self._simulate_api_request("/v1/products", "POST", product)
            if response["success"]:
                # Update the product with the real ID returned by Stripe
                real_product = response["data"]
                original_id = product["id"]
                
                # Update the product_price_generator's internal mapping
                for key, config in PRODUCTS.items():
                    if config["id"] == original_id:
                        self.product_price_generator.product_id_map[key] = real_product["id"]
                        break
                
                successful_products.append(real_product)
            else:
                failed_products.append(product["id"])
        
        # Update the products list with successful ones
        products_prices["products"] = successful_products
        
        # Simulate API requests for prices using updated product IDs
        print("  📡 Simulating price creation API requests...")
        failed_prices = []
        successful_prices = []
        
        for price in products_prices["prices"]:
            # Update the price with the real product ID
            for key, real_product_id in self.product_price_generator.product_id_map.items():
                if PRODUCTS[key]["id"] == price["product"]:
                    price["product"] = real_product_id
                    break
            
            response = self._simulate_api_request("/v1/prices", "POST", price)
            if response["success"]:
                # Update the price with the real ID returned by Stripe
                real_price = response["data"]
                original_id = price["id"]
                
                # Update the product_price_generator's internal price mapping
                for key, price_id in self.product_price_generator.price_id_map.items():
                    if price_id == original_id:
                        self.product_price_generator.price_id_map[key] = real_price["id"]
                        break
                
                successful_prices.append(real_price)
            else:
                failed_prices.append(price["id"])
        
        # Update the prices list with successful ones
        products_prices["prices"] = successful_prices
        
        if failed_products or failed_prices:
            print(f"  ⚠️  Failed to create {len(failed_products)} products and {len(failed_prices)} prices")
        
        return products_prices
    
    def _generate_customers_with_api_sim(self) -> List[Dict[str, Any]]:
        """Generate customers with API simulation."""
        customers = self.customer_generator.generate_customers()
        
        if not self.simulate_api_requests:
            return customers
        
        print("  📡 Simulating customer creation API requests...")
        successful_customers = []
        failed_customers = []
        
        for customer in customers:
            response = self._simulate_api_request("/v1/customers", "POST", customer)
            if response["success"]:
                successful_customers.append(response["data"])
            else:
                failed_customers.append(customer["id"])
        
        if failed_customers:
            print(f"  ⚠️  Failed to create {len(failed_customers)} customers")
        
        return successful_customers
    
    def _generate_payment_methods_with_api_sim(self, customers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate payment methods with API simulation."""
        payment_methods = self.payment_method_generator.generate_payment_methods(customers)
        
        if not self.simulate_api_requests:
            return payment_methods
        
        print("  📡 Simulating payment method creation and attachment API requests...")
        successful_payment_methods = []
        failed_payment_methods = []
        
        for pm in payment_methods:
            # For real API calls, create PaymentMethods with test card numbers
            if self.use_real_stripe_api and pm.get("type") == "card":
                customer_id = pm["customer"]
                
                # Create payment method with test card number
                create_response = self._simulate_api_request("/v1/payment_methods", "POST", pm)
                if not create_response["success"]:
                    failed_payment_methods.append(pm["id"])
                    continue
                
                # Get the actual payment method ID from Stripe
                real_pm = create_response["data"]
                
                # Simulate payment method attachment to customer
                attach_response = self._simulate_api_request(
                    f"/v1/payment_methods/{real_pm['id']}/attach", 
                    "POST", 
                    {"customer": customer_id}
                )
                if attach_response["success"]:
                    # Update the payment method with customer info and real ID
                    real_pm["customer"] = customer_id
                    successful_payment_methods.append(real_pm)
                    
                    # Update the payment method generator's mapping with real ID
                    self.payment_method_generator.customer_payment_methods[customer_id] = real_pm["id"]
                else:
                    failed_payment_methods.append(pm["id"])
            else:
                # Use the original approach for simulation mode
                create_response = self._simulate_api_request("/v1/payment_methods", "POST", pm)
                if not create_response["success"]:
                    failed_payment_methods.append(pm["id"])
                    continue
                
                # Get the actual payment method ID from Stripe
                real_pm = create_response["data"]
                customer_id = pm["customer"]
                
                # Simulate payment method attachment to customer
                attach_response = self._simulate_api_request(
                    f"/v1/payment_methods/{real_pm['id']}/attach", 
                    "POST", 
                    {"customer": customer_id}
                )
                if attach_response["success"]:
                    # Update the payment method with customer info and real ID
                    real_pm["customer"] = customer_id
                    successful_payment_methods.append(real_pm)
                    
                    # Update the payment method generator's mapping with real ID
                    self.payment_method_generator.customer_payment_methods[customer_id] = real_pm["id"]
                else:
                    failed_payment_methods.append(pm["id"])
        
        if failed_payment_methods:
            print(f"  ⚠️  Failed to create/attach {len(failed_payment_methods)} payment methods")
        
        return successful_payment_methods
    
    def _generate_subscriptions_with_api_sim(self, customers: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """Generate subscriptions with API simulation."""
        subscriptions = self.subscription_generator.generate_subscriptions(customers)
        subscription_events = self.subscription_generator.subscription_events
        
        if not self.simulate_api_requests:
            return subscriptions, subscription_events
        
        print("  📡 Simulating subscription creation API requests...")
        successful_subscriptions = []
        failed_subscriptions = []
        
        for subscription in subscriptions:
            # Fix dates to be in the future for real API calls
            if self.use_real_stripe_api:
                current_time = datetime_to_timestamp(datetime.datetime.now())
                
                # Ensure trial_end is in the future
                if subscription.get("trial_end") and subscription["trial_end"] < current_time:
                    subscription["trial_end"] = current_time + (30 * 24 * 60 * 60)  # 30 days from now
                
                # Ensure billing_cycle_anchor is in the future
                if subscription.get("billing_cycle_anchor") and subscription["billing_cycle_anchor"] < current_time:
                    subscription["billing_cycle_anchor"] = current_time + (30 * 24 * 60 * 60)  # 30 days from now
                
                # Update current_period_end to be in the future
                if subscription.get("current_period_end") and subscription["current_period_end"] < current_time:
                    subscription["current_period_end"] = current_time + (30 * 24 * 60 * 60)  # 30 days from now
                
                # Update payment method ID to use the real test payment method ID
                customer_id = subscription.get("customer")
                if customer_id:
                    real_payment_method_id = self.payment_method_generator.get_payment_method_for_customer(customer_id)
                    if real_payment_method_id:
                        subscription["default_payment_method"] = real_payment_method_id
            
            response = self._simulate_api_request("/v1/subscriptions", "POST", subscription)
            if response["success"]:
                successful_subscriptions.append(response["data"])
            else:
                failed_subscriptions.append(subscription["id"])
        
        if failed_subscriptions:
            print(f"  ⚠️  Failed to create {len(failed_subscriptions)} subscriptions")
        
        return successful_subscriptions, subscription_events
    
    def _generate_invoices_with_api_sim(self, subscription_events: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """Generate invoices with API simulation."""
        invoice_data = self.invoice_generator.generate_invoices_from_subscription_events(subscription_events)
        
        if not self.simulate_api_requests:
            return invoice_data
        
        print("  📡 Simulating invoice and payment API requests...")
        
        # Simulate invoice creation
        for invoice in invoice_data.get("invoices", []):
            response = self._simulate_api_request("/v1/invoices", "POST", invoice)
            if response["success"]:
                invoice["id"] = response["data"]["id"] # Update with real ID
        
        # Simulate charge creation
        for charge in invoice_data.get("charges", []):
            response = self._simulate_api_request("/v1/charges", "POST", charge)
            if response["success"]:
                charge["id"] = response["data"]["id"] # Update with real ID
        
        # Simulate payment intent creation
        for pi in invoice_data.get("payment_intents", []):
            response = self._simulate_api_request("/v1/payment_intents", "POST", pi)
            if response["success"]:
                pi["id"] = response["data"]["id"] # Update with real ID
        
        return invoice_data
    
    def _generate_refunds_disputes_with_api_sim(self) -> Dict[str, List[Dict[str, Any]]]:
        """Generate refunds and disputes with API simulation."""
        refund_dispute_data = self.refund_dispute_generator.generate_refunds_and_disputes(
            self.generated_data["charges"], 
            self.generated_data["invoices"]
        )
        
        if not self.simulate_api_requests:
            return refund_dispute_data
        
        print("  📡 Simulating refund creation API requests...")
        
        # Simulate refund creation
        for refund in refund_dispute_data.get("refunds", []):
            response = self._simulate_api_request("/v1/refunds", "POST", refund)
            if response["success"]:
                refund["id"] = response["data"]["id"] # Update with real ID
        
        return refund_dispute_data
    
    def _generate_invoice_items_with_api_sim(self) -> List[Dict[str, Any]]:
        """Generate invoice items with API simulation."""
        invoices = self.generated_data.get("invoices", [])
        customers = self.generated_data.get("customers", [])
        
        invoice_items = self.invoice_item_generator.generate_invoice_items(invoices, customers)
        
        if not self.simulate_api_requests:
            return invoice_items
        
        print("  📡 Simulating invoice item creation API requests...")
        successful_items = []
        failed_items = []
        
        for item in invoice_items:
            response = self._simulate_api_request("/v1/invoice_items", "POST", item)
            if response["success"]:
                successful_items.append(response["data"])
            else:
                failed_items.append(item["id"])
        
        if failed_items:
            print(f"  ⚠️  Failed to create {len(failed_items)} invoice items")
        
        return successful_items
    
    def _generate_credit_notes_with_api_sim(self) -> List[Dict[str, Any]]:
        """Generate credit notes with API simulation."""
        invoices = self.generated_data.get("invoices", [])
        refunds = self.generated_data.get("refunds", [])
        
        credit_notes = self.credit_note_generator.generate_credit_notes(invoices, refunds)
        
        if not self.simulate_api_requests:
            return credit_notes
        
        print("  📡 Simulating credit note creation API requests...")
        successful_notes = []
        failed_notes = []
        
        for note in credit_notes:
            response = self._simulate_api_request("/v1/credit_notes", "POST", note)
            if response["success"]:
                successful_notes.append(response["data"])
            else:
                failed_notes.append(note["id"])
        
        if failed_notes:
            print(f"  ⚠️  Failed to create {len(failed_notes)} credit notes")
        
        return successful_notes
    
    def _generate_tax_ids_with_api_sim(self) -> List[Dict[str, Any]]:
        """Generate tax IDs with API simulation."""
        customers = self.generated_data.get("customers", [])
        
        tax_ids = self.tax_id_generator.generate_tax_ids(customers)
        
        if not self.simulate_api_requests:
            return tax_ids
        
        print("  📡 Simulating tax ID creation API requests...")
        successful_tax_ids = []
        failed_tax_ids = []
        
        for tax_id in tax_ids:
            response = self._simulate_api_request("/v1/tax_ids", "POST", tax_id)
            if response["success"]:
                successful_tax_ids.append(response["data"])
            else:
                failed_tax_ids.append(tax_id["id"])
        
        if failed_tax_ids:
            print(f"  ⚠️  Failed to create {len(failed_tax_ids)} tax IDs")
        
        return successful_tax_ids

    def _print_api_stats(self) -> None:
        """Print API simulation statistics."""
        if not self.api_stats:
            return
        
        print("\n📊 API Simulation Statistics:")
        print(f"  API Mode: {'Real Stripe API' if self.api_stats['using_real_api'] else 'Simulated'}")
        print(f"  Total requests: {self.api_stats['total_requests']}")
        print(f"  Successful requests: {self.api_stats['successful_requests']}")
        print(f"  Failed requests: {self.api_stats['failed_requests']}")
        print(f"  Retried requests: {self.api_stats['retried_requests']}")
        print(f"  Success rate: {self.api_stats['success_rate']:.2%}")
        print(f"  Error rate: {self.api_stats['error_rate']:.2%}")
        print(f"  Retry rate: {self.api_stats['retry_rate']:.2%}")
        print(f"  Average response time: {self.api_stats['avg_response_time_ms']:.1f}ms")
        print(f"  Requests per second: {self.api_stats['requests_per_second']:.2f}")
        
        # Show error breakdown
        if self.api_stats['error_breakdown']:
            print(f"\n🔍 Error Breakdown:")
            for error_type, count in self.api_stats['error_breakdown'].items():
                print(f"  {error_type}: {count}")
        
        # Show endpoint performance
        if self.api_stats['endpoint_stats']:
            print(f"\n⚡ Endpoint Performance:")
            for endpoint, stats in self.api_stats['endpoint_stats'].items():
                success_rate = stats['successful_requests'] / max(1, stats['total_requests'])
                print(f"  {endpoint}: {stats['total_requests']} requests, {success_rate:.1%} success, {stats['avg_response_time']:.1f}ms avg")
        
        # Show failed requests if any
        if self.api_simulator:
            failed_requests = self.api_simulator.get_failed_requests()
            if failed_requests:
                print(f"\n❌ Failed Requests ({len(failed_requests)}):")
                for i, (req, resp) in enumerate(failed_requests[:5]):  # Show first 5
                    error_type = resp.error.get('type', 'unknown') if resp.error else 'unknown'
                    print(f"  {i+1}. {req.method} {req.endpoint} - {resp.status_code} {error_type}")
                if len(failed_requests) > 5:
                    print(f"  ... and {len(failed_requests) - 5} more")

    def _validate_generated_data(self) -> Dict[str, Any]:
        """Validate the generated data against expected benchmarks."""
        metrics = {}
        
        # Basic counts
        metrics["data_counts"] = {
            "customers": len(self.generated_data["customers"]),
            "subscriptions": len(self.generated_data["subscriptions"]),
            "invoices": len(self.generated_data["invoices"]),
            "charges": len(self.generated_data["charges"]),
            "refunds": len(self.generated_data["refunds"]),
            "disputes": len(self.generated_data["disputes"]),
            "payment_methods": len(self.generated_data["payment_methods"]),
            "invoice_items": len(self.generated_data["invoice_items"]),
            "credit_notes": len(self.generated_data["credit_notes"]),
            "tax_ids": len(self.generated_data["tax_ids"])
        }
        
        # Trial conversion rate
        trial_events = [e for e in self.generated_data["subscription_events"] if e["type"] == "subscription_created"]
        conversion_events = [e for e in self.generated_data["subscription_events"] if e["type"] == "subscription_converted"]
        
        if trial_events:
            trial_conversion_rate = len(conversion_events) / len(trial_events)
            metrics["trial_conversion_rate"] = trial_conversion_rate
            
            # Validate against thresholds
            min_rate, max_rate = VALIDATION_THRESHOLDS["trial_conversion_rate"]
            metrics["trial_conversion_rate_valid"] = min_rate <= trial_conversion_rate <= max_rate
        
        # Churn analysis
        active_subscriptions = [s for s in self.generated_data["subscriptions"] if s["status"] == "active"]
        canceled_events = [e for e in self.generated_data["subscription_events"] if e["type"] == "subscription_canceled"]
        
        if active_subscriptions:
            # Approximate monthly churn rate
            total_subscription_months = 0
            for event in self.generated_data["subscription_events"]:
                if event["type"] == "subscription_renewed":
                    total_subscription_months += 1
            
            if total_subscription_months > 0:
                monthly_churn_rate = len(canceled_events) / total_subscription_months
                metrics["monthly_churn_rate"] = monthly_churn_rate
                
                # Validate against thresholds
                min_rate, max_rate = VALIDATION_THRESHOLDS["monthly_churn_rate"]
                metrics["monthly_churn_rate_valid"] = min_rate <= monthly_churn_rate <= max_rate
        
        # Payment success rate
        successful_charges = [c for c in self.generated_data["charges"] if c["status"] == "succeeded"]
        if self.generated_data["charges"]:
            payment_success_rate = len(successful_charges) / len(self.generated_data["charges"])
            metrics["payment_success_rate"] = payment_success_rate
        
        # Refund rate
        if successful_charges:
            refund_rate = len(self.generated_data["refunds"]) / len(successful_charges)
            metrics["refund_rate"] = refund_rate
            
            # Validate against thresholds
            min_rate, max_rate = VALIDATION_THRESHOLDS["refund_rate"]
            metrics["refund_rate_valid"] = min_rate <= refund_rate <= max_rate
        
        # Dispute rate
        if successful_charges:
            dispute_rate = len(self.generated_data["disputes"]) / len(successful_charges)
            metrics["dispute_rate"] = dispute_rate
            
            # Validate against thresholds
            min_rate, max_rate = VALIDATION_THRESHOLDS["dispute_rate"]
            metrics["dispute_rate_valid"] = min_rate <= dispute_rate <= max_rate
        
        # Geographic distribution
        region_counts = {}
        for customer in self.generated_data["customers"]:
            region = customer["metadata"]["region"]
            region_counts[region] = region_counts.get(region, 0) + 1
        
        total_customers = len(self.generated_data["customers"])
        metrics["geographic_distribution"] = {
            region: count / total_customers 
            for region, count in region_counts.items()
        }
        
        # Plan distribution
        plan_counts = {}
        for event in self.generated_data["subscription_events"]:
            if event["type"] == "subscription_created":
                plan = event["plan_key"]
                plan_counts[plan] = plan_counts.get(plan, 0) + 1
        
        total_subscriptions = sum(plan_counts.values())
        if total_subscriptions > 0:
            metrics["plan_distribution"] = {
                plan: count / total_subscriptions 
                for plan, count in plan_counts.items()
            }
        
        # Revenue metrics
        successful_invoices = [i for i in self.generated_data["invoices"] if i["paid"]]
        if successful_invoices:
            revenue_amounts = [i["total"] / 100 for i in successful_invoices]  # Convert to dollars
            metrics["revenue_stats"] = calculate_summary_stats(revenue_amounts)
        
        # Print validation summary
        print_validation_summary(metrics)
        
        return metrics
    
    def _save_all_data(self) -> None:
        """Save all generated data to files."""
        ensure_directory_exists(OUTPUT_DIRECTORY)
        
        # Define all data files to save
        data_files = {
            "customers": self.generated_data.get("customers", []),
            "products": self.generated_data.get("products", []),
            "prices": self.generated_data.get("prices", []),
            "payment_methods": self.generated_data.get("payment_methods", []),
            "subscriptions": self.generated_data.get("subscriptions", []),
            "subscription_events": self.generated_data.get("subscription_events", []),
            "invoices": self.generated_data.get("invoices", []),
            "invoice_items": self.generated_data.get("invoice_items", []),
            "charges": self.generated_data.get("charges", []),
            "payment_intents": self.generated_data.get("payment_intents", []),
            "balance_transactions": self.generated_data.get("balance_transactions", []),
            "refunds": self.generated_data.get("refunds", []),
            "disputes": self.generated_data.get("disputes", []),
            "credit_notes": self.generated_data.get("credit_notes", []),
            "tax_ids": self.generated_data.get("tax_ids", [])
        }
        
        # Save each data file
        for filename, data in data_files.items():
            filepath = os.path.join(OUTPUT_DIRECTORY, f"{filename}.json")
            save_json(data, filepath)
            print(f"  💾 Saved {len(data)} {filename} to {filepath}")
        
        # Save validation metrics
        metrics_filepath = os.path.join(OUTPUT_DIRECTORY, "validation_metrics.json")
        save_json(self.validation_metrics, metrics_filepath)
        
        # Save API statistics and detailed log
        if self.api_simulator:
            api_stats_filepath = os.path.join(OUTPUT_DIRECTORY, "api_statistics.json")
            save_json(self.api_stats, api_stats_filepath)
            
            # Save detailed request log
            detailed_log_filepath = os.path.join(OUTPUT_DIRECTORY, "api_request_log.json")
            self.api_simulator.save_detailed_log(detailed_log_filepath)
            
            # Save generation summary
            summary_filepath = os.path.join(OUTPUT_DIRECTORY, "generation_summary.json")
            save_json(self.generation_summary, summary_filepath)
        
        # Save basic generation summary
        summary = {
            "generation_date": datetime.datetime.now().isoformat(),
            "total_customers": len(self.generated_data["customers"]),
            "total_subscriptions": len(self.generated_data["subscriptions"]),
            "total_invoices": len(self.generated_data["invoices"]),
            "total_revenue": sum(i["total"] for i in self.generated_data["invoices"] if i["paid"]) / 100,
            "data_files": [f"{dt}.json" for dt in data_files.keys() if dt in self.generated_data],
            "validation_passed": self._check_validation_passed(),
            "api_mode": "real" if self.use_real_stripe_api else "simulated" if self.simulate_api_requests else "none"
        }
        
        basic_summary_filepath = os.path.join(OUTPUT_DIRECTORY, "basic_summary.json")
        save_json(summary, basic_summary_filepath)
        
        print(f"\n📁 Data saved to: {OUTPUT_DIRECTORY}")
        print(f"📊 Generated {len(self.generated_data)} data types")
        print(f"💰 Total revenue: ${summary['total_revenue']:,.2f}")
        
        # Print saved files
        print(f"\n📄 Files saved:")
        for data_type in data_files.keys():
            if data_type in self.generated_data:
                print(f"  - {data_type}.json ({len(self.generated_data[data_type])} records)")
        
        if self.api_simulator:
            print(f"  - api_statistics.json (performance metrics)")
            print(f"  - api_request_log.json (detailed request log)")
            print(f"  - generation_summary.json (comprehensive summary)")

    def _check_validation_passed(self) -> bool:
        """Check if all validation metrics passed."""
        validation_keys = [
            "trial_conversion_rate_valid",
            "monthly_churn_rate_valid", 
            "refund_rate_valid",
            "dispute_rate_valid"
        ]
        
        return all(
            self.validation_metrics.get(key, True) 
            for key in validation_keys
        )
    
    def get_summary_stats(self) -> Dict[str, Any]:
        """Get summary statistics about the generated data."""
        if not self.generated_data:
            return {}
        
        return {
            "customers": len(self.generated_data.get("customers", [])),
            "subscriptions": len(self.generated_data.get("subscriptions", [])),
            "invoices": len(self.generated_data.get("invoices", [])),
            "revenue": sum(i["total"] for i in self.generated_data.get("invoices", []) if i["paid"]) / 100,
            "refunds": len(self.generated_data.get("refunds", [])),
            "disputes": len(self.generated_data.get("disputes", [])),
            "validation_passed": self._check_validation_passed()
        }

def main():
    """
    Main function to generate Stripe data with configurable options.
    
    Usage examples:
    - Basic generation (no API simulation): python main.py --no-api-sim
    - With rate limiting: python main.py --rate-limit
    - With error simulation: python main.py --rate-limit --errors --error-rate 0.05
    - Fast mode (no delays): python main.py --no-rate-limit
    - Real Stripe API: python main.py --real-api --rate-limit
    """
    
    parser = argparse.ArgumentParser(description="Generate realistic Stripe data for analytics")
    parser.add_argument("--no-api-sim", action="store_true", 
                       help="Disable API simulation (fastest mode)")
    parser.add_argument("--rate-limit", action="store_true", default=True,
                       help="Enable rate limiting simulation (default: True)")
    parser.add_argument("--no-rate-limit", action="store_true",
                       help="Disable rate limiting (faster generation)")
    parser.add_argument("--errors", action="store_true", 
                       help="Enable random API error simulation")
    parser.add_argument("--error-rate", type=float, default=0.01,
                       help="Error rate for random API errors (default: 0.01)")
    parser.add_argument("--real-api", action="store_true",
                       help="Use real Stripe API (requires STRIPE_API_SECRET_KEY in .env)")
    parser.add_argument("--output-dir", type=str, default="output",
                       help="Output directory for generated data (default: output)")
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.real_api and args.no_api_sim:
        print("❌ ERROR: Cannot use --real-api with --no-api-sim")
        return
    
    if args.real_api and not STRIPE_API_SECRET_KEY:
        print("❌ ERROR: --real-api requires STRIPE_API_SECRET_KEY in .env file")
        print("   Please set your Stripe API key in the .env file")
        return
    
    # Configure API simulation options
    simulate_api = not args.no_api_sim
    enable_rate_limiting = args.rate_limit and not args.no_rate_limit
    enable_errors = args.errors
    error_rate = max(0.0, min(1.0, args.error_rate))  # Clamp between 0 and 1
    use_real_api = args.real_api
    
    print("🔧 Configuration:")
    print(f"  API Simulation: {'Enabled' if simulate_api else 'Disabled'}")
    if simulate_api:
        print(f"  API Mode: {'Real Stripe API' if use_real_api else 'Simulated'}")
        print(f"  Rate Limiting: {'Enabled' if enable_rate_limiting else 'Disabled'}")
        print(f"  Error Simulation: {'Enabled' if enable_errors else 'Disabled'}")
        if enable_errors:
            print(f"  Error Rate: {error_rate:.1%}")
        if use_real_api:
            print(f"  Stripe API Key: {'✅ Found' if STRIPE_API_SECRET_KEY else '❌ Missing'}")
    print(f"  Output Directory: {args.output_dir}")
    print()
    
    # Update output directory in config if specified
    if args.output_dir != "output":
        import config
        config.OUTPUT_DIRECTORY = args.output_dir
    
    # Initialize generator with configuration
    generator = StripeDataGenerator(
        simulate_api_requests=simulate_api,
        enable_rate_limiting=enable_rate_limiting,
        enable_random_errors=enable_errors,
        error_rate=error_rate,
        use_real_stripe_api=use_real_api
    )
    
    # Generate all data
    start_time = time.time()
    data = generator.generate_all_data()
    end_time = time.time()
    
    if not data:  # Generation failed
        return
    
    # Print final summary
    print(f"\n⏱️  Total generation time: {end_time - start_time:.2f} seconds")
    
    # Print API statistics if available
    if generator.api_stats:
        print(f"\n📊 Final API Statistics:")
        print(f"  Total API requests: {generator.api_stats['total_requests']}")
        print(f"  Success rate: {generator.api_stats['success_rate']:.2%}")
        print(f"  Average response time: {generator.api_stats['avg_response_time_ms']:.1f}ms")
        print(f"  Throughput: {generator.api_stats['requests_per_second']:.2f} req/sec")
        if generator.api_stats['failed_requests'] > 0:
            print(f"  Failed requests: {generator.api_stats['failed_requests']}")
        if generator.api_stats['using_real_api']:
            print(f"  🎯 Real Stripe API was used successfully!")
    
    # Print data summary
    print(f"\n📈 Generated Data Summary:")
    for object_type, objects in data.items():
        if isinstance(objects, list):
            print(f"  {object_type}: {len(objects)} objects")
    
    # Print next steps
    print(f"\n🚀 Next Steps:")
    print(f"  1. Review generated data in: {args.output_dir}/")
    print(f"  2. Check validation metrics: {args.output_dir}/validation_metrics.json")
    if generator.api_simulator:
        print(f"  3. Analyze API performance: {args.output_dir}/api_statistics.json")
        print(f"  4. Review detailed logs: {args.output_dir}/api_request_log.json")
    print(f"  5. Import data into your analytics platform")
    
    return data

if __name__ == "__main__":
    main() 