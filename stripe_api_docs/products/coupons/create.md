# Create a coupon

You can create coupons easily via the [coupon management](https://dashboard.stripe.com/coupons) page of the Stripe dashboard. Coupon creation is also accessible via the API if you need to create coupons on the fly.

A coupon has either a `percent_off` or an `amount_off` and `currency`. If you set an `amount_off`, that amount will be subtracted from any invoice’s subtotal. For example, an invoice with a subtotal of  will have a final total of  if a coupon with an `amount_off` of  is applied to it and an invoice with a subtotal of  will have a final total of  if a coupon with an `amount_off` of  is applied to it.

Returns the coupon object.

- `amount_off` (integer, optional)
  A positive integer representing the amount to subtract from an invoice total (required if `percent_off` is not passed).

- `applies_to` (object, optional)
  A hash containing directions for what this Coupon will apply discounts to.

  - `applies_to.products` (array of strings, optional)
    An array of Product IDs that this Coupon will apply to.

- `currency` (enum, optional)
  Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the `amount_off` parameter (required if `amount_off` is passed).

- `currency_options` (object, optional)
  Coupons defined in each available currency option (only supported if `amount_off` is passed). Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

  - `currency_options.<currency>.amount_off` (integer, required)
    A positive integer representing the amount to subtract from an invoice total.

- `duration` (enum, optional)
  Specifies how long the discount will be in effect if used on a subscription. Defaults to `once`.

  Applies to all charges from a subscription with this coupon applied.

  Applies to the first charge from a subscription with this coupon applied.

  Applies to charges in the first `duration_in_months` months from a subscription with this coupon applied. This value is deprecated and will be replaced in future versions of the API.

- `duration_in_months` (integer, optional)
  Required only if `duration` is `repeating`, in which case it must be a positive integer that specifies the number of months the discount will be in effect.

- `id` (string, optional)
  Unique string of your choice that will be used to identify this coupon when applying it to a customer. If you don’t want to specify a particular code, you can leave the ID blank and we’ll generate a random code for you.

- `max_redemptions` (integer, optional)
  A positive integer specifying the number of times the coupon can be redeemed before it’s no longer valid. For example, you might have a 50% off coupon that the first 20 readers of your blog can use.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `name` (string, optional)
  Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the `id` is shown if `name` is not set.

- `percent_off` (float, optional)
  A positive float larger than 0, and smaller or equal to 100, that represents the discount the coupon will apply (required if `amount_off` is not passed).

- `redeem_by` (timestamp, optional)
  Unix timestamp specifying the last time at which the coupon can be redeemed. After the redeem_by date, the coupon can no longer be applied to new customers.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CouponCreateOptions { Duration = "forever", PercentOff = 25.5M };
var service = new CouponService();
Coupon coupon = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CouponParams{
  Duration: stripe.String(string(stripe.CouponDurationForever)),
  PercentOff: stripe.Float64(25.5),
};
result, err := coupon.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

CouponCreateParams params =
  CouponCreateParams.builder()
    .setDuration(CouponCreateParams.Duration.FOREVER)
    .setPercentOff(new BigDecimal(25.5))
    .build();

Coupon coupon = Coupon.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const coupon = await stripe.coupons.create({
  duration: 'forever',
  percent_off: 25.5,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

coupon = stripe.Coupon.create(
  duration="forever",
  percent_off=25.5,
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$coupon = $stripe->coupons->create([
  'duration' => 'forever',
  'percent_off' => 25.5,
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

coupon = Stripe::Coupon.create({
  duration: 'forever',
  percent_off: 25.5,
})
```

### Response

```json
{
  "id": "jMT0WJUD",
  "object": "coupon",
  "amount_off": null,
  "created": 1678037688,
  "currency": null,
  "duration": "forever",
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