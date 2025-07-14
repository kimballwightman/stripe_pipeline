"""
Credit Note Generator for Stripe data generation.
Creates credit notes for invoice adjustments, refunds, and credits.
"""

import datetime
import random
from typing import Dict, List, Any, Optional
from utils import (
    generate_credit_note_id, datetime_to_timestamp, 
    weighted_choice, bernoulli_trial, ProgressTracker
)

class CreditNoteGenerator:
    """Generates realistic Stripe credit note data."""
    
    def __init__(self):
        self.credit_notes = []
        
    def generate_credit_notes(self, invoices: List[Dict[str, Any]], 
                             refunds: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate credit notes from invoices and refunds."""
        print(f"Generating credit notes for {len(invoices)} invoices...")
        
        progress = ProgressTracker(len(invoices), "Generating credit notes")
        
        for invoice in invoices:
            # 5% chance of credit note per invoice
            if bernoulli_trial(0.05):
                credit_note = self._generate_credit_note_for_invoice(invoice)
                if credit_note:
                    self.credit_notes.append(credit_note)
            
            progress.update()
        
        progress.finish()
        
        # Generate credit notes for refunds
        print(f"Generating credit notes for {len(refunds)} refunds...")
        refund_progress = ProgressTracker(len(refunds), "Processing refunds")
        
        for refund in refunds:
            # 30% chance of credit note per refund
            if bernoulli_trial(0.3):
                credit_note = self._generate_credit_note_for_refund(refund)
                if credit_note:
                    self.credit_notes.append(credit_note)
            
            refund_progress.update()
        
        refund_progress.finish()
        
        return self.credit_notes
    
    def _generate_credit_note_for_invoice(self, invoice: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Generate a credit note for an invoice."""
        credit_note_id = generate_credit_note_id()
        
        # Choose credit note type
        credit_types = {
            "duplicate": {"weight": 0.3, "amount_factor": 1.0},  # Full amount
            "fraudulent": {"weight": 0.2, "amount_factor": 1.0},  # Full amount
            "product_unacceptable": {"weight": 0.3, "amount_factor": 0.5},  # Partial
            "subscription_canceled": {"weight": 0.2, "amount_factor": 0.8}  # Most of amount
        }
        
        credit_type = weighted_choice(
            list(credit_types.keys()),
            [credit_types[t]["weight"] for t in credit_types.keys()]
        )
        
        # Calculate credit amount
        invoice_amount = invoice.get("amount_paid", 0)
        amount_factor = credit_types[credit_type]["amount_factor"]
        credit_amount = int(invoice_amount * amount_factor)
        
        # Create credit note date (after invoice)
        credit_date = datetime_to_timestamp(
            datetime.datetime.fromtimestamp(invoice["created"]) + 
            datetime.timedelta(days=random.randint(1, 30))
        )
        
        reasons = {
            "duplicate": "Duplicate charge",
            "fraudulent": "Fraudulent transaction",
            "product_unacceptable": "Product not acceptable",
            "subscription_canceled": "Subscription canceled"
        }
        
        return {
            "id": credit_note_id,
            "object": "credit_note",
            "amount": credit_amount,
            "amount_shipping": 0,  # No shipping for SaaS
            "created": credit_date,
            "currency": "usd",
            "customer": invoice["customer"],
            "customer_balance_transaction": None,
            "discount_amount": 0,
            "discount_amounts": [],
            "effective_at": credit_date,
            "invoice": invoice["id"],
            "lines": {
                "object": "list",
                "data": [{
                    "id": f"cnli_{credit_note_id[3:]}",
                    "object": "credit_note_line_item",
                    "amount": credit_amount,
                    "amount_excluding_tax": credit_amount,
                    "description": f"Credit for {reasons[credit_type]}",
                    "discount_amount": 0,
                    "discount_amounts": [],
                    "invoice_line_item": f"il_{invoice['id'][3:]}",
                    "livemode": False,
                    "quantity": 1,
                    "tax_amounts": [],
                    "tax_rates": [],
                    "type": "invoice_line_item",
                    "unit_amount": credit_amount,
                    "unit_amount_decimal": str(credit_amount),
                    "unit_amount_excluding_tax": str(credit_amount)
                }],
                "has_more": False,
                "total_count": 1,
                "url": f"/v1/credit_notes/{credit_note_id}/lines"
            },
            "livemode": False,
            "memo": f"Credit note for {reasons[credit_type].lower()}",
            "metadata": {
                "credit_type": credit_type,
                "original_invoice": invoice["id"],
                "generated_for": "invoice_credit"
            },
            "number": f"CN-{credit_note_id[-8:].upper()}",
            "out_of_band_amount": 0,
            "pdf": f"https://pay.stripe.com/credit_notes/{credit_note_id}/pdf",
            "reason": credit_type,
            "refund": None,  # Will be set if refund is created
            "shipping_cost": None,
            "status": "issued",
            "subtotal": credit_amount,
            "subtotal_excluding_tax": credit_amount,
            "tax_amounts": [],
            "total": credit_amount,
            "total_excluding_tax": credit_amount,
            "type": "pre_payment",
            "voided_at": None
        }
    
    def _generate_credit_note_for_refund(self, refund: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Generate a credit note for a refund."""
        credit_note_id = generate_credit_note_id()
        
        # Create credit note date (same as refund)
        credit_date = refund["created"]
        
        return {
            "id": credit_note_id,
            "object": "credit_note",
            "amount": refund["amount"],
            "amount_shipping": 0,
            "created": credit_date,
            "currency": "usd",
            "customer": refund.get("customer"),
            "customer_balance_transaction": None,
            "discount_amount": 0,
            "discount_amounts": [],
            "effective_at": credit_date,
            "invoice": None,  # Refund-based credit note
            "lines": {
                "object": "list",
                "data": [{
                    "id": f"cnli_{credit_note_id[3:]}",
                    "object": "credit_note_line_item",
                    "amount": refund["amount"],
                    "amount_excluding_tax": refund["amount"],
                    "description": f"Credit for refund: {refund.get('reason', 'requested_by_customer')}",
                    "discount_amount": 0,
                    "discount_amounts": [],
                    "invoice_line_item": None,
                    "livemode": False,
                    "quantity": 1,
                    "tax_amounts": [],
                    "tax_rates": [],
                    "type": "custom_line_item",
                    "unit_amount": refund["amount"],
                    "unit_amount_decimal": str(refund["amount"]),
                    "unit_amount_excluding_tax": str(refund["amount"])
                }],
                "has_more": False,
                "total_count": 1,
                "url": f"/v1/credit_notes/{credit_note_id}/lines"
            },
            "livemode": False,
            "memo": f"Credit note for refund {refund['id']}",
            "metadata": {
                "credit_type": "refund",
                "original_refund": refund["id"],
                "generated_for": "refund_credit"
            },
            "number": f"CN-{credit_note_id[-8:].upper()}",
            "out_of_band_amount": 0,
            "pdf": f"https://pay.stripe.com/credit_notes/{credit_note_id}/pdf",
            "reason": refund.get("reason", "requested_by_customer"),
            "refund": refund["id"],
            "shipping_cost": None,
            "status": "issued",
            "subtotal": refund["amount"],
            "subtotal_excluding_tax": refund["amount"],
            "tax_amounts": [],
            "total": refund["amount"],
            "total_excluding_tax": refund["amount"],
            "type": "post_payment",
            "voided_at": None
        }


def main():
    """Test the credit note generator."""
    from customer_generator import CustomerGenerator
    
    # Create sample data
    customer_gen = CustomerGenerator(total_customers=5)
    customers = customer_gen.generate_customers()
    
    # Create sample invoices
    sample_invoices = [
        {
            "id": "in_test1",
            "customer": customers[0]["id"],
            "created": datetime_to_timestamp(datetime.datetime.now() - datetime.timedelta(days=10)),
            "amount_paid": 5000
        },
        {
            "id": "in_test2",
            "customer": customers[1]["id"],
            "created": datetime_to_timestamp(datetime.datetime.now() - datetime.timedelta(days=5)),
            "amount_paid": 2000
        }
    ]
    
    # Create sample refunds
    sample_refunds = [
        {
            "id": "re_test1",
            "customer": customers[0]["id"],
            "created": datetime_to_timestamp(datetime.datetime.now() - datetime.timedelta(days=3)),
            "amount": 1000,
            "reason": "requested_by_customer"
        }
    ]
    
    generator = CreditNoteGenerator()
    credit_notes = generator.generate_credit_notes(sample_invoices, sample_refunds)
    
    print(f"\nGenerated {len(credit_notes)} credit notes")
    
    # Show distribution
    type_counts = {}
    for note in credit_notes:
        credit_type = note["metadata"]["credit_type"]
        type_counts[credit_type] = type_counts.get(credit_type, 0) + 1
    
    print("\nCredit Note Type Distribution:")
    for credit_type, count in type_counts.items():
        percentage = (count / len(credit_notes)) * 100 if credit_notes else 0
        print(f"  {credit_type}: {count} ({percentage:.1f}%)")
    
    # Show sample credit notes
    print("\nSample Credit Notes:")
    for note in credit_notes[:3]:
        amount_str = f"${note['amount']/100:.2f}"
        print(f"  {note['reason']}: {amount_str} ({note['type']})")


if __name__ == "__main__":
    main() 