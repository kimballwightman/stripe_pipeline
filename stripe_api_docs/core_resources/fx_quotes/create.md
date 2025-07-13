# Create an FX Quote

Creates an FX Quote object

## Parameters

### from_currencies
**array of enums**  
*Required*  
A list of three letter ISO currency code, in lowercase. Must be supported currencies.

### lock_duration
**enum**  
*Required*  
The duration that you wish the quote to be locked for. The quote will be usable for the duration specified. The default is `none`. The maximum is 1 day.

**Possible enum values:**
- `day` - Requests a quote valid for one day
- `five_minutes` - Requests a quote valid for five minutes
- `hour` - Requests a quote valid for one hour
- `none` - Requests a quote valid without lock rate

### to_currency
**enum**  
*Required*  
Three-letter ISO currency code, in lowercase. Must be a supported currency.

### usage
**object**  
The usage specific information for the quote.

#### usage.type
**enum**  
*Required*  
Which transaction the FX Quote will be used for

Can be `"payment"` | `"transfer"`

**Possible enum values:**
- `payment` - The usage of the FX Quote is for payments.
- `transfer` - The usage of the FX Quote is for transfers.

#### usage.payment
**object**  
The payment transaction details that are intended for the FX Quote.

##### usage.payment.destination
**string**  
The Stripe account ID that the funds will be transferred to.

This field should match the account ID that would be used in the PaymentIntent's `transfer_data[destination]` field.

##### usage.payment.on_behalf_of
**string**  
The Stripe account ID that these funds are intended for.

This field should match the account ID that would be used in the PaymentIntent's `on_behalf_of` field.

#### usage.transfer
**object**  
The transfer transaction details that are intended for the FX Quote.

##### usage.transfer.destination
**string**  
*Required*  
The Stripe account ID that the funds will be transferred to.

This field should match the account ID that would be used in the Transfer's `destination` field.

## Returns

Returns an FX Quote object

## Request

**POST** `/v1/fx_quotes`

### Example

```python
# This example uses the beta SDK. See https://github.com/stripe/stripe-python#beta-sdks
import stripe
stripe.api_key = "sk_test_..."
fx_quote = stripe.FxQuote.create(
  to_currency="chf",
  from_currencies=["gbp", "krw"],
  lock_duration="hour",
)
```

### Response

```json
{
  "id": "fxq_1QKf8UET9NELqCotgW6CNTnm",
  "object": "fx_quote",
  "created": 1731498806.6424642,
  "lock_duration": "hour",
  "lock_expires_at": 1731502406.5579598,
  "lock_status": "active",
  "rates": {
    "gbp": {
      "exchange_rate": 1.10167,
      "rate_details": {
        "base_rate": 1.12415,
        "fx_fee_rate": 0.02,
        "reference_rate": 1.12437,
        "reference_rate_provider": "ecb"
      }
    },
    "krw": {
      "exchange_rate": 0.000617274,
      "rate_details": {
        "base_rate": 0.000629871,
        "fx_fee_rate": 0.02,
        "reference_rate": 0.000629997,
        "reference_rate_provider": "ecb"
      }
    }
  },
  "to_currency": "chf",
  "usage": {
    "payment": null,
    "transfer": null,
    "type": "payment"
  }
}
``` 