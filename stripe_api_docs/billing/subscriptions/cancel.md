# Cancel # Cancel a subscription

Cancels a customer’s subscription immediately. The customer won’t be charged again for the subscription. After it’s canceled, you can no longer update the subscription or its [metadata](https://docs.stripe.com/metadata.md).

Any pending invoice items that you’ve created are still charged at the end of the period, unless manually [deleted](#delete_invoiceitem). If you’ve set the subscription to cancel at the end of the period, any pending prorations are also left in place and collected at the end of the period. But if the subscription is set to cancel immediately, pending prorations are removed if `invoice_now` and `prorate` are both set to true.

By default, upon subscription cancellation, Stripe stops automatic collection of all finalized invoices for the customer. This is intended to prevent unexpected payment attempts after the customer has canceled a subscription. However, you can resume automatic collection of the invoices manually after subscription cancellation to have us proceed. Or, you could check for unpaid invoices before allowing the customer to cancel the subscription at all.

The canceled `Subscription` object. Its subscription status will be set to `canceled`.

- `cancellation_details` (object, optional)
  Details about why this subscription was cancelled

  - `cancellation_details.comment` (string, optional)
    Additional comments about why the user canceled the subscription, if the subscription was canceled explicitly by the user.

  - `cancellation_details.feedback` (enum, optional)
    The customer submitted reason for why they canceled, if the subscription was canceled explicitly by the user.

    Customer service was less than expected

    Quality was less than expected

    Some features are missing

    Other reason

    I’m switching to a different service

    Ease of use was less than expected

    It’s too expensive

    I don’t use the service enough

- `invoice_now` (boolean, optional)
  Will generate a final invoice that invoices for any un-invoiced metered usage and new/pending proration invoice items. Defaults to `false`.

- `prorate` (boolean, optional)
  Will generate a proration invoice item that credits remaining unused time until the subscription period end. Defaults to `false`.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new SubscriptionService();
Subscription subscription = service.Cancel("sub_1MlPf9LkdIwHu7ixB6VIYRyX");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.SubscriptionCancelParams{};
result, err := subscription.Cancel("sub_1MlPf9LkdIwHu7ixB6VIYRyX", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Subscription resource = Subscription.retrieve("sub_1MlPf9LkdIwHu7ixB6VIYRyX");

SubscriptionCancelParams params = SubscriptionCancelParams.builder().build();

Subscription subscription = resource.cancel(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const subscription = await stripe.subscriptions.cancel('sub_1MlPf9LkdIwHu7ixB6VIYRyX');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

subscription = stripe.Subscription.cancel("sub_1MlPf9LkdIwHu7ixB6VIYRyX")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$subscription = $stripe->subscriptions->cancel('sub_1MlPf9LkdIwHu7ixB6VIYRyX', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

subscription = Stripe::Subscription.cancel('sub_1MlPf9LkdIwHu7ixB6VIYRyX')
```

### Response

```json
{
  "id": "sub_1MlPf9LkdIwHu7ixB6VIYRyX",
  "object": "subscription",
  "application": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null
  },
  "billing_cycle_anchor": 1678768838,
  "cancel_at": null,
  "cancel_at_period_end": false,
  "canceled_at": 1678768842,
  "cancellation_details": {
    "comment": null,
    "feedback": null,
    "reason": "cancellation_requested"
  },
  "collection_method": "charge_automatically",
  "created": 1678768838,
  "currency": "usd",
  "customer": "cus_NWSaVkvdacCUi4",
  "days_until_due": null,
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discounts": null,
  "ended_at": 1678768842,
  "invoice_settings": {
    "issuer": {
      "type": "self"
    }
  },
  "items": {
    "object": "list",
    "data": [
      {
        "id": "si_NWSaWTp80M123q",
        "object": "subscription_item",
        "created": 1678768839,
        "current_period_end": 1681447238,
        "current_period_start": 1678768838,
        "metadata": {},
        "plan": {
          "id": "price_1MlPf7LkdIwHu7ixgcbP7cwE",
          "object": "plan",
          "active": true,
          "amount": 1099,
          "amount_decimal": "1099",
          "billing_scheme": "per_unit",
          "created": 1678768837,
          "currency": "usd",
          "interval": "month",
          "interval_count": 1,
          "livemode": false,
          "metadata": {},
          "nickname": null,
          "product": "prod_NWSaMgipulx8IQ",
          "tiers_mode": null,
          "transform_usage": null,
          "trial_period_days": null,
          "usage_type": "licensed"
        },
        "price": {
          "id": "price_1MlPf7LkdIwHu7ixgcbP7cwE",
          "object": "price",
          "active": true,
          "billing_scheme": "per_unit",
          "created": 1678768837,
          "currency": "usd",
          "custom_unit_amount": null,
          "livemode": false,
          "lookup_key": null,
          "metadata": {},
          "nickname": null,
          "product": "prod_NWSaMgipulx8IQ",
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
        "subscription": "sub_1MlPf9LkdIwHu7ixB6VIYRyX",
        "tax_rates": []
      }
    ],
    "has_more": false,
    "total_count": 1,
    "url": "/v1/subscription_items?subscription=sub_1MlPf9LkdIwHu7ixB6VIYRyX"
  },
  "latest_invoice": "in_1MlPf9LkdIwHu7ixEo6hdgCw",
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
    "id": "price_1MlPf7LkdIwHu7ixgcbP7cwE",
    "object": "plan",
    "active": true,
    "amount": 1099,
    "amount_decimal": "1099",
    "billing_scheme": "per_unit",
    "created": 1678768837,
    "currency": "usd",
    "interval": "month",
    "interval_count": 1,
    "livemode": false,
    "metadata": {},
    "nickname": null,
    "product": "prod_NWSaMgipulx8IQ",
    "tiers_mode": null,
    "transform_usage": null,
    "trial_period_days": null,
    "usage_type": "licensed"
  },
  "quantity": 1,
  "schedule": null,
  "start_date": 1678768838,
  "status": "canceled",
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
