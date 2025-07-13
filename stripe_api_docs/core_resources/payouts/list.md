# List all payouts

Returns a list of existing payouts sent to third-party bank accounts or payouts that Stripe sent to you. The payouts return in sorted order, with the most recently created payouts appearing first.

A dictionary with a `data` property that contains an array of up to `limit` payouts, starting after payout `starting_after`. Each entry in the array is a separate payout object. If no other payouts are available, the resulting array is empty.

- `arrival_date` (object, optional)
  Only return payouts that are expected to arrive during the given date interval.

  - `arrival_date.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `arrival_date.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `arrival_date.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `arrival_date.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `created` (object, optional)
  Only return payouts that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `destination` (string, optional)
  The ID of an external account - only return payouts sent to this external account.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (string, optional)
  Only return payouts that have the given status: `pending`, `paid`, `failed`, or `canceled`.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new PayoutListOptions { Limit = 3 };
var service = new PayoutService();
StripeList<Payout> payouts = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PayoutListParams{};
params.Limit = stripe.Int64(3)
result := payout.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

PayoutListParams params = PayoutListParams.builder().setLimit(3L).build();

PayoutCollection payouts = Payout.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const payouts = await stripe.payouts.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payouts = stripe.Payout.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$payouts = $stripe->payouts->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

payouts = Stripe::Payout.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/payouts",
  "has_more": false,
  "data": [
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
  ]
}
```