# Create a customer balance transaction

Creates an immutable transaction that updates the customer’s credit [balance](https://docs.stripe.com/docs/billing/customer/balance.md).

Returns a customer balance transaction object if the call succeeded.

- `amount` (integer, required)
  The integer amount in **** to apply to the customer’s credit balance.

- `currency` (enum, required)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). Specifies the [`invoice_credit_balance`](https://docs.stripe.com/docs/api/customers/object.md#customer_object-invoice_credit_balance) that this transaction will apply to. If the customer’s `currency` is not set, it will be updated to this value.

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CustomerBalanceTransactionCreateOptions { Amount = -500, Currency = "usd" };
var service = new CustomerBalanceTransactionService();
CustomerBalanceTransaction customerBalanceTransaction = service.Create(
    "cus_NcjdgdwZyI9Rj7",
    options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CustomerBalanceTransactionParams{
  Amount: stripe.Int64(-500),
  Currency: stripe.String(string(stripe.CurrencyUSD)),
  Customer: stripe.String("cus_NcjdgdwZyI9Rj7"),
};
result, err := customerbalancetransaction.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

Customer customer = Customer.retrieve("cus_NcjdgdwZyI9Rj7");

CustomerBalanceTransactionCollectionCreateParams params =
  CustomerBalanceTransactionCollectionCreateParams.builder()
    .setAmount(-500L)
    .setCurrency("usd")
    .build();

CustomerBalanceTransaction customerBalanceTransaction =
  customer.balanceTransactions().create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const customerBalanceTransaction = await stripe.customers.createBalanceTransaction(
  'cus_NcjdgdwZyI9Rj7',
  {
    amount: -500,
    currency: 'usd',
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

customer_balance_transaction = stripe.Customer.create_balance_transaction(
  "cus_NcjdgdwZyI9Rj7",
  amount=-500,
  currency="usd",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$customerBalanceTransaction = $stripe->customers->createBalanceTransaction(
  'cus_NcjdgdwZyI9Rj7',
  [
    'amount' => -500,
    'currency' => 'usd',
  ]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

customer_balance_transaction = Stripe::Customer.create_balance_transaction(
  'cus_NcjdgdwZyI9Rj7',
  {
    amount: -500,
    currency: 'usd',
  },
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