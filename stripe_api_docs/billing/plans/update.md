# Update a plan

Updates the specified plan by setting the values of the parameters passed. Any parameters not provided are left unchanged. By design, you cannot change a plan’s ID, amount, currency, or billing cycle.

The updated plan object is returned upon success. Otherwise, this call raises [an error](#errors).

- `active` (boolean, optional)
  Whether the plan is currently available for new subscriptions.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `nickname` (string, optional)
  A brief description of the plan, hidden from customers.

- `product` (string, optional)
  The product the plan belongs to. This cannot be changed once it has been used in a subscription or subscription schedule.

- `trial_period_days` (integer, optional)
  Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](https://docs.stripe.com/docs/api.md#create_subscription-trial_from_plan).

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new PlanUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var service = new PlanService();
Plan plan = service.Update("plan_NjpIbv3g3ZibnD", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PlanParams{};
params.AddMetadata("order_id", "6735")
result, err := plan.Update("plan_NjpIbv3g3ZibnD", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Plan resource = Plan.retrieve("plan_NjpIbv3g3ZibnD");

PlanUpdateParams params = PlanUpdateParams.builder().putMetadata("order_id", "6735").build();

Plan plan = resource.update(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const plan = await stripe.plans.update(
  'plan_NjpIbv3g3ZibnD',
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

plan = stripe.Plan.modify(
  "plan_NjpIbv3g3ZibnD",
  metadata={"order_id": "6735"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$plan = $stripe->plans->update('plan_NjpIbv3g3ZibnD', ['metadata' => ['order_id' => '6735']]);
```

```ruby
Stripe.api_key = '<<secret key>>'

plan = Stripe::Plan.update('plan_NjpIbv3g3ZibnD', {metadata: {order_id: '6735'}})
```

### Response

```json
{
  "id": "plan_NjpIbv3g3ZibnD",
  "object": "plan",
  "active": true,
  "amount": 1200,
  "amount_decimal": "1200",
  "billing_scheme": "per_unit",
  "created": 1681851647,
  "currency": "usd",
  "interval": "month",
  "interval_count": 1,
  "livemode": false,
  "metadata": {
    "order_id": "6735"
  },
  "nickname": null,
  "product": "prod_NjpI7DbZx6AlWQ",
  "tiers_mode": null,
  "transform_usage": null,
  "trial_period_days": null,
  "usage_type": "licensed"
}
```