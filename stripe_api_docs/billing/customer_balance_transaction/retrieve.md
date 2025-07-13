# Retrieve a customer balance transaction

Retrieves a specific customer balance transaction that updated the customer’s [balances](https://docs.stripe.com/docs/billing/customer/balance.md).

Returns a customer balance transaction object if a valid identifier was provided.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new CustomerBalanceTransactionService();
CustomerBalanceTransaction customerBalanceTransaction = service.Get(
    "cus_NcjdgdwZyI9Rj7",
    "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CustomerBalanceTransactionParams{Customer: stripe.String("cus_NcjdgdwZyI9Rj7")};
result, err := customerbalancetransaction.Get("cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Customer customer = Customer.retrieve("cus_NcjdgdwZyI9Rj7");

CustomerBalanceTransaction customerBalanceTransaction =
  customer.balanceTransactions().retrieve("cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI");
```

```node
const stripe = require('stripe')('<<secret key>>');

const customerBalanceTransaction = await stripe.customers.retrieveBalanceTransaction(
  'cus_NcjdgdwZyI9Rj7',
  'cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

customer_balance_transaction = stripe.Customer.retrieve_balance_transaction(
  "cus_NcjdgdwZyI9Rj7",
  "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$customerBalanceTransaction = $stripe->customers->retrieveBalanceTransaction(
  'cus_NcjdgdwZyI9Rj7',
  'cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI',
  []
);
```

```ruby
Stripe.api_key = '<<secret key>>'

customer_balance_transaction = Stripe::Customer.retrieve_balance_transaction(
  'cus_NcjdgdwZyI9Rj7',
  'cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI',
)
```

### Response

```json
{
  "id": "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI",
  "object": "customer_balance_transaction",
  "amount": -500,
  "created": 1680216086,
  "credit_note": null,
  "currency": "usd",
  "customer": "cus_NcjdgdwZyI9Rj7",
  "description": null,
  "ending_balance": -500,
  "invoice": null,
  "livemode": false,
  "metadata": {},
  "type": "adjustment"
}
```