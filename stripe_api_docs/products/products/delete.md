# Delete a product

Delete a product. Deleting a product is only possible if it has no prices associated with it. Additionally, deleting a product with `type=good` is only possible if it has no SKUs associated with it.

Returns a deleted object on success. Otherwise, this call raises [an error](#errors).


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new ProductService();
Product deleted = service.Delete("prod_NWjs8kKbJWmuuc");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.ProductParams{};
result, err := product.Del("prod_NWjs8kKbJWmuuc", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Product resource = Product.retrieve("prod_NWjs8kKbJWmuuc");

Product product = resource.delete();
```

```node
const stripe = require('stripe')('<<secret key>>');

const deleted = await stripe.products.del('prod_NWjs8kKbJWmuuc');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

deleted = stripe.Product.delete("prod_NWjs8kKbJWmuuc")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$deleted = $stripe->products->delete('prod_NWjs8kKbJWmuuc', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

deleted = Stripe::Product.delete('prod_NWjs8kKbJWmuuc')
```

### Response

```json
{
  "id": "prod_NWjs8kKbJWmuuc",
  "object": "product",
  "deleted": true
}
```