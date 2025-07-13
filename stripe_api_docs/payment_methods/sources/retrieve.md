# Retrieve a source

Retrieves an existing source object. Supply the unique source ID from a source creation request and Stripe will return the corresponding up-to-date source object information.

Returns a source if a valid identifier was provided.

- `client_secret` (string, optional)
  The client secret of the source. Required if a publishable key is used to retrieve the source.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new SourceService();
Source source = service.Get("src_1N3lxdLkdIwHu7ixPHXy8UcI");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.SourceParams{};
result, err := source.Get("src_1N3lxdLkdIwHu7ixPHXy8UcI", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Source source = Source.retrieve("src_1N3lxdLkdIwHu7ixPHXy8UcI");
```

```node
const stripe = require('stripe')('<<secret key>>');

const source = await stripe.sources.retrieve('src_1N3lxdLkdIwHu7ixPHXy8UcI');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

source = stripe.Source.retrieve("src_1N3lxdLkdIwHu7ixPHXy8UcI")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$source = $stripe->sources->retrieve('src_1N3lxdLkdIwHu7ixPHXy8UcI', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

source = Stripe::Source.retrieve('src_1N3lxdLkdIwHu7ixPHXy8UcI')
```

### Response

```json
{
  "id": "src_1N3lxdLkdIwHu7ixPHXy8UcI",
  "object": "source",
  "ach_credit_transfer": {
    "account_number": "test_eb829353ed79",
    "bank_name": "TEST BANK",
    "fingerprint": "kBQsBk9KtfCgjEYK",
    "refund_account_holder_name": null,
    "refund_account_holder_type": null,
    "refund_routing_number": null,
    "routing_number": "110000000",
    "swift_code": "TSTEZ122"
  },
  "amount": null,
  "client_secret": "src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr",
  "created": 1683144457,
  "currency": "usd",
  "flow": "receiver",
  "livemode": false,
  "metadata": {},
  "owner": {
    "address": null,
    "email": "jenny.rosen@example.com",
    "name": null,
    "phone": null,
    "verified_address": null,
    "verified_email": null,
    "verified_name": null,
    "verified_phone": null
  },
  "receiver": {
    "address": "110000000-test_eb829353ed79",
    "amount_charged": 0,
    "amount_received": 0,
    "amount_returned": 0,
    "refund_attributes_method": "email",
    "refund_attributes_status": "missing"
  },
  "statement_descriptor": null,
  "status": "pending",
  "type": "ach_credit_transfer",
  "usage": "reusable"
}
```