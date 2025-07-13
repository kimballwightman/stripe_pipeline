# The Token object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `bank_account` (nullable object)
  Hash describing the bank account.

  - `bank_account.id` (string)
    Unique identifier for the object.

  - `bank_account.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `bank_account.account_holder_name` (nullable string)
    The name of the person or business that owns the bank account.

  - `bank_account.account_holder_type` (nullable string)
    The type of entity that holds the account. This can be either `individual` or `company`.

  - `bank_account.account_type` (nullable string)
    The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`.

  - `bank_account.bank_name` (nullable string)
    Name of the bank associated with the routing number (e.g., `WELLS FARGO`).

  - `bank_account.country` (string)
    Two-letter ISO code representing the country the bank account is located in.

  - `bank_account.currency` (enum)
    Three-letter [ISO code for the currency](https://stripe.com/docs/payouts) paid out to the bank account.

  - `bank_account.fingerprint` (nullable string)
    Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

  - `bank_account.last4` (string)
    The last four digits of the bank account number.

  - `bank_account.routing_number` (nullable string)
    The routing transit number for the bank account.

  - `bank_account.status` (string)
    For bank accounts, possible values are `new`, `validated`, `verified`, `verification_failed`, or `errored`. A bank account that hasn’t had any activity or validation performed is `new`. If Stripe can determine that the bank account exists, its status will be `validated`. Note that there often isn’t enough information to know (e.g., for smaller credit unions), and the validation is not always run. If customer bank account verification has succeeded, the bank account status will be `verified`. If the verification failed for any reason, such as microdeposit failure, the status will be `verification_failed`. If a payout sent to this bank account fails, we’ll set the status to `errored` and will not continue to send [scheduled payouts](https://stripe.com/docs/payouts#payout-schedule) until the bank details are updated.

    For external accounts, possible values are `new`, `errored` and `verification_failed`. If a payout fails, the status is set to `errored` and scheduled payouts are stopped until account details are updated. In the US and India, if we can’t [verify the owner of the bank account](https://support.stripe.com/questions/bank-account-ownership-verification), we’ll set the status to `verification_failed`. Other validations aren’t run against external accounts because they’re only used for payouts. This means the other statuses don’t apply.

- `card` (nullable object)
  Hash describing the card used to make the charge.

  - `card.id` (string)
    Unique identifier for the object.

  - `card.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `card.address_city` (nullable string)
    City/District/Suburb/Town/Village.

  - `card.address_country` (nullable string)
    Billing address country, if provided when creating card.

  - `card.address_line1` (nullable string)
    Address line 1 (Street address/PO Box/Company name).

  - `card.address_line1_check` (nullable string)
    If `address_line1` was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`.

  - `card.address_line2` (nullable string)
    Address line 2 (Apartment/Suite/Unit/Building).

  - `card.address_state` (nullable string)
    State/County/Province/Region.

  - `card.address_zip` (nullable string)
    ZIP or postal code.

  - `card.address_zip_check` (nullable string)
    If `address_zip` was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`.

  - `card.brand` (string)
    Card brand. Can be `American Express`, `Diners Club`, `Discover`, `Eftpos Australia`, `Girocard`, `JCB`, `MasterCard`, `UnionPay`, `Visa`, or `Unknown`.

  - `card.country` (nullable string)
    Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

  - `card.currency` (nullable enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `card.cvc_check` (nullable string)
    If a CVC was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`. A result of unchecked indicates that CVC was provided but hasn’t been checked yet. Checks are typically performed when attaching a card to a Customer object, or when creating a charge. For more details, see [Check if a card is valid without a charge](https://support.stripe.com/questions/check-if-a-card-is-valid-without-a-charge).

  - `card.dynamic_last4` (nullable string)
    (For tokenized numbers only.) The last four digits of the device account number.

  - `card.exp_month` (integer)
    Two-digit number representing the card’s expiration month.

  - `card.exp_year` (integer)
    Four-digit number representing the card’s expiration year.

  - `card.fingerprint` (nullable string)
    Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

    *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

  - `card.funding` (string)
    Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

  - `card.last4` (string)
    The last four digits of the card.

  - `card.metadata` (nullable object)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

  - `card.name` (nullable string)
    Cardholder name.

  - `card.networks` (nullable object)
    Contains information about card networks used to process the payment.

    - `card.networks.preferred` (nullable string)
      The preferred network for co-branded cards. Can be `cartes_bancaires`, `mastercard`, `visa` or `invalid_preference` if requested network is not valid for the card.

  - `card.regulated_status` (nullable enum)
    Status of a card based on the card issuer.

    The card falls under a regulated account range.

    The card does not fall under a regulated account range.

  - `card.tokenization_method` (nullable string)
    If the card number is tokenized, this is the method that was used. Can be `android_pay` (includes Google Pay), `apple_pay`, `masterpass`, `visa_checkout`, or null.

- `client_ip` (nullable string)
  IP address of the client that generates the token.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `description` (nullable string)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `type` (string)
  Type of the token: `account`, `bank_account`, `card`, or `pii`.

- `used` (boolean)
  Determines if you have already used this token (you can only use tokens once).

### The Token object

```json
{
  "id": "tok_1N3T00LkdIwHu7ixt44h1F8k",
  "object": "token",
  "card": {
    "id": "card_1N3T00LkdIwHu7ixRdxpVI1Q",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "US",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2026,
    "fingerprint": "mToisGZ01V71BCos",
    "funding": "credit",
    "last4": "4242",
    "metadata": {},
    "name": null,
    "tokenization_method": null,
    "wallet": null
  },
  "client_ip": "52.35.78.6",
  "created": 1683071568,
  "livemode": false,
  "type": "card",
  "used": false
}
```