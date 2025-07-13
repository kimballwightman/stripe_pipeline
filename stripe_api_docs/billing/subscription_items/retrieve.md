# Retrieve a subscription item

Retrieves the subscription item with the given ID.

Returns a subscription item if a valid subscription item ID was provided. Raises [an error](#errors) otherwise.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new SubscriptionItemService();
SubscriptionItem subscriptionItem = service.Get("si_NcLYdDxLHxlFo7");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.SubscriptionItemParams{};
result, err := subscriptionitem.Get("si_NcLYdDxLHxlFo7", params);
```

```java
Stripe.apiKey = "<<secret key>>";

SubscriptionItem subscriptionItem = SubscriptionItem.retrieve("si_NcLYdDxLHxlFo7");
```

```node
const stripe = require('stripe')('<<secret key>>');

const subscriptionItem = await stripe.subscriptionItems.retrieve('si_NcLYdDxLHxlFo7');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

subscription_item = stripe.SubscriptionItem.retrieve("si_NcLYdDxLHxlFo7")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$subscriptionItem = $stripe->subscriptionItems->retrieve('si_NcLYdDxLHxlFo7', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

subscription_item = Stripe::SubscriptionItem.retrieve('si_NcLYdDxLHxlFo7')
```

### Response

```json
{
  "id": "si_NcLYdDxLHxlFo7",
  "object": "subscription_item",
  "created": 1680126546,
  "metadata": {},
  "price": {
    "id": "price_1Mr6rdLkdIwHu7ixwPmiybbR",
    "object": "price",
    "active": true,
    "billing_scheme": "per_unit",
    "created": 1680126545,
    "currency": "usd",
    "custom_unit_amount": null,
    "discounts": null,
    "livemode": false,
    "lookup_key": null,
    "metadata": {},
    "nickname": null,
    "product": "prod_NcLYGKH0eY5b8s",
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
  "quantity": 2,
  "subscription": "sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd",
  "tax_rates": []
}
```