"""
Product and Price Generator for Stripe data generation.
Creates products and prices that match the SaaS business model.
"""

import datetime
from typing import Dict, List, Any
from config import PRODUCTS
from utils import (
    generate_product_id, generate_price_id, 
    datetime_to_timestamp, dollars_to_cents
)

class ProductPriceGenerator:
    """Generates Stripe products and prices for the SaaS business."""
    
    def __init__(self):
        self.products = []
        self.prices = []
        self.product_id_map = {}
        self.price_id_map = {}
    
    def generate_products(self) -> List[Dict[str, Any]]:
        """Generate Stripe product objects."""
        created_timestamp = datetime_to_timestamp(datetime.datetime(2019, 12, 1))
        
        for product_key, product_config in PRODUCTS.items():
            product_id = product_config["id"]
            
            product = {
                "id": product_id,
                "object": "product",
                "active": True,
                "created": created_timestamp,
                "default_price": None,  # Will be set after prices are created
                "description": product_config["description"],
                "images": [],
                "livemode": False,
                "metadata": {
                    "plan_type": product_key
                },
                "name": product_config["name"],
                "package_dimensions": None,
                "shippable": None,
                "statement_descriptor": None,
                "tax_code": None,
                "type": "service",
                "unit_label": None,
                "updated": created_timestamp,
                "url": None,
                "features": product_config["features"]
            }
            
            self.products.append(product)
            self.product_id_map[product_key] = product_id
        
        return self.products
    
    def generate_prices(self) -> List[Dict[str, Any]]:
        """Generate Stripe price objects for each product."""
        created_timestamp = datetime_to_timestamp(datetime.datetime(2019, 12, 1))
        
        # Add timestamp suffix for unique lookup keys in testing
        import time
        timestamp_suffix = str(int(time.time()))[-6:]  # Last 6 digits of timestamp
        
        for product_key, product_config in PRODUCTS.items():
            product_id = self.product_id_map[product_key]
            
            # Monthly price
            monthly_price_id = generate_price_id()
            monthly_price = {
                "id": monthly_price_id,
                "object": "price",
                "active": True,
                "billing_scheme": "per_unit",
                "created": created_timestamp,
                "currency": "usd",
                "custom_unit_amount": None,
                "livemode": False,
                "lookup_key": f"{product_key}_monthly_{timestamp_suffix}",
                "metadata": {
                    "plan_type": product_key,
                    "billing_interval": "month"
                },
                "nickname": f"{product_config['name']} - Monthly",
                "product": product_id,
                "recurring": {
                    "aggregate_usage": None,
                    "interval": "month",
                    "interval_count": 1,
                    "trial_period_days": 30,
                    "usage_type": "licensed"
                },
                "tax_behavior": "exclusive",
                "tiers_mode": None,
                "transform_quantity": None,
                "type": "recurring",
                "unit_amount": dollars_to_cents(product_config["monthly_price"]),
                "unit_amount_decimal": str(dollars_to_cents(product_config["monthly_price"]))
            }
            
            # Annual price
            annual_price_id = generate_price_id()
            annual_price = {
                "id": annual_price_id,
                "object": "price",
                "active": True,
                "billing_scheme": "per_unit",
                "created": created_timestamp,
                "currency": "usd",
                "custom_unit_amount": None,
                "livemode": False,
                "lookup_key": f"{product_key}_yearly_{timestamp_suffix}",
                "metadata": {
                    "plan_type": product_key,
                    "billing_interval": "year"
                },
                "nickname": f"{product_config['name']} - Annual",
                "product": product_id,
                "recurring": {
                    "aggregate_usage": None,
                    "interval": "year",
                    "interval_count": 1,
                    "trial_period_days": 30,
                    "usage_type": "licensed"
                },
                "tax_behavior": "exclusive",
                "tiers_mode": None,
                "transform_quantity": None,
                "type": "recurring",
                "unit_amount": dollars_to_cents(product_config["annual_price"]),
                "unit_amount_decimal": str(dollars_to_cents(product_config["annual_price"]))
            }
            
            self.prices.extend([monthly_price, annual_price])
            
            # Store price IDs for easy lookup
            self.price_id_map[f"{product_key}_monthly"] = monthly_price_id
            self.price_id_map[f"{product_key}_yearly"] = annual_price_id
        
        # Update products with default prices (monthly)
        for product in self.products:
            product_key = None
            for key, config in PRODUCTS.items():
                if config["id"] == product["id"]:
                    product_key = key
                    break
            
            if product_key:
                product["default_price"] = self.price_id_map[f"{product_key}_monthly"]
        
        return self.prices
    
    def get_price_id(self, product_key: str, interval: str) -> str:
        """Get price ID for a product and billing interval."""
        # Normalize interval to the format used in price_id_map
        if interval in ["month", "monthly"]:
            lookup_key = f"{product_key}_monthly"
        elif interval in ["year", "yearly"]:
            lookup_key = f"{product_key}_yearly"
        else:
            raise ValueError(f"Unsupported interval: {interval}")
        return self.price_id_map.get(lookup_key)
    
    def get_product_id(self, product_key: str) -> str:
        """Get product ID for a product key."""
        return self.product_id_map.get(product_key)
    
    def get_price_amount(self, product_key: str, interval: str) -> int:
        """Get price amount in cents for a product and billing interval."""
        if interval in ["month", "monthly"]:
            return dollars_to_cents(PRODUCTS[product_key]["monthly_price"])
        elif interval in ["year", "yearly"]:
            return dollars_to_cents(PRODUCTS[product_key]["annual_price"])
        else:
            raise ValueError(f"Unsupported interval: {interval}")
    
    def generate_all(self) -> Dict[str, List[Dict[str, Any]]]:
        """Generate all products and prices."""
        products = self.generate_products()
        prices = self.generate_prices()
        
        return {
            "products": products,
            "prices": prices
        }

def main():
    """Test the product and price generator."""
    generator = ProductPriceGenerator()
    data = generator.generate_all()
    
    print("Generated Products:")
    for product in data["products"]:
        print(f"  {product['name']} ({product['id']})")
    
    print("\nGenerated Prices:")
    for price in data["prices"]:
        print(f"  {price['nickname']} - ${price['unit_amount']/100:.2f} ({price['id']})")
    
    return data

if __name__ == "__main__":
    main() 