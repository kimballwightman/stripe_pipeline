# Create a billing meter event with synchronous validation

Creates a meter event. Events are validated synchronously, but are processed asynchronously. Supports up to 1,000 events per second in livemode. For higher rate-limits, please use meter event streams instead.
`object` (string, value is "v2.billing.meter_event")
String representing the object’s type. Objects of the same type share the same value of the object field.
`created` (timestamp)
The creation time of this meter event.
`event_name` (string)
The name of the meter event. Corresponds with the `event_name` field on a meter.
`identifier` (string)
A unique identifier for the event. If not provided, one will be generated. We recommend using a globally unique identifier for this. We’ll enforce uniqueness within a rolling 24 hour period.
`livemode` (boolean)
Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
`payload` (map)
The payload of the event. This must contain the fields corresponding to a meter’s
`customer_mapping.event_payload_key` (default is `stripe_customer_id`) and
`value_settings.event_payload_key` (default is `value`). Read more about the payload.
`timestamp` (timestamp)
The time of the event. Must be within the past 35 calendar days or up to
5 minutes in the future. Defaults to current timestamp if not specified.

The meter must be Active to submit events.

A meter event with a duplicate identifier has already been submitted.

A meter must exist to submit events.

The value must be a positive integer.

The payload must have a reference to the customer.

The payload must have a value.

Cannot create multiple usage events for the same customer, meter concurrently.

- `event_name` (string, required)
  The name of the meter event. Corresponds with the `event_name` field on a meter.

- `payload` (map, required)
  The payload of the event. This must contain the fields corresponding to a meter’s
  `customer_mapping.event_payload_key` (default is `stripe_customer_id`) and
  `value_settings.event_payload_key` (default is `value`). Read more about
  the
  [payload](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#payload-key-overrides).

- `identifier` (string, optional)
  A unique identifier for the event. If not provided, one will be generated.
  We recommend using a globally unique identifier for this. We’ll enforce
  uniqueness within a rolling 24 hour period.

- `timestamp` (timestamp, optional)
  The time of the event. Must be within the past 35 calendar days or up to
  5 minutes in the future. Defaults to current timestamp if not specified.

```dotnet
var options = new Stripe.V2.Billing.MeterEventCreateOptions
{
    Identifier = "idmp_12345678",
    EventName = "ai_search_api",
    Timestamp = DateTimeOffset.Parse("2024-06-01T12:00:00.000Z").UtcDateTime,
    Payload = new Dictionary<string, string>
    {
        { "stripe_customer_id", "cus_12345678" },
        { "value", "25" },
    },
};
var client = new StripeClient("<<secret key>>");
var service = client.V2.Billing.MeterEvents;
Stripe.V2.Billing.MeterEvent meterEvent = service.Create(options);
```

```go

sc := stripe.NewClient("<<secret key>>");
params := &stripe.V2BillingMeterEventCreateParams{
  Identifier: stripe.String("idmp_12345678"),
  EventName: stripe.String("ai_search_api"),
  Timestamp: stripe.Time(time.Now()),
  Payload: map[string]string{"stripe_customer_id": "cus_12345678", "value": "25"},
};
result, err := sc.V2BillingMeterEvents.Create(context.TODO(), params);
```

```java
StripeClient client = new StripeClient("<<secret key>>");

MeterEventCreateParams params =
  MeterEventCreateParams.builder()
    .setIdentifier("idmp_12345678")
    .setEventName("ai_search_api")
    .setTimestamp(Instant.parse("2024-06-01T12:00:00.000Z"))
    .putPayload("stripe_customer_id", "cus_12345678")
    .putPayload("value", "25")
    .build();

MeterEvent meterEvent = client.v2().billing().meterEvents().create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const meterEvent = await stripe.v2.billing.meterEvents.create({
  identifier: 'idmp_12345678',
  event_name: 'ai_search_api',
  timestamp: '2024-06-01T12:00:00.000Z',
  payload: {
    stripe_customer_id: 'cus_12345678',
    value: '25',
  },
});
```

```python
client = StripeClient("<<secret key>>")

meter_event = client.v2.billing.meter_events.create({
  "identifier": "idmp_12345678",
  "event_name": "ai_search_api",
  "timestamp": "2024-06-01T12:00:00.000Z",
  "payload": {"stripe_customer_id": "cus_12345678", "value": "25"},
})
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$meterEvent = $stripe->v2->billing->meterEvents->create([
  'identifier' => 'idmp_12345678',
  'event_name' => 'ai_search_api',
  'timestamp' => '2024-06-01T12:00:00.000Z',
  'payload' => [
    'stripe_customer_id' => 'cus_12345678',
    'value' => '25',
  ],
]);
```

```ruby
client = Stripe::StripeClient.new("<<secret key>>")

meter_event = client.v2.billing.meter_events.create({
  identifier: 'idmp_12345678',
  event_name: 'ai_search_api',
  timestamp: '2024-06-01T12:00:00.000Z',
  payload: {
    stripe_customer_id: 'cus_12345678',
    value: '25',
  },
})
```

### Response

```json
{
  "object": "v2.billing.meter_event",
  "created": "2024-06-01T12:10:00.000Z",
  "livemode": false,
  "identifier": "idmp_12345678",
  "event_name": "ai_search_api",
  "timestamp": "2024-06-01T12:00:00.000Z",
  "payload": {
    "stripe_customer_id": "cus_12345678",
    "value": "25"
  }
}
```