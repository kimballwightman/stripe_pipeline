# Create billing meter event stream authentication session

Creates a meter event session to send usage on the high-throughput meter event stream. Authentication tokens are only valid for 15 minutes, so you will need to create a new meter event session when your token expires.
`id` (string)
The unique id of this auth session.
`object` (string, value is "v2.billing.meter_event_session")
String representing the object’s type. Objects of the same type share the same value of the object field.
`authentication_token` (string)
The authentication token for this session.  Use this token when calling the
high-throughput meter event API.
`created` (timestamp)
The creation time of this session.
`expires_at` (timestamp)
The time at which this session will expire.
`livemode` (boolean)
Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.


```dotnet
var options = new Stripe.V2.Billing.MeterEventSessionCreateOptions();
var client = new StripeClient("<<secret key>>");
var service = client.V2.Billing.MeterEventSession;
Stripe.V2.Billing.MeterEventSession meterEventSession = service.Create(options);
```

```go

sc := stripe.NewClient("<<secret key>>");
params := &stripe.V2BillingMeterEventSessionCreateParams{};
result, err := sc.V2BillingMeterEventSessions.Create(context.TODO(), params);
```

```java
StripeClient client = new StripeClient("<<secret key>>");

MeterEventSession meterEventSession = client.v2().billing().meterEventSession().create();
```

```node
const stripe = require('stripe')('<<secret key>>');

const meterEventSession = await stripe.v2.billing.meterEventSession.create();
```

```python
client = StripeClient("<<secret key>>")

meter_event_session = client.v2.billing.meter_event_session.create()
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$meterEventSession = $stripe->v2->billing->meterEventSession->create([]);
```

```ruby
client = Stripe::StripeClient.new("<<secret key>>")

meter_event_session = client.v2.billing.meter_event_session.create()
```

### Response

```json
{
  "id": "<AUTH_SESSION_ID>",
  "livemode": "false",
  "object": "v2.billing.meter_event_session",
  "authentication_token": "token_12345678",
  "created": "2024-06-01T12:00:00.000Z",
  "expires_at": "2024-06-01T12:15:00.000Z"
}
```