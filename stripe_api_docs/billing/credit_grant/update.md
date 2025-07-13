# Update a credit grant

Updates a credit grant.

Returns the updated credit grant.

- `id` (string, required)
  Unique identifier for the object.

- `expires_at` (timestamp, optional)
  The time when the billing credits created by this credit grant expire. If set to empty, the billing credits never expire.

- `metadata` (object, optional)
  Set of key-value pairs you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new Stripe.Billing.CreditGrantUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "cost_basis", "0.9" } },
    ExpiresAt = DateTimeOffset.FromUnixTimeSeconds(1759302000).UtcDateTime,
};
var service = new Stripe.Billing.CreditGrantService();
Stripe.Billing.CreditGrant creditGrant = service.Update(
    "credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa",
    options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BillingCreditGrantParams{ExpiresAt: stripe.Int64(1759302000)};
params.AddMetadata("cost_basis", "0.9")
result, err := creditgrant.Update("credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa", params);
```

```java
Stripe.apiKey = "<<secret key>>";

CreditGrant resource = CreditGrant.retrieve("credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa");

CreditGrantUpdateParams params =
  CreditGrantUpdateParams.builder()
    .putMetadata("cost_basis", "0.9")
    .setExpiresAt(1759302000L)
    .build();

CreditGrant creditGrant = resource.update(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const creditGrant = await stripe.billing.creditGrants.update(
  'credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa',
  {
    metadata: {
      cost_basis: '0.9',
    },
    expires_at: 1759302000,
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

credit_grant = stripe.billing.CreditGrant.modify(
  "credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa",
  metadata={"cost_basis": "0.9"},
  expires_at=1759302000,
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$creditGrant = $stripe->billing->creditGrants->update(
  'credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa',
  [
    'metadata' => ['cost_basis' => '0.9'],
    'expires_at' => 1759302000,
  ]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

credit_grant = Stripe::Billing::CreditGrant.update(
  'credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa',
  {
    metadata: {cost_basis: '0.9'},
    expires_at: 1759302000,
  },
)
```

### Response

```json
{
  "id": "credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa",
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
  "created": 1726688933,
  "customer": "cus_QsEHa3GKweMwih",
  "effective_at": 1726688933,
  "expires_at": 1759302000,
  "livemode": false,
  "metadata": {
    "cost_basis": "0.9"
  },
  "name": "Purchased Credits",
  "priority": 50,
  "test_clock": null,
  "updated": 1726688977,
  "voided_at": null
}
```