# Delete a plan

Deleting plans means new subscribers can’t be added. Existing subscribers aren’t affected.

An object with the deleted plan’s ID and a deleted flag upon success. Otherwise, this call raises [an error](#errors), such as if the plan has already been deleted.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new PlanService();
Plan deleted = service.Delete("plan_NjpIbv3g3ZibnD");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PlanParams{};
result, err := plan.Del("plan_NjpIbv3g3ZibnD", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Plan resource = Plan.retrieve("plan_NjpIbv3g3ZibnD");

Plan plan = resource.delete();
```

```node
const stripe = require('stripe')('<<secret key>>');

const deleted = await stripe.plans.del('plan_NjpIbv3g3ZibnD');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

deleted = stripe.Plan.delete("plan_NjpIbv3g3ZibnD")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$deleted = $stripe->plans->delete('plan_NjpIbv3g3ZibnD', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

deleted = Stripe::Plan.delete('plan_NjpIbv3g3ZibnD')
```

### Response

```json
{
  "id": "plan_NjpIbv3g3ZibnD",
  "object": "plan",
  "deleted": true
}
```