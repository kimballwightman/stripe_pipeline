# The Credit Grant object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (object)
  Amount of this credit grant.

  - `amount.monetary` (nullable object)
    The monetary amount.

    - `amount.monetary.currency` (string)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `amount.monetary.value` (integer)
      A positive integer representing the amount.

  - `amount.type` (enum)
    The type of this amount. We currently only support `monetary` billing credits.

    The amount is a monetary amount.

- `applicability_config` (object)
  Configuration specifying what this credit grant applies to. We currently only support `metered` prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter) attached to them.

  - `applicability_config.scope` (object)
    Specify the scope of this applicability config.

    - `applicability_config.scope.price_type` (nullable enum)
      The price type that credit grants can apply to. We currently only support the `metered` price type. This refers to prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter) attached to them. Cannot be used in combination with `prices`.

      Credit grants being created can only apply to metered prices.

- `category` (enum)
  The category of this credit grant. This is for tracking purposes and isn’t displayed to the customer.

  The credit grant was purchased by the customer for some amount.

  The credit grant was given to the customer for free.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `customer` (string)
  ID of the customer receiving the billing credits.

- `effective_at` (nullable timestamp)
  The time when the billing credits become effective-when they’re eligible for use.

- `expires_at` (nullable timestamp)
  The time when the billing credits expire. If not present, the billing credits don’t expire.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `name` (nullable string)
  A descriptive name shown in dashboard.

- `test_clock` (nullable string)
  ID of the test clock this credit grant belongs to.

- `updated` (timestamp)
  Time at which the object was last updated. Measured in seconds since the Unix epoch.

- `voided_at` (nullable timestamp)
  The time when this credit grant was voided. If not present, the credit grant hasn’t been voided.

### The Credit Grant object

```json
{
  "id": "credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo",
  "object": "billing.credit_grant",
  "amount": {
    "monetary": {
      "currency": "usd",
      "value": 1000
    },
    "type": "monetary"
  },
  "applicability_config": {
    "scope": {
      "price_type": "metered"
    }
  },
  "category": "paid",
  "created": 1726620803,
  "customer": "cus_QrvQguzkIK8zTj",
  "effective_at": 1729297860,
  "expires_at": null,
  "livemode": false,
  "metadata": {},
  "name": "Purchased Credits",
  "priority": 50,
  "test_clock": null,
  "updated": 1726620803,
  "voided_at": null
}
```