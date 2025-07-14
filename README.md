# SaaS Funnel Analytics Project: End-to-End Stripe Data Pipeline

## 🚀 Project Overview
This project simulates a modern B2C SaaS business and builds a full-stack, end-to-end analytics pipeline using Stripe data. It demonstrates advanced Analytics Engineering skills by covering the entire data lifecycle: from data generation and ingestion, through orchestration, modeling, testing, CI/CD, and stakeholder-facing dashboards.

**Key Business Goal:** Deliver actionable funnel, revenue, and retention insights to Product, Growth, and Finance teams using a scalable, production-grade data stack.

---

## 🧩 Problem Statement
Stakeholders lack unified, timely visibility into the SaaS customer lifecycle—from acquisition to activation, subscription, revenue, and churn. This project solves that by building a robust analytics platform on real (simulated) Stripe data.

---

## 🎯 Project Objectives
- Ingest Stripe data via API into Google BigQuery
- Orchestrate jobs with Airflow (Dockerized)
- Transform data using dbt Core (Star schema)
- Implement robust testing, CI/CD, and observability
- Deliver dashboards tracking core SaaS metrics
- Simulate a realistic SaaS funnel and monetization model

---

## ⚙️ Tech Stack
| Layer           | Tools/Technologies                |
|-----------------|-----------------------------------|
| Ingestion       | Python, Stripe API, Docker         |
| Orchestration   | Airflow (Docker)                  |
| Data Warehouse  | Google BigQuery                   |
| Modeling        | dbt Core (Star schema)           |
| Testing         | dbt tests, dbt-expectations       |
| CI/CD           | GitHub Actions, dbt Core         |
| Observability   | dbt Docs, Slack alerts            |
| Dashboarding    | Streamlit, Hex, or Metabase       |

---

## 🧱 Architecture
```
Stripe API (simulated data)
    ↓
Python ingestion (Docker)
    ↓
Google BigQuery (raw tables)
    ↓
Airflow DAGs (scheduled)
    ↓
dbt Transformations (staging → int → marts, star schema)
    ↓
Tests, CI/CD, docs, observability
    ↓
Stakeholder Dashboards
```

---

## 📊 Core Metrics & Dimensions
- **Metrics:** Signups, Trial Starts, Paid Conversions, MRR, ARR, Churn Rate, LTV, CAC (simulated), Retention, Cohorts, Refunds, Disputes
- **Dimensions:** Product/Plan, Acquisition Channel, Geography, Subscription Status, Cohort, Payment Method

---

## 🏗️ Data Modeling (dbt Star Schema)
- **Staging Models:** Clean and normalize raw Stripe objects (customers, subscriptions, invoices, etc.)
- **Dimension Models:** Customer, Product, Price, Subscription, Payment Method, Date
- **Fact Models:** Subscription Events, Invoices, Payments, Refunds, Disputes, Customer Balance Transactions, Credit Notes

---

## 🧠 Data Generation Strategy
- Simulate realistic SaaS user behavior and billing events in Stripe's test environment
- Generate new data on a regular cadence (via Airflow) to mimic real business growth, churn, and seasonality
- Use industry benchmarks and exogenous variables to drive trends and inflection points

---

## 📈 Dashboards & Insights
- Funnel visualizations (signup → paid → retained)
- MRR, ARR, churn, and LTV over time
- Retention curves and cohort analysis
- Revenue by product, plan, and channel
- CAC vs. LTV by channel (using simulated ad spend)

---

## 👥 Stakeholder Personas
- **Product:** Feature engagement, usage conversion
- **Growth:** Funnel conversion, CAC/LTV
- **Finance/RevOps:** MRR, ARR, invoice health, revenue forecasting
- **Customer Success:** Churn, retention, upsell moments

---

## 🏆 Why This Project Stands Out
- Realistic, large-scale simulated data
- Business-ready, stakeholder-focused models
- Modern engineering stack and best practices
- Robust testing, CI/CD, and observability
- Clear documentation and data lineage

---

## 📝 Getting Started
1. Clone the repo and follow setup instructions in `/setup/`
2. Configure your Stripe test account and BigQuery credentials
3. Run the Dockerized ingestion pipeline
4. Deploy Airflow and schedule DAGs
5. Set up dbt Core and run models/tests
6. Launch dashboards and explore insights

---

## 📚 More Info
- See `/stripe_api_docs/README.md` for Stripe object coverage
- See `/dbt/` for data models and lineage
- See `/docs/` for business logic and metric definitions

---

**Questions?** Open an issue or reach out on LinkedIn!
