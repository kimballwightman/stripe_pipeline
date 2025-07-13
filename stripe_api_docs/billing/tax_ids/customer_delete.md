# Delete a Customer tax ID

Deletes an existing `tax_id` object.

Returns an object with a deleted parameter on success. If the `tax_id` object does not exist, this call raises [an error](#errors).


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new CustomerTaxIdService();
TaxId deleted = service.Delete("cus_NZKoSNZZ58qtO0", "txi_1MoC8zLkdIwHu7ixEhgWcHzJ");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TaxIDParams{Customer: stripe.String("cus_NZKoSNZZ58qtO0")};
result, err := taxid.Del("txi_1MoC8zLkdIwHu7ixEhgWcHzJ", params);
```

```java
Stripe.apiKey = "<<secret key>>";

TaxId resource = TaxId.retrieve("cus_NZKoSNZZ58qtO0", "txi_1MoC8zLkdIwHu7ixEhgWcHzJ");

TaxId taxId = resource.delete();
```

```node
const stripe = require('stripe')('<<secret key>>');

const deleted = await stripe.customers.deleteTaxId(
  'cus_NZKoSNZZ58qtO0',
  'txi_1MoC8zLkdIwHu7ixEhgWcHzJ'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

deleted = stripe.Customer.delete_tax_id(
  "cus_NZKoSNZZ58qtO0",
  "txi_1MoC8zLkdIwHu7ixEhgWcHzJ",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$deleted = $stripe->customers->deleteTaxId(
  'cus_NZKoSNZZ58qtO0',
  'txi_1MoC8zLkdIwHu7ixEhgWcHzJ',
  []
);
```

```ruby
Stripe.api_key = '<<secret key>>'

deleted = Stripe::Customer.delete_tax_id('cus_NZKoSNZZ58qtO0', 'txi_1MoC8zLkdIwHu7ixEhgWcHzJ')
```

### Response

```json
{
  "id": "txi_1MoC8zLkdIwHu7ixEhgWcHzJ",
  "object": "tax_id",
  "deleted": true
}
```