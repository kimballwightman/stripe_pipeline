# Cancel a refund

Cancels a refund with a status of `requires_action`.

You can’t cancel refunds in other states. Only refunds for payment methods that require customer action can enter the `requires_action` state.

Returns the refund object if the cancellation succeeds. This call raises [an error](#errors) if you can’t cancel the refund.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new RefundService();
Refund refund = service.Cancel("re_1Nispe2eZvKYlo2Cd31jOCgZ");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.RefundCancelParams{};
result, err := refund.Cancel("re_1Nispe2eZvKYlo2Cd31jOCgZ", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Refund resource = Refund.retrieve("re_1Nispe2eZvKYlo2Cd31jOCgZ");

RefundCancelParams params = RefundCancelParams.builder().build();

Refund refund = resource.cancel(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const refund = await stripe.refunds.cancel('re_1Nispe2eZvKYlo2Cd31jOCgZ');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

refund = stripe.Refund.cancel("re_1Nispe2eZvKYlo2Cd31jOCgZ")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$refund = $stripe->refunds->cancel('re_1Nispe2eZvKYlo2Cd31jOCgZ', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

refund = Stripe::Refund.cancel('re_1Nispe2eZvKYlo2Cd31jOCgZ')
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
  "failure_balance_transaction": "txn_3MmlLrLkdIwHu7ix0uke3Ezy",
  "failure_reason": "merchant_request",
  "metadata": {},
  "payment_intent": "pi_1GszsK2eZvKYlo2CfhZyoZLp",
  "reason": null,
  "receipt_number": null,
  "source_transfer_reversal": null,
  "status": "canceled",
  "transfer_reversal": null
}
```