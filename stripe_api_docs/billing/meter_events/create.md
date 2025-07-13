# Create a billing meter event

Creates a billing meter event.

Returns a billing meter event.

- `event_name` (string, required)
  The name of the meter event. Corresponds with the `event_name` field on a meter.

- `payload` (object, required)
  The payload of the event. This must contain the fields corresponding to a meter’s `customer_mapping.event_payload_key` (default is `stripe_customer_id`) and `value_settings.event_payload_key` (default is `value`). Read more about the [payload](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#payload-key-overrides).

- `identifier` (string, optional)
  A unique identifier for the event. If not provided, one is generated. We recommend using UUID-like identifiers. We will enforce uniqueness within a rolling period of at least 24 hours. The enforcement of uniqueness primarily addresses issues arising from accidental retries or other problems occurring within extremely brief time intervals. This approach helps prevent duplicate entries and ensures data integrity in high-frequency operations.

- `timestamp` (timestamp, optional)
  The time of the event. Measured in seconds since the Unix epoch. Must be within the past 35 calendar days or up to 5 minutes in the future. Defaults to current timestamp if not specified.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new Stripe.Billing.MeterEventCreateOptions
{
    EventName = "ai_search_api",
    Payload = new Dictionary<string, string>
    {
        { "value", "25" },
        { "stripe_customer_id", "cus_NciAYcXfLnqBoz" },
    },
    Identifier = "identifier_123",
};
var service = new Stripe.Billing.MeterEventService();
Stripe.Billing.MeterEvent meterEvent = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BillingMeterEventParams{
  EventName: stripe.String("ai_search_api"),
  Payload: map[string]string{"value": "25", "stripe_customer_id": "cus_NciAYcXfLnqBoz"},
  Identifier: stripe.String("identifier_123"),
};
result, err := meterevent.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

MeterEventCreateParams params =
  MeterEventCreateParams.builder()
    .setEventName("ai_search_api")
    .putPayload("value", "25")
    .putPayload("stripe_customer_id", "cus_NciAYcXfLnqBoz")
    .setIdentifier("identifier_123")
    .build();

MeterEvent meterEvent = MeterEvent.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const meterEvent = await stripe.billing.meterEvents.create({
  event_name: 'ai_search_api',
  payload: {
    value: '25',
    stripe_customer_id: 'cus_NciAYcXfLnqBoz',
  },
  identifier: 'identifier_123',
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

meter_event = stripe.billing.MeterEvent.create(
  event_name="ai_search_api",
  payload={"value": "25", "stripe_customer_id": "cus_NciAYcXfLnqBoz"},
  identifier="identifier_123",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$meterEvent = $stripe->billing->meterEvents->create([
  'event_name' => 'ai_search_api',
  'payload' => [
    'value' => '25',
    'stripe_customer_id' => 'cus_NciAYcXfLnqBoz',
  ],
  'identifier' => 'identifier_123',
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

meter_event = Stripe::Billing::MeterEvent.create({
  event_name: 'ai_search_api',
  payload: {
    value: '25',
    stripe_customer_id: 'cus_NciAYcXfLnqBoz',
  },
  identifier: 'identifier_123',
})
```

### Response

```json
{
  "object": "billing.meter_event",
  "created": 1704824589,
  "event_name": "ai_search_api",
  "identifier": "identifier_123",
  "livemode": true,
  "payload": {
    "value": "25",
    "stripe_customer_id": "cus_NciAYcXfLnqBoz"
  },
  "timestamp": 1680210639
}
```