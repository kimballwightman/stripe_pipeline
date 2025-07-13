# Create a portal configuration

Creates a configuration that describes the functionality and behavior of a PortalSession

Returns a portal configuration object.

- `features` (object, required)
  Information about the features available in the portal.

  - `features.customer_update` (object, optional)
    Information about updating the customer details in the portal.

    - `features.customer_update.enabled` (boolean, required)
      Whether the feature is enabled.

    - `features.customer_update.allowed_updates` (array of enums, optional)
      The types of customer updates that are supported. When empty, customers are not updateable.

      Allow updating billing addresses.

      Allow updating email addresses.

      Allow updating names.

      Allow updating phone numbers.

      Allow updating shipping addresses.

      Allow updating tax IDs.

  - `features.invoice_history` (object, optional)
    Information about showing the billing history in the portal.

    - `features.invoice_history.enabled` (boolean, required)
      Whether the feature is enabled.

  - `features.payment_method_update` (object, optional)
    Information about updating payment methods in the portal.

    - `features.payment_method_update.enabled` (boolean, required)
      Whether the feature is enabled.

  - `features.subscription_cancel` (object, optional)
    Information about canceling subscriptions in the portal.

    - `features.subscription_cancel.enabled` (boolean, required)
      Whether the feature is enabled.

    - `features.subscription_cancel.cancellation_reason` (object, optional)
      Whether the cancellation reasons will be collected in the portal and which options are exposed to the customer

      - `features.subscription_cancel.cancellation_reason.enabled` (boolean, required)
        Whether the feature is enabled.

      - `features.subscription_cancel.cancellation_reason.options` (array of enums, required)
        Which cancellation reasons will be given as options to the customer.

        Customer service was less than expected

        Quality was less than expected

        Some features are missing

        Other reason

        I’m switching to a different service

        Ease of use was less than expected

        It’s too expensive

        I don’t use the service enough

    - `features.subscription_cancel.mode` (enum, optional)
      Whether to cancel subscriptions immediately or at the end of the billing period.

      After canceling, customers can still renew subscriptions until the billing period ends.

      Cancel subscriptions immediately.

    - `features.subscription_cancel.proration_behavior` (enum, optional)
      Whether to create prorations when canceling subscriptions. Possible values are `none` and `create_prorations`, which is only compatible with `mode=immediately`. Passing `always_invoice` will result in an error. No prorations are generated when canceling a subscription at the end of its natural billing period.

  - `features.subscription_update` (object, optional)
    Information about updating subscriptions in the portal.

    - `features.subscription_update.enabled` (boolean, required)
      Whether the feature is enabled.

    - `features.subscription_update.default_allowed_updates` (array of enums, optional)
      The types of subscription updates that are supported. When empty, subscriptions are not updateable.

      Allow switching to a different price.

      Allow applying promotion codes to subscriptions.

      Allow updating subscription quantities.

    - `features.subscription_update.products` (array of objects, optional)
      The list of up to 10 products that support subscription updates.

      - `features.subscription_update.products.prices` (array of strings, required)
        The list of price IDs for the product that a subscription can be updated to.

      - `features.subscription_update.products.product` (string, required)
        The product id.

    - `features.subscription_update.proration_behavior` (enum, optional)
      Determines how to handle prorations resulting from subscription updates. Valid values are `none`, `create_prorations`, and `always_invoice`.

    - `features.subscription_update.schedule_at_period_end` (object, optional)
      Setting to control when an update should be scheduled at the end of the period instead of applying immediately.

      - `features.subscription_update.schedule_at_period_end.conditions` (array of objects, optional)
        List of conditions. When any condition is true, the update will be scheduled at the end of the current period.

        - `features.subscription_update.schedule_at_period_end.conditions.type` (enum, required)
          The type of condition.

          Schedule the update when the subscription’s item amount decreases. This can happen when changing to a cheaper price or decreasing the quantity.

          Schedule the update when the subscription’s interval is becoming shorter and no other changes to the subscription’s items are made. For example, this applies when changing from a yearly to monthly pricing interval.

