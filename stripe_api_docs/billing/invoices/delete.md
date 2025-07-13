# Delete a draft invoice

Permanently deletes a one-off invoice draft. This cannot be undone. Attempts to delete invoices that are no longer in a draft state will fail; once an invoice has been finalized or if an invoice is for a subscription, it must be [voided](#void_invoice).

A successfully deleted invoice. Otherwise, this call raises [an error](#errors), such as if the invoice has already been deleted.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new InvoiceService();
Invoice deleted = service.Delete("in_1MtHbELkdIwHu7ixl4OzzPMv");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.InvoiceParams{};
result, err := invoice.Del("in_1MtHbELkdIwHu7ixl4OzzPMv", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Invoice resource = Invoice.retrieve("in_1MtHbELkdIwHu7ixl4OzzPMv");

Invoice invoice = resource.delete();
```

```node
const stripe = require('stripe')('<<secret key>>');

const deleted = await stripe.invoices.del('in_1MtHbELkdIwHu7ixl4OzzPMv');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

deleted = stripe.Invoice.delete("in_1MtHbELkdIwHu7ixl4OzzPMv")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$deleted = $stripe->invoices->delete('in_1MtHbELkdIwHu7ixl4OzzPMv', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

deleted = Stripe::Invoice.delete('in_1MtHbELkdIwHu7ixl4OzzPMv')
```

### Response

```json
{
  "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",
  "object": "invoice",
  "deleted": true
}
```