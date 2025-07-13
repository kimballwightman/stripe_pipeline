# Create a promotion code

A promotion code points to a coupon. You can optionally restrict the code to a specific customer, redemption limit, and expiration date.

Returns the promotion code object.

- `coupon` (string, required)
  The coupon for this promotion code.

- `active` (boolean, optional)
  Whether the promotion code is currently active.

- `code` (string, optional)
  The customer-facing code. Regardless of case, this code must be unique across all active promotion codes for a specific customer. Valid characters are lower case letters (a-z), upper case letters (A-Z), and digits (0-9).

  If left blank, we will generate one automatically.

- `customer` (string, optional)
  The customer that this promotion code can be used by. If not set, the promotion code can be used by all customers.

- `expires_at` (timestamp, optional)
  The timestamp at which this promotion code will expire. If the coupon has specified a `redeems_by`, then this value cannot be after the coupon’s `redeems_by`.

- `max_redemptions` (integer, optional)
  A positive integer specifying the number of times the promotion code can be redeemed. If the coupon has specified a `max_redemptions`, then this value cannot be greater than the coupon’s `max_redemptions`.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `restrictions` (object, optional)
  Settings that restrict the redemption of the promotion code.

  - `restrictions.currency_options` (object, optional)
    Promotion codes defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

    - `restrictions.currency_options.<currency>.minimum_amount` (integer, optional)
      Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a purchase must be $100 or more to work).

  - `restrictions.first_time_transaction` (boolean, optional)
    A Boolean indicating if the Promotion Code should only be redeemed for Customers without any successful payments or invoices

  - `restrictions.minimum_amount` (integer, optional)
    Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a purchase must be $100 or more to work).

  - `restrictions.minimum_amount_currency` (enum, optional)
    Three-letter [ISO code](https://stripe.com/docs/currencies) for minimum_amount

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new PromotionCodeCreateOptions { Coupon = "nVJYDOag" };
var service = new PromotionCodeService();
PromotionCode promotionCode = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PromotionCodeParams{Coupon: stripe.String("nVJYDOag")};
result, err := promotioncode.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

PromotionCodeCreateParams params =
  PromotionCodeCreateParams.builder().setCoupon("nVJYDOag").build();

PromotionCode promotionCode = PromotionCode.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const promotionCode = await stripe.promotionCodes.create({
  coupon: 'nVJYDOag',
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

promotion_code = stripe.PromotionCode.create(coupon="nVJYDOag")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$promotionCode = $stripe->promotionCodes->create(['coupon' => 'nVJYDOag']);
```

```ruby
Stripe.api_key = '<<secret key>>'

promotion_code = Stripe::PromotionCode.create({coupon: 'nVJYDOag'})
```

### Response

```json
{
  "id": "promo_1MiM6KLkdIwHu7ixrIaX4wgn",
  "object": "promotion_code",
  "active": true,
  "code": "A1H1Q1MG",
  "coupon": {
    "id": "nVJYDOag",
    "object": "coupon",
    "amount_off": null,
    "created": 1678040164,
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
  },
  "created": 1678040164,
  "customer": null,
  "expires_at": null,
  "livemode": false,
  "max_redemptions": null,
  "metadata": {},
  "restrictions": {
    "first_time_transaction": false,
    "minimum_amount": null,
    "minimum_amount_currency": null
  },
  "times_redeemed": 0
}
```