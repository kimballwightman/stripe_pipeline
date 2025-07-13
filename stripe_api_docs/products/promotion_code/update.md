# Update a promotion code

Updates the specified promotion code by setting the values of the parameters passed. Most fields are, by design, not editable.

The updated promotion code object is returned upon success. Otherwise, this call raises [an error](#errors).

- `active` (boolean, optional)
  Whether the promotion code is currently active. A promotion code can only be reactivated when the coupon is still valid and the promotion code is otherwise redeemable.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `restrictions` (object, optional)
  Settings that restrict the redemption of the promotion code.

  - `restrictions.currency_options` (object, optional)
    Promotion codes defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

    - `restrictions.currency_options.<currency>.minimum_amount` (integer, optional)
      Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a purchase must be $100 or more to work).

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new PromotionCodeUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var service = new PromotionCodeService();
PromotionCode promotionCode = service.Update("promo_1MiM6KLkdIwHu7ixrIaX4wgn", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PromotionCodeParams{};
params.AddMetadata("order_id", "6735")
result, err := promotioncode.Update("promo_1MiM6KLkdIwHu7ixrIaX4wgn", params);
```

```java
Stripe.apiKey = "<<secret key>>";

PromotionCode resource = PromotionCode.retrieve("promo_1MiM6KLkdIwHu7ixrIaX4wgn");

PromotionCodeUpdateParams params =
  PromotionCodeUpdateParams.builder().putMetadata("order_id", "6735").build();

PromotionCode promotionCode = resource.update(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const promotionCode = await stripe.promotionCodes.update(
  'promo_1MiM6KLkdIwHu7ixrIaX4wgn',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

promotion_code = stripe.PromotionCode.modify(
  "promo_1MiM6KLkdIwHu7ixrIaX4wgn",
  metadata={"order_id": "6735"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$promotionCode = $stripe->promotionCodes->update(
  'promo_1MiM6KLkdIwHu7ixrIaX4wgn',
  ['metadata' => ['order_id' => '6735']]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

promotion_code = Stripe::PromotionCode.update(
  'promo_1MiM6KLkdIwHu7ixrIaX4wgn',
  {metadata: {order_id: '6735'}},
)
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
  "metadata": {
    "order_id": "6735"
  },
  "restrictions": {
    "first_time_transaction": false,
    "minimum_amount": null,
    "minimum_amount_currency": null
  },
  "times_redeemed": 0
}
```