# Stripe Data Generator

A comprehensive Python tool for generating realistic Stripe API data for analytics engineering and testing purposes. This tool simulates a complete SaaS business with customers, subscriptions, payments, refunds, and disputes across multiple geographic regions.

## 🆕 New Features

### Real Stripe API Integration
- **Live API Calls**: Option to use real Stripe API instead of simulation
- **Environment Variables**: Secure API key management via .env file
- **Rate Limiting**: Respects Stripe's 25 requests/second rate limit
- **Error Handling**: Proper handling of real Stripe API errors and retries

### Enhanced API Simulation
- **Rate Limiting**: Simulates Stripe's 25 requests/second rate limit
- **Error Handling**: Simulates real API errors with exponential backoff retry logic
- **Request Tracking**: Comprehensive logging of all API requests and responses
- **Performance Metrics**: Detailed statistics on throughput, response times, and errors

### Comprehensive Tracking
- **Success/Failure Tracking**: Detailed logs of all generation attempts
- **Endpoint Statistics**: Performance metrics per API endpoint
- **Error Analysis**: Breakdown of error types and frequencies
- **Generation Summary**: Complete audit trail of the generation process

### Enhanced Schema Compliance
- **Complete Object Schemas**: All objects now include every field from Stripe API documentation
- **Nullable Fields**: Proper handling of nullable vs required fields
- **Nested Objects**: Full support for complex nested object structures
- **API Versioning**: Objects match the latest Stripe API version

## 🚀 Quick Start

### Basic Usage (No API Simulation)
```bash
python main.py --no-api-sim
```

### With Rate Limiting (Realistic API Behavior)
```bash
python main.py --rate-limit
```

### With Error Simulation (Testing Resilience)
```bash
python main.py --rate-limit --errors --error-rate 0.05
```

### Real Stripe API (Recommended for Production)
```bash
python main.py --real-api --rate-limit
```

### Fast Development Mode
```bash
python main.py --no-rate-limit
```

## 📋 Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--no-api-sim` | Disable API simulation (fastest) | False |
| `--rate-limit` | Enable rate limiting simulation | True |
| `--no-rate-limit` | Disable rate limiting | False |
| `--errors` | Enable random API errors | False |
| `--error-rate` | Error rate (0.0-1.0) | 0.01 |
| `--real-api` | Use real Stripe API | False |
| `--output-dir` | Output directory | "output" |

## 🔧 Environment Setup

### Required Environment Variables
Create a `.env` file in your project root:

```bash
# Stripe API Configuration
STRIPE_API_SECRET_KEY=sk_test_your_secret_key_here
STRIPE_API_PUBLISHABLE_KEY=pk_test_your_publishable_key_here
STRIPE_API_URL=https://api.stripe.com/v1

# Optional: Other configurations
# GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account.json
# DBT_PROJECT_ID=your-gcp-project-id
```

### API Key Requirements
- **Simulation Mode**: No API key required
- **Real API Mode**: `STRIPE_API_SECRET_KEY` must be set in `.env`
- **Test vs Live**: Use test keys (`sk_test_*`) for development

## 🏗️ Architecture

### API Integration Framework
- **Real API Mode**: Makes actual calls to Stripe API with proper authentication
- **Simulation Mode**: Mimics API behavior without external calls
- **Rate Limiter**: Enforces Stripe's 25 requests/second limit
- **Error Handler**: Implements exponential backoff for failed requests
- **Request Logger**: Comprehensive logging of all API interactions

### Data Generation Flow
1. **Products & Prices**: Create SaaS plan structure
2. **Customers**: Generate realistic customer profiles
3. **Payment Methods**: Attach cards and ACH to customers
4. **Subscriptions**: Simulate trial → paid → churn lifecycle
5. **Invoices & Payments**: Generate billing events
6. **Refunds & Disputes**: Simulate payment issues

### Schema Compliance
- **Stripe API v2024**: All objects match latest API documentation
- **Field Completeness**: Every documented field is included
- **Type Safety**: Proper typing for all data structures
- **Validation**: Built-in validation against industry benchmarks

