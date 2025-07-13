# The Meter Event Adjustment object

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `cancel` (nullable object)
  Specifies which event to cancel.

  - `cancel.identifier` (nullable string)
    Unique identifier for the event.

- `event_name` (string)
  The name of the meter event. Corresponds with the `event_name` field on a meter.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `status` (enum)
  The meter event adjustment’s status.

  The event adjustment has been processed.

  The event adjustment is still being processed.

- `type` (enum)
  Specifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet.

  Cancel a single meter event by identifier.

### The Meter Event Adjustment object

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