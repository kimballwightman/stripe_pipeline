# List all event destinations

Lists all event destinations.
`data` (array of objects)
List of event destinations.

- `data.id` (string)
  Unique identifier for the object.

- `data.object` (string, value is "v2.core.event_destination")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `data.amazon_eventbridge` (nullable object)
  Amazon EventBridge configuration.

  - `data.amazon_eventbridge.aws_account_id` (string)
    The AWS account ID.

  - `data.amazon_eventbridge.aws_event_source_arn` (string)
    The ARN of the AWS event source.

  - `data.amazon_eventbridge.aws_event_source_status` (enum)
    The state of the AWS event source.

    The event source is in active state.

    The event source is in deleted state.

    The event source is in pending state.

    The event source state cannot be retrieved.

- `data.created` (timestamp)
  Time at which the object was created.

- `data.description` (string)
  An optional description of what the event destination is used for.

- `data.enabled_events` (array of strings)
  The list of events to enable for this endpoint.

- `data.event_payload` (enum)
  Payload type of events being subscribed to.

  Events from v1 APIs.

  Events from v2 APIs.

- `data.events_from` (nullable array of enums)
  Where events should be routed from.

  Receive events from accounts connected to the account that owns the event destination.

  Receive events from the account that owns the event destination.

- `data.livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `data.metadata` (nullable map)
  Metadata.

- `data.name` (string)
  Event destination name.

- `data.snapshot_api_version` (nullable string)
  If using the snapshot event payload, the API version events are rendered as.

- `data.status` (enum)
  Status. It can be set to either enabled or disabled.

  Event destination is disabled.

  Event destination is enabled.

- `data.status_details` (nullable object)
  Additional information about event destination status.

  - `data.status_details.disabled` (nullable object)
    Details about why the event destination has been disabled.

    - `data.status_details.disabled.reason` (enum)
      Reason event destination has been disabled.

      Event destination has been disabled because the underlying AWS event source does not exist.

      Event destination has been disabled by user.

- `data.type` (enum)
  Event destination type.

  Amazon EventBridge.

  Webhook endpoint.

- `data.updated` (timestamp)
  Time at which the object was last updated.

- `data.webhook_endpoint` (nullable object)
  Webhook endpoint configuration.

  - `data.webhook_endpoint.signing_secret` (nullable string)
    The signing secret of the webhook endpoint, only includable on creation.

  - `data.webhook_endpoint.url` (nullable string)
    The URL of the webhook endpoint, includable.
`next_page_url` (nullable string)
The next page url.
`previous_page_url` (nullable string)
The previous page url.

- `include` (array of enums, optional)
  Additional fields to include in the response. Currently supports `webhook_endpoint.url`.

  Include parameter to expose `webhook_endpoint.url`.

- `limit` (integer, optional)
  The page size.

- `page` (string, optional)
  The requested page.

```dotnet
var options = new Stripe.V2.Core.EventDestinationListOptions
{
    Include = new List<string> { "webhook_endpoint.url" },
};
var client = new StripeClient("<<secret key>>");
var service = client.V2.Core.EventDestinations;
Stripe.V2.StripeList<Stripe.V2.EventDestination> eventDestinations = service.List(options);
```

```go

sc := stripe.NewClient("<<secret key>>");
params := &stripe.V2CoreEventDestinationListParams{
  Include: []*string{stripe.String("webhook_endpoint.url")},
};
result := sc.V2CoreEventDestinations.List(context.TODO(), params);
```

```java
StripeClient client = new StripeClient("<<secret key>>");

EventDestinationListParams params =
  EventDestinationListParams.builder()
    .addInclude(EventDestinationListParams.Include.WEBHOOK_ENDPOINT__URL)
    .build();

StripeCollection<EventDestination> stripeCollection =
  client.v2().core().eventDestinations().list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const eventDestinations = await stripe.v2.core.eventDestinations.list({
  include: ['webhook_endpoint.url'],
});
```

```python
client = StripeClient("<<secret key>>")

event_destinations = client.v2.core.event_destinations.list({"include": ["webhook_endpoint.url"]})
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$eventDestinations = $stripe->v2->core->eventDestinations->all([
  'include' => ['webhook_endpoint.url'],
]);
```

```ruby
client = Stripe::StripeClient.new("<<secret key>>")

event_destinations = client.v2.core.event_destinations.list({include: ['webhook_endpoint.url']})
```

### Response

```json
{
  "data": [
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
      "status": "disabled",
      "status_details": {
        "disabled": {
          "reason": "user"
        }
      },
      "type": "webhook_endpoint",
      "updated": "2024-10-22T16:22:02.524Z",
      "webhook_endpoint": {
        "signing_secret": null,
        "url": null
      }
    }
  ],
  "next_page_url": null,
  "previous_page_url": null
}
```