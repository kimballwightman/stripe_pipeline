# List all customers

Returns a list of your customers. The customers are returned sorted by creation date, with the most recent customers appearing first.

A dictionary with a `data` property that contains an array of up to `limit` customers, starting after customer `starting_after`. Passing an optional `email` will result in filtering to customers with only that exact email address. Each entry in the array is a separate customer object. If no more customers are available, the resulting array will be empty.

- `created` (object, optional)
  Only return customers that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `email` (string, optional)
  A case-sensitive filter on the list based on the customer’s `email` field. The value must be a string.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `test_clock` (string, optional)
  Provides a list of customers that are associated with the specified test clock. The response will not include customers with test clocks if this parameter is not set.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CustomerListOptions { Limit = 3 };
var service = new CustomerService();
StripeList<Customer> customers = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CustomerListParams{};
params.Limit = stripe.Int64(3)
result := customer.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

CustomerListParams params = CustomerListParams.builder().setLimit(3L).build();

CustomerCollection customers = Customer.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const customers = await stripe.customers.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

customers = stripe.Customer.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$customers = $stripe->customers->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

customers = Stripe::Customer.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/customers",
  "has_more": false,
  "data": [
    {
      "id": "cus_NffrFeUfNV2Hib",
      "object": "customer",
      "address": null,
      "balance": 0,
      "created": 1680893993,
      "currency": null,
      "default_source": null,
      "delinquent": false,
      "description": null,
      "email": "jennyrosen@example.com",
      "invoice_prefix": "0759376C",
      "invoice_settings": {
        "custom_fields": null,
        "default_payment_method": null,
        "footer": null,
        "rendering_options": null
      },
      "livemode": false,
      "metadata": {},
      "name": "Jenny Rosen",
      "next_invoice_sequence": 1,
      "phone": null,
      "preferred_locales": [],
      "shipping": null,
      "tax_exempt": "none",
      "test_clock": null
    }
  ]
}
```