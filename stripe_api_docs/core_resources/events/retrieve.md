# Retrieve an event

Retrieves the details of an event if it was created in the last 30 days. Supply the unique identifier of the event, which you might have received in a webhook.

Returns an event object if a valid identifier was provided. All events share a common structure, detailed to the right. The only property that will differ is the `data` property.

In each case, the `data` dictionary will have an attribute called `object` and its value will be the same as retrieving the same object directly from the API. For example, a `customer.created` event will have the same information as retrieving the relevant customer would.

In cases where the attributes of an object have changed, `data` will also contain a dictionary containing the changes.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new EventService();
Event result = service.Get("evt_1NG8Du2eZvKYlo2CUI79vXWy");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.EventParams{};
result, err := event.Get("evt_1NG8Du2eZvKYlo2CUI79vXWy", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Event event = Event.retrieve("evt_1NG8Du2eZvKYlo2CUI79vXWy");
```

```node
const stripe = require('stripe')('<<secret key>>');

const event = await stripe.events.retrieve('evt_1NG8Du2eZvKYlo2CUI79vXWy');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

event = stripe.Event.retrieve("evt_1NG8Du2eZvKYlo2CUI79vXWy")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$event = $stripe->events->retrieve('evt_1NG8Du2eZvKYlo2CUI79vXWy', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

event = Stripe::Event.retrieve('evt_1NG8Du2eZvKYlo2CUI79vXWy')
```

### Response

```json
{
  "id": "evt_1NG8Du2eZvKYlo2CUI79vXWy",
  "object": "event",
  "api_version": "2019-02-19",
  "created": 1686089970,
  "data": {
    "object": {
      "id": "seti_1NG8Du2eZvKYlo2C9XMqbR0x",
      "object": "setup_intent",
      "application": null,
      "automatic_payment_methods": null,
      "cancellation_reason": null,
      "client_secret": "seti_1NG8Du2eZvKYlo2C9XMqbR0x_secret_O2CdhLwGFh2Aej7bCY7qp8jlIuyR8DJ",
      "created": 1686089970,
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
      "payment_method": "pm_1NG8Du2eZvKYlo2CYzzldNr7",
      "payment_method_options": {
        "acss_debit": {
          "currency": "cad",
          "mandate_options": {
            "interval_description": "First day of every month",
            "payment_schedule": "interval",
            "transaction_type": "personal"
          },
          "verification_method": "automatic"
        }
      },
      "payment_method_types": [
        "acss_debit"
      ],
      "single_use_mandate": null,
      "status": "requires_confirmation",
      "usage": "off_session"
    }
  },
  "livemode": false,
  "pending_webhooks": 0,
  "request": {
    "id": null,
    "idempotency_key": null
  },
  "type": "setup_intent.created"
}
```