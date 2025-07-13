# Void a credit grant

Voids a credit grant.

Returns the voided credit grant.

- `id` (string, required)
  Unique identifier for the object.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new Stripe.Billing.CreditGrantService();
Stripe.Billing.CreditGrant creditGrant = service.VoidGrant(
    "credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BillingCreditGrantVoidGrantParams{};
result, err := creditgrant.VoidGrant("credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae", params);
```

```java
Stripe.apiKey = "<<secret key>>";

CreditGrant resource = CreditGrant.retrieve("credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae");

CreditGrantVoidGrantParams params = CreditGrantVoidGrantParams.builder().build();

CreditGrant creditGrant = resource.voidGrant(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const creditGrant = await stripe.billing.creditGrants.voidGrant(
  'credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

credit_grant = stripe.billing.CreditGrant.void_grant("credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$creditGrant = $stripe->billing->creditGrants->voidGrant(
  'credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae',
  []
);
```

```ruby
Stripe.api_key = '<<secret key>>'

credit_grant = Stripe::Billing::CreditGrant.void_grant('credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae')
```

### Response

```json
{
  "id": "credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae",
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
  "created": 1726688817,
  "customer": "cus_QsEHa3GKweMwih",
  "effective_at": 1726688817,
  "expires_at": null,
  "livemode": false,
  "metadata": {},
  "name": "Purchased Credits",
  "priority": 50,
  "test_clock": null,
  "updated": 1726688829,
  "voided_at": 1726688829
}
```