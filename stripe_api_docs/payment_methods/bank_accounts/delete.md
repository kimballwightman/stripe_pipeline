# Delete a bank account

You can delete bank accounts from a Customer.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new SourceService();
IPaymentSource iPaymentSource = service.Detach("cus_9s6XKzkNRiz8i3", "ba_1NkxyL2eZvKYlo2CwZgb2mzO");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CardParams{Customer: stripe.String("cus_9s6XKzkNRiz8i3")};
result, err := card.Del("ba_1NkxyL2eZvKYlo2CwZgb2mzO", params);
```

```java
Stripe.apiKey = "<<secret key>>";

CardDeleteParams params = CardDeleteParams.builder().build();

PaymentSource paymentSource =
  Card.delete("cus_9s6XKzkNRiz8i3", "ba_1NkxyL2eZvKYlo2CwZgb2mzO", params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const customerSource = await stripe.customers.deleteSource(
  'cus_9s6XKzkNRiz8i3',
  'ba_1NkxyL2eZvKYlo2CwZgb2mzO'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_source = stripe.Customer.delete_source(
  "cus_9s6XKzkNRiz8i3",
  "ba_1NkxyL2eZvKYlo2CwZgb2mzO",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentSource = $stripe->customers->deleteSource(
  'cus_9s6XKzkNRiz8i3',
  'ba_1NkxyL2eZvKYlo2CwZgb2mzO',
  []
);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_source = Stripe::Source.detach('cus_9s6XKzkNRiz8i3', 'ba_1NkxyL2eZvKYlo2CwZgb2mzO')
```

### Response

```json
{
  "customer": "cus_9s6XKzkNRiz8i3",
  "id": "ba_1NkxyL2eZvKYlo2CwZgb2mzO",
  "object": "bank_account",
  "deleted": true
}
```