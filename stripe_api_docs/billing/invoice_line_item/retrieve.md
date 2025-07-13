# Retrieve an invoice's line items

When retrieving an invoice, you’ll get a **lines** property containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

Returns a list of [line_item objects](#invoice_line_item_object).

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new InvoiceLineItemService();
StripeList<InvoiceLineItem> invoiceLineItems = service.List("in_1NpHok2eZvKYlo2CyeiBref0");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.InvoiceListLinesParams{Invoice: stripe.String("in_1NpHok2eZvKYlo2CyeiBref0")};
result := invoice.ListLines(params);
```

```java
Stripe.apiKey = "<<secret key>>";

Invoice invoice = Invoice.retrieve("in_1NpHok2eZvKYlo2CyeiBref0");

InvoiceLineItemCollectionListParams params = InvoiceLineItemCollectionListParams.builder().build();

InvoiceLineItemCollection invoiceLineItems = invoice.getLines().list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const invoiceLineItems = await stripe.invoices.listLineItems('in_1NpHok2eZvKYlo2CyeiBref0');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

invoice_line_items = stripe.Invoice.list_lines("in_1NpHok2eZvKYlo2CyeiBref0")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$invoiceLineItems = $stripe->invoices->allLines('in_1NpHok2eZvKYlo2CyeiBref0', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

invoice_line_items = Stripe::Invoice.list_lines('in_1NpHok2eZvKYlo2CyeiBref0')
```

### Response

```json
{
  "object": "list",
  "url": "/v1/invoices/in_1NpHiG2eZvKYlo2CZV0ZkEBT/lines",
  "has_more": false,
  "data": [
    {
      "id": "il_tmp_1NpHiK2eZvKYlo2C9NdV8VrI",
      "object": "line_item",
      "amount": 129999,
      "currency": "usd",
      "description": "My First Invoice Item (created for API docs)",
      "discount_amounts": [],
      "discountable": true,
      "discounts": [],
      "livemode": false,
      "metadata": {},
      "parent": {
        "type": "invoice_item_details",
        "invoice_item_details": {
          "invoice_item": "ii_1NpHiK2eZvKYlo2C9NdV8VrI",
          "proration": false,
          "proration_details": {
            "credited_items": null
          },
          "subscription": null
        }
      },
      "period": {
        "end": 1694467932,
        "start": 1694467932
      },
      "pricing": {
        "price_details": {
          "price": "price_1NpEIa2eZvKYlo2CXcy5DRPA",
          "product": "prod_OcTFTbV7qh48bd"
        },
        "type": "price_details",
        "unit_amount_decimal": "129999"
      },
      "quantity": 1,
      "taxes": []
    }
  ]
}
```