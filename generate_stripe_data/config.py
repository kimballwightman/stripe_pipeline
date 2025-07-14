"""
Configuration file for Stripe data generation.
Contains all business logic parameters and API configuration.
"""

import os
import datetime
from typing import Dict, Any, List, Tuple
import numpy as np

# ============================================================================
# STRIPE API CONFIGURATION
# ============================================================================

# Load Stripe API credentials from environment variables
STRIPE_API_SECRET_KEY = os.getenv("STRIPE_API_SECRET_KEY")
STRIPE_API_PUBLISHABLE_KEY = os.getenv("STRIPE_API_PUBLISHABLE_KEY")
STRIPE_API_URL = os.getenv("STRIPE_API_URL", "https://api.stripe.com/v1")

# Validate required environment variables
if not STRIPE_API_SECRET_KEY:
    print("⚠️  WARNING: STRIPE_API_SECRET_KEY not found in environment variables")
    print("   Set this in your .env file for real API integration")

# API Configuration
STRIPE_API_VERSION = "2024-06-20"  # Latest API version
STRIPE_RATE_LIMIT_REQUESTS_PER_SECOND = 25  # Stripe's default rate limit
STRIPE_MAX_RETRIES = 3  # Maximum retry attempts for failed requests
STRIPE_RETRY_DELAY = 1.0  # Base delay for exponential backoff (seconds)

# ============================================================================
# BUSINESS PARAMETERS
# ============================================================================

# Company Overview
COMPANY_NAME = "DataFlow Analytics"
COMPANY_DOMAIN = "dataflow-analytics.com"
TOTAL_CUSTOMERS = 1
SIMULATION_START_DATE = datetime.date(2020, 1, 1)
SIMULATION_END_DATE = datetime.date(2024, 12, 31)
SIMULATION_YEARS = 5

# Product Configuration
PRODUCTS = {
    "starter": {
        "id": "prod_starter",
        "name": "Starter Plan",
        "description": "Perfect for small teams getting started with analytics",
        "monthly_price": 20.00,
        "annual_price": 200.00,  # 2 months free
        "features": ["Up to 5 users", "Basic dashboards", "Email support"]
    },
    "professional": {
        "id": "prod_professional", 
        "name": "Professional Plan",
        "description": "Advanced analytics for growing businesses",
        "monthly_price": 50.00,
        "annual_price": 500.00,  # 2 months free
        "features": ["Up to 25 users", "Advanced dashboards", "Priority support", "Custom integrations"]
    }
}

# Free Trial Configuration
FREE_TRIAL_DAYS = 30
TRIAL_START_RATE = 0.85  # 85% of signups start trial
TRIAL_CONVERSION_RATE_BASE = 0.22  # 22% base conversion rate

# ============================================================================
# GEOGRAPHIC DISTRIBUTION
# ============================================================================

GEOGRAPHIC_DISTRIBUTION = {
    "north_america": {
        "weight": 0.45,
        "countries": {
            "US": 0.75,
            "CA": 0.20,
            "MX": 0.05
        },
        "trial_conversion_multiplier": 1.2,
        "churn_multiplier": 0.9,
        "timezone_offset": -5  # EST
    },
    "europe": {
        "weight": 0.35,
        "countries": {
            "GB": 0.25,
            "DE": 0.20,
            "FR": 0.15,
            "NL": 0.10,
            "ES": 0.10,
            "IT": 0.10,
            "SE": 0.05,
            "CH": 0.05
        },
        "trial_conversion_multiplier": 1.0,
        "churn_multiplier": 1.0,
        "timezone_offset": 1  # CET
    },
    "asia_pacific": {
        "weight": 0.20,
        "countries": {
            "AU": 0.30,
            "JP": 0.25,
            "SG": 0.15,
            "HK": 0.10,
            "NZ": 0.10,
            "IN": 0.10
        },
        "trial_conversion_multiplier": 0.8,
        "churn_multiplier": 1.2,
        "timezone_offset": 9  # JST
    }
}

# ============================================================================
# PAYMENT METHOD DISTRIBUTION
# ============================================================================

PAYMENT_METHOD_DISTRIBUTION = {
    "card": {
        "weight": 0.85,
        "types": {
            "visa": 0.45,
            "mastercard": 0.35,
            "amex": 0.15,
            "discover": 0.05
        },
        "failure_rate": 0.03,
        "churn_multiplier": 1.0
    },
    "ach_debit": {
        "weight": 0.15,
        "failure_rate": 0.01,
        "churn_multiplier": 0.7  # ACH customers churn less
    }
}

# ============================================================================
# SUBSCRIPTION BEHAVIOR PATTERNS
# ============================================================================

