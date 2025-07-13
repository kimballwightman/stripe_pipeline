# Create a card

When you create a new credit card, you must specify a customer or recipient on which to create it.

If the card’s owner has no default card, then the new card will become the default.
However, if the owner already has a default, then it will not change.
To change the default, you should [update the customer](https://docs.stripe.com/docs/api.md#update_customer) to have a new `default_source`.

Returns the `Card` object.

- `source` (object | string, required)
  A token, like the ones returned by [Stripe.js](https://docs.stripe.com/docs/js.md) or a dictionary containing a user’s card details (with the options shown below). Stripe will automatically validate the card.

  - `source.exp_month` (integer, required)
    Two-digit number representing the card’s expiration month.

  - `source.exp_year` (integer, required)
    Two- or -four-digit number representing the card’s expiration year.

  - `source.number` (string, required)
    The card number, as a string without any separators.

  - `source.object` (string, required)
    The type of payment source. It should be `card`.

  - `source.address_city` (string, optional)
    City / District / Suburb / Town / Village.

  - `source.address_country` (string, optional)
    Billing address country, if provided.

  - `source.address_line1` (string, optional)
    Address line 1 (Street address / PO Box / Company name).

  - `source.address_line2` (string, optional)
    Address line 2 (Apartment / Suite / Unit / Building).

  - `source.address_state` (string, optional)
    State / County / Province / Region.

  - `source.address_zip` (string, optional)
    ZIP or postal code.

  - `source.currency` (string, optional)
    Required when adding a card to an account (not applicable to customers or recipients). The card (which must be a debit card) can be used as a transfer destination for funds in this currency.

  - `source.cvc` (string, optional)
    Card security code. Highly recommended to always include this value, but it’s required only for accounts based in European countries.

  - `source.default_for_currency` (boolean, optional)
    Applicable only on accounts (not customers or recipients). If you set this to `true` (or if this is the first external account being added in this currency), this card will become the default external account for its currency.

  - `source.metadata` (object, optional)
    A set of key-value pairs that you can attach to a card object. This can be useful for storing additional information about the card in a structured format.

  - `source.name` (string, optional)
    Cardholder’s full name.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CustomerPaymentSourceCreateOptions { Source = "tok_visa" };
var service = new CustomerPaymentSourceService();
IPaymentSource iPaymentSource = service.Create("cus_9s6XGDTHzA66Po", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentSourceParams{
  Source: stripe.String("tok_visa"),
  Customer: stripe.String("cus_9s6XGDTHzA66Po"),
};
result, err := paymentsource.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

Customer customer = Customer.retrieve("cus_9s6XGDTHzA66Po");

PaymentSourceCollectionCreateParams params =
  PaymentSourceCollectionCreateParams.builder().setSource("tok_visa").build();

PaymentSource paymentSource = customer.getSources().create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const customerSource = await stripe.customers.createSource(
  'cus_9s6XGDTHzA66Po',
  {
    source: 'tok_visa',
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_source = stripe.Customer.create_source(
  "cus_9s6XGDTHzA66Po",
  source="tok_visa",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentSource = $stripe->customers->createSource('cus_9s6XGDTHzA66Po', ['source' => 'tok_visa']);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_source = Stripe::Customer.create_source('cus_9s6XGDTHzA66Po', {source: 'tok_visa'})
```

### Response

```json
{
  "id": "card_1NGTaT2eZvKYlo2CZWSctn5n",
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
  "customer": "cus_9s6XGDTHzA66Po",
  "cvc_check": "pass",
  "dynamic_last4": null,
  "exp_month": 8,
  "exp_year": 2024,
  "fingerprint": "Xt5EWLLDS7FJjR1c",
  "funding": "credit",
  "last4": "4242",
  "metadata": {},
  "name": null,
  "redaction": null,
  "tokenization_method": null,
  "wallet": null
}
```