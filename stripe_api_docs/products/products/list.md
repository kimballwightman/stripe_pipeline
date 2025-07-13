# List all products

Returns a list of your products. The products are returned sorted by creation date, with the most recently created products appearing first.

A dictionary with a `data` property that contains an array of up to `limit` products, starting after product `starting_after`. Each entry in the array is a separate product object. If no more products are available, the resulting array will be empty.

- `active` (boolean, optional)
  Only return products that are active or inactive (e.g., pass `false` to list all inactive products).

- `created` (object, optional)
  Only return products that were created during the given date interval.

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

- `ids` (array of strings, optional)
  Only return products with the given IDs. Cannot be used with [starting_after](#list_products-starting_after) or [ending_before](#list_products-ending_before).

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `shippable` (boolean, optional)
  Only return products that can be shipped (i.e., physical, not digital products).

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `url` (string, optional)
  Only return products with the given url.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new ProductListOptions { Limit = 3 };
var service = new ProductService();
StripeList<Product> products = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.ProductListParams{};
params.Limit = stripe.Int64(3)
result := product.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

ProductListParams params = ProductListParams.builder().setLimit(3L).build();

ProductCollection products = Product.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const products = await stripe.products.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

products = stripe.Product.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$products = $stripe->products->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

products = Stripe::Product.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/products",
  "has_more": false,
  "data": [
    {
      "id": "prod_NWjs8kKbJWmuuc",
      "object": "product",
      "active": true,
      "created": 1678833149,
      "default_price": null,
      "description": null,
      "images": [],
      "marketing_features": [],
      "livemode": false,
      "metadata": {},
      "name": "Gold Plan",
      "package_dimensions": null,
      "shippable": null,
      "statement_descriptor": null,
      "tax_code": null,
      "unit_label": null,
      "updated": 1678833149,
      "url": null
    }
  ]
}
```