# Delete a customer

Permanently deletes a customer. It cannot be undone. Also immediately cancels any active subscriptions on the customer.

Returns an object with a deleted parameter on success. If the customer ID does not exist, this call raises [an error](#errors).

Unlike other objects, deleted customers can still be retrieved through the API in order to be able to track their history. Deleting customers removes all credit card details and prevents any further operations to be performed (such as adding a new subscription).


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new CustomerService();
Customer deleted = service.Delete("cus_NffrFeUfNV2Hib");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CustomerParams{};
result, err := customer.Del("cus_NffrFeUfNV2Hib", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Customer resource = Customer.retrieve("cus_NffrFeUfNV2Hib");

Customer customer = resource.delete();
```

```node
const stripe = require('stripe')('<<secret key>>');

const deleted = await stripe.customers.del('cus_NffrFeUfNV2Hib');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

deleted = stripe.Customer.delete("cus_NffrFeUfNV2Hib")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$deleted = $stripe->customers->delete('cus_NffrFeUfNV2Hib', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

deleted = Stripe::Customer.delete('cus_NffrFeUfNV2Hib')
```

### Response

```json
{
  "id": "cus_NffrFeUfNV2Hib",
  "object": "customer",
  "deleted": true
}
```