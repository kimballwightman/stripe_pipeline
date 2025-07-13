# List all credit notes

Returns a list of credit notes.

A dictionary with a `data` property that contains an array of up to `limit` credit notes, starting after credit note `starting_after`. Each entry in the array is a separate credit note object. If no more credit notes are available, the resulting array will be empty.

- `created` (object, optional)
  Only return credit notes that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `customer` (string, optional)
  Only return credit notes for the customer specified by this customer ID.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `invoice` (string, optional)
  Only return credit notes for the invoice specified by this invoice ID.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CreditNoteListOptions { Limit = 3 };
var service = new CreditNoteService();
StripeList<CreditNote> creditNotes = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CreditNoteListParams{};
params.Limit = stripe.Int64(3)
result := creditnote.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

CreditNoteListParams params = CreditNoteListParams.builder().setLimit(3L).build();

CreditNoteCollection creditNotes = CreditNote.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const creditNotes = await stripe.creditNotes.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

credit_notes = stripe.CreditNote.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$creditNotes = $stripe->creditNotes->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

credit_notes = Stripe::CreditNote.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/credit_notes",
  "has_more": false,
  "data": [
    {
      "id": "cn_1MxvRqLkdIwHu7ixY0xbUcxk",
      "object": "credit_note",
      "amount": 1099,
      "amount_shipping": 0,
      "created": 1681750958,
      "currency": "usd",
      "customer": "cus_NjLgPhUokHubJC",
      "customer_balance_transaction": null,
      "discount_amount": 0,
      "discount_amounts": [],
      "invoice": "in_1MxvRkLkdIwHu7ixABNtI99m",
      "lines": {
        "object": "list",
        "data": [
          {
            "id": "cnli_1MxvRqLkdIwHu7ixFpdhBFQf",
            "object": "credit_note_line_item",
            "amount": 1099,
            "description": "T-shirt",
            "discount_amount": 0,
            "discount_amounts": [],
            "invoice_line_item": "il_1MxvRlLkdIwHu7ixnkbntxUV",
            "livemode": false,
            "quantity": 1,
            "tax_rates": [],
            "taxes": [],
            "type": "invoice_line_item",
            "unit_amount": 1099,
            "unit_amount_decimal": "1099"
          }
        ],
        "has_more": false,
        "url": "/v1/credit_notes/cn_1MxvRqLkdIwHu7ixY0xbUcxk/lines"
      },
      "livemode": false,
      "memo": null,
      "metadata": {},
      "number": "C9E0C52C-0036-CN-01",
      "out_of_band_amount": null,
      "pdf": "https://pay.stripe.com/credit_notes/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9Oak9FOUtQNFlPdk52UXhFd2Z4SU45alpEd21kd0Y4LDcyMjkxNzU50200cROQsSK2/pdf?s=ap",
      "pre_payment_amount": 1099,
      "post_payment_amount": 0,
      "reason": null,
      "refunds": [],
      "shipping_cost": null,
      "status": "issued",
      "subtotal": 1099,
      "subtotal_excluding_tax": 1099,
      "total": 1099,
      "total_excluding_tax": 1099,
      "total_taxes": [],
      "type": "pre_payment",
      "voided_at": null
    }
  ]
}
```