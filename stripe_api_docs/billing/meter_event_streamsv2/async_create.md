# Create a billing meter event with asynchronous validation

Creates meter events. Events are processed asynchronously, including validation. Requires a meter event session for authentication. Supports up to 10,000 requests per second in livemode. For even higher rate-limits, contact sales.

The temporary session token has expired.

- `events` (array of objects, required)
  List of meter events to include in the request.

  - `events.event_name` (string, required)
    The name of the meter event. Corresponds with the `event_name` field on a meter.

  - `events.identifier` (string, optional)
    A unique identifier for the event. If not provided, one will be generated.
    We recommend using a globally unique identifier for this. We’ll enforce
    uniqueness within a rolling 24 hour period.

  - `events.payload` (map, required)
    The payload of the event. This must contain the fields corresponding to a meter’s
    `customer_mapping.event_payload_key` (default is `stripe_customer_id`) and
    `value_settings.event_payload_key` (default is `value`). Read more about
    the
    [payload](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#payload-key-overrides).

  - `events.timestamp` (timestamp, optional)
    The time of the event. Must be within the past 35 calendar days or up to
    5 minutes in the future. Defaults to current timestamp if not specified.

```dotnet
var options = new Stripe.V2.Billing.MeterEventStreamCreateOptions
{
    Events = new List<Stripe.V2.Billing.MeterEventStreamCreateEventOptions>
    {
        new Stripe.V2.Billing.MeterEventStreamCreateEventOptions
        {
            Identifier = "idmp_12345678",
            EventName = "ai_search_api",
            Timestamp = DateTimeOffset.Parse("2024-06-01T12:00:00.000Z").UtcDateTime,
            Payload = new Dictionary<string, string>
            {
                { "stripe_customer_id", "cus_12345678" },
                { "value", "25" },
            },
        },
    },
};
var client = new StripeClient("<<secret key>>");
var service = client.V2.Billing.MeterEventStream;
service.Create(options);
```

```go

sc := stripe.NewClient("<<secret key>>");
params := &stripe.V2BillingMeterEventStreamCreateParams{
  Events: []*stripe.V2BillingMeterEventStreamCreateEventParams{
    &stripe.V2BillingMeterEventStreamCreateEventParams{
      Identifier: stripe.String("idmp_12345678"),
      EventName: stripe.String("ai_search_api"),
      Timestamp: stripe.Time(time.Now()),
      Payload: map[string]string{"stripe_customer_id": "cus_12345678", "value": "25"},
    },
  },
};
result, err := sc.V2BillingMeterEventStreams.Create(context.TODO(), params);
```

```java
StripeClient client = new StripeClient("<<secret key>>");

MeterEventStreamCreateParams params =
  MeterEventStreamCreateParams.builder()
    .addEvent(
      MeterEventStreamCreateParams.Event.builder()
        .setIdentifier("idmp_12345678")
        .setEventName("ai_search_api")
        .setTimestamp(Instant.parse("2024-06-01T12:00:00.000Z"))
        .putPayload("stripe_customer_id", "cus_12345678")
        .putPayload("value", "25")
        .build()
    )
    .build();

client.v2().billing().meterEventStream().create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const emptyObject = await stripe.v2.billing.meterEventStream.create({
  events: [
    {
      identifier: 'idmp_12345678',
      event_name: 'ai_search_api',
      timestamp: '2024-06-01T12:00:00.000Z',
      payload: {
        stripe_customer_id: 'cus_12345678',
        value: '25',
      },
    },
  ],
});
```

```python
client = StripeClient("<<secret key>>")

empty_object = client.v2.billing.meter_event_stream.create({
  "events": [
    {
      "identifier": "idmp_12345678",
      "event_name": "ai_search_api",
      "timestamp": "2024-06-01T12:00:00.000Z",
      "payload": {"stripe_customer_id": "cus_12345678", "value": "25"},
    },
  ],
})
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$emptyObject = $stripe->v2->billing->meterEventStream->create([
  'events' => [
    [
      'identifier' => 'idmp_12345678',
      'event_name' => 'ai_search_api',
      'timestamp' => '2024-06-01T12:00:00.000Z',
      'payload' => [
        'stripe_customer_id' => 'cus_12345678',
        'value' => '25',
      ],
    ],
  ],
]);
```

```ruby
client = Stripe::StripeClient.new("<<secret key>>")

empty_object = client.v2.billing.meter_event_stream.create({
  events: [
    {
      identifier: 'idmp_12345678',
      event_name: 'ai_search_api',
      timestamp: '2024-06-01T12:00:00.000Z',
      payload: {
        stripe_customer_id: 'cus_12345678',
        value: '25',
      },
    },
  ],
})
```

### Response

```json
{}
```