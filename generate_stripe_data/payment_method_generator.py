"""
Payment Method Generator for Stripe data generation.
Creates realistic payment methods for customers with proper distribution.
"""

import datetime
import random
from typing import Dict, List, Any, Optional
from config import PAYMENT_METHOD_DISTRIBUTION
from utils import (
    generate_payment_method_id, generate_card_details, 
    datetime_to_timestamp, weighted_choice, ProgressTracker
)

class PaymentMethodGenerator:
    """Generates realistic Stripe payment method data."""
    
    def __init__(self):
        self.payment_methods = []
        self.customer_payment_methods = {}  # Map customer_id to payment_method_id
    
    def generate_payment_methods(self, customers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate payment methods for all customers."""
        print(f"Generating payment methods for {len(customers)} customers...")
        
        progress = ProgressTracker(len(customers), "Generating payment methods")
        
        for customer in customers:
            customer_id = customer["id"]
            customer_country = customer["metadata"]["country"]
            created_timestamp = customer["created"]
            
            # Determine payment method type
            payment_method_type = self._choose_payment_method_type()
            
            # Generate payment method
            payment_method = self._generate_payment_method(
                customer_id, customer_country, payment_method_type, created_timestamp
            )
            
            self.payment_methods.append(payment_method)
            self.customer_payment_methods[customer_id] = payment_method["id"]
            
            progress.update()
        
        progress.finish()
        return self.payment_methods
    
    def _choose_payment_method_type(self) -> str:
        """Choose payment method type based on distribution."""
        method_types = list(PAYMENT_METHOD_DISTRIBUTION.keys())
        weights = [PAYMENT_METHOD_DISTRIBUTION[method]["weight"] for method in method_types]
        return weighted_choice(method_types, weights)
    
    def _generate_payment_method(self, customer_id: str, customer_country: str, 
                                method_type: str, created_timestamp: int) -> Dict[str, Any]:
        """Generate a specific payment method."""
        payment_method_id = generate_payment_method_id()
        
        base_payment_method = {
            "id": payment_method_id,
            "object": "payment_method",
            "allow_redisplay": "unspecified",  # Default value per API docs
            "billing_details": {
                "address": {
                    "city": None,
                    "country": customer_country,
                    "line1": None,
                    "line2": None,
                    "postal_code": None,
                    "state": None
                },
                "email": None,
                "name": None,
                "phone": None
            },
            "created": created_timestamp,
            "customer": customer_id,
            "livemode": False,
            "metadata": {
                "customer_country": customer_country
            },
            "type": method_type
        }
        
        # Initialize all payment method type fields as None (per API docs)
        payment_method_types = [
            "acss_debit", "affirm", "afterpay_clearpay", "alipay", "alma", "amazon_pay",
            "au_becs_debit", "bacs_debit", "bancontact", "billie", "blik", "boleto",
            "card", "cashapp", "customer_balance", "eps", "fpx", "giropay", "grabpay",
            "ideal", "interac_present", "kakao_pay", "klarna", "konbini", "link",
            "multibanco", "naver_pay", "oxxo", "p24", "payco", "paynow", "paypal",
            "pix", "promptpay", "revolut_pay", "sepa_debit", "sofort", "swish",
            "twint", "us_bank_account", "wechat_pay", "zip"
        ]
        
        for pm_type in payment_method_types:
            base_payment_method[pm_type] = None
        
        if method_type == "card":
            card_type = self._choose_card_type()
            card_details = generate_card_details(card_type)
            
            base_payment_method["card"] = {
                "brand": card_details["brand"],
                "checks": {
                    "address_line1_check": None,
                    "address_postal_code_check": None,
                    "cvc_check": "pass"
                },
                "country": card_details["country"],
                "exp_month": card_details["exp_month"],
                "exp_year": card_details["exp_year"],
                "fingerprint": self._generate_fingerprint(),
                "funding": card_details["funding"],
                "generated_from": None,
                "last4": card_details["last4"],
                "networks": {
                    "available": [card_details["brand"]],
                    "preferred": None
                },
                "three_d_secure_usage": {
                    "supported": True
                },
                "wallet": None
            }
            
            # Add card-specific metadata
            base_payment_method["metadata"]["card_brand"] = card_details["brand"]
            base_payment_method["metadata"]["card_funding"] = card_details["funding"]
            
        elif method_type == "ach_debit":
            base_payment_method["us_bank_account"] = {
                "account_holder_type": "individual",
                "account_type": "checking",
                "bank_name": self._get_random_bank_name(),
                "fingerprint": self._generate_fingerprint(),
                "last4": f"{random.randint(1000, 9999)}",
                "networks": {
                    "preferred": "ach"
                },
                "routing_number": self._generate_routing_number()
            }
            
            # Add ACH-specific metadata
            base_payment_method["metadata"]["bank_account_type"] = "checking"
        
        return base_payment_method
    
    def _choose_card_type(self) -> str:
        """Choose card type based on distribution."""
        card_config = PAYMENT_METHOD_DISTRIBUTION["card"]
        card_types = list(card_config["types"].keys())
        weights = list(card_config["types"].values())
        return weighted_choice(card_types, weights)
    
    def _generate_fingerprint(self) -> str:
        """Generate a realistic fingerprint for payment methods."""
        import string
        return ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    
    def _get_random_bank_name(self) -> str:
        """Get a random US bank name for ACH payments."""
        banks = [
            "JPMorgan Chase Bank",
            "Bank of America",
            "Wells Fargo Bank",
            "Citibank",
            "U.S. Bank",
            "PNC Bank",
            "Goldman Sachs Bank",
            "Truist Bank",
            "Capital One",
            "TD Bank",
            "Bank of New York Mellon",
            "State Street Bank",
            "American Express Bank",
            "HSBC Bank USA",
            "Fifth Third Bank",
            "KeyBank",
            "Huntington National Bank",
            "Regions Bank",
            "M&T Bank",
            "Citizens Bank"
        ]
        return random.choice(banks)
    
    def _generate_routing_number(self) -> str:
        """Generate a valid-looking routing number."""
        # Generate 9-digit routing number (simplified - not actually validated)
        return f"{random.randint(100000000, 999999999)}"
    
    def get_payment_method_for_customer(self, customer_id: str) -> Optional[str]:
        """Get the payment method ID for a customer."""
        return self.customer_payment_methods.get(customer_id)
    
    def get_payment_methods_by_type(self, method_type: str) -> List[Dict[str, Any]]:
        """Get all payment methods of a specific type."""
        return [pm for pm in self.payment_methods if pm["type"] == method_type]
    
    def get_payment_method_failure_rate(self, payment_method_id: str) -> float:
        """Get the failure rate for a specific payment method."""
        payment_method = next(
            (pm for pm in self.payment_methods if pm["id"] == payment_method_id), 
            None
        )
        
        if not payment_method:
            return 0.0
        
        method_type = payment_method["type"]
        return PAYMENT_METHOD_DISTRIBUTION[method_type]["failure_rate"]
    
    def get_churn_multiplier(self, payment_method_id: str) -> float:
        """Get the churn multiplier for a specific payment method."""
        payment_method = next(
            (pm for pm in self.payment_methods if pm["id"] == payment_method_id), 
            None
        )
        
        if not payment_method:
            return 1.0
        
        method_type = payment_method["type"]
        return PAYMENT_METHOD_DISTRIBUTION[method_type]["churn_multiplier"]

def main():
    """Test the payment method generator."""
    # Create some sample customers
    sample_customers = [
        {
            "id": "cus_test1",
            "created": datetime_to_timestamp(datetime.datetime.now()),
            "metadata": {"country": "US"}
        },
        {
            "id": "cus_test2", 
            "created": datetime_to_timestamp(datetime.datetime.now()),
            "metadata": {"country": "CA"}
        },
        {
            "id": "cus_test3",
            "created": datetime_to_timestamp(datetime.datetime.now()),
            "metadata": {"country": "GB"}
        }
    ]
    
    generator = PaymentMethodGenerator()
    payment_methods = generator.generate_payment_methods(sample_customers)
    
    print(f"\nGenerated {len(payment_methods)} payment methods")
    
    # Show distribution
    type_counts = {}
    for pm in payment_methods:
        pm_type = pm["type"]
        type_counts[pm_type] = type_counts.get(pm_type, 0) + 1
    
    print("\nPayment Method Distribution:")
    for pm_type, count in type_counts.items():
        percentage = (count / len(payment_methods)) * 100
        print(f"  {pm_type}: {count} ({percentage:.1f}%)")
    
    # Show sample payment methods
    print("\nSample Payment Methods:")
    for pm in payment_methods:
        if pm["type"] == "card":
            print(f"  Card: {pm['card']['brand']} ending in {pm['card']['last4']}")
        elif pm["type"] == "ach_debit":
            print(f"  ACH: {pm['us_bank_account']['bank_name']} ending in {pm['us_bank_account']['last4']}")
    
    return payment_methods

if __name__ == "__main__":
    main() 