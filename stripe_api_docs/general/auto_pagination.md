# Auto-pagination

Our libraries support auto-pagination. This feature allows you to easily iterate through large lists of resources without having to manually perform the requests to fetch subsequent pages.

```sh
\# The auto-pagination feature is specific to Stripe's
# libraries and cannot be used directly with curl.
```

```ruby
require 'stripe'
Stripe.api_key = '<<secret key>>'

customers = Stripe::Customer.list({limit: 3})
customers.auto_paging_each do |customer|
  # Do something with customer
end
```

```sh
\# The auto-pagination feature is specific to Stripe's
# libraries and cannot be used directly with the CLI.
```

```python
import stripe
stripe.api_key = "<<secret key>>"

customers = stripe.Customer.list(limit=3)
for customer in customers.auto_paging_iter():
  # Do something with customer
```

```php
$stripe = new \Stripe\StripeClient("<<secret key>>");
$customers = $stripe->customers->all([
  'limit' => 3,
]);
foreach ($customers->autoPagingIterator() as $customer) {
  // Do something with $customer
}
```

```java
Stripe.apiKey = "<<secret key>>";

Map<String, Object> customerParams = new HashMap<>();
customerParams.put("limit", 3);

Iterable<Customers> itCustomers = Customer.list(customerParams).autoPagingIterable();

for (Customer customer : itCustomers) {
  // Do something with customer
}
```

```javascript
const Stripe = require('stripe');
const stripe = Stripe('<<secret key>>');
// In Node 10+:
for await (const customer of stripe.customers.list({limit: 3})) {
  // Do something with customer
}

// In other environments:
stripe.customers.list({limit: 3})
  .autoPagingEach(function(customer) {
    // Do something with customer
  });
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CustomerListParams{}
params.Filters.AddFilter("limit", "", "3")
i := customer.List(params)
for i.Next() {
  customer := i.Customer()
  // Do something with customer
}
```

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new CustomerService();
var options = new CustomerListOptions {
  Limit = 3
};

// Synchronously paginate
foreach (var customer in service.ListAutoPaging(options)) {
  // Do something with customer
}

// Asynchronously paginate
await foreach (var customer in service.ListAutoPagingAsync(options)) {
  // Do something with customer
}
```