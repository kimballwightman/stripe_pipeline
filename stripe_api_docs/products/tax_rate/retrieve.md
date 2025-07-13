# Retrieve a tax rate

Retrieves a tax rate with the given ID

Returns an tax rate if a valid tax rate ID was provided. Raises [an error](#errors) otherwise.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new TaxRateService();
TaxRate taxRate = service.Get("txr_1MzS4RLkdIwHu7ixwvpZ9c2i");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TaxRateParams{};
result, err := taxrate.Get("txr_1MzS4RLkdIwHu7ixwvpZ9c2i", params);
```

```java
Stripe.apiKey = "<<secret key>>";

TaxRate taxRate = TaxRate.retrieve("txr_1MzS4RLkdIwHu7ixwvpZ9c2i");
```

```node
const stripe = require('stripe')('<<secret key>>');

const taxRate = await stripe.taxRates.retrieve('txr_1MzS4RLkdIwHu7ixwvpZ9c2i');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

tax_rate = stripe.TaxRate.retrieve("txr_1MzS4RLkdIwHu7ixwvpZ9c2i")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$taxRate = $stripe->taxRates->retrieve('txr_1MzS4RLkdIwHu7ixwvpZ9c2i', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

tax_rate = Stripe::TaxRate.retrieve('txr_1MzS4RLkdIwHu7ixwvpZ9c2i')
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