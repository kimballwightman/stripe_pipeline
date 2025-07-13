# Create a tax rate

Creates a new tax rate.

The created tax rate object.

- `display_name` (string, required)
  The display name of the tax rate, which will be shown to users.

- `inclusive` (boolean, required)
  This specifies if the tax rate is inclusive or exclusive.

- `percentage` (float, required)
  This represents the tax rate percent out of 100.

- `active` (boolean, optional)
  Flag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

- `country` (string, optional)
  Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

- `description` (string, optional)
  An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

- `jurisdiction` (string, optional)
  The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `state` (string, optional)
  [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

- `tax_type` (enum, optional)
  The high-level tax type, such as `vat` or `sales_tax`.

  Amusement Tax

  Communications Tax

  Goods and Services Tax

  Harmonized Sales Tax

  Integrated Goods and Services Tax

  Japanese Consumption Tax

  Chicago Lease Tax

  Provincial Sales Tax

  Quebec Sales Tax

  Retail Delivery Fee

  Retail Sales Tax

  Sales Tax

  Service Tax

  Value-Added Tax

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new TaxRateCreateOptions
{
    DisplayName = "VAT",
    Description = "VAT Germany",
    Percentage = 16M,
    Jurisdiction = "DE",
    Inclusive = false,
};
var service = new TaxRateService();
TaxRate taxRate = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TaxRateParams{
  DisplayName: stripe.String("VAT"),
  Description: stripe.String("VAT Germany"),
  Percentage: stripe.Float64(16),
  Jurisdiction: stripe.String("DE"),
  Inclusive: stripe.Bool(false),
};
result, err := taxrate.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

TaxRateCreateParams params =
  TaxRateCreateParams.builder()
    .setDisplayName("VAT")
    .setDescription("VAT Germany")
    .setPercentage(new BigDecimal(16))
    .setJurisdiction("DE")
    .setInclusive(false)
    .build();

TaxRate taxRate = TaxRate.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const taxRate = await stripe.taxRates.create({
  display_name: 'VAT',
  description: 'VAT Germany',
  percentage: 16,
  jurisdiction: 'DE',
  inclusive: false,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

tax_rate = stripe.TaxRate.create(
  display_name="VAT",
  description="VAT Germany",
  percentage=16,
  jurisdiction="DE",
  inclusive=False,
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$taxRate = $stripe->taxRates->create([
  'display_name' => 'VAT',
  'description' => 'VAT Germany',
  'percentage' => 16,
  'jurisdiction' => 'DE',
  'inclusive' => false,
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

tax_rate = Stripe::TaxRate.create({
  display_name: 'VAT',
  description: 'VAT Germany',
  percentage: 16,
  jurisdiction: 'DE',
  inclusive: false,
})
```

### Response

```json
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
```