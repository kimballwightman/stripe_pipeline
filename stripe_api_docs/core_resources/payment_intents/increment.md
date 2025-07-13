# Increment an authorization

Perform an incremental authorization on an eligible
[PaymentIntent](https://docs.stripe.com/docs/api/payment_intents/object.md). To be eligible, the
PaymentIntent’s status must be `requires_capture` and
[incremental_authorization_supported](https://docs.stripe.com/docs/api/charges/object.md#charge_object-payment_method_details-card_present-incremental_authorization_supported)
must be `true`.

Incremental authorizations attempt to increase the authorized amount on
your customer’s card to the new, higher `amount` provided. Similar to the
initial authorization, incremental authorizations can be declined. A
single PaymentIntent can call this endpoint multiple times to further
increase the authorized amount.

If the incremental authorization succeeds, the PaymentIntent object
returns with the updated
[amount](https://docs.stripe.com/docs/api/payment_intents/object.md#payment_intent_object-amount).
If the incremental authorization fails, a
[card_declined](https://docs.stripe.com/docs/error-codes.md#card-declined) error returns, and no other
fields on the PaymentIntent or Charge update. The PaymentIntent
object remains capturable for the previously authorized amount.

Each PaymentIntent can have a maximum of 10 incremental authorization attempts, including declines.
After it’s captured, a PaymentIntent can no longer be incremented.

Learn more about [incremental authorizations](https://docs.stripe.com/docs/terminal/features/incremental-authorizations.md).

Returns a PaymentIntent object with the updated amount if the incremental authorization succeeds. Returns an error if the incremental authorization failed or the PaymentIntent isn’t eligible for incremental authorizations.

- `amount` (integer, required)
  The updated total amount that you intend to collect from the cardholder. This amount must be greater than the currently authorized amount.

- `application_fee_amount` (integer, optional)
  The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner’s Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://docs.stripe.com/docs/payments/connected-accounts.md).

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `statement_descriptor` (string, optional)
  Text that appears on the customer’s statement as the statement descriptor for a non-card or card charge. This value overrides the account’s default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).

- `transfer_data` (object, optional)
  The parameters used to automatically create a transfer after the payment is captured.
  Learn more about the [use case for connected accounts](https://docs.stripe.com/docs/payments/connected-accounts.md).

  - `transfer_data.amount` (integer, optional)
    The amount that will be transferred automatically when a charge succeeds.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new PaymentIntentIncrementAuthorizationOptions { Amount = 2099 };
var service = new PaymentIntentService();
PaymentIntent paymentIntent = service.IncrementAuthorization(
    "pi_1DtBRR2eZvKYlo2CmCVxxvd7",
    options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentIntentIncrementAuthorizationParams{Amount: stripe.Int64(2099)};
result, err := paymentintent.IncrementAuthorization("pi_1DtBRR2eZvKYlo2CmCVxxvd7", params);
```

```java
Stripe.apiKey = "<<secret key>>";

PaymentIntent resource = PaymentIntent.retrieve("pi_1DtBRR2eZvKYlo2CmCVxxvd7");

PaymentIntentIncrementAuthorizationParams params =
  PaymentIntentIncrementAuthorizationParams.builder().setAmount(2099L).build();

PaymentIntent paymentIntent = resource.incrementAuthorization(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const paymentIntent = await stripe.paymentIntents.incrementAuthorization(
  'pi_1DtBRR2eZvKYlo2CmCVxxvd7',
  {
    amount: 2099,
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_intent = stripe.PaymentIntent.increment_authorization(
  "pi_1DtBRR2eZvKYlo2CmCVxxvd7",
  amount=2099,
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentIntent = $stripe->paymentIntents->incrementAuthorization(
  'pi_1DtBRR2eZvKYlo2CmCVxxvd7',
  ['amount' => 2099]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_intent = Stripe::PaymentIntent.increment_authorization(
  'pi_1DtBRR2eZvKYlo2CmCVxxvd7',
  {amount: 2099},
)
```

### Response

```json
{
  "id": "pi_1DtBRR2eZvKYlo2CmCVxxvd7",
  "object": "payment_intent",
  "amount": 2099,
  "amount_capturable": 2099,
  "amount_details": {
    "tip": {}
  },
  "amount_received": 0,
  "application": null,
  "application_fee_amount": null,
  "automatic_payment_methods": null,
  "canceled_at": null,
  "cancellation_reason": null,
  "capture_method": "manual",
  "client_secret": "pi_1DtBRR2eZvKYlo2CmCVxxvd7_secret_cWsUkvyTOjhLKh5Wxu61nYc0i",
  "confirmation_method": "automatic",
  "created": 1680196960,
  "currency": "usd",
  "customer": null,
  "description": null,
  "last_payment_error": null,
  "latest_charge": "ch_3MrPBM2eZvKYlo2C1CEBUD4A",
  "livemode": false,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": "pm_1MrPBL2eZvKYlo2CaNa8L11Z",
  "payment_method_options": {
    "card": {
      "installments": null,
      "mandate_options": null,
      "network": null,
      "request_three_d_secure": "automatic"
    }
  },
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
  "status": "requires_capture",
  "transfer_data": null,
  "transfer_group": null
}
```