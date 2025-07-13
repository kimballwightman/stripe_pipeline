# The Customer Portal Session object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `configuration` (string)
  The configuration used by this session, describing the features available.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `customer` (string)
  The ID of the customer for this session.

- `flow` (nullable object)
  Information about a specific flow for the customer to go through. See the [docs](https://docs.stripe.com/docs/customer-management/portal-deep-links.md) to learn more about using customer portal deep links and flows.

  - `flow.after_completion` (object)
    Behavior after the flow is completed.

    - `flow.after_completion.hosted_confirmation` (nullable object)
      Configuration when `after_completion.type=hosted_confirmation`.

      - `flow.after_completion.hosted_confirmation.custom_message` (nullable string)
        A custom message to display to the customer after the flow is completed.

    - `flow.after_completion.redirect` (nullable object)
      Configuration when `after_completion.type=redirect`.

      - `flow.after_completion.redirect.return_url` (string)
        The URL the customer will be redirected to after the flow is completed.

    - `flow.after_completion.type` (enum)
      The specified type of behavior after the flow is completed.

      Displays a confirmation message on the hosted surface after the flow is complete

      Redirects to the portal homepage after the flow is complete.

      Redirects the customer to the specified `redirect.return_url` after the flow is complete.

  - `flow.subscription_cancel` (nullable object)
    Configuration when `flow.type=subscription_cancel`.

    - `flow.subscription_cancel.retention` (nullable object)
      Specify a retention strategy to be used in the cancellation flow.

      - `flow.subscription_cancel.retention.coupon_offer` (nullable object)
        Configuration when `retention.type=coupon_offer`.

        - `flow.subscription_cancel.retention.coupon_offer.coupon` (string)
          The ID of the coupon to be offered.

      - `flow.subscription_cancel.retention.type` (enum)
        Type of retention strategy that will be used.

        Offer customers a coupon as a retention strategy.

    - `flow.subscription_cancel.subscription` (string)
      The ID of the subscription to be canceled.

  - `flow.subscription_update` (nullable object)
    Configuration when `flow.type=subscription_update`.

    - `flow.subscription_update.subscription` (string)
      The ID of the subscription to be updated.

  - `flow.subscription_update_confirm` (nullable object)
    Configuration when `flow.type=subscription_update_confirm`.

    - `flow.subscription_update_confirm.discounts` (nullable array of objects)
      The coupon or promotion code to apply to this subscription update.

      - `flow.subscription_update_confirm.discounts.coupon` (nullable string)
        The ID of the coupon to apply to this subscription update.

      - `flow.subscription_update_confirm.discounts.promotion_code` (nullable string)
        The ID of a promotion code to apply to this subscription update.

    - `flow.subscription_update_confirm.subscription` (string)
      The ID of the subscription to be updated.

  - `flow.type` (enum)
    Type of flow that the customer will go through.

    Customer will be able to add a new payment method. The payment method will be set as the [`customer.invoice_settings.default_payment_method`](https://docs.stripe.com/docs/api/customers/object.md#customer_object-invoice_settings-default_payment_method).

    Customer will be able to cancel their subscription.

    Customer will be able to select prices to update to based on the configuration’s [`features.subscription_update`](https://docs.stripe.com/docs/api/customer_portal/configuration.md#portal_configuration_object-features-subscription_update).

    Customer will be able to confirm a specified subscription update.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `locale` (nullable enum)
  The IETF language tag of the locale Customer Portal is displayed in. If blank or auto, the customer’s `preferred_locales` or browser’s locale is used.

- `on_behalf_of` (nullable string)
  The account for which the session was created on behalf of. When specified, only subscriptions and invoices with this `on_behalf_of` account appear in the portal. For more information, see the [docs](https://docs.stripe.com/docs/connect/separate-charges-and-transfers.md#settlement-merchant). Use the [Accounts API](https://docs.stripe.com/docs/api/accounts/object.md#account_object-settings-branding) to modify the `on_behalf_of` account’s branding settings, which the portal displays.

- `return_url` (nullable string)
  The URL to redirect customers to when they click on the portal’s link to return to your website.

- `url` (string)
  The short-lived URL of the session that gives customers access to the customer portal.

### The Customer Portal Session object

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