# Detach a source

Detaches a Source object from a Customer. The status of a source is changed to `consumed` when it is detached and it can no longer be used to create a charge.

Returns the detached Source object.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new SourceService();
IPaymentSource iPaymentSource = service.Detach(
    "cus_9s6XKzkNRiz8i3",
    "src_1Nlghd2eZvKYlo2C6RFLJcv4");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CardParams{Customer: stripe.String("cus_9s6XKzkNRiz8i3")};
result, err := card.Del("src_1Nlghd2eZvKYlo2C6RFLJcv4", params);
```

```java
Stripe.apiKey = "<<secret key>>";

CardDeleteParams params = CardDeleteParams.builder().build();

PaymentSource paymentSource =
  Card.delete("cus_9s6XKzkNRiz8i3", "src_1Nlghd2eZvKYlo2C6RFLJcv4", params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const customerSource = await stripe.customers.deleteSource(
  'cus_9s6XKzkNRiz8i3',
  'src_1Nlghd2eZvKYlo2C6RFLJcv4'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_source = stripe.Customer.delete_source(
  "cus_9s6XKzkNRiz8i3",
  "src_1Nlghd2eZvKYlo2C6RFLJcv4",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentSource = $stripe->customers->deleteSource(
  'cus_9s6XKzkNRiz8i3',
  'src_1Nlghd2eZvKYlo2C6RFLJcv4',
  []
);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_source = Stripe::Source.detach('cus_9s6XKzkNRiz8i3', 'src_1Nlghd2eZvKYlo2C6RFLJcv4')
```

### Response

```json
{
  "id": "src_1Nlghd2eZvKYlo2C6RFLJcv4",
  "object": "source",
  "ach_credit_transfer": {
    "account_number": "test_52796e3294dc",
    "routing_number": "110000000",
    "fingerprint": "ecpwEzmBOSMOqQTL",
    "bank_name": "TEST BANK",
    "swift_code": "TSTEZ122"
  },
  "amount": 0,
  "client_secret": "src_client_secret_smKYWLhbzxzgLfvhKt1QeQOn",
  "created": 1693610677,
  "currency": "usd",
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
    "amount_charged": 1000,
    "amount_returned": 0,
    "refund_attributes_status": "missing",
    "refund_attributes_method": "email"
  },
  "redaction": null,
  "statement_descriptor": null,
  "status": "consumed",
  "type": "ach_credit_transfer",
  "usage": "reusable",
  "customer": "cus_9s6XKzkNRiz8i3"
}
```