# Delete a subscription discount

Removes the currently applied discount on a subscription.

An object with a deleted flag set to true upon success. This call returns [an error](#errors) otherwise, such as if no discount exists on this subscription.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new SubscriptionService();
Discount discount = service.DeleteDiscount("sub_1NlcNX2eZvKYlo2CFqnrn9ow");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.SubscriptionDeleteDiscountParams{};
result, err := subscription.DeleteDiscount("sub_1NlcNX2eZvKYlo2CFqnrn9ow", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Subscription resource = Subscription.retrieve("sub_1NlcNX2eZvKYlo2CFqnrn9ow");

Discount discount = resource.deleteDiscount();
```

```node
const stripe = require('stripe')('<<secret key>>');

const deleted = await stripe.subscriptions.deleteDiscount('sub_1NlcNX2eZvKYlo2CFqnrn9ow');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

deleted = stripe.Subscription.delete_discount("sub_1NlcNX2eZvKYlo2CFqnrn9ow")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$deleted = $stripe->subscriptions->deleteDiscount('sub_1NlcNX2eZvKYlo2CFqnrn9ow', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

deleted = Stripe::Subscription.delete_discount('sub_1NlcNX2eZvKYlo2CFqnrn9ow')
```

### Response

```json
{
  "object": "discount",
  "deleted": true
}
```