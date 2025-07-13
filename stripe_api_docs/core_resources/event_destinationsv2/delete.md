# Delete an event destination

Delete an event destination.
`id` (string)
Identifier for the deleted event destination.

The resource wasn’t found.

An idempotent retry occurred with different request parameters.

- `id` (string, required)
  Identifier for the event destination to delete.

```dotnet
var client = new StripeClient("<<secret key>>");
var service = client.V2.Core.EventDestinations;
Stripe.V2.EventDestination deleted = service.Delete(
    "ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6");
```

```go

sc := stripe.NewClient("<<secret key>>");
params := &stripe.V2CoreEventDestinationDeleteParams{
  ID: stripe.String("ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6"),
};
result, err := sc.V2CoreEventDestinations.Delete(context.TODO(), params);
```

```java
StripeClient client = new StripeClient("<<secret key>>");

EventDestination eventDestination =
  client.v2().core().eventDestinations().delete(
    "ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6"
  );
```

```node
const stripe = require('stripe')('<<secret key>>');

const eventDestination = await stripe.v2.core.eventDestinations.del(
  'ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6'
);
```

```python
client = StripeClient("<<secret key>>")

event_destination = client.v2.core.event_destinations.delete(
  "ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$eventDestination = $stripe->v2->core->eventDestinations->delete(
  'ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6',
  []
);
```

```ruby
client = Stripe::StripeClient.new("<<secret key>>")

deleted = client.v2.core.event_destinations.delete('ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6')
```

### Response

```json
{
  "id": "ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6"
}
```