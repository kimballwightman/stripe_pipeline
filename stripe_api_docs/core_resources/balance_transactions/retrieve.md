# Retrieve a balance transaction

Retrieves the balance transaction with the given ID.

Note that this endpoint previously used the path `/v1/balance/history/:id`.

Returns a balance transaction if a valid balance transaction ID was provided. Raises [an error](#errors) otherwise.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new BalanceTransactionService();
BalanceTransaction balanceTransaction = service.Get("txn_1MiN3gLkdIwHu7ixxapQrznl");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BalanceTransactionParams{};
result, err := balancetransaction.Get("txn_1MiN3gLkdIwHu7ixxapQrznl", params);
```

```java
Stripe.apiKey = "<<secret key>>";

BalanceTransaction balanceTransaction = BalanceTransaction.retrieve("txn_1MiN3gLkdIwHu7ixxapQrznl");
```

```node
const stripe = require('stripe')('<<secret key>>');

const balanceTransaction = await stripe.balanceTransactions.retrieve(
  'txn_1MiN3gLkdIwHu7ixxapQrznl'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

balance_transaction = stripe.BalanceTransaction.retrieve("txn_1MiN3gLkdIwHu7ixxapQrznl")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$balanceTransaction = $stripe->balanceTransactions->retrieve('txn_1MiN3gLkdIwHu7ixxapQrznl', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

balance_transaction = Stripe::BalanceTransaction.retrieve('txn_1MiN3gLkdIwHu7ixxapQrznl')
```

### Response

```json
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
```