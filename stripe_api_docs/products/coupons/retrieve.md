# Retrieve a coupon

Retrieves the coupon with the given ID.

Returns a coupon if a valid coupon ID was provided. Raises [an error](#errors) otherwise.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new CouponService();
Coupon coupon = service.Get("jMT0WJUD");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CouponParams{};
result, err := coupon.Get("jMT0WJUD", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Coupon coupon = Coupon.retrieve("jMT0WJUD");
```

```node
const stripe = require('stripe')('<<secret key>>');

const coupon = await stripe.coupons.retrieve('jMT0WJUD');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

coupon = stripe.Coupon.retrieve("jMT0WJUD")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$coupon = $stripe->coupons->retrieve('jMT0WJUD', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

coupon = Stripe::Coupon.retrieve('jMT0WJUD')
```

### Response

```json
{
  "id": "jMT0WJUD",
  "object": "coupon",
  "amount_off": null,
  "created": 1678037688,
  "currency": null,
  "duration": "repeating",
  "duration_in_months": 3,
  "livemode": false,
  "max_redemptions": null,
  "metadata": {},
  "name": null,
  "percent_off": 25.5,
  "redeem_by": null,
  "times_redeemed": 0,
  "valid": true
}
```