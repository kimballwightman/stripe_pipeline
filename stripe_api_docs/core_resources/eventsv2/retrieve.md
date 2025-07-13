# Retrieve an Event object

Retrieves the details of an event.
`id` (string)
Unique identifier for the event.
`object` (string, value is "v2.core.event")
String representing the object’s type. Objects of the same type share the same value of the object field.
`context` (nullable string)
Authentication context needed to fetch the event or related object.
`created` (timestamp)
Time at which the object was created.
`data` (nullable object)
Additional data about the event.
`livemode` (boolean)
Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
`reason` (nullable object)
Reason for the event.

- `reason.request` (nullable object)
  Information on the API request that instigated the event.

  - `reason.request.id` (string)
    ID of the API request that caused the event.

  - `reason.request.idempotency_key` (string)
    The idempotency key transmitted during the request.

- `reason.type` (enum)
  Event reason type.

  The event was published as the result of an API request.
`related_object` (nullable object)
Object containing the reference to API resource relevant to the event.

- `related_object.id` (string)
  Unique identifier for the object relevant to the event.

- `related_object.type` (string)
  Object tag of the resource relevant to the event.

- `related_object.url` (string)
  URL to retrieve the resource.
`type` (string)
The type of the event.

The resource wasn’t found.

- `id` (string, required)
  Unique identifier for the object.

```dotnet
var client = new StripeClient("<<secret key>>");
var service = client.V2.Core.Events;
Stripe.V2.Event result = service.Get("evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u");
```

```go

sc := stripe.NewClient("<<secret key>>");
params := &stripe.V2CoreEventRetrieveParams{
  ID: stripe.String("evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u"),
};
result, err := sc.V2CoreEvents.Retrieve(context.TODO(), params);
```

```java
StripeClient client = new StripeClient("<<secret key>>");

Event event =
  client.v2().core().events().retrieve("evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u");
```

```node
const stripe = require('stripe')('<<secret key>>');

const event = await stripe.v2.core.events.retrieve(
  'evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u'
);
```

```python
client = StripeClient("<<secret key>>")

event = client.v2.core.events.retrieve("evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$event = $stripe->v2->core->events->retrieve(
  'evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u',
  []
);
```

```ruby
client = Stripe::StripeClient.new("<<secret key>>")

event = client.v2.core.events.retrieve('evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u')
```

### Response

```json
{
  "id": "evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u",
  "object": "v2.core.event",
  "context": null,
  "created": "2024-09-26T17:46:22.134Z",
  "data": {
    "developer_message_summary": "There is 1 invalid event",
    "reason": {
      "error_count": 1,
      "error_types": [
        {
          "code": "meter_event_no_customer_defined",
          "error_count": 1,
          "sample_errors": [
            {
              "error_message": "Customer mapping key stripe_customer_id not found in payload.",
              "request": {
                "identifier": "cb447754-6880-45c2-8f2f-ef19b6ce81e9"
              }
            }
          ]
        }
      ]
    },
    "validation_end": "2024-09-26T17:46:20.000Z",
    "validation_start": "2024-09-26T17:46:10.000Z"
  },
  "livemode": false,
  "reason": null,
  "related_object": {
    "id": "mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc",
    "type": "billing.meter",
    "url": "/v1/billing/meters/mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc"
  },
  "type": "v1.billing.meter.error_report_triggered"
}
```