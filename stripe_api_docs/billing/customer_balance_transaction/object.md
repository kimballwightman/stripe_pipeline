# The Customer Balance Transaction object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  The amount of the transaction. A negative value is a credit for the customer’s balance, and a positive value is a debit to the customer’s `balance`.

- `checkout_session` (nullable string)
  The ID of the checkout session (if any) that created the transaction.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `credit_note` (nullable string)
  The ID of the credit note (if any) related to the transaction.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `customer` (string)
  The ID of the customer the transaction belongs to.

- `description` (nullable string)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `ending_balance` (integer)
  The customer’s `balance` after the transaction was applied. A negative value decreases the amount due on the customer’s next invoice. A positive value increases the amount due on the customer’s next invoice.

- `invoice` (nullable string)
  The ID of the invoice (if any) related to the transaction.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (nullable object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `type` (enum)
  Transaction type: `adjustment`, `applied_to_invoice`, `credit_note`, `initial`, `invoice_overpaid`, `invoice_too_large`, `invoice_too_small`, `unspent_receiver_credit`, `unapplied_from_invoice`, `checkout_session_subscription_payment`, or `checkout_session_subscription_payment_canceled`. See the [Customer Balance page](https://docs.stripe.com/docs/billing/customer/balance.md#types) to learn more about transaction types.

  An explicitly created adjustment transaction to debit or credit the credit balance.

  Traces the application of credit against a linked Invoice.

  Traces the customer balance applied to an Invoice to be created for the linked Checkout Session.

  Traces the reversal of an applied balance by the linked Checkout Session. Paired with an earlier ‘checkout_session_subscription_payment‘ transaction.

  Traces the creation of credit to a Credit Note and its associated Invoice.

  The starting value of the customer’s credit balance.

  Credits to the credit balance when an invoice receives payments exceeding the amount due.

  Debits to the credit balance when the amount due on an invoice is greater than Stripe’s maximum chargeable amount and the customer does not have a cash balance.

  Debits to the credit balance when the amount due on an invoice is less than Stripe’s minimum chargeable amount and the customer does not have a cash balance.

  Funds migrated from the legacy customer credit balance.

  Traces the reversal of an applied credit balance from a linked Invoice. Paired with an earlier ‘applied_to_invoice’ transaction.

  Unspent funds in receiver Sources that got automatically charged and credited to the balance.

### The Customer Balance Transaction object

```json
{
  "id": "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI",
  "object": "customer_balance_transaction",
  "amount": -500,
  "created": 1680216086,
  "credit_note": null,
  "currency": "usd",
  "customer": "cus_NcjdgdwZyI9Rj7",
  "description": null,
  "ending_balance": -500,
  "invoice": null,
  "livemode": false,
  "metadata": {},
  "type": "adjustment"
}
```