# List all promotion codes

Returns a list of your promotion codes.

A dictionary with a `data` property that contains an array of up to `limit` promotion codes, starting after promotion code `starting_after`. Each entry in the array is a separate promotion code object. If no more promotion codes are available, the resulting array will be empty.

- `active` (boolean, optional)
  Filter promotion codes by whether they are active.

- `code` (string, optional)
  Only return promotion codes that have this case-insensitive code.

- `coupon` (string, optional)
  Only return promotion codes for this coupon.

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

- `customer` (string, optional)
  Only return promotion codes that are restricted to this customer.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new PromotionCodeListOptions { Limit = 3 };
var service = new PromotionCodeService();
StripeList<PromotionCode> promotionCodes = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PromotionCodeListParams{};
params.Limit = stripe.Int64(3)
result := promotioncode.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

PromotionCodeListParams params = PromotionCodeListParams.builder().setLimit(3L).build();

PromotionCodeCollection promotionCodes = PromotionCode.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const promotionCodes = await stripe.promotionCodes.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

promotion_codes = stripe.PromotionCode.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$promotionCodes = $stripe->promotionCodes->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

promotion_codes = Stripe::PromotionCode.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/promotion_codes",
  "has_more": false,
  "data": [
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
  ]
}
```