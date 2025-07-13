# Retrieve a tax code

Retrieves the details of an existing tax code. Supply the unique tax code ID and Stripe will return the corresponding tax code information.

Returns a tax code object if a valid identifier was provided.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new TaxCodeService();
TaxCode taxCode = service.Get("txcd_99999999");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TaxCodeParams{};
result, err := taxcode.Get("txcd_99999999", params);
```

```java
Stripe.apiKey = "<<secret key>>";

TaxCode taxCode = TaxCode.retrieve("txcd_99999999");
```

```node
const stripe = require('stripe')('<<secret key>>');

const taxCode = await stripe.taxCodes.retrieve('txcd_99999999');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

tax_code = stripe.TaxCode.retrieve("txcd_99999999")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$taxCode = $stripe->taxCodes->retrieve('txcd_99999999', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

tax_code = Stripe::TaxCode.retrieve('txcd_99999999')
```

### Response

```json
{
  "id": "txcd_99999999",
  "object": "tax_code",
  "description": "Any tangible or physical good. For jurisdictions that impose a tax, the standard rate is applied.",
  "name": "General - Tangible Goods"
}
```