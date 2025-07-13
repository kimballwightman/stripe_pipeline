# Request IDs

Each API request has an associated request identifier. You can find this value in the response headers, under `Request-Id`. You can also find request identifiers in the URLs of individual request logs in your [Dashboard](https://dashboard.stripe.com/logs).

To expedite the resolution process, provide the request identifier when you contact us about a specific request.

```sh
curl https://api.stripe.com/v1/customers \
  -u <<secret key>>: \
  -D "-" \
  -X POST
```

```ruby
require 'stripe'
Stripe.api_key = '<<secret key>>'

client = Stripe::StripeClient.new()
customer, response = client.request do
  Stripe::Customer.create()
end
puts response.request_id
```

```sh
stripe customers create --show-headers
```

```python
import stripe
stripe.api_key = "<<secret key>>"

customer = stripe.Customer.create()
print(customer.last_response.request_id)
```

```php
$stripe = new \Stripe\StripeClient("<<secret key>>");
$customer = $stripe->customers->create();
echo $customer->getLastResponse()->headers["Request-Id"];
```

```java
Stripe.apiKey = "<<secret key>>";

Customer customer = Customer.create(params);
System.out.println(customer.getLastResponse().requestId());
```

```javascript
const Stripe = require('stripe');
const stripe = Stripe('<<secret key>>');
var customer = await stripe.customers.create();
console.log(customer.lastResponse.requestId);
```

```go
stripe.Key = "<<secret key>>"

// currently stripe-go only returns the request ID for an error.
params := &stripe.CustomerParams{
}
params.SetSource("tok_chargeDeclined")
cus, err := customer.New(params)
if err != nil {
  if stripeErr, ok := err.(*stripe.Error); ok {
    fmt.Printf("Request ID : %v\n", stripeErr.RequestID)
  }
}
```

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

Customer customer = new CustomerService().Create(null);
Console.WriteLine(customer.RequestId);
```