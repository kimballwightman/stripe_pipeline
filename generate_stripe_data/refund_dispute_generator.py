"""
Refund and Dispute Generator for Stripe data generation.
Creates realistic refunds and disputes based on successful charges.
"""

import datetime
import random
from typing import Dict, List, Any, Optional
from config import REFUND_RATES, REFUND_REASONS, DISPUTE_RATES, DISPUTE_REASONS
from utils import (
    generate_refund_id, generate_dispute_id, generate_balance_transaction_id,
    datetime_to_timestamp, weighted_choice, bernoulli_trial, ProgressTracker
)

class RefundDisputeGenerator:
    """Generates realistic Stripe refund and dispute data."""
    
    def __init__(self):
        self.refunds = []
        self.disputes = []
        self.credit_notes = []
        self.balance_transactions = []
    
    def generate_refunds_and_disputes(self, charges: List[Dict[str, Any]], 
                                    invoices: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """Generate refunds and disputes from successful charges."""
        print(f"Generating refunds and disputes from {len(charges)} charges...")
        
        # Filter successful charges only
        successful_charges = [charge for charge in charges if charge["status"] == "succeeded"]
        
        progress = ProgressTracker(len(successful_charges), "Processing charges for refunds/disputes")
        
        for charge in successful_charges:
            # Get associated invoice to determine plan
            invoice = self._get_invoice_for_charge(charge["id"], invoices)
            if not invoice:
                progress.update()
                continue
            
            plan_key = invoice["metadata"].get("plan_key", "starter")
            
            # Generate refund if applicable
            refund_data = self._maybe_generate_refund(charge, invoice, plan_key)
            if refund_data:
                self.refunds.append(refund_data["refund"])
                if refund_data["balance_transaction"]:
                    self.balance_transactions.append(refund_data["balance_transaction"])
                if refund_data["credit_note"]:
                    self.credit_notes.append(refund_data["credit_note"])
            
            # Generate dispute if applicable (and not already refunded)
            elif self._should_generate_dispute(plan_key):
                dispute_data = self._generate_dispute(charge, invoice, plan_key)
                if dispute_data:
                    self.disputes.append(dispute_data["dispute"])
                    if dispute_data["balance_transaction"]:
                        self.balance_transactions.append(dispute_data["balance_transaction"])
            
            progress.update()
        
        progress.finish()
        
        return {
            "refunds": self.refunds,
            "disputes": self.disputes,
            "credit_notes": self.credit_notes,
            "balance_transactions": self.balance_transactions
        }
    
    def _get_invoice_for_charge(self, charge_id: str, invoices: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Find the invoice associated with a charge."""
        return next((invoice for invoice in invoices if invoice.get("charge") == charge_id), None)
    
    def _should_generate_refund(self, plan_key: str) -> bool:
        """Determine if a refund should be generated."""
        refund_rate = REFUND_RATES.get(plan_key, 0.02)
        return bernoulli_trial(refund_rate)
    
    def _should_generate_dispute(self, plan_key: str) -> bool:
        """Determine if a dispute should be generated."""
        dispute_rate = DISPUTE_RATES.get(plan_key, 0.002)
        return bernoulli_trial(dispute_rate)
    
    def _maybe_generate_refund(self, charge: Dict[str, Any], invoice: Dict[str, Any], 
                              plan_key: str) -> Optional[Dict[str, Any]]:
        """Maybe generate a refund for a charge."""
        if not self._should_generate_refund(plan_key):
            return None
        
        return self._generate_refund(charge, invoice, plan_key)
    
    def _generate_refund(self, charge: Dict[str, Any], invoice: Dict[str, Any], 
                        plan_key: str) -> Dict[str, Any]:
        """Generate a refund for a charge."""
        refund_id = generate_refund_id()
        charge_id = charge["id"]
        amount = charge["amount"]
        
        # Determine refund timing (usually within 30 days of charge)
        charge_date = datetime.datetime.fromtimestamp(charge["created"])
        refund_date = charge_date + datetime.timedelta(days=random.randint(1, 30))
        refund_timestamp = datetime_to_timestamp(refund_date)
        
        # Choose refund reason
        reason = weighted_choice(list(REFUND_REASONS.keys()), list(REFUND_REASONS.values()))
        
        # Determine if it's a partial or full refund
        is_partial = random.random() < 0.2  # 20% chance of partial refund
        refund_amount = amount if not is_partial else random.randint(int(amount * 0.3), int(amount * 0.8))
        
        refund = {
            "id": refund_id,
            "object": "refund",
            "amount": refund_amount,
            "balance_transaction": f"txn_{refund_id[3:]}",
            "charge": charge_id,
            "created": refund_timestamp,
            "currency": "usd",
            "metadata": {
                "plan_key": plan_key,
                "refund_reason": reason,
                "invoice_id": invoice["id"]
            },
            "reason": reason,
            "receipt_number": None,
            "source_transfer_reversal": None,
            "status": "succeeded",
            "transfer_reversal": None
        }
        
        # Create balance transaction for refund
        balance_transaction = self._create_refund_balance_transaction(
            refund_id, charge_id, refund_amount, refund_timestamp
        )
        
        # Create credit note if this is a subscription refund
        credit_note = None
        if invoice.get("subscription"):
            credit_note = self._create_credit_note(
                refund, invoice, refund_amount, refund_timestamp
            )
        
        return {
            "refund": refund,
            "balance_transaction": balance_transaction,
            "credit_note": credit_note
        }
    
    def _generate_dispute(self, charge: Dict[str, Any], invoice: Dict[str, Any], 
                         plan_key: str) -> Dict[str, Any]:
        """Generate a dispute for a charge."""
        dispute_id = generate_dispute_id()
        charge_id = charge["id"]
        amount = charge["amount"]
        
        # Determine dispute timing (usually within 120 days of charge)
        charge_date = datetime.datetime.fromtimestamp(charge["created"])
        dispute_date = charge_date + datetime.timedelta(days=random.randint(1, 120))
        dispute_timestamp = datetime_to_timestamp(dispute_date)
        
        # Choose dispute reason
        reason = weighted_choice(list(DISPUTE_REASONS.keys()), list(DISPUTE_REASONS.values()))
        
        # Determine dispute status
        status = weighted_choice(
            ["warning_needs_response", "needs_response", "under_review", "charge_refunded", "lost", "won"],
            [0.1, 0.3, 0.2, 0.15, 0.15, 0.1]
        )
        
        dispute = {
            "id": dispute_id,
            "object": "dispute",
            "amount": amount,
            "balance_transactions": [f"txn_{dispute_id[3:]}"],
            "charge": charge_id,
            "created": dispute_timestamp,
            "currency": "usd",
            "evidence": {
                "access_activity_log": None,
                "billing_address": None,
                "cancellation_policy": None,
                "cancellation_policy_disclosure": None,
                "cancellation_rebuttal": None,
                "customer_communication": None,
                "customer_email_address": None,
                "customer_name": None,
                "customer_purchase_ip": None,
                "customer_signature": None,
                "duplicate_charge_documentation": None,
                "duplicate_charge_explanation": None,
                "duplicate_charge_id": None,
                "product_description": None,
                "receipt": None,
                "refund_policy": None,
                "refund_policy_disclosure": None,
                "refund_refusal_explanation": None,
                "service_date": None,
                "service_documentation": None,
                "shipping_address": None,
                "shipping_carrier": None,
                "shipping_date": None,
                "shipping_documentation": None,
                "shipping_tracking_number": None,
                "uncategorized_file": None,
                "uncategorized_text": None
            },
            "evidence_details": {
                "due_by": dispute_timestamp + 86400 * 7,  # 7 days to respond
                "has_evidence": False,
                "past_due": False,
                "submission_count": 0
            },
            "is_charge_refundable": status not in ["charge_refunded", "lost"],
            "livemode": False,
            "metadata": {
                "plan_key": plan_key,
                "dispute_reason": reason,
                "invoice_id": invoice["id"]
            },
            "network_reason_code": self._get_network_reason_code(reason),
            "reason": reason,
            "status": status
        }
        
        # Create balance transaction for dispute
        balance_transaction = self._create_dispute_balance_transaction(
            dispute_id, charge_id, amount, dispute_timestamp
        )
        
        return {
            "dispute": dispute,
            "balance_transaction": balance_transaction
        }
    
    def _create_refund_balance_transaction(self, refund_id: str, charge_id: str, 
                                         amount: int, timestamp: int) -> Dict[str, Any]:
        """Create balance transaction for refund."""
        transaction_id = generate_balance_transaction_id()
        
        return {
            "id": transaction_id,
            "object": "balance_transaction",
            "amount": -amount,  # Negative for refund
            "available_on": timestamp + 86400,  # Available next day
            "created": timestamp,
            "currency": "usd",
            "description": f"Refund for {charge_id}",
            "exchange_rate": None,
            "fee": 0,  # No fee for refunds
            "fee_details": [],
            "net": -amount,
            "reporting_category": "refund",
            "source": refund_id,
            "status": "available",
            "type": "refund"
        }
    
    def _create_dispute_balance_transaction(self, dispute_id: str, charge_id: str, 
                                          amount: int, timestamp: int) -> Dict[str, Any]:
        """Create balance transaction for dispute."""
        transaction_id = generate_balance_transaction_id()
        
        # Dispute fee is typically $15
        dispute_fee = 1500  # $15 in cents
        
        return {
            "id": transaction_id,
            "object": "balance_transaction",
            "amount": -(amount + dispute_fee),  # Negative for dispute
            "available_on": timestamp,
            "created": timestamp,
            "currency": "usd",
            "description": f"Chargeback withdrawal for {charge_id}",
            "exchange_rate": None,
            "fee": dispute_fee,
            "fee_details": [{
                "amount": dispute_fee,
                "currency": "usd",
                "description": "Dispute fee",
                "type": "stripe_fee"
            }],
            "net": -(amount + dispute_fee),
            "reporting_category": "dispute",
            "source": dispute_id,
            "status": "available",
            "type": "adjustment"
        }
    
    def _create_credit_note(self, refund: Dict[str, Any], invoice: Dict[str, Any], 
                           amount: int, timestamp: int) -> Dict[str, Any]:
        """Create credit note for subscription refund."""
        from utils import generate_credit_note_id
        
        credit_note_id = generate_credit_note_id()
        
        return {
            "id": credit_note_id,
            "object": "credit_note",
            "amount": amount,
            "created": timestamp,
            "currency": "usd",
            "customer": invoice["customer"],
            "customer_balance_transaction": None,
            "discount_amount": 0,
            "discount_amounts": [],
            "invoice": invoice["id"],
            "lines": {
                "object": "list",
                "data": [{
                    "id": f"cnli_{credit_note_id[3:]}",
                    "object": "credit_note_line_item",
                    "amount": amount,
                    "description": f"Refund for {invoice['lines']['data'][0]['description']}",
                    "discount_amount": 0,
                    "discount_amounts": [],
                    "invoice_line_item": invoice["lines"]["data"][0]["id"],
                    "livemode": False,
                    "quantity": 1,
                    "tax_amounts": [],
                    "tax_rates": [],
                    "type": "invoice_line_item",
                    "unit_amount": amount,
                    "unit_amount_decimal": str(amount)
                }],
                "has_more": False,
                "total_count": 1,
                "url": f"/v1/credit_notes/{credit_note_id}/lines"
            },
            "livemode": False,
            "memo": f"Refund processed: {refund['reason']}",
            "metadata": {
                "refund_id": refund["id"],
                "invoice_id": invoice["id"]
            },
            "number": f"CN-{random.randint(100000, 999999)}",
            "out_of_band_amount": None,
            "pdf": f"https://pay.stripe.com/credit_notes/{credit_note_id}/pdf",
            "reason": "duplicate",
            "refund": refund["id"],
            "status": "issued",
            "subtotal": amount,
            "tax_amounts": [],
            "total": amount,
            "type": "post_payment",
            "voided_at": None
        }
    
    def _get_network_reason_code(self, reason: str) -> str:
        """Get network reason code for dispute reason."""
        reason_code_map = {
            "fraudulent": "4855",
            "subscription_canceled": "4855",
            "product_unacceptable": "4855",
            "unrecognized": "4515",
            "duplicate": "4834"
        }
        return reason_code_map.get(reason, "4855")
    
    def get_refunds_for_charge(self, charge_id: str) -> List[Dict[str, Any]]:
        """Get all refunds for a specific charge."""
        return [refund for refund in self.refunds if refund["charge"] == charge_id]
    
    def get_disputes_for_charge(self, charge_id: str) -> List[Dict[str, Any]]:
        """Get all disputes for a specific charge."""
        return [dispute for dispute in self.disputes if dispute["charge"] == charge_id]
    
    def get_refund_rate_by_plan(self, plan_key: str) -> float:
        """Get refund rate for a specific plan."""
        return REFUND_RATES.get(plan_key, 0.02)
    
    def get_dispute_rate_by_plan(self, plan_key: str) -> float:
        """Get dispute rate for a specific plan."""
        return DISPUTE_RATES.get(plan_key, 0.002)

def main():
    """Test the refund and dispute generator."""
    # Create sample charges for testing
    sample_charges = [
        {
            "id": "ch_test1",
            "amount": 2000,
            "status": "succeeded",
            "created": datetime_to_timestamp(datetime.datetime.now() - datetime.timedelta(days=10))
        },
        {
            "id": "ch_test2",
            "amount": 5000,
            "status": "succeeded", 
            "created": datetime_to_timestamp(datetime.datetime.now() - datetime.timedelta(days=5))
        }
    ]
    
    sample_invoices = [
        {
            "id": "in_test1",
            "charge": "ch_test1",
            "customer": "cus_test1",
            "subscription": "sub_test1",
            "metadata": {"plan_key": "starter"},
            "lines": {
                "data": [{
                    "id": "il_test1",
                    "description": "Starter plan (monthly billing)"
                }]
            }
        },
        {
            "id": "in_test2",
            "charge": "ch_test2",
            "customer": "cus_test2",
            "subscription": "sub_test2",
            "metadata": {"plan_key": "professional"},
            "lines": {
                "data": [{
                    "id": "il_test2",
                    "description": "Professional plan (monthly billing)"
                }]
            }
        }
    ]
    
    generator = RefundDisputeGenerator()
    data = generator.generate_refunds_and_disputes(sample_charges, sample_invoices)
    
    print(f"Generated {len(data['refunds'])} refunds")
    print(f"Generated {len(data['disputes'])} disputes")
    print(f"Generated {len(data['credit_notes'])} credit notes")
    print(f"Generated {len(data['balance_transactions'])} balance transactions")
    
    return data

if __name__ == "__main__":
    main() 