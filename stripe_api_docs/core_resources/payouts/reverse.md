 # Reverse a payout

Reverses a payout by debiting the destination bank account. At this time, you can only reverse payouts for connected accounts to US bank accounts. If the payout is manual and in the `pending` status, use `/v1/payouts/:id/cancel` instead.

By requesting a reversal through `/v1/payouts/:id/reverse`, you confirm that the authorized signatory of the selected bank account authorizes the debit on the bank account and that no other authorization is required.

Returns the reversing payout object if the reversal is successful. Returns an error if the payout is already reversed or can’t be reversed.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new PayoutService();
Payout payout = service.Reverse("po_1OaFDbEcg9tTZuTgNYmX0PKB");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PayoutReverseParams{};
result, err := payout.Reverse("po_1OaFDbEcg9tTZuTgNYmX0PKB", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Payout resource = Payout.retrieve("po_1OaFDbEcg9tTZuTgNYmX0PKB");

PayoutReverseParams params = PayoutReverseParams.builder().build();

Payout payout = resource.reverse(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const payout = await stripe.payouts.reverse('po_1OaFDbEcg9tTZuTgNYmX0PKB');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payout = stripe.Payout.reverse("po_1OaFDbEcg9tTZuTgNYmX0PKB")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$payout = $stripe->payouts->reverse('po_1OaFDbEcg9tTZuTgNYmX0PKB', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

payout = Stripe::Payout.reverse('po_1OaFDbEcg9tTZuTgNYmX0PKB')
```

### Response

```json
{
  "id": "po_1Oj6B8rU4sY9X3L2mQ6T5fZ1",
  "object": "payout",
  "amount": -1100,
  "arrival_date": 1680652800,
  "automatic": false,
  "balance_transaction": "txn_1O5G7H8k1p2Q9a6c0N8elkI0",
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
  "original_payout": "po_1OaFDbEcg9tTZuTgNYmX0PKB",
  "reconciliation_status": "not_applicable",
  "reversed_by": null,
  "source_type": "card",
  "statement_descriptor": null,
  "status": "pending",
  "type": "bank_account"
}
```