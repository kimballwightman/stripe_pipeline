# Retrieve a billing meter

Retrieves a billing meter given an ID.

Returns a billing meter.

- `id` (string, required)
  Unique identifier for the object.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new Stripe.Billing.MeterService();
Stripe.Billing.Meter meter = service.Get("mtr_123");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BillingMeterParams{};
result, err := meter.Get("mtr_123", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Meter meter = Meter.retrieve("mtr_123");
```

```node
const stripe = require('stripe')('<<secret key>>');

const meter = await stripe.billing.meters.retrieve('mtr_123');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

meter = stripe.billing.Meter.retrieve("mtr_123")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$meter = $stripe->billing->meters->retrieve('mtr_123', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

meter = Stripe::Billing::Meter.retrieve('mtr_123')
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