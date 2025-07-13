# Search products

Search for products you’ve previously created using Stripe’s [Search Query Language](https://docs.stripe.com/docs/search.md#search-query-language).
Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
to an hour behind during outages. Search functionality is not available to merchants in India.

A dictionary with a `data` property that contains an array of up to `limit` products. If no objects match the
query, the resulting array will be empty. See the related guide on [expanding properties in lists](https://docs.stripe.com/docs/expand.md#lists).

- `query` (string, required)
  The search query string. See [search query language](https://docs.stripe.com/docs/search.md#search-query-language) and the list of supported [query fields for products](https://docs.stripe.com/docs/search.md#query-fields-for-products).

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `page` (string, optional)
  A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new ProductSearchOptions { Query = "active:'true' AND metadata['order_id']:'6735'" };
var service = new ProductService();
StripeSearchResult<Product> products = service.Search(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.ProductSearchParams{
  SearchParams: stripe.SearchParams{Query: "active:'true' AND metadata['order_id']:'6735'"},
};
result := product.Search(params);
```

```java
Stripe.apiKey = "<<secret key>>";

ProductSearchParams params =
  ProductSearchParams.builder().setQuery("active:'true' AND metadata['order_id']:'6735'").build();

ProductSearchResult products = Product.search(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const products = await stripe.products.search({
  query: 'active:\'true\' AND metadata[\'order_id\']:\'6735\'',
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

products = stripe.Product.search(query="active:'true' AND metadata['order_id']:'6735'")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$products = $stripe->products->search([
  'query' => 'active:\'true\' AND metadata[\'order_id\']:\'6735\'',
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

products = Stripe::Product.search({query: 'active:\'true\' AND metadata[\'order_id\']:\'6735\''})
```

### Response

```json
{
  "object": "search_result",
  "url": "/v1/products/search",
  "has_more": false,
  "data": [
    {
      "id": "prod_NZOkxQ8eTZEHwN",
      "object": "product",
      "active": true,
      "created": 1679446501,
      "default_price": null,
      "description": null,
      "images": [],
      "livemode": false,
      "metadata": {
        "order_id": "6735"
      },
      "name": "Gold Plan",
      "package_dimensions": null,
      "shippable": null,
      "statement_descriptor": null,
      "tax_code": null,
      "unit_label": null,
      "updated": 1679446501,
      "url": null
    }
  ]
}
```