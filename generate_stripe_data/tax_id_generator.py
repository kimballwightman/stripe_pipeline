"""
Tax ID Generator for Stripe data generation.
Creates tax IDs for customers based on their geography and business requirements.
"""

import datetime
import random
from typing import Dict, List, Any, Optional
from utils import (
    generate_tax_id, datetime_to_timestamp, 
    weighted_choice, bernoulli_trial, ProgressTracker
)

class TaxIdGenerator:
    """Generates realistic Stripe tax ID data."""
    
    def __init__(self):
        self.tax_ids = []
        
    def generate_tax_ids(self, customers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate tax IDs for customers based on geography and business type."""
        print(f"Generating tax IDs for {len(customers)} customers...")
        
        progress = ProgressTracker(len(customers), "Generating tax IDs")
        
        for customer in customers:
            # 30% chance of having a tax ID (business customers)
            if bernoulli_trial(0.3):
                tax_id = self._generate_tax_id_for_customer(customer)
                if tax_id:
                    self.tax_ids.append(tax_id)
            
            progress.update()
        
        progress.finish()
        
        return self.tax_ids
    
    def _generate_tax_id_for_customer(self, customer: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Generate a tax ID for a specific customer."""
        customer_country = customer["metadata"]["country"]
        
        # Get appropriate tax ID type for country
        tax_id_type, tax_id_value = self._get_tax_id_for_country(customer_country)
        
        if not tax_id_type:
            return None
        
        tax_id_id = generate_tax_id()
        
        # Create tax ID date (after customer creation)
        tax_id_date = datetime_to_timestamp(
            datetime.datetime.fromtimestamp(customer["created"]) + 
            datetime.timedelta(days=random.randint(0, 30))
        )
        
        return {
            "id": tax_id_id,
            "object": "tax_id",
            "country": customer_country,
            "created": tax_id_date,
            "customer": customer["id"],
            "livemode": False,
            "type": tax_id_type,
            "value": tax_id_value,
            "verification": {
                "status": "verified",
                "verified_address": None,
                "verified_name": customer.get("name")
            }
        }
    
    def _get_tax_id_for_country(self, country: str) -> tuple[Optional[str], Optional[str]]:
        """Get appropriate tax ID type and value for a country."""
        tax_id_formats = {
            "US": {
                "types": ["us_ein", "us_ssn"],
                "weights": [0.8, 0.2],  # Most businesses use EIN
                "generators": {
                    "us_ein": self._generate_us_ein,
                    "us_ssn": self._generate_us_ssn
                }
            },
            "CA": {
                "types": ["ca_bn", "ca_gst_hst", "ca_pst_bc", "ca_pst_mb", "ca_pst_sk", "ca_qst"],
                "weights": [0.4, 0.3, 0.1, 0.05, 0.05, 0.1],
                "generators": {
                    "ca_bn": self._generate_ca_bn,
                    "ca_gst_hst": self._generate_ca_gst_hst,
                    "ca_pst_bc": self._generate_ca_pst_bc,
                    "ca_pst_mb": self._generate_ca_pst_mb,
                    "ca_pst_sk": self._generate_ca_pst_sk,
                    "ca_qst": self._generate_ca_qst
                }
            },
            "GB": {
                "types": ["gb_vat"],
                "weights": [1.0],
                "generators": {
                    "gb_vat": self._generate_gb_vat
                }
            },
            "DE": {
                "types": ["eu_vat"],
                "weights": [1.0],
                "generators": {
                    "eu_vat": lambda: self._generate_eu_vat("DE")
                }
            },
            "FR": {
                "types": ["eu_vat"],
                "weights": [1.0],
                "generators": {
                    "eu_vat": lambda: self._generate_eu_vat("FR")
                }
            },
            "AU": {
                "types": ["au_abn", "au_arn"],
                "weights": [0.8, 0.2],
                "generators": {
                    "au_abn": self._generate_au_abn,
                    "au_arn": self._generate_au_arn
                }
            },
            "IN": {
                "types": ["in_gst"],
                "weights": [1.0],
                "generators": {
                    "in_gst": self._generate_in_gst
                }
            },
            "JP": {
                "types": ["jp_cn", "jp_rn"],
                "weights": [0.7, 0.3],
                "generators": {
                    "jp_cn": self._generate_jp_cn,
                    "jp_rn": self._generate_jp_rn
                }
            }
        }
        
        if country not in tax_id_formats:
            return None, None
        
        country_config = tax_id_formats[country]
        tax_id_type = weighted_choice(country_config["types"], country_config["weights"])
        tax_id_value = country_config["generators"][tax_id_type]()
        
        return tax_id_type, tax_id_value
    
    # Tax ID generators for different countries
    def _generate_us_ein(self) -> str:
        """Generate US EIN (Employer Identification Number)."""
        # Format: XX-XXXXXXX
        return f"{random.randint(10, 99)}-{random.randint(1000000, 9999999)}"
    
    def _generate_us_ssn(self) -> str:
        """Generate US SSN (Social Security Number) - for sole proprietors."""
        # Format: XXX-XX-XXXX (simplified, not real SSN)
        return f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"
    
    def _generate_ca_bn(self) -> str:
        """Generate Canadian Business Number."""
        # Format: 123456789 (9 digits)
        return f"{random.randint(100000000, 999999999)}"
    
    def _generate_ca_gst_hst(self) -> str:
        """Generate Canadian GST/HST number."""
        # Format: 123456789RT0001
        bn = self._generate_ca_bn()
        return f"{bn}RT0001"
    
    def _generate_ca_pst_bc(self) -> str:
        """Generate BC PST number."""
        # Format: PST-1234-5678
        return f"PST-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
    
    def _generate_ca_pst_mb(self) -> str:
        """Generate Manitoba PST number."""
        # Format: 123456-7
        return f"{random.randint(100000, 999999)}-{random.randint(1, 9)}"
    
    def _generate_ca_pst_sk(self) -> str:
        """Generate Saskatchewan PST number."""
        # Format: 1234567
        return f"{random.randint(1000000, 9999999)}"
    
    def _generate_ca_qst(self) -> str:
        """Generate Quebec QST number."""
        # Format: 1234567890TQ0001
        return f"{random.randint(1000000000, 9999999999)}TQ0001"
    
    def _generate_gb_vat(self) -> str:
        """Generate UK VAT number."""
        # Format: GB123456789 or GB123456789012
        base = random.randint(100000000, 999999999)
        if random.choice([True, False]):
            return f"GB{base}"
        else:
            return f"GB{base}{random.randint(100, 999)}"
    
    def _generate_eu_vat(self, country_code: str) -> str:
        """Generate EU VAT number."""
        # Format varies by country
        formats = {
            "DE": f"DE{random.randint(100000000, 999999999)}",
            "FR": f"FR{random.randint(10000000000, 99999999999)}",
            "IT": f"IT{random.randint(10000000000, 99999999999)}",
            "ES": f"ES{random.randint(10000000, 99999999)}{random.choice(['A', 'B', 'C'])}",
            "NL": f"NL{random.randint(100000000, 999999999)}B{random.randint(10, 99)}",
            "SE": f"SE{random.randint(100000000000, 999999999999)}",
            "CH": f"CHE-{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}"
        }
        return formats.get(country_code, f"{country_code}{random.randint(100000000, 999999999)}")
    
    def _generate_au_abn(self) -> str:
        """Generate Australian Business Number."""
        # Format: 12 345 678 901
        return f"{random.randint(10, 99)} {random.randint(100, 999)} {random.randint(100, 999)} {random.randint(100, 999)}"
    
    def _generate_au_arn(self) -> str:
        """Generate Australian Registered Number."""
        # Format: 123 456 789
        return f"{random.randint(100, 999)} {random.randint(100, 999)} {random.randint(100, 999)}"
    
    def _generate_in_gst(self) -> str:
        """Generate Indian GST number."""
        # Format: 12ABCDE1234F1Z5
        state_code = random.randint(10, 99)
        pan_like = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5))
        numbers = ''.join(random.choices('0123456789', k=4))
        check_digit = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        entity_code = random.randint(1, 9)
        final_char = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        final_digit = random.randint(0, 9)
        
        return f"{state_code}{pan_like}{numbers}{check_digit}{entity_code}{final_char}{final_digit}"
    
    def _generate_jp_cn(self) -> str:
        """Generate Japanese Corporate Number."""
        # Format: 1234567890123 (13 digits)
        return f"{random.randint(1000000000000, 9999999999999)}"
    
    def _generate_jp_rn(self) -> str:
        """Generate Japanese Registration Number."""
        # Format: T1234567890123
        return f"T{random.randint(1000000000000, 9999999999999)}"


