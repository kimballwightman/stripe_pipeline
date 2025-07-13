# List all subscription items

Returns a list of your subscription items for a given subscription.

A dictionary with a `data` property that contains an array of up to `limit` subscription items, starting after subscription item `starting_after`. Each entry in the array is a separate subscription item object. If no more subscription items are available, the resulting array will be empty.

- `subscription` (string, required)
  The ID of the subscription whose items will be retrieved.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new SubscriptionItemListOptions
{
    Limit = 3,
    Subscription = "sub_1NQH9iLkdIwHu7ixxhHui9yi",
};
var service = new SubscriptionItemService();
StripeList<SubscriptionItem> subscriptionItems = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.SubscriptionItemListParams{
  Subscription: stripe.String("sub_1NQH9iLkdIwHu7ixxhHui9yi"),
};
params.Limit = stripe.Int64(3)
result := subscriptionitem.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

SubscriptionItemListParams params =
  SubscriptionItemListParams.builder()
    .setLimit(3L)
    .setSubscription("sub_1NQH9iLkdIwHu7ixxhHui9yi")
    .build();

SubscriptionItemCollection subscriptionItems = SubscriptionItem.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const subscriptionItems = await stripe.subscriptionItems.list({
  limit: 3,
  subscription: 'sub_1NQH9iLkdIwHu7ixxhHui9yi',
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

subscription_items = stripe.SubscriptionItem.list(
  limit=3,
  subscription="sub_1NQH9iLkdIwHu7ixxhHui9yi",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$subscriptionItems = $stripe->subscriptionItems->all([
  'limit' => 3,
  'subscription' => 'sub_1NQH9iLkdIwHu7ixxhHui9yi',
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

subscription_items = Stripe::SubscriptionItem.list({
  limit: 3,
  subscription: 'sub_1NQH9iLkdIwHu7ixxhHui9yi',
})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/subscription_items",
  "has_more": false,
  "data": [
    {
      "id": "si_OCgWsGlqpbN4EP",
      "object": "subscription_item",
      "created": 1688507587,
      "metadata": {},
      "price": {
        "id": "price_1NQH9iLkdIwHu7ix3tkaSxhj",
        "object": "price",
        "active": true,
        "billing_scheme": "per_unit",
        "created": 1688507586,
        "currency": "usd",
        "custom_unit_amount": null,
        "livemode": false,
        "lookup_key": null,
        "metadata": {},
        "nickname": null,
        "product": "prod_OCgWE6cbwiSu27",
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
        "unit_amount": 1000,
        "unit_amount_decimal": "1000"
      },
      "quantity": 1,
      "subscription": "sub_1NQH9iLkdIwHu7ixxhHui9yi",
      "tax_rates": []
    }
  ]
}
```