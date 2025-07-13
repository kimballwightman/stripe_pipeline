# Update a card

Updates a specified card for a given customer.

- `address_city` (string, optional)
  City/District/Suburb/Town/Village.

- `address_country` (string, optional)
  Billing address country, if provided when creating card.

- `address_line1` (string, optional)
  Address line 1 (Street address/PO Box/Company name).

- `address_line2` (string, optional)
  Address line 2 (Apartment/Suite/Unit/Building).

- `address_state` (string, optional)
  State/County/Province/Region.

- `address_zip` (string, optional)
  ZIP or postal code.

- `exp_month` (string, optional)
  Two digit number representing the card’s expiration month.

- `exp_year` (string, optional)
  Four digit number representing the card’s expiration year.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `name` (string, optional)
  Cardholder name.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CustomerPaymentSourceUpdateOptions { Name = "Jenny Rosen" };
var service = new CustomerPaymentSourceService();
IPaymentSource iPaymentSource = service.Update(
    "acct_1032D82eZvKYlo2C",
    "card_1NBLeN2eZvKYlo2CIq1o7Pzs",
    options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CardParams{
  Name: stripe.String("Jenny Rosen"),
  Customer: stripe.String("acct_1032D82eZvKYlo2C"),
};
result, err := card.Update("card_1NBLeN2eZvKYlo2CIq1o7Pzs", params);
```

```java
Stripe.apiKey = "<<secret key>>";

CardUpdateParams params = CardUpdateParams.builder().setName("Jenny Rosen").build();

TODO tODO = Card.update("acct_1032D82eZvKYlo2C", "card_1NBLeN2eZvKYlo2CIq1o7Pzs", params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const customerSource = await stripe.customers.updateSource(
  'acct_1032D82eZvKYlo2C',
  'card_1NBLeN2eZvKYlo2CIq1o7Pzs',
  {
    name: 'Jenny Rosen',
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_source = stripe.Customer.modify_source(
  "acct_1032D82eZvKYlo2C",
  "card_1NBLeN2eZvKYlo2CIq1o7Pzs",
  name="Jenny Rosen",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentSource = $stripe->customers->updateSource(
  'acct_1032D82eZvKYlo2C',
  'card_1NBLeN2eZvKYlo2CIq1o7Pzs',
  ['name' => 'Jenny Rosen']
);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_source = Stripe::Customer.update_source(
  'acct_1032D82eZvKYlo2C',
  'card_1NBLeN2eZvKYlo2CIq1o7Pzs',
  {name: 'Jenny Rosen'},
)
```

### Response

```json
{
  "id": "card_1NBLeN2eZvKYlo2CIq1o7Pzs",
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
  "cvc_check": "pass",
  "dynamic_last4": null,
  "exp_month": 8,
  "exp_year": 2024,
  "fingerprint": "Xt5EWLLDS7FJjR1c",
  "funding": "credit",
  "last4": "4242",
  "metadata": {},
  "name": "Jenny Rosen",
  "redaction": null,
  "tokenization_method": null,
  "wallet": null,
  "account": "acct_1032D82eZvKYlo2C"
}
```