# The Balance object

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `available` (array of objects)
  Available funds that you can transfer or pay out automatically by Stripe or explicitly through the [Transfers API](#transfers) or [Payouts API](#payouts). You can find the available balance for each currency and payment type in the `source_types` property.

  - `available.amount` (integer)
    Balance amount.

  - `available.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `available.source_types` (nullable object)
    Breakdown of balance by source types. Funds coming from certain source / payment method types must be shown separately. All payment methods that do not have this restriction will be combined with the `card` source type balance.

    - `available.source_types.bank_account` (nullable integer)
      Amount coming from [legacy US ACH payments](https://docs.stripe.com/ach-deprecated).

    - `available.source_types.card` (nullable integer)
      Amount coming from most payment methods, including cards as well as [non-legacy bank debits](https://docs.stripe.com/payments/bank-debits).

    - `available.source_types.fpx` (nullable integer)
      Amount coming from [FPX](https://docs.stripe.com/payments/fpx), a Malaysian payment method.

- `connect_reserved` (nullable array of objects)
  Funds held due to negative balances on connected accounts where [account.controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `application`, which includes Custom accounts. You can find the connect reserve balance for each currency and payment type in the `source_types` property.

  - `connect_reserved.amount` (integer)
    Balance amount.

  - `connect_reserved.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `connect_reserved.source_types` (nullable object)
    Breakdown of balance by source types. Funds coming from certain source / payment method types must be shown separately. All payment methods that do not have this restriction will be combined with the `card` source type balance.

    - `connect_reserved.source_types.bank_account` (nullable integer)
      Amount coming from [legacy US ACH payments](https://docs.stripe.com/ach-deprecated).

    - `connect_reserved.source_types.card` (nullable integer)
      Amount coming from most payment methods, including cards as well as [non-legacy bank debits](https://docs.stripe.com/payments/bank-debits).

    - `connect_reserved.source_types.fpx` (nullable integer)
      Amount coming from [FPX](https://docs.stripe.com/payments/fpx), a Malaysian payment method.

- `instant_available` (nullable array of objects)
  Funds that you can pay out using Instant Payouts.

  - `instant_available.amount` (integer)
    Balance amount.

  - `instant_available.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `instant_available.net_available` (nullable array of objects)
    Breakdown of balance by destination.

    - `instant_available.net_available.amount` (integer)
      Net balance amount, subtracting fees from platform-set pricing.

    - `instant_available.net_available.destination` (string)
      ID of the external account for this net balance (not expandable).

    - `instant_available.net_available.source_types` (nullable object)
      Breakdown of balance by source types. Funds coming from certain source / payment method types must be shown separately. All payment methods that do not have this restriction will be combined with the `card` source type balance.

      - `instant_available.net_available.source_types.bank_account` (nullable integer)
        Amount coming from [legacy US ACH payments](https://docs.stripe.com/ach-deprecated).

      - `instant_available.net_available.source_types.card` (nullable integer)
        Amount coming from most payment methods, including cards as well as [non-legacy bank debits](https://docs.stripe.com/payments/bank-debits).

      - `instant_available.net_available.source_types.fpx` (nullable integer)
        Amount coming from [FPX](https://docs.stripe.com/payments/fpx), a Malaysian payment method.

  - `instant_available.source_types` (nullable object)
    Breakdown of balance by source types. Funds coming from certain source / payment method types must be shown separately. All payment methods that do not have this restriction will be combined with the `card` source type balance.

    - `instant_available.source_types.bank_account` (nullable integer)
      Amount coming from [legacy US ACH payments](https://docs.stripe.com/ach-deprecated).

    - `instant_available.source_types.card` (nullable integer)
      Amount coming from most payment methods, including cards as well as [non-legacy bank debits](https://docs.stripe.com/payments/bank-debits).

    - `instant_available.source_types.fpx` (nullable integer)
      Amount coming from [FPX](https://docs.stripe.com/payments/fpx), a Malaysian payment method.

- `issuing` (nullable object)
  Funds that you can spend on your [Issued Cards](#issuing/cards).

  - `issuing.available` (array of objects)
    Funds that are available for use.

    - `issuing.available.amount` (integer)
      Balance amount.

    - `issuing.available.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `issuing.available.source_types` (nullable object)
      Breakdown of balance by source types. Funds coming from certain source / payment method types must be shown separately. All payment methods that do not have this restriction will be combined with the `card` source type balance.

      - `issuing.available.source_types.bank_account` (nullable integer)
        Amount coming from [legacy US ACH payments](https://docs.stripe.com/ach-deprecated).

      - `issuing.available.source_types.card` (nullable integer)
        Amount coming from most payment methods, including cards as well as [non-legacy bank debits](https://docs.stripe.com/payments/bank-debits).

      - `issuing.available.source_types.fpx` (nullable integer)
        Amount coming from [FPX](https://docs.stripe.com/payments/fpx), a Malaysian payment method.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `pending` (array of objects)
  Funds that aren’t available in the balance yet. You can find the pending balance for each currency and each payment type in the `source_types` property.

  - `pending.amount` (integer)
    Balance amount.

  - `pending.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `pending.source_types` (nullable object)
    Breakdown of balance by source types. Funds coming from certain source / payment method types must be shown separately. All payment methods that do not have this restriction will be combined with the `card` source type balance.

    - `pending.source_types.bank_account` (nullable integer)
      Amount coming from [legacy US ACH payments](https://docs.stripe.com/ach-deprecated).

    - `pending.source_types.card` (nullable integer)
      Amount coming from most payment methods, including cards as well as [non-legacy bank debits](https://docs.stripe.com/payments/bank-debits).

    - `pending.source_types.fpx` (nullable integer)
      Amount coming from [FPX](https://docs.stripe.com/payments/fpx), a Malaysian payment method.

- `refund_and_dispute_prefunding` (nullable object)
  Funds to cover future refunds, disputes, or a negative balance.

  - `refund_and_dispute_prefunding.available` (array of objects)
    Funds that are available for use.

    - `refund_and_dispute_prefunding.available.amount` (integer)
      Balance amount.

    - `refund_and_dispute_prefunding.available.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `refund_and_dispute_prefunding.available.source_types` (nullable object)
      Breakdown of balance by source types. Funds coming from certain source / payment method types must be shown separately. All payment methods that do not have this restriction will be combined with the `card` source type balance.

      - `refund_and_dispute_prefunding.available.source_types.bank_account` (nullable integer)
        Amount coming from [legacy US ACH payments](https://docs.stripe.com/ach-deprecated).

      - `refund_and_dispute_prefunding.available.source_types.card` (nullable integer)
        Amount coming from most payment methods, including cards as well as [non-legacy bank debits](https://docs.stripe.com/payments/bank-debits).

      - `refund_and_dispute_prefunding.available.source_types.fpx` (nullable integer)
        Amount coming from [FPX](https://docs.stripe.com/payments/fpx), a Malaysian payment method.

  - `refund_and_dispute_prefunding.pending` (array of objects)
    Funds that are pending

    - `refund_and_dispute_prefunding.pending.amount` (integer)
      Balance amount.

    - `refund_and_dispute_prefunding.pending.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `refund_and_dispute_prefunding.pending.source_types` (nullable object)
      Breakdown of balance by source types. Funds coming from certain source / payment method types must be shown separately. All payment methods that do not have this restriction will be combined with the `card` source type balance.

      - `refund_and_dispute_prefunding.pending.source_types.bank_account` (nullable integer)
        Amount coming from [legacy US ACH payments](https://docs.stripe.com/ach-deprecated).

      - `refund_and_dispute_prefunding.pending.source_types.card` (nullable integer)
        Amount coming from most payment methods, including cards as well as [non-legacy bank debits](https://docs.stripe.com/payments/bank-debits).

      - `refund_and_dispute_prefunding.pending.source_types.fpx` (nullable integer)
        Amount coming from [FPX](https://docs.stripe.com/payments/fpx), a Malaysian payment method.

### The Balance object

```json
{
  "object": "balance",
  "available": [
    {
      "amount": 666670,
      "currency": "usd",
      "source_types": {
        "card": 666670
      }
    }
  ],
  "connect_reserved": [
    {
      "amount": 0,
      "currency": "usd"
    }
  ],
  "livemode": false,
  "pending": [
    {
      "amount": 61414,
      "currency": "usd",
      "source_types": {
        "card": 61414
      }
    }
  ]
}
```