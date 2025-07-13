# Delete a card

You can delete cards from a customer.
If you delete a card that is currently the default source, then the most recently added source will become the new default. If you delete a card that is the last remaining source on the customer, then the default_source attribute will become null.

For recipients: if you delete the default card, then the most recently added card will become the new default. If you delete the last remaining card on a recipient, then the default_card attribute will become null.

Note that for cards belonging to customers, you might want to prevent customers on paid subscriptions from deleting all cards on file, so that there is at least one default card for the next invoice payment attempt.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new SourceService();
IPaymentSource iPaymentSource = service.Detach(
    "acct_1032D82eZvKYlo2C",
    "card_1NGTaT2eZvKYlo2CZWSctn5n");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CardParams{Customer: stripe.String("acct_1032D82eZvKYlo2C")};
result, err := card.Del("card_1NGTaT2eZvKYlo2CZWSctn5n", params);
```

```java
Stripe.apiKey = "<<secret key>>";

CardDeleteParams params = CardDeleteParams.builder().build();

PaymentSource paymentSource =
  Card.delete("acct_1032D82eZvKYlo2C", "card_1NGTaT2eZvKYlo2CZWSctn5n", params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const customerSource = await stripe.customers.deleteSource(
  'acct_1032D82eZvKYlo2C',
  'card_1NGTaT2eZvKYlo2CZWSctn5n'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_source = stripe.Customer.delete_source(
  "acct_1032D82eZvKYlo2C",
  "card_1NGTaT2eZvKYlo2CZWSctn5n",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentSource = $stripe->customers->deleteSource(
  'acct_1032D82eZvKYlo2C',
  'card_1NGTaT2eZvKYlo2CZWSctn5n',
  []
);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_source = Stripe::Source.detach('acct_1032D82eZvKYlo2C', 'card_1NGTaT2eZvKYlo2CZWSctn5n')
```

### Response

```json
{
  "id": "card_1NGTaT2eZvKYlo2CZWSctn5n",
  "object": "card",
  "deleted": true
}
```