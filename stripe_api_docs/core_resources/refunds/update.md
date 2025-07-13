# Update a refund

Updates the refund that you specify by setting the values of the passed parameters. Any parameters that you don’t provide remain unchanged.

This request only accepts `metadata` as an argument.

Returns the refund object if the update succeeds. This call raises [an error](#errors) if update parameters are invalid.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new RefundUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var service = new RefundService();
Refund refund = service.Update("re_1Nispe2eZvKYlo2Cd31jOCgZ", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.RefundParams{};
params.AddMetadata("order_id", "6735")
result, err := refund.Update("re_1Nispe2eZvKYlo2Cd31jOCgZ", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Refund resource = Refund.retrieve("re_1Nispe2eZvKYlo2Cd31jOCgZ");

RefundUpdateParams params = RefundUpdateParams.builder().putMetadata("order_id", "6735").build();

Refund refund = resource.update(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const refund = await stripe.refunds.update(
  're_1Nispe2eZvKYlo2Cd31jOCgZ',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

refund = stripe.Refund.modify(
  "re_1Nispe2eZvKYlo2Cd31jOCgZ",
  metadata={"order_id": "6735"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$refund = $stripe->refunds->update(
  're_1Nispe2eZvKYlo2Cd31jOCgZ',
  ['metadata' => ['order_id' => '6735']]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

refund = Stripe::Refund.update('re_1Nispe2eZvKYlo2Cd31jOCgZ', {metadata: {order_id: '6735'}})
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
  "metadata": {
    "order_id": "6735"
  },
  "payment_intent": "pi_1GszsK2eZvKYlo2CfhZyoZLp",
  "reason": null,
  "receipt_number": null,
  "source_transfer_reversal": null,
  "status": "succeeded",
  "transfer_reversal": null
}
```