# Retrieve a portal configuration

Retrieves a configuration that describes the functionality of the customer portal.

Returns a portal configuration object.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new Stripe.BillingPortal.ConfigurationService();
Stripe.BillingPortal.Configuration configuration = service.Get("bpc_1MrnZsLkdIwHu7ixNiQL1xPM");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BillingPortalConfigurationParams{};
result, err := configuration.Get("bpc_1MrnZsLkdIwHu7ixNiQL1xPM", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Configuration configuration = Configuration.retrieve("bpc_1MrnZsLkdIwHu7ixNiQL1xPM");
```

```node
const stripe = require('stripe')('<<secret key>>');

const configuration = await stripe.billingPortal.configurations.retrieve(
  'bpc_1MrnZsLkdIwHu7ixNiQL1xPM'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

configuration = stripe.billing_portal.Configuration.retrieve("bpc_1MrnZsLkdIwHu7ixNiQL1xPM")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$configuration = $stripe->billingPortal->configurations->retrieve(
  'bpc_1MrnZsLkdIwHu7ixNiQL1xPM',
  []
);
```

```ruby
Stripe.api_key = '<<secret key>>'

configuration = Stripe::BillingPortal::Configuration.retrieve('bpc_1MrnZsLkdIwHu7ixNiQL1xPM')
```

### Response

```json
{
  "id": "bpc_1MrnZsLkdIwHu7ixNiQL1xPM",
  "object": "billing_portal.configuration",
  "active": true,
  "application": null,
  "business_profile": {
    "headline": null,
    "privacy_policy_url": null,
    "terms_of_service_url": null
  },
  "created": 1680290736,
  "default_return_url": null,
  "features": {
    "customer_update": {
      "allowed_updates": [
        "email",
        "tax_id"
      ],
      "enabled": true
    },
    "invoice_history": {
      "enabled": true
    },
    "payment_method_update": {
      "enabled": false
    },
    "subscription_cancel": {
      "cancellation_reason": {
        "enabled": false,
        "options": [
          "too_expensive",
          "missing_features",
          "switched_service",
          "unused",
          "other"
        ]
      },
      "enabled": false,
      "mode": "at_period_end",
      "proration_behavior": "none"
    },
    "subscription_update": {
      "default_allowed_updates": [],
      "enabled": false,
      "proration_behavior": "none"
    }
  },
  "is_default": false,
  "livemode": false,
  "login_page": {
    "enabled": false,
    "url": null
  },
  "metadata": {},
  "updated": 1680290736
}
```