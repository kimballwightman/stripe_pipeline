# Metadata

Updateable Stripe objects—including [Account](https://docs.stripe.com/api/accounts.md), [Charge](https://docs.stripe.com/api/charges.md), [Customer](https://docs.stripe.com/api/customers.md), [PaymentIntent](https://docs.stripe.com/api/payment_intents.md), [Refund](https://docs.stripe.com/api/refunds.md), [Subscription](https://docs.stripe.com/api/subscriptions.md), and [Transfer](https://docs.stripe.com/api/transfers.md) have a `metadata` parameter. You can use this parameter to attach key-value data to these Stripe objects.

You can specify up to 50 keys, with key names up to 40 characters long and values up to 500 characters long. Keys and values are stored as strings and can contain any characters with one exception: you can’t use square brackets ([ and ]) in keys.

You can use metadata to store additional, structured information on an object. For example, you could store your user’s full name and corresponding unique identifier from your system on a Stripe [Customer](https://docs.stripe.com/api/customers.md) object. Stripe doesn’t use metadata—for example, we don’t use it to authorize or decline a charge and it won’t be seen by your users unless you choose to show it to them.

Some of the objects listed above also support a `description` parameter. You can use the `description` parameter to annotate a charge-for example, a human-readable description such as `2 shirts for test@example.com`. Unlike `metadata`, `description` is a single string, which your users might see (for example, in email receipts Stripe sends on your behalf).

Don’t store any sensitive information (bank account numbers, card details, and so on) as metadata or in the `description` parameter.

## Sample metadata use cases

- **Link IDs**: Attach your system’s unique IDs to a Stripe object to simplify lookups. For example, add your order number to a charge, your user ID to a customer or recipient, or a unique receipt number to a transfer.
- **Refund papertrails**: Store information about the reason for a refund and the individual responsible for its creation.
- **Customer details**: Annotate a customer by storing an internal ID for your future use.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CustomerCreateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var service = new CustomerService();
Customer customer = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CustomerParams{};
params.AddMetadata("order_id", "6735")
result, err := customer.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

CustomerCreateParams params =
  CustomerCreateParams.builder().putMetadata("order_id", "6735").build();

Customer customer = Customer.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const customer = await stripe.customers.create({
  metadata: {
    order_id: '6735',
  },
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

customer = stripe.Customer.create(metadata={"order_id": "6735"})
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$customer = $stripe->customers->create(['metadata' => ['order_id' => '6735']]);
```

```ruby
Stripe.api_key = '<<secret key>>'

customer = Stripe::Customer.create({metadata: {order_id: '6735'}})
```

```json
{
  "id": "cus_123456789",
  "object": "customer",
  "address": {
    "city": "city",
    "country": "US",
    "line1": "line 1",
    "line2": "line 2",
    "postal_code": "90210",
    "state": "CA"
  },
  "balance": 0,
  "created": 1483565364,
  "currency": null,
  "default_source": null,
  "delinquent": false,
  "description": null,
  "discount": null,
  "email": null,
  "invoice_prefix": "C11F7E1",
  "invoice_settings": {
    "custom_fields": null,
    "default_payment_method": null,
    "footer": null,
    "rendering_options": null
  },
  "livemode": false,
  "metadata": {
    "order_id": "6735"
  },
  "name": null,
  "next_invoice_sequence": 1,
  "phone": null,
  "preferred_locales": [],
  "shipping": null,
  "tax_exempt": "none"
}
```