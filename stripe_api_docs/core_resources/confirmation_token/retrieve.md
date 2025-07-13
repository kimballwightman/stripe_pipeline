# Retrieve a ConfirmationToken

Retrieves an existing ConfirmationToken object

Returns the specified ConfirmationToken


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new ConfirmationTokenService();
ConfirmationToken confirmationToken = service.Get("ctoken_1NnQUf2eZvKYlo2CIObdtbnb");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.ConfirmationTokenParams{};
result, err := confirmationtoken.Get("ctoken_1NnQUf2eZvKYlo2CIObdtbnb", params);
```

```java
Stripe.apiKey = "<<secret key>>";

ConfirmationToken confirmationToken = ConfirmationToken.retrieve("ctoken_1NnQUf2eZvKYlo2CIObdtbnb");
```

```node
const stripe = require('stripe')('<<secret key>>');

const confirmationToken = await stripe.confirmationTokens.retrieve(
  'ctoken_1NnQUf2eZvKYlo2CIObdtbnb'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

confirmation_token = stripe.ConfirmationToken.retrieve("ctoken_1NnQUf2eZvKYlo2CIObdtbnb")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$confirmationToken = $stripe->confirmationTokens->retrieve('ctoken_1NnQUf2eZvKYlo2CIObdtbnb', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

confirmation_token = Stripe::ConfirmationToken.retrieve('ctoken_1NnQUf2eZvKYlo2CIObdtbnb')
```

### Response

```json
{
  "id": "ctoken_1NnQUf2eZvKYlo2CIObdtbnb",
  "object": "confirmation_token",
  "created": 1694025025,
  "expires_at": 1694068225,
  "livemode": true,
  "mandate_data": null,
  "payment_intent": null,
  "payment_method": null,
  "payment_method_preview": {
    "billing_details": {
      "address": {
        "city": "Hyde Park",
        "country": "US",
        "line1": "50 Sprague St",
        "line2": "",
        "postal_code": "02136",
        "state": "MA"
      },
      "email": "jennyrosen@stripe.com",
      "name": "Jenny Rosen",
      "phone": null
    },
    "card": {
      "brand": "visa",
      "checks": {
        "address_line1_check": null,
        "address_postal_code_check": null,
        "cvc_check": null
      },
      "country": "US",
      "display_brand": "visa",
      "exp_month": 8,
      "exp_year": 2026,
      "funding": "credit",
      "generated_from": null,
      "last4": "4242",
      "networks": {
        "available": [
          "visa"
        ],
        "preferred": null
      },
      "three_d_secure_usage": {
        "supported": true
      },
      "wallet": null
    },
    "type": "card"
  },
  "return_url": "https://example.com/return",
  "setup_future_usage": "off_session",
  "setup_intent": null,
  "shipping": {
    "address": {
      "city": "Hyde Park",
      "country": "US",
      "line1": "50 Sprague St",
      "line2": "",
      "postal_code": "02136",
      "state": "MA"
    },
    "name": "Jenny Rosen",
    "phone": null
  }
}
```