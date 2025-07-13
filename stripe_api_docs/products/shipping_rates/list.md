# List all shipping rates

Returns a list of your shipping rates.

A dictionary with a `data` property that contains an array of up to `limit` shipping rates, starting after shipping rate `starting_after`. Each entry in the array is a separate shipping rate object. If no more shipping rates are available, the resulting array will be empty. This require should never raise an error.

- `active` (boolean, optional)
  Only return shipping rates that are active or inactive.

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

- `currency` (enum, optional)
  Only return shipping rates for the given currency.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new ShippingRateListOptions { Limit = 3 };
var service = new ShippingRateService();
StripeList<ShippingRate> shippingRates = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.ShippingRateListParams{};
params.Limit = stripe.Int64(3)
result := shippingrate.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

ShippingRateListParams params = ShippingRateListParams.builder().setLimit(3L).build();

ShippingRateCollection shippingRates = ShippingRate.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const shippingRates = await stripe.shippingRates.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

shipping_rates = stripe.ShippingRate.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$shippingRates = $stripe->shippingRates->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

shipping_rates = Stripe::ShippingRate.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/shipping_rates",
  "has_more": false,
  "data": [
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
  ]
}
```