# Create an event destination

Create a new event destination.
`id` (string)
Unique identifier for the object.
`object` (string, value is "v2.core.event_destination")
String representing the object’s type. Objects of the same type share the same value of the object field.
`amazon_eventbridge` (nullable object)
Amazon EventBridge configuration.

- `amazon_eventbridge.aws_account_id` (string)
  The AWS account ID.

- `amazon_eventbridge.aws_event_source_arn` (string)
  The ARN of the AWS event source.

- `amazon_eventbridge.aws_event_source_status` (enum)
  The state of the AWS event source.

  The event source is in active state.

  The event source is in deleted state.

  The event source is in pending state.

  The event source state cannot be retrieved.
`created` (timestamp)
Time at which the object was created.
`description` (string)
An optional description of what the event destination is used for.
`enabled_events` (array of strings)
The list of events to enable for this endpoint.
`event_payload` (enum)
Payload type of events being subscribed to.

Events from v1 APIs.

Events from v2 APIs.
`events_from` (nullable array of enums)
Where events should be routed from.

Receive events from accounts connected to the account that owns the event destination.

Receive events from the account that owns the event destination.
`livemode` (boolean)
Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
`metadata` (nullable map)
Metadata.
`name` (string)
Event destination name.
`snapshot_api_version` (nullable string)
If using the snapshot event payload, the API version events are rendered as.
`status` (enum)
Status. It can be set to either enabled or disabled.

Event destination is disabled.

Event destination is enabled.
`status_details` (nullable object)
Additional information about event destination status.

- `status_details.disabled` (nullable object)
  Details about why the event destination has been disabled.

  - `status_details.disabled.reason` (enum)
    Reason event destination has been disabled.

    Event destination has been disabled because the underlying AWS event source does not exist.

    Event destination has been disabled by user.
`type` (enum)
Event destination type.

Amazon EventBridge.

Webhook endpoint.
`updated` (timestamp)
Time at which the object was last updated.
`webhook_endpoint` (nullable object)
Webhook endpoint configuration.

- `webhook_endpoint.signing_secret` (nullable string)
  The signing secret of the webhook endpoint, only includable on creation.

- `webhook_endpoint.url` (nullable string)
  The URL of the webhook endpoint, includable.

An idempotent retry occurred with different request parameters.

- `enabled_events` (array of strings, required)
  The list of events to enable for this endpoint.

- `event_payload` (enum, required)
  Payload type of events being subscribed to.

  Events from v1 APIs.

  Events from v2 APIs.

- `name` (string, required)
  Event destination name.

- `type` (enum, required)
  Event destination type.

  Amazon EventBridge.

  Webhook endpoint.

- `amazon_eventbridge` (object, optional)
  Amazon EventBridge configuration.

  - `amazon_eventbridge.aws_account_id` (string, required)
    The AWS account ID.

  - `amazon_eventbridge.aws_region` (string, required)
    The region of the AWS event source.

- `description` (string, optional)
  An optional description of what the event destination is used for.

- `events_from` (array of enums, optional)
  Where events should be routed from.

  Receive events from accounts connected to the account that owns the event destination.

  Receive events from the account that owns the event destination.

- `include` (array of enums, optional)
  Additional fields to include in the response.

  Include parameter to expose `webhook_endpoint.signing_secret`.

  Include parameter to expose `webhook_endpoint.url`.

- `metadata` (map, optional)
  Metadata.

- `snapshot_api_version` (string, optional)
  If using the snapshot event payload, the API version events are rendered as.

- `webhook_endpoint` (object, optional)
  Webhook endpoint configuration.

  - `webhook_endpoint.url` (string, required)
    The URL of the webhook endpoint.

```dotnet
var options = new Stripe.V2.Core.EventDestinationCreateOptions
{
    Name = "My Event Destination",
    Description = "This is my event destination, I like it a lot",
    EnabledEvents = new List<string> { "v1.billing.meter.error_report_triggered" },
    Type = "webhook_endpoint",
    WebhookEndpoint = new Stripe.V2.Core.EventDestinationCreateWebhookEndpointOptions
    {
        Url = "https://example.com/my/webhook/endpoint",
    },
    EventPayload = "thin",
    Include = new List<string> { "webhook_endpoint.url" },
};
var client = new StripeClient("<<secret key>>");
var service = client.V2.Core.EventDestinations;
Stripe.V2.EventDestination eventDestination = service.Create(options);
```

