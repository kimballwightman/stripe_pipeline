# Retrieve a refund

Retrieves the details of an existing refund.

Returns a refund if you provide a valid ID. Raises [an error](#errors) otherwise.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new RefundService();
Refund refund = service.Get("re_1Nispe2eZvKYlo2Cd31jOCgZ");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.RefundParams{};
result, err := refund.Get("re_1Nispe2eZvKYlo2Cd31jOCgZ", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Refund refund = Refund.retrieve("re_1Nispe2eZvKYlo2Cd31jOCgZ");
```

```node
const stripe = require('stripe')('<<secret key>>');

const refund = await stripe.refunds.retrieve('re_1Nispe2eZvKYlo2Cd31jOCgZ');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

refund = stripe.Refund.retrieve("re_1Nispe2eZvKYlo2Cd31jOCgZ")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$refund = $stripe->refunds->retrieve('re_1Nispe2eZvKYlo2Cd31jOCgZ', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

refund = Stripe::Refund.retrieve('re_1Nispe2eZvKYlo2Cd31jOCgZ')
```

### Response

```json
{
  "id": "re_1Nispe2eZvKYlo2Cd31jOCgZ",
  "object": "refund",
  "amount": 1000,
  "balance_transaction": "txn_1Nispe2eZvKYlo2CYezqFhEx",
  "charge": "ch_1NirD82eZvKYlo2CIvbtLWuY",
  "created": 1692942318,
  "currency": "usd",
  "destination_details": {
    "card": {
      "reference": "123456789012",
      "reference_status": "available",
      "reference_type": "acquirer_reference_number",
      "type": "refund"
    },
    "type": "card"
  },
  "metadata": {},
  "payment_intent": "pi_1GszsK2eZvKYlo2CfhZyoZLp",
  "reason": null,
  "receipt_number": null,
  "source_transfer_reversal": null,
  "status": "succeeded",
  "transfer_reversal": null
}
```