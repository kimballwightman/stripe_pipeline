# Cancel a schedule

Cancels a subscription schedule and its associated subscription immediately (if the subscription schedule has an active subscription). A subscription schedule can only be canceled if its status is `not_started` or `active`.

The canceled `subscription_schedule` object. Its status will be `canceled` and `canceled_at` will be the current time.

- `invoice_now` (boolean, optional)
  If the subscription schedule is `active`, indicates if a final invoice will be generated that contains any un-invoiced metered usage and new/pending proration invoice items. Defaults to `true`.

- `prorate` (boolean, optional)
  If the subscription schedule is `active`, indicates if the cancellation should be prorated. Defaults to `true`.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new SubscriptionScheduleService();
SubscriptionSchedule subscriptionSchedule = service.Cancel("sub_sched_1Mr3owLkdIwHu7ix38CXMudt");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.SubscriptionScheduleCancelParams{};
result, err := subscriptionschedule.Cancel("sub_sched_1Mr3owLkdIwHu7ix38CXMudt", params);
```

```java
Stripe.apiKey = "<<secret key>>";

SubscriptionSchedule resource = SubscriptionSchedule.retrieve("sub_sched_1Mr3owLkdIwHu7ix38CXMudt");

SubscriptionScheduleCancelParams params = SubscriptionScheduleCancelParams.builder().build();

SubscriptionSchedule subscriptionSchedule = resource.cancel(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const subscriptionSchedule = await stripe.subscriptionSchedules.cancel(
  'sub_sched_1Mr3owLkdIwHu7ix38CXMudt'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

subscription_schedule = stripe.SubscriptionSchedule.cancel("sub_sched_1Mr3owLkdIwHu7ix38CXMudt")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$subscriptionSchedule = $stripe->subscriptionSchedules->cancel(
  'sub_sched_1Mr3owLkdIwHu7ix38CXMudt',
  []
);
```

```ruby
Stripe.api_key = '<<secret key>>'

subscription_schedule = Stripe::SubscriptionSchedule.cancel('sub_sched_1Mr3owLkdIwHu7ix38CXMudt')
```

### Response

```json
{
  "id": "sub_sched_1Mr3owLkdIwHu7ix38CXMudt",
  "object": "subscription_schedule",
  "application": null,
  "canceled_at": 1680114847,
  "completed_at": null,
  "created": 1680114846,
  "current_phase": null,
  "customer": "cus_NcIPFRC981NmaY",
  "default_settings": {
    "application_fee_percent": null,
    "automatic_tax": {
      "enabled": false,
      "liability": null
    },
    "billing_cycle_anchor": "automatic",
    "collection_method": "charge_automatically",
    "default_payment_method": null,
    "default_source": null,
    "description": null,
    "invoice_settings": {
      "issuer": {
        "type": "self"
      }
    },
    "on_behalf_of": null,
    "transfer_data": null
  },
  "end_behavior": "release",
  "livemode": false,
  "metadata": {},
  "phases": [
    {
      "add_invoice_items": [],
      "application_fee_percent": null,
      "billing_cycle_anchor": null,
      "collection_method": null,
      "currency": "usd",
      "default_payment_method": null,
      "default_tax_rates": [],
      "description": null,
      "discounts": null,
      "end_date": 1712339228,
      "invoice_settings": null,
      "items": [
        {
          "metadata": {},
          "plan": "price_1Mr3owLkdIwHu7ix0RyYpQzk",
          "price": "price_1Mr3owLkdIwHu7ix0RyYpQzk",
          "quantity": 1,
          "tax_rates": []
        }
      ],
      "metadata": {},
      "on_behalf_of": null,
      "proration_behavior": "create_prorations",
      "start_date": 1680716828,
      "transfer_data": null,
      "trial_end": null
    }
  ],
  "released_at": null,
  "released_subscription": null,
  "renewal_interval": null,
  "status": "canceled",
  "subscription": null,
  "test_clock": null
}
```