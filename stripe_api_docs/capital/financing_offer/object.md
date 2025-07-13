# The Financing offer object

- `id` (string)
  A unique identifier for the financing object.

- `object` (string)
  The object type: financing_offer.

- `accepted_terms` (nullable object)
  Information about the current financing object. Describes currency, advance amount,
  fee amount, withhold rate, and fee discount of previous financing.

  - `accepted_terms.advance_amount` (integer)
    Amount of financing offered, in minor units. For example, $1,000 USD will be represented as 100000.

  - `accepted_terms.currency` (string)
    Currency that the financing offer is transacted in. For example, `usd`.

  - `accepted_terms.fee_amount` (integer)
    Fixed fee amount, in minor units. For example, $100 USD will be represented as 10000.

  - `accepted_terms.previous_financing_fee_discount_amount` (nullable integer)
    Populated when the `product_type` of the `financingoffer` is `refill`.
    Represents the discount amount on remaining premium for the existing loan at payout time.

  - `accepted_terms.withhold_rate` (float)
    Per-transaction rate at which Stripe will withhold funds to repay the financing.

- `account` (string)
  The ID of the merchant associated with this financing object.

- `charged_off_at` (nullable timestamp)
  The time at which this financing offer was charged off, if applicable. Given in seconds since unix epoch.

- `created` (integer)
  Time at which the offer was created. Given in seconds since unix epoch.

- `expires_after` (float)
  Time at which the offer expires. Given in seconds since unix epoch.

- `financing_type` (nullable enum)
  The type of financing being offered.

  Capital’s Merchant Cash Advance program.

  Capital’s flex loan offering. See the [integration guide](https://docs.stripe.com/docs/capital/platforms.md) for more information.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (nullable object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `offered_terms` (nullable object)
  Information about the financing offer. Describes currency, offered advance amount,
  offered fee amount, campaign type, withhold rate, and fee discount rate of previous
  financing.

  - `offered_terms.advance_amount` (integer)
    Amount of financing offered, in minor units. For example, $1,000 USD will be represented as 100000.

  - `offered_terms.campaign_type` (enum)
    Describes the type of user the offer is being extended to.

    A user who has never been eligible for Capital before.

    A user who has been offered financing through Capital before, but never accepted an offer.

    A user who has already accepted or fully repaid a loan, and is receiving another offer.

  - `offered_terms.currency` (string)
    Currency that the financing offer is transacted in. For example, `usd`.

  - `offered_terms.fee_amount` (integer)
    Fixed fee amount, in minor units. For example, $100 USD will be represented as 10000.

  - `offered_terms.previous_financing_fee_discount_rate` (nullable float)
    Populated when the `product_type` of the `financingoffer` is `refill`.
    Represents the discount rate percentage on remaining fee on the existing loan. When the `financing_offer`
    is paid out, the `previous_financing_fee_discount_amount` will be computed as the multiple of this rate
    and the remaining fee.

  - `offered_terms.withhold_rate` (float)
    Per-transaction rate at which Stripe will withhold funds to repay the financing.

- `product_type` (nullable enum)
  Financing product identifier.

  A “refill” financing offer extended through Stripe Capital. Refills are a form of discounted refinancing. See
  the [integration guide](https://docs.stripe.com/docs/capital/platforms.md#refills) for more information.

  A standard financing offer extended through Stripe Capital.

- `replacement` (nullable string)
  The ID of the financing offer that replaced this offer.

- `replacement_for` (nullable string)
  The ID of the financing offer that this offer is a replacement for.

- `status` (enum)
  The current status of the offer.

  Set once an offer has been accepted by the Connected account.

  Set when the Connected account has reached out to Capital’s servicing team within 48 hours of acceptance and requested cancellation of their offer.

  Set when the financing offer has fully repaid. This status is no longer in use. See `fully_repaid` instead.

  Once an offer has been delivered, mark it so using the [mark_delivered](https://docs.stripe.com/docs/api/capital/financing_offers/mark_delivered.md) endpoint.

  Set when the financing offer has expired, usually 30 days after creation.

  Set when the financing offer has been fully repaid.

  Set once an offer has been paid out to the Connected account.

  Set when Capital’s servicing team has rejected the application for financing. The Connected account receives an
  email with the reason for rejection.

  Set when the financing offer has been replaced.

  All offers begin in this state. A financing offer must be delivered to its Connected account using approved
  marketing materials.

- `type` (nullable enum)
  See [financing_type](https://docs.stripe.com/docs/api/capital/connect_financing_object.md#financing_offer_object-financing_type).

### The Financing offer object

```json
{
  "id": "financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh",
  "object": "capital.financing_offer",
  "account": "acct_1NPvKgBY65lDjjDk",
  "created": 1688423699,
  "expires_after": 1690934400,
  "financing_type": "flex_loan",
  "livemode": true,
  "offered_terms": {
    "advance_amount": 10000,
    "campaign_type": "newly_eligible_user",
    "currency": "usd",
    "fee_amount": 1000,
    "previous_financing_fee_discount_rate": null,
    "withhold_rate": 0.05
  },
  "product_type": "standard",
  "status": "undelivered"
}
```