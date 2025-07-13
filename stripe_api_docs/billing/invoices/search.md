# Search invoices

Search for invoices you’ve previously created using Stripe’s [Search Query Language](https://docs.stripe.com/docs/search.md#search-query-language).
Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
to an hour behind during outages. Search functionality is not available to merchants in India.

A dictionary with a `data` property that contains an array of up to `limit` invoices. If no objects match the
query, the resulting array will be empty. See the related guide on [expanding properties in lists](https://docs.stripe.com/docs/expand.md#lists).

- `query` (string, required)
  The search query string. See [search query language](https://docs.stripe.com/docs/search.md#search-query-language) and the list of supported [query fields for invoices](https://docs.stripe.com/docs/search.md#query-fields-for-invoices).

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `page` (string, optional)
  A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new InvoiceSearchOptions { Query = "total<1" };
var service = new InvoiceService();
StripeSearchResult<Invoice> invoices = service.Search(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.InvoiceSearchParams{SearchParams: stripe.SearchParams{Query: "total<1"}};
result := invoice.Search(params);
```

```java
Stripe.apiKey = "<<secret key>>";

InvoiceSearchParams params = InvoiceSearchParams.builder().setQuery("total<1").build();

InvoiceSearchResult invoices = Invoice.search(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const invoices = await stripe.invoices.search({
  query: 'total<1',
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

invoices = stripe.Invoice.search(query="total<1")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$invoices = $stripe->invoices->search(['query' => 'total<1']);
```

```ruby
Stripe.api_key = '<<secret key>>'

invoices = Stripe::Invoice.search({query: 'total<1'})
```

### Response

```json
{
  "object": "search_result",
  "url": "/v1/invoices/search",
  "has_more": false,
  "data": [
    {
      "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",
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
        "url": "/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"
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
      "receipt_number": null,
      "shipping_cost": null,
      "shipping_details": null,
      "starting_balance": 0,
      "statement_descriptor": null,
      "status": "draft",
      "status_transitions": {
        "finalized_at": null,
        "marked_uncollectible_at": null,
        "paid_at": null,
        "voided_at": null
      },
      "subtotal": 0,
      "subtotal_excluding_tax": 0,
      "test_clock": null,
      "total": 0,
      "total_discount_amounts": [],
      "total_excluding_tax": 0,
      "total_taxes": [],
      "webhooks_delivered_at": 1680644467
    }
  ]
}
```