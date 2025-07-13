# The Shipping Rate object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `active` (boolean)
  Whether the shipping rate can be used for new purchases. Defaults to `true`.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `delivery_estimate` (nullable object)
  The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.

  - `delivery_estimate.maximum` (nullable object)
    The upper bound of the estimated range. If empty, represents no upper bound i.e., infinite.

    - `delivery_estimate.maximum.unit` (enum)
      A unit of time.

      The delivery estimate is in business days.

      The delivery estimate is in days.

      The delivery estimate is in hours.

      The delivery estimate is in months.

      The delivery estimate is in weeks.

    - `delivery_estimate.maximum.value` (integer)
      Must be greater than 0.

  - `delivery_estimate.minimum` (nullable object)
    The lower bound of the estimated range. If empty, represents no lower bound.

    - `delivery_estimate.minimum.unit` (enum)
      A unit of time.

      The delivery estimate is in business days.

      The delivery estimate is in days.

      The delivery estimate is in hours.

      The delivery estimate is in months.

      The delivery estimate is in weeks.

    - `delivery_estimate.minimum.value` (integer)
      Must be greater than 0.

- `display_name` (nullable string)
  The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.

- `fixed_amount` (nullable object)
  Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.

  - `fixed_amount.amount` (integer)
    A non-negative integer in cents representing how much to charge.

  - `fixed_amount.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `fixed_amount.currency_options` (nullable object)
    Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

    - `fixed_amount.currency_options.<currency>.amount` (integer)
      A non-negative integer in cents representing how much to charge.

    - `fixed_amount.currency_options.<currency>.tax_behavior` (enum)
      Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `tax_behavior` (nullable enum)
  Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.

- `tax_code` (nullable string)
  A [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID. The Shipping tax code is `txcd_92010001`.

- `type` (enum)
  The type of calculation to use on the shipping rate.

  The shipping rate is a fixed amount.

### The Shipping Rate object

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