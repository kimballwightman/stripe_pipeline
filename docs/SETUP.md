# Stripe Analytics Pipeline Setup Guide

This guide walks you through setting up the complete end-to-end analytics pipeline for Stripe data.

## 📋 Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Google Cloud Platform account with BigQuery enabled
- Stripe test account
- Git and GitHub account

## 🔧 Environment Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd stripe_pipeline
```

### 2. Environment Variables

Copy the example environment file and configure your settings:

```bash
cp .env.example .env
```

Edit `.env` with your actual values:

```bash
# Stripe API Configuration
STRIPE_API_SECRET_KEY=sk_test_your_secret_key_here
STRIPE_API_PUBLISHABLE_KEY=pk_test_your_publishable_key_here

# GCP Configuration
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service-account-key.json
DBT_PROJECT_ID=your-gcp-project-id

# Environment Configuration
DBT_DATASET=stripe_dev  # Use stripe_dev for development
DBT_TARGET=dev
ENVIRONMENT=development
```

### 3. Google Cloud Setup

1. Create a GCP project
2. Enable BigQuery API
3. Create a service account with BigQuery Admin permissions
4. Download the service account key JSON file
5. Update `GOOGLE_APPLICATION_CREDENTIALS` in `.env`

### 4. BigQuery Datasets

Create the required datasets in BigQuery:

```sql
-- Development dataset
CREATE SCHEMA IF NOT EXISTS `your-project-id.stripe_dev`;

-- Production dataset (optional for now)
CREATE SCHEMA IF NOT EXISTS `your-project-id.stripe_prod`;
```

## 🚀 Running the Pipeline

### Option 1: Step-by-Step (Recommended for First Run)

#### Step 1: Generate Stripe Data

```bash
cd generate_stripe_data
python -m pip install -r requirements.txt
python main.py --no-api-sim
```

#### Step 2: Run Data Ingestion

```bash
cd ../ingestion
python -m pip install -r requirements.txt
python ingestion.py
```

#### Step 3: Run dbt Transformations

```bash
cd ../dbt/stripe_analytics
dbt deps
dbt debug
dbt run --select staging
dbt test --select staging
```

### Option 2: Using Airflow (Full Orchestration)

#### Start Airflow

```bash
cd airflow
export AIRFLOW_UID=$(id -u)
docker-compose up -d
```

#### Access Airflow UI

- URL: http://localhost:8080
- Username: `airflow`
- Password: `airflow`

#### Run the Pipeline

1. Navigate to the Airflow UI
2. Find the `stripe_data_pipeline` DAG
3. Enable the DAG
4. Trigger a manual run

## 📊 dbt Development

### Local Development

```bash
cd dbt/stripe_analytics

# Install dependencies
dbt deps

# Test connection
dbt debug

# Run models
dbt run

# Run tests
dbt test

# Generate documentation
dbt docs generate
dbt docs serve
```

### Model Structure

```
models/
├── staging/          # Clean and normalize raw data
│   ├── stg_customers.sql
│   ├── stg_subscriptions.sql
│   └── sources.yml
├── intermediate/     # Business logic transformations
├── dimensions/       # Slowly changing dimensions
├── facts/           # Event-level data
└── marts/           # Final business metrics
```

## 🔄 CI/CD Setup

### GitHub Secrets

Add the following secrets to your GitHub repository:

```
GCP_SERVICE_ACCOUNT_KEY         # Dev service account JSON
GCP_SERVICE_ACCOUNT_KEY_PROD    # Prod service account JSON (optional)
DBT_PROJECT_ID                  # Your GCP project ID
```

### Branch Strategy

- `main`: Production environment
- `dev`: Development environment
- `feature/*`: Feature branches

### Workflow

1. Create feature branch from `dev`
2. Make changes and commit
3. Open PR to `dev` → triggers CI tests
4. Merge to `dev` → deploys to dev environment
5. Open PR from `dev` to `main` → triggers CI tests
6. Merge to `main` → deploys to production

## 🧪 Testing

### Data Generation Tests

```bash
cd generate_stripe_data
python test_implementation.py
```

### Ingestion Tests

```bash
cd ingestion
python -m pytest tests/  # (if tests exist)
```

### dbt Tests

```bash
cd dbt/stripe_analytics
dbt test
```

## 📈 Monitoring

### Airflow Monitoring

- Check DAG runs in Airflow UI
- Monitor task logs for errors
- Set up email alerts (optional)

### dbt Monitoring

- Review dbt test results
- Monitor model freshness
- Check data quality metrics

### BigQuery Monitoring

- Monitor query performance
- Check dataset costs
- Review data lineage

## 🔍 Troubleshooting

### Common Issues

1. **BigQuery Authentication Error**
   - Verify service account key path
   - Check service account permissions
   - Ensure BigQuery API is enabled

2. **dbt Connection Error**
   - Run `dbt debug` to diagnose
   - Check profiles.yml configuration
   - Verify environment variables

3. **Airflow Task Failures**
   - Check task logs in Airflow UI
   - Verify volume mounts in docker-compose.yml
   - Check environment variables

### Debugging Commands

```bash
# Check dbt connection
dbt debug

# Validate dbt models
dbt compile

# Check BigQuery tables
bq ls stripe_dev

# Check Airflow logs
docker-compose logs airflow-scheduler
```

## 📚 Next Steps

1. **Add More Models**: Create intermediate, dimension, fact, and mart models
2. **Implement Testing**: Add comprehensive dbt tests
3. **Set Up Monitoring**: Configure alerting and observability
4. **Create Dashboards**: Build stakeholder-facing analytics
5. **Optimize Performance**: Tune BigQuery queries and dbt models

## 🆘 Support

- Check the [dbt documentation](https://docs.getdbt.com/)
- Review [Airflow documentation](https://airflow.apache.org/docs/)
- Consult [BigQuery documentation](https://cloud.google.com/bigquery/docs)
- Open an issue in this repository for project-specific questions 