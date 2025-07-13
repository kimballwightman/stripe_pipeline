# List all SetupAttempts

Returns a list of SetupAttempts that associate with a provided SetupIntent.

A dictionary with a `data` property that contains
an array of up to `limit` SetupAttempts that are created by the
specified SetupIntent, which start after SetupAttempts `starting_after`. Each
entry in the array is a separate SetupAttempts object. If no other
SetupAttempts are available, the resulting array is be empty. This
request should never raise an error.

- `setup_intent` (string, required)
  Only return SetupAttempts created by the SetupIntent specified by
  this ID.

- `created` (object, optional)
  A filter on the list, based on the object `created` field. The value
  can be a string with an integer Unix timestamp or a
  dictionary with a number of different query options.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new SetupAttemptListOptions
{
    Limit = 3,
    SetupIntent = "seti_1ErTsG2eZvKYlo2CKaT8MITz",
};
var service = new SetupAttemptService();
StripeList<SetupAttempt> setupAttempts = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.SetupAttemptListParams{
  SetupIntent: stripe.String("seti_1ErTsG2eZvKYlo2CKaT8MITz"),
};
params.Limit = stripe.Int64(3)
result := setupattempt.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

SetupAttemptListParams params =
  SetupAttemptListParams.builder()
    .setLimit(3L)
    .setSetupIntent("seti_1ErTsG2eZvKYlo2CKaT8MITz")
    .build();

SetupAttemptCollection setupAttempts = SetupAttempt.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const setupAttempts = await stripe.setupAttempts.list({
  limit: 3,
  setup_intent: 'seti_1ErTsG2eZvKYlo2CKaT8MITz',
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

setup_attempts = stripe.SetupAttempt.list(
  limit=3,
  setup_intent="seti_1ErTsG2eZvKYlo2CKaT8MITz",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$setupAttempts = $stripe->setupAttempts->all([
  'limit' => 3,
  'setup_intent' => 'seti_1ErTsG2eZvKYlo2CKaT8MITz',
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

setup_attempts = Stripe::SetupAttempt.list({
  limit: 3,
  setup_intent: 'seti_1ErTsG2eZvKYlo2CKaT8MITz',
})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/setup_attempts",
  "has_more": false,
  "data": [
    {
      "id": "setatt_1ErTsH2eZvKYlo2CI7ukcoF7",
      "object": "setup_attempt",
      "application": null,
      "created": 1562004309,
      "customer": null,
      "flow_directions": null,
      "livemode": false,
      "on_behalf_of": null,
      "payment_method": "pm_1ErTsG2eZvKYlo2CH0DNen59",
      "payment_method_details": {
        "card": {
          "three_d_secure": null
        },
        "type": "card"
      },
      "setup_error": null,
      "setup_intent": "seti_1ErTsG2eZvKYlo2CKaT8MITz",
      "status": "succeeded",
      "usage": "off_session"
    }
  ]
}
```