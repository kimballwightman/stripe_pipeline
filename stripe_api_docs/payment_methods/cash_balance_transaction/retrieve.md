# Retrieve a cash balance transaction

Retrieves a specific cash balance transaction, which updated the customer’s [cash balance](https://docs.stripe.com/docs/payments/customer-balance.md).

Returns a cash balance transaction object if a valid identifier was provided.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new CustomerCashBalanceTransactionService();
CustomerCashBalanceTransaction customerCashBalanceTransaction = service.Get(
    "cus_9s6XKzkNRiz8i3",
    "ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CustomerCashBalanceTransactionParams{
  Customer: stripe.String("cus_9s6XKzkNRiz8i3"),
};
result, err := customercashbalancetransaction.Get("ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Customer customer = Customer.retrieve("cus_9s6XKzkNRiz8i3");

CustomerCashBalanceTransaction customerCashBalanceTransaction =
  customer.cashBalanceTransactions().retrieve("ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF");
```

```node
const stripe = require('stripe')('<<secret key>>');

const customerCashBalanceTransaction = await stripe.customers.retrieveCashBalanceTransaction(
  'cus_9s6XKzkNRiz8i3',
  'ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

customer_cash_balance_transaction = stripe.Customer.retrieve_cash_balance_transaction(
  "cus_9s6XKzkNRiz8i3",
  "ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$customerCashBalanceTransaction = $stripe->customers->retrieveCashBalanceTransaction(
  'cus_9s6XKzkNRiz8i3',
  'ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF',
  []
);
```

```ruby
Stripe.api_key = '<<secret key>>'

customer_cash_balance_transaction = Stripe::Customer.retrieve_cash_balance_transaction(
  'cus_9s6XKzkNRiz8i3',
  'ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF',
)
```

### Response

```json
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
```