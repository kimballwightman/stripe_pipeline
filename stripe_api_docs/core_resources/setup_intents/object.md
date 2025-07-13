# The SetupIntent object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `application` (nullable string)
  ID of the Connect application that created the SetupIntent.

- `attach_to_self` (nullable boolean)
  If present, the SetupIntent’s payment method will be attached to the in-context Stripe Account.

  It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.

- `automatic_payment_methods` (nullable object)
  Settings for dynamic payment methods compatible with this Setup Intent

  - `automatic_payment_methods.allow_redirects` (nullable enum)
    Controls whether this SetupIntent will accept redirect-based payment methods.

    Redirect-based payment methods may require your customer to be redirected to a payment method’s app or site for authentication or additional steps. To [confirm](https://docs.stripe.com/docs/api/setup_intents/confirm.md) this SetupIntent, you may be required to provide a `return_url` to redirect customers back to your site after they authenticate or complete the setup.

    (Default) This SetupIntent will accept redirect-based payment methods. `return_url` may be required to       [confirm](https://docs.stripe.com/docs/api/setup_intents/confirm.md) this SetupIntent.

    This SetupIntent will not accept redirect-based payment methods. Payment methods that require redirect will       be filtered. `return_url` will not be required to [confirm](https://docs.stripe.com/docs/api/setup_intents/confirm.md) this       SetupIntent.

  - `automatic_payment_methods.enabled` (nullable boolean)
    Automatically calculates compatible payment methods

- `cancellation_reason` (nullable enum)
  Reason for cancellation of this SetupIntent, one of `abandoned`, `requested_by_customer`, or `duplicate`.

- `client_secret` (nullable string)
  The client secret of this SetupIntent. Used for client-side retrieval using a publishable key.

  The client secret can be used to complete payment setup from your frontend. It should not be stored, logged, or exposed to anyone other than the customer. Make sure that you have TLS enabled on any page that includes the client secret.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `customer` (nullable string)
  ID of the Customer this SetupIntent belongs to, if one exists.

  If present, the SetupIntent’s payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.

- `description` (nullable string)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `flow_directions` (nullable array of enums)
  Indicates the directions of money movement for which this payment method is intended to be used.

  Include `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes.

- `last_setup_error` (nullable object)
  The error encountered in the previous SetupIntent confirmation.

  - `last_setup_error.advice_code` (nullable string)
    For card errors resulting from a card issuer decline, a short string indicating [how to proceed with an error](https://docs.stripe.com/docs/declines.md#retrying-issuer-declines) if they provide one.

  - `last_setup_error.code` (nullable string)
    For some errors that could be handled programmatically, a short string indicating the [error code](https://docs.stripe.com/docs/error-codes.md) reported.

  - `last_setup_error.decline_code` (nullable string)
    For card errors resulting from a card issuer decline, a short string indicating the [card issuer’s reason for the decline](https://docs.stripe.com/docs/declines.md#issuer-declines) if they provide one.

  - `last_setup_error.doc_url` (nullable string)
    A URL to more information about the [error code](https://docs.stripe.com/docs/error-codes.md) reported.

  - `last_setup_error.message` (nullable string)
    A human-readable message providing more details about the error. For card errors, these messages can be shown to your users.

  - `last_setup_error.network_advice_code` (nullable string)
    For card errors resulting from a card issuer decline, a 2 digit code which indicates the advice given to merchant by the card network on how to proceed with an error.

  - `last_setup_error.network_decline_code` (nullable string)
    For card errors resulting from a card issuer decline, a brand specific 2, 3, or 4 digit code which indicates the reason the authorization failed.

  - `last_setup_error.param` (nullable string)
    If the error is parameter-specific, the parameter related to the error. For example, you can use this to display a message near the correct form field.

  - `last_setup_error.payment_method` (nullable object)
    The [PaymentMethod object](https://docs.stripe.com/docs/api/payment_methods/object.md) for errors returned on a request involving a PaymentMethod.

    - `last_setup_error.payment_method.id` (string)
      Unique identifier for the object.

    - `last_setup_error.payment_method.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `last_setup_error.payment_method.acss_debit` (nullable object)
      If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method.

      - `last_setup_error.payment_method.acss_debit.bank_name` (nullable string)
        Name of the bank associated with the bank account.

      - `last_setup_error.payment_method.acss_debit.fingerprint` (nullable string)
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

      - `last_setup_error.payment_method.acss_debit.institution_number` (nullable string)
        Institution number of the bank account.

      - `last_setup_error.payment_method.acss_debit.last4` (nullable string)
        Last four digits of the bank account number.

      - `last_setup_error.payment_method.acss_debit.transit_number` (nullable string)
        Transit number of the bank account.

    - `last_setup_error.payment_method.affirm` (nullable object)
      If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method.

    - `last_setup_error.payment_method.afterpay_clearpay` (nullable object)
      If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method.

    - `last_setup_error.payment_method.alipay` (nullable object)
      If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method.

    - `last_setup_error.payment_method.allow_redisplay` (nullable enum)
      This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to “unspecified”.

      Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

      Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

      This is the default value for payment methods where `allow_redisplay` wasn’t set.

    - `last_setup_error.payment_method.alma` (nullable object)
      If this is a Alma PaymentMethod, this hash contains details about the Alma payment method.

    - `last_setup_error.payment_method.amazon_pay` (nullable object)
      If this is a AmazonPay PaymentMethod, this hash contains details about the AmazonPay payment method.

    - `last_setup_error.payment_method.au_becs_debit` (nullable object)
      If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account.

      - `last_setup_error.payment_method.au_becs_debit.bsb_number` (nullable string)
        Six-digit number identifying bank and branch associated with this bank account.

      - `last_setup_error.payment_method.au_becs_debit.fingerprint` (nullable string)
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

      - `last_setup_error.payment_method.au_becs_debit.last4` (nullable string)
        Last four digits of the bank account number.

    - `last_setup_error.payment_method.bacs_debit` (nullable object)
      If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account.

      - `last_setup_error.payment_method.bacs_debit.fingerprint` (nullable string)
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

      - `last_setup_error.payment_method.bacs_debit.last4` (nullable string)
        Last four digits of the bank account number.

      - `last_setup_error.payment_method.bacs_debit.sort_code` (nullable string)
        Sort code of the bank account. (e.g., `10-20-30`)

    - `last_setup_error.payment_method.bancontact` (nullable object)
      If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method.

    - `last_setup_error.payment_method.billie` (nullable object)
      If this is a `billie` PaymentMethod, this hash contains details about the Billie payment method.

    - `last_setup_error.payment_method.billing_details` (object)
      Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.

      - `last_setup_error.payment_method.billing_details.address` (nullable object)
        Billing address.

        - `last_setup_error.payment_method.billing_details.address.city` (nullable string)
          City, district, suburb, town, or village.

        - `last_setup_error.payment_method.billing_details.address.country` (nullable string)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `last_setup_error.payment_method.billing_details.address.line1` (nullable string)
          Address line 1 (e.g., street, PO Box, or company name).

        - `last_setup_error.payment_method.billing_details.address.line2` (nullable string)
          Address line 2 (e.g., apartment, suite, unit, or building).

        - `last_setup_error.payment_method.billing_details.address.postal_code` (nullable string)
          ZIP or postal code.

        - `last_setup_error.payment_method.billing_details.address.state` (nullable string)
          State, county, province, or region.

      - `last_setup_error.payment_method.billing_details.email` (nullable string)
        Email address.

      - `last_setup_error.payment_method.billing_details.name` (nullable string)
        Full name.

      - `last_setup_error.payment_method.billing_details.phone` (nullable string)
        Billing phone number (including extension).

      - `last_setup_error.payment_method.billing_details.tax_id` (nullable string)
        Taxpayer identification number. Used only for transactions between LATAM buyers and non-LATAM sellers.

    - `last_setup_error.payment_method.blik` (nullable object)
      If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method.

    - `last_setup_error.payment_method.boleto` (nullable object)
      If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method.

      - `last_setup_error.payment_method.boleto.tax_id` (string)
        Uniquely identifies the customer tax id (CNPJ or CPF)

    - `last_setup_error.payment_method.card` (nullable object)
      If this is a `card` PaymentMethod, this hash contains the user’s card details.

      - `last_setup_error.payment_method.card.brand` (string)
        Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

      - `last_setup_error.payment_method.card.checks` (nullable object)
        Checks on Card address and CVC if provided.

        - `last_setup_error.payment_method.card.checks.address_line1_check` (nullable string)
          If a address line1 was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.

        - `last_setup_error.payment_method.card.checks.address_postal_code_check` (nullable string)
          If a address postal code was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.

        - `last_setup_error.payment_method.card.checks.cvc_check` (nullable string)
          If a CVC was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.

      - `last_setup_error.payment_method.card.country` (nullable string)
        Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

      - `last_setup_error.payment_method.card.display_brand` (nullable string)
        The brand to use when displaying the card, this accounts for customer’s brand choice on dual-branded cards. Can be `american_express`, `cartes_bancaires`, `diners_club`, `discover`, `eftpos_australia`, `interac`, `jcb`, `mastercard`, `union_pay`, `visa`, or `other` and may contain more values in the future.

      - `last_setup_error.payment_method.card.exp_month` (integer)
        Two-digit number representing the card’s expiration month.

      - `last_setup_error.payment_method.card.exp_year` (integer)
        Four-digit number representing the card’s expiration year.

      - `last_setup_error.payment_method.card.fingerprint` (nullable string)
        Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

        *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

      - `last_setup_error.payment_method.card.funding` (string)
        Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

      - `last_setup_error.payment_method.card.generated_from` (nullable object)
        Details of the original PaymentMethod that created this object.

        - `last_setup_error.payment_method.card.generated_from.charge` (nullable string)
          The charge that created this object.

        - `last_setup_error.payment_method.card.generated_from.payment_method_details` (nullable object)
          Transaction-specific details of the payment method used in the payment.

          - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present` (nullable object)
            This hash contains the snapshot of the `card_present` transaction-specific details which generated this `card` payment method.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.amount_authorized` (nullable integer)
              The authorized amount

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.brand` (nullable string)
              Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.brand_product` (nullable string)
              The [product code](https://stripe.com/docs/card-product-codes) that identifies the specific program or product associated with a card.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.capture_before` (nullable timestamp)
              When using manual capture, a future timestamp after which the charge will be automatically refunded if uncaptured.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.cardholder_name` (nullable string)
              The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.country` (nullable string)
              Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.emv_auth_data` (nullable string)
              Authorization response cryptogram.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.exp_month` (integer)
              Two-digit number representing the card’s expiration month.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.exp_year` (integer)
              Four-digit number representing the card’s expiration year.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.fingerprint` (nullable string)
              Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

              *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.funding` (nullable string)
              Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.generated_card` (nullable string)
              ID of a card PaymentMethod generated from the card_present PaymentMethod that may be attached to a Customer for future transactions. Only present if it was possible to generate a card PaymentMethod.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.incremental_authorization_supported` (boolean)
              Whether this [PaymentIntent](https://docs.stripe.com/docs/api/payment_intents.md) is eligible for incremental authorizations. Request support using [request_incremental_authorization_support](https://docs.stripe.com/docs/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-request_incremental_authorization_support).

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.last4` (nullable string)
              The last four digits of the card.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.network` (nullable string)
              Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.network_transaction_id` (nullable string)
              This is used by the financial networks to identify a transaction. Visa calls this the Transaction ID, Mastercard calls this the Trace ID, and American Express calls this the Acquirer Reference Data. This value will be present if it is returned by the financial network in the authorization response, and null otherwise.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.offline` (nullable object)
              Details about payments collected offline.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.offline.stored_at` (nullable timestamp)
                Time at which the payment was collected while offline

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.offline.type` (nullable enum)
                The method used to process this payment method offline. Only deferred is allowed.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.overcapture_supported` (boolean)
              Defines whether the authorized amount can be over-captured or not

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.preferred_locales` (nullable array of strings)
              The languages that the issuing bank recommends using for localizing any customer-facing text, as read from the card. Referenced from EMV tag 5F2D, data encoded on the card’s chip.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.read_method` (nullable enum)
              How card details were read in this transaction.

              Inserting a chip card into the card reader.

              Tapping a contactless-enabled chip card or mobile wallet.

              Older standard for contactless payments that emulated a magnetic stripe read.

              When inserting a chip card fails three times in a row, fallback to a magnetic stripe read.

              Swiping a card using the magnetic stripe reader.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt` (nullable object)
              A collection of fields required to be displayed on receipts. Only required for EMV transactions.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt.account_type` (nullable enum)
                The type of account being debited or credited

                A checking account, as when using a debit card

                A credit account, as when using a credit card

                A prepaid account, as when using a debit gift card

                An unknown account

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt.application_cryptogram` (nullable string)
                The Application Cryptogram, a unique value generated by the card to authenticate the transaction with issuers.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt.application_preferred_name` (nullable string)
                The Application Identifier (AID) on the card used to determine which networks are eligible to process the transaction. Referenced from EMV tag 9F12, data encoded on the card’s chip.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt.authorization_code` (nullable string)
                Identifier for this transaction.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt.authorization_response_code` (nullable string)
                EMV tag 8A. A code returned by the card issuer.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt.cardholder_verification_method` (nullable string)
                Describes the method used by the cardholder to verify ownership of the card. One of the following: `approval`, `failure`, `none`, `offline_pin`, `offline_pin_and_signature`, `online_pin`, or `signature`.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt.dedicated_file_name` (nullable string)
                Similar to the application_preferred_name, identifying the applications (AIDs) available on the card. Referenced from EMV tag 84.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt.terminal_verification_results` (nullable string)
                A 5-byte string that records the checks and validations that occur between the card and the terminal. These checks determine how the terminal processes the transaction and what risk tolerance is acceptable. Referenced from EMV Tag 95.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.receipt.transaction_status_information` (nullable string)
                An indication of which steps were completed during the card read process. Referenced from EMV Tag 9B.

            - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.wallet` (nullable object)
              If a mobile wallet was presented in the transaction, this contains the details of the mobile wallet.

              - `last_setup_error.payment_method.card.generated_from.payment_method_details.card_present.wallet.type` (enum)
                The type of mobile wallet, one of `apple_pay`, `google_pay`, `samsung_pay`, or `unknown`.

                Apple Pay is a mobile payment service by Apple.

                Google Pay is a mobile payment service by Google.

                Samsung Pay is a mobile payment service by Samsung Electronics.

                The wallet provider is unknown.

          - `last_setup_error.payment_method.card.generated_from.payment_method_details.type` (string)
            The type of payment method transaction-specific details from the transaction that generated this `card` payment method. Always `card_present`.

        - `last_setup_error.payment_method.card.generated_from.setup_attempt` (nullable string)
          The ID of the SetupAttempt that generated this PaymentMethod, if any.

      - `last_setup_error.payment_method.card.last4` (string)
        The last four digits of the card.

      - `last_setup_error.payment_method.card.networks` (nullable object)
        Contains information about card networks that can be used to process the payment.

        - `last_setup_error.payment_method.card.networks.available` (array of strings)
          All networks available for selection via [payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-card-network).

        - `last_setup_error.payment_method.card.networks.preferred` (nullable string)
          The preferred network for co-branded cards. Can be `cartes_bancaires`, `mastercard`, `visa` or `invalid_preference` if requested network is not valid for the card.

      - `last_setup_error.payment_method.card.regulated_status` (nullable enum)
        Status of a card based on the card issuer.

        The card falls under a regulated account range.

        The card does not fall under a regulated account range.

      - `last_setup_error.payment_method.card.three_d_secure_usage` (nullable object)
        Contains details on how this Card may be used for 3D Secure authentication.

        - `last_setup_error.payment_method.card.three_d_secure_usage.supported` (boolean)
          Whether 3D Secure is supported on this card.

      - `last_setup_error.payment_method.card.wallet` (nullable object)
        If this Card is part of a card wallet, this contains the details of the card wallet.

        - `last_setup_error.payment_method.card.wallet.amex_express_checkout` (nullable object)
          If this is a `amex_express_checkout` card wallet, this hash contains details about the wallet.

        - `last_setup_error.payment_method.card.wallet.apple_pay` (nullable object)
          If this is a `apple_pay` card wallet, this hash contains details about the wallet.

        - `last_setup_error.payment_method.card.wallet.dynamic_last4` (nullable string)
          (For tokenized numbers only.) The last four digits of the device account number.

        - `last_setup_error.payment_method.card.wallet.google_pay` (nullable object)
          If this is a `google_pay` card wallet, this hash contains details about the wallet.

        - `last_setup_error.payment_method.card.wallet.link` (nullable object)
          If this is a `link` card wallet, this hash contains details about the wallet.

        - `last_setup_error.payment_method.card.wallet.masterpass` (nullable object)
          If this is a `masterpass` card wallet, this hash contains details about the wallet.

          - `last_setup_error.payment_method.card.wallet.masterpass.billing_address` (nullable object)
            Owner’s verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

            - `last_setup_error.payment_method.card.wallet.masterpass.billing_address.city` (nullable string)
              City, district, suburb, town, or village.

            - `last_setup_error.payment_method.card.wallet.masterpass.billing_address.country` (nullable string)
              Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

            - `last_setup_error.payment_method.card.wallet.masterpass.billing_address.line1` (nullable string)
              Address line 1 (e.g., street, PO Box, or company name).

            - `last_setup_error.payment_method.card.wallet.masterpass.billing_address.line2` (nullable string)
              Address line 2 (e.g., apartment, suite, unit, or building).

            - `last_setup_error.payment_method.card.wallet.masterpass.billing_address.postal_code` (nullable string)
              ZIP or postal code.

            - `last_setup_error.payment_method.card.wallet.masterpass.billing_address.state` (nullable string)
              State, county, province, or region.

          - `last_setup_error.payment_method.card.wallet.masterpass.email` (nullable string)
            Owner’s verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

          - `last_setup_error.payment_method.card.wallet.masterpass.name` (nullable string)
            Owner’s verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

          - `last_setup_error.payment_method.card.wallet.masterpass.shipping_address` (nullable object)
            Owner’s verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

            - `last_setup_error.payment_method.card.wallet.masterpass.shipping_address.city` (nullable string)
              City, district, suburb, town, or village.

            - `last_setup_error.payment_method.card.wallet.masterpass.shipping_address.country` (nullable string)
              Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

            - `last_setup_error.payment_method.card.wallet.masterpass.shipping_address.line1` (nullable string)
              Address line 1 (e.g., street, PO Box, or company name).

            - `last_setup_error.payment_method.card.wallet.masterpass.shipping_address.line2` (nullable string)
              Address line 2 (e.g., apartment, suite, unit, or building).

            - `last_setup_error.payment_method.card.wallet.masterpass.shipping_address.postal_code` (nullable string)
              ZIP or postal code.

            - `last_setup_error.payment_method.card.wallet.masterpass.shipping_address.state` (nullable string)
              State, county, province, or region.

        - `last_setup_error.payment_method.card.wallet.samsung_pay` (nullable object)
          If this is a `samsung_pay` card wallet, this hash contains details about the wallet.

        - `last_setup_error.payment_method.card.wallet.type` (enum)
          The type of the card wallet, one of `amex_express_checkout`, `apple_pay`, `google_pay`, `masterpass`, `samsung_pay`, `visa_checkout`, or `link`. An additional hash is included on the Wallet subhash with a name matching this value. It contains additional information specific to the card wallet type.

        - `last_setup_error.payment_method.card.wallet.visa_checkout` (nullable object)
          If this is a `visa_checkout` card wallet, this hash contains details about the wallet.

          - `last_setup_error.payment_method.card.wallet.visa_checkout.billing_address` (nullable object)
            Owner’s verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

            - `last_setup_error.payment_method.card.wallet.visa_checkout.billing_address.city` (nullable string)
              City, district, suburb, town, or village.

            - `last_setup_error.payment_method.card.wallet.visa_checkout.billing_address.country` (nullable string)
              Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

            - `last_setup_error.payment_method.card.wallet.visa_checkout.billing_address.line1` (nullable string)
              Address line 1 (e.g., street, PO Box, or company name).

            - `last_setup_error.payment_method.card.wallet.visa_checkout.billing_address.line2` (nullable string)
              Address line 2 (e.g., apartment, suite, unit, or building).

            - `last_setup_error.payment_method.card.wallet.visa_checkout.billing_address.postal_code` (nullable string)
              ZIP or postal code.

            - `last_setup_error.payment_method.card.wallet.visa_checkout.billing_address.state` (nullable string)
              State, county, province, or region.

          - `last_setup_error.payment_method.card.wallet.visa_checkout.email` (nullable string)
            Owner’s verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

          - `last_setup_error.payment_method.card.wallet.visa_checkout.name` (nullable string)
            Owner’s verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

          - `last_setup_error.payment_method.card.wallet.visa_checkout.shipping_address` (nullable object)
            Owner’s verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

            - `last_setup_error.payment_method.card.wallet.visa_checkout.shipping_address.city` (nullable string)
              City, district, suburb, town, or village.

            - `last_setup_error.payment_method.card.wallet.visa_checkout.shipping_address.country` (nullable string)
              Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

            - `last_setup_error.payment_method.card.wallet.visa_checkout.shipping_address.line1` (nullable string)
              Address line 1 (e.g., street, PO Box, or company name).

            - `last_setup_error.payment_method.card.wallet.visa_checkout.shipping_address.line2` (nullable string)
              Address line 2 (e.g., apartment, suite, unit, or building).

            - `last_setup_error.payment_method.card.wallet.visa_checkout.shipping_address.postal_code` (nullable string)
              ZIP or postal code.

            - `last_setup_error.payment_method.card.wallet.visa_checkout.shipping_address.state` (nullable string)
              State, county, province, or region.

    - `last_setup_error.payment_method.card_present` (nullable object)
      If this is a `card_present` PaymentMethod, this hash contains details about the Card Present payment method.

      - `last_setup_error.payment_method.card_present.brand` (nullable string)
        Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

      - `last_setup_error.payment_method.card_present.brand_product` (nullable string)
        The [product code](https://stripe.com/docs/card-product-codes) that identifies the specific program or product associated with a card.

      - `last_setup_error.payment_method.card_present.cardholder_name` (nullable string)
        The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.

      - `last_setup_error.payment_method.card_present.country` (nullable string)
        Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

      - `last_setup_error.payment_method.card_present.exp_month` (integer)
        Two-digit number representing the card’s expiration month.

      - `last_setup_error.payment_method.card_present.exp_year` (integer)
        Four-digit number representing the card’s expiration year.

      - `last_setup_error.payment_method.card_present.fingerprint` (nullable string)
        Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

        *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

      - `last_setup_error.payment_method.card_present.funding` (nullable string)
        Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

      - `last_setup_error.payment_method.card_present.last4` (nullable string)
        The last four digits of the card.

      - `last_setup_error.payment_method.card_present.networks` (nullable object)
        Contains information about card networks that can be used to process the payment.

        - `last_setup_error.payment_method.card_present.networks.available` (array of strings)
          All networks available for selection via [payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-card-network).

        - `last_setup_error.payment_method.card_present.networks.preferred` (nullable string)
          The preferred network for the card.

      - `last_setup_error.payment_method.card_present.offline` (nullable object)
        Details about payment methods collected offline.

        - `last_setup_error.payment_method.card_present.offline.stored_at` (nullable timestamp)
          Time at which the payment was collected while offline

        - `last_setup_error.payment_method.card_present.offline.type` (nullable enum)
          The method used to process this payment method offline. Only deferred is allowed.

      - `last_setup_error.payment_method.card_present.preferred_locales` (nullable array of strings)
        The languages that the issuing bank recommends using for localizing any customer-facing text, as read from the card. Referenced from EMV tag 5F2D, data encoded on the card’s chip.

      - `last_setup_error.payment_method.card_present.read_method` (nullable enum)
        How card details were read in this transaction.

        Inserting a chip card into the card reader.

        Tapping a contactless-enabled chip card or mobile wallet.

        Older standard for contactless payments that emulated a magnetic stripe read.

        When inserting a chip card fails three times in a row, fallback to a magnetic stripe read.

        Swiping a card using the magnetic stripe reader.

      - `last_setup_error.payment_method.card_present.wallet` (nullable object)
        If a mobile wallet was presented in the transaction, this contains the details of the mobile wallet.

        - `last_setup_error.payment_method.card_present.wallet.type` (enum)
          The type of mobile wallet, one of `apple_pay`, `google_pay`, `samsung_pay`, or `unknown`.

          Apple Pay is a mobile payment service by Apple.

          Google Pay is a mobile payment service by Google.

          Samsung Pay is a mobile payment service by Samsung Electronics.

          The wallet provider is unknown.

    - `last_setup_error.payment_method.cashapp` (nullable object)
      If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method.

      - `last_setup_error.payment_method.cashapp.buyer_id` (nullable string)
        A unique and immutable identifier assigned by Cash App to every buyer.

      - `last_setup_error.payment_method.cashapp.cashtag` (nullable string)
        A public identifier for buyers using Cash App.

    - `last_setup_error.payment_method.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `last_setup_error.payment_method.crypto` (nullable object)
      If this is a Crypto PaymentMethod, this hash contains details about the Crypto payment method.

    - `last_setup_error.payment_method.customer` (nullable string)
      The ID of the Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer.

    - `last_setup_error.payment_method.customer_balance` (nullable object)
      If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method.

    - `last_setup_error.payment_method.eps` (nullable object)
      If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method.

      - `last_setup_error.payment_method.eps.bank` (nullable enum)
        The customer’s bank. Should be one of `arzte_und_apotheker_bank`, `austrian_anadi_bank_ag`, `bank_austria`, `bankhaus_carl_spangler`, `bankhaus_schelhammer_und_schattera_ag`, `bawag_psk_ag`, `bks_bank_ag`, `brull_kallmus_bank_ag`, `btv_vier_lander_bank`, `capital_bank_grawe_gruppe_ag`, `deutsche_bank_ag`, `dolomitenbank`, `easybank_ag`, `erste_bank_und_sparkassen`, `hypo_alpeadriabank_international_ag`, `hypo_noe_lb_fur_niederosterreich_u_wien`, `hypo_oberosterreich_salzburg_steiermark`, `hypo_tirol_bank_ag`, `hypo_vorarlberg_bank_ag`, `hypo_bank_burgenland_aktiengesellschaft`, `marchfelder_bank`, `oberbank_ag`, `raiffeisen_bankengruppe_osterreich`, `schoellerbank_ag`, `sparda_bank_wien`, `volksbank_gruppe`, `volkskreditbank_ag`, or `vr_bank_braunau`.

    - `last_setup_error.payment_method.fpx` (nullable object)
      If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method.

      - `last_setup_error.payment_method.fpx.bank` (enum)
        The customer’s bank, if provided. Can be one of `affin_bank`, `agrobank`, `alliance_bank`, `ambank`, `bank_islam`, `bank_muamalat`, `bank_rakyat`, `bsn`, `cimb`, `hong_leong_bank`, `hsbc`, `kfh`, `maybank2u`, `ocbc`, `public_bank`, `rhb`, `standard_chartered`, `uob`, `deutsche_bank`, `maybank2e`, `pb_enterprise`, or `bank_of_china`.

    - `last_setup_error.payment_method.giropay` (nullable object)
      If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method.

    - `last_setup_error.payment_method.grabpay` (nullable object)
      If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method.

    - `last_setup_error.payment_method.ideal` (nullable object)
      If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method.

      - `last_setup_error.payment_method.ideal.bank` (nullable enum)
        The customer’s bank, if provided. Can be one of `abn_amro`, `asn_bank`, `bunq`, `buut`, `handelsbanken`, `ing`, `knab`, `moneyou`, `n26`, `nn`, `rabobank`, `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, `van_lanschot`, or `yoursafe`.

      - `last_setup_error.payment_method.ideal.bic` (nullable enum)
        The Bank Identifier Code of the customer’s bank, if the bank was provided.

    - `last_setup_error.payment_method.kakao_pay` (nullable object)
      If this is a `kakao_pay` PaymentMethod, this hash contains details about the Kakao Pay payment method.

    - `last_setup_error.payment_method.klarna` (nullable object)
      If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method.

      - `last_setup_error.payment_method.klarna.dob` (nullable object)
        The customer’s date of birth, if provided.

        - `last_setup_error.payment_method.klarna.dob.day` (nullable integer)
          The day of birth, between 1 and 31.

        - `last_setup_error.payment_method.klarna.dob.month` (nullable integer)
          The month of birth, between 1 and 12.

        - `last_setup_error.payment_method.klarna.dob.year` (nullable integer)
          The four-digit year of birth.

    - `last_setup_error.payment_method.konbini` (nullable object)
      If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method.

    - `last_setup_error.payment_method.kr_card` (nullable object)
      If this is a `kr_card` PaymentMethod, this hash contains details about the Korean Card payment method.

      - `last_setup_error.payment_method.kr_card.brand` (nullable enum)
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

      - `last_setup_error.payment_method.kr_card.last4` (nullable string)
        The last four digits of the card. This may not be present for American Express cards.

    - `last_setup_error.payment_method.link` (nullable object)
      If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.

      - `last_setup_error.payment_method.link.email` (nullable string)
        Account owner’s email address.

    - `last_setup_error.payment_method.livemode` (boolean)
      Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

    - `last_setup_error.payment_method.metadata` (nullable object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `last_setup_error.payment_method.mobilepay` (nullable object)
      If this is a `mobilepay` PaymentMethod, this hash contains details about the MobilePay payment method.

    - `last_setup_error.payment_method.multibanco` (nullable object)
      If this is a `multibanco` PaymentMethod, this hash contains details about the Multibanco payment method.

    - `last_setup_error.payment_method.naver_pay` (nullable object)
      If this is a `naver_pay` PaymentMethod, this hash contains details about the Naver Pay payment method.

      - `last_setup_error.payment_method.naver_pay.buyer_id` (nullable string)
        Uniquely identifies this particular Naver Pay account. You can use this attribute to check whether two Naver Pay accounts are the same.

      - `last_setup_error.payment_method.naver_pay.funding` (enum)
        Whether to fund this transaction with Naver Pay points or a card.

        Use a card to fund this transaction.

        Use Naver Pay points to fund this transaction.

    - `last_setup_error.payment_method.nz_bank_account` (nullable object)
      If this is an nz_bank_account PaymentMethod, this hash contains details about the nz_bank_account payment method.

      - `last_setup_error.payment_method.nz_bank_account.account_holder_name` (nullable string)
        The name on the bank account. Only present if the account holder name is different from the name of the authorized signatory collected in the PaymentMethod’s billing details.

      - `last_setup_error.payment_method.nz_bank_account.bank_code` (string)
        The numeric code for the bank account’s bank.

      - `last_setup_error.payment_method.nz_bank_account.bank_name` (string)
        The name of the bank.

      - `last_setup_error.payment_method.nz_bank_account.branch_code` (string)
        The numeric code for the bank account’s bank branch.

      - `last_setup_error.payment_method.nz_bank_account.last4` (string)
        Last four digits of the bank account number.

      - `last_setup_error.payment_method.nz_bank_account.suffix` (nullable string)
        The suffix of the bank account number.

    - `last_setup_error.payment_method.oxxo` (nullable object)
      If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method.

    - `last_setup_error.payment_method.p24` (nullable object)
      If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method.

      - `last_setup_error.payment_method.p24.bank` (nullable enum)
        The customer’s bank, if provided.

    - `last_setup_error.payment_method.pay_by_bank` (nullable object)
      If this is a `pay_by_bank` PaymentMethod, this hash contains details about the PayByBank payment method.

    - `last_setup_error.payment_method.payco` (nullable object)
      If this is a `payco` PaymentMethod, this hash contains details about the PAYCO payment method.

    - `last_setup_error.payment_method.paynow` (nullable object)
      If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method.

    - `last_setup_error.payment_method.paypal` (nullable object)
      If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method.

      - `last_setup_error.payment_method.paypal.country` (nullable string)
        Two-letter ISO code representing the buyer’s country. Values are provided by PayPal directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

      - `last_setup_error.payment_method.paypal.payer_email` (nullable string)
        Owner’s email. Values are provided by PayPal directly
        (if supported) at the time of authorization or settlement. They cannot be set or mutated.

      - `last_setup_error.payment_method.paypal.payer_id` (nullable string)
        PayPal account PayerID. This identifier uniquely identifies the PayPal customer.

    - `last_setup_error.payment_method.pix` (nullable object)
      If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method.

    - `last_setup_error.payment_method.promptpay` (nullable object)
      If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method.

    - `last_setup_error.payment_method.radar_options` (nullable object)
      Options to configure Radar. See [Radar Session](https://docs.stripe.com/docs/radar/radar-session.md) for more information.

      - `last_setup_error.payment_method.radar_options.session` (nullable string)
        A [Radar Session](https://docs.stripe.com/docs/radar/radar-session.md) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.

    - `last_setup_error.payment_method.revolut_pay` (nullable object)
      If this is a `revolut_pay` PaymentMethod, this hash contains details about the Revolut Pay payment method.

    - `last_setup_error.payment_method.samsung_pay` (nullable object)
      If this is a `samsung_pay` PaymentMethod, this hash contains details about the SamsungPay payment method.

    - `last_setup_error.payment_method.satispay` (nullable object)
      If this is a `satispay` PaymentMethod, this hash contains details about the Satispay payment method.

    - `last_setup_error.payment_method.sepa_debit` (nullable object)
      If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account.

      - `last_setup_error.payment_method.sepa_debit.bank_code` (nullable string)
        Bank code of bank associated with the bank account.

      - `last_setup_error.payment_method.sepa_debit.branch_code` (nullable string)
        Branch code of bank associated with the bank account.

      - `last_setup_error.payment_method.sepa_debit.country` (nullable string)
        Two-letter ISO code representing the country the bank account is located in.

      - `last_setup_error.payment_method.sepa_debit.fingerprint` (nullable string)
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

      - `last_setup_error.payment_method.sepa_debit.generated_from` (nullable object)
        Information about the object that generated this PaymentMethod.

        - `last_setup_error.payment_method.sepa_debit.generated_from.charge` (nullable string)
          The ID of the Charge that generated this PaymentMethod, if any.

        - `last_setup_error.payment_method.sepa_debit.generated_from.setup_attempt` (nullable string)
          The ID of the SetupAttempt that generated this PaymentMethod, if any.

      - `last_setup_error.payment_method.sepa_debit.last4` (nullable string)
        Last four characters of the IBAN.

    - `last_setup_error.payment_method.sofort` (nullable object)
      If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method.

      - `last_setup_error.payment_method.sofort.country` (nullable string)
        Two-letter ISO code representing the country the bank account is located in.

    - `last_setup_error.payment_method.swish` (nullable object)
      If this is a `swish` PaymentMethod, this hash contains details about the Swish payment method.

    - `last_setup_error.payment_method.twint` (nullable object)
      If this is a TWINT PaymentMethod, this hash contains details about the TWINT payment method.

    - `last_setup_error.payment_method.type` (enum)
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

    - `last_setup_error.payment_method.us_bank_account` (nullable object)
      If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.

      - `last_setup_error.payment_method.us_bank_account.account_holder_type` (nullable enum)
        Account holder type: individual or company.

        Account belongs to a company

        Account belongs to an individual

      - `last_setup_error.payment_method.us_bank_account.account_type` (nullable enum)
        Account type: checkings or savings. Defaults to checking if omitted.

        Bank account type is checking

        Bank account type is savings

      - `last_setup_error.payment_method.us_bank_account.bank_name` (nullable string)
        The name of the bank.

      - `last_setup_error.payment_method.us_bank_account.financial_connections_account` (nullable string)
        The ID of the Financial Connections Account used to create the payment method.

      - `last_setup_error.payment_method.us_bank_account.fingerprint` (nullable string)
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

      - `last_setup_error.payment_method.us_bank_account.last4` (nullable string)
        Last four digits of the bank account number.

      - `last_setup_error.payment_method.us_bank_account.networks` (nullable object)
        Contains information about US bank account networks that can be used.

        - `last_setup_error.payment_method.us_bank_account.networks.preferred` (nullable string)
          The preferred network.

        - `last_setup_error.payment_method.us_bank_account.networks.supported` (array of enums)
          All supported networks.

      - `last_setup_error.payment_method.us_bank_account.routing_number` (nullable string)
        Routing number of the bank account.

      - `last_setup_error.payment_method.us_bank_account.status_details` (nullable object)
        Contains information about the future reusability of this PaymentMethod.

        - `last_setup_error.payment_method.us_bank_account.status_details.blocked` (nullable object)
          Contains more information about the underlying block.
          This field will only be rendered if the PaymentMethod is blocked.

          - `last_setup_error.payment_method.us_bank_account.status_details.blocked.network_code` (nullable enum)
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

          - `last_setup_error.payment_method.us_bank_account.status_details.blocked.reason` (nullable enum)
            The reason why this PaymentMethod’s fingerprint has been blocked

            Bank account has been closed.

            Bank account has been frozen.

            Bank account details are incorrect. Please check the account number, routing number, account holder name, and account type.

            Bank account does not support debits.

            Bank account has been blocked by Stripe. Please contact Support.

            Customer has disputed a previous payment with their bank. If the `network_code` is R29, please confirm that Stripe’s Company IDs are allowlisted before attempting additional payments.

    - `last_setup_error.payment_method.wechat_pay` (nullable object)
      If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method.

    - `last_setup_error.payment_method.zip` (nullable object)
      If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method.

  - `last_setup_error.payment_method_type` (nullable string)
    If the error is specific to the type of payment method, the payment method type that had a problem. This field is only populated for invoice-related errors.

  - `last_setup_error.type` (enum)
    The type of error returned. One of `api_error`, `card_error`, `idempotency_error`, or `invalid_request_error`

- `latest_attempt` (nullable string)
  The most recent SetupAttempt for this SetupIntent.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `mandate` (nullable string)
  ID of the multi use Mandate generated by the SetupIntent.

- `metadata` (nullable object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `next_action` (nullable object)
  If present, this property tells you what actions you need to take in order for your customer to continue payment setup.

  - `next_action.cashapp_handle_redirect_or_display_qr_code` (nullable object)
    The field that contains Cash App Pay QR code info

    - `next_action.cashapp_handle_redirect_or_display_qr_code.hosted_instructions_url` (string)
      The URL to the hosted Cash App Pay instructions page, which allows customers to view the QR code, and supports QR code refreshing on expiration.

    - `next_action.cashapp_handle_redirect_or_display_qr_code.mobile_auth_url` (string)
      The url for mobile redirect based auth

    - `next_action.cashapp_handle_redirect_or_display_qr_code.qr_code` (object)
      The field that contains CashApp QR code info

      - `next_action.cashapp_handle_redirect_or_display_qr_code.qr_code.expires_at` (timestamp)
        The date (unix timestamp) when the QR code expires.

      - `next_action.cashapp_handle_redirect_or_display_qr_code.qr_code.image_url_png` (string)
        The image_url_png string used to render QR code

      - `next_action.cashapp_handle_redirect_or_display_qr_code.qr_code.image_url_svg` (string)
        The image_url_svg string used to render QR code

  - `next_action.redirect_to_url` (nullable object)
    Contains instructions for authenticating a payment by redirecting your customer to another page or application.

    - `next_action.redirect_to_url.return_url` (nullable string)
      If the customer does not exit their browser while authenticating, they will be redirected to this specified URL after completion.

    - `next_action.redirect_to_url.url` (nullable string)
      The URL you must redirect your customer to in order to authenticate.

  - `next_action.type` (string)
    Type of the next action to perform. Refer to the other child attributes under `next_action` for available values. Examples include: `redirect_to_url`, `use_stripe_sdk`, `alipay_handle_redirect`, `oxxo_display_details`, or `verify_with_microdeposits`.

  - `next_action.use_stripe_sdk` (nullable object)
    When confirming a SetupIntent with Stripe.js, Stripe.js depends on the contents of this dictionary to invoke authentication flows. The shape of the contents is subject to change and is only intended to be used by Stripe.js.

  - `next_action.verify_with_microdeposits` (nullable object)
    Contains details describing microdeposits verification flow.

    - `next_action.verify_with_microdeposits.arrival_date` (timestamp)
      The timestamp when the microdeposits are expected to land.

    - `next_action.verify_with_microdeposits.hosted_verification_url` (string)
      The URL for the hosted verification page, which allows customers to verify their bank account.

    - `next_action.verify_with_microdeposits.microdeposit_type` (nullable enum)
      The type of the microdeposit sent to the customer. Used to distinguish between different verification methods.

- `on_behalf_of` (nullable string)
  The account (if any) for which the setup is intended.

- `payment_method` (nullable string)
  ID of the payment method used with this SetupIntent. If the payment method is `card_present` and isn’t a digital wallet, then the [generated_card](https://docs.stripe.com/api/setup_attempts/object#setup_attempt_object-payment_method_details-card_present-generated_card) associated with the `latest_attempt` is attached to the Customer instead.

- `payment_method_configuration_details` (nullable object)
  Information about the [payment method configuration](https://docs.stripe.com/docs/api/payment_method_configurations.md) used for this Setup Intent.

  - `payment_method_configuration_details.id` (string)
    ID of the payment method configuration used.

  - `payment_method_configuration_details.parent` (nullable string)
    ID of the parent payment method configuration used.

- `payment_method_options` (nullable object)
  Payment method-specific configuration for this SetupIntent.

  - `payment_method_options.acss_debit` (nullable object)
    If the SetupIntent’s payment_method_types includes `acss_debit`, this hash contains the configurations that will be applied to each setup attempt of that type.

    - `payment_method_options.acss_debit.currency` (nullable enum)
      Currency supported by the bank account

      Canadian dollars

      US dollars

    - `payment_method_options.acss_debit.mandate_options` (nullable object)
      Additional fields for Mandate creation

      - `payment_method_options.acss_debit.mandate_options.custom_mandate_url` (nullable string)
        A URL for custom mandate text

      - `payment_method_options.acss_debit.mandate_options.default_for` (nullable array of enums)
        List of Stripe products where this mandate can be selected automatically.

        Enables payments for Stripe Invoices. ‘subscription’ must also be provided.

        Enables payments for Stripe Subscriptions. ‘invoice’ must also be provided.

      - `payment_method_options.acss_debit.mandate_options.interval_description` (nullable string)
        Description of the interval. Only required if the ‘payment_schedule’ parameter is ‘interval’ or ‘combined’.

      - `payment_method_options.acss_debit.mandate_options.payment_schedule` (nullable enum)
        Payment schedule for the mandate.

        Payments can be initiated at a pre-defined interval or sporadically

        Payments are initiated at a regular pre-defined interval

        Payments are initiated sporadically

      - `payment_method_options.acss_debit.mandate_options.transaction_type` (nullable enum)
        Transaction type of the mandate.

        Transactions are made for business reasons

        Transactions are made for personal reasons

    - `payment_method_options.acss_debit.verification_method` (nullable enum)
      Bank account verification method.

      Instant verification with fallback to microdeposits.

      Instant verification.

      Verification using microdeposits.

  - `payment_method_options.amazon_pay` (nullable object)
    If the SetupIntent’s payment_method_types includes `amazon_pay`, this hash contains the configurations that will be applied to each setup attempt of that type.

  - `payment_method_options.bacs_debit` (nullable object)
    If the SetupIntent’s payment_method_types includes `bacs_debit`, this hash contains the configurations that will be applied to each setup attempt of that type.

    - `payment_method_options.bacs_debit.mandate_options` (nullable object)
      Additional fields for Mandate creation

  - `payment_method_options.card` (nullable object)
    If the SetupIntent’s payment_method_types includes `card`, this hash contains the configurations that will be applied to each setup attempt of that type.

    - `payment_method_options.card.mandate_options` (nullable object)
      Configuration options for setting up an eMandate for cards issued in India.

      - `payment_method_options.card.mandate_options.amount` (integer)
        Amount to be charged for future payments.

      - `payment_method_options.card.mandate_options.amount_type` (enum)
        One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param.

      - `payment_method_options.card.mandate_options.currency` (enum)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `payment_method_options.card.mandate_options.description` (nullable string)
        A description of the mandate or subscription that is meant to be displayed to the customer.

      - `payment_method_options.card.mandate_options.end_date` (nullable timestamp)
        End date of the mandate or subscription. If not provided, the mandate will be active until canceled. If provided, end date should be after start date.

      - `payment_method_options.card.mandate_options.interval` (enum)
        Specifies payment frequency. One of `day`, `week`, `month`, `year`, or `sporadic`.

      - `payment_method_options.card.mandate_options.interval_count` (nullable integer)
        The number of intervals between payments. For example, `interval=month` and `interval_count=3` indicates one payment every three months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks). This parameter is optional when `interval=sporadic`.

      - `payment_method_options.card.mandate_options.reference` (string)
        Unique identifier for the mandate or subscription.

      - `payment_method_options.card.mandate_options.start_date` (timestamp)
        Start date of the mandate or subscription. Start date should not be lesser than yesterday.

      - `payment_method_options.card.mandate_options.supported_types` (nullable array of enums)
        Specifies the type of mandates supported. Possible values are `india`.

    - `payment_method_options.card.network` (nullable enum)
      Selected network to process this SetupIntent on. Depends on the available networks of the card attached to the setup intent. Can be only set confirm-time.

    - `payment_method_options.card.request_three_d_secure` (nullable enum)
      We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://docs.stripe.com/docs/strong-customer-authentication.md). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. If not provided, this value defaults to `automatic`. Read our guide on [manually requesting 3D Secure](https://docs.stripe.com/docs/payments/3d-secure/authentication-flow.md#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.

      Use `any` to manually request 3DS with a preference for a `frictionless` flow, increasing the likelihood of the authentication being completed without any additional input from the customer.
      3DS will always be attempted if it is supported for the card, but Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow.
      To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

      (Default) Our SCA Engine automatically prompts your customers for authentication based on risk level and other requirements.

      Use `challenge` to request 3DS with a preference for a `challenge` flow, where the customer must respond to a prompt for active authentication. Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow. To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

  - `payment_method_options.card_present` (nullable object)
    If the SetupIntent’s payment_method_types includes `card_present`, this hash contains the configurations that will be applied to each setup attempt of that type.

  - `payment_method_options.klarna` (nullable object)
    If the SetupIntent’s payment_method_types includes `klarna`, this hash contains the configurations that will be applied to each setup attempt of that type.

    - `payment_method_options.klarna.currency` (nullable enum)
      The currency of the setup intent. Three letter ISO currency code.

    - `payment_method_options.klarna.preferred_locale` (nullable string)
      Preferred locale of the Klarna checkout page that the customer is redirected to.

  - `payment_method_options.link` (nullable object)
    If the SetupIntent’s payment_method_types includes `link`, this hash contains the configurations that will be applied to each setup attempt of that type.

  - `payment_method_options.paypal` (nullable object)
    If the SetupIntent’s payment_method_types includes `paypal`, this hash contains the configurations that will be applied to each setup attempt of that type.

    - `payment_method_options.paypal.billing_agreement_id` (nullable string)
      The PayPal Billing Agreement ID (BAID). This is an ID generated by PayPal which represents the mandate between the merchant and the customer.

  - `payment_method_options.sepa_debit` (nullable object)
    If the SetupIntent’s payment_method_types includes `sepa_debit`, this hash contains the configurations that will be applied to each setup attempt of that type.

    - `payment_method_options.sepa_debit.mandate_options` (nullable object)
      Additional fields for Mandate creation

  - `payment_method_options.us_bank_account` (nullable object)
    If the SetupIntent’s payment_method_types includes `us_bank_account`, this hash contains the configurations that will be applied to each setup attempt of that type.

    - `payment_method_options.us_bank_account.financial_connections` (nullable object)
      Additional fields for Financial Connections Session creation

      - `payment_method_options.us_bank_account.financial_connections.filters` (nullable object)
        Filter the list of accounts that are allowed to be linked.

        - `payment_method_options.us_bank_account.financial_connections.filters.account_subcategories` (nullable array of enums)
          The account subcategories to use to filter for possible accounts to link. Valid subcategories are `checking` and `savings`.

          Bank account subcategory is checking

          Bank account subcategory is savings

      - `payment_method_options.us_bank_account.financial_connections.permissions` (nullable array of enums)
        The list of permissions to request. The `payment_method` permission must be included.

        Allows accessing balance data from the account.

        Allows accessing ownership data from the account.

        Allows the creation of a payment method from the account.

        Allows accessing transactions data from the account.

      - `payment_method_options.us_bank_account.financial_connections.prefetch` (nullable array of enums)
        Data features requested to be retrieved upon account creation.

        Requests to prefetch balance data on accounts collected in this session.

        Requests to prefetch ownership data on accounts collected in this session.

        Requests to prefetch transaction data on accounts collected in this session.

      - `payment_method_options.us_bank_account.financial_connections.return_url` (nullable string)
        For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app.

    - `payment_method_options.us_bank_account.mandate_options` (nullable object)
      Additional fields for Mandate creation

      - `payment_method_options.us_bank_account.mandate_options.collection_method` (nullable enum)
        Mandate collection method

        Mandate customer acceptance was collected using a paper document

    - `payment_method_options.us_bank_account.verification_method` (nullable enum)
      Bank account verification method.

      Instant verification with fallback to microdeposits.

      Instant verification only.

      Verification using microdeposits. Cannot be used with Stripe Checkout, Hosted Invoices, or Payment Element.

- `payment_method_types` (array of strings)
  The list of payment method types (e.g. card) that this SetupIntent is allowed to set up. A list of valid payment method types can be found [here](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type).

- `single_use_mandate` (nullable string)
  ID of the single_use Mandate generated by the SetupIntent.

- `status` (enum)
  [Status](https://docs.stripe.com/docs/payments/intents.md#intent-statuses) of this SetupIntent, one of `requires_payment_method`, `requires_confirmation`, `requires_action`, `processing`, `canceled`, or `succeeded`.

- `usage` (string)
  Indicates how the payment method is intended to be used in the future.

  Use `on_session` if you intend to only reuse the payment method when the customer is in your checkout flow. Use `off_session` if your customer may or may not be in your checkout flow. If not provided, this value defaults to `off_session`.

### The SetupIntent object

```json
{
  "id": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG",
  "object": "setup_intent",
  "application": null,
  "cancellation_reason": null,
  "client_secret": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe",
  "created": 1678942624,
  "customer": null,
  "description": null,
  "flow_directions": null,
  "last_setup_error": null,
  "latest_attempt": null,
  "livemode": false,
  "mandate": null,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": null,
  "payment_method_options": {
    "card": {
      "mandate_options": null,
      "network": null,
      "request_three_d_secure": "automatic"
    }
  },
  "payment_method_types": [
    "card"
  ],
  "single_use_mandate": null,
  "status": "requires_payment_method",
  "usage": "off_session"
}
```