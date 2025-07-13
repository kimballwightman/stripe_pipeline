# Update a payout

Updates the specified payout by setting the values of the parameters you pass. We don’t change parameters that you don’t provide. This request only accepts the metadata as arguments.

Returns the payout object if the update succeeds. This call raises [an error](#errors) if update parameters are invalid.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new PayoutUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var service = new PayoutService();
Payout payout = service.Update("po_1OaFDbEcg9tTZuTgNYmX0PKB", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PayoutParams{};
params.AddMetadata("order_id", "6735")
result, err := payout.Update("po_1OaFDbEcg9tTZuTgNYmX0PKB", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Payout resource = Payout.retrieve("po_1OaFDbEcg9tTZuTgNYmX0PKB");

PayoutUpdateParams params = PayoutUpdateParams.builder().putMetadata("order_id", "6735").build();

Payout payout = resource.update(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const payout = await stripe.payouts.update(
  'po_1OaFDbEcg9tTZuTgNYmX0PKB',
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

payout = stripe.Payout.modify(
  "po_1OaFDbEcg9tTZuTgNYmX0PKB",
  metadata={"order_id": "6735"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$payout = $stripe->payouts->update(
  'po_1OaFDbEcg9tTZuTgNYmX0PKB',
  ['metadata' => ['order_id' => '6735']]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

payout = Stripe::Payout.update('po_1OaFDbEcg9tTZuTgNYmX0PKB', {metadata: {order_id: '6735'}})
```

### Response

```json
{
  "id": "po_1OaFDbEcg9tTZuTgNYmX0PKB",
  "object": "payout",
  "amount": 1100,
  "arrival_date": 1680652800,
  "automatic": false,
  "balance_transaction": "txn_1OaFDcEcg9tTZuTgYMR25tSe",
  "created": 1680648691,
  "currency": "usd",
  "description": null,
  "destination": "ba_1MtIhL2eZvKYlo2CAElKwKu2",
  "failure_balance_transaction": null,
  "failure_code": null,
  "failure_message": null,
  "livemode": false,
  "metadata": {
    "order_id": "6735"
  },
  "method": "standard",
  "original_payout": null,
  "reconciliation_status": "not_applicable",
  "reversed_by": null,
  "source_type": "card",
  "statement_descriptor": null,
  "status": "pending",
  "type": "bank_account"
}
```