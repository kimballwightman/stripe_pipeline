# Expire a credit grant

Expires a credit grant.

Returns the expired credit grant.

- `id` (string, required)
  Unique identifier for the object.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new Stripe.Billing.CreditGrantService();
Stripe.Billing.CreditGrant creditGrant = service.Expire(
    "credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BillingCreditGrantExpireParams{};
result, err := creditgrant.Expire("credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim", params);
```

```java
Stripe.apiKey = "<<secret key>>";

CreditGrant resource = CreditGrant.retrieve("credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim");

CreditGrantExpireParams params = CreditGrantExpireParams.builder().build();

CreditGrant creditGrant = resource.expire(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const creditGrant = await stripe.billing.creditGrants.expire(
  'credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

credit_grant = stripe.billing.CreditGrant.expire("credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$creditGrant = $stripe->billing->creditGrants->expire(
  'credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim',
  []
);
```

```ruby
Stripe.api_key = '<<secret key>>'

credit_grant = Stripe::Billing::CreditGrant.expire('credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim')
```

### Response

```json
{
  "id": "credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim",
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
  "created": 1726688741,
  "customer": "cus_QsEHa3GKweMwih",
  "effective_at": 1726688741,
  "expires_at": 1726688796,
  "livemode": false,
  "metadata": {},
  "name": "Purchased Credits",
  "priority": 50,
  "test_clock": null,
  "updated": 1726688796,
  "voided_at": null
}
```