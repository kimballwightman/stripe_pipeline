# Delete a customer discount

Removes the currently applied discount on a customer.

An object with a deleted flag set to true upon success. This call returns [an error](#errors) otherwise, such as if no discount exists on this customer.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new CustomerService();
Discount discount = service.DeleteDiscount("cus_9s6XKzkNRiz8i3");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CustomerDeleteDiscountParams{};
result, err := customer.DeleteDiscount("cus_9s6XKzkNRiz8i3", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Customer resource = Customer.retrieve("cus_9s6XKzkNRiz8i3");

Discount discount = resource.deleteDiscount();
```

```node
const stripe = require('stripe')('<<secret key>>');

const deleted = await stripe.customers.deleteDiscount('cus_9s6XKzkNRiz8i3');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

deleted = stripe.Customer.delete_discount("cus_9s6XKzkNRiz8i3")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$deleted = $stripe->customers->deleteDiscount('cus_9s6XKzkNRiz8i3', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

deleted = Stripe::Customer.delete_discount('cus_9s6XKzkNRiz8i3')
```

### Response

```json
{
  "object": "discount",
  "deleted": true
}
```