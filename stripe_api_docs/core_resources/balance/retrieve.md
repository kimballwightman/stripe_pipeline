# Retrieve balance

Retrieves the current account balance, based on the authentication that was used to make the request.
For a sample request, see [Accounting for negative balances](https://docs.stripe.com/docs/connect/account-balances.md#accounting-for-negative-balances).

Returns a balance object for the account that was authenticated in the request.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new BalanceGetOptions();
var service = new BalanceService();
Balance balance = service.Get(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BalanceParams{};
result, err := balance.Get(params);
```

```java
Stripe.apiKey = "<<secret key>>";

Balance balance = Balance.retrieve();
```

```node
const stripe = require('stripe')('<<secret key>>');

const balance = await stripe.balance.retrieve();
```

```python
import stripe
stripe.api_key = "<<secret key>>"

balance = stripe.Balance.retrieve()
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$balance = $stripe->balance->retrieve([]);
```

```ruby
Stripe.api_key = '<<secret key>>'

balance = Stripe::Balance.retrieve()
```

### Response

```json
{
  "object": "balance",
  "available": [
    {
      "amount": 666670,
      "currency": "usd",
      "source_types": {
        "card": 666670
      }
    }
  ],
  "connect_reserved": [
    {
      "amount": 0,
      "currency": "usd"
    }
  ],
  "livemode": false,
  "pending": [
    {
      "amount": 61414,
      "currency": "usd",
      "source_types": {
        "card": 61414
      }
    }
  ]
}
```