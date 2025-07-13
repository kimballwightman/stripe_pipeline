# Fund a test mode cash balance

Create an incoming testmode bank transfer

Returns a specific cash balance transaction, which funded the customer’s [cash balance](https://docs.stripe.com/docs/payments/customer-balance.md).

- `amount` (integer, required)
  Amount to be used for this test cash balance transaction. A positive integer representing how much to fund in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal) (e.g., 100 cents to fund $1.00 or 100 to fund ¥100, a zero-decimal currency).

- `currency` (enum, required)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `reference` (string, optional)
  A description of the test funding. This simulates free-text references supplied by customers when making bank transfers to their cash balance. You can use this to test how Stripe’s [reconciliation algorithm](https://docs.stripe.com/docs/payments/customer-balance/reconciliation.md) applies to different user inputs.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new Stripe.TestHelpers.CustomerFundCashBalanceOptions
{
    Amount = 5000,
    Currency = "eur",
};
var service = new Stripe.TestHelpers.CustomerService();
CustomerCashBalanceTransaction customerCashBalanceTransaction = service.FundCashBalance(
    "cus_9s6XKzkNRiz8i3",
    options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TestHelpersCustomerFundCashBalanceParams{
  Amount: stripe.Int64(5000),
  Currency: stripe.String(string(stripe.CurrencyEUR)),
};
result, err := customer.FundCashBalance("cus_9s6XKzkNRiz8i3", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Customer resource = Customer.retrieve("cus_9s6XKzkNRiz8i3");

CustomerFundCashBalanceParams params =
  CustomerFundCashBalanceParams.builder().setAmount(5000L).setCurrency("eur").build();

CustomerCashBalanceTransaction customerCashBalanceTransaction =
  resource.getTestHelpers().fundCashBalance(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const customerCashBalanceTransaction = await stripe.testHelpers.customers.fundCashBalance(
  'cus_9s6XKzkNRiz8i3',
  {
    amount: 5000,
    currency: 'eur',
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

customer_cash_balance_transaction = stripe.Customer.TestHelpers.fund_cash_balance(
  "cus_9s6XKzkNRiz8i3",
  amount=5000,
  currency="eur",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$customerCashBalanceTransaction = $stripe->testHelpers->customers->fundCashBalance(
  'cus_9s6XKzkNRiz8i3',
  [
    'amount' => 5000,
    'currency' => 'eur',
  ]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

customer_cash_balance_transaction = Stripe::Customer::TestHelpers.fund_cash_balance(
  'cus_9s6XKzkNRiz8i3',
  {
    amount: 5000,
    currency: 'eur',
  },
)
```

### Response

```json
{
  "id": "ccsbtxn_1NlhIV2eZvKYlo2CKwRcXkii",
  "object": "customer_cash_balance_transaction",
  "created": 1693612963,
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