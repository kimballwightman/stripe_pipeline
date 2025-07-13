# List all quotes

Returns a list of your quotes.

A dictionary with a `data` property that contains an array of up to `limit` quotes, starting after quote `starting_after`. Each entry in the array is a separate quote object. If no more quotes are available, the resulting array will be empty.

- `customer` (string, optional)
  The ID of the customer whose quotes will be retrieved.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  The status of the quote.

- `test_clock` (string, optional)
  Provides a list of quotes that are associated with the specified test clock. The response will not include quotes with test clocks if this and the customer parameter is not set.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new QuoteListOptions { Limit = 3 };
var service = new QuoteService();
StripeList<Quote> quotes = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.QuoteListParams{};
params.Limit = stripe.Int64(3)
result := quote.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

QuoteListParams params = QuoteListParams.builder().setLimit(3L).build();

QuoteCollection quotes = Quote.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const quotes = await stripe.quotes.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

quotes = stripe.Quote.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$quotes = $stripe->quotes->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

quotes = Stripe::Quote.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/quotes",
  "has_more": false,
  "data": [
    {
      "id": "qt_1Mr7SqLkdIwHu7ixpI1ClZ6z",
      "object": "quote",
      "amount_subtotal": 2198,
      "amount_total": 2198,
      "application": null,
      "application_fee_amount": null,
      "application_fee_percent": null,
      "automatic_tax": {
        "enabled": false,
        "liability": null,
        "status": null
      },
      "collection_method": "charge_automatically",
      "computed": {
        "recurring": null,
        "upfront": {
          "amount_subtotal": 2198,
          "amount_total": 2198,
          "total_details": {
            "amount_discount": 0,
            "amount_shipping": 0,
            "amount_tax": 0
          }
        }
      },
      "created": 1680128852,
      "currency": "usd",
      "customer": "cus_NcMBZUWCIOEgEW",
      "default_tax_rates": [],
      "description": null,
      "discounts": [],
      "expires_at": 1682720852,
      "footer": null,
      "from_quote": null,
      "header": null,
      "invoice": null,
      "invoice_settings": {
        "days_until_due": null,
        "issuer": {
          "type": "self"
        }
      },
      "livemode": false,
      "metadata": {},
      "number": "QT-5B9DA057-0001-1",
      "on_behalf_of": null,
      "status": "open",
      "status_transitions": {
        "accepted_at": null,
        "canceled_at": null,
        "finalized_at": 1680128853
      },
      "subscription": null,
      "subscription_data": {
        "description": null,
        "effective_date": null,
        "trial_period_days": null
      },
      "subscription_schedule": null,
      "test_clock": null,
      "total_details": {
        "amount_discount": 0,
        "amount_shipping": 0,
        "amount_tax": 0
      },
      "transfer_data": null
    }
  ]
}
```