# Update a billing meter

Updates a billing meter.

Returns a billing meter.

- `id` (string, required)
  Unique identifier for the object.

- `display_name` (string, optional)
  The meter’s name. Not visible to the customer.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new Stripe.Billing.MeterUpdateOptions { DisplayName = "Updated Display Name" };
var service = new Stripe.Billing.MeterService();
Stripe.Billing.Meter meter = service.Update("mtr_123", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BillingMeterParams{DisplayName: stripe.String("Updated Display Name")};
result, err := meter.Update("mtr_123", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Meter resource = Meter.retrieve("mtr_123");

MeterUpdateParams params =
  MeterUpdateParams.builder().setDisplayName("Updated Display Name").build();

Meter meter = resource.update(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const meter = await stripe.billing.meters.update(
  'mtr_123',
  {
    display_name: 'Updated Display Name',
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

meter = stripe.billing.Meter.modify(
  "mtr_123",
  display_name="Updated Display Name",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$meter = $stripe->billing->meters->update('mtr_123', ['display_name' => 'Updated Display Name']);
```

```ruby
Stripe.api_key = '<<secret key>>'

meter = Stripe::Billing::Meter.update('mtr_123', {display_name: 'Updated Display Name'})
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
  "display_name": "Updated Display Name",
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