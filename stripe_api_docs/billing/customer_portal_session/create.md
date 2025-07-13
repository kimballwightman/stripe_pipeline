# Create a portal session

Creates a session of the customer portal.

Returns a portal session object.

- `customer` (string, optional)
  The ID of an existing customer.

- `configuration` (string, optional)
  The ID of an existing [configuration](https://docs.stripe.com/docs/api/customer_portal/configuration.md) to use for this session, describing its functionality and features. If not specified, the session uses the default configuration.

- `flow_data` (object, optional)
  Information about a specific flow for the customer to go through. See the [docs](https://docs.stripe.com/docs/customer-management/portal-deep-links.md) to learn more about using customer portal deep links and flows.

  - `flow_data.type` (enum, required)
    Type of flow that the customer will go through.

    Customer will be able to add a new payment method. The payment method will be set as the [`customer.invoice_settings.default_payment_method`](https://docs.stripe.com/docs/api/customers/object.md#customer_object-invoice_settings-default_payment_method).

    Customer will be able to cancel their subscription.

    Customer will be able to select prices to update to based on the configuration’s [`features.subscription_update`](https://docs.stripe.com/docs/api/customer_portal/configuration.md#portal_configuration_object-features-subscription_update).

    Customer will be able to confirm a specified subscription update.

  - `flow_data.after_completion` (object, optional)
    Behavior after the flow is completed.

    - `flow_data.after_completion.type` (enum, required)
      The specified behavior after the flow is completed.

      Displays a confirmation message on the hosted surface after the flow is complete

      Redirects to the portal homepage after the flow is complete.

      Redirects the customer to the specified `redirect.return_url` after the flow is complete.

    - `flow_data.after_completion.hosted_confirmation` (object, optional)
      Configuration when `after_completion.type=hosted_confirmation`.

      - `flow_data.after_completion.hosted_confirmation.custom_message` (string, optional)
        A custom message to display to the customer after the flow is completed.

    - `flow_data.after_completion.redirect` (object, optional)
      Configuration when `after_completion.type=redirect`.

      - `flow_data.after_completion.redirect.return_url` (string, required)
        The URL the customer will be redirected to after the flow is completed.

  - `flow_data.subscription_cancel` (object, optional)
    Configuration when `flow_data.type=subscription_cancel`.

    - `flow_data.subscription_cancel.subscription` (string, required)
      The ID of the subscription to be canceled.

    - `flow_data.subscription_cancel.retention` (object, optional)
      Specify a retention strategy to be used in the cancellation flow.

      - `flow_data.subscription_cancel.retention.coupon_offer` (object, required)
        Configuration when `retention.type=coupon_offer`.

        - `flow_data.subscription_cancel.retention.coupon_offer.coupon` (string, required)
          The ID of the coupon to be offered.

      - `flow_data.subscription_cancel.retention.type` (enum, required)
        Type of retention strategy to use with the customer.

  - `flow_data.subscription_update` (object, optional)
    Configuration when `flow_data.type=subscription_update`.

    - `flow_data.subscription_update.subscription` (string, required)
      The ID of the subscription to be updated.

  - `flow_data.subscription_update_confirm` (object, optional)
    Configuration when `flow_data.type=subscription_update_confirm`.

    - `flow_data.subscription_update_confirm.subscription` (string, required)
      The ID of the subscription to be updated.

    - `flow_data.subscription_update_confirm.discounts` (array of objects, optional)
      The coupon or promotion code to apply to this subscription update.

      - `flow_data.subscription_update_confirm.discounts.coupon` (string, optional)
        The ID of the coupon to apply to this subscription update.

      - `flow_data.subscription_update_confirm.discounts.promotion_code` (string, optional)
        The ID of a promotion code to apply to this subscription update.

- `locale` (enum, optional)
  The IETF language tag of the locale customer portal is displayed in. If blank or auto, the customer’s `preferred_locales` or browser’s locale is used.

- `on_behalf_of` (string, optional)
  The `on_behalf_of` account to use for this session. When specified, only subscriptions and invoices with this `on_behalf_of` account appear in the portal. For more information, see the [docs](https://docs.stripe.com/docs/connect/separate-charges-and-transfers.md#settlement-merchant). Use the [Accounts API](https://docs.stripe.com/docs/api/accounts/object.md#account_object-settings-branding) to modify the `on_behalf_of` account’s branding settings, which the portal displays.

- `return_url` (string, optional)
  The default URL to redirect customers to when they click on the portal’s link to return to your website.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new Stripe.BillingPortal.SessionCreateOptions
{
    Customer = "cus_NciAYcXfLnqBoz",
    ReturnUrl = "https://example.com/account",
};
var service = new Stripe.BillingPortal.SessionService();
Stripe.BillingPortal.Session session = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BillingPortalSessionParams{
  Customer: stripe.String("cus_NciAYcXfLnqBoz"),
  ReturnURL: stripe.String("https://example.com/account"),
};
result, err := session.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

SessionCreateParams params =
  SessionCreateParams.builder()
    .setCustomer("cus_NciAYcXfLnqBoz")
    .setReturnUrl("https://example.com/account")
    .build();

Session session = Session.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const session = await stripe.billingPortal.sessions.create({
  customer: 'cus_NciAYcXfLnqBoz',
  return_url: 'https://example.com/account',
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

session = stripe.billing_portal.Session.create(
  customer="cus_NciAYcXfLnqBoz",
  return_url="https://example.com/account",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$session = $stripe->billingPortal->sessions->create([
  'customer' => 'cus_NciAYcXfLnqBoz',
  'return_url' => 'https://example.com/account',
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

session = Stripe::BillingPortal::Session.create({
  customer: 'cus_NciAYcXfLnqBoz',
  return_url: 'https://example.com/account',
})
```

### Response

```json
{
  "id": "bps_1MrSjzLkdIwHu7ixex0IvU9b",
  "object": "billing_portal.session",
  "configuration": "bpc_1MAhNDLkdIwHu7ixckACO1Jq",
  "created": 1680210639,
  "customer": "cus_NciAYcXfLnqBoz",
  "flow": null,
  "livemode": false,
  "locale": null,
  "on_behalf_of": null,
  "return_url": "https://example.com/account",
  "url": "https://billing.stripe.com/p/session/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9OY2lBYjJXcHY4a2NPck96UjBEbFVYRnU5bjlwVUF50100BUtQs3bl"
}
```