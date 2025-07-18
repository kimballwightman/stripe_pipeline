# Retrieve payment link

Retrieve a payment link.

Returns the payment link.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new PaymentLinkService();
PaymentLink paymentLink = service.Get("plink_1MoC3ULkdIwHu7ixZjtGpVl2");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentLinkParams{};
result, err := paymentlink.Get("plink_1MoC3ULkdIwHu7ixZjtGpVl2", params);
```

```java
Stripe.apiKey = "<<secret key>>";

PaymentLink paymentLink = PaymentLink.retrieve("plink_1MoC3ULkdIwHu7ixZjtGpVl2");
```

```node
const stripe = require('stripe')('<<secret key>>');

const paymentLink = await stripe.paymentLinks.retrieve('plink_1MoC3ULkdIwHu7ixZjtGpVl2');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_link = stripe.PaymentLink.retrieve("plink_1MoC3ULkdIwHu7ixZjtGpVl2")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentLink = $stripe->paymentLinks->retrieve('plink_1MoC3ULkdIwHu7ixZjtGpVl2', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_link = Stripe::PaymentLink.retrieve('plink_1MoC3ULkdIwHu7ixZjtGpVl2')
```

### Response

```json
{
  "id": "plink_1MoC3ULkdIwHu7ixZjtGpVl2",
  "object": "payment_link",
  "active": true,
  "after_completion": {
    "hosted_confirmation": {
      "custom_message": null
    },
    "type": "hosted_confirmation"
  },
  "allow_promotion_codes": false,
  "application_fee_amount": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null
  },
  "billing_address_collection": "auto",
  "consent_collection": null,
  "currency": "usd",
  "custom_fields": [],
  "custom_text": {
    "shipping_address": null,
    "submit": null
  },
  "customer_creation": "if_required",
  "invoice_creation": {
    "enabled": false,
    "invoice_data": {
      "account_tax_ids": null,
      "custom_fields": null,
      "description": null,
      "footer": null,
      "issuer": null,
      "metadata": {},
      "rendering_options": null
    }
  },
  "livemode": false,
  "metadata": {},
  "on_behalf_of": null,
  "payment_intent_data": null,
  "payment_method_collection": "always",
  "payment_method_types": null,
  "phone_number_collection": {
    "enabled": false
  },
  "shipping_address_collection": null,
  "shipping_options": [],
  "submit_type": "auto",
  "subscription_data": {
    "description": null,
    "invoice_settings": {
      "issuer": {
        "type": "self"
      }
    },
    "trial_period_days": null
  },
  "tax_id_collection": {
    "enabled": false
  },
  "transfer_data": null,
  "url": "https://buy.stripe.com/test_cN25nr0iZ7bUa7meUY"
}
```