- `business_profile` (object, optional)
  The business information shown to customers in the portal.

  - `business_profile.headline` (string, optional)
    The messaging shown to customers in the portal.

  - `business_profile.privacy_policy_url` (string, optional)
    A link to the business’s publicly available privacy policy.

  - `business_profile.terms_of_service_url` (string, optional)
    A link to the business’s publicly available terms of service.

- `default_return_url` (string, optional)
  The default URL to redirect customers to when they click on the portal’s link to return to your website. This can be [overriden](https://docs.stripe.com/docs/api/customer_portal/sessions/create.md#create_portal_session-return_url) when creating the session.

- `login_page` (object, optional)
  The hosted login page for this configuration. Learn more about the portal login page in our [integration docs](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal#share).

  - `login_page.enabled` (boolean, required)
    Set to `true` to generate a shareable URL [`login_page.url`](https://docs.stripe.com/docs/api/customer_portal/configuration.md#portal_configuration_object-login_page-url) that will take your customers to a hosted login page for the customer portal.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new Stripe.BillingPortal.ConfigurationCreateOptions
{
    Features = new Stripe.BillingPortal.ConfigurationFeaturesOptions
    {
        CustomerUpdate = new Stripe.BillingPortal.ConfigurationFeaturesCustomerUpdateOptions
        {
            AllowedUpdates = new List<string> { "email", "tax_id" },
            Enabled = true,
        },
        InvoiceHistory = new Stripe.BillingPortal.ConfigurationFeaturesInvoiceHistoryOptions
        {
            Enabled = true,
        },
    },
};
var service = new Stripe.BillingPortal.ConfigurationService();
Stripe.BillingPortal.Configuration configuration = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BillingPortalConfigurationParams{
  Features: &stripe.BillingPortalConfigurationFeaturesParams{
    CustomerUpdate: &stripe.BillingPortalConfigurationFeaturesCustomerUpdateParams{
      AllowedUpdates: []*string{
        stripe.String(string(stripe.BillingPortalConfigurationFeaturesCustomerUpdateAllowedUpdateEmail)),
        stripe.String(string(stripe.BillingPortalConfigurationFeaturesCustomerUpdateAllowedUpdateTaxID)),
      },
      Enabled: stripe.Bool(true),
    },
    InvoiceHistory: &stripe.BillingPortalConfigurationFeaturesInvoiceHistoryParams{
      Enabled: stripe.Bool(true),
    },
  },
};
result, err := configuration.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

ConfigurationCreateParams params =
  ConfigurationCreateParams.builder()
    .setFeatures(
      ConfigurationCreateParams.Features.builder()
        .setCustomerUpdate(
          ConfigurationCreateParams.Features.CustomerUpdate.builder()
            .addAllowedUpdate(ConfigurationCreateParams.Features.CustomerUpdate.AllowedUpdate.EMAIL)
            .addAllowedUpdate(
              ConfigurationCreateParams.Features.CustomerUpdate.AllowedUpdate.TAX_ID
            )
            .setEnabled(true)
            .build()
        )
        .setInvoiceHistory(
          ConfigurationCreateParams.Features.InvoiceHistory.builder().setEnabled(true).build()
        )
        .build()
    )
    .build();

Configuration configuration = Configuration.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const configuration = await stripe.billingPortal.configurations.create({
  features: {
    customer_update: {
      allowed_updates: ['email', 'tax_id'],
      enabled: true,
    },
    invoice_history: {
      enabled: true,
    },
  },
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

configuration = stripe.billing_portal.Configuration.create(
  features={
    "customer_update": {"allowed_updates": ["email", "tax_id"], "enabled": True},
    "invoice_history": {"enabled": True},
  },
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$configuration = $stripe->billingPortal->configurations->create([
  'features' => [
    'customer_update' => [
      'allowed_updates' => ['email', 'tax_id'],
      'enabled' => true,
    ],
    'invoice_history' => ['enabled' => true],
  ],
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

configuration = Stripe::BillingPortal::Configuration.create({
  features: {
    customer_update: {
      allowed_updates: ['email', 'tax_id'],
      enabled: true,
    },
    invoice_history: {enabled: true},
  },
})
```

### Response

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