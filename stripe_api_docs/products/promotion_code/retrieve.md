# Retrieve a promotion code

Retrieves the promotion code with the given ID. In order to retrieve a promotion code by the customer-facing `code` use [list](https://docs.stripe.com/docs/api/promotion_codes/list.md) with the desired `code`.

Returns a promotion code if a valid promotion code ID was provided. Raises [an error](#errors) otherwise.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new PromotionCodeService();
PromotionCode promotionCode = service.Get("promo_1MiM6KLkdIwHu7ixrIaX4wgn");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PromotionCodeParams{};
result, err := promotioncode.Get("promo_1MiM6KLkdIwHu7ixrIaX4wgn", params);
```

```java
Stripe.apiKey = "<<secret key>>";

PromotionCode promotionCode = PromotionCode.retrieve("promo_1MiM6KLkdIwHu7ixrIaX4wgn");
```

```node
const stripe = require('stripe')('<<secret key>>');

const promotionCode = await stripe.promotionCodes.retrieve('promo_1MiM6KLkdIwHu7ixrIaX4wgn');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

promotion_code = stripe.PromotionCode.retrieve("promo_1MiM6KLkdIwHu7ixrIaX4wgn")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$promotionCode = $stripe->promotionCodes->retrieve('promo_1MiM6KLkdIwHu7ixrIaX4wgn', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

promotion_code = Stripe::PromotionCode.retrieve('promo_1MiM6KLkdIwHu7ixrIaX4wgn')
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