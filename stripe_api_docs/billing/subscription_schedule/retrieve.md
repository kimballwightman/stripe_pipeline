# Retrieve a schedule

Retrieves the details of an existing subscription schedule. You only need to supply the unique subscription schedule identifier that was returned upon subscription schedule creation.

Returns a subscription schedule object if a valid identifier was provided.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new SubscriptionScheduleService();
SubscriptionSchedule subscriptionSchedule = service.Get("sub_sched_1Mr3YdLkdIwHu7ixjop3qtff");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.SubscriptionScheduleParams{};
result, err := subscriptionschedule.Get("sub_sched_1Mr3YdLkdIwHu7ixjop3qtff", params);
```

```java
Stripe.apiKey = "<<secret key>>";

SubscriptionSchedule subscriptionSchedule =
  SubscriptionSchedule.retrieve("sub_sched_1Mr3YdLkdIwHu7ixjop3qtff");
```

```node
const stripe = require('stripe')('<<secret key>>');

const subscriptionSchedule = await stripe.subscriptionSchedules.retrieve(
  'sub_sched_1Mr3YdLkdIwHu7ixjop3qtff'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

subscription_schedule = stripe.SubscriptionSchedule.retrieve("sub_sched_1Mr3YdLkdIwHu7ixjop3qtff")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$subscriptionSchedule = $stripe->subscriptionSchedules->retrieve(
  'sub_sched_1Mr3YdLkdIwHu7ixjop3qtff',
  []
);
```

```ruby
Stripe.api_key = '<<secret key>>'

subscription_schedule = Stripe::SubscriptionSchedule.retrieve('sub_sched_1Mr3YdLkdIwHu7ixjop3qtff')
```

### Response

```json
{
  "id": "sub_sched_1Mr3YdLkdIwHu7ixjop3qtff",
  "object": "subscription_schedule",
  "application": null,
  "canceled_at": null,
  "completed_at": null,
  "created": 1724058651,
  "current_phase": null,
  "customer": "cus_NcI8FsMbh0OeFs",
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
      "end_date": 1818666418,
      "invoice_settings": null,
      "items": [
        {
          "discounts": null,
          "metadata": {},
          "plan": "price_1Mr3YcLkdIwHu7ixYCFhXHNb",
          "price": "price_1Mr3YcLkdIwHu7ixYCFhXHNb",
          "quantity": 1,
          "tax_rates": []
        }
      ],
      "metadata": {},
      "on_behalf_of": null,
      "proration_behavior": "create_prorations",
      "start_date": 1787130418,
      "transfer_data": null,
      "trial_end": null
    }
  ],
  "released_at": null,
  "released_subscription": null,
  "renewal_interval": null,
  "status": "not_started",
  "subscription": null,
  "test_clock": null
}
```