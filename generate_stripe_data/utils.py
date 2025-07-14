"""
Utility functions for Stripe data generation.
"""

import datetime
import random
import string
import uuid
from typing import Dict, List, Any, Optional, Callable, Tuple
import json
import os
from decimal import Decimal
import numpy as np
import time
from dataclasses import dataclass, field
from enum import Enum

# ============================================================================
# STRIPE API INTEGRATION
# ============================================================================

try:
    import stripe
    STRIPE_AVAILABLE = True
except ImportError:
    STRIPE_AVAILABLE = False
    print("⚠️  WARNING: stripe library not installed. API simulation only.")

# ============================================================================
# ID GENERATION FUNCTIONS
# ============================================================================

def generate_stripe_id(prefix: str, length: int = 24) -> str:
    """Generate a Stripe-style ID with the given prefix."""
    chars = string.ascii_lowercase + string.digits
    suffix = ''.join(random.choices(chars, k=length))
    return f"{prefix}_{suffix}"

def generate_customer_id() -> str:
    """Generate a customer ID (cus_xxx)."""
    return generate_stripe_id("cus")

def generate_subscription_id() -> str:
    """Generate a subscription ID (sub_xxx)."""
    return generate_stripe_id("sub")

def generate_invoice_id() -> str:
    """Generate an invoice ID (in_xxx)."""
    return generate_stripe_id("in")

def generate_payment_intent_id() -> str:
    """Generate a payment intent ID (pi_xxx)."""
    return generate_stripe_id("pi")

def generate_charge_id() -> str:
    """Generate a charge ID (ch_xxx)."""
    return generate_stripe_id("ch")

def generate_refund_id() -> str:
    """Generate a refund ID (re_xxx)."""
    return generate_stripe_id("re")

def generate_dispute_id() -> str:
    """Generate a dispute ID (dp_xxx)."""
    return generate_stripe_id("dp")

def generate_payment_method_id() -> str:
    """Generate a payment method ID (pm_xxx)."""
    return generate_stripe_id("pm")

def generate_product_id() -> str:
    """Generate a product ID (prod_xxx)."""
    return generate_stripe_id("prod")

def generate_price_id() -> str:
    """Generate a price ID (price_xxx)."""
    return generate_stripe_id("price")

def generate_credit_note_id() -> str:
    """Generate a credit note ID (cn_xxx)."""
    return generate_stripe_id("cn")

def generate_balance_transaction_id() -> str:
    """Generate a balance transaction ID (txn_xxx)."""
    return generate_stripe_id("txn")

def generate_invoice_item_id() -> str:
    """Generate a Stripe invoice item ID."""
    return generate_stripe_id("ii", 24)

def generate_credit_note_id() -> str:
    """Generate a Stripe credit note ID."""
    return generate_stripe_id("cn", 24)

def generate_tax_id() -> str:
    """Generate a Stripe tax ID."""
    return generate_stripe_id("txi", 24)

# ============================================================================
# DATE UTILITIES
# ============================================================================

def random_date_in_range(start_date: datetime.date, end_date: datetime.date) -> datetime.date:
    """Generate a random date between start_date and end_date."""
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + datetime.timedelta(days=random_days)

def random_datetime_in_range(start_date: datetime.date, end_date: datetime.date) -> datetime.datetime:
    """Generate a random datetime between start_date and end_date."""
    random_date = random_date_in_range(start_date, end_date)
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    return datetime.datetime.combine(random_date, datetime.time(random_hour, random_minute, random_second))

