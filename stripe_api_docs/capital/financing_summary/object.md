# The Financing Summary object

- `object` (string)
  The object type: financing_summary

- `details` (nullable object)
  Additional information about the financing summary. Describes currency, advance amount,
  fee amount, withhold rate, remaining amount, paid amount, current repayment interval,
  repayment start date, and advance payout date.

  - `details.advance_amount` (integer)
    Amount of financing offered, in minor units. For example, $1,000 USD will be represented as 100000.

  - `details.advance_paid_out_at` (nullable float)
    The time at which the funds were paid out to the connected account’s Stripe balance. Given in milliseconds since unix epoch.

  - `details.currency` (string)
    Currency that the financing offer is transacted in. For example, `usd`.

  - `details.current_repayment_interval` (nullable object)
    The chronologically current repayment interval for the financing offer.

    - `details.current_repayment_interval.due_at` (float)
      The time at which the minimum payment amount will be due. If not met through withholding, the Connected account’s linked bank account or account balance will be debited.
      Given in seconds since unix epoch.

    - `details.current_repayment_interval.paid_amount` (nullable integer)
      The amount that has already been paid in the current repayment interval, in minor units. For example, $100 USD will be represented as 10000.

    - `details.current_repayment_interval.remaining_amount` (integer)
      The amount that is yet to be paid in the current repayment interval, in minor units. For example, $100 USD will be represented as 10000.

  - `details.fee_amount` (integer)
    Fixed fee amount, in minor units. For example, $100 USD will be represented as 10000.

  - `details.paid_amount` (integer)
    The amount the Connected account has paid toward the financing debt so far, in minor units. For example, $1,000 USD will be represented as 100000.

  - `details.remaining_amount` (integer)
    The balance remaining to be paid on the financing, in minor units. For example, $1,000 USD will be represented as 100000.

  - `details.repayments_begin_at` (nullable float)
    The time at which Capital will begin withholding from payments. Given in seconds since unix epoch.

  - `details.withhold_rate` (float)
    Per-transaction rate at which Stripe will withhold funds to repay the financing.

- `financing_offer` (nullable string)
  The Financing Offer ID this Financing Summary corresponds to

- `status` (nullable enum)
  Status of the Connected Account’s financing. [/v1/capital/financing_summary](https://docs.stripe.com/docs/api/capital/financing_summary.md) will only return `details` for `paid_out` financing.

  The Connected account has an accepted financing offer.

  A financing offer has been marketed to the Connected account, but the account has not yet accepted.

  The Connected account does not have any active financing.

### The Financing Summary object

```json
{
  "object": "capital.financing_summary",
  "details": {
    "advance_amount": 100000,
    "advance_paid_out_at": 1688424277.0578003,
    "currency": "usd",
    "current_repayment_interval": null,
    "fee_amount": 10000,
    "paid_amount": 100263,
    "remaining_amount": 9737,
    "repayments_begin_at": 1688424277.0577993,
    "withhold_rate": 0.05
  },
  "financing_offer": "financingoffer_1NPvU12eZvKYlo2CotjdGRzu",
  "status": "accepted"
}
```