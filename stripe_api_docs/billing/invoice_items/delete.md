# Delete an invoice item

Deletes an invoice item, removing it from an invoice. Deleting invoice items is only possible when they’re not attached to invoices, or if it’s attached to a draft invoice.

An object with the deleted invoice item’s ID and a deleted flag upon success. Otherwise, this call raises [an error](#errors), such as if the invoice item has already been deleted.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new InvoiceItemService();
InvoiceItem deleted = service.Delete("ii_1MtGUtLkdIwHu7ixBYwjAM00");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.InvoiceItemParams{};
result, err := invoiceitem.Del("ii_1MtGUtLkdIwHu7ixBYwjAM00", params);
```

```java
Stripe.apiKey = "<<secret key>>";

InvoiceItem resource = InvoiceItem.retrieve("ii_1MtGUtLkdIwHu7ixBYwjAM00");

InvoiceItem invoiceItem = resource.delete();
```

```node
const stripe = require('stripe')('<<secret key>>');

const deleted = await stripe.invoiceItems.del('ii_1MtGUtLkdIwHu7ixBYwjAM00');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

deleted = stripe.InvoiceItem.delete("ii_1MtGUtLkdIwHu7ixBYwjAM00")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$deleted = $stripe->invoiceItems->delete('ii_1MtGUtLkdIwHu7ixBYwjAM00', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

deleted = Stripe::InvoiceItem.delete('ii_1MtGUtLkdIwHu7ixBYwjAM00')
```

### Response

```json
{
  "id": "ii_1MtGUtLkdIwHu7ixBYwjAM00",
  "object": "invoiceitem",
  "deleted": true
}
```