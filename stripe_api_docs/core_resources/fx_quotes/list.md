# List active FX Quotes

Returns a list of FX quotes that have been issued. The FX quotes are returned in sorted order, with the most recent FX quotes appearing first.

## Parameters

No parameters.

### Optional Parameters

#### ending_before
**string**  
A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

#### limit
**integer**  
A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

#### starting_after
**string**  
A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

## Returns

Returns a list of active FX Quote objects

## Request

**GET** `/v1/fx_quotes`

### Example

```python
# This example uses the beta SDK. See https://github.com/stripe/stripe-python#beta-sdks
import stripe
stripe.api_key = "sk_test_..."
fx_quotes = stripe.FxQuote.list()
```

### Response

```json
{
  "object": "list",
  "data": [
    {
      "id": "fxq_1QKhOFJNWfm6rTxStk9ZbHFc",
      "object": "fx_quote",
      "created": 1731507471.9745815,
      "lock_duration": "hour",
      "lock_expires_at": 1731511071.8779202,
      "lock_status": "active",
      "rates": {
        "krw": {
          "exchange_rate": 0.00054915,
          "rate_details": {
            "base_rate": 0.000560357,
            "fx_fee_rate": 0.02,
            "reference_rate": 0.000560469,
            "reference_rate_provider": "ecb"
          }
        },
        "usd": {
          "exchange_rate": 0.767475,
          "rate_details": {
            "base_rate": 0.783138,
            "fx_fee_rate": 0.02,
            "reference_rate": 0.783295,
            "reference_rate_provider": "ecb"
          }
        }
      },
      "to_currency": "gbp",
      "usage": {
        "payment": null,
        "transfer": null,
        "type": "payment"
      }
    },
    {
      "id": "fxq_1QAtdiIHwhphhlQlU0ckVq4L",
      "object": "fx_quote",
      "created": 1729171278.667021,
      "lock_duration": "day",
      "lock_expires_at": 1729257678.5269883,
      "lock_status": "active",
      "rates": {
        "gbp": {
          "exchange_rate": 1.10078,
          "rate_details": {
            "base_rate": 1.12325,
            "fx_fee_rate": 0.02,
            "reference_rate": 1.12347,
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
  ],
  "has_more": false,
  "url": "/v1/fx_quotes"
}
``` 