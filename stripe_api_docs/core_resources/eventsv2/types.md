# Types of events

This is a list of all public [thin events](https://docs.stripe.com/event-destinations.md#thin-events) we currently send for /v1 and /v2 resources, which are continually evolving and expanding. The payload of thin events is unversioned. During processing, you must fetch the versioned event from the API or fetch the resource’s current state.
`id` (string)
Unique identifier for the event.
`object` (string, value is "v2.core.event")
String representing the object’s type. Objects of the same type share the same value of the object field.
`context` (nullable string)
Authentication context needed to fetch the event or related object.
`created` (timestamp)
Time at which the object was created.
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
`type` (string, value is "v1.billing.meter.error_report_triggered")
The type of the event.
`data` (object)
Additional data about the event.

- `data.developer_message_summary` (string)
  Extra field included in the event’s `data` when fetched from /v2/events.

- `data.reason` (object)
  This contains information about why meter error happens.

  - `data.reason.error_count` (integer)
    The total error count within this window.

  - `data.reason.error_types` (array of objects)
    The error details.

    - `data.reason.error_types.code` (enum)
      Enum value: archived_meter.

      Enum value: meter_event_customer_not_found.

      Enum value: meter_event_dimension_count_too_high.

      Enum value: meter_event_invalid_value.

      Enum value: meter_event_no_customer_defined.

      Enum value: missing_dimension_payload_keys.

      Enum value: no_meter.

      Enum value: timestamp_in_future.

      Enum value: timestamp_too_far_in_past.

    - `data.reason.error_types.error_count` (integer)
      The number of errors of this type.

    - `data.reason.error_types.sample_errors` (array of objects)
      A list of sample errors of this type.

      - `data.reason.error_types.sample_errors.error_message` (string)
        The error message.

      - `data.reason.error_types.sample_errors.request` (object)
        The request causes the error.

        - `data.reason.error_types.sample_errors.request.identifier` (string)
          The request idempotency key.

- `data.validation_end` (timestamp)
  The end of the window that is encapsulated by this summary.

- `data.validation_start` (timestamp)
  The start of the window that is encapsulated by this summary.

### Event handler

```curl
\# Select a client library to see examples of
# parsing and retrieving event details.
```

### Event handler

```bash
\# Select a client library to see examples of
# parsing and retrieving event details.
```

### Event handler

```ruby
client = Stripe::StripeClient.new("{{YOUR_API_KEY}}")

endpoint_secret = 'whsec_...'
signature_header = request.env['HTTP_STRIPE_SIGNATURE']

thin_event = client.parse_thin_event(
  payload,
  signature_header,
  endpoint_secret
)

event = client.v2.core.events.retrieve(thin_event.id)
```

### Event handler

```python
client = StripeClient("{{YOUR_API_KEY}}")

endpoint_secret = 'whsec_...'
signature_header = ''

thin_event = client.parse_thin_event(
  payload,
  signature_header,
  endpoint_secret
)

event = client.v2.core.events.retrieve(thin_event.id)
```

### Event handler

```php
$stripe = new StripeStripeClient('{{YOUR_API_KEY}}');

$endpoint_secret = 'whsec_...';
$signature_header = $_SERVER['HTTP_STRIPE_SIGNATURE'];

$thin_event = $client->parseThinEvent(
  $payload,
  $signature_header,
  $endpoint_secret
);

$event = $client->v2->core->events->retrieve($thin_event->id);
```

### Event handler

```java
StripeClient client = new StripeClient("{{YOUR_API_KEY}}");

String signatureHeader = request.headers("Stripe-Signature");
String endpointSecret = "whsec_...";

com.stripe.model.ThinEvent thinEvent = client.parseThinEvent(
  payload,
  signatureHeader,
  endpointSecret
);

com.stripe.model.v2.Event event = client.v2().core().events().retrieve(
  thinEvent.getId()
);
```

### Event handler

```javascript
const stripe = require('stripe')('{{YOUR_API_KEY}}');

const endpoint_secret = 'whsec_...'
const signature_header = '...'

const thinEvent = stripe.parseThinEvent(
  payload,
  signature_header,
  endpoint_secret
);

const event = await stripe.v2.core.events.retrieve(thinEvent.id);

```

### Event handler

```go
err = webhook.ValidatePayload(
  payload,
  signatureHeader,
  endpointSecret
)

if err != nil {
    fmt.Fprintf(os.Stderr, "Error reading request body: %v
", err)
    return
}

var thinEvent map[string]interface{}

if err := json.Unmarshal(payload, &thinEvent); err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to parse thin event body json: %v
", err.Error()
    )
    return
}

eventID := thinEvent["id"].(string)

var event map[string]interface{}
resp, err := client.RawRequest(
  http.MethodGet,
  "/v2/core/events/"+eventID,
  "",
  nil
)
if err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to get pull event: %v
",
      err.Error()
    )
    return
}

if err := json.Unmarshal(resp.RawJSON, &event); err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to parse pull event body json: %v
",
      err.Error()
    )
    return
}
```

### Event handler

```dotnet
var client = new StripeClient("{{YOUR_API_KEY}}");

string endpointSecret = "whsec_...";
string signatureHeader = Request.Headers["Stripe-Signature"];

var thinEvent = client.ParseThinEvent(
  payload,
  signatureHeader,
  endpointSecret
);

var event = await client.V2.Core.Events.GetAsync(thinEvent.Id);
```
`id` (string)
Unique identifier for the event.
`object` (string, value is "v2.core.event")
String representing the object’s type. Objects of the same type share the same value of the object field.
`context` (nullable string)
Authentication context needed to fetch the event or related object.
`created` (timestamp)
Time at which the object was created.
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
`type` (string, value is "v1.billing.meter.no_meter_found")
The type of the event.
`data` (object)
Additional data about the event.

- `data.developer_message_summary` (string)
  Extra field included in the event’s `data` when fetched from /v2/events.

- `data.reason` (object)
  This contains information about why meter error happens.

  - `data.reason.error_count` (integer)
    The total error count within this window.

  - `data.reason.error_types` (array of objects)
    The error details.

    - `data.reason.error_types.code` (enum)
      Enum value: archived_meter.

      Enum value: meter_event_customer_not_found.

      Enum value: meter_event_dimension_count_too_high.

      Enum value: meter_event_invalid_value.

      Enum value: meter_event_no_customer_defined.

      Enum value: missing_dimension_payload_keys.

      Enum value: no_meter.

      Enum value: timestamp_in_future.

      Enum value: timestamp_too_far_in_past.

    - `data.reason.error_types.error_count` (integer)
      The number of errors of this type.

    - `data.reason.error_types.sample_errors` (array of objects)
      A list of sample errors of this type.

      - `data.reason.error_types.sample_errors.error_message` (string)
        The error message.

      - `data.reason.error_types.sample_errors.request` (object)
        The request causes the error.

        - `data.reason.error_types.sample_errors.request.identifier` (string)
          The request idempotency key.

- `data.validation_end` (timestamp)
  The end of the window that is encapsulated by this summary.

- `data.validation_start` (timestamp)
  The start of the window that is encapsulated by this summary.

### Event handler

```curl
\# Select a client library to see examples of
# parsing and retrieving event details.
```

### Event handler

```bash
\# Select a client library to see examples of
# parsing and retrieving event details.
```

### Event handler

```ruby
client = Stripe::StripeClient.new("{{YOUR_API_KEY}}")

endpoint_secret = 'whsec_...'
signature_header = request.env['HTTP_STRIPE_SIGNATURE']

thin_event = client.parse_thin_event(
  payload,
  signature_header,
  endpoint_secret
)

event = client.v2.core.events.retrieve(thin_event.id)
```

### Event handler

```python
client = StripeClient("{{YOUR_API_KEY}}")

endpoint_secret = 'whsec_...'
signature_header = ''

thin_event = client.parse_thin_event(
  payload,
  signature_header,
  endpoint_secret
)

event = client.v2.core.events.retrieve(thin_event.id)
```

### Event handler

```php
$stripe = new StripeStripeClient('{{YOUR_API_KEY}}');

$endpoint_secret = 'whsec_...';
$signature_header = $_SERVER['HTTP_STRIPE_SIGNATURE'];

$thin_event = $client->parseThinEvent(
  $payload,
  $signature_header,
  $endpoint_secret
);

$event = $client->v2->core->events->retrieve($thin_event->id);
```

### Event handler

```java
StripeClient client = new StripeClient("{{YOUR_API_KEY}}");

String signatureHeader = request.headers("Stripe-Signature");
String endpointSecret = "whsec_...";

com.stripe.model.ThinEvent thinEvent = client.parseThinEvent(
  payload,
  signatureHeader,
  endpointSecret
);

com.stripe.model.v2.Event event = client.v2().core().events().retrieve(
  thinEvent.getId()
);
```

### Event handler

```javascript
const stripe = require('stripe')('{{YOUR_API_KEY}}');

const endpoint_secret = 'whsec_...'
const signature_header = '...'

const thinEvent = stripe.parseThinEvent(
  payload,
  signature_header,
  endpoint_secret
);

const event = await stripe.v2.core.events.retrieve(thinEvent.id);

```

### Event handler

```go
err = webhook.ValidatePayload(
  payload,
  signatureHeader,
  endpointSecret
)

if err != nil {
    fmt.Fprintf(os.Stderr, "Error reading request body: %v
", err)
    return
}

var thinEvent map[string]interface{}

if err := json.Unmarshal(payload, &thinEvent); err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to parse thin event body json: %v
", err.Error()
    )
    return
}

eventID := thinEvent["id"].(string)

var event map[string]interface{}
resp, err := client.RawRequest(
  http.MethodGet,
  "/v2/core/events/"+eventID,
  "",
  nil
)
if err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to get pull event: %v
",
      err.Error()
    )
    return
}

if err := json.Unmarshal(resp.RawJSON, &event); err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to parse pull event body json: %v
",
      err.Error()
    )
    return
}
```

### Event handler

```dotnet
var client = new StripeClient("{{YOUR_API_KEY}}");

string endpointSecret = "whsec_...";
string signatureHeader = Request.Headers["Stripe-Signature"];

var thinEvent = client.ParseThinEvent(
  payload,
  signatureHeader,
  endpointSecret
);

var event = await client.V2.Core.Events.GetAsync(thinEvent.Id);
```
`id` (string)
Unique identifier for the event.
`object` (string, value is "v2.core.event")
String representing the object’s type. Objects of the same type share the same value of the object field.
`context` (nullable string)
Authentication context needed to fetch the event or related object.
`created` (timestamp)
Time at which the object was created.
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
`type` (string, value is "v2.core.event_destination.ping")
The type of the event.
`data` (object)
Additional data about the event.

### Event payload

```json
{
  "context": null,
  "created": "2025-01-01T00:00:00.000Z",
  "id": "evt_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u",
  "object": "v2.core.event",
  "reason": {
    "type": "request",
    "request": {
      "id": "req_v24sUK2aV6o01RdVU",
      "idempotency_key": "fe21992d-e123-3f8c-bc90-fec93712bcb2"
    }
  },
  "related_object": {
    "id": "ed_65SDS7HTasdQYsDClFT16CGd2aE2kBpeAvvRnBUcS2me",
    "type": "v2.core.event_destination",
    "url": "/v2/core/event_destinations/ed_65SDS7HTasdQYsDClFT16CGd2aE2kBpeAvvRnBUcS2me"
  },
  "type": "v2.core.event_destination.ping",
  "livemode": true
}
```

### Event handler

```curl
\# Select a client library to see examples of
# parsing and retrieving event details.
```

### Event handler

```bash
\# Select a client library to see examples of
# parsing and retrieving event details.
```

### Event handler

```ruby
client = Stripe::StripeClient.new("{{YOUR_API_KEY}}")

endpoint_secret = 'whsec_...'
signature_header = request.env['HTTP_STRIPE_SIGNATURE']

thin_event = client.parse_thin_event(
  payload,
  signature_header,
  endpoint_secret
)

event = client.v2.core.events.retrieve(thin_event.id)
```

### Event handler

```python
client = StripeClient("{{YOUR_API_KEY}}")

endpoint_secret = 'whsec_...'
signature_header = ''

thin_event = client.parse_thin_event(
  payload,
  signature_header,
  endpoint_secret
)

event = client.v2.core.events.retrieve(thin_event.id)
```

### Event handler

```php
$stripe = new StripeStripeClient('{{YOUR_API_KEY}}');

$endpoint_secret = 'whsec_...';
$signature_header = $_SERVER['HTTP_STRIPE_SIGNATURE'];

$thin_event = $client->parseThinEvent(
  $payload,
  $signature_header,
  $endpoint_secret
);

$event = $client->v2->core->events->retrieve($thin_event->id);
```

### Event handler

```java
StripeClient client = new StripeClient("{{YOUR_API_KEY}}");

String signatureHeader = request.headers("Stripe-Signature");
String endpointSecret = "whsec_...";

com.stripe.model.ThinEvent thinEvent = client.parseThinEvent(
  payload,
  signatureHeader,
  endpointSecret
);

com.stripe.model.v2.Event event = client.v2().core().events().retrieve(
  thinEvent.getId()
);
```

### Event handler

```javascript
const stripe = require('stripe')('{{YOUR_API_KEY}}');

const endpoint_secret = 'whsec_...'
const signature_header = '...'

const thinEvent = stripe.parseThinEvent(
  payload,
  signature_header,
  endpoint_secret
);

const event = await stripe.v2.core.events.retrieve(thinEvent.id);

```

### Event handler

```go
err = webhook.ValidatePayload(
  payload,
  signatureHeader,
  endpointSecret
)

if err != nil {
    fmt.Fprintf(os.Stderr, "Error reading request body: %v
", err)
    return
}

var thinEvent map[string]interface{}

if err := json.Unmarshal(payload, &thinEvent); err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to parse thin event body json: %v
", err.Error()
    )
    return
}

eventID := thinEvent["id"].(string)

var event map[string]interface{}
resp, err := client.RawRequest(
  http.MethodGet,
  "/v2/core/events/"+eventID,
  "",
  nil
)
if err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to get pull event: %v
",
      err.Error()
    )
    return
}

if err := json.Unmarshal(resp.RawJSON, &event); err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to parse pull event body json: %v
",
      err.Error()
    )
    return
}
```

### Event handler

```dotnet
var client = new StripeClient("{{YOUR_API_KEY}}");

string endpointSecret = "whsec_...";
string signatureHeader = Request.Headers["Stripe-Signature"];

var thinEvent = client.ParseThinEvent(
  payload,
  signatureHeader,
  endpointSecret
);

var event = await client.V2.Core.Events.GetAsync(thinEvent.Id);
```

### Fetched payload

```json
{
  "context": null,
  "created": "2025-01-01T00:00:00.000Z",
  "id": "evt_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u",
  "object": "v2.core.event",
  "reason": {
    "type": "request",
    "request": {
      "id": "req_v24sUK2aV6o01RdVU",
      "idempotency_key": "fe21992d-e123-3f8c-bc90-fec93712bcb2"
    }
  },
  "related_object": {
    "id": "ed_65SDS7HTasdQYsDClFT16CGd2aE2kBpeAvvRnBUcS2me",
    "type": "v2.core.event_destination",
    "url": "/v2/core/event_destinations/ed_65SDS7HTasdQYsDClFT16CGd2aE2kBpeAvvRnBUcS2me"
  },
  "type": "v2.core.event_destination.ping",
  "livemode": true,
  "changes": {},
  "data": {}
}
```