# Resume a subscription

Initiates resumption of a paused subscription, optionally resetting the billing cycle anchor and creating prorations. If a resumption invoice is generated, it must be paid or marked uncollectible before the subscription will be unpaused. If payment succeeds the subscription will become `active`, and if payment fails the subscription will be `past_due`. The resumption invoice will void automatically if not paid by the expiration date.

The subscription object.

- `billing_cycle_anchor` (enum, optional)
  The billing cycle anchor that applies when the subscription is resumed. Either `now` or `unchanged`. The default is `now`. For more information, see the billing cycle [documentation](https://docs.stripe.com/docs/billing/subscriptions/billing-cycle.md).

  Reset the subscription’s billing cycle anchor to the current time (in UTC) and start a new billing period.

  Advance the subscription to the period that surrounds the current time without resetting the billing cycle anchor.

- `proration_behavior` (enum, optional)
  Determines how to handle [prorations](https://docs.stripe.com/docs/billing/subscriptions/prorations.md) resulting from the `billing_cycle_anchor` being `unchanged`. When the `billing_cycle_anchor` is set to `now` (default value), no prorations are generated. If no value is passed, the default is `create_prorations`.

  Always invoice immediately for prorations.

  Will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under [certain conditions](https://docs.stripe.com/docs/subscriptions/upgrading-downgrading.md#immediate-payment).

  Disable creating prorations in this request.

- `proration_date` (timestamp, optional)
  If set, prorations will be calculated as though the subscription was resumed at the given time. This can be used to apply exactly the same prorations that were previewed with the [create preview](https://stripe.com/docs/api/invoices/create_preview) endpoint.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new SubscriptionResumeOptions
{
    BillingCycleAnchor = SubscriptionBillingCycleAnchor.Now,
};
var service = new SubscriptionService();
Subscription subscription = service.Resume("sub_1MoGGtLkdIwHu7ixk5CfdiqC", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.SubscriptionResumeParams{BillingCycleAnchor: stripe.String("now")};
result, err := subscription.Resume("sub_1MoGGtLkdIwHu7ixk5CfdiqC", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Subscription resource = Subscription.retrieve("sub_1MoGGtLkdIwHu7ixk5CfdiqC");

SubscriptionResumeParams params =
  SubscriptionResumeParams.builder()
    .setBillingCycleAnchor(SubscriptionResumeParams.BillingCycleAnchor.NOW)
    .build();

Subscription subscription = resource.resume(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const subscription = await stripe.subscriptions.resume(
  'sub_1MoGGtLkdIwHu7ixk5CfdiqC',
  {
    billing_cycle_anchor: 'now',
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

subscription = stripe.Subscription.resume(
  "sub_1MoGGtLkdIwHu7ixk5CfdiqC",
  billing_cycle_anchor="now",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$subscription = $stripe->subscriptions->resume(
  'sub_1MoGGtLkdIwHu7ixk5CfdiqC',
  ['billing_cycle_anchor' => 'now']
);
```

```ruby
Stripe.api_key = '<<secret key>>'

subscription = Stripe::Subscription.resume(
  'sub_1MoGGtLkdIwHu7ixk5CfdiqC',
  {billing_cycle_anchor: 'now'},
)
```

### Response

```json
{
  "id": "sub_1MoGGtLkdIwHu7ixk5CfdiqC",
  "object": "subscription",
  "application": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null
  },
  "billing_cycle_anchor": 1679447726,
  "cancel_at": null,
  "cancel_at_period_end": false,
  "canceled_at": null,
  "cancellation_details": {
    "comment": null,
    "feedback": null,
    "reason": null
  },
  "collection_method": "charge_automatically",
  "created": 1679447723,
  "currency": "usd",
  "customer": "cus_NZP5i1diUz55jp",
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
        "id": "si_NZP5BhUIuWzXDG",
        "object": "subscription_item",
        "created": 1679447724,
        "current_period_end": 1682126126,
        "current_period_start": 1679447726,
        "metadata": {},
        "plan": {
          "id": "price_1MoGGsLkdIwHu7ixA9yHsq2N",
          "object": "plan",
          "active": true,
          "amount": 1099,
          "amount_decimal": "1099",
          "billing_scheme": "per_unit",
          "created": 1679447722,
          "currency": "usd",
          "interval": "month",
          "interval_count": 1,
          "livemode": false,
          "metadata": {},
          "nickname": null,
          "product": "prod_NZP5rEATBlScM9",
          "tiers_mode": null,
          "transform_usage": null,
          "trial_period_days": null,
          "usage_type": "licensed"
        },
        "price": {
          "id": "price_1MoGGsLkdIwHu7ixA9yHsq2N",
          "object": "price",
          "active": true,
          "billing_scheme": "per_unit",
          "created": 1679447722,
          "currency": "usd",
          "custom_unit_amount": null,
          "livemode": false,
          "lookup_key": null,
          "metadata": {},
          "nickname": null,
          "product": "prod_NZP5rEATBlScM9",
          "recurring": {
            "interval": "month",
            "interval_count": 1,
            "trial_period_days": null,
            "usage_type": "licensed"
          },
          "tax_behavior": "unspecified",
          "tiers_mode": null,
          "transform_quantity": null,
          "type": "recurring",
          "unit_amount": 1099,
          "unit_amount_decimal": "1099"
        },
        "quantity": 1,
        "subscription": "sub_1MoGGtLkdIwHu7ixk5CfdiqC",
        "tax_rates": []
      }
    ],
    "has_more": false,
    "total_count": 1,
    "url": "/v1/subscription_items?subscription=sub_1MoGGtLkdIwHu7ixk5CfdiqC"
  },
  "latest_invoice": "in_1MoGGwLkdIwHu7ixHSrelo8X",
  "livemode": false,
  "metadata": {},
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
  "plan": {
    "id": "price_1MoGGsLkdIwHu7ixA9yHsq2N",
    "object": "plan",
    "active": true,
    "amount": 1099,
    "amount_decimal": "1099",
    "billing_scheme": "per_unit",
    "created": 1679447722,
    "currency": "usd",
    "interval": "month",
    "interval_count": 1,
    "livemode": false,
    "metadata": {},
    "nickname": null,
    "product": "prod_NZP5rEATBlScM9",
    "tiers_mode": null,
    "transform_usage": null,
    "trial_period_days": null,
    "usage_type": "licensed"
  },
  "quantity": 1,
  "schedule": null,
  "start_date": 1679447723,
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