## 📊 Generated Objects

### Core Resources
- **Customers**: Complete customer profiles with addresses, metadata
- **Payment Methods**: Cards and ACH with realistic failure rates
- **Charges**: Payment transactions with success/failure states
- **Refunds**: Partial and full refunds with proper timing
- **Disputes**: Chargeback simulation with resolution states

### Billing Objects
- **Subscriptions**: Full lifecycle from trial to churn
- **Invoices**: Detailed billing with line items
- **Invoice Items**: Individual charges and credits
- **Payment Intents**: Modern payment flow objects
- **Balance Transactions**: Complete transaction ledger
- **Credit Notes**: Refund documentation

### Product Catalog
- **Products**: SaaS plan definitions (Basic, Pro, Enterprise)
- **Prices**: Multiple billing intervals (monthly, yearly)

## 🎯 Business Model Simulation

### SaaS Metrics
- **Plans**: Basic ($20/mo), Pro ($50/mo), Enterprise ($200/mo)
- **Trial Period**: 30-day free trial
- **Conversion Rates**: Realistic by geography and plan
- **Churn Rates**: Industry-standard retention curves
- **Payment Mix**: 80% cards, 20% ACH

### Geographic Distribution
- **North America**: 60% of customers
- **EMEA**: 25% of customers  
- **APAC**: 15% of customers
- **Localization**: Currency, payment methods, tax handling

### Industry Benchmarks
- **Trial Conversion**: 15-30% (varies by region)
- **Monthly Churn**: 2-8% (varies by plan)
- **Refund Rate**: 1-3% of charges
- **Dispute Rate**: 0.1-0.5% of charges

## 🔧 Configuration

### Business Parameters
Edit `config.py` to adjust:
- Customer volume and growth patterns
- Plan pricing and features
- Geographic distribution
- Conversion and churn rates
- Stripe API settings

### API Configuration
```python
# Environment variables (set in .env)
STRIPE_API_SECRET_KEY = "sk_test_..."
STRIPE_API_PUBLISHABLE_KEY = "pk_test_..."
STRIPE_API_URL = "https://api.stripe.com/v1"

# Rate limiting
STRIPE_RATE_LIMIT_REQUESTS_PER_SECOND = 25
STRIPE_MAX_RETRIES = 3
STRIPE_RETRY_DELAY = 1.0
```

## 📈 Output Files

### Generated Data
```
output/
├── customers.json              # Customer profiles
├── products.json              # Product catalog
├── prices.json                # Pricing tiers
├── payment_methods.json       # Payment instruments
├── subscriptions.json         # Subscription records
├── subscription_events.json   # Lifecycle events
├── invoices.json              # Billing documents
├── charges.json               # Payment transactions
├── payment_intents.json       # Payment flow objects
├── balance_transactions.json  # Transaction ledger
├── refunds.json               # Refund records
├── disputes.json              # Chargeback data
└── credit_notes.json          # Credit documentation
```

### Tracking & Analytics
```
output/
├── api_statistics.json        # API performance metrics
├── api_request_log.json       # Detailed request/response log
├── generation_summary.json    # Comprehensive generation report
├── validation_metrics.json    # Data quality validation
└── basic_summary.json         # Quick overview
```

## 📊 Success/Failure Tracking

### API Request Tracking
- **Request ID**: Unique identifier for each API call
- **Endpoint**: Target API endpoint
- **Method**: HTTP method (POST, GET, etc.)
- **Status Code**: HTTP response status
- **Response Time**: Processing time in milliseconds
- **Error Details**: Complete error information for failures

### Performance Metrics
- **Success Rate**: Percentage of successful requests
- **Error Rate**: Percentage of failed requests
- **Retry Rate**: Percentage of requests that required retries
- **Throughput**: Requests per second
- **Average Response Time**: Mean processing time

