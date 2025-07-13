# Detach a PaymentMethod from a Customer

Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.

Returns a PaymentMethod object.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new PaymentMethodService();
PaymentMethod paymentMethod = service.Detach("pm_1MqLiJLkdIwHu7ixUEgbFdYF");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentMethodDetachParams{};
result, err := paymentmethod.Detach("pm_1MqLiJLkdIwHu7ixUEgbFdYF", params);
```

```java
Stripe.apiKey = "<<secret key>>";

PaymentMethod resource = PaymentMethod.retrieve("pm_1MqLiJLkdIwHu7ixUEgbFdYF");

PaymentMethodDetachParams params = PaymentMethodDetachParams.builder().build();

PaymentMethod paymentMethod = resource.detach(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const paymentMethod = await stripe.paymentMethods.detach('pm_1MqLiJLkdIwHu7ixUEgbFdYF');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_method = stripe.PaymentMethod.detach("pm_1MqLiJLkdIwHu7ixUEgbFdYF")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentMethod = $stripe->paymentMethods->detach('pm_1MqLiJLkdIwHu7ixUEgbFdYF', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_method = Stripe::PaymentMethod.detach('pm_1MqLiJLkdIwHu7ixUEgbFdYF')
```

### Response

```json
{
  "id": "pm_1MqLiJLkdIwHu7ixUEgbFdYF",
  "object": "payment_method",
  "billing_details": {
    "address": {
      "city": null,
      "country": null,
      "line1": null,
      "line2": null,
      "postal_code": null,
      "state": null
    },
    "email": null,
    "name": null,
    "phone": null
  },
  "card": {
    "brand": "visa",
    "checks": {
      "address_line1_check": null,
      "address_postal_code_check": null,
      "cvc_check": "unchecked"
    },
    "country": "US",
    "exp_month": 8,
    "exp_year": 2026,
    "fingerprint": "mToisGZ01V71BCos",
    "funding": "credit",
    "generated_from": null,
    "last4": "4242",
    "networks": {
      "available": [
        "visa"
      ],
      "preferred": null
    },
    "three_d_secure_usage": {
      "supported": true
    },
    "wallet": null
  },
  "created": 1679945299,
  "customer": null,
  "livemode": false,
  "metadata": {},
  "type": "card"
}
```