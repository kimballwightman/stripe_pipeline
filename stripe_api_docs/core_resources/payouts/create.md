# Create a payout

To send funds to your own bank account, create a new payout object. Your [Stripe balance](#balance) must cover the payout amount. If it doesn’t, you receive an “Insufficient Funds” error.

If your API key is in test mode, money won’t actually be sent, though every other action occurs as if you’re in live mode.

If you create a manual payout on a Stripe account that uses multiple payment source types, you need to specify the source type balance that the payout draws from. The [balance object](#balance_object) details available and pending amounts by source type.

Returns a payout object if no initial errors are present during the payout creation (invalid routing number, insufficient funds, and so on). We initially mark the status of the payout object as `pending`.

- `amount` (integer, required)
  A positive integer in cents representing how much to payout.

- `currency` (enum, required)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `destination` (string, optional)
  The ID of a bank account or a card to send the payout to. If you don’t provide a destination, we use the default external account for the specified currency.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `method` (string, optional)
  The method used to send this payout, which is `standard` or `instant`. We support `instant` for payouts to debit cards and bank accounts in certain countries. Learn more about [bank support for Instant Payouts](https://stripe.com/docs/payouts/instant-payouts-banks).

- `source_type` (string, optional)
  The balance type of your Stripe balance to draw this payout from. Balances for different payment sources are kept separately. You can find the amounts with the Balances API. One of `bank_account`, `card`, or `fpx`.

- `statement_descriptor` (string, optional)
  A string that displays on the recipient’s bank or card statement (up to 22 characters). A `statement_descriptor` that’s longer than 22 characters return an error. Most banks truncate this information and display it inconsistently. Some banks might not display it at all.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new PayoutCreateOptions { Amount = 1100, Currency = "usd" };
var service = new PayoutService();
Payout payout = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PayoutParams{
  Amount: stripe.Int64(1100),
  Currency: stripe.String(string(stripe.CurrencyUSD)),
};
result, err := payout.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

PayoutCreateParams params =
  PayoutCreateParams.builder().setAmount(1100L).setCurrency("usd").build();

Payout payout = Payout.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const payout = await stripe.payouts.create({
  amount: 1100,
  currency: 'usd',
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payout = stripe.Payout.create(
  amount=1100,
  currency="usd",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$payout = $stripe->payouts->create([
  'amount' => 1100,
  'currency' => 'usd',
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

payout = Stripe::Payout.create({
  amount: 1100,
  currency: 'usd',
})
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