# Retrieve an invoice item

Retrieves the invoice item with the given ID.

Returns an invoice item if a valid invoice item ID was provided. Raises [an error](#errors) otherwise.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new InvoiceItemService();
InvoiceItem invoiceItem = service.Get("ii_1MtGUtLkdIwHu7ixBYwjAM00");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.InvoiceItemParams{};
result, err := invoiceitem.Get("ii_1MtGUtLkdIwHu7ixBYwjAM00", params);
```

```java
Stripe.apiKey = "<<secret key>>";

InvoiceItem invoiceItem = InvoiceItem.retrieve("ii_1MtGUtLkdIwHu7ixBYwjAM00");
```

```node
const stripe = require('stripe')('<<secret key>>');

const invoiceItem = await stripe.invoiceItems.retrieve('ii_1MtGUtLkdIwHu7ixBYwjAM00');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

invoice_item = stripe.InvoiceItem.retrieve("ii_1MtGUtLkdIwHu7ixBYwjAM00")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$invoiceItem = $stripe->invoiceItems->retrieve('ii_1MtGUtLkdIwHu7ixBYwjAM00', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

invoice_item = Stripe::InvoiceItem.retrieve('ii_1MtGUtLkdIwHu7ixBYwjAM00')
```

### Response

```json
{
  "id": "ii_1MtGUtLkdIwHu7ixBYwjAM00",
  "object": "invoiceitem",
  "amount": 1099,
  "currency": "usd",
  "customer": "cus_NeZei8imSbMVvi",
  "date": 1680640231,
  "description": "T-shirt",
  "discountable": true,
  "discounts": [],
  "invoice": null,
  "livemode": false,
  "metadata": {},
  "parent": null,
  "period": {
    "end": 1680640231,
    "start": 1680640231
  },
  "pricing": {
    "price_details": {
      "price": "price_1MtGUsLkdIwHu7ix1be5Ljaj",
      "product": "prod_NeZe7xbBdJT8EN"
    },
    "type": "price_details",
    "unit_amount_decimal": "1099"
  },
  "proration": false,
  "quantity": 1,
  "tax_rates": [],
  "test_clock": null
}
```