# The Card object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `account` (nullable string)
  The account this card belongs to. Only applicable on Accounts (not customers or recipients) This property is only available when returned as an [External Account](https://docs.stripe.com/api/external_account_cards/object.md) where [controller.is_controller](https://docs.stripe.com/api/accounts/object.md#account_object-controller-is_controller) is `true`.

- `address_city` (nullable string)
  City/District/Suburb/Town/Village.

- `address_country` (nullable string)
  Billing address country, if provided when creating card.

- `address_line1` (nullable string)
  Address line 1 (Street address/PO Box/Company name).

- `address_line1_check` (nullable string)
  If `address_line1` was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`.

- `address_line2` (nullable string)
  Address line 2 (Apartment/Suite/Unit/Building).

- `address_state` (nullable string)
  State/County/Province/Region.

- `address_zip` (nullable string)
  ZIP or postal code.

- `address_zip_check` (nullable string)
  If `address_zip` was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`.

- `allow_redisplay` (nullable enum)
  This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to “unspecified”.

  Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

  Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

  This is the default value for payment methods where `allow_redisplay` wasn’t set.

- `available_payout_methods` (nullable array of enums)
  A set of available payout methods for this card. Only values from this set should be passed as the `method` when creating a payout.

- `brand` (string)
  Card brand. Can be `American Express`, `Diners Club`, `Discover`, `Eftpos Australia`, `Girocard`, `JCB`, `MasterCard`, `UnionPay`, `Visa`, or `Unknown`.

- `country` (nullable string)
  Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

- `currency` (nullable enum)
  Three-letter [ISO code for currency](https://www.iso.org/iso-4217-currency-codes.html) in lowercase. Must be a [supported currency](https://docs.stripe.com/currencies). Only applicable on accounts (not customers or recipients). The card can be used as a transfer destination for funds in this currency. This property is only available when returned as an [External Account](https://docs.stripe.com/api/external_account_cards/object.md) where [controller.is_controller](https://docs.stripe.com/api/accounts/object.md#account_object-controller-is_controller) is `true`.

- `customer` (nullable string)
  The customer that this card belongs to. This attribute will not be in the card object if the card belongs to an account or recipient instead.

- `cvc_check` (nullable string)
  If a CVC was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`. A result of unchecked indicates that CVC was provided but hasn’t been checked yet. Checks are typically performed when attaching a card to a Customer object, or when creating a charge. For more details, see [Check if a card is valid without a charge](https://support.stripe.com/questions/check-if-a-card-is-valid-without-a-charge).

- `dynamic_last4` (nullable string)
  (For tokenized numbers only.) The last four digits of the device account number.

- `exp_month` (integer)
  Two-digit number representing the card’s expiration month.

- `exp_year` (integer)
  Four-digit number representing the card’s expiration year.

- `fingerprint` (nullable string)
  Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

  *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

- `funding` (string)
  Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

- `last4` (string)
  The last four digits of the card.

- `metadata` (nullable object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `name` (nullable string)
  Cardholder name.

- `regulated_status` (nullable enum)
  Status of a card based on the card issuer.

  The card falls under a regulated account range.

  The card does not fall under a regulated account range.

- `tokenization_method` (nullable string)
  If the card number is tokenized, this is the method that was used. Can be `android_pay` (includes Google Pay), `apple_pay`, `masterpass`, `visa_checkout`, or null.

### The Card object

```json
{
  "id": "card_1MvoiELkdIwHu7ixOeFGbN9D",
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
  "customer": "cus_NhD8HD2bY8dP3V",
  "cvc_check": null,
  "dynamic_last4": null,
  "exp_month": 4,
  "exp_year": 2024,
  "fingerprint": "mToisGZ01V71BCos",
  "funding": "credit",
  "last4": "4242",
  "metadata": {},
  "name": null,
  "tokenization_method": null,
  "wallet": null
}
```