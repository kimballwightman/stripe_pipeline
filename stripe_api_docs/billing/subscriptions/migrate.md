# Migrate a subscription

Upgrade the billing_mode of an existing subscription.

The newly migrated `Subscription` object, if the call succeeded.

- `billing_mode` (object, required)
  Controls how prorations and invoices for subscriptions are calculated and orchestrated.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new SubscriptionMigrateOptions
{
    BillingMode = new SubscriptionBillingModeOptions { Type = "flexible" },
};
var service = new SubscriptionService();
Subscription subscription = service.Migrate("sub_1MowQVLkdIwHu7ixeRlqHVzs", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.SubscriptionMigrateParams{
  BillingMode: &stripe.SubscriptionMigrateBillingModeParams{Type: stripe.String("flexible")},
};
result, err := subscription.Migrate("sub_1MowQVLkdIwHu7ixeRlqHVzs", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Subscription resource = Subscription.retrieve("sub_1MowQVLkdIwHu7ixeRlqHVzs");

SubscriptionMigrateParams params =
  SubscriptionMigrateParams.builder()
    .setBillingMode(
      SubscriptionMigrateParams.BillingMode.builder()
        .setType(SubscriptionMigrateParams.BillingMode.Type.FLEXIBLE)
        .build()
    )
    .build();

Subscription subscription = resource.migrate(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const subscription = await stripe.subscriptions.migrate(
  'sub_1MowQVLkdIwHu7ixeRlqHVzs',
  {
    billing_mode: {
      type: 'flexible',
    },
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

subscription = stripe.Subscription.migrate(
  "sub_1MowQVLkdIwHu7ixeRlqHVzs",
  billing_mode={"type": "flexible"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$subscription = $stripe->subscriptions->migrate(
  'sub_1MowQVLkdIwHu7ixeRlqHVzs',
  ['billing_mode' => ['type' => 'flexible']]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

subscription = Stripe::Subscription.migrate(
  'sub_1MowQVLkdIwHu7ixeRlqHVzs',
  {billing_mode: {type: 'flexible'}},
)
```

### Response

```json
{
  "id": "sub_1MowQVLkdIwHu7ixeRlqHVzs",
  "object": "subscription",
  "application": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null
  },
  "billing_cycle_anchor": 1679609767,
  "billing_mode": "flexible",
  "billing_mode_details": {
    "updated_at": 1679609768
  },
  "billing_thresholds": null,
  "cancel_at": null,
  "cancel_at_period_end": false,
  "canceled_at": null,
  "cancellation_details": {
    "comment": null,
    "feedback": null,
    "reason": null
  },
  "collection_method": "charge_automatically",
  "created": 1679609767,
  "currency": "usd",
  "customer": "cus_Na6dX7aXxi11N4",
  "days_until_due": null,
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discounts": null,
  "ended_at": null,
  "invoice_settings": {
    "issuer": {
      "type": "self"
    }
  },
  "items": {
    "object": "list",
    "data": [
      {
        "id": "si_Na6dzxczY5fwHx",
        "object": "subscription_item",
        "billing_thresholds": null,
        "created": 1679609768,
        "current_period_end": 1682288167,
        "current_period_start": 1679609767,
        "metadata": {},
        "plan": {
          "id": "price_1MowQULkdIwHu7ixraBm864M",
          "object": "plan",
          "active": true,
          "aggregate_usage": null,
          "amount": 1000,
          "amount_decimal": "1000",
          "billing_scheme": "per_unit",
          "created": 1679609766,
          "currency": "usd",
          "discounts": null,
          "interval": "month",
          "interval_count": 1,
          "livemode": false,
          "metadata": {},
          "nickname": null,
          "product": "prod_Na6dGcTsmU0I4R",
          "tiers_mode": null,
          "transform_usage": null,
          "trial_period_days": null,
          "usage_type": "licensed"
        },
        "price": {
          "id": "price_1MowQULkdIwHu7ixraBm864M",
          "object": "price",
          "active": true,
          "billing_scheme": "per_unit",
          "created": 1679609766,
          "currency": "usd",
          "custom_unit_amount": null,
          "livemode": false,
          "lookup_key": null,
          "metadata": {},
          "nickname": null,
          "product": "prod_Na6dGcTsmU0I4R",
          "recurring": {
            "aggregate_usage": null,
            "interval": "month",
            "interval_count": 1,
            "trial_period_days": null,
            "usage_type": "licensed"
          },
          "tax_behavior": "unspecified",
          "tiers_mode": null,
          "transform_quantity": null,
          "type": "recurring",
          "unit_amount": 1000,
          "unit_amount_decimal": "1000"
        },
        "quantity": 1,
        "subscription": "sub_1MowQVLkdIwHu7ixeRlqHVzs",
        "tax_rates": []
      }
    ],
    "has_more": false,
    "total_count": 1,
    "url": "/v1/subscription_items?subscription=sub_1MowQVLkdIwHu7ixeRlqHVzs"
  },
  "latest_invoice": "in_1MowQWLkdIwHu7ixuzkSPfKd",
  "livemode": false,
  "metadata": {
    "order_id": "6735"
  },
  "next_pending_invoice_item_invoice": null,
  "on_behalf_of": null,
  "pause_collection": null,
  "payment_settings": {
    "payment_method_options": null,
    "payment_method_types": null,
    "save_default_payment_method": "off"
  },
  "pending_invoice_item_interval": null,
  "pending_setup_intent": null,
  "pending_update": null,
  "schedule": null,
  "start_date": 1679609767,
  "status": "active",
  "test_clock": null,
  "transfer_data": null,
  "trial_end": null,
  "trial_settings": {
    "end_behavior": {
      "missing_payment_method": "create_invoice"
    }
  },
  "trial_start": null
}
```