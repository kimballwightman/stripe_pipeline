# Retrieve a Customer tax ID

Retrieves the `tax_id` object with the given identifier.

Returns a `tax_id` object if a valid identifier was provided.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new CustomerTaxIdService();
TaxId taxId = service.Get("cus_NZKoSNZZ58qtO0", "txi_1MoC8zLkdIwHu7ixEhgWcHzJ");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TaxIDParams{Customer: stripe.String("cus_NZKoSNZZ58qtO0")};
result, err := taxid.Get("txi_1MoC8zLkdIwHu7ixEhgWcHzJ", params);
```

```java
Stripe.apiKey = "<<secret key>>";

TaxId taxId = TaxId.retrieve("cus_NZKoSNZZ58qtO0", "txi_1MoC8zLkdIwHu7ixEhgWcHzJ");
```

```node
const stripe = require('stripe')('<<secret key>>');

const taxId = await stripe.customers.retrieveTaxId(
  'cus_NZKoSNZZ58qtO0',
  'txi_1MoC8zLkdIwHu7ixEhgWcHzJ'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

tax_id = stripe.Customer.retrieve_tax_id(
  "cus_NZKoSNZZ58qtO0",
  "txi_1MoC8zLkdIwHu7ixEhgWcHzJ",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$taxId = $stripe->customers->retrieveTaxId(
  'cus_NZKoSNZZ58qtO0',
  'txi_1MoC8zLkdIwHu7ixEhgWcHzJ',
  []
);
```

```ruby
Stripe.api_key = '<<secret key>>'

tax_id = Stripe::Customer.retrieve_tax_id('cus_NZKoSNZZ58qtO0', 'txi_1MoC8zLkdIwHu7ixEhgWcHzJ')
```

### Response

```json
{
  "id": "txi_1MoC8zLkdIwHu7ixEhgWcHzJ",
  "object": "tax_id",
  "country": "DE",
  "created": 1679431857,
  "customer": "cus_NZKoSNZZ58qtO0",
  "livemode": false,
  "type": "eu_vat",
  "value": "DE123456789",
  "verification": {
    "status": "pending",
    "verified_address": null,
    "verified_name": null
  }
}
```