# Retrieve a SetupIntent

Retrieves the details of a SetupIntent that has previously been created.

Client-side retrieval using a publishable key is allowed when the `client_secret` is provided in the query string.

When retrieved with a publishable key, only a subset of properties will be returned. Please refer to the [SetupIntent](#setup_intent_object) object reference for more details.

Returns a SetupIntent if a valid identifier was provided.

- `client_secret` (string, required)
  The client secret of the SetupIntent. We require this string if you use a publishable key to retrieve the SetupIntent.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new SetupIntentService();
SetupIntent setupIntent = service.Get("seti_1Mm8s8LkdIwHu7ix0OXBfTRG");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.SetupIntentParams{};
result, err := setupintent.Get("seti_1Mm8s8LkdIwHu7ix0OXBfTRG", params);
```

```java
Stripe.apiKey = "<<secret key>>";

SetupIntent setupIntent = SetupIntent.retrieve("seti_1Mm8s8LkdIwHu7ix0OXBfTRG");
```

```node
const stripe = require('stripe')('<<secret key>>');

const setupIntent = await stripe.setupIntents.retrieve('seti_1Mm8s8LkdIwHu7ix0OXBfTRG');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

setup_intent = stripe.SetupIntent.retrieve("seti_1Mm8s8LkdIwHu7ix0OXBfTRG")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$setupIntent = $stripe->setupIntents->retrieve('seti_1Mm8s8LkdIwHu7ix0OXBfTRG', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

setup_intent = Stripe::SetupIntent.retrieve('seti_1Mm8s8LkdIwHu7ix0OXBfTRG')
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
  "status": "requires_payment_method",
  "usage": "off_session"
}
```