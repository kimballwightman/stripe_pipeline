# Reactivate a billing meter

When a meter is reactivated, events for this meter can be accepted and you can attach the meter to a price.

Returns a billing meter.

- `id` (string, required)
  Unique identifier for the object.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new Stripe.Billing.MeterService();
Stripe.Billing.Meter meter = service.Reactivate("mtr_123");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BillingMeterReactivateParams{};
result, err := meter.Reactivate("mtr_123", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Meter resource = Meter.retrieve("mtr_123");

MeterReactivateParams params = MeterReactivateParams.builder().build();

Meter meter = resource.reactivate(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const meter = await stripe.billing.meters.reactivate('mtr_123');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

meter = stripe.billing.Meter.reactivate("mtr_123")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$meter = $stripe->billing->meters->reactivate('mtr_123', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

meter = Stripe::Billing::Meter.reactivate('mtr_123')
```

### Response

```json
{
  "id": "mtr_123",
  "object": "billing.meter",
  "created": 1704824589,
  "customer_mapping": {
    "type": "by_id",
    "event_payload_key": "stripe_customer_id"
  },
  "default_aggregation": {
    "formula": "sum"
  },
  "display_name": "Search API Calls",
  "event_name": "ai_search_api",
  "event_time_window": null,
  "livemode": false,
  "status": "active",
  "status_transitions": {
    "deactivated_at": null
  },
  "updated": 1704898330,
  "value_settings": {
    "event_payload_key": "value"
  }
}
```