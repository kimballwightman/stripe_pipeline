# The Discount object

- `id` (string)
  The ID of the discount object. Discounts cannot be fetched by ID. Use `expand[]=discounts` in API calls to expand discount IDs in an array.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `checkout_session` (nullable string)
  The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode.

- `coupon` (object)
  Hash describing the coupon applied to create this discount.

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

- `customer` (nullable string)
  The ID of the customer associated with this discount.

- `end` (nullable timestamp)
  If the coupon has a duration of `repeating`, the date that this discount will end. If the coupon has a duration of `once` or `forever`, this attribute will be null.

- `invoice` (nullable string)
  The invoice that the discount’s coupon was applied to, if it was applied directly to a particular invoice.

- `invoice_item` (nullable string)
  The invoice item `id` (or invoice line item `id` for invoice line items of type=‘subscription’) that the discount’s coupon was applied to, if it was applied directly to a particular invoice item or invoice line item.

- `promotion_code` (nullable string)
  The promotion code applied to create this discount.

- `start` (timestamp)
  Date that the coupon was applied.

- `subscription` (nullable string)
  The subscription that this coupon is applied to, if it is applied to a particular subscription.

- `subscription_item` (nullable string)
  The subscription item that this coupon is applied to, if it is applied to a particular subscription item.

### The Discount object

```json
{
  "id": "di_1M6vk22eZvKYlo2CYMGIhk14",
  "object": "discount",
  "checkout_session": "cs_test_b1mywbZHtQCQW2ncaItVPFqupwmfqNU4IMMdw3lArEBGt0QD0CZDrNQswR",
  "coupon": {
    "id": "wsd",
    "object": "coupon",
    "amount_off": null,
    "created": 1669116350,
    "currency": null,
    "duration": "forever",
    "duration_in_months": null,
    "livemode": false,
    "max_redemptions": null,
    "metadata": {},
    "name": null,
    "percent_off": 10,
    "redeem_by": null,
    "times_redeemed": 1,
    "valid": true
  },
  "customer": "cus_9s6XKzkNRiz8i3",
  "end": null,
  "invoice": null,
  "invoice_item": null,
  "promotion_code": null,
  "start": 1669120702,
  "subscription": null
}
```