def add_months(date: datetime.date, months: int) -> datetime.date:
    """Add months to a date, handling month overflow."""
    month = date.month - 1 + months
    year = date.year + month // 12
    month = month % 12 + 1
    day = min(date.day, [31, 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
    return datetime.date(year, month, day)

def get_next_billing_date(start_date: datetime.date, interval: str) -> datetime.date:
    """Get the next billing date based on interval."""
    if interval in ["month", "monthly"]:
        return add_months(start_date, 1)
    elif interval in ["year", "yearly"]:
        return add_months(start_date, 12)
    else:
        raise ValueError(f"Unsupported interval: {interval}")

def date_to_timestamp(date: datetime.date) -> int:
    """Convert date to Unix timestamp."""
    return int(datetime.datetime.combine(date, datetime.time()).timestamp())

def datetime_to_timestamp(dt: datetime.datetime) -> int:
    """Convert datetime to Unix timestamp."""
    return int(dt.timestamp())

# ============================================================================
# DATA GENERATION UTILITIES
# ============================================================================

def generate_email(first_name: str, last_name: str, domain: str = None) -> str:
    """Generate a realistic email address."""
    if domain is None:
        domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "company.com"]
        domain = random.choice(domains)
    
    # Various email formats
    formats = [
        f"{first_name.lower()}.{last_name.lower()}",
        f"{first_name.lower()}{last_name.lower()}",
        f"{first_name.lower()}_{last_name.lower()}",
        f"{first_name[0].lower()}{last_name.lower()}",
        f"{first_name.lower()}{random.randint(1, 999)}"
    ]
    
    username = random.choice(formats)
    return f"{username}@{domain}"

def generate_phone_number(country: str) -> str:
    """Generate a phone number for the given country."""
    if country == "US":
        return f"+1{random.randint(200, 999)}{random.randint(200, 999)}{random.randint(1000, 9999)}"
    elif country == "CA":
        return f"+1{random.randint(200, 999)}{random.randint(200, 999)}{random.randint(1000, 9999)}"
    elif country == "GB":
        return f"+44{random.randint(1000000000, 9999999999)}"
    elif country == "DE":
        return f"+49{random.randint(100000000, 999999999)}"
    elif country == "FR":
        return f"+33{random.randint(100000000, 999999999)}"
    elif country == "AU":
        return f"+61{random.randint(100000000, 999999999)}"
    elif country == "JP":
        return f"+81{random.randint(1000000000, 9999999999)}"
    else:
        return f"+{random.randint(1, 999)}{random.randint(1000000000, 9999999999)}"

def generate_address(country: str) -> Dict[str, str]:
    """Generate a realistic address for the given country."""
    addresses = {
        "US": {
            "line1": f"{random.randint(1, 9999)} {random.choice(['Main St', 'Oak Ave', 'Park Rd', 'First St', 'Second Ave'])}",
            "city": random.choice(["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"]),
            "state": random.choice(["NY", "CA", "IL", "TX", "AZ", "PA"]),
            "postal_code": f"{random.randint(10000, 99999)}",
            "country": "US"
        },
        "CA": {
            "line1": f"{random.randint(1, 9999)} {random.choice(['Main St', 'Oak Ave', 'Park Rd', 'First St', 'Second Ave'])}",
            "city": random.choice(["Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa", "Edmonton"]),
            "state": random.choice(["ON", "BC", "QC", "AB", "MB", "SK"]),
            "postal_code": f"{random.choice(string.ascii_uppercase)}{random.randint(0, 9)}{random.choice(string.ascii_uppercase)} {random.randint(0, 9)}{random.choice(string.ascii_uppercase)}{random.randint(0, 9)}",
            "country": "CA"
        },
        "GB": {
            "line1": f"{random.randint(1, 999)} {random.choice(['High Street', 'Church Lane', 'Victoria Road', 'Mill Lane', 'School Lane'])}",
            "city": random.choice(["London", "Birmingham", "Manchester", "Liverpool", "Leeds", "Sheffield"]),
            "postal_code": f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.randint(0, 9)} {random.randint(0, 9)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}",
            "country": "GB"
        }
    }
    
    return addresses.get(country, {
        "line1": f"{random.randint(1, 999)} Main Street",
        "city": "City",
        "postal_code": f"{random.randint(10000, 99999)}",
        "country": country
    })

def generate_card_details(card_type: str) -> Dict[str, Any]:
    """Generate card details for the given card type."""
    card_prefixes = {
        "visa": ["4"],
        "mastercard": ["5"],
        "amex": ["34", "37"],
        "discover": ["6"]
    }
    
    prefix = random.choice(card_prefixes[card_type])
    if card_type == "amex":
        number = prefix + ''.join([str(random.randint(0, 9)) for _ in range(13)])
    else:
        number = prefix + ''.join([str(random.randint(0, 9)) for _ in range(15)])
    
    exp_month = random.randint(1, 12)
    exp_year = random.randint(2025, 2030)
    
    return {
        "brand": card_type,
        "last4": number[-4:],
        "exp_month": exp_month,
        "exp_year": exp_year,
        "funding": "credit" if card_type != "discover" else random.choice(["credit", "debit"]),
        "country": "US"  # Simplified for now
    }

# ============================================================================
# FINANCIAL UTILITIES
# ============================================================================

def cents_to_dollars(cents: int) -> float:
    """Convert cents to dollars."""
    return cents / 100.0

def dollars_to_cents(dollars: float) -> int:
    """Convert dollars to cents."""
    return int(round(dollars * 100))

def calculate_tax(amount: float, tax_rate: float = 0.08) -> float:
    """Calculate tax amount."""
    return round(amount * tax_rate, 2)

def apply_discount(amount: float, discount_percent: float) -> float:
    """Apply discount to amount."""
    return round(amount * (1 - discount_percent / 100), 2)

# ============================================================================
# PROBABILITY UTILITIES
# ============================================================================

def weighted_choice(choices: List[Any], weights: List[float]) -> Any:
    """Make a weighted random choice."""
    return random.choices(choices, weights=weights)[0]

def bernoulli_trial(probability: float) -> bool:
    """Perform a Bernoulli trial with given probability."""
    return random.random() < probability

def poisson_sample(lambda_param: float) -> int:
    """Sample from a Poisson distribution."""
    return np.random.poisson(lambda_param)

def normal_sample(mean: float, std: float) -> float:
    """Sample from a normal distribution."""
    return np.random.normal(mean, std)

def lognormal_sample(mean: float, std: float) -> float:
    """Sample from a log-normal distribution."""
    return np.random.lognormal(mean, std)

# ============================================================================
# DATA VALIDATION
# ============================================================================

