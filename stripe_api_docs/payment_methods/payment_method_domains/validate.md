# Validate an existing payment method domain

Some payment methods might require additional steps to register a domain. If the requirements weren’t satisfied when the domain was created, the payment method will be inactive on the domain.
The payment method doesn’t appear in Elements or Embedded Checkout for this domain until it is active.

To activate a payment method on an existing payment method domain, complete the required registration steps specific to the payment method, and then validate the payment method domain with this endpoint.

Related guides: [Payment method domains](https://docs.stripe.com/docs/payments/payment-methods/pmd-registration.md).

Returns the updated payment method domain object.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new PaymentMethodDomainService();
PaymentMethodDomain paymentMethodDomain = service.Validate("pmd_1Nnrer2eZvKYlo2Cips79tWl");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentMethodDomainValidateParams{};
result, err := paymentmethoddomain.Validate("pmd_1Nnrer2eZvKYlo2Cips79tWl", params);
```

```java
Stripe.apiKey = "<<secret key>>";

PaymentMethodDomain resource = PaymentMethodDomain.retrieve("pmd_1Nnrer2eZvKYlo2Cips79tWl");

PaymentMethodDomainValidateParams params = PaymentMethodDomainValidateParams.builder().build();

PaymentMethodDomain paymentMethodDomain = resource.validate(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const paymentMethodDomain = await stripe.paymentMethodDomains.validate(
  'pmd_1Nnrer2eZvKYlo2Cips79tWl'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_method_domain = stripe.PaymentMethodDomain.validate("pmd_1Nnrer2eZvKYlo2Cips79tWl")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentMethodDomain = $stripe->paymentMethodDomains->validate('pmd_1Nnrer2eZvKYlo2Cips79tWl', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_method_domain = Stripe::PaymentMethodDomain.validate('pmd_1Nnrer2eZvKYlo2Cips79tWl')
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