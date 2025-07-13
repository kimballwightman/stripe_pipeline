# Attach a source

Attaches a Source object to a Customer. The source must be in a chargeable or pending state.

Returns the attached Source object.

- `source` (string, required)
  The identifier of the source to be attached.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CustomerPaymentSourceCreateOptions { Source = "src_1NfRGv2eZvKYlo2Cv7NAImBL" };
var service = new CustomerPaymentSourceService();
IPaymentSource iPaymentSource = service.Create("cus_9s6XKzkNRiz8i3", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentSourceParams{
  Source: stripe.String("src_1NfRGv2eZvKYlo2Cv7NAImBL"),
  Customer: stripe.String("cus_9s6XKzkNRiz8i3"),
};
result, err := paymentsource.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

Customer customer = Customer.retrieve("cus_9s6XKzkNRiz8i3");

PaymentSourceCollectionCreateParams params =
  PaymentSourceCollectionCreateParams.builder().setSource("src_1NfRGv2eZvKYlo2Cv7NAImBL").build();

PaymentSource paymentSource = customer.getSources().create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const customerSource = await stripe.customers.createSource(
  'cus_9s6XKzkNRiz8i3',
  {
    source: 'src_1NfRGv2eZvKYlo2Cv7NAImBL',
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_source = stripe.Customer.create_source(
  "cus_9s6XKzkNRiz8i3",
  source="src_1NfRGv2eZvKYlo2Cv7NAImBL",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentSource = $stripe->customers->createSource(
  'cus_9s6XKzkNRiz8i3',
  ['source' => 'src_1NfRGv2eZvKYlo2Cv7NAImBL']
);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_source = Stripe::Customer.create_source(
  'cus_9s6XKzkNRiz8i3',
  {source: 'src_1NfRGv2eZvKYlo2Cv7NAImBL'},
)
```

### Response

```json
{
  "id": "src_1NfRGv2eZvKYlo2Cv7NAImBL",
  "object": "source",
  "ach_credit_transfer": {
    "account_number": "test_52796e3294dc",
    "routing_number": "110000000",
    "fingerprint": "ecpwEzmBOSMOqQTL",
    "bank_name": "TEST BANK",
    "swift_code": "TSTEZ122"
  },
  "amount": 1000,
  "client_secret": "src_client_secret_sBqfX18eq6GPfGxGvVfMByCp",
  "created": 1692121393,
  "currency": "usd",
  "customer": "cus_9s6XKzkNRiz8i3",
  "flow": "receiver",
  "livemode": false,
  "metadata": {},
  "owner": {
    "address": null,
    "email": "jenny.rosen@example.com",
    "name": null,
    "phone": null,
    "verified_address": null,
    "verified_email": null,
    "verified_name": null,
    "verified_phone": null
  },
  "receiver": {
    "address": "121042882-38381234567890123",
    "amount_received": 1000,
    "amount_charged": 0,
    "amount_returned": 0,
    "refund_attributes_status": "missing",
    "refund_attributes_method": "email"
  },
  "redaction": null,
  "statement_descriptor": null,
  "status": "chargeable",
  "type": "ach_credit_transfer",
  "usage": "reusable"
}
```