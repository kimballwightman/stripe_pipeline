# Cancel a payout

You can cancel a previously created payout if its status is `pending`. Stripe refunds the funds to your available balance. You can’t cancel automatic Stripe payouts.

Returns the payout object if the cancellation succeeds. Returns an error if the payout is already canceled or can’t be canceled.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new PayoutService();
Payout payout = service.Cancel("po_1OaFDbEcg9tTZuTgNYmX0PKB");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PayoutParams{};
result, err := payout.Cancel("po_1OaFDbEcg9tTZuTgNYmX0PKB", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Payout resource = Payout.retrieve("po_1OaFDbEcg9tTZuTgNYmX0PKB");

PayoutCancelParams params = PayoutCancelParams.builder().build();

Payout payout = resource.cancel(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const payout = await stripe.payouts.cancel('po_1OaFDbEcg9tTZuTgNYmX0PKB');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payout = stripe.Payout.cancel("po_1OaFDbEcg9tTZuTgNYmX0PKB")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$payout = $stripe->payouts->cancel('po_1OaFDbEcg9tTZuTgNYmX0PKB', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

payout = Stripe::Payout.cancel('po_1OaFDbEcg9tTZuTgNYmX0PKB')
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
  "failure_balance_transaction": "txn_1OaFJKEcg9tTZuTg2RdsWQhi",
  "failure_code": null,
  "failure_message": null,
  "livemode": false,
  "metadata": {},
  "method": "standard",
  "original_payout": null,
  "reconciliation_status": "not_applicable",
  "reversed_by": null,
  "source_type": "card",
  "statement_descriptor": null,
  "status": "canceled",
  "type": "bank_account"
}
```