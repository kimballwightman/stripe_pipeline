# Retrieve a Mandate

Retrieves a Mandate object.

Returns a Mandate object.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new MandateService();
Mandate mandate = service.Get("mandate_1MvojA2eZvKYlo2CvqTABjZs");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.MandateParams{};
result, err := mandate.Get("mandate_1MvojA2eZvKYlo2CvqTABjZs", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Mandate mandate = Mandate.retrieve("mandate_1MvojA2eZvKYlo2CvqTABjZs");
```

```node
const stripe = require('stripe')('<<secret key>>');

const mandate = await stripe.mandates.retrieve('mandate_1MvojA2eZvKYlo2CvqTABjZs');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

mandate = stripe.Mandate.retrieve("mandate_1MvojA2eZvKYlo2CvqTABjZs")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$mandate = $stripe->mandates->retrieve('mandate_1MvojA2eZvKYlo2CvqTABjZs', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

mandate = Stripe::Mandate.retrieve('mandate_1MvojA2eZvKYlo2CvqTABjZs')
```

### Response

```json
{
  "id": "mandate_1MvojA2eZvKYlo2CvqTABjZs",
  "object": "mandate",
  "customer_acceptance": {
    "accepted_at": 123456789,
    "online": {
      "ip_address": "127.0.0.0",
      "user_agent": "device"
    },
    "type": "online"
  },
  "livemode": false,
  "multi_use": {},
  "payment_method": "pm_123456789",
  "payment_method_details": {
    "sepa_debit": {
      "reference": "123456789",
      "url": ""
    },
    "type": "sepa_debit"
  },
  "status": "active",
  "type": "multi_use"
}
```