# Delete a subscription item

Deletes an item from the subscription. Removing a subscription item from a subscription will not cancel the subscription.

An subscription item object with a deleted flag upon success. Otherwise, this call raises [an error](#errors), such as if the subscription item has already been deleted.

- `clear_usage` (boolean, optional)
  Delete all usage for the given subscription item. Allowed only when the current plan’s `usage_type` is `metered`.

- `proration_behavior` (enum, optional)
  Determines how to handle [prorations](https://docs.stripe.com/docs/billing/subscriptions/prorations.md) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item’s `quantity` changes. The default value is `create_prorations`.

  Always invoice immediately for prorations.

  Will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under [certain conditions](https://docs.stripe.com/docs/subscriptions/upgrading-downgrading.md#immediate-payment).

  Disable creating prorations in this request.

- `proration_date` (timestamp, optional)
  If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](#retrieve_customer_invoice) endpoint.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new SubscriptionItemService();
SubscriptionItem deleted = service.Delete("si_NcLYdDxLHxlFo7");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.SubscriptionItemParams{};
result, err := subscriptionitem.Del("si_NcLYdDxLHxlFo7", params);
```

```java
Stripe.apiKey = "<<secret key>>";

SubscriptionItem resource = SubscriptionItem.retrieve("si_NcLYdDxLHxlFo7");

SubscriptionItemDeleteParams params = SubscriptionItemDeleteParams.builder().build();

SubscriptionItem subscriptionItem = resource.delete(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const deleted = await stripe.subscriptionItems.del('si_NcLYdDxLHxlFo7');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

deleted = stripe.SubscriptionItem.delete("si_NcLYdDxLHxlFo7")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$deleted = $stripe->subscriptionItems->delete('si_NcLYdDxLHxlFo7', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

deleted = Stripe::SubscriptionItem.delete('si_NcLYdDxLHxlFo7')
```

### Response

```json
{
  "id": "si_NcLYdDxLHxlFo7",
  "object": "subscription_item",
  "deleted": true
}
```