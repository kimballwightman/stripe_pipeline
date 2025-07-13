# The Customer portal configuration object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `active` (boolean)
  Whether the configuration is active and can be used to create portal sessions.

- `application` (nullable string)
  ID of the Connect Application that created the configuration.

- `business_profile` (object)
  The business information shown to customers in the portal.

  - `business_profile.headline` (nullable string)
    The messaging shown to customers in the portal.

  - `business_profile.privacy_policy_url` (nullable string)
    A link to the business’s publicly available privacy policy.

  - `business_profile.terms_of_service_url` (nullable string)
    A link to the business’s publicly available terms of service.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `default_return_url` (nullable string)
  The default URL to redirect customers to when they click on the portal’s link to return to your website. This can be [overriden](https://docs.stripe.com/docs/api/customer_portal/sessions/create.md#create_portal_session-return_url) when creating the session.

- `features` (object)
  Information about the features available in the portal.

  - `features.customer_update` (object)
    Information about updating customer details in the portal.

    - `features.customer_update.allowed_updates` (array of enums)
      The types of customer updates that are supported. When empty, customers are not updateable.

      Allow updating billing addresses.

      Allow updating email addresses.

      Allow updating names.

      Allow updating phone numbers.

      Allow updating shipping addresses.

      Allow updating tax IDs.

    - `features.customer_update.enabled` (boolean)
      Whether the feature is enabled.

  - `features.invoice_history` (object)
    Information about showing invoice history in the portal.

    - `features.invoice_history.enabled` (boolean)
      Whether the feature is enabled.

  - `features.payment_method_update` (object)
    Information about updating payment methods in the portal. View the list of supported payment methods in the [docs](https://docs.stripe.com/docs/billing/subscriptions/integrating-customer-portal.md#supported-payment-methods).

    - `features.payment_method_update.enabled` (boolean)
      Whether the feature is enabled.

  - `features.subscription_cancel` (object)
    Information about canceling subscriptions in the portal.

    - `features.subscription_cancel.cancellation_reason` (object)
      Whether the cancellation reasons will be collected in the portal and which options are exposed to the customer

      - `features.subscription_cancel.cancellation_reason.enabled` (boolean)
        Whether the feature is enabled.

      - `features.subscription_cancel.cancellation_reason.options` (array of enums)
        Which cancellation reasons will be given as options to the customer.

        Customer service was less than expected

        Quality was less than expected

        Some features are missing

        Other reason

        I’m switching to a different service

        Ease of use was less than expected

        It’s too expensive

        I don’t use the service enough

    - `features.subscription_cancel.enabled` (boolean)
      Whether the feature is enabled.

    - `features.subscription_cancel.mode` (enum)
      Whether to cancel subscriptions immediately or at the end of the billing period.

      After canceling, customers can still renew subscriptions until the billing period ends.

      Cancel subscriptions immediately.

    - `features.subscription_cancel.proration_behavior` (enum)
      Whether to create prorations when canceling subscriptions. Possible values are `none` and `create_prorations`.

  - `features.subscription_update` (object)
    Information about updating subscriptions in the portal.

    - `features.subscription_update.default_allowed_updates` (array of enums)
      The types of subscription updates that are supported for items listed in the `products` attribute. When empty, subscriptions are not updateable.

      Allow switching to a different price.

      Allow applying promotion codes to subscriptions.

      Allow updating subscription quantities.

    - `features.subscription_update.enabled` (boolean)
      Whether the feature is enabled.

    - `features.subscription_update.products` (nullable array of objects)
      The list of up to 10 products that support subscription updates.

      - `features.subscription_update.products.prices` (array of strings)
        The list of price IDs which, when subscribed to, a subscription can be updated.

      - `features.subscription_update.products.product` (string)
        The product ID.

    - `features.subscription_update.proration_behavior` (enum)
      Determines how to handle prorations resulting from subscription updates. Valid values are `none`, `create_prorations`, and `always_invoice`. Defaults to a value of `none` if you don’t set it during creation.

    - `features.subscription_update.schedule_at_period_end` (object)
      Setting to control when an update should be scheduled at the end of the period instead of applying immediately.

      - `features.subscription_update.schedule_at_period_end.conditions` (array of objects)
        List of conditions. When any condition is true, an update will be scheduled at the end of the current period.

        - `features.subscription_update.schedule_at_period_end.conditions.type` (enum)
          The type of condition.

          Schedule the update when the subscription’s item amount decreases. This can happen when changing to a cheaper price or decreasing the quantity.

          Schedule the update when the subscription’s interval is becoming shorter and no other changes to the subscription’s items are made. For example, this applies when changing from a yearly to monthly pricing interval.

- `is_default` (boolean)
  Whether the configuration is the default. If `true`, this configuration can be managed in the Dashboard and portal sessions will use this configuration unless it is overriden when creating the session.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `login_page` (object)
  The hosted login page for this configuration. Learn more about the portal login page in our [integration docs](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal#share).

  - `login_page.enabled` (boolean)
    If `true`, a shareable `url` will be generated that will take your customers to a hosted login page for the customer portal.

    If `false`, the previously generated `url`, if any, will be deactivated.

  - `login_page.url` (nullable string)
    A shareable URL to the hosted portal login page. Your customers will be able to log in with their [email](https://docs.stripe.com/docs/api/customers/object.md#customer_object-email) and receive a link to their customer portal.

- `metadata` (nullable object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `updated` (timestamp)
  Time at which the object was last updated. Measured in seconds since the Unix epoch.

### The Customer portal configuration object

```json
{
  "id": "bpc_1MrnZsLkdIwHu7ixNiQL1xPM",
  "object": "billing_portal.configuration",
  "active": true,
  "application": null,
  "business_profile": {
    "headline": null,
    "privacy_policy_url": null,
    "terms_of_service_url": null
  },
  "created": 1680290736,
  "default_return_url": null,
  "features": {
    "customer_update": {
      "allowed_updates": [
        "email",
        "tax_id"
      ],
      "enabled": true
    },
    "invoice_history": {
      "enabled": true
    },
    "payment_method_update": {
      "enabled": false
    },
    "subscription_cancel": {
      "cancellation_reason": {
        "enabled": false,
        "options": [
          "too_expensive",
          "missing_features",
          "switched_service",
          "unused",
          "other"
        ]
      },
      "enabled": false,
      "mode": "at_period_end",
      "proration_behavior": "none"
    },
    "subscription_update": {
      "default_allowed_updates": [],
      "enabled": false,
      "proration_behavior": "none"
    }
  },
  "is_default": false,
  "livemode": false,
  "login_page": {
    "enabled": false,
    "url": null
  },
  "metadata": {},
  "updated": 1680290736
}
```