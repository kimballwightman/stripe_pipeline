# Retrieve a credit note's line items

When retrieving a credit note, you’ll get a **lines** property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

Returns a list of [line_item objects](#credit_note_line_item_object).

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

### Response

```json
{
  "object": "list",
  "url": "/v1/credit_notes/cn_1NPtPy2eZvKYlo2CPaEMGMY8/lines",
  "has_more": false,
  "data": [
    {
      "object": "list",
      "url": "/v1/credit_notes/cn_1Nn7fB2eZvKYlo2CuJ0wZBlA/lines",
      "has_more": false,
      "data": [
        {
          "id": "cnli_1Nn7fB2eZvKYlo2COYgPG88j",
          "object": "credit_note_line_item",
          "amount": 799,
          "description": "My First Invoice Item (created for API docs)",
          "discount_amount": 0,
          "discount_amounts": [],
          "invoice_line_item": "il_1Nn7fB2eZvKYlo2C3GKZP9wi",
          "livemode": false,
          "quantity": 1,
          "tax_rates": [],
          "taxes": [],
          "type": "invoice_line_item",
          "unit_amount": null,
          "unit_amount_decimal": null
        }
      ]
    }
  ]
}
```