# Retrieve a payout

Retrieves the details of an existing payout. Supply the unique payout ID from either a payout creation request or the payout list. Stripe returns the corresponding payout information.

Returns a payout object if a you provide a valid identifier. raises [An error](#errors) occurs otherwise.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new PayoutService();
Payout payout = service.Get("po_1OaFDbEcg9tTZuTgNYmX0PKB");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PayoutParams{};
result, err := payout.Get("po_1OaFDbEcg9tTZuTgNYmX0PKB", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Payout payout = Payout.retrieve("po_1OaFDbEcg9tTZuTgNYmX0PKB");
```

```node
const stripe = require('stripe')('<<secret key>>');

const payout = await stripe.payouts.retrieve('po_1OaFDbEcg9tTZuTgNYmX0PKB');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payout = stripe.Payout.retrieve("po_1OaFDbEcg9tTZuTgNYmX0PKB")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$payout = $stripe->payouts->retrieve('po_1OaFDbEcg9tTZuTgNYmX0PKB', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

payout = Stripe::Payout.retrieve('po_1OaFDbEcg9tTZuTgNYmX0PKB')
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
  "metadata": {},
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