# Retrieve a token

Retrieves the token with the given ID.

Returns a token if you provide a valid ID. Raises [an error](#errors) otherwise.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new TokenService();
Token token = service.Get("tok_1N3T00LkdIwHu7ixt44h1F8k");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TokenParams{};
result, err := token.Get("tok_1N3T00LkdIwHu7ixt44h1F8k", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Token token = Token.retrieve("tok_1N3T00LkdIwHu7ixt44h1F8k");
```

```node
const stripe = require('stripe')('<<secret key>>');

const token = await stripe.tokens.retrieve('tok_1N3T00LkdIwHu7ixt44h1F8k');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

token = stripe.Token.retrieve("tok_1N3T00LkdIwHu7ixt44h1F8k")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$token = $stripe->tokens->retrieve('tok_1N3T00LkdIwHu7ixt44h1F8k', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

token = Stripe::Token.retrieve('tok_1N3T00LkdIwHu7ixt44h1F8k')
```

### Response

```json
{
  "id": "tok_1N3T00LkdIwHu7ixt44h1F8k",
  "object": "token",
  "card": {
    "id": "card_1N3T00LkdIwHu7ixRdxpVI1Q",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "US",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2026,
    "fingerprint": "mToisGZ01V71BCos",
    "funding": "credit",
    "last4": "4242",
    "metadata": {},
    "name": null,
    "tokenization_method": null,
    "wallet": null
  },
  "client_ip": "52.35.78.6",
  "created": 1683071568,
  "livemode": false,
  "type": "card",
  "used": false
}
```