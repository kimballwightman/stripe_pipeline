# Create a card token

Creates a single-use token that represents a credit card’s details.
You can use this token in place of a credit card dictionary with any v1 API method.
You can only use these tokens once
by [creating a new Charge object](#create_charge)
or by attaching them to a [Customer object](#create_customer).

To use this functionality, you need to [enable access
to the raw card data APIs](https://support.stripe.com/questions/enabling-access-to-raw-card-data-apis).
In most cases, you can use our recommended
[payments integrations](https://docs.stripe.com/payments) instead of using the API.

Returns the created card token if it’s successful. Otherwise, this call raises [an error](#errors).

- `card` (object | string, optional)
  The card this token will represent. If you also pass in a customer, the card must be the ID of a card belonging to the customer. Otherwise, if you do not pass in a customer, this is a dictionary containing a user’s credit card details, with the options described below.

  - `card.exp_month` (string, required)
    Two-digit number representing the card’s expiration month.

  - `card.exp_year` (string, required)
    Two- or four-digit number representing the card’s expiration year.

  - `card.number` (string, required)
    The card number, as a string without any separators.

  - `card.address_city` (string, optional)
    City / District / Suburb / Town / Village.

  - `card.address_country` (string, optional)
    Billing address country, if provided.

  - `card.address_line1` (string, optional)
    Address line 1 (Street address / PO Box / Company name).

  - `card.address_line2` (string, optional)
    Address line 2 (Apartment / Suite / Unit / Building).

  - `card.address_state` (string, optional)
    State / County / Province / Region.

  - `card.address_zip` (string, optional)
    ZIP or postal code.

  - `card.currency` (string, optional)
    Required in order to add the card to an account; in all other cases, this parameter is not used. When added to an account, the card (which must be a debit card) can be used as a transfer destination for funds in this currency.

  - `card.cvc` (string, optional)
    Card security code. Highly recommended to always include this value.

  - `card.name` (string, optional)
    Cardholder’s full name.

  - `card.networks` (object, optional)
    Contains information about card networks used to process the payment.

    - `card.networks.preferred` (enum, optional)
      The customer’s preferred card network for co-branded cards. Supports `cartes_bancaires`, `mastercard`, or `visa`. Selection of a network that does not apply to the card will be stored as `invalid_preference` on the card.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new TokenCreateOptions
{
    Card = new TokenCardOptions
    {
        Number = "4242424242424242",
        ExpMonth = "5",
        ExpYear = "2026",
        Cvc = "314",
    },
};
var service = new TokenService();
Token token = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TokenParams{
  Card: &stripe.CardParams{
    Number: stripe.String("4242424242424242"),
    ExpMonth: stripe.String("5"),
    ExpYear: stripe.String("2026"),
    CVC: stripe.String("314"),
  },
};
result, err := token.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

TokenCreateParams params =
  TokenCreateParams.builder()
    .setCard(
      TokenCreateParams.Card.builder()
        .setNumber("4242424242424242")
        .setExpMonth("5")
        .setExpYear("2026")
        .setCvc("314")
        .build()
    )
    .build();

Token token = Token.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const token = await stripe.tokens.create({
  card: {
    number: '4242424242424242',
    exp_month: '5',
    exp_year: '2026',
    cvc: '314',
  },
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

token = stripe.Token.create(
  card={"number": "4242424242424242", "exp_month": "5", "exp_year": "2026", "cvc": "314"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$token = $stripe->tokens->create([
  'card' => [
    'number' => '4242424242424242',
    'exp_month' => '5',
    'exp_year' => '2026',
    'cvc' => '314',
  ],
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

token = Stripe::Token.create({
  card: {
    number: '4242424242424242',
    exp_month: '5',
    exp_year: '2026',
    cvc: '314',
  },
})
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