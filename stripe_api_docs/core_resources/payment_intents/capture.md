# Capture a PaymentIntent

Capture the funds of an existing uncaptured PaymentIntent when its status is `requires_capture`.

Uncaptured PaymentIntents are cancelled a set number of days (7 by default) after their creation.

Learn more about [separate authorization and capture](https://docs.stripe.com/docs/payments/capture-later.md).

Returns a PaymentIntent object with `status="succeeded"` if the PaymentIntent is capturable. Returns an error if the PaymentIntent isn’t capturable or if an invalid amount to capture is provided.

- `amount_to_capture` (integer, optional)
  The amount to capture from the PaymentIntent, which must be less than or equal to the original amount. Defaults to the full `amount_capturable` if it’s not provided.

- `application_fee_amount` (integer, optional)
  The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner’s Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://docs.stripe.com/docs/payments/connected-accounts.md).

- `final_capture` (boolean, optional)
  Defaults to `true`. When capturing a PaymentIntent, setting `final_capture` to `false` notifies Stripe to not release the remaining uncaptured funds to make sure that they’re captured in future requests. You can only use this setting when [multicapture](https://docs.stripe.com/docs/payments/multicapture.md) is available for PaymentIntents.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `statement_descriptor` (string, optional)
  Text that appears on the customer’s statement as the statement descriptor for a non-card charge. This value overrides the account’s default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).

  Setting this value for a card charge returns an error. For card charges, set the [statement_descriptor_suffix](https://docs.stripe.com/get-started/account/statement-descriptors#dynamic) instead.

- `statement_descriptor_suffix` (string, optional)
  Provides information about a card charge. Concatenated to the account’s [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer’s statement.

- `transfer_data` (object, optional)
  The parameters that you can use to automatically create a transfer after the payment
  is captured. Learn more about the [use case for connected accounts](https://docs.stripe.com/docs/payments/connected-accounts.md).

  - `transfer_data.amount` (integer, optional)
    The amount that will be transferred automatically when a charge succeeds.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new PaymentIntentService();
PaymentIntent paymentIntent = service.Capture("pi_3MrPBM2eZvKYlo2C1TEMacFD");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentIntentCaptureParams{};
result, err := paymentintent.Capture("pi_3MrPBM2eZvKYlo2C1TEMacFD", params);
```

```java
Stripe.apiKey = "<<secret key>>";

PaymentIntent resource = PaymentIntent.retrieve("pi_3MrPBM2eZvKYlo2C1TEMacFD");

PaymentIntentCaptureParams params = PaymentIntentCaptureParams.builder().build();

PaymentIntent paymentIntent = resource.capture(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const paymentIntent = await stripe.paymentIntents.capture('pi_3MrPBM2eZvKYlo2C1TEMacFD');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_intent = stripe.PaymentIntent.capture("pi_3MrPBM2eZvKYlo2C1TEMacFD")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentIntent = $stripe->paymentIntents->capture('pi_3MrPBM2eZvKYlo2C1TEMacFD', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_intent = Stripe::PaymentIntent.capture('pi_3MrPBM2eZvKYlo2C1TEMacFD')
```

### Response

```json
{
  "id": "pi_3MrPBM2eZvKYlo2C1TEMacFD",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 0,
  "amount_details": {
    "tip": {}
  },
  "amount_received": 1000,
  "application": null,
  "application_fee_amount": null,
  "automatic_payment_methods": null,
  "canceled_at": null,
  "cancellation_reason": null,
  "capture_method": "automatic",
  "client_secret": "pi_3MrPBM2eZvKYlo2C1TEMacFD_secret_9J35eTzWlxVmfbbQhmkNbewuL",
  "confirmation_method": "automatic",
  "created": 1524505326,
  "currency": "usd",
  "customer": null,
  "description": "One blue fish",
  "last_payment_error": null,
  "latest_charge": "ch_1EXUPv2eZvKYlo2CStIqOmbY",
  "livemode": false,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": "pm_1EXUPv2eZvKYlo2CUkqZASBe",
  "payment_method_options": {},
  "payment_method_types": [
    "card"
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