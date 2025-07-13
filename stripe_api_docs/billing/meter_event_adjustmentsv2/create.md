# Create a billing meter event adjustment

Creates a meter event adjustment to cancel a previously sent meter event.
`id` (string)
The unique id of this meter event adjustment.
`object` (string, value is "v2.billing.meter_event_adjustment")
String representing the object’s type. Objects of the same type share the same value of the object field.
`cancel` (object)
Specifies which event to cancel.

- `cancel.identifier` (string)
  Unique identifier for the event. You can only cancel events within 24 hours of Stripe receiving them.
`created` (timestamp)
The time the adjustment was created.
`event_name` (string)
The name of the meter event. Corresponds with the `event_name` field on a meter.
`livemode` (boolean)
Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
`status` (enum)
The meter event adjustment’s status.

The event adjustment has been processed.

The event adjustment is still being processed.
`type` (enum)
Specifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet.

Cancel a single meter event by identifier.

The adjustment configuration is invalid for the adjustment type.

- `cancel` (object, required)
  Specifies which event to cancel.

  - `cancel.identifier` (string, required)
    Unique identifier for the event. You can only cancel events within 24 hours of Stripe receiving them.

- `event_name` (string, required)
  The name of the meter event. Corresponds with the `event_name` field on a meter.

- `type` (enum, required)
  Specifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet.

  Cancel a single meter event by identifier.

```dotnet
var options = new Stripe.V2.Billing.MeterEventAdjustmentCreateOptions
{
    EventName = "ai_search_api",
    Type = "cancel",
    Cancel = new Stripe.V2.Billing.MeterEventAdjustmentCreateCancelOptions
    {
        Identifier = "idmp_12345678",
    },
};
var client = new StripeClient("<<secret key>>");
var service = client.V2.Billing.MeterEventAdjustments;
Stripe.V2.Billing.MeterEventAdjustment meterEventAdjustment = service.Create(options);
```

```go

sc := stripe.NewClient("<<secret key>>");
params := &stripe.V2BillingMeterEventAdjustmentCreateParams{
  EventName: stripe.String("ai_search_api"),
  Type: stripe.String("cancel"),
  Cancel: &stripe.V2BillingMeterEventAdjustmentCreateCancelParams{
    Identifier: stripe.String("idmp_12345678"),
  },
};
result, err := sc.V2BillingMeterEventAdjustments.Create(context.TODO(), params);
```

```java
StripeClient client = new StripeClient("<<secret key>>");

MeterEventAdjustmentCreateParams params =
  MeterEventAdjustmentCreateParams.builder()
    .setEventName("ai_search_api")
    .setType(MeterEventAdjustmentCreateParams.Type.CANCEL)
    .setCancel(
      MeterEventAdjustmentCreateParams.Cancel.builder().setIdentifier("idmp_12345678").build()
    )
    .build();

MeterEventAdjustment meterEventAdjustment =
  client.v2().billing().meterEventAdjustments().create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const meterEventAdjustment = await stripe.v2.billing.meterEventAdjustments.create({
  event_name: 'ai_search_api',
  type: 'cancel',
  cancel: {
    identifier: 'idmp_12345678',
  },
});
```

```python
client = StripeClient("<<secret key>>")

meter_event_adjustment = client.v2.billing.meter_event_adjustments.create({
  "event_name": "ai_search_api",
  "type": "cancel",
  "cancel": {"identifier": "idmp_12345678"},
})
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$meterEventAdjustment = $stripe->v2->billing->meterEventAdjustments->create([
  'event_name' => 'ai_search_api',
  'type' => 'cancel',
  'cancel' => ['identifier' => 'idmp_12345678'],
]);
```

```ruby
client = Stripe::StripeClient.new("<<secret key>>")

meter_event_adjustment = client.v2.billing.meter_event_adjustments.create({
  event_name: 'ai_search_api',
  type: 'cancel',
  cancel: {identifier: 'idmp_12345678'},
})
```

### Response

```json
{
  "object": "v2.billing.meter_event_adjustment",
  "id": "mtr_event_adj_12345678",
  "livemode": false,
  "created": "2024-06-01T12:00:00.000Z",
  "status": "pending",
  "event_name": "ai_search_api",
  "type": "cancel",
  "cancel": {
    "identifier": "idmp_12345678"
  }
}
```