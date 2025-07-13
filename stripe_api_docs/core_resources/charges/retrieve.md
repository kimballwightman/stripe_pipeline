# Retrieve a charge

Retrieves the details of a charge that has previously been created. Supply the unique charge ID that was returned from your previous request, and Stripe will return the corresponding charge information. The same information is returned when creating or refunding the charge.

Returns a charge if a valid identifier was provided, and raises [an error](#errors) otherwise.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new ChargeService();
Charge charge = service.Get("ch_3MmlLrLkdIwHu7ix0snN0B15");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.ChargeParams{};
result, err := charge.Get("ch_3MmlLrLkdIwHu7ix0snN0B15", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Charge charge = Charge.retrieve("ch_3MmlLrLkdIwHu7ix0snN0B15");
```

```node
const stripe = require('stripe')('<<secret key>>');

const charge = await stripe.charges.retrieve('ch_3MmlLrLkdIwHu7ix0snN0B15');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

charge = stripe.Charge.retrieve("ch_3MmlLrLkdIwHu7ix0snN0B15")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$charge = $stripe->charges->retrieve('ch_3MmlLrLkdIwHu7ix0snN0B15', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

charge = Stripe::Charge.retrieve('ch_3MmlLrLkdIwHu7ix0snN0B15')
```

### Response

```json
{
  "id": "ch_3MmlLrLkdIwHu7ix0snN0B15",
  "object": "charge",
  "amount": 1099,
  "amount_captured": 1099,
  "amount_refunded": 0,
  "application": null,
  "application_fee": null,
  "application_fee_amount": null,
  "balance_transaction": "txn_3MmlLrLkdIwHu7ix0uke3Ezy",
  "billing_details": {
    "address": {
      "city": null,
      "country": null,
      "line1": null,
      "line2": null,
      "postal_code": null,
      "state": null
    },
    "email": null,
    "name": null,
    "phone": null
  },
  "calculated_statement_descriptor": "Stripe",
  "captured": true,
  "created": 1679090539,
  "currency": "usd",
  "customer": null,
  "description": null,
  "disputed": false,
  "failure_balance_transaction": null,
  "failure_code": null,
  "failure_message": null,
  "fraud_details": {},
  "livemode": false,
  "metadata": {},
  "on_behalf_of": null,
  "outcome": {
    "network_status": "approved_by_network",
    "reason": null,
    "risk_level": "normal",
    "risk_score": 32,
    "seller_message": "Payment complete.",
    "type": "authorized"
  },
  "paid": true,
  "payment_intent": null,
  "payment_method": "card_1MmlLrLkdIwHu7ixIJwEWSNR",
  "payment_method_details": {
    "card": {
      "brand": "visa",
      "checks": {
        "address_line1_check": null,
        "address_postal_code_check": null,
        "cvc_check": null
      },
      "country": "US",
      "exp_month": 3,
      "exp_year": 2024,
      "fingerprint": "mToisGZ01V71BCos",
      "funding": "credit",
      "installments": null,
      "last4": "4242",
      "mandate": null,
      "network": "visa",
      "three_d_secure": null,
      "wallet": null
    },
    "type": "card"
  },
  "receipt_email": null,
  "receipt_number": null,
  "receipt_url": "https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KOvG06AGMgZfBXyr1aw6LBa9vaaSRWU96d8qBwz9z2J_CObiV_H2-e8RezSK_sw0KISesp4czsOUlVKY",
  "refunded": false,
  "review": null,
  "shipping": null,
  "source_transfer": null,
  "statement_descriptor": null,
  "statement_descriptor_suffix": null,
  "status": "succeeded",
  "transfer_data": null,
  "transfer_group": null
}
```