# Verify microdeposits on a SetupIntent

Verifies microdeposits on a SetupIntent object.

Returns a SetupIntent object.

- `amounts` (array of integers, optional)
  Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account.

- `descriptor_code` (string, optional)
  A six-character code starting with SM present in the microdeposit sent to the bank account.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new SetupIntentVerifyMicrodepositsOptions { Amounts = new List<long?> { 32, 45 } };
var service = new SetupIntentService();
SetupIntent setupIntent = service.VerifyMicrodeposits("seti_1Mm5yZLkdIwHu7ixm0sPzrx4", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.SetupIntentVerifyMicrodepositsParams{
  Amounts: []*int64{stripe.Int64(32), stripe.Int64(45)},
};
result, err := setupintent.VerifyMicrodeposits("seti_1Mm5yZLkdIwHu7ixm0sPzrx4", params);
```

```java
Stripe.apiKey = "<<secret key>>";

SetupIntent resource = SetupIntent.retrieve("seti_1Mm5yZLkdIwHu7ixm0sPzrx4");

SetupIntentVerifyMicrodepositsParams params =
  SetupIntentVerifyMicrodepositsParams.builder().addAmount(32L).addAmount(45L).build();

SetupIntent setupIntent = resource.verifyMicrodeposits(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const setupIntent = await stripe.setupIntents.verifyMicrodeposits(
  'seti_1Mm5yZLkdIwHu7ixm0sPzrx4',
  {
    amounts: [32, 45],
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

setup_intent = stripe.SetupIntent.verify_microdeposits(
  "seti_1Mm5yZLkdIwHu7ixm0sPzrx4",
  amounts=[32, 45],
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$setupIntent = $stripe->setupIntents->verifyMicrodeposits(
  'seti_1Mm5yZLkdIwHu7ixm0sPzrx4',
  ['amounts' => [32, 45]]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

setup_intent = Stripe::SetupIntent.verify_microdeposits(
  'seti_1Mm5yZLkdIwHu7ixm0sPzrx4',
  {amounts: [32, 45]},
)
```

### Response

```json
{
  "id": "seti_1Mm5yZLkdIwHu7ixm0sPzrx4",
  "object": "setup_intent",
  "application": null,
  "cancellation_reason": null,
  "client_secret": "seti_1Mm5yZLkdIwHu7ixm0sPzrx4_secret_NXAJ5iPM38ITW1pI7o8VZZhoZyDrrWR",
  "created": 1678931491,
  "customer": null,
  "description": null,
  "flow_directions": null,
  "last_setup_error": null,
  "latest_attempt": "setatt_1Mm5yZLkdIwHu7ix7QtOkLAu",
  "livemode": false,
  "mandate": "mandate_1Mm5yaLkdIwHu7ixmNoLkKLC",
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": "pm_1Mm5yZLkdIwHu7ixf89jW57b",
  "payment_method_options": {
    "acss_debit": {
      "currency": "cad",
      "mandate_options": {
        "interval_description": "First of every month",
        "payment_schedule": "interval",
        "transaction_type": "personal"
      },
      "verification_method": "automatic"
    }
  },
  "payment_method_types": [
    "acss_debit"
  ],
  "single_use_mandate": null,
  "status": "succeeded",
  "usage": "off_session"
}
```