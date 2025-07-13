# Retrieve a credit grant

Retrieves a credit grant.

Returns a credit grant.

- `id` (string, required)
  Unique identifier for the object.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new Stripe.Billing.CreditGrantService();
Stripe.Billing.CreditGrant creditGrant = service.Get(
    "credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BillingCreditGrantParams{};
result, err := creditgrant.Get("credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo", params);
```

```java
Stripe.apiKey = "<<secret key>>";

CreditGrant creditGrant = CreditGrant.retrieve("credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo");
```

```node
const stripe = require('stripe')('<<secret key>>');

const creditGrant = await stripe.billing.creditGrants.retrieve(
  'credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

credit_grant = stripe.billing.CreditGrant.retrieve("credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$creditGrant = $stripe->billing->creditGrants->retrieve(
  'credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo',
  []
);
```

```ruby
Stripe.api_key = '<<secret key>>'

credit_grant = Stripe::Billing::CreditGrant.retrieve('credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo')
```

### Response

```json
{
  "id": "credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo",
  "object": "billing.credit_grant",
  "amount": {
    "monetary": {
      "currency": "usd",
      "value": 1000
    },
    "type": "monetary"
  },
  "applicability_config": {
    "scope": {
      "price_type": "metered"
    }
  },
  "category": "paid",
  "created": 1726620803,
  "customer": "cus_QrvQguzkIK8zTj",
  "effective_at": 1729297860,
  "expires_at": null,
  "livemode": false,
  "metadata": {},
  "name": "Purchased Credits",
  "priority": 50,
  "test_clock": null,
  "updated": 1726620803
}
```