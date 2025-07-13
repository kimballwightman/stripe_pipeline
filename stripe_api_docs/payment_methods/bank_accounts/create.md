# Create a bank account

When you create a new bank account, you must specify a `Customer` object on which to create it.

Returns the bank account object.

- `source` (object | string, required)
  Either a token, like the ones returned by [Stripe.js](https://docs.stripe.com/docs/js.md), or a dictionary containing a user’s bank account details (with the options shown below).

  - `source.account_number` (string, required)
    The account number for the bank account, in string form. Must be a checking account.

  - `source.country` (string, required)
    The country in which the bank account is located.

  - `source.currency` (string, required)
    The currency the bank account is in. This must be a country/currency pairing that [Stripe supports](https://docs.stripe.com/docs/payouts.md).

  - `source.object` (string, required)
    The type of external account. Should be `bank_account`

  - `source.account_holder_name` (string, optional)
    The name of the person or business that owns the bank account. This field is required when attaching the bank account to a `Customer` object.

  - `source.account_holder_type` (enum, optional)
    The type of entity that holds the account. This field is required when attaching the bank account to a `Customer` object.

  - `source.routing_number` (string, optional)
    The routing number, sort code, or other country-appropriate institution number for the bank account. For US bank accounts, this is required and should be the ACH routing number, not the wire routing number. If you are providing an IBAN for `account_number`, this field is not required.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CustomerPaymentSourceCreateOptions { Source = "btok_1MvoS32eZvKYlo2CDhGTErAe" };
var service = new CustomerPaymentSourceService();
IPaymentSource iPaymentSource = service.Create("cus_9s6XI9OFIdpjIg", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentSourceParams{
  Source: stripe.String("btok_1MvoS32eZvKYlo2CDhGTErAe"),
  Customer: stripe.String("cus_9s6XI9OFIdpjIg"),
};
result, err := paymentsource.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

Customer customer = Customer.retrieve("cus_9s6XI9OFIdpjIg");

PaymentSourceCollectionCreateParams params =
  PaymentSourceCollectionCreateParams.builder().setSource("btok_1MvoS32eZvKYlo2CDhGTErAe").build();

PaymentSource paymentSource = customer.getSources().create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const customerSource = await stripe.customers.createSource(
  'cus_9s6XI9OFIdpjIg',
  {
    source: 'btok_1MvoS32eZvKYlo2CDhGTErAe',
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_source = stripe.Customer.create_source(
  "cus_9s6XI9OFIdpjIg",
  source="btok_1MvoS32eZvKYlo2CDhGTErAe",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentSource = $stripe->customers->createSource(
  'cus_9s6XI9OFIdpjIg',
  ['source' => 'btok_1MvoS32eZvKYlo2CDhGTErAe']
);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_source = Stripe::Customer.create_source(
  'cus_9s6XI9OFIdpjIg',
  {source: 'btok_1MvoS32eZvKYlo2CDhGTErAe'},
)
```

### Response

```json
{
  "id": "ba_1MvoIJ2eZvKYlo2CO9f0MabO",
  "object": "bank_account",
  "account_holder_name": "Jane Austen",
  "account_holder_type": "company",
  "account_type": null,
  "bank_name": "STRIPE TEST BANK",
  "country": "US",
  "currency": "usd",
  "customer": "cus_9s6XI9OFIdpjIg",
  "fingerprint": "1JWtPxqbdX5Gamtc",
  "last4": "6789",
  "metadata": {},
  "routing_number": "110000000",
  "status": "new"
}
```