# Retrieve a quote

Retrieves the quote with the given ID.

Returns a quote if a valid quote ID was provided. Raises [an error](#errors) otherwise.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new QuoteService();
Quote quote = service.Get("qt_1Mr7wVLkdIwHu7ixJYSiPTGq");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.QuoteParams{};
result, err := quote.Get("qt_1Mr7wVLkdIwHu7ixJYSiPTGq", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Quote quote = Quote.retrieve("qt_1Mr7wVLkdIwHu7ixJYSiPTGq");
```

```node
const stripe = require('stripe')('<<secret key>>');

const quote = await stripe.quotes.retrieve('qt_1Mr7wVLkdIwHu7ixJYSiPTGq');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

quote = stripe.Quote.retrieve("qt_1Mr7wVLkdIwHu7ixJYSiPTGq")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$quote = $stripe->quotes->retrieve('qt_1Mr7wVLkdIwHu7ixJYSiPTGq', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

quote = Stripe::Quote.retrieve('qt_1Mr7wVLkdIwHu7ixJYSiPTGq')
```

### Response

```json
{
  "id": "qt_1Mr7wVLkdIwHu7ixJYSiPTGq",
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
  "created": 1680130691,
  "currency": "usd",
  "customer": "cus_NcMfB0SSFHINCV",
  "default_tax_rates": [],
  "description": null,
  "discounts": [],
  "expires_at": 1682722691,
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
  "number": null,
  "on_behalf_of": null,
  "status": "draft",
  "status_transitions": {
    "accepted_at": null,
    "canceled_at": null,
    "finalized_at": null
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
```