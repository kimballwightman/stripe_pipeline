# Update a Checkout Session

Updates a Checkout Session object.

Related guide: [Dynamically update Checkout](https://docs.stripe.com/payments/checkout/dynamic-updates.md)

Returns a Checkout Session object.

- `collected_information` (object, optional)
  Information about the customer collected within the Checkout Session. Can only be set when updating `embedded` or `custom` sessions.

  - `collected_information.shipping_details` (object, optional)
    The shipping details to apply to this Session.

    - `collected_information.shipping_details.address` (object, required)
      The address of the customer

      - `collected_information.shipping_details.address.country` (string, required)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `collected_information.shipping_details.address.line1` (string, required)
        Address line 1 (e.g., street, PO Box, or company name).

      - `collected_information.shipping_details.address.city` (string, optional)
        City, district, suburb, town, or village.

      - `collected_information.shipping_details.address.line2` (string, optional)
        Address line 2 (e.g., apartment, suite, unit, or building).

      - `collected_information.shipping_details.address.postal_code` (string, optional)
        ZIP or postal code.

      - `collected_information.shipping_details.address.state` (string, optional)
        State, county, province, or region.

    - `collected_information.shipping_details.name` (string, required)
      The name of customer

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `shipping_options` (array of objects, optional)
  The shipping rate options to apply to this Session. Up to a maximum of 5.

  - `shipping_options.shipping_rate` (string, optional)
    The ID of the Shipping Rate to use for this shipping option.

  - `shipping_options.shipping_rate_data` (object, optional)
    Parameters to be passed to Shipping Rate creation for this shipping option.

    - `shipping_options.shipping_rate_data.display_name` (string, required)
      The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.

    - `shipping_options.shipping_rate_data.delivery_estimate` (object, optional)
      The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.

      - `shipping_options.shipping_rate_data.delivery_estimate.maximum` (object, optional)
        The upper bound of the estimated range. If empty, represents no upper bound i.e., infinite.

        - `shipping_options.shipping_rate_data.delivery_estimate.maximum.unit` (enum, required)
          A unit of time.

          The delivery estimate is in business days.

          The delivery estimate is in days.

          The delivery estimate is in hours.

          The delivery estimate is in months.

          The delivery estimate is in weeks.

        - `shipping_options.shipping_rate_data.delivery_estimate.maximum.value` (integer, required)
          Must be greater than 0.

      - `shipping_options.shipping_rate_data.delivery_estimate.minimum` (object, optional)
        The lower bound of the estimated range. If empty, represents no lower bound.

        - `shipping_options.shipping_rate_data.delivery_estimate.minimum.unit` (enum, required)
          A unit of time.

          The delivery estimate is in business days.

          The delivery estimate is in days.

          The delivery estimate is in hours.

          The delivery estimate is in months.

          The delivery estimate is in weeks.

        - `shipping_options.shipping_rate_data.delivery_estimate.minimum.value` (integer, required)
          Must be greater than 0.

    - `shipping_options.shipping_rate_data.fixed_amount` (object, optional)
      Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.

      - `shipping_options.shipping_rate_data.fixed_amount.amount` (integer, required)
        A non-negative integer in cents representing how much to charge.

      - `shipping_options.shipping_rate_data.fixed_amount.currency` (enum, required)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `shipping_options.shipping_rate_data.fixed_amount.currency_options` (object, optional)
        Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

        - `shipping_options.shipping_rate_data.fixed_amount.currency_options.<currency>.amount` (integer, required)
          A non-negative integer in cents representing how much to charge.

        - `shipping_options.shipping_rate_data.fixed_amount.currency_options.<currency>.tax_behavior` (enum, optional)
          Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.

    - `shipping_options.shipping_rate_data.metadata` (object, optional)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

    - `shipping_options.shipping_rate_data.tax_behavior` (enum, optional)
      Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.

    - `shipping_options.shipping_rate_data.tax_code` (string, optional)
      A [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID. The Shipping tax code is `txcd_92010001`.

    - `shipping_options.shipping_rate_data.type` (enum, optional)
      The type of calculation to use on the shipping rate.

      The shipping rate is a fixed amount.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new Stripe.Checkout.SessionUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var service = new Stripe.Checkout.SessionService();
Stripe.Checkout.Session session = service.Update(
    "cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u",
    options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CheckoutSessionParams{};
params.AddMetadata("order_id", "6735")
result, err := session.Update(
  "cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Session resource =
  Session.retrieve("cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u");

SessionUpdateParams params = SessionUpdateParams.builder().putMetadata("order_id", "6735").build();

Session session = resource.update(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const session = await stripe.checkout.sessions.update(
  'cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

session = stripe.checkout.Session.modify(
  "cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u",
  metadata={"order_id": "6735"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$session = $stripe->checkout->sessions->update(
  'cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u',
  ['metadata' => ['order_id' => '6735']]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

session = Stripe::Checkout::Session.update(
  'cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u',
  {metadata: {order_id: '6735'}},
)
```

### Response

```json
{
  "id": "cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u",
  "object": "checkout.session",
  "after_expiration": null,
  "allow_promotion_codes": null,
  "amount_subtotal": 2198,
  "amount_total": 2198,
  "automatic_tax": {
    "enabled": false,
    "liability": null,
    "status": null
  },
  "billing_address_collection": null,
  "cancel_url": null,
  "client_reference_id": null,
  "consent": null,
  "consent_collection": null,
  "created": 1679600215,
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
  "expires_at": 1679686615,
  "invoice": null,
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
  "locale": null,
  "metadata": {
    "order_id": "6735"
  },
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
  "status": "open",
  "submit_type": null,
  "subscription": null,
  "success_url": "https://example.com/success",
  "total_details": {
    "amount_discount": 0,
    "amount_shipping": 0,
    "amount_tax": 0
  },
  "url": "https://checkout.stripe.com/c/pay/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u#fidkdWxOYHwnPyd1blpxYHZxWjA0SDdPUW5JbmFMck1wMmx9N2BLZjFEfGRUNWhqTmJ%2FM2F8bUA2SDRySkFdUV81T1BSV0YxcWJcTUJcYW5rSzN3dzBLPUE0TzRKTTxzNFBjPWZEX1NKSkxpNTVjRjN8VHE0YicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl"
}
```