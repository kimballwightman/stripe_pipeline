# The Cash Balance Transaction object

## Attributes

### id
**string**  
Unique identifier for the object.

### object
**string**  
String representing the object's type. Objects of the same type share the same value.

### adjusted_for_overdraft
**nullable dictionary**  
If this is a `type=adjusted_for_overdraft` transaction, contains information about what caused the overdraft, which triggered this transaction.

#### adjusted_for_overdraft.balance_transaction
**string**  
*Expandable*  
The Balance Transaction that corresponds to funds taken out of your Stripe balance.

#### adjusted_for_overdraft.linked_transaction
**string**  
*Expandable*  
The Cash Balance Transaction that brought the customer balance negative, triggering the clawback of funds.

### applied_to_payment
**nullable dictionary**  
If this is a `type=applied_to_payment` transaction, contains information about how funds were applied.

#### applied_to_payment.payment_intent
**string**  
*Expandable*  
The Payment Intent that funds were applied to.

### created
**timestamp**  
Time at which the object was created. Measured in seconds since the Unix epoch.

### currency
**string**  
Three-letter ISO currency code, in lowercase. Must be a supported currency.

### customer
**string**  
*Expandable*  
The customer whose available cash balance changed as a result of this transaction.

### ending_balance
**integer**  
The total available cash balance for the specified currency after this transaction was applied. Represented in the smallest currency unit.

### funded
**nullable dictionary**  
If this is a `type=funded` transaction, contains information about the funding.

#### funded.bank_transfer
**dictionary**  
Information about the bank transfer that funded the customer's cash balance.

##### funded.bank_transfer.eu_bank_transfer
**nullable dictionary**  
EU-specific details of the bank transfer.

###### funded.bank_transfer.eu_bank_transfer.bic
**nullable string**  
The BIC of the bank of the sender of the funding.

###### funded.bank_transfer.eu_bank_transfer.iban_last4
**nullable string**  
The last 4 digits of the IBAN of the sender of the funding.

###### funded.bank_transfer.eu_bank_transfer.sender_name
**nullable string**  
The full name of the sender, as supplied by the sending bank.

##### funded.bank_transfer.gb_bank_transfer
**nullable dictionary**  
UK-specific details of the bank transfer.

###### funded.bank_transfer.gb_bank_transfer.account_number_last4
**nullable string**  
The last 4 digits of the account number of the sender of the funding.

###### funded.bank_transfer.gb_bank_transfer.sender_name
**nullable string**  
The full name of the sender, as supplied by the sending bank.

###### funded.bank_transfer.gb_bank_transfer.sort_code
**nullable string**  
The sort code of the bank of the sender of the funding

##### funded.bank_transfer.jp_bank_transfer
**nullable dictionary**  
Japan-specific details of the bank transfer.

###### funded.bank_transfer.jp_bank_transfer.sender_bank
**nullable string**  
The name of the bank of the sender of the funding.

###### funded.bank_transfer.jp_bank_transfer.sender_branch
**nullable string**  
The name of the bank branch of the sender of the funding.

###### funded.bank_transfer.jp_bank_transfer.sender_name
**nullable string**  
The full name of the sender, as supplied by the sending bank.

##### funded.bank_transfer.reference
**nullable string**  
The user-supplied reference field on the bank transfer.

##### funded.bank_transfer.type
**enum**  
The funding method type used to fund the customer balance. Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.

**Possible enum values:**
- `eu_bank_transfer` - A bank transfer of type eu_bank_transfer
- `gb_bank_transfer` - A bank transfer of type gb_bank_transfer
- `jp_bank_transfer` - A bank transfer of type jp_bank_transfer
- `mx_bank_transfer` - A bank transfer of type mx_bank_transfer
- `us_bank_transfer` - A bank transfer of type us_bank_transfer

##### funded.bank_transfer.us_bank_transfer
**nullable dictionary**  
US-specific details of the bank transfer.

###### funded.bank_transfer.us_bank_transfer.network
**nullable enum**  
The banking network used for this funding.

**Possible enum values:**
- `ach` - Banking network is ACH
- `domestic_wire_us` - Banking network is US Domestic Wire
- `swift` - Banking network is SWIFT

###### funded.bank_transfer.us_bank_transfer.sender_name
**nullable string**  
The full name of the sender, as supplied by the sending bank.

### livemode
**boolean**  
Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

### net_amount
**integer**  
The amount by which the cash balance changed, represented in the smallest currency unit. A positive value represents funds being added to the cash balance, a negative value represents funds being removed from the cash balance.

### refunded_from_payment
**nullable dictionary**  
If this is a `type=refunded_from_payment` transaction, contains information about the source of the refund.

#### refunded_from_payment.refund
**string**  
*Expandable*  
The Refund that moved these funds into the customer's cash balance.

### transferred_to_balance
**nullable dictionary**  
If this is a `type=transferred_to_balance` transaction, contains the balance transaction linked to the transfer.

#### transferred_to_balance.balance_transaction
**string**  
*Expandable*  
The Balance Transaction that corresponds to funds transferred to your Stripe balance.

### type
**enum**  
The type of the cash balance transaction. New types may be added in future. See Customer Balance to learn more about these types.

**Possible enum values:**
- `adjusted_for_overdraft` - A cash balance transaction type: adjusted_for_overdraft
- `applied_to_payment` - A cash balance transaction type: applied_to_payment
- `funded` - A cash balance transaction type: funded
- `funding_reversed` - A cash balance transaction type: funding_reversed
- `refunded_from_payment` - A cash balance transaction type: refunded_from_payment
- `return_canceled` - A cash balance transaction type: return_canceled
- `return_initiated` - A cash balance transaction type: return_initiated
- `transferred_to_balance` - A cash balance transaction type: transferred_to_balance
- `unapplied_from_payment` - A cash balance transaction type: unapplied_from_payment

### unapplied_from_payment
**nullable dictionary**  
If this is a `type=unapplied_from_payment` transaction, contains information about how funds were unapplied.

#### unapplied_from_payment.payment_intent
**string**  
*Expandable*  
The Payment Intent that funds were unapplied from.

## The Cash Balance Transaction object

```json
{
  "id": "ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF",
  "object": "customer_cash_balance_transaction",
  "created": 1690829143,
  "currency": "eur",
  "customer": "cus_9s6XKzkNRiz8i3",
  "ending_balance": 10000,
  "funded": {
    "bank_transfer": {
      "eu_bank_transfer": {
        "bic": "BANKDEAAXXX",
        "iban_last4": "7089",
        "sender_name": "Sample Business GmbH"
      },
      "reference": "Payment for Invoice 28278FC-155",
      "type": "eu_bank_transfer"
    }
  },
  "livemode": false,
  "net_amount": 5000,
  "type": "funded"
}
```