# Create a billing meter event adjustment

Creates a billing meter event adjustment.

Returns a billing meter event adjustment.

- `event_name` (string, required)
  The name of the meter event. Corresponds with the `event_name` field on a meter.

- `type` (enum, required)
  Specifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet.

  Cancel a single meter event by identifier.

- `cancel` (object, optional)
  Specifies which event to cancel.

  - `cancel.identifier` (string, optional)
    Unique identifier for the event. You can only cancel events within 24 hours of Stripe receiving them.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new Stripe.Billing.MeterEventAdjustmentCreateOptions
{
    Type = "cancel",
    EventName = "ai_search_api",
    Cancel = new Stripe.Billing.MeterEventAdjustmentCancelOptions { Identifier = "identifier_123" },
};
var service = new Stripe.Billing.MeterEventAdjustmentService();
Stripe.Billing.MeterEventAdjustment meterEventAdjustment = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BillingMeterEventAdjustmentParams{
  Type: stripe.String("cancel"),
  EventName: stripe.String("ai_search_api"),
  Cancel: &stripe.BillingMeterEventAdjustmentCancelParams{
    Identifier: stripe.String("identifier_123"),
  },
};
result, err := metereventadjustment.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

MeterEventAdjustmentCreateParams params =
  MeterEventAdjustmentCreateParams.builder()
    .setType(MeterEventAdjustmentCreateParams.Type.CANCEL)
    .setEventName("ai_search_api")
    .setCancel(
      MeterEventAdjustmentCreateParams.Cancel.builder().setIdentifier("identifier_123").build()
    )
    .build();

MeterEventAdjustment meterEventAdjustment = MeterEventAdjustment.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const meterEventAdjustment = await stripe.billing.meterEventAdjustments.create({
  type: 'cancel',
  event_name: 'ai_search_api',
  cancel: {
    identifier: 'identifier_123',
  },
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

meter_event_adjustment = stripe.billing.MeterEventAdjustment.create(
  type="cancel",
  event_name="ai_search_api",
  cancel={"identifier": "identifier_123"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$meterEventAdjustment = $stripe->billing->meterEventAdjustments->create([
  'type' => 'cancel',
  'event_name' => 'ai_search_api',
  'cancel' => ['identifier' => 'identifier_123'],
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

meter_event_adjustment = Stripe::Billing::MeterEventAdjustment.create({
  type: 'cancel',
  event_name: 'ai_search_api',
  cancel: {identifier: 'identifier_123'},
})
```

### Response

```json
{
  "object": "billing.meter_event_adjustment",
  "livemode": false,
  "status": "pending",
  "event_name": "ai_search_api",
  "type": "cancel",
  "cancel": {
    "identifier": "identifier_123"
  }
}
```