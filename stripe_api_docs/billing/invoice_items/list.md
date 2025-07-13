# List all invoice items

Returns a list of your invoice items. Invoice items are returned sorted by creation date, with the most recently created invoice items appearing first.

A dictionary with a `data` property that contains an array of up to `limit` invoice items, starting after invoice item `starting_after`. Each entry in the array is a separate invoice item object. If no more invoice items are available, the resulting array will be empty.

- `created` (object, optional)
  Only return invoice items that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `customer` (string, optional)
  The identifier of the customer whose invoice items to return. If none is provided, all invoice items will be returned.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `invoice` (string, optional)
  Only return invoice items belonging to this invoice. If none is provided, all invoice items will be returned. If specifying an invoice, no customer identifier is needed.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `pending` (boolean, optional)
  Set to `true` to only show pending invoice items, which are not yet attached to any invoices. Set to `false` to only show invoice items already attached to invoices. If unspecified, no filter is applied.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new InvoiceItemListOptions { Limit = 3 };
var service = new InvoiceItemService();
StripeList<InvoiceItem> invoiceItems = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.InvoiceItemListParams{};
params.Limit = stripe.Int64(3)
result := invoiceitem.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

InvoiceItemListParams params = InvoiceItemListParams.builder().setLimit(3L).build();

InvoiceItemCollection invoiceItems = InvoiceItem.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const invoiceItems = await stripe.invoiceItems.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

invoice_items = stripe.InvoiceItem.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$invoiceItems = $stripe->invoiceItems->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

invoice_items = Stripe::InvoiceItem.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/invoiceitems",
  "has_more": false,
  "data": [
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
  ]
}
```