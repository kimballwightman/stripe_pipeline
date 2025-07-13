# Update a customer credit balance transaction

Most credit balance transaction fields are immutable, but you may update its `description` and `metadata`.

Returns a customer balance transaction object if the call succeeded.

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CustomerBalanceTransactionUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var service = new CustomerBalanceTransactionService();
CustomerBalanceTransaction customerBalanceTransaction = service.Update(
    "cus_NcjdgdwZyI9Rj7",
    "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI",
    options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CustomerBalanceTransactionParams{Customer: stripe.String("cus_NcjdgdwZyI9Rj7")};
params.AddMetadata("order_id", "6735")
result, err := customerbalancetransaction.Update("cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Customer customer = Customer.retrieve("cus_NcjdgdwZyI9Rj7");

CustomerBalanceTransaction resource =
  customer.balanceTransactions().retrieve("cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI");

CustomerBalanceTransactionUpdateParams params =
  CustomerBalanceTransactionUpdateParams.builder().putMetadata("order_id", "6735").build();

CustomerBalanceTransaction customerBalanceTransaction = resource.update(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const customerBalanceTransaction = await stripe.customers.updateBalanceTransaction(
  'cus_NcjdgdwZyI9Rj7',
  'cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI',
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

customer_balance_transaction = stripe.Customer.modify_balance_transaction(
  "cus_NcjdgdwZyI9Rj7",
  "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI",
  metadata={"order_id": "6735"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$customerBalanceTransaction = $stripe->customers->updateBalanceTransaction(
  'cus_NcjdgdwZyI9Rj7',
  'cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI',
  ['metadata' => ['order_id' => '6735']]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

customer_balance_transaction = Stripe::Customer.update_balance_transaction(
  'cus_NcjdgdwZyI9Rj7',
  'cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI',
  {metadata: {order_id: '6735'}},
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
  "metadata": {
    "order_id": "6735"
  },
  "type": "adjustment"
}
```