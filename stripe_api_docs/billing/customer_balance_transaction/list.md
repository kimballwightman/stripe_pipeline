# List customer balance transactions

Returns a list of transactions that updated the customer’s [balances](https://docs.stripe.com/docs/billing/customer/balance.md).

A dictionary with a `data` property that contains an array of up to `limit` customer balance transactions, starting after item `starting_after`. Each entry in the array is a separate customer balance transaction object. If no more items are available, the resulting array will be empty.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CustomerBalanceTransactionListOptions { Limit = 3 };
var service = new CustomerBalanceTransactionService();
StripeList<CustomerBalanceTransaction> customerBalanceTransactions = service.List(
    "cus_NcjdgdwZyI9Rj7",
    options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CustomerBalanceTransactionListParams{
  Customer: stripe.String("cus_NcjdgdwZyI9Rj7"),
};
params.Limit = stripe.Int64(3)
result := customerbalancetransaction.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

Customer resource = Customer.retrieve("cus_NcjdgdwZyI9Rj7");

CustomerBalanceTransactionsParams params =
  CustomerBalanceTransactionsParams.builder().setLimit(3L).build();

CustomerBalanceTransactionCollection customerBalanceTransactions =
  resource.balanceTransactions(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const customerBalanceTransactions = await stripe.customers.listBalanceTransactions(
  'cus_NcjdgdwZyI9Rj7',
  {
    limit: 3,
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

customer_balance_transactions = stripe.Customer.list_balance_transactions(
  "cus_NcjdgdwZyI9Rj7",
  limit=3,
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$customerBalanceTransactions = $stripe->customers->allBalanceTransactions(
  'cus_NcjdgdwZyI9Rj7',
  ['limit' => 3]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

customer_balance_transactions = Stripe::Customer.list_balance_transactions(
  'cus_NcjdgdwZyI9Rj7',
  {limit: 3},
)
```

### Response

```json
{
  "object": "list",
  "url": "/v1/customers/cus_NcjdgdwZyI9Rj7/balance_transactions",
  "has_more": false,
  "data": [
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
  ]
}
```