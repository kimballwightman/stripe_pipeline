# Update a product

Updates the specific product by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

Returns the product object if the update succeeded.

- `active` (boolean, optional)
  Whether the product is available for purchase.

- `description` (string, optional)
  The product’s description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.

- `images` (array of strings, optional)
  A list of up to 8 URLs of images for this product, meant to be displayable to the customer.

- `marketing_features` (array of objects, optional)
  A list of up to 15 marketing features for this product. These are displayed in [pricing tables](https://docs.stripe.com/docs/payments/checkout/pricing-table.md).

  - `marketing_features.name` (string, required)
    The marketing feature name. Up to 80 characters long.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `name` (string, optional)
  The product’s name, meant to be displayable to the customer.

- `shippable` (boolean, optional)
  Whether this product is shipped (i.e., physical goods).

- `statement_descriptor` (string, optional)
  An arbitrary string to be displayed on your customer’s credit card or bank statement. While most banks display this information consistently, some may display it incorrectly or not at all.

  This may be up to 22 characters. The statement description may not include `<`, `>`, `\`, `"`, `'` characters, and will appear on your customer’s statement in capital letters. Non-ASCII characters are automatically stripped.
  It must contain at least one letter. May only be set if `type=service`. Only used for subscription payments.

- `tax_code` (string, optional)
  A [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID.

- `unit_label` (string, optional)
  A label that represents units of this product. When set, this will be included in customers’ receipts, invoices, Checkout, and the customer portal. May only be set if `type=service`.

- `url` (string, optional)
  A URL of a publicly-accessible webpage for this product.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new ProductUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var service = new ProductService();
Product product = service.Update("prod_NWjs8kKbJWmuuc", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.ProductParams{};
params.AddMetadata("order_id", "6735")
result, err := product.Update("prod_NWjs8kKbJWmuuc", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Product resource = Product.retrieve("prod_NWjs8kKbJWmuuc");

ProductUpdateParams params = ProductUpdateParams.builder().putMetadata("order_id", "6735").build();

Product product = resource.update(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const product = await stripe.products.update(
  'prod_NWjs8kKbJWmuuc',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

product = stripe.Product.modify(
  "prod_NWjs8kKbJWmuuc",
  metadata={"order_id": "6735"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$product = $stripe->products->update('prod_NWjs8kKbJWmuuc', ['metadata' => ['order_id' => '6735']]);
```

```ruby
Stripe.api_key = '<<secret key>>'

product = Stripe::Product.update('prod_NWjs8kKbJWmuuc', {metadata: {order_id: '6735'}})
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
  "metadata": {
    "order_id": "6735"
  },
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