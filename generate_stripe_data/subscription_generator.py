"""
Subscription Generator for Stripe data generation.
Handles complete subscription lifecycle including trials, conversions, and churn.
"""

import datetime
import random
from typing import Dict, List, Any, Optional, Tuple
from config import (
    FREE_TRIAL_DAYS, TRIAL_START_RATE, PLAN_PREFERENCE, 
    BILLING_INTERVAL_PREFERENCE, SIMULATION_END_DATE,
    get_trial_conversion_rate, get_churn_rate
)
from utils import (
    generate_subscription_id, add_months, get_next_billing_date,
    datetime_to_timestamp, weighted_choice, bernoulli_trial, 
    ProgressTracker
)

class SubscriptionGenerator:
    """Generates realistic Stripe subscription data with lifecycle management."""
    
    def __init__(self, product_price_generator, payment_method_generator):
        self.product_price_generator = product_price_generator
        self.payment_method_generator = payment_method_generator
        self.subscriptions = []
        self.customer_subscriptions = {}  # Map customer_id to subscription data
        self.subscription_events = []  # Track subscription lifecycle events
    
    def generate_subscriptions(self, customers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate subscription lifecycle for all customers."""
        print(f"Generating subscriptions for {len(customers)} customers...")
        
        progress = ProgressTracker(len(customers), "Generating subscriptions")
        
        for customer in customers:
            customer_id = customer["id"]
            customer_metadata = {
                "region": customer["metadata"]["region"],
                "country": customer["metadata"]["country"],
                "signup_date": datetime.date.fromisoformat(customer["metadata"]["signup_date"])
            }
            
            # Generate subscription lifecycle for this customer
            subscription_data = self._generate_customer_subscription_lifecycle(
                customer_id, customer_metadata
            )
            
            if subscription_data:
                self.subscriptions.extend(subscription_data["subscriptions"])
                self.subscription_events.extend(subscription_data["events"])
                self.customer_subscriptions[customer_id] = subscription_data
            
            progress.update()
        
        progress.finish()
        return self.subscriptions
    
    def _generate_customer_subscription_lifecycle(self, customer_id: str, 
                                                 customer_metadata: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Generate the complete subscription lifecycle for a customer."""
        region = customer_metadata["region"]
        signup_date = customer_metadata["signup_date"]
        
        # Determine if customer starts a trial
        if not bernoulli_trial(TRIAL_START_RATE):
            return None  # Customer doesn't start trial
        
        # Choose plan and billing interval
        plan_key = self._choose_plan(region)
        billing_interval = self._choose_billing_interval()
        
        # Get payment method
        payment_method_id = self.payment_method_generator.get_payment_method_for_customer(customer_id)
        if not payment_method_id:
            return None  # No payment method available
        
        # Generate subscription lifecycle
        subscriptions = []
        events = []
        
        # Create trial subscription
        trial_start_date = signup_date + datetime.timedelta(days=random.randint(0, 7))  # Start trial within a week
        trial_subscription, trial_events = self._create_trial_subscription(
            customer_id, plan_key, billing_interval, payment_method_id, trial_start_date
        )
        
        subscriptions.append(trial_subscription)
        events.extend(trial_events)
        
        # Determine trial outcome
        conversion_rate = get_trial_conversion_rate(region)
        if bernoulli_trial(conversion_rate):
            # Convert to paid subscription
            paid_subscription, paid_events = self._convert_to_paid_subscription(
                trial_subscription, customer_metadata
            )
            subscriptions.append(paid_subscription)
            events.extend(paid_events)
            
            # Simulate ongoing subscription lifecycle (renewals, potential churn)
            ongoing_events = self._simulate_ongoing_subscription_lifecycle(
                paid_subscription, customer_metadata
            )
            events.extend(ongoing_events)
        else:
            # Trial expires without conversion
            trial_end_event = self._create_trial_end_event(trial_subscription)
            events.append(trial_end_event)
        
        return {
            "subscriptions": subscriptions,
            "events": events,
            "customer_id": customer_id,
            "plan_key": plan_key,
            "billing_interval": billing_interval
        }
    
    def _choose_plan(self, region: str) -> str:
        """Choose a plan based on regional preferences."""
        preferences = PLAN_PREFERENCE[region]
        plans = list(preferences.keys())
        weights = list(preferences.values())
        return weighted_choice(plans, weights)
    
    def _choose_billing_interval(self) -> str:
        """Choose billing interval based on preferences."""
        intervals = list(BILLING_INTERVAL_PREFERENCE.keys())
        weights = list(BILLING_INTERVAL_PREFERENCE.values())
        return weighted_choice(intervals, weights)
    
    def _create_trial_subscription(self, customer_id: str, plan_key: str, 
                                  billing_interval: str, payment_method_id: str,
                                  trial_start_date: datetime.date) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
        """Create a trial subscription."""
        subscription_id = generate_subscription_id()
        price_id = self.product_price_generator.get_price_id(plan_key, billing_interval)
        
        trial_end_date = trial_start_date + datetime.timedelta(days=FREE_TRIAL_DAYS)
        current_period_end = get_next_billing_date(trial_end_date, billing_interval)
        
        subscription = {
            "id": subscription_id,
            "object": "subscription",
            "application": None,
            "application_fee_percent": None,
            "automatic_tax": {
                "enabled": False,
                "liability": None
            },
            "billing_cycle_anchor": datetime_to_timestamp(
                datetime.datetime.combine(trial_end_date, datetime.time(0, 0))
            ),
            "billing_cycle_anchor_config": None,
            "billing_mode": {
                "type": "legacy",
                "updated_at": None
            },
            "billing_thresholds": None,
            "cancel_at": None,
            "cancel_at_period_end": False,
            "canceled_at": None,
            "cancellation_details": {
                "comment": None,
                "feedback": None,
                "reason": None
            },
            "collection_method": "charge_automatically",
            "created": datetime_to_timestamp(
                datetime.datetime.combine(trial_start_date, datetime.time(
                    random.randint(9, 17), random.randint(0, 59)
                ))
            ),
            "currency": "usd",
            "current_period_end": datetime_to_timestamp(
                datetime.datetime.combine(current_period_end, datetime.time(23, 59))
            ),
            "current_period_start": datetime_to_timestamp(
                datetime.datetime.combine(trial_start_date, datetime.time(0, 0))
            ),
            "customer": customer_id,
            "default_payment_method": payment_method_id,
            "default_source": None,
            "default_tax_rates": [],
            "description": None,
            "discounts": [],
            "ended_at": None,
            "invoice_settings": {
                "account_tax_ids": None,
                "issuer": {
                    "type": "self"
                }
            },
            "items": {
                "object": "list",
                "data": [{
                    "id": f"si_{subscription_id[4:]}",
                    "object": "subscription_item",
                    "billing_thresholds": None,
                    "created": datetime_to_timestamp(
                        datetime.datetime.combine(trial_start_date, datetime.time(
                            random.randint(9, 17), random.randint(0, 59)
                        ))
                    ),
                    "current_period_end": datetime_to_timestamp(
                        datetime.datetime.combine(current_period_end, datetime.time(23, 59))
                    ),
                    "current_period_start": datetime_to_timestamp(
                        datetime.datetime.combine(trial_start_date, datetime.time(0, 0))
                    ),
                    "discounts": [],
                    "metadata": {},
                    "price": {
                        "id": price_id,
                        "object": "price",
                        "active": True,
                        "billing_scheme": "per_unit",
                        "created": datetime_to_timestamp(datetime.datetime(2019, 12, 1)),
                        "currency": "usd",
                        "custom_unit_amount": None,
                        "livemode": False,
                        "lookup_key": f"{plan_key}_{billing_interval}ly",
                        "metadata": {"plan_type": plan_key, "billing_interval": billing_interval},
                        "nickname": f"{plan_key.title()} Plan - {billing_interval.title()}ly",
                        "product": self.product_price_generator.get_product_id(plan_key),
                        "recurring": {
                            "interval": billing_interval,
                            "interval_count": 1,
                            "meter": None,
                            "usage_type": "licensed"
                        },
                        "tax_behavior": "unspecified",
                        "tiers": None,
                        "tiers_mode": None,
                        "transform_quantity": None,
                        "type": "recurring",
                        "unit_amount": self.product_price_generator.get_price_amount(plan_key, billing_interval),
                        "unit_amount_decimal": str(self.product_price_generator.get_price_amount(plan_key, billing_interval))
                    },
                    "quantity": 1,
                    "subscription": subscription_id,
                    "tax_rates": []
                }],
                "has_more": False,
                "total_count": 1,
                "url": f"/v1/subscription_items?subscription={subscription_id}"
            },
            "latest_invoice": None,
            "livemode": False,
            "metadata": {
                "plan_type": plan_key,
                "billing_interval": billing_interval,
                "trial_start_date": trial_start_date.isoformat()
            },
            "next_pending_invoice_item_invoice": None,
            "on_behalf_of": None,
            "pause_collection": None,
            "payment_settings": {
                "payment_method_options": None,
                "payment_method_types": None,
                "save_default_payment_method": "off"
            },
            "pending_invoice_item_interval": None,
            "pending_setup_intent": None,
            "pending_update": None,
            "schedule": None,
            "start_date": datetime_to_timestamp(
                datetime.datetime.combine(trial_start_date, datetime.time(0, 0))
            ),
            "status": "trialing",
            "test_clock": None,
            "transfer_data": None,
            "trial_end": datetime_to_timestamp(
                datetime.datetime.combine(trial_end_date, datetime.time(23, 59))
            ),
            "trial_settings": {
                "end_behavior": {
                    "missing_payment_method": "create_invoice"
                }
            },
            "trial_start": datetime_to_timestamp(
                datetime.datetime.combine(trial_start_date, datetime.time(0, 0))
            )
        }
        
        # Create subscription creation event
        events = [{
            "type": "subscription_created",
            "subscription_id": subscription_id,
            "customer_id": customer_id,
            "timestamp": subscription["created"],
            "status": "trialing",
            "plan_key": plan_key,
            "billing_interval": billing_interval,
            "trial_start": trial_start_date.isoformat(),
            "trial_end": trial_end_date.isoformat()
        }]
        
        return subscription, events
    
    def _convert_to_paid_subscription(self, trial_subscription: Dict[str, Any],
                                     customer_metadata: Dict[str, Any]) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
        """Convert trial subscription to paid subscription."""
        # Get trial end date from the trial_end timestamp
        trial_end_timestamp = trial_subscription["trial_end"]
        trial_end_date = datetime.date.fromtimestamp(trial_end_timestamp)
        
        # Create paid subscription (copy trial and modify)
        paid_subscription = trial_subscription.copy()
        paid_subscription["status"] = "active"
        paid_subscription["trial_end"] = None
        paid_subscription["trial_start"] = None
        paid_subscription["trial_settings"] = None
        
        # Update current period
        billing_interval = trial_subscription["metadata"]["billing_interval"]
        current_period_start = trial_end_date
        current_period_end = get_next_billing_date(current_period_start, billing_interval)
        
        paid_subscription["current_period_start"] = datetime_to_timestamp(
            datetime.datetime.combine(current_period_start, datetime.time(0, 0))
        )
        paid_subscription["current_period_end"] = datetime_to_timestamp(
            datetime.datetime.combine(current_period_end, datetime.time(23, 59))
        )
        
        # Create conversion event
        events = [{
            "type": "subscription_converted",
            "subscription_id": trial_subscription["id"],
            "customer_id": trial_subscription["customer"],
            "timestamp": datetime_to_timestamp(
                datetime.datetime.combine(trial_end_date, datetime.time(0, 0))
            ),
            "status": "active",
            "plan_key": trial_subscription["metadata"]["plan_type"],
            "billing_interval": billing_interval,
            "conversion_date": trial_end_date.isoformat()
        }]
        
        return paid_subscription, events
    
    def _create_trial_end_event(self, trial_subscription: Dict[str, Any]) -> Dict[str, Any]:
        """Create event for trial ending without conversion."""
        # Get trial end date from the trial_end timestamp
        trial_end_timestamp = trial_subscription["trial_end"]
        trial_end_date = datetime.date.fromtimestamp(trial_end_timestamp)
        
        return {
            "type": "subscription_trial_ended",
            "subscription_id": trial_subscription["id"],
            "customer_id": trial_subscription["customer"],
            "timestamp": datetime_to_timestamp(
                datetime.datetime.combine(trial_end_date, datetime.time(23, 59))
            ),
            "status": "canceled",
            "plan_key": trial_subscription["metadata"]["plan_type"],
            "billing_interval": trial_subscription["metadata"]["billing_interval"],
            "trial_end_date": trial_end_date.isoformat()
        }
    
    def _simulate_ongoing_subscription_lifecycle(self, subscription: Dict[str, Any],
                                               customer_metadata: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Simulate ongoing subscription lifecycle with renewals and potential churn."""
        events = []
        region = customer_metadata["region"]
        plan_key = subscription["metadata"]["plan_type"]
        billing_interval = subscription["metadata"]["billing_interval"]
        
        # Get churn rate and payment method multiplier
        base_churn_rate = get_churn_rate(plan_key, region)
        payment_method_id = subscription["default_payment_method"]
        churn_multiplier = self.payment_method_generator.get_churn_multiplier(payment_method_id)
        monthly_churn_rate = base_churn_rate * churn_multiplier
        
        # Simulate billing cycles until churn or end of simulation
        current_period_start = datetime.datetime.fromtimestamp(subscription["current_period_start"]).date()
        current_subscription = subscription.copy()
        
        while current_period_start < SIMULATION_END_DATE:
            # Calculate next billing date
            next_billing_date = get_next_billing_date(current_period_start, billing_interval)
            
            if next_billing_date > SIMULATION_END_DATE:
                break
            
            # Check for churn (adjust probability based on billing interval)
            if billing_interval == "month":
                churn_probability = monthly_churn_rate
            else:  # yearly
                churn_probability = 1 - (1 - monthly_churn_rate) ** 12
            
            if bernoulli_trial(churn_probability):
                # Customer churns
                churn_event = {
                    "type": "subscription_canceled",
                    "subscription_id": subscription["id"],
                    "customer_id": subscription["customer"],
                    "timestamp": datetime_to_timestamp(
                        datetime.datetime.combine(next_billing_date, datetime.time(
                            random.randint(9, 17), random.randint(0, 59)
                        ))
                    ),
                    "status": "canceled",
                    "plan_key": plan_key,
                    "billing_interval": billing_interval,
                    "churn_date": next_billing_date.isoformat(),
                    "churn_reason": self._get_churn_reason()
                }
                events.append(churn_event)
                break
            else:
                # Successful renewal
                renewal_event = {
                    "type": "subscription_renewed",
                    "subscription_id": subscription["id"],
                    "customer_id": subscription["customer"],
                    "timestamp": datetime_to_timestamp(
                        datetime.datetime.combine(next_billing_date, datetime.time(
                            random.randint(0, 5), random.randint(0, 59)
                        ))
                    ),
                    "status": "active",
                    "plan_key": plan_key,
                    "billing_interval": billing_interval,
                    "renewal_date": next_billing_date.isoformat(),
                    "amount": self.product_price_generator.get_price_amount(plan_key, billing_interval)
                }
                events.append(renewal_event)
                
                # Update current period
                current_period_start = next_billing_date
        
        return events
    
    def _get_churn_reason(self) -> str:
        """Get a realistic churn reason."""
        reasons = [
            "payment_failed",
            "customer_request",
            "feature_insufficient",
            "price_too_high",
            "competitor_switch",
            "business_closed",
            "seasonal_pause"
        ]
        weights = [0.3, 0.25, 0.15, 0.12, 0.08, 0.05, 0.05]
        return weighted_choice(reasons, weights)
    
    def get_subscription_for_customer(self, customer_id: str) -> Optional[Dict[str, Any]]:
        """Get subscription data for a customer."""
        return self.customer_subscriptions.get(customer_id)
    
    def get_active_subscriptions_at_date(self, date: datetime.date) -> List[Dict[str, Any]]:
        """Get all subscriptions that were active on a specific date."""
        active_subscriptions = []
        target_timestamp = datetime_to_timestamp(datetime.datetime.combine(date, datetime.time(12, 0)))
        
        for subscription in self.subscriptions:
            start_time = subscription["start_date"]
            
            # Check if subscription was active on the target date
            if start_time <= target_timestamp:
                # Check if it wasn't canceled before the target date
                canceled_event = next(
                    (event for event in self.subscription_events 
                     if event["subscription_id"] == subscription["id"] 
                     and event["type"] == "subscription_canceled" 
                     and event["timestamp"] <= target_timestamp),
                    None
                )
                
                if not canceled_event:
                    active_subscriptions.append(subscription)
        
        return active_subscriptions
    
    def get_subscription_events(self) -> List[Dict[str, Any]]:
        """Get all subscription lifecycle events."""
        return self.subscription_events

def main():
    """Test the subscription generator."""
    # This would normally be called with real generators
    print("Subscription generator test would require product_price_generator and payment_method_generator")
    print("Run from main.py for full integration test")

if __name__ == "__main__":
    main() 