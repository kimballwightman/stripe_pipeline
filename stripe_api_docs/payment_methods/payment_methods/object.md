# The PaymentMethod object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `acss_debit` (nullable object)
  If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method.

  - `acss_debit.bank_name` (nullable string)
    Name of the bank associated with the bank account.

  - `acss_debit.fingerprint` (nullable string)
    Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

  - `acss_debit.institution_number` (nullable string)
    Institution number of the bank account.

  - `acss_debit.last4` (nullable string)
    Last four digits of the bank account number.

  - `acss_debit.transit_number` (nullable string)
    Transit number of the bank account.

- `affirm` (nullable object)
  If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method.

- `afterpay_clearpay` (nullable object)
  If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method.

- `alipay` (nullable object)
  If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method.

- `allow_redisplay` (nullable enum)
  This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to “unspecified”.

  Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

  Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

  This is the default value for payment methods where `allow_redisplay` wasn’t set.

- `alma` (nullable object)
  If this is a Alma PaymentMethod, this hash contains details about the Alma payment method.

- `amazon_pay` (nullable object)
  If this is a AmazonPay PaymentMethod, this hash contains details about the AmazonPay payment method.

- `au_becs_debit` (nullable object)
  If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account.

  - `au_becs_debit.bsb_number` (nullable string)
    Six-digit number identifying bank and branch associated with this bank account.

  - `au_becs_debit.fingerprint` (nullable string)
    Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

  - `au_becs_debit.last4` (nullable string)
    Last four digits of the bank account number.

- `bacs_debit` (nullable object)
  If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account.

  - `bacs_debit.fingerprint` (nullable string)
    Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

  - `bacs_debit.last4` (nullable string)
    Last four digits of the bank account number.

  - `bacs_debit.sort_code` (nullable string)
    Sort code of the bank account. (e.g., `10-20-30`)

- `bancontact` (nullable object)
  If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method.

- `billie` (nullable object)
  If this is a `billie` PaymentMethod, this hash contains details about the Billie payment method.

- `billing_details` (object)
  Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.

  - `billing_details.address` (nullable object)
    Billing address.

    - `billing_details.address.city` (nullable string)
      City, district, suburb, town, or village.

    - `billing_details.address.country` (nullable string)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `billing_details.address.line1` (nullable string)
      Address line 1 (e.g., street, PO Box, or company name).

    - `billing_details.address.line2` (nullable string)
      Address line 2 (e.g., apartment, suite, unit, or building).

    - `billing_details.address.postal_code` (nullable string)
      ZIP or postal code.

    - `billing_details.address.state` (nullable string)
      State, county, province, or region.

  - `billing_details.email` (nullable string)
    Email address.

  - `billing_details.name` (nullable string)
    Full name.

  - `billing_details.phone` (nullable string)
    Billing phone number (including extension).

  - `billing_details.tax_id` (nullable string)
    Taxpayer identification number. Used only for transactions between LATAM buyers and non-LATAM sellers.

- `blik` (nullable object)
  If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method.

- `boleto` (nullable object)
  If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method.

  - `boleto.tax_id` (string)
    Uniquely identifies the customer tax id (CNPJ or CPF)

