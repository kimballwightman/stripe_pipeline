# Void an invoice

Mark a finalized invoice as void. This cannot be undone. Voiding an invoice is similar to [deletion](#delete_invoice), however it only applies to finalized invoices and maintains a papertrail where the invoice can still be found.

Consult with local regulations to determine whether and how an invoice might be amended, canceled, or voided in the jurisdiction you’re doing business in. You might need to [issue another invoice](#create_invoice) or [credit note](#create_credit_note) instead. Stripe recommends that you consult with your legal counsel for advice specific to your business.

Returns the voided invoice object.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new InvoiceService();
Invoice invoice = service.VoidInvoice("in_1MtGmCLkdIwHu7ix6PgS6g8S");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.InvoiceVoidInvoiceParams{};
result, err := invoice.VoidInvoice("in_1MtGmCLkdIwHu7ix6PgS6g8S", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Invoice resource = Invoice.retrieve("in_1MtGmCLkdIwHu7ix6PgS6g8S");

InvoiceVoidInvoiceParams params = InvoiceVoidInvoiceParams.builder().build();

Invoice invoice = resource.voidInvoice(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const invoice = await stripe.invoices.voidInvoice('in_1MtGmCLkdIwHu7ix6PgS6g8S');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

invoice = stripe.Invoice.void_invoice("in_1MtGmCLkdIwHu7ix6PgS6g8S")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$invoice = $stripe->invoices->voidInvoice('in_1MtGmCLkdIwHu7ix6PgS6g8S', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

invoice = Stripe::Invoice.void_invoice('in_1MtGmCLkdIwHu7ix6PgS6g8S')
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
  "attempted": false,
  "auto_advance": false,
  "automatic_tax": {
    "enabled": false,
    "liability": null,
    "status": null
  },
  "billing_reason": "manual",
  "collection_method": "charge_automatically",
  "created": 1680644467,
  "currency": "usd",
  "custom_fields": null,
  "customer": "cus_NeZwdNtLEOXuvB",
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
  "due_date": null,
  "ending_balance": null,
  "footer": null,
  "from_invoice": null,
  "hosted_invoice_url": null,
  "invoice_pdf": null,
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
  "number": null,
  "on_behalf_of": null,
  "parent": null,
  "payment_settings": {
    "default_mandate": null,
    "payment_method_options": null,
    "payment_method_types": null
  },
  "period_end": 1680644467,
  "period_start": 1680644467,
  "post_payment_credit_notes_amount": 0,
  "pre_payment_credit_notes_amount": 0,
  "quote": null,
  "receipt_number": null,
  "shipping_cost": null,
  "shipping_details": null,
  "starting_balance": 0,
  "statement_descriptor": null,
  "status": "void",
  "status_transitions": {
    "finalized_at": null,
    "marked_uncollectible_at": null,
    "paid_at": null,
    "voided_at": null
  },
  "subscription": null,
  "subtotal": 0,
  "subtotal_excluding_tax": 0,
  "test_clock": null,
  "total": 0,
  "total_discount_amounts": [],
  "total_excluding_tax": 0,
  "total_taxes": [],
  "webhooks_delivered_at": 1680644467
}
```