# List payment method domains

Lists the details of existing payment method domains.

Returns a list of payment method domain objects.

- `domain_name` (string, optional)
  The domain name that this payment method domain object represents.

- `enabled` (boolean, optional)
  Whether this payment method domain is enabled. If the domain is not enabled, payment methods will not appear in Elements or Embedded Checkout

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new PaymentMethodDomainListOptions { Limit = 3 };
var service = new PaymentMethodDomainService();
StripeList<PaymentMethodDomain> paymentMethodDomains = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentMethodDomainListParams{};
params.Limit = stripe.Int64(3)
result := paymentmethoddomain.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

PaymentMethodDomainListParams params = PaymentMethodDomainListParams.builder().setLimit(3L).build();

PaymentMethodDomainCollection paymentMethodDomains = PaymentMethodDomain.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const paymentMethodDomains = await stripe.paymentMethodDomains.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_method_domains = stripe.PaymentMethodDomain.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentMethodDomains = $stripe->paymentMethodDomains->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_method_domains = Stripe::PaymentMethodDomain.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/payment_method_domains",
  "has_more": false,
  "data": [
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
  ]
}
```