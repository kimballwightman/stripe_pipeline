# Create a customer

Creates a new customer object.

## HTTP Request

`POST /v1/customers`

## Parameters

### Required Parameters

None. All parameters are optional.

### Optional Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `address` | object | The customer's address. **Required if calculating taxes** |
| `description` | string | An arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard. |
| `email` | string | Customer's email address. It's displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to 512 characters. |
| `metadata` | object | Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `name` | string | The customer's full name or business name. |
| `payment_method` | string | The ID of the PaymentMethod to attach to the customer. |
| `phone` | string | The customer's phone number. |
| `shipping` | object | The customer's shipping information. Appears on invoices emailed to this customer. |
| `tax` | object | Tax details about the customer. **Recommended if calculating taxes** |

### Additional Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `balance` | integer | An integer amount in cents that represents the customer's current balance, which affects the customer's future invoices. A negative amount represents a credit that decreases the amount due on an invoice; a positive amount increases the amount due on an invoice. |
| `cash_balance` | object | Balance information and default balance settings for this customer. |
| `invoice_prefix` | string | The prefix for the customer used to generate unique invoice numbers. Must be 3–12 uppercase letters or numbers. |
| `invoice_settings` | object | Default invoice settings for this customer. |
| `next_invoice_sequence` | integer | The suffix of the customer's next invoice number, e.g., 0001. |
| `preferred_locales` | array of strings | The customer's preferred locales (languages), ordered by preference. |
| `source` | string | The ID of the Source object to attach to the customer. |
| `tax_exempt` | enum | The customer's tax exemption. One of `none`, `exempt`, or `reverse`. |
| `tax_id_data` | array of objects | The customer's tax IDs. |
| `test_clock` | string | ID of the test clock to attach to the customer. |

## Address Object

| Parameter | Type | Description |
|-----------|------|-------------|
| `city` | string | City, district, suburb, town, or village. |
| `country` | string | Two-letter country code (ISO 3166-1 alpha-2). |
| `line1` | string | Address line 1 (e.g., street, PO Box, or company name). |
| `line2` | string | Address line 2 (e.g., apartment, suite, unit, or building). |
| `postal_code` | string | ZIP or postal code. |
| `state` | string | State, county, province, or region. |

## Shipping Object

| Parameter | Type | Description |
|-----------|------|-------------|
| `address` | object | Customer's shipping address. |
| `name` | string | Customer name. |
| `phone` | string | Customer phone (including extension). |

## Tax Object

| Parameter | Type | Description |
|-----------|------|-------------|
| `ip_address` | string | A recent IP address of the customer used for tax reporting and tax location inference. |
| `location` | object | The customer's location as determined by their IP address. |

## Returns

Returns the Customer object after successful customer creation. Raises an error if create parameters are invalid (for example, specifying an invalid coupon or an invalid source).

## Example Request

```bash
curl https://api.stripe.com/v1/customers \
  -u "sk_test_BQokikJ...2HlWgH4olfQ2:" \
  -d name="Jenny Rosen" \
  --data-urlencode email="jennyrosen@example.com"
```

## Example Response

```json
{
  "id": "cus_NffrFeUfNV2Hib",
  "object": "customer",
  "address": null,
  "balance": 0,
  "created": 1680893993,
  "currency": null,
  "default_source": null,
  "delinquent": false,
  "description": null,
  "email": "jennyrosen@example.com",
  "invoice_prefix": "0759376C",
  "invoice_settings": {
    "custom_fields": null,
    "default_payment_method": null,
    "footer": null,
    "rendering_options": null
  },
  "livemode": false,
  "metadata": {},
  "name": "Jenny Rosen",
  "next_invoice_sequence": 1,
  "phone": null,
  "preferred_locales": [],
  "shipping": null,
  "tax_exempt": "none",
  "test_clock": null
}
```

## Common Use Cases

1. **Basic Customer Creation**: Create a customer with minimal information (name and email)
2. **Customer with Address**: Create a customer with billing address for tax calculations
3. **Customer with Metadata**: Store your internal customer ID in metadata for easy reference
4. **Customer with Payment Method**: Attach a payment method during customer creation

## Field Constraints and Realistic Values

### Email Field
- **Constraint**: Up to 512 characters
- **Realistic Values**: Standard email formats
  - `user@example.com`
  - `firstname.lastname@company.com`
  - `user+tag@domain.co.uk`

### Name Field
- **Realistic Values**: 
  - Personal names: `"John Smith"`, `"Maria Garcia"`, `"李小明"`
  - Business names: `"Acme Corp"`, `"Smith & Associates LLC"`, `"Tech Startup Inc"`

### Phone Field
- **Realistic Values**: Various international formats
  - `"+1-555-123-4567"` (US)
  - `"+44 20 7123 4567"` (UK)
  - `"+49 30 12345678"` (Germany)

### Address Fields
- **Country**: ISO 3166-1 alpha-2 codes (`"US"`, `"GB"`, `"DE"`, `"CA"`)
- **Postal Code**: Format varies by country
  - US: `"12345"` or `"12345-6789"`
  - UK: `"SW1A 1AA"`
  - Canada: `"K1A 0A6"`

### Tax Exempt Values
- `"none"` - Customer is taxable (default)
- `"exempt"` - Customer is tax exempt
- `"reverse"` - Customer is responsible for paying tax

### Preferred Locales
- **Realistic Values**: RFC-4646 language codes
  - `["en"]` - English
  - `["en-US"]` - US English
  - `["fr-CA", "en"]` - Canadian French, fallback to English
  - `["es", "en"]` - Spanish, fallback to English 