### Error Analysis
- **Error Types**: Breakdown by error category
- **Failed Endpoints**: Which endpoints had issues
- **Retry Patterns**: How many retries were needed
- **Recovery Rate**: Percentage of retries that succeeded

## 🧪 Testing Scenarios

### Development Testing
```bash
# Fast iteration (no API calls)
python main.py --no-api-sim

# Quick validation with minimal rate limiting
python main.py --no-rate-limit

# Simulated API with errors
python main.py --rate-limit --errors --error-rate 0.05
```

### Production Simulation
```bash
# Real Stripe API (recommended)
python main.py --real-api --rate-limit

# Stress testing with high error rate
python main.py --real-api --rate-limit --errors --error-rate 0.1
```

### Data Pipeline Testing
```bash
# Generate to custom directory
python main.py --real-api --output-dir /path/to/pipeline/input
```

## 🔍 Validation & Quality

### Automated Validation
- **Schema Validation**: Every object validated against Stripe API
- **Business Rules**: Conversion rates within industry ranges
- **Data Consistency**: Cross-object relationships maintained
- **Temporal Logic**: Event sequences follow realistic timing

### Quality Metrics
- **Completeness**: All required fields populated
- **Realism**: Values follow real-world distributions
- **Consistency**: Related objects have matching data
- **Compliance**: Objects pass Stripe API validation

### Generation Reports
- **Success Summary**: Overview of successful generation
- **Failure Analysis**: Detailed breakdown of any issues
- **Performance Report**: API call statistics and timing
- **Data Quality**: Validation results and recommendations

## 🛠️ Development

### Adding New Objects
1. Study Stripe API documentation for the object
2. Create generator class following existing patterns
3. Add API simulation support
4. Include comprehensive field mapping
5. Add validation logic

### Extending Business Logic
1. Update `config.py` with new parameters
2. Modify generator logic for new scenarios
3. Add validation for new metrics
4. Update documentation

## 📚 Dependencies

- `numpy>=1.21.0`: Statistical distributions and calculations
- `stripe>=7.0.0`: Official Stripe Python library
- `dataclasses>=0.6`: For Python < 3.7 compatibility (API simulation)

## 🎯 Use Cases

### Analytics Engineering
- **dbt Development**: Realistic data for model development
- **Dashboard Testing**: Rich datasets for visualization
- **Metric Validation**: Industry-standard KPIs and benchmarks

### Data Engineering
- **Pipeline Testing**: Realistic data volumes and schemas
- **Error Handling**: Test resilience with simulated API failures
- **Performance Testing**: Large datasets with proper relationships

### Business Intelligence
- **Cohort Analysis**: Multi-year customer lifecycle data
- **Revenue Modeling**: Subscription and usage-based billing
- **Churn Prediction**: Historical patterns for ML training

### API Integration Testing
- **Rate Limiting**: Test application behavior under API limits
- **Error Handling**: Validate retry logic and error recovery
- **Authentication**: Test API key management and security

## 🚨 Important Notes

### Security
- **API Keys**: Never commit API keys to version control
- **Environment Variables**: Always use `.env` files for secrets
- **Test Keys**: Use test keys (`sk_test_*`) for development
- **Production**: Use live keys (`sk_live_*`) only in production

### Rate Limiting
- **Stripe Limits**: 25 requests/second by default
- **Backoff Strategy**: Exponential backoff for failed requests
- **Monitoring**: Track API usage to avoid hitting limits
- **Optimization**: Batch operations when possible

### Data Privacy
- **Simulated Data**: All generated data is fictional
- **No PII**: No real personal information is used
- **Compliance**: Follows data protection best practices

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add comprehensive tests
4. Update documentation
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details.

## 🔗 Related Projects

- [Stripe API Documentation](https://docs.stripe.com/api)
- [dbt Analytics Engineering](https://www.getdbt.com/)
- [Stripe Sample Data](https://github.com/stripe-samples)

---

*This tool generates simulated data for development and testing purposes only. It is not affiliated with Stripe Inc.* 