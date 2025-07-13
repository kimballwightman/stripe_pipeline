# List all balance transactions

Returns a list of transactions that have contributed to the Stripe account balance (e.g., charges, transfers, and so forth). The transactions are returned in sorted order, with the most recent transactions appearing first.

Note that this endpoint was previously called “Balance history” and used the path `/v1/balance/history`.

A dictionary with a `data` property that contains an array of up to `limit` transactions, starting after transaction `starting_after`. Each entry in the array is a separate transaction history object. If no more transactions are available, the resulting array will be empty.

- `created` (object, optional)
  Only return transactions that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `currency` (enum, optional)
  Only return transactions in a certain currency. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `payout` (string, optional)
  For automatic Stripe payouts only, only returns transactions that were paid out on the specified payout ID.

- `source` (string, optional)
  Only returns the original transaction.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `type` (string, optional)
  Only returns transactions of the given type. One of: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `obligation_outbound`, `obligation_reversal_inbound`, `payment`, `payment_failure_refund`, `payment_network_reserve_hold`, `payment_network_reserve_release`, `payment_refund`, `payment_reversal`, `payment_unreconciled`, `payout`, `payout_cancel`, `payout_failure`, `payout_minimum_balance_hold`, `payout_minimum_balance_release`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `stripe_balance_payment_debit`, `stripe_balance_payment_debit_reversal`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new BalanceTransactionListOptions { Limit = 3 };
var service = new BalanceTransactionService();
StripeList<BalanceTransaction> balanceTransactions = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BalanceTransactionListParams{};
params.Limit = stripe.Int64(3)
result := balancetransaction.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

BalanceTransactionListParams params = BalanceTransactionListParams.builder().setLimit(3L).build();

BalanceTransactionCollection balanceTransactions = BalanceTransaction.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const balanceTransactions = await stripe.balanceTransactions.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

balance_transactions = stripe.BalanceTransaction.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$balanceTransactions = $stripe->balanceTransactions->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

balance_transactions = Stripe::BalanceTransaction.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/balance_transactions",
  "has_more": false,
  "data": [
    {
      "id": "txn_1MiN3gLkdIwHu7ixxapQrznl",
      "object": "balance_transaction",
      "amount": -400,
      "available_on": 1678043844,
      "created": 1678043844,
      "currency": "usd",
      "description": null,
      "exchange_rate": null,
      "fee": 0,
      "fee_details": [],
      "net": -400,
      "reporting_category": "transfer",
      "source": "tr_1MiN3gLkdIwHu7ixNCZvFdgA",
      "status": "available",
      "type": "transfer"
    }
  ]
}
```