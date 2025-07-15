{{ config(
    materialized='view',
    description='Staging model for Stripe customers - cleans and normalizes raw customer data'
) }}

with raw_customers as (
    select * from {{ source('stripe_raw', 'customers') }}
),

cleaned_customers as (
    select
        -- Primary key
        id as customer_id,
        
        -- Basic customer information
        object,
        name as customer_name,
        email as customer_email,
        phone as customer_phone,
        description as customer_description,
        
        -- Address information (parsed from JSON)
        json_extract_scalar(address, '$.line1') as address_line1,
        json_extract_scalar(address, '$.line2') as address_line2,
        json_extract_scalar(address, '$.city') as address_city,
        json_extract_scalar(address, '$.state') as address_state,
        json_extract_scalar(address, '$.postal_code') as address_postal_code,
        json_extract_scalar(address, '$.country') as address_country,
        
        -- Shipping information (parsed from JSON)
        json_extract_scalar(shipping, '$.name') as shipping_name,
        json_extract_scalar(shipping, '$.address.line1') as shipping_address_line1,
        json_extract_scalar(shipping, '$.address.line2') as shipping_address_line2,
        json_extract_scalar(shipping, '$.address.city') as shipping_address_city,
        json_extract_scalar(shipping, '$.address.state') as shipping_address_state,
        json_extract_scalar(shipping, '$.address.postal_code') as shipping_address_postal_code,
        json_extract_scalar(shipping, '$.address.country') as shipping_address_country,
        
        -- Financial information
        balance,
        currency,
        delinquent,
        tax_exempt,
        
        -- Metadata (parsed from JSON)
        json_extract_scalar(metadata, '$.region') as customer_region,
        json_extract_scalar(metadata, '$.country') as customer_country,
        json_extract_scalar(metadata, '$.signup_date') as customer_signup_date,
        json_extract_scalar(metadata, '$.acquisition_channel') as acquisition_channel,
        json_extract_scalar(metadata, '$.company_size') as company_size,
        json_extract_scalar(metadata, '$.industry') as industry,
        
        -- System fields
        livemode,
        created as customer_created_at,
        default_source,
        invoice_prefix,
        next_invoice_sequence,
        preferred_locales,
        test_clock,
        
        -- Ingestion metadata
        _ingested_at,
        _updated_at
        
    from raw_customers
)

select * from cleaned_customers 