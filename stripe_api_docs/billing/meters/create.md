# Create a billing meter

Creates a billing meter.

Returns a billing meter.

- `default_aggregation` (object, required)
  The default settings to aggregate a meter’s events with.

  - `default_aggregation.formula` (enum, required)
    Specifies how events are aggregated. Allowed values are `count` to count the number of events, `sum` to sum each event’s value and `last` to take the last event’s value in the window.

    Count the number of events.

    Sum each event’s value.

- `display_name` (string, required)
  The meter’s name. Not visible to the customer.

- `event_name` (string, required)
  The name of the meter event to record usage for. Corresponds with the `event_name` field on meter events.

- `customer_mapping` (object, optional)
  Fields that specify how to map a meter event to a customer.

  - `customer_mapping.event_payload_key` (string, required)
    The key in the meter event payload to use for mapping the event to a customer.

  - `customer_mapping.type` (enum, required)
    The method for mapping a meter event to a customer. Must be `by_id`.

    Map a meter event to a customer by passing a customer ID in the event’s payload.

- `event_time_window` (enum, optional)
  The time window to pre-aggregate meter events for, if any.

  Events are pre-aggregated in daily buckets.

  Events are pre-aggregated in hourly buckets.

- `value_settings` (object, optional)
  Fields that specify how to calculate a meter event’s value.

  - `value_settings.event_payload_key` (string, required)
    The key in the usage event payload to use as the value for this meter. For example, if the event payload contains usage on a `bytes_used` field, then set the event_payload_key to “bytes_used”.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new Stripe.Billing.MeterCreateOptions
{
    DisplayName = "Search API Calls",
    EventName = "ai_search_api",
    DefaultAggregation = new Stripe.Billing.MeterDefaultAggregationOptions { Formula = "sum" },
    ValueSettings = new Stripe.Billing.MeterValueSettingsOptions { EventPayloadKey = "value" },
    CustomerMapping = new Stripe.Billing.MeterCustomerMappingOptions
    {
        Type = "by_id",
        EventPayloadKey = "stripe_customer_id",
    },
};
var service = new Stripe.Billing.MeterService();
Stripe.Billing.Meter meter = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BillingMeterParams{
  DisplayName: stripe.String("Search API Calls"),
  EventName: stripe.String("ai_search_api"),
  DefaultAggregation: &stripe.BillingMeterDefaultAggregationParams{
    Formula: stripe.String(string(stripe.BillingMeterDefaultAggregationFormulaSum)),
  },
  ValueSettings: &stripe.BillingMeterValueSettingsParams{EventPayloadKey: stripe.String("value")},
  CustomerMapping: &stripe.BillingMeterCustomerMappingParams{
    Type: stripe.String("by_id"),
    EventPayloadKey: stripe.String("stripe_customer_id"),
  },
};
result, err := meter.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

MeterCreateParams params =
  MeterCreateParams.builder()
    .setDisplayName("Search API Calls")
    .setEventName("ai_search_api")
    .setDefaultAggregation(
      MeterCreateParams.DefaultAggregation.builder()
        .setFormula(MeterCreateParams.DefaultAggregation.Formula.SUM)
        .build()
    )
    .setValueSettings(MeterCreateParams.ValueSettings.builder().setEventPayloadKey("value").build())
    .setCustomerMapping(
      MeterCreateParams.CustomerMapping.builder()
        .setType(MeterCreateParams.CustomerMapping.Type.BY_ID)
        .setEventPayloadKey("stripe_customer_id")
        .build()
    )
    .build();

Meter meter = Meter.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const meter = await stripe.billing.meters.create({
  display_name: 'Search API Calls',
  event_name: 'ai_search_api',
  default_aggregation: {
    formula: 'sum',
  },
  value_settings: {
    event_payload_key: 'value',
  },
  customer_mapping: {
    type: 'by_id',
    event_payload_key: 'stripe_customer_id',
  },
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

meter = stripe.billing.Meter.create(
  display_name="Search API Calls",
  event_name="ai_search_api",
  default_aggregation={"formula": "sum"},
  value_settings={"event_payload_key": "value"},
  customer_mapping={"type": "by_id", "event_payload_key": "stripe_customer_id"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$meter = $stripe->billing->meters->create([
  'display_name' => 'Search API Calls',
  'event_name' => 'ai_search_api',
  'default_aggregation' => ['formula' => 'sum'],
  'value_settings' => ['event_payload_key' => 'value'],
  'customer_mapping' => [
    'type' => 'by_id',
    'event_payload_key' => 'stripe_customer_id',
  ],
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

meter = Stripe::Billing::Meter.create({
  display_name: 'Search API Calls',
  event_name: 'ai_search_api',
  default_aggregation: {formula: 'sum'},
  value_settings: {event_payload_key: 'value'},
  customer_mapping: {
    type: 'by_id',
    event_payload_key: 'stripe_customer_id',
  },
})
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
  "updated": 1704824589,
  "value_settings": {
    "event_payload_key": "value"
  }
}
```