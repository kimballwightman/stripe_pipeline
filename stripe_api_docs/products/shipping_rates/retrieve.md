# Retrieve a shipping rate

Returns the shipping rate object with the given ID.

Returns a shipping rate object if a valid identifier was provided.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new ShippingRateService();
ShippingRate shippingRate = service.Get("shr_1MrRx2LkdIwHu7ixikgEA6Wd");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.ShippingRateParams{};
result, err := shippingrate.Get("shr_1MrRx2LkdIwHu7ixikgEA6Wd", params);
```

```java
Stripe.apiKey = "<<secret key>>";

ShippingRate shippingRate = ShippingRate.retrieve("shr_1MrRx2LkdIwHu7ixikgEA6Wd");
```

```node
const stripe = require('stripe')('<<secret key>>');

const shippingRate = await stripe.shippingRates.retrieve('shr_1MrRx2LkdIwHu7ixikgEA6Wd');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

shipping_rate = stripe.ShippingRate.retrieve("shr_1MrRx2LkdIwHu7ixikgEA6Wd")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$shippingRate = $stripe->shippingRates->retrieve('shr_1MrRx2LkdIwHu7ixikgEA6Wd', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

shipping_rate = Stripe::ShippingRate.retrieve('shr_1MrRx2LkdIwHu7ixikgEA6Wd')
```

### Response

```json
{
  "id": "shr_1MrRx2LkdIwHu7ixikgEA6Wd",
  "object": "shipping_rate",
  "active": true,
  "created": 1680207604,
  "delivery_estimate": null,
  "display_name": "Ground shipping",
  "fixed_amount": {
    "amount": 500,
    "currency": "usd"
  },
  "livemode": false,
  "metadata": {},
  "tax_behavior": "unspecified",
  "tax_code": null,
  "type": "fixed_amount"
}
```