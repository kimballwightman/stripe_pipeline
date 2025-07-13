# List all payment links

Returns a list of your payment links.

A dictionary with a `data` property that contains an array of up to `limit` payment links, starting after payment link `starting_after`. Each entry in the array is a separate payment link object. If no more payment links are available, the resulting array will be empty. This request should never raise an error.

- `active` (boolean, optional)
  Only return payment links that are active or inactive (e.g., pass `false` to list all inactive payment links).

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new PaymentLinkListOptions { Limit = 3 };
var service = new PaymentLinkService();
StripeList<PaymentLink> paymentLinks = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentLinkListParams{};
params.Limit = stripe.Int64(3)
result := paymentlink.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

PaymentLinkListParams params = PaymentLinkListParams.builder().setLimit(3L).build();

PaymentLinkCollection paymentLinks = PaymentLink.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const paymentLinks = await stripe.paymentLinks.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_links = stripe.PaymentLink.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentLinks = $stripe->paymentLinks->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_links = Stripe::PaymentLink.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/payment_links",
  "has_more": false,
  "data": [
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
  ]
}
```