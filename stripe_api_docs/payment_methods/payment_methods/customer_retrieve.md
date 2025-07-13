 # Retrieve a Customer's PaymentMethod

Retrieves a PaymentMethod object for a given Customer.

Returns a PaymentMethod object.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new CustomerPaymentMethodService();
PaymentMethod paymentMethod = service.Get("cus_9s6XKzkNRiz8i3", "pm_1NVChw2eZvKYlo2CHxiM5E2E");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CustomerRetrievePaymentMethodParams{
  Customer: stripe.String("cus_9s6XKzkNRiz8i3"),
};
result, err := customer.RetrievePaymentMethod("pm_1NVChw2eZvKYlo2CHxiM5E2E", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Customer resource = Customer.retrieve("cus_9s6XKzkNRiz8i3", "pm_1NVChw2eZvKYlo2CHxiM5E2E");

CustomerRetrievePaymentMethodParams params = CustomerRetrievePaymentMethodParams.builder().build();

PaymentMethod paymentMethod = resource.retrievePaymentMethod(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const paymentMethod = await stripe.customers.retrievePaymentMethod(
  'cus_9s6XKzkNRiz8i3',
  'pm_1NVChw2eZvKYlo2CHxiM5E2E'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_method = stripe.Customer.retrieve_payment_method(
  "cus_9s6XKzkNRiz8i3",
  "pm_1NVChw2eZvKYlo2CHxiM5E2E",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentMethod = $stripe->customers->retrievePaymentMethod(
  'cus_9s6XKzkNRiz8i3',
  'pm_1NVChw2eZvKYlo2CHxiM5E2E',
  []
);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_method = Stripe::Customer.retrieve_payment_method(
  'cus_9s6XKzkNRiz8i3',
  'pm_1NVChw2eZvKYlo2CHxiM5E2E',
)
```

### Response

```json
{
  "id": "pm_1NVChw2eZvKYlo2CHxiM5E2E",
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
      "cvc_check": "pass"
    },
    "country": "US",
    "exp_month": 12,
    "exp_year": 2034,
    "fingerprint": "Xt5EWLLDS7FJjR1c",
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
  "created": 1689682128,
  "customer": "cus_9s6XKzkNRiz8i3",
  "livemode": false,
  "metadata": {},
  "redaction": null,
  "type": "card"
}
```