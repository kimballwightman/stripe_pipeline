"""
Invoice Item Generator for Stripe data generation.
Creates invoice items for additional charges, credits, and adjustments.
"""

import datetime
import random
from typing import Dict, List, Any, Optional
from utils import (
    generate_invoice_item_id, datetime_to_timestamp, 
    weighted_choice, bernoulli_trial, ProgressTracker
)

class InvoiceItemGenerator:
    """Generates realistic Stripe invoice item data."""
    
    def __init__(self):
        self.invoice_items = []
        
    def generate_invoice_items(self, invoices: List[Dict[str, Any]], 
                              customers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate invoice items for invoices and standalone charges."""
        print(f"Generating invoice items for {len(invoices)} invoices...")
        
        progress = ProgressTracker(len(invoices), "Generating invoice items")
        
        for invoice in invoices:
            # 20% chance of additional invoice items
            if bernoulli_trial(0.2):
                invoice_item = self._generate_invoice_item_for_invoice(invoice)
                if invoice_item:
                    self.invoice_items.append(invoice_item)
            
            progress.update()
        
        progress.finish()
        
        # Generate some standalone invoice items (not attached to invoices)
        print("Generating standalone invoice items...")
        standalone_items = self._generate_standalone_invoice_items(customers)
        self.invoice_items.extend(standalone_items)
        
        return self.invoice_items
    
    def _generate_invoice_item_for_invoice(self, invoice: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Generate an invoice item for a specific invoice."""
        invoice_item_id = generate_invoice_item_id()
        
        # Choose type of invoice item
        item_types = {
            "setup_fee": {"weight": 0.3, "amount_range": (5000, 15000)},  # $50-$150
            "overage_charge": {"weight": 0.4, "amount_range": (1000, 5000)},  # $10-$50
            "discount": {"weight": 0.2, "amount_range": (-2000, -500)},  # -$20 to -$5
            "adjustment": {"weight": 0.1, "amount_range": (-1000, 1000)}  # -$10 to $10
        }
        
        item_type = weighted_choice(
            list(item_types.keys()),
            [item_types[t]["weight"] for t in item_types.keys()]
        )
        
        amount_range = item_types[item_type]["amount_range"]
        amount = random.randint(amount_range[0], amount_range[1])
        
        descriptions = {
            "setup_fee": "One-time setup fee",
            "overage_charge": "Usage overage charge",
            "discount": "Promotional discount",
            "adjustment": "Account adjustment"
        }
        
        return {
            "id": invoice_item_id,
            "object": "invoiceitem",
            "amount": amount,
            "currency": "usd",
            "customer": invoice["customer"],
            "date": invoice["created"],
            "description": descriptions[item_type],
            "discountable": item_type != "discount",
            "discounts": [],
            "invoice": invoice["id"],
            "livemode": False,
            "metadata": {
                "item_type": item_type,
                "generated_for": "invoice_attachment"
            },
            "period": {
                "end": invoice["created"] + 86400,  # 1 day period
                "start": invoice["created"]
            },
            "price": None,
            "proration": False,
            "quantity": 1,
            "subscription": invoice.get("subscription"),
            "tax_rates": [],
            "test_clock": None,
            "unit_amount": amount,
            "unit_amount_decimal": str(amount)
        }
    
    def _generate_standalone_invoice_items(self, customers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate standalone invoice items (not attached to invoices)."""
        standalone_items = []
        
        # Generate 5% of customers having standalone items
        num_items = max(1, int(len(customers) * 0.05))
        
        for i in range(num_items):
            customer = random.choice(customers)
            invoice_item_id = generate_invoice_item_id()
            
            # Standalone items are typically credits or adjustments
            item_types = {
                "credit": {"weight": 0.6, "amount_range": (-5000, -1000)},  # -$50 to -$10
                "adjustment": {"weight": 0.3, "amount_range": (-2000, 2000)},  # -$20 to $20
                "manual_charge": {"weight": 0.1, "amount_range": (1000, 10000)}  # $10-$100
            }
            
            item_type = weighted_choice(
                list(item_types.keys()),
                [item_types[t]["weight"] for t in item_types.keys()]
            )
            
            amount_range = item_types[item_type]["amount_range"]
            amount = random.randint(amount_range[0], amount_range[1])
            
            descriptions = {
                "credit": "Account credit",
                "adjustment": "Manual adjustment",
                "manual_charge": "Manual charge"
            }
            
            # Create date within customer's lifecycle
            created_date = datetime_to_timestamp(
                datetime.datetime.fromtimestamp(customer["created"]) + 
                datetime.timedelta(days=random.randint(1, 365))
            )
            
            standalone_item = {
                "id": invoice_item_id,
                "object": "invoiceitem",
                "amount": amount,
                "currency": "usd",
                "customer": customer["id"],
                "date": created_date,
                "description": descriptions[item_type],
                "discountable": item_type != "credit",
                "discounts": [],
                "invoice": None,  # Standalone item
                "livemode": False,
                "metadata": {
                    "item_type": item_type,
                    "generated_for": "standalone"
                },
                "period": {
                    "end": created_date + 86400,  # 1 day period
                    "start": created_date
                },
                "price": None,
                "proration": False,
                "quantity": 1,
                "subscription": None,
                "tax_rates": [],
                "test_clock": None,
                "unit_amount": amount,
                "unit_amount_decimal": str(amount)
            }
            
            standalone_items.append(standalone_item)
        
        return standalone_items


def main():
    """Test the invoice item generator."""
    from customer_generator import CustomerGenerator
    from invoice_generator import InvoiceGenerator
    
    # Create sample data
    customer_gen = CustomerGenerator(total_customers=10)
    customers = customer_gen.generate_customers()
    
    # Create sample invoices
    sample_invoices = [
        {
            "id": "in_test1",
            "customer": customers[0]["id"],
            "created": datetime_to_timestamp(datetime.datetime.now()),
            "subscription": "sub_test1"
        },
        {
            "id": "in_test2",
            "customer": customers[1]["id"],
            "created": datetime_to_timestamp(datetime.datetime.now()),
            "subscription": None
        }
    ]
    
    generator = InvoiceItemGenerator()
    invoice_items = generator.generate_invoice_items(sample_invoices, customers)
    
    print(f"\nGenerated {len(invoice_items)} invoice items")
    
    # Show distribution
    type_counts = {}
    for item in invoice_items:
        item_type = item["metadata"]["item_type"]
        type_counts[item_type] = type_counts.get(item_type, 0) + 1
    
    print("\nInvoice Item Type Distribution:")
    for item_type, count in type_counts.items():
        percentage = (count / len(invoice_items)) * 100
        print(f"  {item_type}: {count} ({percentage:.1f}%)")
    
    # Show sample items
    print("\nSample Invoice Items:")
    for item in invoice_items[:5]:
        amount_str = f"${item['amount']/100:.2f}"
        print(f"  {item['description']}: {amount_str} ({'attached' if item['invoice'] else 'standalone'})")


if __name__ == "__main__":
    main() 