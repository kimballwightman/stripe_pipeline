# List cash balance transactions

Returns a list of transactions that modified the customer’s [cash balance](https://docs.stripe.com/docs/payments/customer-balance.md).

A dictionary with a `data` property that contains an array of up to `limit` cash balance transactions, starting after item `starting_after`. Each entry in the array is a separate cash balance transaction object. If no more items are available, the resulting array will be empty.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CustomerCashBalanceTransactionListOptions { Limit = 3 };
var service = new CustomerCashBalanceTransactionService();
StripeList<CustomerCashBalanceTransaction> customerCashBalanceTransactions = service.List(
    "cus_9s6XKzkNRiz8i3",
    options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CustomerCashBalanceTransactionListParams{
  Customer: stripe.String("cus_9s6XKzkNRiz8i3"),
};
params.Limit = stripe.Int64(3)
result := customercashbalancetransaction.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

Customer resource = Customer.retrieve("cus_9s6XKzkNRiz8i3");

CustomerCashBalanceTransactionsParams params =
  CustomerCashBalanceTransactionsParams.builder().setLimit(3L).build();

CustomerCashBalanceTransactionCollection customerCashBalanceTransactions =
  resource.cashBalanceTransactions(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const customerCashBalanceTransactions = await stripe.customers.listCashBalanceTransactions(
  'cus_9s6XKzkNRiz8i3',
  {
    limit: 3,
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

customer_cash_balance_transactions = stripe.Customer.list_cash_balance_transactions(
  "cus_9s6XKzkNRiz8i3",
  limit=3,
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$customerCashBalanceTransactions = $stripe->customers->allCashBalanceTransactions(
  'cus_9s6XKzkNRiz8i3',
  ['limit' => 3]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

customer_cash_balance_transactions = Stripe::Customer.list_cash_balance_transactions(
  'cus_9s6XKzkNRiz8i3',
  {limit: 3},
)
```

### Response

```json
{
  "object": "list",
  "url": "/v1/customers/cus_9s6XKzkNRiz8i3/cash_balance_transactions",
  "has_more": false,
  "data": [
    {
      "id": "ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF",
      "object": "customer_cash_balance_transaction",
      "created": 1690829143,
      "currency": "eur",
      "customer": "cus_9s6XKzkNRiz8i3",
      "ending_balance": 10000,
      "funded": {
        "bank_transfer": {
          "eu_bank_transfer": {
            "bic": "BANKDEAAXXX",
            "iban_last4": "7089",
            "sender_name": "Sample Business GmbH"
          },
          "reference": "Payment for Invoice 28278FC-155",
          "type": "eu_bank_transfer"
        }
      },
      "livemode": false,
      "net_amount": 5000,
      "type": "funded"
    }
  ]
}
```