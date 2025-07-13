# Retrieve a cash balance

Retrieves a customer’s cash balance.

The Cash Balance object for a given customer.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new CustomerCashBalanceService();
CashBalance cashBalance = service.Get("cus_OaCLf8Fi1nbFpJ");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CashBalanceParams{Customer: stripe.String("cus_OaCLf8Fi1nbFpJ")};
result, err := cashbalance.Get(params);
```

```java
Stripe.apiKey = "<<secret key>>";

CashBalance cashBalance = CashBalance.retrieve("cus_OaCLf8Fi1nbFpJ");
```

```node
const stripe = require('stripe')('<<secret key>>');

const cashBalance = await stripe.customers.retrieveCashBalance('cus_OaCLf8Fi1nbFpJ');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

cash_balance = stripe.Customer.retrieve_cash_balance("cus_OaCLf8Fi1nbFpJ")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$cashBalance = $stripe->customers->retrieveCashBalance('cus_OaCLf8Fi1nbFpJ', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

cash_balance = Stripe::Customer.retrieve_cash_balance('cus_OaCLf8Fi1nbFpJ')
```

### Response

```json
{
  "object": "cash_balance",
  "available": {
    "eur": 10000
  },
  "customer": "cus_OaCLf8Fi1nbFpJ",
  "livemode": false,
  "settings": {
    "reconciliation_mode": "automatic",
    "using_merchant_default": true
  }
}
```