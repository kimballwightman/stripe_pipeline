# The Payout object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  The amount (in ) that transfers to your bank account or debit card.

- `application_fee` (nullable string)
  The application fee (if any) for the payout. [See the Connect documentation](https://docs.stripe.com/docs/connect/instant-payouts.md#monetization-and-fees) for details.

- `application_fee_amount` (nullable integer)
  The amount of the application fee (if any) requested for the payout. [See the Connect documentation](https://docs.stripe.com/docs/connect/instant-payouts.md#monetization-and-fees) for details.

- `arrival_date` (timestamp)
  Date that you can expect the payout to arrive in the bank. This factors in delays to account for weekends or bank holidays.

- `automatic` (boolean)
  Returns `true` if the payout is created by an [automated payout schedule](https://docs.stripe.com/docs/payouts.md#payout-schedule) and `false` if it’s [requested manually](https://stripe.com/docs/payouts#manual-payouts).

- `balance_transaction` (nullable string)
  ID of the balance transaction that describes the impact of this payout on your account balance.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `description` (nullable string)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `destination` (nullable string)
  ID of the bank account or card the payout is sent to.

- `failure_balance_transaction` (nullable string)
  If the payout fails or cancels, this is the ID of the balance transaction that reverses the initial balance transaction and returns the funds from the failed payout back in your balance.

- `failure_code` (nullable enum)
  Error code that provides a reason for a payout failure, if available.

  The bank account has been closed.

  The bank account has been frozen.

  The bank account has restrictions on either the type, or the number, of payouts allowed. This normally indicates that the bank account is a savings or other non-checking account.

  The destination bank account is no longer valid because its branch has changed ownership.

  The bank could not process this payout.

  Debit transactions are not approved on the bank account. (Stripe requires bank accounts to be set up for both credit and debit payouts.)

  The bank has declined this transfer. Please contact the bank before retrying.

  Your bank notified us that the bank account holder address on file is incorrect.

  Your bank notified us that the bank account holder name on file is incorrect.

  Your bank notified us that the bank account holder tax ID on file is incorrect.

  Your bank notified us that the bank account type on file is incorrect. This value can only be checking or savings in most countries. In Japan, it can only be futsu or toza.

  Your Stripe account has insufficient funds to cover the payout.

  The routing number seems correct, but the account number is invalid.

  Your bank notified us that the bank account number is too long.

  The bank was unable to process this payout because of its currency. This is probably because the bank account cannot accept payments in that currency.

  The bank account details on file are probably incorrect. No bank account could be located with those details.

  The bank no longer supports payouts to this card.

- `failure_message` (nullable string)
  Message that provides the reason for a payout failure, if available.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (nullable object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `method` (string)
  The method used to send this payout, which can be `standard` or `instant`. `instant` is supported for payouts to debit cards and bank accounts in certain countries. Learn more about [bank support for Instant Payouts](https://stripe.com/docs/payouts/instant-payouts-banks).

- `original_payout` (nullable string)
  If the payout reverses another, this is the ID of the original payout.

- `reconciliation_status` (enum)
  If `completed`, you can use the [Balance Transactions API](https://docs.stripe.com/docs/api/balance_transactions/list.md#balance_transaction_list-payout) to list all balance transactions that are paid out in this payout.

  The Balance Transactions paid out in this payout. You can query it with the [Balance Transactions API](https://docs.stripe.com/docs/api/balance_transactions/list.md#balance_transaction_list-payout).

  You can query the Balance Transactions paid out in this payout soon.

  We don’t support listing Balance Transactions for this payout. We only support this for standard automatic payouts.

- `reversed_by` (nullable string)
  If the payout reverses, this is the ID of the payout that reverses this payout.

- `source_type` (string)
  The source balance this payout came from, which can be one of the following: `card`, `fpx`, or `bank_account`.

- `statement_descriptor` (nullable string)
  Extra information about a payout that displays on the user’s bank statement.

- `status` (string)
  Current status of the payout: `paid`, `pending`, `in_transit`, `canceled` or `failed`. A payout is `pending` until it’s submitted to the bank, when it becomes `in_transit`. The status changes to `paid` if the transaction succeeds, or to `failed` or `canceled` (within 5 business days). Some payouts that fail might initially show as `paid`, then change to `failed`.

- `trace_id` (nullable object)
  A value that generates from the beneficiary’s bank that allows users to track payouts with their bank. Banks might call this a “reference number” or something similar.

  - `trace_id.status` (string)
    Possible values are `pending`, `supported`, and `unsupported`. When `payout.status` is `pending` or `in_transit`, this will be `pending`. When the payout transitions to `paid`, `failed`, or `canceled`, this status will become `supported` or `unsupported` shortly after in most cases. In some cases, this may appear as `pending` for up to 10 days after `arrival_date` until transitioning to `supported` or `unsupported`.

  - `trace_id.value` (nullable string)
    The trace ID value if `trace_id.status` is `supported`, otherwise `nil`.

- `type` (enum)
  Can be `bank_account` or `card`.

### The Payout object

```json
{
  "id": "po_1OaFDbEcg9tTZuTgNYmX0PKB",
  "object": "payout",
  "amount": 1100,
  "arrival_date": 1680652800,
  "automatic": false,
  "balance_transaction": "txn_1OaFDcEcg9tTZuTgYMR25tSe",
  "created": 1680648691,
  "currency": "usd",
  "description": null,
  "destination": "ba_1MtIhL2eZvKYlo2CAElKwKu2",
  "failure_balance_transaction": null,
  "failure_code": null,
  "failure_message": null,
  "livemode": false,
  "metadata": {},
  "method": "standard",
  "original_payout": null,
  "reconciliation_status": "not_applicable",
  "reversed_by": null,
  "source_type": "card",
  "statement_descriptor": null,
  "status": "pending",
  "type": "bank_account"
}
```