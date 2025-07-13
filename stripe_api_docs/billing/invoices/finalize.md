# Finalize an invoice

Stripe automatically finalizes drafts before sending and attempting payment on invoices. However, if you’d like to finalize a draft invoice manually, you can do so using this method.

Returns an invoice object with `status=open`.

- `auto_advance` (boolean, optional)
  Controls whether Stripe performs [automatic collection](https://docs.stripe.com/docs/invoicing/integration/automatic-advancement-collection.md) of the invoice. If `false`, the invoice’s state doesn’t automatically advance without an explicit action.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new InvoiceService();
Invoice invoice = service.FinalizeInvoice("in_1MtGmCLkdIwHu7ix6PgS6g8S");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.InvoiceFinalizeInvoiceParams{};
result, err := invoice.FinalizeInvoice("in_1MtGmCLkdIwHu7ix6PgS6g8S", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Invoice resource = Invoice.retrieve("in_1MtGmCLkdIwHu7ix6PgS6g8S");

InvoiceFinalizeInvoiceParams params = InvoiceFinalizeInvoiceParams.builder().build();

Invoice invoice = resource.finalizeInvoice(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const invoice = await stripe.invoices.finalizeInvoice('in_1MtGmCLkdIwHu7ix6PgS6g8S');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

invoice = stripe.Invoice.finalize_invoice("in_1MtGmCLkdIwHu7ix6PgS6g8S")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$invoice = $stripe->invoices->finalizeInvoice('in_1MtGmCLkdIwHu7ix6PgS6g8S', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

invoice = Stripe::Invoice.finalize_invoice('in_1MtGmCLkdIwHu7ix6PgS6g8S')
```

### Response

```json
{
  "id": "in_1MtGmCLkdIwHu7ix6PgS6g8S",
  "object": "invoice",
  "account_country": "US",
  "account_name": "Stripe Docs",
  "account_tax_ids": null,
  "amount_due": 0,
  "amount_paid": 0,
  "amount_overpaid": 0,
  "amount_remaining": 0,
  "amount_shipping": 0,
  "application": null,
  "attempt_count": 0,
  "attempted": true,
  "auto_advance": false,
  "automatic_tax": {
    "enabled": false,
    "liability": null,
    "status": null
  },
  "billing_reason": "manual",
  "collection_method": "send_invoice",
  "created": 1680641304,
  "currency": "usd",
  "custom_fields": null,
  "customer": "cus_NeZw0zvTyquTfF",
  "customer_address": null,
  "customer_email": "jennyrosen@example.com",
  "customer_name": "Jenny Rosen",
  "customer_phone": null,
  "customer_shipping": null,
  "customer_tax_exempt": "none",
  "customer_tax_ids": [],
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discounts": [],
  "due_date": 1681246104,
  "ending_balance": 0,
  "footer": null,
  "from_invoice": null,
  "hosted_invoice_url": "https://invoice.stripe.com/i/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9OZVp3dVBYNnF0dGlvdXRubGVjSXVOOWhiVWpmUktPLDcxMTgyMTA10200x7P2wMSm?s=ap",
  "invoice_pdf": "https://pay.stripe.com/invoice/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9OZVp3dVBYNnF0dGlvdXRubGVjSXVOOWhiVWpmUktPLDcxMTgyMTA10200x7P2wMSm/pdf?s=ap",
  "issuer": {
    "type": "self"
  },
  "last_finalization_error": null,
  "latest_revision": null,
  "lines": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/invoices/in_1MtGmCLkdIwHu7ix6PgS6g8S/lines"
  },
  "livemode": false,
  "metadata": {},
  "next_payment_attempt": null,
  "number": "9545A614-0001",
  "on_behalf_of": null,
  "parent": null,
  "payment_settings": {
    "default_mandate": null,
    "payment_method_options": null,
    "payment_method_types": null
  },
  "period_end": 1680641304,
  "period_start": 1680641304,
  "post_payment_credit_notes_amount": 0,
  "pre_payment_credit_notes_amount": 0,
  "receipt_number": null,
  "shipping_cost": null,
  "shipping_details": null,
  "starting_balance": 0,
  "statement_descriptor": null,
  "status": "paid",
  "status_transitions": {
    "finalized_at": 1680641304,
    "marked_uncollectible_at": null,
    "paid_at": 1680641304,
    "voided_at": null
  },
  "subtotal": 0,
  "subtotal_excluding_tax": 0,
  "test_clock": null,
  "total": 0,
  "total_discount_amounts": [],
  "total_excluding_tax": 0,
  "total_taxes": [],
  "webhooks_delivered_at": 1680641304
}
```