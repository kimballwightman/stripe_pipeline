# Verify microdeposits on a PaymentIntent

Verifies microdeposits on a PaymentIntent object.

Returns a PaymentIntent object.

- `amounts` (array of integers, optional)
  Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account.

- `descriptor_code` (string, optional)
  A six-character code starting with SM present in the microdeposit sent to the bank account.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new PaymentIntentVerifyMicrodepositsOptions { Amounts = new List<long?> { 32, 45 } };
var service = new PaymentIntentService();
PaymentIntent paymentIntent = service.VerifyMicrodeposits("pi_1DtBRR2eZvKYlo2CmCVxxvd7", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentIntentVerifyMicrodepositsParams{
  Amounts: []*int64{stripe.Int64(32), stripe.Int64(45)},
};
result, err := paymentintent.VerifyMicrodeposits("pi_1DtBRR2eZvKYlo2CmCVxxvd7", params);
```

```java
Stripe.apiKey = "<<secret key>>";

PaymentIntent resource = PaymentIntent.retrieve("pi_1DtBRR2eZvKYlo2CmCVxxvd7");

PaymentIntentVerifyMicrodepositsParams params =
  PaymentIntentVerifyMicrodepositsParams.builder().addAmount(32L).addAmount(45L).build();

PaymentIntent paymentIntent = resource.verifyMicrodeposits(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const paymentIntent = await stripe.paymentIntents.verifyMicrodeposits(
  'pi_1DtBRR2eZvKYlo2CmCVxxvd7',
  {
    amounts: [32, 45],
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_intent = stripe.PaymentIntent.verify_microdeposits(
  "pi_1DtBRR2eZvKYlo2CmCVxxvd7",
  amounts=[32, 45],
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentIntent = $stripe->paymentIntents->verifyMicrodeposits(
  'pi_1DtBRR2eZvKYlo2CmCVxxvd7',
  ['amounts' => [32, 45]]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_intent = Stripe::PaymentIntent.verify_microdeposits(
  'pi_1DtBRR2eZvKYlo2CmCVxxvd7',
  {amounts: [32, 45]},
)
```

### Response

```json
{
  "id": "pi_1DtBRR2eZvKYlo2CmCVxxvd7",
  "object": "payment_intent",
  "amount": 1099,
  "amount_capturable": 0,
  "amount_details": {
    "tip": {}
  },
  "amount_received": 0,
  "application": null,
  "application_fee_amount": null,
  "automatic_payment_methods": null,
  "canceled_at": null,
  "cancellation_reason": null,
  "capture_method": "automatic",
  "client_secret": "pi_1DtBRR2eZvKYlo2CmCVxxvd7_secret_l80vlOGz9kZQwnzocExJQUsJx",
  "confirmation_method": "automatic",
  "created": 1680800210,
  "currency": "usd",
  "customer": null,
  "description": null,
  "last_payment_error": null,
  "latest_charge": null,
  "livemode": false,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": "pm_1Mtw7C2eZvKYlo2CPsW0F8g0",
  "payment_method_options": {
    "acss_debit": {
      "mandate_options": {
        "interval_description": "First day of every month",
        "payment_schedule": "interval",
        "transaction_type": "personal"
      },
      "verification_method": "automatic"
    }
  },
  "payment_method_types": [
    "acss_debit"
  ],
  "processing": null,
  "receipt_email": null,
  "redaction": null,
  "review": null,
  "setup_future_usage": null,
  "shipping": null,
  "statement_descriptor": null,
  "statement_descriptor_suffix": null,
  "status": "succeeded",
  "transfer_data": null,
  "transfer_group": null
}
```