# List all coupons

Returns a list of your coupons.

A dictionary with a `data` property that contains an array of up to `limit` coupons, starting after coupon `starting_after`. Each entry in the array is a separate coupon object. If no more coupons are available, the resulting array will be empty.

- `created` (object, optional)
  A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CouponListOptions { Limit = 3 };
var service = new CouponService();
StripeList<Coupon> coupons = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CouponListParams{};
params.Limit = stripe.Int64(3)
result := coupon.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

CouponListParams params = CouponListParams.builder().setLimit(3L).build();

CouponCollection coupons = Coupon.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const coupons = await stripe.coupons.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

coupons = stripe.Coupon.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$coupons = $stripe->coupons->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

coupons = Stripe::Coupon.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/coupons",
  "has_more": false,
  "data": [
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
  ]
}
```