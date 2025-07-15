{{ config(
    materialized='view',
    description='Staging model for Stripe subscriptions - cleans and normalizes raw subscription data'
) }}

with raw_subscriptions as (
    select * from {{ source('stripe_raw', 'subscriptions') }}
),

cleaned_subscriptions as (
    select
        -- Primary key
        id as subscription_id,
        
        -- Basic subscription information
        object,
        customer as customer_id,
        status as subscription_status,
        description as subscription_description,
        
        -- Billing information
        collection_method,
        currency,
        billing_cycle_anchor,
        current_period_start,
        current_period_end,
        days_until_due,
        
        -- Trial information
        trial_start,
        trial_end,
        json_extract_scalar(trial_settings, '$.end_behavior.missing_payment_method') as trial_end_behavior,
        
        -- Cancellation information
        cancel_at,
        cancel_at_period_end,
        canceled_at,
        ended_at,
        json_extract_scalar(cancellation_details, '$.reason') as cancellation_reason,
        json_extract_scalar(cancellation_details, '$.comment') as cancellation_comment,
        json_extract_scalar(cancellation_details, '$.feedback') as cancellation_feedback,
        
        -- Payment information
        default_payment_method,
        default_source,
        json_extract_scalar(payment_settings, '$.payment_method_options') as payment_method_options,
        json_extract_scalar(payment_settings, '$.payment_method_types') as payment_method_types,
        json_extract_scalar(payment_settings, '$.save_default_payment_method') as save_default_payment_method,
        
        -- Pricing information
        application_fee_percent,
        json_extract_scalar(automatic_tax, '$.enabled') as automatic_tax_enabled,
        json_extract_scalar(billing_thresholds, '$.amount_gte') as billing_threshold_amount,
        json_extract_scalar(billing_thresholds, '$.reset_billing_cycle_anchor') as billing_threshold_reset_anchor,
        
        -- Metadata (parsed from JSON)
        json_extract_scalar(metadata, '$.plan_name') as plan_name,
        json_extract_scalar(metadata, '$.billing_interval') as billing_interval,
        json_extract_scalar(metadata, '$.trial_converted') as trial_converted,
        json_extract_scalar(metadata, '$.upgrade_path') as upgrade_path,
        json_extract_scalar(metadata, '$.churn_reason') as churn_reason,
        
        -- System fields
        livemode,
        created as subscription_created_at,
        start_date as subscription_start_date,
        application,
        latest_invoice,
        next_pending_invoice_item_invoice,
        on_behalf_of,
        pending_setup_intent,
        schedule,
        test_clock,
        
        -- Ingestion metadata
        _ingested_at,
        _updated_at
        
    from raw_subscriptions
)

select * from cleaned_subscriptions 