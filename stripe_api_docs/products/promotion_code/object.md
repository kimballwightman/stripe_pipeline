# The Promotion Code object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `active` (boolean)
  Whether the promotion code is currently active. A promotion code is only active if the coupon is also valid.

- `code` (string)
  The customer-facing code. Regardless of case, this code must be unique across all active promotion codes for each customer. Valid characters are lower case letters (a-z), upper case letters (A-Z), and digits (0-9).

- `coupon` (object)
  Hash describing the coupon for this promotion code.

  - `coupon.id` (string)
    Unique identifier for the object.

  - `coupon.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `coupon.amount_off` (nullable integer)
    Amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer.

  - `coupon.applies_to` (nullable object)
    Contains information about what this coupon applies to.

    - `coupon.applies_to.products` (array of strings)
      A list of product IDs this coupon applies to

  - `coupon.created` (timestamp)
    Time at which the object was created. Measured in seconds since the Unix epoch.

  - `coupon.currency` (nullable enum)
    If `amount_off` has been set, the three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the amount to take off.

  - `coupon.currency_options` (nullable object)
    Coupons defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

    - `coupon.currency_options.<currency>.amount_off` (integer)
      Amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer.

  - `coupon.duration` (enum)
    One of `forever`, `once`, or `repeating`. Describes how long a customer who applies this coupon will get the discount.

    Applies to all charges from a subscription with this coupon applied.

    Applies to the first charge from a subscription with this coupon applied.

    Applies to charges in the first `duration_in_months` months from a subscription with this coupon applied. This value is deprecated and will be replaced in future versions of the API.

  - `coupon.duration_in_months` (nullable integer)
    If `duration` is `repeating`, the number of months the coupon applies. Null if coupon `duration` is `forever` or `once`.

  - `coupon.livemode` (boolean)
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

  - `coupon.max_redemptions` (nullable integer)
    Maximum number of times this coupon can be redeemed, in total, across all customers, before it is no longer valid.

  - `coupon.metadata` (nullable object)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

  - `coupon.name` (nullable string)
    Name of the coupon displayed to customers on for instance invoices or receipts.

  - `coupon.percent_off` (nullable float)
    Percent that will be taken off the subtotal of any invoices for this customer for the duration of the coupon. For example, a coupon with percent_off of 50 will make a 100 invoice 50 instead.

  - `coupon.redeem_by` (nullable timestamp)
    Date after which the coupon can no longer be redeemed.

  - `coupon.times_redeemed` (integer)
    Number of times this coupon has been applied to a customer.

  - `coupon.valid` (boolean)
    Taking account of the above properties, whether this coupon can still be applied to a customer.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `customer` (nullable string)
  The customer that this promotion code can be used by.

- `expires_at` (nullable timestamp)
  Date at which the promotion code can no longer be redeemed.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `max_redemptions` (nullable integer)
  Maximum number of times this promotion code can be redeemed.

- `metadata` (nullable object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `restrictions` (object)
  Settings that restrict the redemption of the promotion code.

  - `restrictions.currency_options` (nullable object)
    Promotion code restrictions defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

    - `restrictions.currency_options.<currency>.minimum_amount` (integer)
      Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a purchase must be $100 or more to work).

  - `restrictions.first_time_transaction` (boolean)
    A Boolean indicating if the Promotion Code should only be redeemed for Customers without any successful payments or invoices

  - `restrictions.minimum_amount` (nullable integer)
    Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a purchase must be $100 or more to work).

  - `restrictions.minimum_amount_currency` (nullable string)
    Three-letter [ISO code](https://stripe.com/docs/currencies) for minimum_amount

- `times_redeemed` (integer)
  Number of times this promotion code has been used.

### The Promotion Code object

```json
{
  "id": "promo_1MiM6KLkdIwHu7ixrIaX4wgn",
  "object": "promotion_code",
  "active": true,
  "code": "A1H1Q1MG",
  "coupon": {
    "id": "nVJYDOag",
    "object": "coupon",
    "amount_off": null,
    "created": 1678040164,
    "currency": null,
    "duration": "repeating",
    "duration_in_months": 3,
    "livemode": false,
    "max_redemptions": null,
    "metadata": {},
    "name": null,
    "percent_off": 25.5,
    "redeem_by": null,
    "times_redeemed": 0,
    "valid": true
  },
  "created": 1678040164,
  "customer": null,
  "expires_at": null,
  "livemode": false,
  "max_redemptions": null,
  "metadata": {},
  "restrictions": {
    "first_time_transaction": false,
    "minimum_amount": null,
    "minimum_amount_currency": null
  },
  "times_redeemed": 0
}
```