"""
Customer Generator for Stripe data generation.
Creates realistic customer data with geographic distribution and signup patterns.
"""

import datetime
import random
from typing import Dict, List, Any, Optional
from config import (
    TOTAL_CUSTOMERS, SIMULATION_START_DATE, SIMULATION_END_DATE,
    GEOGRAPHIC_DISTRIBUTION, get_country_from_region, get_signup_multiplier
)
from utils import (
    generate_customer_id, generate_email, generate_phone_number, 
    generate_address, random_date_in_range, datetime_to_timestamp,
    weighted_choice, poisson_sample, ProgressTracker
)

class CustomerGenerator:
    """Generates realistic Stripe customer data."""
    
    def __init__(self, total_customers: int = TOTAL_CUSTOMERS):
        self.total_customers = total_customers
        self.customers = []
        self.customer_metadata = {}  # Store additional metadata for other generators
        
        # Pre-generate names for realistic email generation
        self.first_names = [
            "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda",
            "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica",
            "Thomas", "Sarah", "Christopher", "Karen", "Charles", "Nancy", "Daniel", "Lisa",
            "Matthew", "Betty", "Anthony", "Helen", "Mark", "Sandra", "Donald", "Donna",
            "Steven", "Carol", "Paul", "Ruth", "Andrew", "Sharon", "Joshua", "Michelle",
            "Kenneth", "Laura", "Kevin", "Sarah", "Brian", "Kimberly", "George", "Deborah",
            "Timothy", "Dorothy", "Ronald", "Lisa", "Jason", "Nancy", "Edward", "Karen",
            "Jeffrey", "Betty", "Ryan", "Helen", "Jacob", "Sandra", "Gary", "Donna",
            "Nicholas", "Carol", "Eric", "Ruth", "Jonathan", "Sharon", "Stephen", "Michelle",
            "Larry", "Laura", "Justin", "Sarah", "Scott", "Kimberly", "Brandon", "Deborah",
            "Benjamin", "Dorothy", "Samuel", "Lisa", "Gregory", "Nancy", "Alexander", "Karen",
            "Frank", "Betty", "Raymond", "Helen", "Jack", "Sandra", "Dennis", "Donna",
            "Jerry", "Carol", "Tyler", "Ruth", "Aaron", "Sharon", "Jose", "Michelle",
            "Henry", "Laura", "Adam", "Sarah", "Douglas", "Kimberly", "Nathan", "Deborah",
            "Peter", "Dorothy", "Zachary", "Lisa", "Kyle", "Nancy", "Noah", "Karen"
        ]
        
        self.last_names = [
            "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
            "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas",
            "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White",
            "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", "Young",
            "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
            "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
            "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker",
            "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy",
            "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey",
            "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson",
            "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza",
            "Ruiz", "Hughes", "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers",
            "Long", "Ross", "Foster", "Jimenez", "Powell", "Jenkins", "Perry", "Russell",
            "Sullivan", "Bell", "Coleman", "Butler", "Henderson", "Barnes", "Gonzales", "Fisher",
            "Vasquez", "Simmons", "Romero", "Jordan", "Patterson", "Alexander", "Hamilton", "Graham"
        ]
    
    def _generate_signup_dates(self) -> List[datetime.date]:
        """Generate realistic signup dates based on business patterns."""
        signup_dates = []
        
        # Calculate daily signup targets
        total_days = (SIMULATION_END_DATE - SIMULATION_START_DATE).days
        base_signups_per_day = self.total_customers / total_days
        
        current_date = SIMULATION_START_DATE
        customers_generated = 0
        
        while current_date <= SIMULATION_END_DATE and customers_generated < self.total_customers:
            # Get signup multiplier for this date
            multiplier = get_signup_multiplier(current_date)
            expected_signups = base_signups_per_day * multiplier
            
            # Sample from Poisson distribution for realistic daily variation
            actual_signups = poisson_sample(expected_signups)
            
            # Add signup dates for this day
            for _ in range(min(actual_signups, self.total_customers - customers_generated)):
                signup_dates.append(current_date)
                customers_generated += 1
            
            current_date += datetime.timedelta(days=1)
        
        # If we haven't generated enough customers, fill the remainder
        while len(signup_dates) < self.total_customers:
            signup_dates.append(random_date_in_range(SIMULATION_START_DATE, SIMULATION_END_DATE))
        
        # Sort dates and return only the required number
        signup_dates.sort()
        return signup_dates[:self.total_customers]
    
    def _assign_geographic_region(self) -> str:
        """Assign a geographic region based on distribution weights."""
        regions = list(GEOGRAPHIC_DISTRIBUTION.keys())
        weights = [GEOGRAPHIC_DISTRIBUTION[region]["weight"] for region in regions]
        return weighted_choice(regions, weights)
    
    def _generate_customer_name(self) -> tuple[str, str]:
        """Generate a realistic customer name."""
        first_name = random.choice(self.first_names)
        last_name = random.choice(self.last_names)
        return first_name, last_name
    
    def generate_customers(self) -> List[Dict[str, Any]]:
        """Generate all customer records."""
        print(f"Generating {self.total_customers} customers...")
        
        # Add timestamp suffix for unique invoice prefixes in testing
        import time
        timestamp_suffix = str(int(time.time()))[-4:]  # Last 4 digits of timestamp
        
        signup_dates = self._generate_signup_dates()
        
        progress = ProgressTracker(self.total_customers, "Generating customers")
        
        for i in range(self.total_customers):
            # Basic customer info
            customer_id = generate_customer_id()
            first_name, last_name = self._generate_customer_name()
            signup_date = signup_dates[i]
            
            # Geographic assignment
            region = self._assign_geographic_region()
            country = get_country_from_region(region)
            
            # Generate contact info
            email = generate_email(first_name, last_name)
            phone = generate_phone_number(country)
            address = generate_address(country)
            
            # Create customer object - now includes all Stripe API fields
            customer = {
                "id": customer_id,
                "object": "customer",
                "address": address,
                "balance": 0,
                "cash_balance": None,  # Nullable - not used for most customers
                "created": datetime_to_timestamp(
                    datetime.datetime.combine(signup_date, datetime.time(
                        random.randint(9, 17),  # Business hours
                        random.randint(0, 59)
                    ))
                ),
                "currency": "usd",
                "default_source": None,  # Will be set when payment methods are attached
                "delinquent": False,
                "description": f"Customer from {country}",
                "discount": None,  # No discounts applied at customer level
                "email": email,
                "invoice_credit_balance": {},  # Empty for new customers
                "invoice_prefix": f"{customer_id[-8:].upper()}{timestamp_suffix}",
                "invoice_settings": {
                    "custom_fields": None,
                    "default_payment_method": None,  # Will be set when payment methods are attached
                    "footer": None,
                    "rendering_options": None
                },
                "livemode": False,
                "metadata": {
                    "region": region,
                    "country": country,
                    "signup_date": signup_date.isoformat(),
                    "first_name": first_name,
                    "last_name": last_name
                },
                "name": f"{first_name} {last_name}",
                "next_invoice_sequence": 1,
                "phone": phone,
                "preferred_locales": self._get_preferred_locales(country),
                "shipping": None,  # No shipping for SaaS
                "sources": {  # Empty list object for payment sources
                    "object": "list",
                    "data": [],
                    "has_more": False,
                    "url": f"/v1/customers/{customer_id}/sources"
                },
                "subscriptions": {  # Empty list object for subscriptions
                    "object": "list", 
                    "data": [],
                    "has_more": False,
                    "url": f"/v1/customers/{customer_id}/subscriptions"
                },
                "tax": {  # Tax computation status
                    "automatic_tax": "not_collecting",  # Default for most customers
                    "ip_address": None,
                    "location": None
                },
                "tax_exempt": "none",
                "tax_ids": {  # Empty list object for tax IDs
                    "object": "list",
                    "data": [],
                    "has_more": False,
                    "url": f"/v1/customers/{customer_id}/tax_ids"
                },
                "test_clock": None
            }
            
            self.customers.append(customer)
            
            # Store metadata for other generators
            self.customer_metadata[customer_id] = {
                "region": region,
                "country": country,
                "signup_date": signup_date,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone": phone,
                "address": address
            }
            
            progress.update()
        
        progress.finish()
        return self.customers
    
    def _get_preferred_locales(self, country: str) -> List[str]:
        """Get preferred locales based on country."""
        locale_map = {
            "US": ["en-US"],
            "CA": ["en-CA", "fr-CA"],
            "GB": ["en-GB"],
            "DE": ["de-DE"],
            "FR": ["fr-FR"],
            "ES": ["es-ES"],
            "IT": ["it-IT"],
            "NL": ["nl-NL"],
            "SE": ["sv-SE"],
            "CH": ["de-CH", "fr-CH"],
            "AU": ["en-AU"],
            "JP": ["ja-JP"],
            "SG": ["en-SG"],
            "HK": ["en-HK", "zh-HK"],
            "NZ": ["en-NZ"],
            "IN": ["en-IN"],
            "MX": ["es-MX"]
        }
        return locale_map.get(country, ["en-US"])
    
    def get_customer_metadata(self, customer_id: str) -> Optional[Dict[str, Any]]:
        """Get metadata for a specific customer."""
        return self.customer_metadata.get(customer_id)
    
    def get_customers_by_region(self, region: str) -> List[Dict[str, Any]]:
        """Get all customers from a specific region."""
        return [
            customer for customer in self.customers 
            if customer["metadata"]["region"] == region
        ]
    
    def get_customers_by_signup_date_range(self, start_date: datetime.date, end_date: datetime.date) -> List[Dict[str, Any]]:
        """Get customers who signed up within a date range."""
        return [
            customer for customer in self.customers
            if start_date <= datetime.date.fromisoformat(customer["metadata"]["signup_date"]) <= end_date
        ]

def main():
    """Test the customer generator."""
    generator = CustomerGenerator(total_customers=100)  # Small test
    customers = generator.generate_customers()
    
    print(f"\nGenerated {len(customers)} customers")
    
    # Show regional distribution
    region_counts = {}
    for customer in customers:
        region = customer["metadata"]["region"]
        region_counts[region] = region_counts.get(region, 0) + 1
    
    print("\nRegional Distribution:")
    for region, count in region_counts.items():
        percentage = (count / len(customers)) * 100
        print(f"  {region}: {count} ({percentage:.1f}%)")
    
    # Show sample customers
    print("\nSample Customers:")
    for i, customer in enumerate(customers[:5]):
        print(f"  {customer['name']} ({customer['metadata']['country']}) - {customer['email']}")
    
    return customers

if __name__ == "__main__":
    main() 