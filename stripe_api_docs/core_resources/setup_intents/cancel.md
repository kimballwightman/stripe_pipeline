# Cancel a SetupIntent

You can cancel a SetupIntent object when it’s in one of these statuses: `requires_payment_method`, `requires_confirmation`, or `requires_action`.

After you cancel it, setup is abandoned and any operations on the SetupIntent fail with an error. You can’t cancel the SetupIntent for a Checkout Session. [Expire the Checkout Session](https://docs.stripe.com/docs/api/checkout/sessions/expire.md) instead.

Returns a SetupIntent object if the cancellation succeeds. Returns an error if the SetupIntent is already canceled or isn’t in a cancelable state.

- `cancellation_reason` (string, optional)
  Reason for canceling this SetupIntent. Possible values are: `abandoned`, `requested_by_customer`, or `duplicate`

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new SetupIntentService();
SetupIntent setupIntent = service.Cancel("seti_1Mm8s8LkdIwHu7ix0OXBfTRG");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.SetupIntentCancelParams{};
result, err := setupintent.Cancel("seti_1Mm8s8LkdIwHu7ix0OXBfTRG", params);
```

```java
Stripe.apiKey = "<<secret key>>";

SetupIntent resource = SetupIntent.retrieve("seti_1Mm8s8LkdIwHu7ix0OXBfTRG");

SetupIntentCancelParams params = SetupIntentCancelParams.builder().build();

SetupIntent setupIntent = resource.cancel(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const setupIntent = await stripe.setupIntents.cancel('seti_1Mm8s8LkdIwHu7ix0OXBfTRG');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

setup_intent = stripe.SetupIntent.cancel("seti_1Mm8s8LkdIwHu7ix0OXBfTRG")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$setupIntent = $stripe->setupIntents->cancel('seti_1Mm8s8LkdIwHu7ix0OXBfTRG', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

setup_intent = Stripe::SetupIntent.cancel('seti_1Mm8s8LkdIwHu7ix0OXBfTRG')
```

### Response

```json
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
  "status": "canceled",
  "usage": "off_session"
}
```