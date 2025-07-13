# Create a PII token

Creates a single-use token that represents the details of personally identifiable information (PII).
You can use this token in place of an [id_number](#update_account-individual-id_number) or [id_number_secondary](#update_account-individual-id_number_secondary) in Account or Person Update API methods.
You can only use a PII token once.

Returns the created PII token if it’s successful. Otherwise, this call raises [an error](#errors).

- `pii` (object, required)
  The PII this token represents.

  - `pii.id_number` (string, optional)
    The `id_number` for the PII, in string form.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new TokenCreateOptions { Pii = new TokenPiiOptions { IdNumber = "000000000" } };
var service = new TokenService();
Token token = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TokenParams{PII: &stripe.TokenPIIParams{IDNumber: stripe.String("000000000")}};
result, err := token.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

TokenCreateParams params =
  TokenCreateParams.builder()
    .setPii(TokenCreateParams.Pii.builder().setIdNumber("000000000").build())
    .build();

Token token = Token.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const token = await stripe.tokens.create({
  pii: {
    id_number: '000000000',
  },
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

token = stripe.Token.create(pii={"id_number": "000000000"})
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$token = $stripe->tokens->create(['pii' => ['id_number' => '000000000']]);
```

```ruby
Stripe.api_key = '<<secret key>>'

token = Stripe::Token.create({pii: {id_number: '000000000'}})
```

### Response

```json
{
  "id": "pii_18PwbX2eZvKYlo2CzRXgwN3J",
  "object": "token",
  "client_ip": "124.123.76.134",
  "created": 1466783547,
  "livemode": false,
  "redaction": null,
  "type": "pii",
  "used": false
}
```