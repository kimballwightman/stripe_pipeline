# Retrieve an FX Quote

Retrieve an FX Quote object

## Parameters

No parameters.

## Returns

Returns an FX Quote object

## Request

**GET** `/v1/fx_quotes/:id`

### Example

```python
# This example uses the beta SDK. See https://github.com/stripe/stripe-python#beta-sdks
import stripe
stripe.api_key = "sk_test_..."
fx_quote = stripe.FxQuote.retrieve("fxq_1QKf8UET9NELqCotgW6CNTnm")
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