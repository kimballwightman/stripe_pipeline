# List all SetupIntents

Returns a list of SetupIntents.

A dictionary with a `data` property that contains an array of up to `limit` SetupIntents, starting after SetupIntent `starting_after`. Each entry in the array is a separate SetupIntent object. If no more SetupIntents are available, the resulting array will be empty.

- `attach_to_self` (boolean, optional)
  If present, the SetupIntent’s payment method will be attached to the in-context Stripe Account.

  It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.

- `created` (object, optional)
  A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `customer` (string, optional)
  Only return SetupIntents for the customer specified by this customer ID.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `payment_method` (string, optional)
  Only return SetupIntents that associate with the specified payment method.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new SetupIntentListOptions { Limit = 3 };
var service = new SetupIntentService();
StripeList<SetupIntent> setupIntents = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.SetupIntentListParams{};
params.Limit = stripe.Int64(3)
result := setupintent.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

SetupIntentListParams params = SetupIntentListParams.builder().setLimit(3L).build();

SetupIntentCollection setupIntents = SetupIntent.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const setupIntents = await stripe.setupIntents.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

setup_intents = stripe.SetupIntent.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$setupIntents = $stripe->setupIntents->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

setup_intents = Stripe::SetupIntent.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/setup_intents",
  "has_more": false,
  "data": [
    {
      "id": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG",
      "object": "setup_intent",
      "application": null,
      "cancellation_reason": null,
      "client_secret": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe",
      "created": 1678942624,
      "customer": null,
      "description": null,
      "flow_directions": null,
      "last_setup_error": null,
      "latest_attempt": null,
      "livemode": false,
      "mandate": null,
      "metadata": {},
      "next_action": null,
      "on_behalf_of": null,
      "payment_method": null,
      "payment_method_options": {
        "card": {
          "mandate_options": null,
          "network": null,
          "request_three_d_secure": "automatic"
        }
      },
      "payment_method_types": [
        "card"
      ],
      "single_use_mandate": null,
      "status": "requires_payment_method",
      "usage": "off_session"
    }
  ]
}
```