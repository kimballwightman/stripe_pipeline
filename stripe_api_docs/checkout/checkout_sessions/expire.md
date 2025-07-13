# Expire a Checkout Session

A Checkout Session can be expired when it is in one of these statuses: `open`

After it expires, a customer can’t complete a Checkout Session and customers loading the Checkout Session see a message saying the Checkout Session is expired.

Returns a Checkout Session object if the expiration succeeded. Returns an error if the Checkout Session has already expired or isn’t in an expireable state.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new Stripe.Checkout.SessionService();
Stripe.Checkout.Session session = service.Expire(
    "cs_test_a1Ae6ClgOkjygKwrf9B3L6ITtUuZW4Xx9FivL6DZYoYFdfAefQxsYpJJd3");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CheckoutSessionExpireParams{};
result, err := session.Expire(
  "cs_test_a1Ae6ClgOkjygKwrf9B3L6ITtUuZW4Xx9FivL6DZYoYFdfAefQxsYpJJd3", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Session resource =
  Session.retrieve("cs_test_a1Ae6ClgOkjygKwrf9B3L6ITtUuZW4Xx9FivL6DZYoYFdfAefQxsYpJJd3");

SessionExpireParams params = SessionExpireParams.builder().build();

Session session = resource.expire(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const session = await stripe.checkout.sessions.expire(
  'cs_test_a1Ae6ClgOkjygKwrf9B3L6ITtUuZW4Xx9FivL6DZYoYFdfAefQxsYpJJd3'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

session = stripe.checkout.Session.expire(
  "cs_test_a1Ae6ClgOkjygKwrf9B3L6ITtUuZW4Xx9FivL6DZYoYFdfAefQxsYpJJd3",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$session = $stripe->checkout->sessions->expire(
  'cs_test_a1Ae6ClgOkjygKwrf9B3L6ITtUuZW4Xx9FivL6DZYoYFdfAefQxsYpJJd3',
  []
);
```

```ruby
Stripe.api_key = '<<secret key>>'

session = Stripe::Checkout::Session.expire('cs_test_a1Ae6ClgOkjygKwrf9B3L6ITtUuZW4Xx9FivL6DZYoYFdfAefQxsYpJJd3')
```

### Response

```json
{
  "id": "cs_test_a1Ae6ClgOkjygKwrf9B3L6ITtUuZW4Xx9FivL6DZYoYFdfAefQxsYpJJd3",
  "object": "checkout.session",
  "after_expiration": null,
  "allow_promotion_codes": null,
  "amount_subtotal": 2198,
  "amount_total": 2198,
  "automatic_tax": {
    "enabled": false,
    "status": null
  },
  "billing_address_collection": null,
  "cancel_url": null,
  "client_reference_id": null,
  "consent": null,
  "consent_collection": null,
  "created": 1679434412,
  "currency": "usd",
  "custom_fields": [],
  "custom_text": {
    "shipping_address": null,
    "submit": null
  },
  "customer": null,
  "customer_creation": "if_required",
  "customer_details": null,
  "customer_email": null,
  "expires_at": 1679520812,
  "invoice": null,
  "invoice_creation": {
    "enabled": false,
    "invoice_data": {
      "account_tax_ids": null,
      "custom_fields": null,
      "description": null,
      "footer": null,
      "metadata": {},
      "rendering_options": null
    }
  },
  "livemode": false,
  "locale": null,
  "metadata": {},
  "mode": "payment",
  "payment_intent": null,
  "payment_link": null,
  "payment_method_collection": "always",
  "payment_method_options": {},
  "payment_method_types": [
    "card"
  ],
  "payment_status": "unpaid",
  "phone_number_collection": {
    "enabled": false
  },
  "recovered_from": null,
  "setup_intent": null,
  "shipping_address_collection": null,
  "shipping_cost": null,
  "shipping_details": null,
  "shipping_options": [],
  "status": "expired",
  "submit_type": null,
  "subscription": null,
  "success_url": "https://example.com/success",
  "total_details": {
    "amount_discount": 0,
    "amount_shipping": 0,
    "amount_tax": 0
  },
  "url": null
}
```