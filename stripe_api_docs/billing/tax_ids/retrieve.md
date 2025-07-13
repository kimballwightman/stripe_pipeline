# Retrieve a tax ID

Retrieves an account or customer `tax_id` object.

Returns a `tax_id` object if a valid identifier was provided.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new TaxIdService();
TaxId taxId = service.Get("txi_1NuMB12eZvKYlo2CMecoWkZd");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TaxIDParams{};
result, err := taxid.Get("txi_1NuMB12eZvKYlo2CMecoWkZd", params);
```

```java
Stripe.apiKey = "<<secret key>>";

TaxId taxId = TaxId.retrieve("txi_1NuMB12eZvKYlo2CMecoWkZd");
```

```node
const stripe = require('stripe')('<<secret key>>');

const taxId = await stripe.taxIds.retrieve('txi_1NuMB12eZvKYlo2CMecoWkZd');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

tax_id = stripe.TaxId.retrieve("txi_1NuMB12eZvKYlo2CMecoWkZd")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$taxId = $stripe->taxIds->retrieve('txi_1NuMB12eZvKYlo2CMecoWkZd', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

tax_id = Stripe::TaxId.retrieve('txi_1NuMB12eZvKYlo2CMecoWkZd')
```

### Response

```json
{
  "id": "txi_1NuMB12eZvKYlo2CMecoWkZd",
  "object": "tax_id",
  "country": "DE",
  "created": 123456789,
  "customer": null,
  "livemode": false,
  "type": "eu_vat",
  "value": "DE123456789",
  "verification": null,
  "owner": {
    "type": "self",
    "customer": null
  }
}
```