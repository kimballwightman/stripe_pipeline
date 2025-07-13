# Update a tax rate

Updates an existing tax rate.

The updated tax rate.

- `active` (boolean, optional)
  Flag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

- `country` (string, optional)
  Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

- `description` (string, optional)
  An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

- `display_name` (string, optional)
  The display name of the tax rate, which will be shown to users.

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

var options = new TaxRateUpdateOptions { Active = false };
var service = new TaxRateService();
TaxRate taxRate = service.Update("txr_1MzS4RLkdIwHu7ixwvpZ9c2i", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TaxRateParams{Active: stripe.Bool(false)};
result, err := taxrate.Update("txr_1MzS4RLkdIwHu7ixwvpZ9c2i", params);
```

```java
Stripe.apiKey = "<<secret key>>";

TaxRate resource = TaxRate.retrieve("txr_1MzS4RLkdIwHu7ixwvpZ9c2i");

TaxRateUpdateParams params = TaxRateUpdateParams.builder().setActive(false).build();

TaxRate taxRate = resource.update(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const taxRate = await stripe.taxRates.update(
  'txr_1MzS4RLkdIwHu7ixwvpZ9c2i',
  {
    active: false,
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

tax_rate = stripe.TaxRate.modify(
  "txr_1MzS4RLkdIwHu7ixwvpZ9c2i",
  active=False,
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$taxRate = $stripe->taxRates->update('txr_1MzS4RLkdIwHu7ixwvpZ9c2i', ['active' => false]);
```

```ruby
Stripe.api_key = '<<secret key>>'

tax_rate = Stripe::TaxRate.update('txr_1MzS4RLkdIwHu7ixwvpZ9c2i', {active: false})
```

### Response

```json
{
  "id": "txr_1MzS4RLkdIwHu7ixwvpZ9c2i",
  "object": "tax_rate",
  "active": false,
  "country": null,
  "created": 1682114687,
  "description": "VAT Germany",
  "display_name": "VAT",
  "effective_percentage": 16,
  "inclusive": false,
  "jurisdiction": "DE",
  "livemode": false,
  "metadata": {},
  "percentage": 16,
  "state": null,
  "tax_type": null
}
```