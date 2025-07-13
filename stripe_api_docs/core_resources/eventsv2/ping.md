# Ping an event destination

Send a `ping` event to an event destination.
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
  Identifier for the event destination to ping.

```dotnet
var client = new StripeClient("<<secret key>>");
var service = client.V2.Core.EventDestinations;
Stripe.V2.Event result = service.Ping("evt_test_65RM8sQH2oXnebF5Rpc16RJyfa2xSQLHJJh1sxm7H0KI92");
```

```go

sc := stripe.NewClient("<<secret key>>");
params := &stripe.V2CoreEventDestinationPingParams{
  ID: stripe.String("evt_test_65RM8sQH2oXnebF5Rpc16RJyfa2xSQLHJJh1sxm7H0KI92"),
};
result, err := sc.V2CoreEventDestinations.Ping(context.TODO(), params);
```

```java
StripeClient client = new StripeClient("<<secret key>>");

Event event =
  client.v2().core().eventDestinations().ping(
    "evt_test_65RM8sQH2oXnebF5Rpc16RJyfa2xSQLHJJh1sxm7H0KI92"
  );
```

```node
const stripe = require('stripe')('<<secret key>>');

const event = await stripe.v2.core.eventDestinations.ping(
  'evt_test_65RM8sQH2oXnebF5Rpc16RJyfa2xSQLHJJh1sxm7H0KI92'
);
```

```python
client = StripeClient("<<secret key>>")

event = client.v2.core.event_destinations.ping(
  "evt_test_65RM8sQH2oXnebF5Rpc16RJyfa2xSQLHJJh1sxm7H0KI92",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$event = $stripe->v2->core->eventDestinations->ping(
  'evt_test_65RM8sQH2oXnebF5Rpc16RJyfa2xSQLHJJh1sxm7H0KI92',
  []
);
```

```ruby
client = Stripe::StripeClient.new("<<secret key>>")

event = client.v2.core.event_destinations.ping('evt_test_65RM8sQH2oXnebF5Rpc16RJyfa2xSQLHJJh1sxm7H0KI92')
```

### Response

```json
{
  "id": "evt_test_65RM8sQH2oXnebF5Rpc16RJyfa2xSQLHJJh1sxm7H0KI92",
  "object": "v2.core.event",
  "context": null,
  "created": "2024-10-22T16:26:54.063Z",
  "data": null,
  "livemode": false,
  "reason": null,
  "related_object": {
    "id": "ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6",
    "type": "event_destination",
    "url": "/v2/core/event_destinations/ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6"
  },
  "type": "v2.core.event_destination.ping"
}
```