```go

sc := stripe.NewClient("<<secret key>>");
params := &stripe.V2CoreEventDestinationCreateParams{
  Name: stripe.String("My Event Destination"),
  Description: stripe.String("This is my event destination, I like it a lot"),
  EnabledEvents: []*string{stripe.String("v1.billing.meter.error_report_triggered")},
  Type: stripe.String(string(stripe.V2CoreEventDestinationTypeWebhookEndpoint)),
  WebhookEndpoint: &stripe.V2CoreEventDestinationCreateWebhookEndpointParams{
    URL: stripe.String("https://example.com/my/webhook/endpoint"),
  },
  EventPayload: stripe.String(string(stripe.V2CoreEventDestinationEventPayloadThin)),
  Include: []*string{
    stripe.String(string(stripe.V2CoreEventDestinationIncludeWebhookEndpoint.url)),
  },
};
result, err := sc.V2CoreEventDestinations.Create(context.TODO(), params);
```

```java
StripeClient client = new StripeClient("<<secret key>>");

EventDestinationCreateParams params =
  EventDestinationCreateParams.builder()
    .setName("My Event Destination")
    .setDescription("This is my event destination, I like it a lot")
    .addEnabledEvent("v1.billing.meter.error_report_triggered")
    .setType(EventDestinationCreateParams.Type.WEBHOOK_ENDPOINT)
    .setWebhookEndpoint(
      EventDestinationCreateParams.WebhookEndpoint.builder()
        .setUrl("https://example.com/my/webhook/endpoint")
        .build()
    )
    .setEventPayload(EventDestinationCreateParams.EventPayload.THIN)
    .addInclude(EventDestinationCreateParams.Include.WEBHOOK_ENDPOINT__URL)
    .build();

EventDestination eventDestination = client.v2().core().eventDestinations().create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const eventDestination = await stripe.v2.core.eventDestinations.create({
  name: 'My Event Destination',
  description: 'This is my event destination, I like it a lot',
  enabled_events: ['v1.billing.meter.error_report_triggered'],
  type: 'webhook_endpoint',
  webhook_endpoint: {
    url: 'https://example.com/my/webhook/endpoint',
  },
  event_payload: 'thin',
  include: ['webhook_endpoint.url'],
});
```

```python
client = StripeClient("<<secret key>>")

event_destination = client.v2.core.event_destinations.create({
  "name": "My Event Destination",
  "description": "This is my event destination, I like it a lot",
  "enabled_events": ["v1.billing.meter.error_report_triggered"],
  "type": "webhook_endpoint",
  "webhook_endpoint": {"url": "https://example.com/my/webhook/endpoint"},
  "event_payload": "thin",
  "include": ["webhook_endpoint.url"],
})
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$eventDestination = $stripe->v2->core->eventDestinations->create([
  'name' => 'My Event Destination',
  'description' => 'This is my event destination, I like it a lot',
  'enabled_events' => ['v1.billing.meter.error_report_triggered'],
  'type' => 'webhook_endpoint',
  'webhook_endpoint' => ['url' => 'https://example.com/my/webhook/endpoint'],
  'event_payload' => 'thin',
  'include' => ['webhook_endpoint.url'],
]);
```

```ruby
client = Stripe::StripeClient.new("<<secret key>>")

event_destination = client.v2.core.event_destinations.create({
  name: 'My Event Destination',
  description: 'This is my event destination, I like it a lot',
  enabled_events: ['v1.billing.meter.error_report_triggered'],
  type: 'webhook_endpoint',
  webhook_endpoint: {url: 'https://example.com/my/webhook/endpoint'},
  event_payload: 'thin',
  include: ['webhook_endpoint.url'],
})
```

### Response

```json
{
  "id": "ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6",
  "object": "v2.core.event_destination",
  "created": "2024-10-22T16:20:09.931Z",
  "description": "This is my event destination, I like it a lot",
  "enabled_events": [
    "v1.billing.meter.error_report_triggered"
  ],
  "event_payload": "thin",
  "events_from": [
    "self"
  ],
  "livemode": false,
  "metadata": {},
  "name": "My Event Destination",
  "snapshot_api_version": null,
  "status": "enabled",
  "status_details": null,
  "type": "webhook_endpoint",
  "updated": "2024-10-22T16:20:09.937Z",
  "webhook_endpoint": {
    "signing_secret": null,
    "url": "https://example.com/my/webhook/endpoint"
  }
}
```