- `card` (nullable object)
  If this is a `card` PaymentMethod, this hash contains the user’s card details.

  - `card.brand` (string)
    Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

  - `card.checks` (nullable object)
    Checks on Card address and CVC if provided.

    - `card.checks.address_line1_check` (nullable string)
      If a address line1 was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.

    - `card.checks.address_postal_code_check` (nullable string)
      If a address postal code was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.

    - `card.checks.cvc_check` (nullable string)
      If a CVC was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.

  - `card.country` (nullable string)
    Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

  - `card.display_brand` (nullable string)
    The brand to use when displaying the card, this accounts for customer’s brand choice on dual-branded cards. Can be `american_express`, `cartes_bancaires`, `diners_club`, `discover`, `eftpos_australia`, `interac`, `jcb`, `mastercard`, `union_pay`, `visa`, or `other` and may contain more values in the future.

  - `card.exp_month` (integer)
    Two-digit number representing the card’s expiration month.

  - `card.exp_year` (integer)
    Four-digit number representing the card’s expiration year.

  - `card.fingerprint` (nullable string)
    Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

    *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

  - `card.funding` (string)
    Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

  - `card.generated_from` (nullable object)
    Details of the original PaymentMethod that created this object.

    - `card.generated_from.charge` (nullable string)
      The charge that created this object.

    - `card.generated_from.payment_method_details` (nullable object)
      Transaction-specific details of the payment method used in the payment.

      - `card.generated_from.payment_method_details.card_present` (nullable object)
        This hash contains the snapshot of the `card_present` transaction-specific details which generated this `card` payment method.

        - `card.generated_from.payment_method_details.card_present.amount_authorized` (nullable integer)
          The authorized amount

        - `card.generated_from.payment_method_details.card_present.brand` (nullable string)
          Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

        - `card.generated_from.payment_method_details.card_present.brand_product` (nullable string)
          The [product code](https://stripe.com/docs/card-product-codes) that identifies the specific program or product associated with a card.

        - `card.generated_from.payment_method_details.card_present.capture_before` (nullable timestamp)
          When using manual capture, a future timestamp after which the charge will be automatically refunded if uncaptured.

        - `card.generated_from.payment_method_details.card_present.cardholder_name` (nullable string)
          The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.

        - `card.generated_from.payment_method_details.card_present.country` (nullable string)
          Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

        - `card.generated_from.payment_method_details.card_present.emv_auth_data` (nullable string)
          Authorization response cryptogram.

        - `card.generated_from.payment_method_details.card_present.exp_month` (integer)
          Two-digit number representing the card’s expiration month.

        - `card.generated_from.payment_method_details.card_present.exp_year` (integer)
          Four-digit number representing the card’s expiration year.

        - `card.generated_from.payment_method_details.card_present.fingerprint` (nullable string)
          Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

          *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

        - `card.generated_from.payment_method_details.card_present.funding` (nullable string)
          Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

        - `card.generated_from.payment_method_details.card_present.generated_card` (nullable string)
          ID of a card PaymentMethod generated from the card_present PaymentMethod that may be attached to a Customer for future transactions. Only present if it was possible to generate a card PaymentMethod.

        - `card.generated_from.payment_method_details.card_present.incremental_authorization_supported` (boolean)
          Whether this [PaymentIntent](https://docs.stripe.com/docs/api/payment_intents.md) is eligible for incremental authorizations. Request support using [request_incremental_authorization_support](https://docs.stripe.com/docs/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-request_incremental_authorization_support).

        - `card.generated_from.payment_method_details.card_present.last4` (nullable string)
          The last four digits of the card.

        - `card.generated_from.payment_method_details.card_present.network` (nullable string)
          Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.

        - `card.generated_from.payment_method_details.card_present.network_transaction_id` (nullable string)
          This is used by the financial networks to identify a transaction. Visa calls this the Transaction ID, Mastercard calls this the Trace ID, and American Express calls this the Acquirer Reference Data. This value will be present if it is returned by the financial network in the authorization response, and null otherwise.

        - `card.generated_from.payment_method_details.card_present.offline` (nullable object)
          Details about payments collected offline.

          - `card.generated_from.payment_method_details.card_present.offline.stored_at` (nullable timestamp)
            Time at which the payment was collected while offline

          - `card.generated_from.payment_method_details.card_present.offline.type` (nullable enum)
            The method used to process this payment method offline. Only deferred is allowed.

        - `card.generated_from.payment_method_details.card_present.overcapture_supported` (boolean)
          Defines whether the authorized amount can be over-captured or not

        - `card.generated_from.payment_method_details.card_present.preferred_locales` (nullable array of strings)
          The languages that the issuing bank recommends using for localizing any customer-facing text, as read from the card. Referenced from EMV tag 5F2D, data encoded on the card’s chip.

        - `card.generated_from.payment_method_details.card_present.read_method` (nullable enum)
          How card details were read in this transaction.

          Inserting a chip card into the card reader.

          Tapping a contactless-enabled chip card or mobile wallet.

          Older standard for contactless payments that emulated a magnetic stripe read.

          When inserting a chip card fails three times in a row, fallback to a magnetic stripe read.

          Swiping a card using the magnetic stripe reader.

        - `card.generated_from.payment_method_details.card_present.receipt` (nullable object)
          A collection of fields required to be displayed on receipts. Only required for EMV transactions.

          - `card.generated_from.payment_method_details.card_present.receipt.account_type` (nullable enum)
            The type of account being debited or credited

            A checking account, as when using a debit card

            A credit account, as when using a credit card

            A prepaid account, as when using a debit gift card

            An unknown account

          - `card.generated_from.payment_method_details.card_present.receipt.application_cryptogram` (nullable string)
            The Application Cryptogram, a unique value generated by the card to authenticate the transaction with issuers.

          - `card.generated_from.payment_method_details.card_present.receipt.application_preferred_name` (nullable string)
            The Application Identifier (AID) on the card used to determine which networks are eligible to process the transaction. Referenced from EMV tag 9F12, data encoded on the card’s chip.

          - `card.generated_from.payment_method_details.card_present.receipt.authorization_code` (nullable string)
            Identifier for this transaction.

          - `card.generated_from.payment_method_details.card_present.receipt.authorization_response_code` (nullable string)
            EMV tag 8A. A code returned by the card issuer.

          - `card.generated_from.payment_method_details.card_present.receipt.cardholder_verification_method` (nullable string)
            Describes the method used by the cardholder to verify ownership of the card. One of the following: `approval`, `failure`, `none`, `offline_pin`, `offline_pin_and_signature`, `online_pin`, or `signature`.

          - `card.generated_from.payment_method_details.card_present.receipt.dedicated_file_name` (nullable string)
            Similar to the application_preferred_name, identifying the applications (AIDs) available on the card. Referenced from EMV tag 84.

          - `card.generated_from.payment_method_details.card_present.receipt.terminal_verification_results` (nullable string)
            A 5-byte string that records the checks and validations that occur between the card and the terminal. These checks determine how the terminal processes the transaction and what risk tolerance is acceptable. Referenced from EMV Tag 95.

          - `card.generated_from.payment_method_details.card_present.receipt.transaction_status_information` (nullable string)
            An indication of which steps were completed during the card read process. Referenced from EMV Tag 9B.

        - `card.generated_from.payment_method_details.card_present.wallet` (nullable object)
          If a mobile wallet was presented in the transaction, this contains the details of the mobile wallet.

          - `card.generated_from.payment_method_details.card_present.wallet.type` (enum)
            The type of mobile wallet, one of `apple_pay`, `google_pay`, `samsung_pay`, or `unknown`.

            Apple Pay is a mobile payment service by Apple.

            Google Pay is a mobile payment service by Google.

            Samsung Pay is a mobile payment service by Samsung Electronics.

            The wallet provider is unknown.

      - `card.generated_from.payment_method_details.type` (string)
        The type of payment method transaction-specific details from the transaction that generated this `card` payment method. Always `card_present`.

    - `card.generated_from.setup_attempt` (nullable string)
      The ID of the SetupAttempt that generated this PaymentMethod, if any.

  - `card.last4` (string)
    The last four digits of the card.

  - `card.networks` (nullable object)
    Contains information about card networks that can be used to process the payment.

    - `card.networks.available` (array of strings)
      All networks available for selection via [payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-card-network).

    - `card.networks.preferred` (nullable string)
      The preferred network for co-branded cards. Can be `cartes_bancaires`, `mastercard`, `visa` or `invalid_preference` if requested network is not valid for the card.

  - `card.regulated_status` (nullable enum)
    Status of a card based on the card issuer.

    The card falls under a regulated account range.

    The card does not fall under a regulated account range.

  - `card.three_d_secure_usage` (nullable object)
    Contains details on how this Card may be used for 3D Secure authentication.

    - `card.three_d_secure_usage.supported` (boolean)
      Whether 3D Secure is supported on this card.

  - `card.wallet` (nullable object)
    If this Card is part of a card wallet, this contains the details of the card wallet.

    - `card.wallet.amex_express_checkout` (nullable object)
      If this is a `amex_express_checkout` card wallet, this hash contains details about the wallet.

    - `card.wallet.apple_pay` (nullable object)
      If this is a `apple_pay` card wallet, this hash contains details about the wallet.

    - `card.wallet.dynamic_last4` (nullable string)
      (For tokenized numbers only.) The last four digits of the device account number.

    - `card.wallet.google_pay` (nullable object)
      If this is a `google_pay` card wallet, this hash contains details about the wallet.

    - `card.wallet.link` (nullable object)
      If this is a `link` card wallet, this hash contains details about the wallet.

    - `card.wallet.masterpass` (nullable object)
      If this is a `masterpass` card wallet, this hash contains details about the wallet.

      - `card.wallet.masterpass.billing_address` (nullable object)
        Owner’s verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

        - `card.wallet.masterpass.billing_address.city` (nullable string)
          City, district, suburb, town, or village.

        - `card.wallet.masterpass.billing_address.country` (nullable string)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `card.wallet.masterpass.billing_address.line1` (nullable string)
          Address line 1 (e.g., street, PO Box, or company name).

        - `card.wallet.masterpass.billing_address.line2` (nullable string)
          Address line 2 (e.g., apartment, suite, unit, or building).

        - `card.wallet.masterpass.billing_address.postal_code` (nullable string)
          ZIP or postal code.

        - `card.wallet.masterpass.billing_address.state` (nullable string)
          State, county, province, or region.

      - `card.wallet.masterpass.email` (nullable string)
        Owner’s verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

      - `card.wallet.masterpass.name` (nullable string)
        Owner’s verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

      - `card.wallet.masterpass.shipping_address` (nullable object)
        Owner’s verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

        - `card.wallet.masterpass.shipping_address.city` (nullable string)
          City, district, suburb, town, or village.

        - `card.wallet.masterpass.shipping_address.country` (nullable string)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `card.wallet.masterpass.shipping_address.line1` (nullable string)
          Address line 1 (e.g., street, PO Box, or company name).

        - `card.wallet.masterpass.shipping_address.line2` (nullable string)
          Address line 2 (e.g., apartment, suite, unit, or building).

        - `card.wallet.masterpass.shipping_address.postal_code` (nullable string)
          ZIP or postal code.

        - `card.wallet.masterpass.shipping_address.state` (nullable string)
          State, county, province, or region.

    - `card.wallet.samsung_pay` (nullable object)
      If this is a `samsung_pay` card wallet, this hash contains details about the wallet.

    - `card.wallet.type` (enum)
      The type of the card wallet, one of `amex_express_checkout`, `apple_pay`, `google_pay`, `masterpass`, `samsung_pay`, `visa_checkout`, or `link`. An additional hash is included on the Wallet subhash with a name matching this value. It contains additional information specific to the card wallet type.

    - `card.wallet.visa_checkout` (nullable object)
      If this is a `visa_checkout` card wallet, this hash contains details about the wallet.

      - `card.wallet.visa_checkout.billing_address` (nullable object)
        Owner’s verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

        - `card.wallet.visa_checkout.billing_address.city` (nullable string)
          City, district, suburb, town, or village.

        - `card.wallet.visa_checkout.billing_address.country` (nullable string)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `card.wallet.visa_checkout.billing_address.line1` (nullable string)
          Address line 1 (e.g., street, PO Box, or company name).

        - `card.wallet.visa_checkout.billing_address.line2` (nullable string)
          Address line 2 (e.g., apartment, suite, unit, or building).

        - `card.wallet.visa_checkout.billing_address.postal_code` (nullable string)
          ZIP or postal code.

        - `card.wallet.visa_checkout.billing_address.state` (nullable string)
          State, county, province, or region.

      - `card.wallet.visa_checkout.email` (nullable string)
        Owner’s verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

      - `card.wallet.visa_checkout.name` (nullable string)
        Owner’s verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

      - `card.wallet.visa_checkout.shipping_address` (nullable object)
        Owner’s verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

        - `card.wallet.visa_checkout.shipping_address.city` (nullable string)
          City, district, suburb, town, or village.

        - `card.wallet.visa_checkout.shipping_address.country` (nullable string)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `card.wallet.visa_checkout.shipping_address.line1` (nullable string)
          Address line 1 (e.g., street, PO Box, or company name).

        - `card.wallet.visa_checkout.shipping_address.line2` (nullable string)
          Address line 2 (e.g., apartment, suite, unit, or building).

        - `card.wallet.visa_checkout.shipping_address.postal_code` (nullable string)
          ZIP or postal code.

        - `card.wallet.visa_checkout.shipping_address.state` (nullable string)
          State, county, province, or region.

- `card_present` (nullable object)
  If this is a `card_present` PaymentMethod, this hash contains details about the Card Present payment method.

  - `card_present.brand` (nullable string)
    Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

  - `card_present.brand_product` (nullable string)
    The [product code](https://stripe.com/docs/card-product-codes) that identifies the specific program or product associated with a card.

  - `card_present.cardholder_name` (nullable string)
    The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.

  - `card_present.country` (nullable string)
    Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

  - `card_present.exp_month` (integer)
    Two-digit number representing the card’s expiration month.

  - `card_present.exp_year` (integer)
    Four-digit number representing the card’s expiration year.

  - `card_present.fingerprint` (nullable string)
    Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

    *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

  - `card_present.funding` (nullable string)
    Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

  - `card_present.last4` (nullable string)
    The last four digits of the card.

  - `card_present.networks` (nullable object)
    Contains information about card networks that can be used to process the payment.

    - `card_present.networks.available` (array of strings)
      All networks available for selection via [payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-card-network).

    - `card_present.networks.preferred` (nullable string)
      The preferred network for the card.

  - `card_present.offline` (nullable object)
    Details about payment methods collected offline.

    - `card_present.offline.stored_at` (nullable timestamp)
      Time at which the payment was collected while offline

    - `card_present.offline.type` (nullable enum)
      The method used to process this payment method offline. Only deferred is allowed.

  - `card_present.preferred_locales` (nullable array of strings)
    The languages that the issuing bank recommends using for localizing any customer-facing text, as read from the card. Referenced from EMV tag 5F2D, data encoded on the card’s chip.

  - `card_present.read_method` (nullable enum)
    How card details were read in this transaction.

    Inserting a chip card into the card reader.

    Tapping a contactless-enabled chip card or mobile wallet.

    Older standard for contactless payments that emulated a magnetic stripe read.

    When inserting a chip card fails three times in a row, fallback to a magnetic stripe read.

    Swiping a card using the magnetic stripe reader.

  - `card_present.wallet` (nullable object)
    If a mobile wallet was presented in the transaction, this contains the details of the mobile wallet.

    - `card_present.wallet.type` (enum)
      The type of mobile wallet, one of `apple_pay`, `google_pay`, `samsung_pay`, or `unknown`.

      Apple Pay is a mobile payment service by Apple.

      Google Pay is a mobile payment service by Google.

      Samsung Pay is a mobile payment service by Samsung Electronics.

      The wallet provider is unknown.

- `cashapp` (nullable object)
  If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method.

  - `cashapp.buyer_id` (nullable string)
    A unique and immutable identifier assigned by Cash App to every buyer.

  - `cashapp.cashtag` (nullable string)
    A public identifier for buyers using Cash App.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `crypto` (nullable object)
  If this is a Crypto PaymentMethod, this hash contains details about the Crypto payment method.

- `customer` (nullable string)
  The ID of the Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer.

- `customer_balance` (nullable object)
  If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method.

- `eps` (nullable object)
  If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method.

  - `eps.bank` (nullable enum)
    The customer’s bank. Should be one of `arzte_und_apotheker_bank`, `austrian_anadi_bank_ag`, `bank_austria`, `bankhaus_carl_spangler`, `bankhaus_schelhammer_und_schattera_ag`, `bawag_psk_ag`, `bks_bank_ag`, `brull_kallmus_bank_ag`, `btv_vier_lander_bank`, `capital_bank_grawe_gruppe_ag`, `deutsche_bank_ag`, `dolomitenbank`, `easybank_ag`, `erste_bank_und_sparkassen`, `hypo_alpeadriabank_international_ag`, `hypo_noe_lb_fur_niederosterreich_u_wien`, `hypo_oberosterreich_salzburg_steiermark`, `hypo_tirol_bank_ag`, `hypo_vorarlberg_bank_ag`, `hypo_bank_burgenland_aktiengesellschaft`, `marchfelder_bank`, `oberbank_ag`, `raiffeisen_bankengruppe_osterreich`, `schoellerbank_ag`, `sparda_bank_wien`, `volksbank_gruppe`, `volkskreditbank_ag`, or `vr_bank_braunau`.

- `fpx` (nullable object)
  If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method.

  - `fpx.bank` (enum)
    The customer’s bank, if provided. Can be one of `affin_bank`, `agrobank`, `alliance_bank`, `ambank`, `bank_islam`, `bank_muamalat`, `bank_rakyat`, `bsn`, `cimb`, `hong_leong_bank`, `hsbc`, `kfh`, `maybank2u`, `ocbc`, `public_bank`, `rhb`, `standard_chartered`, `uob`, `deutsche_bank`, `maybank2e`, `pb_enterprise`, or `bank_of_china`.

- `giropay` (nullable object)
  If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method.

- `grabpay` (nullable object)
  If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method.

- `ideal` (nullable object)
  If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method.

  - `ideal.bank` (nullable enum)
    The customer’s bank, if provided. Can be one of `abn_amro`, `asn_bank`, `bunq`, `buut`, `handelsbanken`, `ing`, `knab`, `moneyou`, `n26`, `nn`, `rabobank`, `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, `van_lanschot`, or `yoursafe`.

  - `ideal.bic` (nullable enum)
    The Bank Identifier Code of the customer’s bank, if the bank was provided.

- `kakao_pay` (nullable object)
  If this is a `kakao_pay` PaymentMethod, this hash contains details about the Kakao Pay payment method.

- `klarna` (nullable object)
  If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method.

  - `klarna.dob` (nullable object)
    The customer’s date of birth, if provided.

    - `klarna.dob.day` (nullable integer)
      The day of birth, between 1 and 31.

    - `klarna.dob.month` (nullable integer)
      The month of birth, between 1 and 12.

    - `klarna.dob.year` (nullable integer)
      The four-digit year of birth.

- `konbini` (nullable object)
  If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method.

- `kr_card` (nullable object)
  If this is a `kr_card` PaymentMethod, this hash contains details about the Korean Card payment method.

  - `kr_card.brand` (nullable enum)
    The local credit or debit card brand.

    BC

    Citi

    Hana

    Hyundai

    Jeju

    Jeonbuk

    Kakao Bank

    KBank

    KDB Bank

    Kookmin

    Kwangju

    Lotte

    MG

    NG

    Post

    Samsung

    Savings Bank

    Shinhan

    Shinhyup

    Suhyup

    Toss Bank

    Woori

  - `kr_card.last4` (nullable string)
    The last four digits of the card. This may not be present for American Express cards.

- `link` (nullable object)
  If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.

  - `link.email` (nullable string)
    Account owner’s email address.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (nullable object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `mobilepay` (nullable object)
  If this is a `mobilepay` PaymentMethod, this hash contains details about the MobilePay payment method.

- `multibanco` (nullable object)
  If this is a `multibanco` PaymentMethod, this hash contains details about the Multibanco payment method.

- `naver_pay` (nullable object)
  If this is a `naver_pay` PaymentMethod, this hash contains details about the Naver Pay payment method.

  - `naver_pay.buyer_id` (nullable string)
    Uniquely identifies this particular Naver Pay account. You can use this attribute to check whether two Naver Pay accounts are the same.

  - `naver_pay.funding` (enum)
    Whether to fund this transaction with Naver Pay points or a card.

    Use a card to fund this transaction.

    Use Naver Pay points to fund this transaction.

- `nz_bank_account` (nullable object)
  If this is an nz_bank_account PaymentMethod, this hash contains details about the nz_bank_account payment method.

  - `nz_bank_account.account_holder_name` (nullable string)
    The name on the bank account. Only present if the account holder name is different from the name of the authorized signatory collected in the PaymentMethod’s billing details.

  - `nz_bank_account.bank_code` (string)
    The numeric code for the bank account’s bank.

  - `nz_bank_account.bank_name` (string)
    The name of the bank.

  - `nz_bank_account.branch_code` (string)
    The numeric code for the bank account’s bank branch.

  - `nz_bank_account.last4` (string)
    Last four digits of the bank account number.

  - `nz_bank_account.suffix` (nullable string)
    The suffix of the bank account number.

- `oxxo` (nullable object)
  If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method.

- `p24` (nullable object)
  If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method.

  - `p24.bank` (nullable enum)
    The customer’s bank, if provided.

- `pay_by_bank` (nullable object)
  If this is a `pay_by_bank` PaymentMethod, this hash contains details about the PayByBank payment method.

- `payco` (nullable object)
  If this is a `payco` PaymentMethod, this hash contains details about the PAYCO payment method.

- `paynow` (nullable object)
  If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method.

- `paypal` (nullable object)
  If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method.

  - `paypal.country` (nullable string)
    Two-letter ISO code representing the buyer’s country. Values are provided by PayPal directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

  - `paypal.payer_email` (nullable string)
    Owner’s email. Values are provided by PayPal directly
    (if supported) at the time of authorization or settlement. They cannot be set or mutated.

  - `paypal.payer_id` (nullable string)
    PayPal account PayerID. This identifier uniquely identifies the PayPal customer.

- `pix` (nullable object)
  If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method.

- `promptpay` (nullable object)
  If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method.

- `radar_options` (nullable object)
  Options to configure Radar. See [Radar Session](https://docs.stripe.com/docs/radar/radar-session.md) for more information.

  - `radar_options.session` (nullable string)
    A [Radar Session](https://docs.stripe.com/docs/radar/radar-session.md) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.

- `revolut_pay` (nullable object)
  If this is a `revolut_pay` PaymentMethod, this hash contains details about the Revolut Pay payment method.

- `samsung_pay` (nullable object)
  If this is a `samsung_pay` PaymentMethod, this hash contains details about the SamsungPay payment method.

- `satispay` (nullable object)
  If this is a `satispay` PaymentMethod, this hash contains details about the Satispay payment method.

- `sepa_debit` (nullable object)
  If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account.

  - `sepa_debit.bank_code` (nullable string)
    Bank code of bank associated with the bank account.

  - `sepa_debit.branch_code` (nullable string)
    Branch code of bank associated with the bank account.

  - `sepa_debit.country` (nullable string)
    Two-letter ISO code representing the country the bank account is located in.

  - `sepa_debit.fingerprint` (nullable string)
    Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

  - `sepa_debit.generated_from` (nullable object)
    Information about the object that generated this PaymentMethod.

    - `sepa_debit.generated_from.charge` (nullable string)
      The ID of the Charge that generated this PaymentMethod, if any.

    - `sepa_debit.generated_from.setup_attempt` (nullable string)
      The ID of the SetupAttempt that generated this PaymentMethod, if any.

  - `sepa_debit.last4` (nullable string)
    Last four characters of the IBAN.

- `sofort` (nullable object)
  If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method.

  - `sofort.country` (nullable string)
    Two-letter ISO code representing the country the bank account is located in.

- `swish` (nullable object)
  If this is a `swish` PaymentMethod, this hash contains details about the Swish payment method.

- `twint` (nullable object)
  If this is a TWINT PaymentMethod, this hash contains details about the TWINT payment method.

- `type` (enum)
  The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.

  [Pre-authorized debit payments](https://docs.stripe.com/docs/payments/acss-debit.md) are used to debit Canadian bank accounts through the Automated Clearing Settlement System (ACSS).

  [Affirm](https://docs.stripe.com/docs/payments/affirm.md) is a buy now, pay later payment method in the US.

  [Afterpay / Clearpay](https://docs.stripe.com/docs/payments/afterpay-clearpay.md) is a buy now, pay later payment method used in Australia, Canada, France, New Zealand, Spain, the UK, and the US.

  [Alipay](https://docs.stripe.com/docs/payments/alipay.md) is a digital wallet payment method used in China.

  [Alma](https://docs.stripe.com/docs/payments/alma.md) is a Buy Now, Pay Later payment method that lets customers pay in 2, 3, or 4 installments.

  [Amazon Pay](https://docs.stripe.com/docs/payments/amazon-pay.md) is a Wallet payment method that lets hundreds of millions of Amazon customers pay their way, every day.

  [BECS Direct Debit](https://docs.stripe.com/docs/payments/au-becs-debit.md) is used to debit Australian bank accounts through the Bulk Electronic Clearing System (BECS).

  [Bacs Direct Debit](https://docs.stripe.com/docs/payments/payment-methods/bacs-debit.md) is used to debit UK bank accounts.

  [Bancontact](https://docs.stripe.com/docs/payments/bancontact.md) is a bank redirect payment method used in Belgium.

  [Billie](https://docs.stripe.com/docs/payments/billie.md) is a payment method.

  [BLIK](https://docs.stripe.com/docs/payments/blik.md) is a single-use payment method common in Poland.

  [Boleto](https://docs.stripe.com/docs/payments/boleto.md) is a voucher-based payment method used in Brazil.

  [Card payments](https://docs.stripe.com/docs/payments/payment-methods/overview.md#cards) are supported through many networks, card brands, and select Link funding sources.

  [Stripe Terminal](https://docs.stripe.com/docs/terminal/payments/collect-card-payment.md) is used to collect in-person card payments.

  [Cash App Pay](https://docs.stripe.com/docs/payments/cash-app-pay.md) enables customers to frictionlessly authenticate payments in the Cash App using their stored balance or linked card.

  Crypto is a payment method.

  Uses a customer’s [cash balance](https://docs.stripe.com/docs/payments/customer-balance.md) for the payment.

  [EPS](https://docs.stripe.com/docs/payments/eps.md) is an Austria-based bank redirect payment method.

  [FPX](https://docs.stripe.com/docs/payments/fpx.md) is a Malaysia-based bank redirect payment method.

  [giropay](https://docs.stripe.com/docs/payments/giropay.md) is a German bank redirect payment method.

  [GrabPay](https://docs.stripe.com/docs/payments/grabpay.md) is a digital wallet payment method used in Southeast Asia.

  [iDEAL](https://docs.stripe.com/docs/payments/ideal.md) is a Netherlands-based bank redirect payment method.

  [Kakao Pay](https://docs.stripe.com/docs/payments/kakao-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  [Klarna](https://docs.stripe.com/docs/payments/klarna.md) is a global buy now, pay later payment method.

  [Konbini](https://docs.stripe.com/docs/payments/konbini.md) is a cash-based voucher payment method used in Japan.

  [Korean cards](https://docs.stripe.com/docs/payments/kr-card/accept-a-payment.md) enables customers to accept local credit and debit cards in South Korea.

  [Link](https://docs.stripe.com/docs/payments/link.md) allows customers to pay with their saved payment details.

  [MobilePay](https://docs.stripe.com/docs/payments/mobilepay.md) is a Nordic card-passthrough wallet payment method where customers authorize the payment in the MobilePay application.

  [Multibanco](https://docs.stripe.com/docs/payments/multibanco.md) is a voucher payment method

  [Naver Pay](https://docs.stripe.com/docs/payments/naver-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  [New Zealand BECS Direct Debit](https://docs.stripe.com/docs/payments/nz-bank-account.md) is used to debit New Zealand bank accounts through the Bulk Electronic Clearing System (BECS).

  [OXXO](https://docs.stripe.com/docs/payments/oxxo.md) is a cash-based voucher payment method used in Mexico.

  [Przelewy24](https://docs.stripe.com/docs/payments/p24.md) is a bank redirect payment method used in Poland.

  [Pay By Bank](https://docs.stripe.com/docs/payments/pay-by-bank.md) is an open banking payment method in the UK.

  [PAYCO](https://docs.stripe.com/docs/payments/payco/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  [PayNow](https://docs.stripe.com/docs/payments/paynow.md) is a QR code payment method used in Singapore.

  [PayPal](https://docs.stripe.com/docs/payments/paypal.md) is an online wallet and redirect payment method commonly used in Europe.

  [Pix](https://docs.stripe.com/docs/payments/pix.md) is an instant bank transfer payment method in Brazil.

  [PromptPay](https://docs.stripe.com/docs/payments/promptpay.md) is an instant funds transfer service popular in Thailand.

  [Revolut Pay](https://docs.stripe.com/docs/payments/revolut-pay.md) is a digital wallet payment method used in the United Kingdom.

  [Samsung Pay](https://docs.stripe.com/docs/payments/samsung-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  [Satispay](https://docs.stripe.com/docs/payments/satispay.md) is a payment method.

  [SEPA Direct Debit](https://docs.stripe.com/docs/payments/sepa-debit.md) is used to debit bank accounts within the Single Euro Payments Area (SEPA) region.

  [Sofort](https://docs.stripe.com/docs/payments/sofort.md) is a bank redirect payment method used in Europe.

  [Swish](https://docs.stripe.com/docs/payments/swish.md) is a Swedish wallet payment method where customers authorize the payment in the Swish application.

  [TWINT](https://docs.stripe.com/docs/payments/twint.md) is a single-use payment method used in Switzerland.

  [ACH Direct Debit](https://docs.stripe.com/docs/payments/ach-direct-debit.md) is used to debit US bank accounts through the Automated Clearing House (ACH) payments system.

  [WeChat Pay](https://docs.stripe.com/docs/payments/wechat-pay.md) is a digital wallet payment method based in China.

  [Zip](https://docs.stripe.com/docs/payments/zip.md) is a Buy now, pay later Payment Method

- `us_bank_account` (nullable object)
  If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.

  - `us_bank_account.account_holder_type` (nullable enum)
    Account holder type: individual or company.

    Account belongs to a company

    Account belongs to an individual

  - `us_bank_account.account_type` (nullable enum)
    Account type: checkings or savings. Defaults to checking if omitted.

    Bank account type is checking

    Bank account type is savings

  - `us_bank_account.bank_name` (nullable string)
    The name of the bank.

  - `us_bank_account.financial_connections_account` (nullable string)
    The ID of the Financial Connections Account used to create the payment method.

  - `us_bank_account.fingerprint` (nullable string)
    Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

  - `us_bank_account.last4` (nullable string)
    Last four digits of the bank account number.

  - `us_bank_account.networks` (nullable object)
    Contains information about US bank account networks that can be used.

    - `us_bank_account.networks.preferred` (nullable string)
      The preferred network.

    - `us_bank_account.networks.supported` (array of enums)
      All supported networks.

  - `us_bank_account.routing_number` (nullable string)
    Routing number of the bank account.

  - `us_bank_account.status_details` (nullable object)
    Contains information about the future reusability of this PaymentMethod.

    - `us_bank_account.status_details.blocked` (nullable object)
      Contains more information about the underlying block.
      This field will only be rendered if the PaymentMethod is blocked.

      - `us_bank_account.status_details.blocked.network_code` (nullable enum)
        The ACH network code that resulted in this block.

        Account Closed

        No Account, Unable to Locate Account

        Invalid Account Number Structure

        Unauthorized Debit to Consumer Account Using Corporate SEC Code

        Authorization Revoked By Consumer

        Payment Stopped

        Customer Advises Originator is Not Known to Receiver and/or Originator is Not Authorized by Receiver to Debit Receiver’s Account

        Customer Advises Entry Not in Accordance with the Terms of Authorization

        Account Frozen, Entry Returned Per OFAC Instructions

        Non-Transaction Account

        Corporate Customer Advises Not Authorized

        Permissible Return Entry (CCD and CTX only)

      - `us_bank_account.status_details.blocked.reason` (nullable enum)
        The reason why this PaymentMethod’s fingerprint has been blocked

        Bank account has been closed.

        Bank account has been frozen.

        Bank account details are incorrect. Please check the account number, routing number, account holder name, and account type.

        Bank account does not support debits.

        Bank account has been blocked by Stripe. Please contact Support.

        Customer has disputed a previous payment with their bank. If the `network_code` is R29, please confirm that Stripe’s Company IDs are allowlisted before attempting additional payments.

- `wechat_pay` (nullable object)
  If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method.

- `zip` (nullable object)
  If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method.

### The PaymentMethod object

```json
{
  "id": "pm_1Q0PsIJvEtkwdCNYMSaVuRz6",
  "object": "payment_method",
  "allow_redisplay": "unspecified",
  "billing_details": {
    "address": {
      "city": null,
      "country": null,
      "line1": null,
      "line2": null,
      "postal_code": null,
      "state": null
    },
    "email": null,
    "name": "John Doe",
    "phone": null
  },
  "created": 1726673582,
  "customer": null,
  "livemode": false,
  "metadata": {},
  "type": "us_bank_account",
  "us_bank_account": {
    "account_holder_type": "individual",
    "account_type": "checking",
    "bank_name": "STRIPE TEST BANK",
    "financial_connections_account": null,
    "fingerprint": "LstWJFsCK7P349Bg",
    "last4": "6789",
    "networks": {
      "preferred": "ach",
      "supported": [
        "ach"
      ]
    },
    "routing_number": "110000000",
    "status_details": {}
  }
}
```