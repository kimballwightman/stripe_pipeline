# Update a credit note

Updates an existing credit note.

Returns the updated credit note object if the call succeeded.

- `memo` (string, optional)
  Credit note memo.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CreditNoteUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var service = new CreditNoteService();
CreditNote creditNote = service.Update("cn_1MxvRqLkdIwHu7ixY0xbUcxk", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CreditNoteParams{};
params.AddMetadata("order_id", "6735")
result, err := creditnote.Update("cn_1MxvRqLkdIwHu7ixY0xbUcxk", params);
```

```java
Stripe.apiKey = "<<secret key>>";

CreditNote resource = CreditNote.retrieve("cn_1MxvRqLkdIwHu7ixY0xbUcxk");

CreditNoteUpdateParams params =
  CreditNoteUpdateParams.builder().putMetadata("order_id", "6735").build();

CreditNote creditNote = resource.update(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const creditNote = await stripe.creditNotes.update(
  'cn_1MxvRqLkdIwHu7ixY0xbUcxk',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

credit_note = stripe.CreditNote.modify(
  "cn_1MxvRqLkdIwHu7ixY0xbUcxk",
  metadata={"order_id": "6735"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$creditNote = $stripe->creditNotes->update(
  'cn_1MxvRqLkdIwHu7ixY0xbUcxk',
  ['metadata' => ['order_id' => '6735']]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

credit_note = Stripe::CreditNote.update(
  'cn_1MxvRqLkdIwHu7ixY0xbUcxk',
  {metadata: {order_id: '6735'}},
)
```

### Response

```json
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
  "metadata": {
    "order_id": "6735"
  },
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
```