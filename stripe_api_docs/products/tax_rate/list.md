# List all tax rates

Returns a list of your tax rates. Tax rates are returned sorted by creation date, with the most recently created tax rates appearing first.

A dictionary with a `data` property that contains an array of up to `limit` tax rates, starting after tax rate `starting_after`. Each entry in the array is a separate tax rate object. If no more tax rates are available, the resulting array will be empty.

- `active` (boolean, optional)
  Optional flag to filter by tax rates that are either active or inactive (archived).

- `created` (object, optional)
  Optional range for filtering created date.

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

- `inclusive` (boolean, optional)
  Optional flag to filter by tax rates that are inclusive (or those that are not inclusive).

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new TaxRateListOptions { Limit = 3 };
var service = new TaxRateService();
StripeList<TaxRate> taxRates = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TaxRateListParams{};
params.Limit = stripe.Int64(3)
result := taxrate.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

TaxRateListParams params = TaxRateListParams.builder().setLimit(3L).build();

TaxRateCollection taxRates = TaxRate.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const taxRates = await stripe.taxRates.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

tax_rates = stripe.TaxRate.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$taxRates = $stripe->taxRates->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

tax_rates = Stripe::TaxRate.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/tax_rates",
  "has_more": false,
  "data": [
    {
      "id": "txr_1MzS4RLkdIwHu7ixwvpZ9c2i",
      "object": "tax_rate",
      "active": true,
      "country": null,
      "created": 1682114687,
      "description": "VAT Germany",
      "display_name": "VAT",
      "inclusive": false,
      "jurisdiction": "DE",
      "livemode": false,
      "metadata": {},
      "percentage": 16,
      "state": null,
      "tax_type": null
    }
  ]
}
```