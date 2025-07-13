# Retrieve a customer

Retrieves a Customer object.

Returns the Customer object for a valid identifier. If it’s for a deleted Customer, a subset of the customer’s information is returned, including a `deleted` property that’s set to true.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new CustomerService();
Customer customer = service.Get("cus_NffrFeUfNV2Hib");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CustomerParams{};
result, err := customer.Get("cus_NffrFeUfNV2Hib", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Customer customer = Customer.retrieve("cus_NffrFeUfNV2Hib");
```

```node
const stripe = require('stripe')('<<secret key>>');

const customer = await stripe.customers.retrieve('cus_NffrFeUfNV2Hib');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

customer = stripe.Customer.retrieve("cus_NffrFeUfNV2Hib")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$customer = $stripe->customers->retrieve('cus_NffrFeUfNV2Hib', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

customer = Stripe::Customer.retrieve('cus_NffrFeUfNV2Hib')
```

### Response

```json
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
```