# Retrieve a PaymentMethod

Retrieves a PaymentMethod object attached to the StripeAccount. To retrieve a payment method attached to a Customer, you should use [Retrieve a Customer’s PaymentMethods](https://docs.stripe.com/docs/api/payment_methods/customer.md)

Returns a PaymentMethod object.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new PaymentMethodService();
PaymentMethod paymentMethod = service.Get("pm_1Q0PsIJvEtkwdCNYMSaVuRz6");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentMethodParams{};
result, err := paymentmethod.Get("pm_1Q0PsIJvEtkwdCNYMSaVuRz6", params);
```

```java
Stripe.apiKey = "<<secret key>>";

PaymentMethod paymentMethod = PaymentMethod.retrieve("pm_1Q0PsIJvEtkwdCNYMSaVuRz6");
```

```node
const stripe = require('stripe')('<<secret key>>');

const paymentMethod = await stripe.paymentMethods.retrieve('pm_1Q0PsIJvEtkwdCNYMSaVuRz6');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_method = stripe.PaymentMethod.retrieve("pm_1Q0PsIJvEtkwdCNYMSaVuRz6")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentMethod = $stripe->paymentMethods->retrieve('pm_1Q0PsIJvEtkwdCNYMSaVuRz6', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_method = Stripe::PaymentMethod.retrieve('pm_1Q0PsIJvEtkwdCNYMSaVuRz6')
```

### Response

```json
{
  "id": "pm_1Q0PsIJvEtkwdCNYMSaVuRz6",
  "object": "payment_method",
  "allow_redisplay": "unspecified",
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
    "name": "John Doe",
    "phone": null
  },
  "created": 1726673582,
  "customer": null,
  "livemode": false,
  "metadata": {},
  "type": "us_bank_account",
  "us_bank_account": {
    "account_holder_type": "individual",
    "account_type": "checking",
    "bank_name": "STRIPE TEST BANK",
    "financial_connections_account": null,
    "fingerprint": "LstWJFsCK7P349Bg",
    "last4": "6789",
    "networks": {
      "preferred": "ach",
      "supported": [
        "ach"
      ]
    },
    "routing_number": "110000000",
    "status_details": {}
  }
}
```