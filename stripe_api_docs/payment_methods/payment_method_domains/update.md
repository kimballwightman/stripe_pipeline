# Update a payment method domain

Updates an existing payment method domain.

Returns the updated payment method domain object.

- `enabled` (boolean, optional)
  Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements or Embedded Checkout.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new PaymentMethodDomainUpdateOptions { Enabled = false };
var service = new PaymentMethodDomainService();
PaymentMethodDomain paymentMethodDomain = service.Update("pmd_1Nnrer2eZvKYlo2Cips79tWl", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentMethodDomainParams{Enabled: stripe.Bool(false)};
result, err := paymentmethoddomain.Update("pmd_1Nnrer2eZvKYlo2Cips79tWl", params);
```

```java
Stripe.apiKey = "<<secret key>>";

PaymentMethodDomain resource = PaymentMethodDomain.retrieve("pmd_1Nnrer2eZvKYlo2Cips79tWl");

PaymentMethodDomainUpdateParams params =
  PaymentMethodDomainUpdateParams.builder().setEnabled(false).build();

PaymentMethodDomain paymentMethodDomain = resource.update(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const paymentMethodDomain = await stripe.paymentMethodDomains.update(
  'pmd_1Nnrer2eZvKYlo2Cips79tWl',
  {
    enabled: false,
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_method_domain = stripe.PaymentMethodDomain.modify(
  "pmd_1Nnrer2eZvKYlo2Cips79tWl",
  enabled=False,
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentMethodDomain = $stripe->paymentMethodDomains->update(
  'pmd_1Nnrer2eZvKYlo2Cips79tWl',
  ['enabled' => false]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_method_domain = Stripe::PaymentMethodDomain.update(
  'pmd_1Nnrer2eZvKYlo2Cips79tWl',
  {enabled: false},
)
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
  "enabled": false,
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