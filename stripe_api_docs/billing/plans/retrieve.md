# Retrieve a plan

Retrieves the plan with the given ID.

Returns a plan if a valid plan ID was provided. Raises [an error](#errors) otherwise.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new PlanService();
Plan plan = service.Get("plan_NjpIbv3g3ZibnD");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PlanParams{};
result, err := plan.Get("plan_NjpIbv3g3ZibnD", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Plan plan = Plan.retrieve("plan_NjpIbv3g3ZibnD");
```

```node
const stripe = require('stripe')('<<secret key>>');

const plan = await stripe.plans.retrieve('plan_NjpIbv3g3ZibnD');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

plan = stripe.Plan.retrieve("plan_NjpIbv3g3ZibnD")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$plan = $stripe->plans->retrieve('plan_NjpIbv3g3ZibnD', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

plan = Stripe::Plan.retrieve('plan_NjpIbv3g3ZibnD')
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
  "metadata": {},
  "nickname": null,
  "product": "prod_NjpI7DbZx6AlWQ",
  "tiers_mode": null,
  "transform_usage": null,
  "trial_period_days": null,
  "usage_type": "licensed"
}
```