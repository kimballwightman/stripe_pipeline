"""
Invoice Generator for Stripe data generation.
Creates invoices, charges, and payment transactions based on subscription events.
"""

import datetime
import random
from typing import Dict, List, Any, Optional
from config import PAYMENT_FAILURE_RATES
from utils import (
    generate_invoice_id, generate_charge_id, generate_payment_intent_id,
    generate_balance_transaction_id, datetime_to_timestamp, 
    weighted_choice, bernoulli_trial, calculate_tax, ProgressTracker
)

class InvoiceGenerator:
    """Generates realistic Stripe invoice and payment data."""
    
    def __init__(self, product_price_generator, payment_method_generator):
        self.product_price_generator = product_price_generator
        self.payment_method_generator = payment_method_generator
        self.invoices = []
        self.charges = []
        self.payment_intents = []
        self.balance_transactions = []
        
    def generate_invoices_from_subscription_events(self, subscription_events: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """Generate invoices from subscription events."""
        print(f"Generating invoices from {len(subscription_events)} subscription events...")
        
        # Filter events that generate invoices
        invoice_events = [
            event for event in subscription_events 
            if event["type"] in ["subscription_converted", "subscription_renewed"]
        ]
        
        progress = ProgressTracker(len(invoice_events), "Generating invoices")
        
        for event in invoice_events:
            invoice_data = self._generate_invoice_from_event(event)
            
            if invoice_data:
                self.invoices.append(invoice_data["invoice"])
                if invoice_data["charge"]:
                    self.charges.append(invoice_data["charge"])
                if invoice_data["payment_intent"]:
                    self.payment_intents.append(invoice_data["payment_intent"])
                if invoice_data["balance_transaction"]:
                    self.balance_transactions.append(invoice_data["balance_transaction"])
            
            progress.update()
        
        progress.finish()
        
        return {
            "invoices": self.invoices,
            "charges": self.charges,
            "payment_intents": self.payment_intents,
            "balance_transactions": self.balance_transactions
        }
    
    def _generate_invoice_from_event(self, event: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Generate invoice data from a subscription event."""
        subscription_id = event["subscription_id"]
        customer_id = event["customer_id"]
        plan_key = event["plan_key"]
        billing_interval = event["billing_interval"]
        
        # Get pricing information
        price_amount = self.product_price_generator.get_price_amount(plan_key, billing_interval)
        price_id = self.product_price_generator.get_price_id(plan_key, billing_interval)
        
        # Calculate amounts
        subtotal = price_amount
        tax_amount = int(calculate_tax(subtotal / 100) * 100)  # Convert to cents
        total_amount = subtotal + tax_amount
        
        # Generate invoice
        invoice_id = generate_invoice_id()
        invoice_timestamp = event["timestamp"]
        
        # Determine payment status
        payment_method_id = self._get_payment_method_for_customer(customer_id)
        payment_success = self._determine_payment_success(payment_method_id)
        
        invoice = {
            "id": invoice_id,
            "object": "invoice",
            "account_country": "US",
            "account_name": "DataFlow Analytics",
            "account_tax_ids": None,
            "amount_due": total_amount if not payment_success else 0,
            "amount_paid": total_amount if payment_success else 0,
            "amount_remaining": 0 if payment_success else total_amount,
            "application": None,
            "application_fee_amount": None,
            "attempt_count": 1,
            "attempted": True,
            "auto_advance": True,
            "automatic_tax": {"enabled": False, "status": None},
            "billing_reason": "subscription_cycle" if event["type"] == "subscription_renewed" else "subscription_create",
            "charge": None,  # Will be set if payment successful
            "collection_method": "charge_automatically",
            "created": invoice_timestamp,
            "currency": "usd",
            "custom_fields": None,
            "customer": customer_id,
            "customer_address": None,
            "customer_email": None,
            "customer_name": None,
            "customer_phone": None,
            "customer_shipping": None,
            "customer_tax_exempt": "none",
            "customer_tax_ids": [],
            "default_payment_method": payment_method_id,
            "default_source": None,
            "default_tax_rates": [],
            "description": None,
            "discount": None,
            "discounts": [],
            "due_date": None,
            "ending_balance": 0,
            "footer": None,
            "hosted_invoice_url": f"https://invoice.stripe.com/i/acct_test/{invoice_id}",
            "invoice_pdf": f"https://pay.stripe.com/invoice/{invoice_id}/pdf",
            "last_finalization_error": None,
            "lines": {
                "object": "list",
                "data": [{
                    "id": f"il_{invoice_id[3:]}",
                    "object": "line_item",
                    "amount": subtotal,
                    "currency": "usd",
                    "description": f"{plan_key.title()} plan ({billing_interval}ly billing)",
                    "discount_amounts": [],
                    "discountable": True,
                    "discounts": [],
                    "livemode": False,
                    "metadata": {},
                    "period": {
                        "end": event["timestamp"] + (86400 * 30 if billing_interval == "month" else 86400 * 365),
                        "start": event["timestamp"]
                    },
                    "price": {
                        "id": price_id,
                        "object": "price",
                        "active": True,
                        "billing_scheme": "per_unit",
                        "created": datetime_to_timestamp(datetime.datetime(2019, 12, 1)),
                        "currency": "usd",
                        "livemode": False,
                        "lookup_key": f"{plan_key}_{billing_interval}ly",
                        "metadata": {"plan_type": plan_key, "billing_interval": billing_interval},
                        "nickname": f"{plan_key.title()} Plan - {billing_interval.title()}ly",
                        "product": self.product_price_generator.get_product_id(plan_key),
                        "recurring": {
                            "aggregate_usage": None,
                            "interval": billing_interval,
                            "interval_count": 1,
                            "trial_period_days": None,
                            "usage_type": "licensed"
                        },
                        "tax_behavior": "exclusive",
                        "tiers_mode": None,
                        "transform_quantity": None,
                        "type": "recurring",
                        "unit_amount": subtotal,
                        "unit_amount_decimal": str(subtotal)
                    },
                    "proration": False,
                    "proration_details": {"credited_items": None},
                    "quantity": 1,
                    "subscription": subscription_id,
                    "subscription_item": f"si_{subscription_id[4:]}",
                    "tax_amounts": [{
                        "amount": tax_amount,
                        "inclusive": False,
                        "tax_rate": "txr_sales_tax"
                    }] if tax_amount > 0 else [],
                    "tax_rates": [],
                    "type": "subscription"
                }],
                "has_more": False,
                "total_count": 1,
                "url": f"/v1/invoices/{invoice_id}/lines"
            },
            "livemode": False,
            "metadata": {
                "subscription_id": subscription_id,
                "plan_key": plan_key,
                "billing_interval": billing_interval
            },
            "next_payment_attempt": None if payment_success else invoice_timestamp + 86400,
            "number": self._generate_invoice_number(),
            "on_behalf_of": None,
            "paid": payment_success,
            "paid_out_of_band": False,
            "payment_intent": None,  # Will be set if payment attempted
            "payment_settings": {
                "payment_method_options": None,
                "payment_method_types": None
            },
            "period_end": event["timestamp"] + (86400 * 30 if billing_interval == "month" else 86400 * 365),
            "period_start": event["timestamp"],
            "post_payment_credit_notes_amount": 0,
            "pre_payment_credit_notes_amount": 0,
            "quote": None,
            "receipt_number": None,
            "starting_balance": 0,
            "statement_descriptor": None,
            "status": "paid" if payment_success else "open",
            "status_transitions": {
                "finalized_at": invoice_timestamp,
                "marked_uncollectible_at": None,
                "paid_at": invoice_timestamp if payment_success else None,
                "voided_at": None
            },
            "subscription": subscription_id,
            "subtotal": subtotal,
            "tax": tax_amount,
            "test_clock": None,
            "total": total_amount,
            "total_discount_amounts": [],
            "total_tax_amounts": [{
                "amount": tax_amount,
                "inclusive": False,
                "tax_rate": "txr_sales_tax"
            }] if tax_amount > 0 else [],
            "transfer_data": None,
            "webhooks_delivered_at": invoice_timestamp + random.randint(1, 10)
        }
        
        # Generate related objects if payment was attempted
        charge = None
        payment_intent = None
        balance_transaction = None
        
        if payment_success:
            # Generate successful payment objects
            charge_id = generate_charge_id()
            payment_intent_id = generate_payment_intent_id()
            balance_transaction_id = generate_balance_transaction_id()
            
            # Update invoice with charge reference
            invoice["charge"] = charge_id
            invoice["payment_intent"] = payment_intent_id
            
            # Create charge object
            charge = self._create_charge(
                charge_id, payment_intent_id, customer_id, total_amount, 
                invoice_timestamp, payment_method_id, True
            )
            
            # Create payment intent
            payment_intent = self._create_payment_intent(
                payment_intent_id, customer_id, total_amount, 
                invoice_timestamp, payment_method_id, True
            )
            
            # Create balance transaction
            balance_transaction = self._create_balance_transaction(
                balance_transaction_id, charge_id, total_amount, invoice_timestamp
            )
        
        return {
            "invoice": invoice,
            "charge": charge,
            "payment_intent": payment_intent,
            "balance_transaction": balance_transaction
        }
    
    def _get_payment_method_for_customer(self, customer_id: str) -> Optional[str]:
        """Get payment method ID for a customer."""
        return self.payment_method_generator.get_payment_method_for_customer(customer_id)
    
    def _determine_payment_success(self, payment_method_id: str) -> bool:
        """Determine if payment should succeed based on payment method failure rates."""
        if not payment_method_id:
            return False
        
        failure_rate = self.payment_method_generator.get_payment_method_failure_rate(payment_method_id)
        return not bernoulli_trial(failure_rate)
    
    def _generate_invoice_number(self) -> str:
        """Generate a realistic invoice number."""
        return f"DF-{random.randint(100000, 999999)}"
    
    def _create_charge(self, charge_id: str, payment_intent_id: str, customer_id: str,
                      amount: int, timestamp: int, payment_method_id: str, 
                      success: bool) -> Dict[str, Any]:
        """Create a charge object."""
        return {
            "id": charge_id,
            "object": "charge",
            "amount": amount,
            "amount_captured": amount if success else 0,
            "amount_refunded": 0,
            "application": None,
            "application_fee": None,
            "application_fee_amount": None,
            "balance_transaction": f"txn_{charge_id[3:]}",
            "billing_details": {
                "address": None,
                "email": None,
                "name": None,
                "phone": None
            },
            "calculated_statement_descriptor": "DATAFLOW ANALYTICS",
            "captured": success,
            "created": timestamp,
            "currency": "usd",
            "customer": customer_id,
            "description": "Subscription payment",
            "destination": None,
            "dispute": None,
            "disputed": False,
            "failure_code": None if success else self._get_failure_code(),
            "failure_message": None if success else self._get_failure_message(),
            "fraud_details": {},
            "invoice": None,  # Will be set by invoice
            "livemode": False,
            "metadata": {},
            "on_behalf_of": None,
            "outcome": {
                "network_status": "approved_by_network" if success else "declined_by_network",
                "reason": None if success else "generic_decline",
                "risk_level": "normal",
                "risk_score": random.randint(20, 40) if success else random.randint(60, 90),
                "seller_message": "Payment complete." if success else "Your card was declined.",
                "type": "authorized" if success else "issuer_declined"
            },
            "paid": success,
            "payment_intent": payment_intent_id,
            "payment_method": payment_method_id,
            "payment_method_details": self._get_payment_method_details(payment_method_id),
            "receipt_email": None,
            "receipt_number": None,
            "receipt_url": f"https://pay.stripe.com/receipts/{charge_id}" if success else None,
            "refunded": False,
            "refunds": {
                "object": "list",
                "data": [],
                "has_more": False,
                "total_count": 0,
                "url": f"/v1/charges/{charge_id}/refunds"
            },
            "review": None,
            "shipping": None,
            "source": None,
            "source_transfer": None,
            "statement_descriptor": None,
            "statement_descriptor_suffix": None,
            "status": "succeeded" if success else "failed",
            "transfer_data": None,
            "transfer_group": None
        }
    
    def _create_payment_intent(self, payment_intent_id: str, customer_id: str, amount: int,
                              timestamp: int, payment_method_id: str, success: bool) -> Dict[str, Any]:
        """Create a payment intent object."""
        return {
            "id": payment_intent_id,
            "object": "payment_intent",
            "amount": amount,
            "amount_capturable": 0,
            "amount_received": amount if success else 0,
            "application": None,
            "application_fee_amount": None,
            "automatic_payment_methods": None,
            "canceled_at": None,
            "cancellation_reason": None,
            "capture_method": "automatic",
            "charges": {
                "object": "list",
                "data": [],  # Would contain charge objects
                "has_more": False,
                "total_count": 1 if success else 0,
                "url": f"/v1/charges?payment_intent={payment_intent_id}"
            },
            "client_secret": f"{payment_intent_id}_secret_{random.randint(100000, 999999)}",
            "confirmation_method": "automatic",
            "created": timestamp,
            "currency": "usd",
            "customer": customer_id,
            "description": "Subscription payment",
            "invoice": None,  # Will be set by invoice
            "last_payment_error": None if success else {
                "charge": None,
                "code": "card_declined",
                "decline_code": "generic_decline",
                "doc_url": "https://stripe.com/docs/error-codes/card-declined",
                "message": "Your card was declined.",
                "payment_method": {
                    "id": payment_method_id,
                    "object": "payment_method"
                },
                "type": "card_error"
            },
            "livemode": False,
            "metadata": {},
            "next_action": None,
            "on_behalf_of": None,
            "payment_method": payment_method_id,
            "payment_method_options": {},
            "payment_method_types": ["card"],
            "processing": None,
            "receipt_email": None,
            "review": None,
            "setup_future_usage": None,
            "shipping": None,
            "source": None,
            "statement_descriptor": None,
            "statement_descriptor_suffix": None,
            "status": "succeeded" if success else "requires_payment_method",
            "transfer_data": None,
            "transfer_group": None
        }
    
    def _create_balance_transaction(self, transaction_id: str, charge_id: str, 
                                   amount: int, timestamp: int) -> Dict[str, Any]:
        """Create a balance transaction object."""
        # Calculate Stripe fees (2.9% + 30¢ for cards)
        fee_amount = int(amount * 0.029) + 30
        net_amount = amount - fee_amount
        
        return {
            "id": transaction_id,
            "object": "balance_transaction",
            "amount": net_amount,
            "available_on": timestamp + 86400 * 2,  # Available in 2 days
            "created": timestamp,
            "currency": "usd",
            "description": "Subscription payment",
            "exchange_rate": None,
            "fee": fee_amount,
            "fee_details": [{
                "amount": fee_amount,
                "currency": "usd",
                "description": "Stripe processing fees",
                "type": "stripe_fee"
            }],
            "net": net_amount,
            "reporting_category": "charge",
            "source": charge_id,
            "status": "available",
            "type": "charge"
        }
    
    def _get_failure_code(self) -> str:
        """Get a realistic failure code."""
        codes = list(PAYMENT_FAILURE_RATES.keys())
        weights = list(PAYMENT_FAILURE_RATES.values())
        return weighted_choice(codes, weights)
    
    def _get_failure_message(self) -> str:
        """Get a failure message based on failure code."""
        messages = {
            "insufficient_funds": "Your card has insufficient funds.",
            "card_declined": "Your card was declined.",
            "expired_card": "Your card has expired.",
            "processing_error": "An error occurred while processing your card."
        }
        return messages.get(self._get_failure_code(), "Your card was declined.")
    
    def _get_payment_method_details(self, payment_method_id: str) -> Dict[str, Any]:
        """Get payment method details for charge."""
        # Simplified - would normally look up actual payment method
        return {
            "card": {
                "brand": "visa",
                "checks": {
                    "address_line1_check": None,
                    "address_postal_code_check": None,
                    "cvc_check": "pass"
                },
                "country": "US",
                "exp_month": 12,
                "exp_year": 2025,
                "fingerprint": "fingerprint123",
                "funding": "credit",
                "installments": None,
                "last4": "4242",
                "network": "visa",
                "three_d_secure": None,
                "wallet": None
            },
            "type": "card"
        }

def main():
    """Test the invoice generator."""
    # This would normally be called with real generators and events
    print("Invoice generator test would require product_price_generator, payment_method_generator, and subscription events")
    print("Run from main.py for full integration test")

if __name__ == "__main__":
    main() 