# Create a product

Creates a new product object.

Returns a product object if the call succeeded.

- `name` (string, required)
  The product’s name, meant to be displayable to the customer.

- `active` (boolean, optional)
  Whether the product is currently available for purchase. Defaults to `true`.

- `default_price_data` (object, optional)
  Data used to generate a new [Price](https://docs.stripe.com/docs/api/prices.md) object. This Price will be set as the default price for this product.

  - `default_price_data.currency` (enum, required)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `default_price_data.currency_options` (object, optional)
    Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

    - `default_price_data.currency_options.<currency>.custom_unit_amount` (object, optional)
      When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

      - `default_price_data.currency_options.<currency>.custom_unit_amount.enabled` (boolean, required)
        Pass in `true` to enable `custom_unit_amount`, otherwise omit `custom_unit_amount`.

      - `default_price_data.currency_options.<currency>.custom_unit_amount.maximum` (integer, optional)
        The maximum unit amount the customer can specify for this item.

      - `default_price_data.currency_options.<currency>.custom_unit_amount.minimum` (integer, optional)
        The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

      - `default_price_data.currency_options.<currency>.custom_unit_amount.preset` (integer, optional)
        The starting unit amount which can be updated by the customer.

    - `default_price_data.currency_options.<currency>.tax_behavior` (enum, optional)
      Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.

    - `default_price_data.currency_options.<currency>.tiers` (array of objects, optional)
      Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

      - `default_price_data.currency_options.<currency>.tiers.up_to` (string | integer, required)
        Specifies the upper bound of this tier. The lower bound of a tier is the upper bound of the previous tier adding one. Use `inf` to define a fallback tier.

      - `default_price_data.currency_options.<currency>.tiers.flat_amount` (integer, optional)
        The flat billing amount for an entire tier, regardless of the number of units in the tier.

      - `default_price_data.currency_options.<currency>.tiers.flat_amount_decimal` (string, optional)
        Same as `flat_amount`, but accepts a decimal value representing an integer in the minor units of the currency. Only one of `flat_amount` and `flat_amount_decimal` can be set.

      - `default_price_data.currency_options.<currency>.tiers.unit_amount` (integer, optional)
        The per unit billing amount for each individual unit for which this tier applies.

      - `default_price_data.currency_options.<currency>.tiers.unit_amount_decimal` (string, optional)
        Same as `unit_amount`, but accepts a decimal value in  with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

    - `default_price_data.currency_options.<currency>.unit_amount` (integer, optional)
      A positive integer in  (or 0 for a free price) representing how much to charge.

    - `default_price_data.currency_options.<currency>.unit_amount_decimal` (string, optional)
      Same as `unit_amount`, but accepts a decimal value in  with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

  - `default_price_data.custom_unit_amount` (object, optional)
    When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

    - `default_price_data.custom_unit_amount.enabled` (boolean, required)
      Pass in `true` to enable `custom_unit_amount`, otherwise omit `custom_unit_amount`.

    - `default_price_data.custom_unit_amount.maximum` (integer, optional)
      The maximum unit amount the customer can specify for this item.

    - `default_price_data.custom_unit_amount.minimum` (integer, optional)
      The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

    - `default_price_data.custom_unit_amount.preset` (integer, optional)
      The starting unit amount which can be updated by the customer.

  - `default_price_data.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

  - `default_price_data.recurring` (object, optional)
    The recurring components of a price such as `interval` and `interval_count`.

    - `default_price_data.recurring.interval` (enum, required)
      Specifies billing frequency. Either `day`, `week`, `month` or `year`.

    - `default_price_data.recurring.interval_count` (integer, optional)
      The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).

  - `default_price_data.tax_behavior` (enum, optional)
    Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.

  - `default_price_data.unit_amount` (integer, optional)
    A positive integer in  (or 0 for a free price) representing how much to charge. One of `unit_amount`, `unit_amount_decimal`, or `custom_unit_amount` is required.

  - `default_price_data.unit_amount_decimal` (string, optional)
    Same as `unit_amount`, but accepts a decimal value in  with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

- `description` (string, optional)
  The product’s description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.

- `id` (string, optional)
  An identifier will be randomly generated by Stripe. You can optionally override this ID, but the ID must be unique across all products in your Stripe account.

- `images` (array of strings, optional)
  A list of up to 8 URLs of images for this product, meant to be displayable to the customer.

- `marketing_features` (array of objects, optional)
  A list of up to 15 marketing features for this product. These are displayed in [pricing tables](https://docs.stripe.com/docs/payments/checkout/pricing-table.md).

  - `marketing_features.name` (string, required)
    The marketing feature name. Up to 80 characters long.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `shippable` (boolean, optional)
  Whether this product is shipped (i.e., physical goods).

- `statement_descriptor` (string, optional)
  An arbitrary string to be displayed on your customer’s credit card or bank statement. While most banks display this information consistently, some may display it incorrectly or not at all.

  This may be up to 22 characters. The statement description may not include `<`, `>`, `\`, `"`, `'` characters, and will appear on your customer’s statement in capital letters. Non-ASCII characters are automatically stripped.
  It must contain at least one letter. Only used for subscription payments.

- `tax_code` (string, optional)
  A [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID.

- `unit_label` (string, optional)
  A label that represents units of this product. When set, this will be included in customers’ receipts, invoices, Checkout, and the customer portal.

- `url` (string, optional)
  A URL of a publicly-accessible webpage for this product.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new ProductCreateOptions { Name = "Gold Plan" };
var service = new ProductService();
Product product = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.ProductParams{Name: stripe.String("Gold Plan")};
result, err := product.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

ProductCreateParams params = ProductCreateParams.builder().setName("Gold Plan").build();

Product product = Product.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const product = await stripe.products.create({
  name: 'Gold Plan',
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

product = stripe.Product.create(name="Gold Plan")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$product = $stripe->products->create(['name' => 'Gold Plan']);
```

```ruby
Stripe.api_key = '<<secret key>>'

product = Stripe::Product.create({name: 'Gold Plan'})
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