def validate_email(email: str) -> bool:
    """Validate email format."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone: str) -> bool:
    """Validate phone number format."""
    import re
    pattern = r'^\+\d{10,15}$'
    return re.match(pattern, phone) is not None

def validate_date_range(date: datetime.date, start_date: datetime.date, end_date: datetime.date) -> bool:
    """Validate that date is within range."""
    return start_date <= date <= end_date

def validate_amount(amount: float) -> bool:
    """Validate that amount is positive."""
    return amount > 0

# ============================================================================
# FILE I/O UTILITIES
# ============================================================================

def ensure_directory_exists(directory: str) -> None:
    """Ensure directory exists, create if it doesn't."""
    os.makedirs(directory, exist_ok=True)

def save_json(data: Any, filepath: str, indent: int = 2) -> None:
    """Save data as JSON file."""
    ensure_directory_exists(os.path.dirname(filepath))
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=indent, default=str)

def load_json(filepath: str) -> Any:
    """Load data from JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def append_to_jsonl(data: Dict[str, Any], filepath: str) -> None:
    """Append data to JSONL file."""
    ensure_directory_exists(os.path.dirname(filepath))
    with open(filepath, 'a') as f:
        json.dump(data, f, default=str)
        f.write('\n')

# ============================================================================
# PROGRESS TRACKING
# ============================================================================

class ProgressTracker:
    """Simple progress tracker for data generation."""
    
    def __init__(self, total: int, description: str = "Processing"):
        self.total = total
        self.current = 0
        self.description = description
        self.last_percent = 0
    
    def update(self, increment: int = 1) -> None:
        """Update progress."""
        self.current += increment
        percent = int((self.current / self.total) * 100)
        
        if percent != self.last_percent and percent % 10 == 0:
            print(f"{self.description}: {percent}% ({self.current}/{self.total})")
            self.last_percent = percent
    
    def finish(self) -> None:
        """Mark as finished."""
        print(f"{self.description}: Complete ({self.current}/{self.total})")

# ============================================================================
# SUMMARY STATISTICS
# ============================================================================

def calculate_summary_stats(data: List[float]) -> Dict[str, float]:
    """Calculate summary statistics for a list of numbers."""
    if not data:
        return {}
    
    data_array = np.array(data)
    return {
        "count": len(data),
        "mean": float(np.mean(data_array)),
        "median": float(np.median(data_array)),
        "std": float(np.std(data_array)),
        "min": float(np.min(data_array)),
        "max": float(np.max(data_array)),
        "q25": float(np.percentile(data_array, 25)),
        "q75": float(np.percentile(data_array, 75))
    }

def print_validation_summary(metrics: Dict[str, Any]) -> None:
    """Print validation summary."""
    print("\n" + "="*60)
    print("DATA VALIDATION SUMMARY")
    print("="*60)
    
    for metric_name, value in metrics.items():
        if isinstance(value, dict):
            print(f"\n{metric_name.upper()}:")
            for key, val in value.items():
                print(f"  {key}: {val}")
        else:
            print(f"{metric_name}: {value}")
    
    print("="*60) 

class APIErrorType(Enum):
    """Types of API errors that can occur."""
    RATE_LIMIT = "rate_limit_error"
    INVALID_REQUEST = "invalid_request_error"
    AUTHENTICATION = "authentication_error"
    CARD_ERROR = "card_error"
    IDEMPOTENCY = "idempotency_error"
    API_CONNECTION = "api_connection_error"
    API_ERROR = "api_error"

@dataclass
class APIRequest:
    """Represents a simulated API request."""
    endpoint: str
    method: str
    payload: Dict[str, Any]
    timestamp: float
    request_id: str
    idempotency_key: Optional[str] = None

@dataclass 
class APIResponse:
    """Represents a simulated API response."""
    status_code: int
    data: Optional[Dict[str, Any]] = None
    error: Optional[Dict[str, Any]] = None
    headers: Dict[str, str] = field(default_factory=dict)
    request_id: str = ""
    processing_time_ms: int = 0

class RateLimiter:
    """Simulates Stripe's rate limiting."""
    
    def __init__(self, requests_per_second: int = 25):
        """
        Initialize rate limiter.
        
        Args:
            requests_per_second: Max requests per second (Stripe default is 25/sec)
        """
        self.requests_per_second = requests_per_second
        self.request_times: List[float] = []
        self.last_request_time = 0.0
    
    def should_rate_limit(self) -> bool:
        """Check if the next request should be rate limited."""
        current_time = time.time()
        
        # Clean up old request times (older than 1 second)
        self.request_times = [t for t in self.request_times if current_time - t < 1.0]
        
        # Check if we've exceeded the rate limit
        if len(self.request_times) >= self.requests_per_second:
            return True
            
        return False
    
    def add_request(self) -> None:
        """Record a new request."""
        self.request_times.append(time.time())
    
    def get_retry_after_seconds(self) -> float:
        """Get how long to wait before retrying."""
        if not self.request_times:
            return 0.0
        
        oldest_request = min(self.request_times)
        return max(0.0, 1.0 - (time.time() - oldest_request))

