# Create a Customer Session

Creates a Customer Session object that includes a single-use client secret that you can use on your front-end to grant client-side API access for certain customer resources.

Returns a Customer Session object.

- `components` (object, optional)
  Configuration for each component. Exactly 1 component must be enabled.

  - `components.buy_button` (object, optional)
    Configuration for buy button.

    - `components.buy_button.enabled` (boolean, required)
      Whether the buy button is enabled.

  - `components.payment_element` (object, optional)
    Configuration for the Payment Element.

    - `components.payment_element.enabled` (boolean, required)
      Whether the Payment Element is enabled.

    - `components.payment_element.features` (object, optional)
      This hash defines whether the Payment Element supports certain features.

      - `components.payment_element.features.payment_method_allow_redisplay_filters` (array of enums, optional)
        A list of [`allow_redisplay`](https://docs.stripe.com/api/payment_methods/object#payment_method_object-allow_redisplay) values that controls which saved payment methods the Payment Element displays by filtering to only show payment methods with an `allow_redisplay` value that is present in this list.

        If not specified, defaults to [“always”]. In order to display all saved payment methods, specify [“always”, “limited”, “unspecified”].

        Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

        Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

        This is the default value for payment methods where `allow_redisplay` wasn’t set.

      - `components.payment_element.features.payment_method_redisplay` (enum, optional)
        Controls whether or not the Payment Element shows saved payment methods. This parameter defaults to `disabled`.

        The feature is disabled.

        The feature is enabled.

      - `components.payment_element.features.payment_method_redisplay_limit` (integer, optional)
        Determines the max number of saved payment methods for the Payment Element to display. This parameter defaults to `3`. The maximum redisplay limit is `10`.

      - `components.payment_element.features.payment_method_remove` (enum, optional)
        Controls whether the Payment Element displays the option to remove a saved payment method.  This parameter defaults to `disabled`.

        Allowing buyers to remove their saved payment methods impacts subscriptions that depend on that payment method. Removing the payment method detaches the [`customer` object](https://docs.stripe.com/api/payment_methods/object#payment_method_object-customer) from that [PaymentMethod](https://docs.stripe.com/api/payment_methods).

        The feature is disabled.

        The feature is enabled.

      - `components.payment_element.features.payment_method_save` (enum, optional)
        Controls whether the Payment Element displays a checkbox offering to save a new payment method. This parameter defaults to `disabled`.

        If a customer checks the box, the [`allow_redisplay`](https://docs.stripe.com/api/payment_methods/object#payment_method_object-allow_redisplay) value on the PaymentMethod is set to `'always'` at confirmation time. For PaymentIntents, the [`setup_future_usage`](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-setup_future_usage) value is also set to the value defined in `payment_method_save_usage`.

        The feature is disabled.

        The feature is enabled.

      - `components.payment_element.features.payment_method_save_usage` (enum, optional)
        When using PaymentIntents and the customer checks the save checkbox, this field determines the [`setup_future_usage`](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-setup_future_usage) value used to confirm the PaymentIntent.

        When using SetupIntents, directly configure the [`usage`](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-usage) value on SetupIntent creation.

        Use `off_session` if your customer may or may not be present in your checkout flow.

        Use `on_session` if you intend to only reuse the payment method when your customer is present in your checkout flow.

  - `components.pricing_table` (object, optional)
    Configuration for the pricing table.

    - `components.pricing_table.enabled` (boolean, required)
      Whether the pricing table is enabled.

- `customer` (string, optional)
  The ID of an existing customer for which to create the Customer Session.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CustomerSessionCreateOptions
{
    Customer = "cus_PO34b57IOUb83c",
    Components = new CustomerSessionComponentsOptions
    {
        PricingTable = new CustomerSessionComponentsPricingTableOptions { Enabled = true },
    },
};
var service = new CustomerSessionService();
CustomerSession customerSession = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CustomerSessionParams{
  Customer: stripe.String("cus_PO34b57IOUb83c"),
  Components: &stripe.CustomerSessionComponentsParams{
    PricingTable: &stripe.CustomerSessionComponentsPricingTableParams{Enabled: stripe.Bool(true)},
  },
};
result, err := customersession.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

CustomerSessionCreateParams params =
  CustomerSessionCreateParams.builder()
    .setCustomer("cus_PO34b57IOUb83c")
    .setComponents(
      CustomerSessionCreateParams.Components.builder()
        .setPricingTable(
          CustomerSessionCreateParams.Components.PricingTable.builder().setEnabled(true).build()
        )
        .build()
    )
    .build();

CustomerSession customerSession = CustomerSession.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const customerSession = await stripe.customerSessions.create({
  customer: 'cus_PO34b57IOUb83c',
  components: {
    pricing_table: {
      enabled: true,
    },
  },
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

customer_session = stripe.CustomerSession.create(
  customer="cus_PO34b57IOUb83c",
  components={"pricing_table": {"enabled": True}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$customerSession = $stripe->customerSessions->create([
  'customer' => 'cus_PO34b57IOUb83c',
  'components' => ['pricing_table' => ['enabled' => true]],
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

customer_session = Stripe::CustomerSession.create({
  customer: 'cus_PO34b57IOUb83c',
  components: {pricing_table: {enabled: true}},
})
```

### Response

```json
{
  "object": "customer_session",
  "client_secret": "_POpxYpmkXdtttYtZQYhrsOJZ2RCQ9kCqqXRU6qrP5c4Jgje",
  "components": {
    "buy_button": {
      "enabled": false
    },
    "pricing_table": {
      "enabled": true
    }
  },
  "customer": "cus_PO34b57IOUb83c",
  "expires_at": 1684790027,
  "livemode": false
}
```