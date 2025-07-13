# Retrieve a product

Retrieves the details of an existing product. Supply the unique product ID from either a product creation request or the product list, and Stripe will return the corresponding product information.

Returns a product object if a valid identifier was provided.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new ProductService();
Product product = service.Get("prod_NWjs8kKbJWmuuc");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.ProductParams{};
result, err := product.Get("prod_NWjs8kKbJWmuuc", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Product product = Product.retrieve("prod_NWjs8kKbJWmuuc");
```

```node
const stripe = require('stripe')('<<secret key>>');

const product = await stripe.products.retrieve('prod_NWjs8kKbJWmuuc');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

product = stripe.Product.retrieve("prod_NWjs8kKbJWmuuc")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$product = $stripe->products->retrieve('prod_NWjs8kKbJWmuuc', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

product = Stripe::Product.retrieve('prod_NWjs8kKbJWmuuc')
```

### Response

```json
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
```