class APISimulator:
    """Simulates Stripe API behavior including rate limiting and errors."""
    
    def __init__(self, 
                 enable_rate_limiting: bool = True,
                 enable_random_errors: bool = True,
                 error_rate: float = 0.02,  # 2% error rate
                 delay_between_requests: float = 0.04,  # 40ms delay (25 req/sec)
                 use_real_api: bool = False,
                 stripe_api_key: Optional[str] = None):
        """
        Initialize API simulator.
        
        Args:
            enable_rate_limiting: Whether to simulate rate limiting
            enable_random_errors: Whether to simulate random API errors
            error_rate: Probability of random errors (0.0 - 1.0)
            delay_between_requests: Minimum delay between requests in seconds
            use_real_api: Whether to make real Stripe API calls
            stripe_api_key: Stripe API key for real API calls
        """
        self.enable_rate_limiting = enable_rate_limiting
        self.enable_random_errors = enable_random_errors
        self.error_rate = error_rate
        self.delay_between_requests = delay_between_requests
        self.use_real_api = use_real_api
        
        # Initialize Stripe API if using real API
        if use_real_api:
            if not STRIPE_AVAILABLE:
                raise ImportError("stripe library is required for real API calls. Install with: pip install stripe")
            if not stripe_api_key:
                raise ValueError("stripe_api_key is required for real API calls")
            stripe.api_key = stripe_api_key
            stripe.api_version = "2024-06-20"
        
        self.rate_limiter = RateLimiter()
        self.request_log: List[Tuple[APIRequest, APIResponse]] = []
        self.total_requests = 0
        self.successful_requests = 0
        self.failed_requests = 0
        self.retried_requests = 0
        
        # Enhanced tracking
        self.request_times: List[float] = []
        self.error_types: Dict[str, int] = {}
        self.endpoint_stats: Dict[str, Dict[str, Any]] = {}
        self.generation_start_time = time.time()
    
    def simulate_request(self, 
                        endpoint: str,
                        method: str,
                        payload: Dict[str, Any],
                        max_retries: int = 3) -> APIResponse:
        """
        Simulate a Stripe API request with rate limiting and error handling.
        
        Args:
            endpoint: API endpoint (e.g., "/v1/customers")
            method: HTTP method (e.g., "POST")
            payload: Request payload
            max_retries: Maximum number of retries
            
        Returns:
            APIResponse object
        """
        request_start_time = time.time()
        request = APIRequest(
            endpoint=endpoint,
            method=method,
            payload=payload,
            timestamp=request_start_time,
            request_id=f"req_{generate_stripe_id('', 16)}"
        )
        
        # Track endpoint statistics
        if endpoint not in self.endpoint_stats:
            self.endpoint_stats[endpoint] = {
                "total_requests": 0,
                "successful_requests": 0,
                "failed_requests": 0,
                "avg_response_time": 0.0
            }
        
        self.endpoint_stats[endpoint]["total_requests"] += 1
        
        for attempt in range(max_retries + 1):
            # Simulate delay between requests
            if self.delay_between_requests > 0:
                time.sleep(self.delay_between_requests)
            
            # Check rate limiting
            if self.enable_rate_limiting and self.rate_limiter.should_rate_limit():
                retry_after = self.rate_limiter.get_retry_after_seconds()
                response = APIResponse(
                    status_code=429,
                    error={
                        "type": APIErrorType.RATE_LIMIT.value,
                        "code": "rate_limit",
                        "message": "Too many requests. Please try again later.",
                        "param": None
                    },
                    headers={"Retry-After": str(int(retry_after))},
                    request_id=request.request_id
                )
                
                if attempt < max_retries:
                    self.retried_requests += 1
                    time.sleep(retry_after + 0.1)  # Wait a bit longer than required
                    continue
                else:
                    self.failed_requests += 1
                    self.endpoint_stats[endpoint]["failed_requests"] += 1
                    self._track_error("rate_limit_error")
                    self._log_request(request, response)
                    return response
            
            # Record successful rate limit check
            self.rate_limiter.add_request()
            
            # Make real API call if enabled
            if self.use_real_api:
                try:
                    response = self._make_real_api_call(request)
                    processing_time = time.time() - request_start_time
                    response.processing_time_ms = int(processing_time * 1000)
                    
                    if response.status_code < 400:
                        self.successful_requests += 1
                        self.endpoint_stats[endpoint]["successful_requests"] += 1
                    else:
                        self.failed_requests += 1
                        self.endpoint_stats[endpoint]["failed_requests"] += 1
                        if response.error:
                            self._track_error(response.error.get("type", "unknown"))
                    
                    self._log_request(request, response)
                    return response
                    
                except Exception as e:
                    # Handle real API errors
                    error_response = APIResponse(
                        status_code=500,
                        error={
                            "type": "api_error",
                            "code": "api_error",
                            "message": str(e),
                            "param": None
                        },
                        request_id=request.request_id
                    )
                    
                    if attempt < max_retries:
                        self.retried_requests += 1
                        time.sleep(2 ** attempt)  # Exponential backoff
                        continue
                    else:
                        self.failed_requests += 1
                        self.endpoint_stats[endpoint]["failed_requests"] += 1
                        self._track_error("api_error")
                        self._log_request(request, error_response)
                        return error_response
            
            # Simulate random errors (only if not using real API)
            if not self.use_real_api and self.enable_random_errors and random.random() < self.error_rate:
                error_type = random.choice([
                    APIErrorType.API_CONNECTION,
                    APIErrorType.API_ERROR,
                    APIErrorType.CARD_ERROR
                ])
                
                response = APIResponse(
                    status_code=400 if error_type == APIErrorType.CARD_ERROR else 500,
                    error={
                        "type": error_type.value,
                        "code": "api_error",
                        "message": f"Simulated {error_type.value}",
                        "param": None
                    },
                    request_id=request.request_id
                )
                
                if attempt < max_retries and error_type in [APIErrorType.API_CONNECTION, APIErrorType.API_ERROR]:
                    self.retried_requests += 1
                    time.sleep(2 ** attempt)  # Exponential backoff
                    continue
                else:
                    self.failed_requests += 1
                    self.endpoint_stats[endpoint]["failed_requests"] += 1
                    self._track_error(error_type.value)
                    self._log_request(request, response)
                    return response
            
            # Successful request
            processing_time = time.time() - request_start_time
            response = APIResponse(
                status_code=200,
                data=payload,  # In real scenario, this would be the created object
                request_id=request.request_id,
                processing_time_ms=int(processing_time * 1000)
            )
            
            self.successful_requests += 1
            self.endpoint_stats[endpoint]["successful_requests"] += 1
            self._log_request(request, response)
            return response
        
        # Should never reach here, but just in case
        self.failed_requests += 1
        self.endpoint_stats[endpoint]["failed_requests"] += 1
        return APIResponse(status_code=500, request_id=request.request_id)
    
    def _make_real_api_call(self, request: APIRequest) -> APIResponse:
        """Make a real Stripe API call."""
        if not self.use_real_api or not STRIPE_AVAILABLE:
            raise RuntimeError("Real API calls not available")
        
        try:
            # Convert full objects to API-safe payloads
            payload = self._convert_to_api_payload(request.endpoint, request.payload)
            
            # Map endpoints to Stripe API calls
            if request.endpoint == "/v1/customers" and request.method == "POST":
                result = stripe.Customer.create(**payload)
            elif request.endpoint == "/v1/products" and request.method == "POST":
                result = stripe.Product.create(**payload)
            elif request.endpoint == "/v1/prices" and request.method == "POST":
                result = stripe.Price.create(**payload)
            elif request.endpoint == "/v1/payment_methods" and request.method == "POST":
                # Special handling for payment methods - use pre-made test objects
                if payload.get("use_existing_payment_method"):
                    # Retrieve the pre-made PaymentMethod instead of creating a new one
                    pm_id = payload["payment_method_id"]
                    result = stripe.PaymentMethod.retrieve(pm_id)
                    
                    # Update the result with any custom metadata or billing details
                    if payload.get("metadata"):
                        result.metadata = payload["metadata"]
                    if payload.get("billing_details"):
                        # Note: We can't actually update billing details on pre-made objects
                        # but we can simulate it in the returned object
                        pass
                else:
                    result = stripe.PaymentMethod.create(**payload)
            elif request.endpoint.startswith("/v1/payment_methods/") and request.endpoint.endswith("/attach"):
                pm_id = request.endpoint.split("/")[3]
                result = stripe.PaymentMethod.attach(pm_id, **payload)
            elif request.endpoint == "/v1/subscriptions" and request.method == "POST":
                result = stripe.Subscription.create(**payload)
            elif request.endpoint == "/v1/invoices" and request.method == "POST":
                result = stripe.Invoice.create(**payload)
            elif request.endpoint == "/v1/charges" and request.method == "POST":
                result = stripe.Charge.create(**payload)
            elif request.endpoint == "/v1/payment_intents" and request.method == "POST":
                result = stripe.PaymentIntent.create(**payload)
            elif request.endpoint == "/v1/refunds" and request.method == "POST":
                result = stripe.Refund.create(**payload)
            elif request.endpoint == "/v1/disputes" and request.method == "POST":
                result = stripe.Dispute.create(**payload)
            elif request.endpoint == "/v1/invoice_items" and request.method == "POST":
                result = stripe.InvoiceItem.create(**payload)
            elif request.endpoint == "/v1/credit_notes" and request.method == "POST":
                result = stripe.CreditNote.create(**payload)
            elif request.endpoint == "/v1/tax_ids" and request.method == "POST":
                result = stripe.TaxId.create(**payload)
            else:
                raise ValueError(f"Unsupported endpoint: {request.endpoint}")
            
            return APIResponse(
                status_code=200,
                data=result,
                request_id=request.request_id
            )
            
        except stripe.error.StripeError as e:
            error_data = {
                "type": e.error.get("type", "api_error"),
                "code": e.error.get("code", "api_error"),
                "message": e.error.get("message", str(e)),
                "param": e.error.get("param")
            }
            
            return APIResponse(
                status_code=e.http_status,
                error=error_data,
                request_id=request.request_id
            )
    
    def _convert_to_api_payload(self, endpoint: str, full_object: Dict[str, Any]) -> Dict[str, Any]:
        """Convert a full Stripe object to an API-safe creation payload."""
        payload = {}
        
        if endpoint == "/v1/products":
            payload = {
                "name": full_object.get("name"),
                "description": full_object.get("description"),
                "type": full_object.get("type", "service"),
                "active": full_object.get("active", True),
                "metadata": full_object.get("metadata", {}),
                "statement_descriptor": full_object.get("statement_descriptor"),
                "unit_label": full_object.get("unit_label"),
                "url": full_object.get("url"),
                "images": full_object.get("images", []),
                "package_dimensions": full_object.get("package_dimensions"),
                "shippable": full_object.get("shippable"),
                "tax_code": full_object.get("tax_code")
            }
        elif endpoint == "/v1/prices":
            payload = {
                "currency": full_object.get("currency", "usd"),
                "product": full_object.get("product"),
                "unit_amount": full_object.get("unit_amount"),
                "active": full_object.get("active", True),
                "billing_scheme": full_object.get("billing_scheme", "per_unit"),
                "lookup_key": full_object.get("lookup_key"),
                "metadata": full_object.get("metadata", {}),
                "nickname": full_object.get("nickname"),
                "recurring": full_object.get("recurring"),
                "tax_behavior": full_object.get("tax_behavior"),
                "tiers_mode": full_object.get("tiers_mode"),
                "transform_quantity": full_object.get("transform_quantity"),
                "custom_unit_amount": full_object.get("custom_unit_amount")
            }
        elif endpoint == "/v1/customers":
            payload = {
                "email": full_object.get("email"),
                "name": full_object.get("name"),
                "phone": full_object.get("phone"),
                "description": full_object.get("description"),
                "metadata": full_object.get("metadata", {}),
                "address": full_object.get("address"),
                "shipping": full_object.get("shipping"),
                "tax_exempt": full_object.get("tax_exempt"),
                "preferred_locales": full_object.get("preferred_locales"),
                "invoice_prefix": full_object.get("invoice_prefix"),
                "next_invoice_sequence": full_object.get("next_invoice_sequence"),
                "balance": full_object.get("balance"),
                "cash_balance": full_object.get("cash_balance"),
                "coupon": full_object.get("coupon"),
                "default_source": full_object.get("default_source"),
                "invoice_settings": full_object.get("invoice_settings"),
                "payment_method": full_object.get("payment_method"),
                "promotional_code": full_object.get("promotional_code"),
                "source": full_object.get("source"),
                "tax_id_data": full_object.get("tax_id_data"),
                "test_clock": full_object.get("test_clock")
            }
        elif endpoint == "/v1/payment_methods":
            # For payment methods, we need to use pre-made test PaymentMethod objects
            # instead of creating new ones with card numbers, as raw card data is not allowed
            card_brand = "visa"  # Default to visa
            if "card" in full_object and full_object["card"]:
                card_brand = full_object["card"].get("brand", "visa")
            
            # Map card brands to pre-made PaymentMethod test objects
            test_payment_methods = {
                "visa": "pm_card_visa",
                "mastercard": "pm_card_mastercard", 
                "amex": "pm_card_amex",
                "discover": "pm_card_discover"
            }
            
            # Store the pre-made PaymentMethod ID in the payload for special handling
            payload = {
                "use_existing_payment_method": True,
                "payment_method_id": test_payment_methods.get(card_brand, "pm_card_visa"),
                "card_brand": card_brand,
                "billing_details": full_object.get("billing_details", {}),
                "metadata": full_object.get("metadata", {})
            }
        elif endpoint.startswith("/v1/payment_methods/") and endpoint.endswith("/attach"):
            payload = {
                "customer": full_object.get("customer")
            }
        elif endpoint == "/v1/subscriptions":
            payload = {
                "customer": full_object.get("customer"),
                "currency": full_object.get("currency", "usd"),
                "description": full_object.get("description"),
                "metadata": full_object.get("metadata", {}),
                "payment_behavior": full_object.get("payment_behavior"),
                "payment_settings": full_object.get("payment_settings"),
                "pending_invoice_item_interval": full_object.get("pending_invoice_item_interval"),
                "promotion_code": full_object.get("promotion_code"),
                "proration_behavior": full_object.get("proration_behavior"),
                "transfer_data": full_object.get("transfer_data"),
                "trial_end": full_object.get("trial_end"),
                "trial_period_days": full_object.get("trial_period_days"),
                "default_payment_method": full_object.get("default_payment_method"),
                "default_source": full_object.get("default_source"),
                "default_tax_rates": full_object.get("default_tax_rates"),
                "collection_method": full_object.get("collection_method"),
                "billing_cycle_anchor": full_object.get("billing_cycle_anchor"),
                "cancel_at": full_object.get("cancel_at"),
                "cancel_at_period_end": full_object.get("cancel_at_period_end"),
                "days_until_due": full_object.get("days_until_due"),
                "automatic_tax": full_object.get("automatic_tax"),
                "billing_thresholds": full_object.get("billing_thresholds"),
                "coupon": full_object.get("coupon"),
                "off_session": full_object.get("off_session"),
                "on_behalf_of": full_object.get("on_behalf_of")
            }
            
            # Handle items array - convert from full object structure to API format
            if "items" in full_object and full_object["items"]:
                items_obj = full_object["items"]
                if isinstance(items_obj, dict) and "data" in items_obj:
                    # Convert from response format to creation format
                    api_items = []
                    for item in items_obj["data"]:
                        if "price" in item and isinstance(item["price"], dict):
                            api_items.append({
                                "price": item["price"]["id"],
                                "quantity": item.get("quantity", 1)
                            })
                    payload["items"] = api_items
                elif isinstance(items_obj, list):
                    # Already in the right format
                    payload["items"] = items_obj
        elif endpoint == "/v1/invoices":
            payload = {
                "customer": full_object.get("customer"),
                "currency": full_object.get("currency", "usd"),
                "description": full_object.get("description"),
                "metadata": full_object.get("metadata", {}),
                "subscription": full_object.get("subscription"),
                "auto_advance": full_object.get("auto_advance"),
                "collection_method": full_object.get("collection_method"),
                "custom_fields": full_object.get("custom_fields"),
                "days_until_due": full_object.get("days_until_due"),
                "default_payment_method": full_object.get("default_payment_method"),
                "default_source": full_object.get("default_source"),
                "default_tax_rates": full_object.get("default_tax_rates"),
                "footer": full_object.get("footer"),
                "rendering_options": full_object.get("rendering_options"),
                "statement_descriptor": full_object.get("statement_descriptor"),
                "transfer_data": full_object.get("transfer_data"),
                "application_fee_amount": full_object.get("application_fee_amount"),
                "discounts": full_object.get("discounts"),
                "due_date": full_object.get("due_date"),
                "on_behalf_of": full_object.get("on_behalf_of"),
                "payment_settings": full_object.get("payment_settings")
            }
        elif endpoint == "/v1/charges":
            payload = {
                "amount": full_object.get("amount"),
                "currency": full_object.get("currency", "usd"),
                "customer": full_object.get("customer"),
                "description": full_object.get("description"),
                "metadata": full_object.get("metadata", {}),
                "payment_method": full_object.get("payment_method"),
                "receipt_email": full_object.get("receipt_email"),
                "shipping": full_object.get("shipping"),
                "source": full_object.get("source"),
                "statement_descriptor": full_object.get("statement_descriptor"),
                "statement_descriptor_suffix": full_object.get("statement_descriptor_suffix"),
                "application_fee_amount": full_object.get("application_fee_amount"),
                "capture": full_object.get("capture"),
                "on_behalf_of": full_object.get("on_behalf_of"),
                "radar_options": full_object.get("radar_options"),
                "transfer_data": full_object.get("transfer_data"),
                "transfer_group": full_object.get("transfer_group")
            }
        elif endpoint == "/v1/payment_intents":
            payload = {
                "amount": full_object.get("amount"),
                "currency": full_object.get("currency", "usd"),
                "customer": full_object.get("customer"),
                "description": full_object.get("description"),
                "metadata": full_object.get("metadata", {}),
                "payment_method": full_object.get("payment_method"),
                "receipt_email": full_object.get("receipt_email"),
                "shipping": full_object.get("shipping"),
                "statement_descriptor": full_object.get("statement_descriptor"),
                "statement_descriptor_suffix": full_object.get("statement_descriptor_suffix"),
                "application_fee_amount": full_object.get("application_fee_amount"),
                "capture_method": full_object.get("capture_method"),
                "confirm": full_object.get("confirm"),
                "confirmation_method": full_object.get("confirmation_method"),
                "error_on_requires_action": full_object.get("error_on_requires_action"),
                "mandate": full_object.get("mandate"),
                "mandate_data": full_object.get("mandate_data"),
                "off_session": full_object.get("off_session"),
                "on_behalf_of": full_object.get("on_behalf_of"),
                "payment_method_data": full_object.get("payment_method_data"),
                "payment_method_options": full_object.get("payment_method_options"),
                "payment_method_types": full_object.get("payment_method_types"),
                "radar_options": full_object.get("radar_options"),
                "return_url": full_object.get("return_url"),
                "setup_future_usage": full_object.get("setup_future_usage"),
                "transfer_data": full_object.get("transfer_data"),
                "transfer_group": full_object.get("transfer_group"),
                "use_stripe_sdk": full_object.get("use_stripe_sdk")
            }
        elif endpoint == "/v1/refunds":
            payload = {
                "charge": full_object.get("charge"),
                "amount": full_object.get("amount"),
                "metadata": full_object.get("metadata", {}),
                "reason": full_object.get("reason"),
                "refund_application_fee": full_object.get("refund_application_fee"),
                "reverse_transfer": full_object.get("reverse_transfer"),
                "payment_intent": full_object.get("payment_intent"),
                "instructions_email": full_object.get("instructions_email"),
                "origin": full_object.get("origin")
            }
        elif endpoint == "/v1/disputes":
            payload = {
                "charge": full_object.get("charge"),
                "metadata": full_object.get("metadata", {}),
                "evidence": full_object.get("evidence"),
                "submit": full_object.get("submit")
            }
        elif endpoint == "/v1/invoice_items":
            payload = {
                "customer": full_object.get("customer"),
                "amount": full_object.get("amount"),
                "currency": full_object.get("currency", "usd"),
                "description": full_object.get("description"),
                "metadata": full_object.get("metadata", {}),
                "invoice": full_object.get("invoice"),
                "price": full_object.get("price"),
                "price_data": full_object.get("price_data"),
                "subscription": full_object.get("subscription"),
                "tax_rates": full_object.get("tax_rates"),
                "discountable": full_object.get("discountable"),
                "discounts": full_object.get("discounts"),
                "period": full_object.get("period"),
                "tax_behavior": full_object.get("tax_behavior")
            }
            
            # Only include quantity if amount is not specified (Stripe API constraint)
            if not full_object.get("amount"):
                payload["quantity"] = full_object.get("quantity")
        elif endpoint == "/v1/credit_notes":
            payload = {
                "invoice": full_object.get("invoice"),
                "amount": full_object.get("amount"),
                "credit_amount": full_object.get("credit_amount"),
                "metadata": full_object.get("metadata", {}),
                "memo": full_object.get("memo"),
                "reason": full_object.get("reason"),
                "refund_amount": full_object.get("refund_amount"),
                "lines": full_object.get("lines"),
                "out_of_band_amount": full_object.get("out_of_band_amount"),
                "shipping_cost": full_object.get("shipping_cost")
            }
        elif endpoint == "/v1/tax_ids":
            payload = {
                "customer": full_object.get("customer"),
                "type": full_object.get("type"),
                "value": full_object.get("value")
            }
        else:
            # For other endpoints, just filter out common response-only fields
            excluded_fields = {
                "id", "object", "created", "updated", "livemode", "url", 
                "invoice_pdf", "hosted_invoice_url", "receipt_url", "status",
                "last_finalization_error", "features", "default_price"
            }
            payload = {k: v for k, v in full_object.items() if k not in excluded_fields}
        
        # Remove None values to avoid sending unnecessary parameters
        return {k: v for k, v in payload.items() if v is not None}
    
    def _track_error(self, error_type: str) -> None:
        """Track error types for statistics."""
        self.error_types[error_type] = self.error_types.get(error_type, 0) + 1
    
    def _log_request(self, request: APIRequest, response: APIResponse) -> None:
        """Log the request and response."""
        self.request_log.append((request, response))
        self.total_requests += 1
        self.request_times.append(response.processing_time_ms)
        
        # Update endpoint average response time
        endpoint = request.endpoint
        if endpoint in self.endpoint_stats:
            current_avg = self.endpoint_stats[endpoint]["avg_response_time"]
            total_requests = self.endpoint_stats[endpoint]["total_requests"]
            new_avg = ((current_avg * (total_requests - 1)) + response.processing_time_ms) / total_requests
            self.endpoint_stats[endpoint]["avg_response_time"] = new_avg
    
    def get_stats(self) -> Dict[str, Any]:
        """Get API simulation statistics."""
        total_time = time.time() - self.generation_start_time
        
        return {
            "total_requests": self.total_requests,
            "successful_requests": self.successful_requests,
            "failed_requests": self.failed_requests,
            "retried_requests": self.retried_requests,
            "success_rate": self.successful_requests / max(1, self.total_requests),
            "error_rate": self.failed_requests / max(1, self.total_requests),
            "retry_rate": self.retried_requests / max(1, self.total_requests),
            "total_generation_time": total_time,
            "requests_per_second": self.total_requests / max(1, total_time),
            "avg_response_time_ms": sum(self.request_times) / max(1, len(self.request_times)),
            "error_breakdown": self.error_types,
            "endpoint_stats": self.endpoint_stats,
            "using_real_api": self.use_real_api
        }
    
    def get_failed_requests(self) -> List[Tuple[APIRequest, APIResponse]]:
        """Get all failed requests for analysis."""
        return [(req, resp) for req, resp in self.request_log if resp.status_code >= 400]
    
    def save_detailed_log(self, filepath: str) -> None:
        """Save detailed request log to file."""
        log_data = []
        for request, response in self.request_log:
            log_entry = {
                "request": {
                    "endpoint": request.endpoint,
                    "method": request.method,
                    "timestamp": request.timestamp,
                    "request_id": request.request_id
                },
                "response": {
                    "status_code": response.status_code,
                    "processing_time_ms": response.processing_time_ms,
                    "error": response.error,
                    "request_id": response.request_id
                }
            }
            log_data.append(log_entry)
        
        with open(filepath, 'w') as f:
            json.dump(log_data, f, indent=2, default=str)
    
    def get_generation_summary(self) -> Dict[str, Any]:
        """Get a comprehensive generation summary."""
        stats = self.get_stats()
        failed_requests = self.get_failed_requests()
        
        return {
            "generation_summary": {
                "total_time_seconds": stats["total_generation_time"],
                "total_requests": stats["total_requests"],
                "throughput_rps": stats["requests_per_second"],
                "success_rate": f"{stats['success_rate']:.2%}",
                "using_real_stripe_api": stats["using_real_api"]
            },
            "performance_metrics": {
                "avg_response_time_ms": stats["avg_response_time_ms"],
                "successful_requests": stats["successful_requests"],
                "failed_requests": stats["failed_requests"],
                "retried_requests": stats["retried_requests"]
            },
            "error_analysis": {
                "error_breakdown": stats["error_breakdown"],
                "failed_request_sample": [
                    {
                        "endpoint": req.endpoint,
                        "method": req.method,
                        "error_type": resp.error.get("type", "unknown") if resp.error else "unknown",
                        "error_message": resp.error.get("message", "No message") if resp.error else "No message"
                    }
                    for req, resp in failed_requests[:10]  # First 10 failed requests
                ]
            },
            "endpoint_performance": stats["endpoint_stats"]
        } 