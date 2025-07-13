# List all tax codes

A list of [all tax codes available](https://stripe.com/docs/tax/tax-categories) to add to Products in order to allow specific tax calculations.

A dictionary with a data property that contains an array of up to limit tax codes, starting after tax code starting_after. Each entry in the array is a separate tax code object. If no more tax codes are available, the resulting array will be empty. This request should never return an error.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new TaxCodeListOptions { Limit = 3 };
var service = new TaxCodeService();
StripeList<TaxCode> taxCodes = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TaxCodeListParams{};
params.Limit = stripe.Int64(3)
result := taxcode.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

TaxCodeListParams params = TaxCodeListParams.builder().setLimit(3L).build();

TaxCodeCollection taxCodes = TaxCode.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const taxCodes = await stripe.taxCodes.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

tax_codes = stripe.TaxCode.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$taxCodes = $stripe->taxCodes->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

tax_codes = Stripe::TaxCode.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/tax_codes",
  "has_more": false,
  "data": [
    {
      "id": "txcd_99999999",
      "object": "tax_code",
      "description": "Any tangible or physical good. For jurisdictions that impose a tax, the standard rate is applied.",
      "name": "General - Tangible Goods"
    }
  ]
}
```