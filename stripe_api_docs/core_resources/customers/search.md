# Search customers

Search for customers you’ve previously created using Stripe’s [Search Query Language](https://docs.stripe.com/docs/search.md#search-query-language).
Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
to an hour behind during outages. Search functionality is not available to merchants in India.

A dictionary with a `data` property that contains an array of up to `limit` customers. If no objects match the
query, the resulting array will be empty. See the related guide on [expanding properties in lists](https://docs.stripe.com/docs/expand.md#lists).

- `query` (string, required)
  The search query string. See [search query language](https://docs.stripe.com/docs/search.md#search-query-language) and the list of supported [query fields for customers](https://docs.stripe.com/docs/search.md#query-fields-for-customers).

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `page` (string, optional)
  A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CustomerSearchOptions { Query = "name:'Jane Doe' AND metadata['foo']:'bar'" };
var service = new CustomerService();
StripeSearchResult<Customer> customers = service.Search(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CustomerSearchParams{
  SearchParams: stripe.SearchParams{Query: "name:'Jane Doe' AND metadata['foo']:'bar'"},
};
result := customer.Search(params);
```

```java
Stripe.apiKey = "<<secret key>>";

CustomerSearchParams params =
  CustomerSearchParams.builder().setQuery("name:'Jane Doe' AND metadata['foo']:'bar'").build();

CustomerSearchResult customers = Customer.search(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const customers = await stripe.customers.search({
  query: 'name:\'Jane Doe\' AND metadata[\'foo\']:\'bar\'',
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

customers = stripe.Customer.search(query="name:'Jane Doe' AND metadata['foo']:'bar'")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$customers = $stripe->customers->search([
  'query' => 'name:\'Jane Doe\' AND metadata[\'foo\']:\'bar\'',
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

customers = Stripe::Customer.search({query: 'name:\'Jane Doe\' AND metadata[\'foo\']:\'bar\''})
```

### Response

```json
{
  "object": "search_result",
  "url": "/v1/customers/search",
  "has_more": false,
  "data": [
    {
      "id": "cus_NeGfPRiPKxeBi1",
      "object": "customer",
      "address": null,
      "balance": 0,
      "created": 1680569616,
      "currency": null,
      "default_source": null,
      "delinquent": false,
      "description": null,
      "email": null,
      "invoice_prefix": "47D37F8F",
      "invoice_settings": {
        "custom_fields": null,
        "default_payment_method": "pm_1Msy7wLkdIwHu7ixsxmFvcz7",
        "footer": null,
        "rendering_options": null
      },
      "livemode": false,
      "metadata": {
        "foo": "bar"
      },
      "name": "Jane Doe",
      "next_invoice_sequence": 1,
      "phone": null,
      "preferred_locales": [],
      "shipping": null,
      "tax_exempt": "none",
      "test_clock": null
    }
  ]
}
```