# The Meter Event object

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `event_name` (string)
  The name of the meter event. Corresponds with the `event_name` field on a meter.

- `identifier` (string)
  A unique identifier for the event.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `payload` (object)
  The payload of the event. This contains the fields corresponding to a meter’s `customer_mapping.event_payload_key` (default is `stripe_customer_id`) and `value_settings.event_payload_key` (default is `value`). Read more about the [payload](https://docs.stripe.com/docs/billing/subscriptions/usage-based/recording-usage.md#payload-key-overrides).

- `timestamp` (timestamp)
  The timestamp passed in when creating the event. Measured in seconds since the Unix epoch.

### The Meter Event object

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