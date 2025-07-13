# Create a payment method domain

Creates a payment method domain.

Returns a payment method domain object.

- `domain_name` (string, required)
  The domain name that this payment method domain object represents.

- `enabled` (boolean, optional)
  Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements or Embedded Checkout.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new PaymentMethodDomainCreateOptions { DomainName = "example.com" };
var service = new PaymentMethodDomainService();
PaymentMethodDomain paymentMethodDomain = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentMethodDomainParams{DomainName: stripe.String("example.com")};
result, err := paymentmethoddomain.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

PaymentMethodDomainCreateParams params =
  PaymentMethodDomainCreateParams.builder().setDomainName("example.com").build();

PaymentMethodDomain paymentMethodDomain = PaymentMethodDomain.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const paymentMethodDomain = await stripe.paymentMethodDomains.create({
  domain_name: 'example.com',
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_method_domain = stripe.PaymentMethodDomain.create(domain_name="example.com")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentMethodDomain = $stripe->paymentMethodDomains->create(['domain_name' => 'example.com']);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_method_domain = Stripe::PaymentMethodDomain.create({domain_name: 'example.com'})
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