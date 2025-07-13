# Create a shipping rate

Creates a new shipping rate object.

Returns a shipping rate object if the call succeeded.

- `display_name` (string, required)
  The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.

- `delivery_estimate` (object, optional)
  The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.

  - `delivery_estimate.maximum` (object, optional)
    The upper bound of the estimated range. If empty, represents no upper bound i.e., infinite.

    - `delivery_estimate.maximum.unit` (enum, required)
      A unit of time.

      The delivery estimate is in business days.

      The delivery estimate is in days.

      The delivery estimate is in hours.

      The delivery estimate is in months.

      The delivery estimate is in weeks.

    - `delivery_estimate.maximum.value` (integer, required)
      Must be greater than 0.

  - `delivery_estimate.minimum` (object, optional)
    The lower bound of the estimated range. If empty, represents no lower bound.

    - `delivery_estimate.minimum.unit` (enum, required)
      A unit of time.

      The delivery estimate is in business days.

      The delivery estimate is in days.

      The delivery estimate is in hours.

      The delivery estimate is in months.

      The delivery estimate is in weeks.

    - `delivery_estimate.minimum.value` (integer, required)
      Must be greater than 0.

- `fixed_amount` (object, optional)
  Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.

  - `fixed_amount.amount` (integer, required)
    A non-negative integer in cents representing how much to charge.

  - `fixed_amount.currency` (enum, required)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `fixed_amount.currency_options` (object, optional)
    Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

    - `fixed_amount.currency_options.<currency>.amount` (integer, required)
      A non-negative integer in cents representing how much to charge.

    - `fixed_amount.currency_options.<currency>.tax_behavior` (enum, optional)
      Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `tax_behavior` (enum, optional)
  Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.

- `tax_code` (string, optional)
  A [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID. The Shipping tax code is `txcd_92010001`.

- `type` (enum, optional)
  The type of calculation to use on the shipping rate.

  The shipping rate is a fixed amount.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new ShippingRateCreateOptions
{
    DisplayName = "Ground shipping",
    Type = "fixed_amount",
    FixedAmount = new ShippingRateFixedAmountOptions { Amount = 500, Currency = "usd" },
};
var service = new ShippingRateService();
ShippingRate shippingRate = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.ShippingRateParams{
  DisplayName: stripe.String("Ground shipping"),
  Type: stripe.String("fixed_amount"),
  FixedAmount: &stripe.ShippingRateFixedAmountParams{
    Amount: stripe.Int64(500),
    Currency: stripe.String(string(stripe.CurrencyUSD)),
  },
};
result, err := shippingrate.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

ShippingRateCreateParams params =
  ShippingRateCreateParams.builder()
    .setDisplayName("Ground shipping")
    .setType(ShippingRateCreateParams.Type.FIXED_AMOUNT)
    .setFixedAmount(
      ShippingRateCreateParams.FixedAmount.builder().setAmount(500L).setCurrency("usd").build()
    )
    .build();

ShippingRate shippingRate = ShippingRate.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const shippingRate = await stripe.shippingRates.create({
  display_name: 'Ground shipping',
  type: 'fixed_amount',
  fixed_amount: {
    amount: 500,
    currency: 'usd',
  },
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

shipping_rate = stripe.ShippingRate.create(
  display_name="Ground shipping",
  type="fixed_amount",
  fixed_amount={"amount": 500, "currency": "usd"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$shippingRate = $stripe->shippingRates->create([
  'display_name' => 'Ground shipping',
  'type' => 'fixed_amount',
  'fixed_amount' => [
    'amount' => 500,
    'currency' => 'usd',
  ],
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

shipping_rate = Stripe::ShippingRate.create({
  display_name: 'Ground shipping',
  type: 'fixed_amount',
  fixed_amount: {
    amount: 500,
    currency: 'usd',
  },
})
```

### Response

```json
{
  "id": "shr_1MrRx2LkdIwHu7ixikgEA6Wd",
  "object": "shipping_rate",
  "active": true,
  "created": 1680207604,
  "delivery_estimate": null,
  "display_name": "Ground shipping",
  "fixed_amount": {
    "amount": 500,
    "currency": "usd"
  },
  "livemode": false,
  "metadata": {},
  "tax_behavior": "unspecified",
  "tax_code": null,
  "type": "fixed_amount"
}
```