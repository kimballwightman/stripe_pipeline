# List credit balance transactions

Retrieve a list of credit balance transactions.

Returns a list of credit balanace transactions.

- `customer` (string, optional)
  The customer for which to fetch credit balance transactions.

- `credit_grant` (string, optional)
  The credit grant for which to fetch credit balance transactions.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new Stripe.Billing.CreditBalanceTransactionListOptions
{
    Customer = "cus_QrvQguzkIK8zTj",
    CreditGrant = "credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE",
};
var service = new Stripe.Billing.CreditBalanceTransactionService();
StripeList<Stripe.Billing.CreditBalanceTransaction> creditBalanceTransactions = service.List(
    options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BillingCreditBalanceTransactionListParams{
  Customer: stripe.String("cus_QrvQguzkIK8zTj"),
  CreditGrant: stripe.String("credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE"),
};
result := creditbalancetransaction.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

CreditBalanceTransactionListParams params =
  CreditBalanceTransactionListParams.builder()
    .setCustomer("cus_QrvQguzkIK8zTj")
    .setCreditGrant("credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE")
    .build();

CreditBalanceTransactionCollection creditBalanceTransactions =
  CreditBalanceTransaction.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const creditBalanceTransactions = await stripe.billing.creditBalanceTransactions.list({
  customer: 'cus_QrvQguzkIK8zTj',
  credit_grant: 'credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE',
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

credit_balance_transactions = stripe.billing.CreditBalanceTransaction.list(
  customer="cus_QrvQguzkIK8zTj",
  credit_grant="credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$creditBalanceTransactions = $stripe->billing->creditBalanceTransactions->all([
  'customer' => 'cus_QrvQguzkIK8zTj',
  'credit_grant' => 'credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE',
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

credit_balance_transactions = Stripe::Billing::CreditBalanceTransaction.list({
  customer: 'cus_QrvQguzkIK8zTj',
  credit_grant: 'credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE',
})
```

### Response

```json
{
  "object": "list",
  "data": [
    {
      "id": "cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue",
      "object": "billing.credit_balance_transaction",
      "created": 1726619524,
      "credit": null,
      "credit_grant": "credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE",
      "debit": {
        "amount": {
          "monetary": {
            "currency": "usd",
            "value": 1000
          },
          "type": "monetary"
        },
        "credits_applied": {
          "invoice": "in_1Q0BoLL6nFOS1ekDbwBM5ER1",
          "invoice_line_item": "il_1QB443L6nFOS1ekDwRiN3Z4n"
        },
        "type": "credits_applied"
      },
      "effective_at": 1729211351,
      "livemode": false,
      "test_clock": "clock_1Q0BoJL6nFOS1ekDbyYYuseM",
      "type": "debit"
    },
    {
      "id": "cbtxn_test_61R9ZkIbb17ze4b2s41L6nFOS1ekDXHs",
      "object": "billing.credit_balance_transaction",
      "created": 1726619434,
      "credit": {
        "amount": {
          "monetary": {
            "currency": "usd",
            "value": 1000
          },
          "type": "monetary"
        },
        "type": "credits_granted"
      },
      "credit_grant": "credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE",
      "debit": null,
      "effective_at": 1726619434,
      "livemode": false,
      "test_clock": "clock_1Q0BoJL6nFOS1ekDbyYYuseM",
      "type": "credit"
    }
  ],
  "has_more": false,
  "url": "/v1/billing/credit_grants"
}
```