def main():
    """Test the tax ID generator."""
    from customer_generator import CustomerGenerator
    
    # Create sample customers from different countries
    customer_gen = CustomerGenerator(total_customers=20)
    customers = customer_gen.generate_customers()
    
    generator = TaxIdGenerator()
    tax_ids = generator.generate_tax_ids(customers)
    
    print(f"\nGenerated {len(tax_ids)} tax IDs")
    
    # Show distribution by country
    country_counts = {}
    type_counts = {}
    
    for tax_id in tax_ids:
        country = tax_id["country"]
        tax_type = tax_id["type"]
        
        country_counts[country] = country_counts.get(country, 0) + 1
        type_counts[tax_type] = type_counts.get(tax_type, 0) + 1
    
    print("\nTax ID Distribution by Country:")
    for country, count in country_counts.items():
        percentage = (count / len(tax_ids)) * 100
        print(f"  {country}: {count} ({percentage:.1f}%)")
    
    print("\nTax ID Distribution by Type:")
    for tax_type, count in type_counts.items():
        percentage = (count / len(tax_ids)) * 100
        print(f"  {tax_type}: {count} ({percentage:.1f}%)")
    
    # Show sample tax IDs
    print("\nSample Tax IDs:")
    for tax_id in tax_ids[:5]:
        print(f"  {tax_id['country']} {tax_id['type']}: {tax_id['value']}")


if __name__ == "__main__":
    main() 