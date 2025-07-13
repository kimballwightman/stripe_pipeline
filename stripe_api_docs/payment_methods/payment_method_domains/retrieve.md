# Retrieve a payment method domain

Retrieves the details of an existing payment method domain.

Returns a payment method domain object.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new PaymentMethodDomainService();
PaymentMethodDomain paymentMethodDomain = service.Get("pmd_1Nnrer2eZvKYlo2Cips79tWl");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentMethodDomainParams{};
result, err := paymentmethoddomain.Get("pmd_1Nnrer2eZvKYlo2Cips79tWl", params);
```

```java
Stripe.apiKey = "<<secret key>>";

PaymentMethodDomain paymentMethodDomain =
  PaymentMethodDomain.retrieve("pmd_1Nnrer2eZvKYlo2Cips79tWl");
```

```node
const stripe = require('stripe')('<<secret key>>');

const paymentMethodDomain = await stripe.paymentMethodDomains.retrieve(
  'pmd_1Nnrer2eZvKYlo2Cips79tWl'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_method_domain = stripe.PaymentMethodDomain.retrieve("pmd_1Nnrer2eZvKYlo2Cips79tWl")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentMethodDomain = $stripe->paymentMethodDomains->retrieve('pmd_1Nnrer2eZvKYlo2Cips79tWl', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_method_domain = Stripe::PaymentMethodDomain.retrieve('pmd_1Nnrer2eZvKYlo2Cips79tWl')
```

### Response

```json
{
  "id": "pmd_1Nnrer2eZvKYlo2Cips79tWl",
  "object": "payment_method_domain",
  "apple_pay": {
    "status": "active"
  },
  "created": 1694129445,
  "domain_name": "example.com",
  "enabled": true,
  "google_pay": {
    "status": "active"
  },
  "link": {
    "status": "active"
  },
  "livemode": false,
  "paypal": {
    "status": "active"
  }
}
```