# Monthly churn rates by plan and geography
MONTHLY_CHURN_RATES = {
    "starter": {
        "north_america": 0.05,
        "europe": 0.055,
        "asia_pacific": 0.06
    },
    "professional": {
        "north_america": 0.03,
        "europe": 0.035,
        "asia_pacific": 0.04
    }
}

# Plan preference by geography
PLAN_PREFERENCE = {
    "north_america": {"starter": 0.6, "professional": 0.4},
    "europe": {"starter": 0.65, "professional": 0.35},
    "asia_pacific": {"starter": 0.7, "professional": 0.3}
}

# Billing interval preference
BILLING_INTERVAL_PREFERENCE = {
    "monthly": 0.75,
    "yearly": 0.25
}

# ============================================================================
# SIGNUP PATTERNS
# ============================================================================

# Seasonal signup multipliers by month
SEASONAL_SIGNUP_MULTIPLIERS = {
    1: 1.2,   # January (New Year effect)
    2: 1.1,   # February
    3: 1.0,   # March
    4: 0.9,   # April
    5: 0.8,   # May
    6: 0.7,   # June (summer slowdown)
    7: 0.6,   # July
    8: 0.7,   # August
    9: 1.1,   # September (back to business)
    10: 1.0,  # October
    11: 0.9,  # November
    12: 0.8   # December (holidays)
}

# Day of week multipliers (Monday = 0, Sunday = 6)
DAY_OF_WEEK_MULTIPLIERS = {
    0: 1.2,   # Monday
    1: 1.3,   # Tuesday
    2: 1.2,   # Wednesday
    3: 1.1,   # Thursday
    4: 1.0,   # Friday
    5: 0.6,   # Saturday
    6: 0.5    # Sunday
}

# Growth rate over time (annual multipliers)
ANNUAL_GROWTH_MULTIPLIERS = {
    2020: 0.8,   # Slower start
    2021: 1.0,   # Baseline
    2022: 1.3,   # Strong growth
    2023: 1.1,   # Moderate growth
    2024: 1.0    # Stable
}

# ============================================================================
# FINANCIAL PATTERNS
# ============================================================================

# Refund rates by plan and reason
REFUND_RATES = {
    "starter": 0.025,    # 2.5% of payments
    "professional": 0.015 # 1.5% of payments
}

REFUND_REASONS = {
    "requested_by_customer": 0.6,
    "duplicate": 0.2,
    "fraudulent": 0.1,
    "subscription_canceled": 0.1
}

# Dispute rates and reasons
DISPUTE_RATES = {
    "starter": 0.003,    # 0.3% of payments
    "professional": 0.002 # 0.2% of payments
}

DISPUTE_REASONS = {
    "fraudulent": 0.4,
    "subscription_canceled": 0.3,
    "product_unacceptable": 0.15,
    "unrecognized": 0.1,
    "duplicate": 0.05
}

# Payment failure rates
PAYMENT_FAILURE_RATES = {
    "insufficient_funds": 0.4,
    "card_declined": 0.3,
    "expired_card": 0.2,
    "processing_error": 0.1
}

# ============================================================================
# DATA GENERATION PARAMETERS
# ============================================================================

# Random seed for reproducibility
RANDOM_SEED = 42

# Batch sizes for memory management
BATCH_SIZE = 1000

# Output configuration
OUTPUT_FORMAT = "json"  # json, csv, or parquet
OUTPUT_DIRECTORY = "output"
COMPRESS_OUTPUT = True

# Validation thresholds
VALIDATION_THRESHOLDS = {
    "trial_conversion_rate": (0.15, 0.35),
    "monthly_churn_rate": (0.02, 0.08),
    "refund_rate": (0.01, 0.04),
    "dispute_rate": (0.001, 0.006)
}

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_country_from_region(region: str) -> str:
    """Get a random country from a geographic region."""
    import random
    countries = GEOGRAPHIC_DISTRIBUTION[region]["countries"]
    return random.choices(list(countries.keys()), weights=list(countries.values()))[0]

def get_signup_multiplier(date: datetime.date) -> float:
    """Get the signup multiplier for a given date."""
    seasonal = SEASONAL_SIGNUP_MULTIPLIERS[date.month]
    day_of_week = DAY_OF_WEEK_MULTIPLIERS[date.weekday()]
    annual = ANNUAL_GROWTH_MULTIPLIERS[date.year]
    return seasonal * day_of_week * annual

def get_churn_rate(plan: str, region: str) -> float:
    """Get the monthly churn rate for a plan and region."""
    base_rate = MONTHLY_CHURN_RATES[plan][region]
    return base_rate * GEOGRAPHIC_DISTRIBUTION[region]["churn_multiplier"]

def get_trial_conversion_rate(region: str) -> float:
    """Get the trial conversion rate for a region."""
    return TRIAL_CONVERSION_RATE_BASE * GEOGRAPHIC_DISTRIBUTION[region]["trial_conversion_multiplier"] 