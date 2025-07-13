# The Charge object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  Amount intended to be collected by this payment. A positive integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://docs.stripe.com/docs/currencies.md#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

- `amount_captured` (integer)
  Amount in  captured (can be less than the amount attribute on the charge if a partial capture was made).

- `amount_refunded` (integer)
  Amount in  refunded (can be less than the amount attribute on the charge if a partial refund was issued).

- `application` (nullable string)
  ID of the Connect application that created the charge.

- `application_fee` (nullable string)
  The application fee (if any) for the charge. [See the Connect documentation](https://docs.stripe.com/docs/connect/direct-charges.md#collect-fees) for details.

- `application_fee_amount` (nullable integer)
  The amount of the application fee (if any) requested for the charge. [See the Connect documentation](https://docs.stripe.com/docs/connect/direct-charges.md#collect-fees) for details.

- `balance_transaction` (nullable string)
  ID of the balance transaction that describes the impact of this charge on your account balance (not including refunds or disputes).

- `billing_details` (object)
  Billing information associated with the payment method at the time of the transaction.

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

- `calculated_statement_descriptor` (nullable string)
  The full statement descriptor that is passed to card networks, and that is displayed on your customers’ credit card and bank statements. Allows you to see what the statement descriptor looks like after the static and dynamic portions are combined. This value only exists for card payments.

- `captured` (boolean)
  If the charge was created without capturing, this Boolean represents whether it is still uncaptured or has since been captured.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `customer` (nullable string)
  ID of the customer this charge is for if one exists.

- `description` (nullable string)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `disputed` (boolean)
  Whether the charge has been disputed.

- `failure_balance_transaction` (nullable string)
  ID of the balance transaction that describes the reversal of the balance on your account due to payment failure.

- `failure_code` (nullable string)
  Error code explaining reason for charge failure if available (see [the errors section](https://docs.stripe.com/docs/error-codes.md) for a list of codes).

- `failure_message` (nullable string)
  Message to user further explaining reason for charge failure if available.

- `fraud_details` (nullable object)
  Information on fraud assessments for the charge.

  - `fraud_details.stripe_report` (nullable string)
    Assessments from Stripe. If set, the value is `fraudulent`.

  - `fraud_details.user_report` (nullable string)
    Assessments reported by you. If set, possible values of are `safe` and `fraudulent`.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `on_behalf_of` (nullable string)
  The account (if any) the charge was made on behalf of without triggering an automatic transfer. See the [Connect documentation](https://docs.stripe.com/docs/connect/separate-charges-and-transfers.md) for details.

- `outcome` (nullable object)
  Details about whether the payment was accepted, and why. See [understanding declines](https://docs.stripe.com/docs/declines.md) for details.

  - `outcome.advice_code` (nullable enum)
    An enumerated value providing a more detailed explanation on [how to proceed with an error](https://docs.stripe.com/docs/declines.md#retrying-issuer-declines).

  - `outcome.network_advice_code` (nullable string)
    For charges declined by the network, a 2 digit code which indicates the advice returned by the network on how to proceed with an error.

  - `outcome.network_decline_code` (nullable string)
    For charges declined by the network, a brand specific 2, 3, or 4 digit code which indicates the reason the authorization failed.

  - `outcome.network_status` (nullable string)
    Possible values are `approved_by_network`, `declined_by_network`, `not_sent_to_network`, and `reversed_after_approval`. The value `reversed_after_approval` indicates the payment was [blocked by Stripe](https://docs.stripe.com/docs/declines.md#blocked-payments) after bank authorization, and may temporarily appear as “pending” on a cardholder’s statement.

  - `outcome.reason` (nullable string)
    An enumerated value providing a more detailed explanation of the outcome’s `type`. Charges blocked by Radar’s default block rule have the value `highest_risk_level`. Charges placed in review by Radar’s default review rule have the value `elevated_risk_level`. Charges authorized, blocked, or placed in review by custom rules have the value `rule`. See [understanding declines](https://docs.stripe.com/docs/declines.md) for more details.

  - `outcome.risk_level` (nullable string)
    Stripe Radar’s evaluation of the riskiness of the payment. Possible values for evaluated payments are `normal`, `elevated`, `highest`. For non-card payments, and card-based payments predating the public assignment of risk levels, this field will have the value `not_assessed`. In the event of an error in the evaluation, this field will have the value `unknown`. This field is only available with Radar.

  - `outcome.risk_score` (nullable integer)
    Stripe Radar’s evaluation of the riskiness of the payment. Possible values for evaluated payments are between 0 and 100. For non-card payments, card-based payments predating the public assignment of risk scores, or in the event of an error during evaluation, this field will not be present. This field is only available with Radar for Fraud Teams.

  - `outcome.rule` (nullable string)
    The ID of the Radar rule that matched the payment, if applicable.

  - `outcome.seller_message` (nullable string)
    A human-readable description of the outcome type and reason, designed for you (the recipient of the payment), not your customer.

  - `outcome.type` (string)
    Possible values are `authorized`, `manual_review`, `issuer_declined`, `blocked`, and `invalid`. See [understanding declines](https://docs.stripe.com/docs/declines.md) and [Radar reviews](https://docs.stripe.com/docs/radar/reviews.md) for details.

- `paid` (boolean)
  `true` if the charge succeeded, or was successfully authorized for later capture.

- `payment_intent` (nullable string)
  ID of the PaymentIntent associated with this charge, if one exists.

- `payment_method` (nullable string)
  ID of the payment method used in this charge.

- `payment_method_details` (nullable object)
  Details about the payment method at the time of the transaction.

  - `payment_method_details.ach_credit_transfer` (nullable object)
    If this is a `ach_credit_transfer` payment, this hash contains a snapshot of the transaction specific details of the `ach_credit_transfer` payment method.

    - `payment_method_details.ach_credit_transfer.account_number` (nullable string)
      Account number to transfer funds to.

    - `payment_method_details.ach_credit_transfer.bank_name` (nullable string)
      Name of the bank associated with the routing number.

    - `payment_method_details.ach_credit_transfer.routing_number` (nullable string)
      Routing transit number for the bank account to transfer funds to.

    - `payment_method_details.ach_credit_transfer.swift_code` (nullable string)
      SWIFT code of the bank associated with the routing number.

  - `payment_method_details.ach_debit` (nullable object)
    If this is a `ach_debit` payment, this hash contains a snapshot of the transaction specific details of the `ach_debit` payment method.

    - `payment_method_details.ach_debit.account_holder_type` (nullable enum)
      Type of entity that holds the account. This can be either `individual` or `company`.

    - `payment_method_details.ach_debit.bank_name` (nullable string)
      Name of the bank associated with the bank account.

    - `payment_method_details.ach_debit.country` (nullable string)
      Two-letter ISO code representing the country the bank account is located in.

    - `payment_method_details.ach_debit.fingerprint` (nullable string)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `payment_method_details.ach_debit.last4` (nullable string)
      Last four digits of the bank account number.

    - `payment_method_details.ach_debit.routing_number` (nullable string)
      Routing transit number of the bank account.

  - `payment_method_details.acss_debit` (nullable object)
    If this is a `acss_debit` payment, this hash contains a snapshot of the transaction specific details of the `acss_debit` payment method.

    - `payment_method_details.acss_debit.bank_name` (nullable string)
      Name of the bank associated with the bank account.

    - `payment_method_details.acss_debit.fingerprint` (nullable string)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `payment_method_details.acss_debit.institution_number` (nullable string)
      Institution number of the bank account

    - `payment_method_details.acss_debit.last4` (nullable string)
      Last four digits of the bank account number.

    - `payment_method_details.acss_debit.mandate` (nullable string)
      ID of the mandate used to make this payment.

    - `payment_method_details.acss_debit.transit_number` (nullable string)
      Transit number of the bank account.

  - `payment_method_details.affirm` (nullable object)
    If this is a `affirm` payment, this hash contains a snapshot of the transaction specific details of the `affirm` payment method.

    - `payment_method_details.affirm.transaction_id` (nullable string)
      The Affirm transaction ID associated with this payment.

  - `payment_method_details.afterpay_clearpay` (nullable object)
    If this is a `afterpay_clearpay` payment, this hash contains a snapshot of the transaction specific details of the `afterpay_clearpay` payment method.

    - `payment_method_details.afterpay_clearpay.order_id` (nullable string)
      The Afterpay order ID associated with this payment intent.

    - `payment_method_details.afterpay_clearpay.reference` (nullable string)
      Order identifier shown to the merchant in Afterpay’s online portal.

  - `payment_method_details.alipay` (nullable object)
    If this is a `alipay` payment, this hash contains a snapshot of the transaction specific details of the `alipay` payment method.

    - `payment_method_details.alipay.buyer_id` (nullable string)
      Uniquely identifies this particular Alipay account. You can use this attribute to check whether two Alipay accounts are the same.

    - `payment_method_details.alipay.fingerprint` (nullable string)
      Uniquely identifies this particular Alipay account. You can use this attribute to check whether two Alipay accounts are the same.

    - `payment_method_details.alipay.transaction_id` (nullable string)
      Transaction ID of this particular Alipay transaction.

  - `payment_method_details.alma` (nullable object)
    If this is a `alma` payment, this hash contains a snapshot of the transaction specific details of the `alma` payment method.

  - `payment_method_details.amazon_pay` (nullable object)
    If this is a `amazon_pay` payment, this hash contains a snapshot of the transaction specific details of the `amazon_pay` payment method.

    - `payment_method_details.amazon_pay.funding` (nullable object)
      the funding details of the underlying payment method.

      - `payment_method_details.amazon_pay.funding.card` (nullable object)
        the funding details of the passthrough card.

        - `payment_method_details.amazon_pay.funding.card.brand` (nullable string)
          Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

        - `payment_method_details.amazon_pay.funding.card.country` (nullable string)
          Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

        - `payment_method_details.amazon_pay.funding.card.exp_month` (nullable integer)
          Two-digit number representing the card’s expiration month.

        - `payment_method_details.amazon_pay.funding.card.exp_year` (nullable integer)
          Four-digit number representing the card’s expiration year.

        - `payment_method_details.amazon_pay.funding.card.funding` (nullable string)
          Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

        - `payment_method_details.amazon_pay.funding.card.last4` (nullable string)
          The last four digits of the card.

      - `payment_method_details.amazon_pay.funding.type` (nullable enum)
        funding type of the underlying payment method.

  - `payment_method_details.au_becs_debit` (nullable object)
    If this is a `au_becs_debit` payment, this hash contains a snapshot of the transaction specific details of the `au_becs_debit` payment method.

    - `payment_method_details.au_becs_debit.bsb_number` (nullable string)
      Bank-State-Branch number of the bank account.

    - `payment_method_details.au_becs_debit.fingerprint` (nullable string)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `payment_method_details.au_becs_debit.last4` (nullable string)
      Last four digits of the bank account number.

    - `payment_method_details.au_becs_debit.mandate` (nullable string)
      ID of the mandate used to make this payment.

  - `payment_method_details.bacs_debit` (nullable object)
    If this is a `bacs_debit` payment, this hash contains a snapshot of the transaction specific details of the `bacs_debit` payment method.

    - `payment_method_details.bacs_debit.fingerprint` (nullable string)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `payment_method_details.bacs_debit.last4` (nullable string)
      Last four digits of the bank account number.

    - `payment_method_details.bacs_debit.mandate` (nullable string)
      ID of the mandate used to make this payment.

    - `payment_method_details.bacs_debit.sort_code` (nullable string)
      Sort code of the bank account. (e.g., `10-20-30`)

  - `payment_method_details.bancontact` (nullable object)
    If this is a `bancontact` payment, this hash contains a snapshot of the transaction specific details of the `bancontact` payment method.

    - `payment_method_details.bancontact.bank_code` (nullable string)
      Bank code of bank associated with the bank account.

    - `payment_method_details.bancontact.bank_name` (nullable string)
      Name of the bank associated with the bank account.

    - `payment_method_details.bancontact.bic` (nullable string)
      Bank Identifier Code of the bank associated with the bank account.

    - `payment_method_details.bancontact.generated_sepa_debit` (nullable string)
      The ID of the SEPA Direct Debit PaymentMethod which was generated by this Charge.

    - `payment_method_details.bancontact.generated_sepa_debit_mandate` (nullable string)
      The mandate for the SEPA Direct Debit PaymentMethod which was generated by this Charge.

    - `payment_method_details.bancontact.iban_last4` (nullable string)
      Last four characters of the IBAN.

    - `payment_method_details.bancontact.preferred_language` (nullable enum)
      Preferred language of the Bancontact authorization page that the customer is redirected to.
      Can be one of `en`, `de`, `fr`, or `nl`

    - `payment_method_details.bancontact.verified_name` (nullable string)
      Owner’s verified full name. Values are verified or provided by Bancontact directly
      (if supported) at the time of authorization or settlement. They cannot be set or mutated.

  - `payment_method_details.billie` (nullable object)
    If this is a `billie` payment, this hash contains a snapshot of the transaction specific details of the `billie` payment method.

  - `payment_method_details.boleto` (nullable object)
    If this is a `boleto` payment, this hash contains a snapshot of the transaction specific details of the `boleto` payment method.

    - `payment_method_details.boleto.tax_id` (string)
      The tax ID of the customer (CPF for individuals consumers or CNPJ for businesses consumers)

  - `payment_method_details.card` (nullable object)
    If this is a `card` payment, this hash contains a snapshot of the transaction specific details of the `card` payment method.

    - `payment_method_details.card.amount_authorized` (nullable integer)
      The authorized amount.

    - `payment_method_details.card.authorization_code` (nullable string)
      Authorization code on the charge.

    - `payment_method_details.card.brand` (nullable string)
      Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

    - `payment_method_details.card.capture_before` (nullable timestamp)
      When using manual capture, a future timestamp at which the charge will be automatically refunded if uncaptured.

    - `payment_method_details.card.checks` (nullable object)
      Check results by Card networks on Card address and CVC at time of payment.

      - `payment_method_details.card.checks.address_line1_check` (nullable string)
        If a address line1 was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.

      - `payment_method_details.card.checks.address_postal_code_check` (nullable string)
        If a address postal code was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.

      - `payment_method_details.card.checks.cvc_check` (nullable string)
        If a CVC was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.

    - `payment_method_details.card.country` (nullable string)
      Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

    - `payment_method_details.card.exp_month` (integer)
      Two-digit number representing the card’s expiration month.

    - `payment_method_details.card.exp_year` (integer)
      Four-digit number representing the card’s expiration year.

    - `payment_method_details.card.extended_authorization` (nullable object)
      Whether the capture window of this charge is extended.

      - `payment_method_details.card.extended_authorization.status` (enum)
        Indicates whether or not the capture window is extended beyond the standard authorization.

        The capture window of the charge is not extended.

        The capture window of the charge is extended.

    - `payment_method_details.card.fingerprint` (nullable string)
      Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

      *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

    - `payment_method_details.card.funding` (nullable string)
      Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

    - `payment_method_details.card.incremental_authorization` (nullable object)
      Whether the authorized amount can be incremented or not.

      - `payment_method_details.card.incremental_authorization.status` (enum)
        Indicates whether or not the incremental authorization feature is supported.

        Incremental authorization is supported.

        Incremental authorization is not supported.

    - `payment_method_details.card.installments` (nullable object)
      Installment details for this payment.

      For more information, see the [installments integration guide](https://docs.stripe.com/docs/payments/installments.md).

      - `payment_method_details.card.installments.plan` (nullable object)
        Installment plan selected for the payment.

        - `payment_method_details.card.installments.plan.count` (nullable integer)
          For `fixed_count` installment plans, this is the number of installment payments your customer will make to their credit card.

        - `payment_method_details.card.installments.plan.interval` (nullable enum)
          For `fixed_count` installment plans, this is the interval between installment payments your customer will make to their credit card.
          One of `month`.

        - `payment_method_details.card.installments.plan.type` (enum)
          Type of installment plan, one of `fixed_count`, `bonus`, or `revolving`.

          An installment plan used in Japan, where the customer defers payment to a later date that aligns with their salary bonus.

          An installment plan where the number of installment payments is fixed and known at the time of purchase.

          An installment plan used in Japan, where the customer pays a certain amount each month, and the remaining balance rolls over to the next month.

    - `payment_method_details.card.last4` (nullable string)
      The last four digits of the card.

    - `payment_method_details.card.mandate` (nullable string)
      ID of the mandate used to make this payment or created by it.

    - `payment_method_details.card.multicapture` (nullable object)
      Information about the multicapture capability of the payment method.

      - `payment_method_details.card.multicapture.status` (enum)
        Indicates whether or not multiple captures are supported.

        Multiple captures are supported.

        Multiple captures are not supported.

    - `payment_method_details.card.network` (nullable string)
      Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.

    - `payment_method_details.card.network_transaction_id` (nullable string)
      This is used by the financial networks to identify a transaction. Visa calls this the Transaction ID, Mastercard calls this the Trace ID, and American Express calls this the Acquirer Reference Data. This value will be present if it is returned by the financial network in the authorization response, and null otherwise.

    - `payment_method_details.card.overcapture` (nullable object)
      Whether the authorized amount can be over-captured or not.

      - `payment_method_details.card.overcapture.maximum_amount_capturable` (integer)
        The maximum amount that can be captured.

      - `payment_method_details.card.overcapture.status` (enum)
        Indicates whether or not the authorized amount can be over-captured.

        The authorized amount can be over-captured.

        The authorized amount can’t be over-captured.

    - `payment_method_details.card.regulated_status` (nullable enum)
      Status of a card based on the card issuer.

      The card falls under a regulated account range.

      The card does not fall under a regulated account range.

    - `payment_method_details.card.three_d_secure` (nullable object)
      Populated if this transaction used 3D Secure authentication.

      - `payment_method_details.card.three_d_secure.authentication_flow` (nullable enum)
        For authenticated transactions: how the customer was authenticated by
        the issuing bank.

        The issuing bank authenticated the customer by presenting a traditional
        challenge window.

        The issuing bank authenticated the customer via the 3DS2 frictionless
        flow.

      - `payment_method_details.card.three_d_secure.electronic_commerce_indicator` (nullable enum)
        The Electronic Commerce Indicator (ECI). A protocol-level field
        indicating what degree of authentication was performed.

        **Mastercard variant:** Attempt acknowledged.

        **Mastercard variant:** Fully authenticated.

        Fully authenticated. The customer likely proved their identity to the
        issuing bank.

        Attempt acknowledged. The customer, or the entire issuing bank, is not
        set up for 3D Secure. Or the issuing bank is experiencing an outage.

        **Mastercard variant:** Acquirer SCA exemption.

        **Mastercard variant:** Fully authenticated recurring transaction.

      - `payment_method_details.card.three_d_secure.exemption_indicator` (nullable enum)
        The exemption requested via 3DS and accepted by the issuer at authentication time.

        Transaction Risk Analysis (TRA) was performed, a low risk exemption was requested via 3DS and granted by the issuer.

        No exemption was requested via 3DS; or, if requested, it was not granted by the issuer.

      - `payment_method_details.card.three_d_secure.exemption_indicator_applied` (nullable boolean)
        Whether Stripe requested the value of `exemption_indicator` in the transaction. This will depend on
        the outcome of Stripe’s internal risk assessment.

      - `payment_method_details.card.three_d_secure.result` (nullable enum)
        Indicates the outcome of 3D Secure authentication.

        The issuing bank does not support 3D Secure, has not set up 3D Secure
        for the card, or is experiencing an outage. No authentication was
        performed, but the card network has provided proof of the attempt.

        In most cases the attempt qualifies for liability shift and it is safe
        to make a charge.

        3D Secure authentication succeeded.

        A 3D Secure exemption has been applied to this transaction. Exemption
        may be requested for a number of reasons including merchant initiation,
        low value, or low risk.

        The customer failed 3D Secure authentication.

        3D Secure authentication cannot be run on this card. Liability will
        generally not be shifted to the issuer.

        The issuing bank’s 3D Secure system is temporarily unavailable and the
        card network is unable to provide proof of the attempt. Liability will
        generally not be shifted to the issuer.

      - `payment_method_details.card.three_d_secure.result_reason` (nullable enum)
        Additional information about why 3D Secure succeeded or failed based
        on the `result`.

        For `failed`. The transaction timed out: the cardholder dropped off
        before completing authentication.

        For `processing_error`. Stripe bypassed 3D Secure because the issuing
        bank’s web-facing server was returning errors or timeouts to customers
        in the challenge window.

        For `failed`. The cardholder canceled authentication (where possible to
        identify).

        For `not_supported`. The issuing bank does not support 3D Secure or has
        not set up 3D Secure for the card, and the card network did not provide
        proof of the attempt.

        This occurs when running 3D Secure on certain kinds of prepaid cards
        and in rare cases where the issuing bank is exempt from the requirement
        to support 3D Secure.

        For `not_supported`. Stripe does not support 3D Secure on this card
        network.

        For `processing_error`. An invalid message was received from the
        card network or issuing bank. (Includes “downgrades” and similar
        errors).

        For `failed`. The cardholder was redirected back from the issuing bank
        without completing authentication.

      - `payment_method_details.card.three_d_secure.transaction_id` (nullable string)
        The 3D Secure 1 XID or 3D Secure 2 Directory Server Transaction ID
        (dsTransId) for this payment.

      - `payment_method_details.card.three_d_secure.version` (nullable enum)
        The version of 3D Secure that was used.

    - `payment_method_details.card.wallet` (nullable object)
      If this Card is part of a card wallet, this contains the details of the card wallet.

      - `payment_method_details.card.wallet.amex_express_checkout` (nullable object)
        If this is a `amex_express_checkout` card wallet, this hash contains details about the wallet.

      - `payment_method_details.card.wallet.apple_pay` (nullable object)
        If this is a `apple_pay` card wallet, this hash contains details about the wallet.

      - `payment_method_details.card.wallet.dynamic_last4` (nullable string)
        (For tokenized numbers only.) The last four digits of the device account number.

      - `payment_method_details.card.wallet.google_pay` (nullable object)
        If this is a `google_pay` card wallet, this hash contains details about the wallet.

      - `payment_method_details.card.wallet.link` (nullable object)
        If this is a `link` card wallet, this hash contains details about the wallet.

      - `payment_method_details.card.wallet.masterpass` (nullable object)
        If this is a `masterpass` card wallet, this hash contains details about the wallet.

        - `payment_method_details.card.wallet.masterpass.billing_address` (nullable object)
          Owner’s verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

          - `payment_method_details.card.wallet.masterpass.billing_address.city` (nullable string)
            City, district, suburb, town, or village.

          - `payment_method_details.card.wallet.masterpass.billing_address.country` (nullable string)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `payment_method_details.card.wallet.masterpass.billing_address.line1` (nullable string)
            Address line 1 (e.g., street, PO Box, or company name).

          - `payment_method_details.card.wallet.masterpass.billing_address.line2` (nullable string)
            Address line 2 (e.g., apartment, suite, unit, or building).

          - `payment_method_details.card.wallet.masterpass.billing_address.postal_code` (nullable string)
            ZIP or postal code.

          - `payment_method_details.card.wallet.masterpass.billing_address.state` (nullable string)
            State, county, province, or region.

        - `payment_method_details.card.wallet.masterpass.email` (nullable string)
          Owner’s verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

        - `payment_method_details.card.wallet.masterpass.name` (nullable string)
          Owner’s verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

        - `payment_method_details.card.wallet.masterpass.shipping_address` (nullable object)
          Owner’s verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

          - `payment_method_details.card.wallet.masterpass.shipping_address.city` (nullable string)
            City, district, suburb, town, or village.

          - `payment_method_details.card.wallet.masterpass.shipping_address.country` (nullable string)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `payment_method_details.card.wallet.masterpass.shipping_address.line1` (nullable string)
            Address line 1 (e.g., street, PO Box, or company name).

          - `payment_method_details.card.wallet.masterpass.shipping_address.line2` (nullable string)
            Address line 2 (e.g., apartment, suite, unit, or building).

          - `payment_method_details.card.wallet.masterpass.shipping_address.postal_code` (nullable string)
            ZIP or postal code.

          - `payment_method_details.card.wallet.masterpass.shipping_address.state` (nullable string)
            State, county, province, or region.

      - `payment_method_details.card.wallet.samsung_pay` (nullable object)
        If this is a `samsung_pay` card wallet, this hash contains details about the wallet.

      - `payment_method_details.card.wallet.type` (enum)
        The type of the card wallet, one of `amex_express_checkout`, `apple_pay`, `google_pay`, `masterpass`, `samsung_pay`, `visa_checkout`, or `link`. An additional hash is included on the Wallet subhash with a name matching this value. It contains additional information specific to the card wallet type.

      - `payment_method_details.card.wallet.visa_checkout` (nullable object)
        If this is a `visa_checkout` card wallet, this hash contains details about the wallet.

        - `payment_method_details.card.wallet.visa_checkout.billing_address` (nullable object)
          Owner’s verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

          - `payment_method_details.card.wallet.visa_checkout.billing_address.city` (nullable string)
            City, district, suburb, town, or village.

          - `payment_method_details.card.wallet.visa_checkout.billing_address.country` (nullable string)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `payment_method_details.card.wallet.visa_checkout.billing_address.line1` (nullable string)
            Address line 1 (e.g., street, PO Box, or company name).

          - `payment_method_details.card.wallet.visa_checkout.billing_address.line2` (nullable string)
            Address line 2 (e.g., apartment, suite, unit, or building).

          - `payment_method_details.card.wallet.visa_checkout.billing_address.postal_code` (nullable string)
            ZIP or postal code.

          - `payment_method_details.card.wallet.visa_checkout.billing_address.state` (nullable string)
            State, county, province, or region.

        - `payment_method_details.card.wallet.visa_checkout.email` (nullable string)
          Owner’s verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

        - `payment_method_details.card.wallet.visa_checkout.name` (nullable string)
          Owner’s verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

        - `payment_method_details.card.wallet.visa_checkout.shipping_address` (nullable object)
          Owner’s verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

          - `payment_method_details.card.wallet.visa_checkout.shipping_address.city` (nullable string)
            City, district, suburb, town, or village.

          - `payment_method_details.card.wallet.visa_checkout.shipping_address.country` (nullable string)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `payment_method_details.card.wallet.visa_checkout.shipping_address.line1` (nullable string)
            Address line 1 (e.g., street, PO Box, or company name).

          - `payment_method_details.card.wallet.visa_checkout.shipping_address.line2` (nullable string)
            Address line 2 (e.g., apartment, suite, unit, or building).

          - `payment_method_details.card.wallet.visa_checkout.shipping_address.postal_code` (nullable string)
            ZIP or postal code.

          - `payment_method_details.card.wallet.visa_checkout.shipping_address.state` (nullable string)
            State, county, province, or region.

  - `payment_method_details.card_present` (nullable object)
    If this is a `card_present` payment, this hash contains a snapshot of the transaction specific details of the `card_present` payment method.

    - `payment_method_details.card_present.amount_authorized` (nullable integer)
      The authorized amount

    - `payment_method_details.card_present.brand` (nullable string)
      Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

    - `payment_method_details.card_present.brand_product` (nullable string)
      The [product code](https://stripe.com/docs/card-product-codes) that identifies the specific program or product associated with a card.

    - `payment_method_details.card_present.capture_before` (nullable timestamp)
      When using manual capture, a future timestamp after which the charge will be automatically refunded if uncaptured.

    - `payment_method_details.card_present.cardholder_name` (nullable string)
      The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.

    - `payment_method_details.card_present.country` (nullable string)
      Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

    - `payment_method_details.card_present.emv_auth_data` (nullable string)
      Authorization response cryptogram.

    - `payment_method_details.card_present.exp_month` (integer)
      Two-digit number representing the card’s expiration month.

    - `payment_method_details.card_present.exp_year` (integer)
      Four-digit number representing the card’s expiration year.

    - `payment_method_details.card_present.fingerprint` (nullable string)
      Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

      *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.*

    - `payment_method_details.card_present.funding` (nullable string)
      Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

    - `payment_method_details.card_present.generated_card` (nullable string)
      ID of a card PaymentMethod generated from the card_present PaymentMethod that may be attached to a Customer for future transactions. Only present if it was possible to generate a card PaymentMethod.

    - `payment_method_details.card_present.incremental_authorization_supported` (boolean)
      Whether this [PaymentIntent](https://docs.stripe.com/docs/api/payment_intents.md) is eligible for incremental authorizations. Request support using [request_incremental_authorization_support](https://docs.stripe.com/docs/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-request_incremental_authorization_support).

    - `payment_method_details.card_present.last4` (nullable string)
      The last four digits of the card.

    - `payment_method_details.card_present.network` (nullable string)
      Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.

    - `payment_method_details.card_present.network_transaction_id` (nullable string)
      This is used by the financial networks to identify a transaction. Visa calls this the Transaction ID, Mastercard calls this the Trace ID, and American Express calls this the Acquirer Reference Data. This value will be present if it is returned by the financial network in the authorization response, and null otherwise.

    - `payment_method_details.card_present.offline` (nullable object)
      Details about payments collected offline.

      - `payment_method_details.card_present.offline.stored_at` (nullable timestamp)
        Time at which the payment was collected while offline

      - `payment_method_details.card_present.offline.type` (nullable enum)
        The method used to process this payment method offline. Only deferred is allowed.

    - `payment_method_details.card_present.overcapture_supported` (boolean)
      Defines whether the authorized amount can be over-captured or not

    - `payment_method_details.card_present.preferred_locales` (nullable array of strings)
      The languages that the issuing bank recommends using for localizing any customer-facing text, as read from the card. Referenced from EMV tag 5F2D, data encoded on the card’s chip.

    - `payment_method_details.card_present.read_method` (nullable enum)
      How card details were read in this transaction.

      Inserting a chip card into the card reader.

      Tapping a contactless-enabled chip card or mobile wallet.

      Older standard for contactless payments that emulated a magnetic stripe read.

      When inserting a chip card fails three times in a row, fallback to a magnetic stripe read.

      Swiping a card using the magnetic stripe reader.

    - `payment_method_details.card_present.receipt` (nullable object)
      A collection of fields required to be displayed on receipts. Only required for EMV transactions.

      - `payment_method_details.card_present.receipt.account_type` (nullable enum)
        The type of account being debited or credited

        A checking account, as when using a debit card

        A credit account, as when using a credit card

        A prepaid account, as when using a debit gift card

        An unknown account

      - `payment_method_details.card_present.receipt.application_cryptogram` (nullable string)
        The Application Cryptogram, a unique value generated by the card to authenticate the transaction with issuers.

      - `payment_method_details.card_present.receipt.application_preferred_name` (nullable string)
        The Application Identifier (AID) on the card used to determine which networks are eligible to process the transaction. Referenced from EMV tag 9F12, data encoded on the card’s chip.

      - `payment_method_details.card_present.receipt.authorization_code` (nullable string)
        Identifier for this transaction.

      - `payment_method_details.card_present.receipt.authorization_response_code` (nullable string)
        EMV tag 8A. A code returned by the card issuer.

      - `payment_method_details.card_present.receipt.cardholder_verification_method` (nullable string)
        Describes the method used by the cardholder to verify ownership of the card. One of the following: `approval`, `failure`, `none`, `offline_pin`, `offline_pin_and_signature`, `online_pin`, or `signature`.

      - `payment_method_details.card_present.receipt.dedicated_file_name` (nullable string)
        Similar to the application_preferred_name, identifying the applications (AIDs) available on the card. Referenced from EMV tag 84.

      - `payment_method_details.card_present.receipt.terminal_verification_results` (nullable string)
        A 5-byte string that records the checks and validations that occur between the card and the terminal. These checks determine how the terminal processes the transaction and what risk tolerance is acceptable. Referenced from EMV Tag 95.

      - `payment_method_details.card_present.receipt.transaction_status_information` (nullable string)
        An indication of which steps were completed during the card read process. Referenced from EMV Tag 9B.

    - `payment_method_details.card_present.wallet` (nullable object)
      If a mobile wallet was presented in the transaction, this contains the details of the mobile wallet.

      - `payment_method_details.card_present.wallet.type` (enum)
        The type of mobile wallet, one of `apple_pay`, `google_pay`, `samsung_pay`, or `unknown`.

        Apple Pay is a mobile payment service by Apple.

        Google Pay is a mobile payment service by Google.

        Samsung Pay is a mobile payment service by Samsung Electronics.

        The wallet provider is unknown.

  - `payment_method_details.cashapp` (nullable object)
    If this is a `cashapp` payment, this hash contains a snapshot of the transaction specific details of the `cashapp` payment method.

    - `payment_method_details.cashapp.buyer_id` (nullable string)
      A unique and immutable identifier assigned by Cash App to every buyer.

    - `payment_method_details.cashapp.cashtag` (nullable string)
      A public identifier for buyers using Cash App.

  - `payment_method_details.crypto` (nullable object)
    If this is a `crypto` payment, this hash contains a snapshot of the transaction specific details of the `crypto` payment method.

    - `payment_method_details.crypto.buyer_address` (nullable string)
      The wallet address of the customer.

    - `payment_method_details.crypto.network` (nullable enum)
      The blockchain network that the transaction was sent on.

      Base

      Ethereum

      Polygon

    - `payment_method_details.crypto.token_currency` (nullable enum)
      The token currency that the transaction was sent with.

      USDC

      USDG

      USDP

    - `payment_method_details.crypto.transaction_hash` (nullable string)
      The blockchain transaction hash of the crypto payment.

  - `payment_method_details.customer_balance` (nullable object)
    If this is a `customer_balance` payment, this hash contains a snapshot of the transaction specific details of the `customer_balance` payment method.

  - `payment_method_details.eps` (nullable object)
    If this is a `eps` payment, this hash contains a snapshot of the transaction specific details of the `eps` payment method.

    - `payment_method_details.eps.bank` (nullable enum)
      The customer’s bank. Should be one of `arzte_und_apotheker_bank`, `austrian_anadi_bank_ag`, `bank_austria`, `bankhaus_carl_spangler`, `bankhaus_schelhammer_und_schattera_ag`, `bawag_psk_ag`, `bks_bank_ag`, `brull_kallmus_bank_ag`, `btv_vier_lander_bank`, `capital_bank_grawe_gruppe_ag`, `deutsche_bank_ag`, `dolomitenbank`, `easybank_ag`, `erste_bank_und_sparkassen`, `hypo_alpeadriabank_international_ag`, `hypo_noe_lb_fur_niederosterreich_u_wien`, `hypo_oberosterreich_salzburg_steiermark`, `hypo_tirol_bank_ag`, `hypo_vorarlberg_bank_ag`, `hypo_bank_burgenland_aktiengesellschaft`, `marchfelder_bank`, `oberbank_ag`, `raiffeisen_bankengruppe_osterreich`, `schoellerbank_ag`, `sparda_bank_wien`, `volksbank_gruppe`, `volkskreditbank_ag`, or `vr_bank_braunau`.

    - `payment_method_details.eps.verified_name` (nullable string)
      Owner’s verified full name. Values are verified or provided by EPS directly
      (if supported) at the time of authorization or settlement. They cannot be set or mutated.
      EPS rarely provides this information so the attribute is usually empty.

  - `payment_method_details.fpx` (nullable object)
    If this is a `fpx` payment, this hash contains a snapshot of the transaction specific details of the `fpx` payment method.

    - `payment_method_details.fpx.bank` (enum)
      The customer’s bank. Can be one of `affin_bank`, `agrobank`, `alliance_bank`, `ambank`, `bank_islam`, `bank_muamalat`, `bank_rakyat`, `bsn`, `cimb`, `hong_leong_bank`, `hsbc`, `kfh`, `maybank2u`, `ocbc`, `public_bank`, `rhb`, `standard_chartered`, `uob`, `deutsche_bank`, `maybank2e`, `pb_enterprise`, or `bank_of_china`.

    - `payment_method_details.fpx.transaction_id` (nullable string)
      Unique transaction id generated by FPX for every request from the merchant

  - `payment_method_details.giropay` (nullable object)
    If this is a `giropay` payment, this hash contains a snapshot of the transaction specific details of the `giropay` payment method.

    - `payment_method_details.giropay.bank_code` (nullable string)
      Bank code of bank associated with the bank account.

    - `payment_method_details.giropay.bank_name` (nullable string)
      Name of the bank associated with the bank account.

    - `payment_method_details.giropay.bic` (nullable string)
      Bank Identifier Code of the bank associated with the bank account.

    - `payment_method_details.giropay.verified_name` (nullable string)
      Owner’s verified full name. Values are verified or provided by Giropay directly
      (if supported) at the time of authorization or settlement. They cannot be set or mutated.
      Giropay rarely provides this information so the attribute is usually empty.

  - `payment_method_details.grabpay` (nullable object)
    If this is a `grabpay` payment, this hash contains a snapshot of the transaction specific details of the `grabpay` payment method.

    - `payment_method_details.grabpay.transaction_id` (nullable string)
      Unique transaction id generated by GrabPay

  - `payment_method_details.ideal` (nullable object)
    If this is a `ideal` payment, this hash contains a snapshot of the transaction specific details of the `ideal` payment method.

    - `payment_method_details.ideal.bank` (nullable enum)
      The customer’s bank. Can be one of `abn_amro`, `asn_bank`, `bunq`, `buut`, `handelsbanken`, `ing`, `knab`, `moneyou`, `n26`, `nn`, `rabobank`, `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, `van_lanschot`, or `yoursafe`.

    - `payment_method_details.ideal.bic` (nullable enum)
      The Bank Identifier Code of the customer’s bank.

    - `payment_method_details.ideal.generated_sepa_debit` (nullable string)
      The ID of the SEPA Direct Debit PaymentMethod which was generated by this Charge.

    - `payment_method_details.ideal.generated_sepa_debit_mandate` (nullable string)
      The mandate for the SEPA Direct Debit PaymentMethod which was generated by this Charge.

    - `payment_method_details.ideal.iban_last4` (nullable string)
      Last four characters of the IBAN.

    - `payment_method_details.ideal.verified_name` (nullable string)
      Owner’s verified full name. Values are verified or provided by iDEAL directly
      (if supported) at the time of authorization or settlement. They cannot be set or mutated.

  - `payment_method_details.kakao_pay` (nullable object)
    If this is a `kakao_pay` payment, this hash contains a snapshot of the transaction specific details of the `kakao_pay` payment method.

    - `payment_method_details.kakao_pay.buyer_id` (nullable string)
      A unique identifier for the buyer as determined by the local payment processor.

  - `payment_method_details.klarna` (nullable object)
    If this is a `klarna` payment, this hash contains a snapshot of the transaction specific details of the `klarna` payment method.

    - `payment_method_details.klarna.payer_details` (nullable object)
      The payer details for this transaction.

      - `payment_method_details.klarna.payer_details.address` (nullable object)
        The payer’s address

        - `payment_method_details.klarna.payer_details.address.country` (nullable string)
          The payer address country

    - `payment_method_details.klarna.payment_method_category` (nullable string)
      The Klarna payment method used for this transaction.
      Can be one of `pay_later`, `pay_now`, `pay_with_financing`, or `pay_in_installments`

    - `payment_method_details.klarna.preferred_locale` (nullable string)
      Preferred language of the Klarna authorization page that the customer is redirected to.
      Can be one of `de-AT`, `en-AT`, `nl-BE`, `fr-BE`, `en-BE`, `de-DE`, `en-DE`, `da-DK`, `en-DK`, `es-ES`, `en-ES`, `fi-FI`, `sv-FI`, `en-FI`, `en-GB`, `en-IE`, `it-IT`, `en-IT`, `nl-NL`, `en-NL`, `nb-NO`, `en-NO`, `sv-SE`, `en-SE`, `en-US`, `es-US`, `fr-FR`, `en-FR`, `cs-CZ`, `en-CZ`, `ro-RO`, `en-RO`, `el-GR`, `en-GR`, `en-AU`, `en-NZ`, `en-CA`, `fr-CA`, `pl-PL`, `en-PL`, `pt-PT`, `en-PT`, `de-CH`, `fr-CH`, `it-CH`, or `en-CH`

  - `payment_method_details.konbini` (nullable object)
    If this is a `konbini` payment, this hash contains a snapshot of the transaction specific details of the `konbini` payment method.

    - `payment_method_details.konbini.store` (nullable object)
      If the payment succeeded, this contains the details of the convenience store where the payment was completed.

      - `payment_method_details.konbini.store.chain` (nullable enum)
        The name of the convenience store chain where the payment was completed.

  - `payment_method_details.kr_card` (nullable object)
    If this is a `kr_card` payment, this hash contains a snapshot of the transaction specific details of the `kr_card` payment method.

    - `payment_method_details.kr_card.brand` (nullable enum)
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

    - `payment_method_details.kr_card.buyer_id` (nullable string)
      A unique identifier for the buyer as determined by the local payment processor.

    - `payment_method_details.kr_card.last4` (nullable string)
      The last four digits of the card. This may not be present for American Express cards.

  - `payment_method_details.link` (nullable object)
    If this is a `link` payment, this hash contains a snapshot of the transaction specific details of the `link` payment method.

    - `payment_method_details.link.country` (nullable string)
      Two-letter ISO code representing the funding source country beneath the Link payment.
      You could use this attribute to get a sense of international fees.

  - `payment_method_details.mobilepay` (nullable object)
    If this is a `mobilepay` payment, this hash contains a snapshot of the transaction specific details of the `mobilepay` payment method.

    - `payment_method_details.mobilepay.card` (nullable object)
      Internal card details

      - `payment_method_details.mobilepay.card.brand` (nullable string)
        Brand of the card used in the transaction

      - `payment_method_details.mobilepay.card.country` (nullable string)
        Two-letter ISO code representing the country of the card

      - `payment_method_details.mobilepay.card.exp_month` (nullable integer)
        Two digit number representing the card’s expiration month

      - `payment_method_details.mobilepay.card.exp_year` (nullable integer)
        Two digit number representing the card’s expiration year

      - `payment_method_details.mobilepay.card.last4` (nullable string)
        The last 4 digits of the card

  - `payment_method_details.multibanco` (nullable object)
    If this is a `multibanco` payment, this hash contains a snapshot of the transaction specific details of the `multibanco` payment method.

    - `payment_method_details.multibanco.entity` (nullable string)
      Entity number associated with this Multibanco payment.

    - `payment_method_details.multibanco.reference` (nullable string)
      Reference number associated with this Multibanco payment.

  - `payment_method_details.naver_pay` (nullable object)
    If this is a `naver_pay` payment, this hash contains a snapshot of the transaction specific details of the `naver_pay` payment method.

    - `payment_method_details.naver_pay.buyer_id` (nullable string)
      A unique identifier for the buyer as determined by the local payment processor.

  - `payment_method_details.nz_bank_account` (nullable object)
    If this is a `nz_bank_account` payment, this hash contains a snapshot of the transaction specific details of the `nz_bank_account` payment method.

    - `payment_method_details.nz_bank_account.account_holder_name` (nullable string)
      The name on the bank account. Only present if the account holder name is different from the name of the authorized signatory collected in the PaymentMethod’s billing details.

    - `payment_method_details.nz_bank_account.bank_code` (string)
      The numeric code for the bank account’s bank.

    - `payment_method_details.nz_bank_account.bank_name` (string)
      The name of the bank.

    - `payment_method_details.nz_bank_account.branch_code` (string)
      The numeric code for the bank account’s bank branch.

    - `payment_method_details.nz_bank_account.last4` (string)
      Last four digits of the bank account number.

    - `payment_method_details.nz_bank_account.suffix` (nullable string)
      The suffix of the bank account number.

  - `payment_method_details.oxxo` (nullable object)
    If this is a `oxxo` payment, this hash contains a snapshot of the transaction specific details of the `oxxo` payment method.

    - `payment_method_details.oxxo.number` (nullable string)
      OXXO reference number

  - `payment_method_details.p24` (nullable object)
    If this is a `p24` payment, this hash contains a snapshot of the transaction specific details of the `p24` payment method.

    - `payment_method_details.p24.bank` (nullable enum)
      The customer’s bank. Can be one of `ing`, `citi_handlowy`, `tmobile_usbugi_bankowe`, `plus_bank`, `etransfer_pocztowy24`, `banki_spbdzielcze`, `bank_nowy_bfg_sa`, `getin_bank`, `velobank`, `blik`, `noble_pay`, `ideabank`, `envelobank`, `santander_przelew24`, `nest_przelew`, `mbank_mtransfer`, `inteligo`, `pbac_z_ipko`, `bnp_paribas`, `credit_agricole`, `toyota_bank`, `bank_pekao_sa`, `volkswagen_bank`, `bank_millennium`, `alior_bank`, or `boz`.

    - `payment_method_details.p24.reference` (nullable string)
      Unique reference for this Przelewy24 payment.

    - `payment_method_details.p24.verified_name` (nullable string)
      Owner’s verified full name. Values are verified or provided by Przelewy24 directly
      (if supported) at the time of authorization or settlement. They cannot be set or mutated.
      Przelewy24 rarely provides this information so the attribute is usually empty.

  - `payment_method_details.pay_by_bank` (nullable object)
    If this is a `pay_by_bank` payment, this hash contains a snapshot of the transaction specific details of the `pay_by_bank` payment method.

  - `payment_method_details.payco` (nullable object)
    If this is a `payco` payment, this hash contains a snapshot of the transaction specific details of the `payco` payment method.

    - `payment_method_details.payco.buyer_id` (nullable string)
      A unique identifier for the buyer as determined by the local payment processor.

  - `payment_method_details.paynow` (nullable object)
    If this is a `paynow` payment, this hash contains a snapshot of the transaction specific details of the `paynow` payment method.

    - `payment_method_details.paynow.reference` (nullable string)
      Reference number associated with this PayNow payment

  - `payment_method_details.paypal` (nullable object)
    If this is a `paypal` payment, this hash contains a snapshot of the transaction specific details of the `paypal` payment method.

    - `payment_method_details.paypal.country` (nullable string)
      Two-letter ISO code representing the buyer’s country. Values are provided by PayPal directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.

    - `payment_method_details.paypal.payer_email` (nullable string)
      Owner’s email. Values are provided by PayPal directly
      (if supported) at the time of authorization or settlement. They cannot be set or mutated.

    - `payment_method_details.paypal.payer_id` (nullable string)
      PayPal account PayerID. This identifier uniquely identifies the PayPal customer.

    - `payment_method_details.paypal.payer_name` (nullable string)
      Owner’s full name. Values provided by PayPal directly
      (if supported) at the time of authorization or settlement. They cannot be set or mutated.

    - `payment_method_details.paypal.seller_protection` (nullable object)
      The level of protection offered as defined by PayPal Seller Protection for Merchants, for this transaction.

      - `payment_method_details.paypal.seller_protection.dispute_categories` (nullable array of enums)
        An array of conditions that are covered for the transaction, if applicable.

        The payer did not authorize the payment.

        The payer paid for an item that they did not receive.

      - `payment_method_details.paypal.seller_protection.status` (enum)
        Indicates whether the transaction is eligible for PayPal’s seller protection.

        Your balance remains intact if the customer claims that they did not receive an item or the account holder claims that they did not authorize the payment.

        This transaction is not eligible for seller protection.

        Your balance remains intact if the customer claims that they did not receive an item.

    - `payment_method_details.paypal.transaction_id` (nullable string)
      A unique ID generated by PayPal for this transaction.

  - `payment_method_details.promptpay` (nullable object)
    If this is a `promptpay` payment, this hash contains a snapshot of the transaction specific details of the `promptpay` payment method.

    - `payment_method_details.promptpay.reference` (nullable string)
      Bill reference generated by PromptPay

  - `payment_method_details.revolut_pay` (nullable object)
    If this is a `revolut_pay` payment, this hash contains a snapshot of the transaction specific details of the `revolut_pay` payment method.

    - `payment_method_details.revolut_pay.funding` (nullable object)
      the funding details of the underlying payment method.

      - `payment_method_details.revolut_pay.funding.card` (nullable object)
        the funding details of the passthrough card.

        - `payment_method_details.revolut_pay.funding.card.brand` (nullable string)
          Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

        - `payment_method_details.revolut_pay.funding.card.country` (nullable string)
          Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

        - `payment_method_details.revolut_pay.funding.card.exp_month` (nullable integer)
          Two-digit number representing the card’s expiration month.

        - `payment_method_details.revolut_pay.funding.card.exp_year` (nullable integer)
          Four-digit number representing the card’s expiration year.

        - `payment_method_details.revolut_pay.funding.card.funding` (nullable string)
          Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.

        - `payment_method_details.revolut_pay.funding.card.last4` (nullable string)
          The last four digits of the card.

      - `payment_method_details.revolut_pay.funding.type` (nullable enum)
        funding type of the underlying payment method.

  - `payment_method_details.samsung_pay` (nullable object)
    If this is a `samsung_pay` payment, this hash contains a snapshot of the transaction specific details of the `samsung_pay` payment method.

    - `payment_method_details.samsung_pay.buyer_id` (nullable string)
      A unique identifier for the buyer as determined by the local payment processor.

  - `payment_method_details.satispay` (nullable object)
    If this is a `satispay` payment, this hash contains a snapshot of the transaction specific details of the `satispay` payment method.

  - `payment_method_details.sepa_debit` (nullable object)
    If this is a `sepa_debit` payment, this hash contains a snapshot of the transaction specific details of the `sepa_debit` payment method.

    - `payment_method_details.sepa_debit.bank_code` (nullable string)
      Bank code of bank associated with the bank account.

    - `payment_method_details.sepa_debit.branch_code` (nullable string)
      Branch code of bank associated with the bank account.

    - `payment_method_details.sepa_debit.country` (nullable string)
      Two-letter ISO code representing the country the bank account is located in.

    - `payment_method_details.sepa_debit.fingerprint` (nullable string)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `payment_method_details.sepa_debit.last4` (nullable string)
      Last four characters of the IBAN.

    - `payment_method_details.sepa_debit.mandate` (nullable string)
      Find the ID of the mandate used for this payment under the [payment_method_details.sepa_debit.mandate](https://docs.stripe.com/docs/api/charges/object.md#charge_object-payment_method_details-sepa_debit-mandate) property on the Charge. Use this mandate ID to [retrieve the Mandate](https://docs.stripe.com/docs/api/mandates/retrieve.md).

  - `payment_method_details.sofort` (nullable object)
    If this is a `sofort` payment, this hash contains a snapshot of the transaction specific details of the `sofort` payment method.

    - `payment_method_details.sofort.bank_code` (nullable string)
      Bank code of bank associated with the bank account.

    - `payment_method_details.sofort.bank_name` (nullable string)
      Name of the bank associated with the bank account.

    - `payment_method_details.sofort.bic` (nullable string)
      Bank Identifier Code of the bank associated with the bank account.

    - `payment_method_details.sofort.country` (nullable string)
      Two-letter ISO code representing the country the bank account is located in.

    - `payment_method_details.sofort.generated_sepa_debit` (nullable string)
      The ID of the SEPA Direct Debit PaymentMethod which was generated by this Charge.

    - `payment_method_details.sofort.generated_sepa_debit_mandate` (nullable string)
      The mandate for the SEPA Direct Debit PaymentMethod which was generated by this Charge.

    - `payment_method_details.sofort.iban_last4` (nullable string)
      Last four characters of the IBAN.

    - `payment_method_details.sofort.preferred_language` (nullable enum)
      Preferred language of the SOFORT authorization page that the customer is redirected to.
      Can be one of `de`, `en`, `es`, `fr`, `it`, `nl`, or `pl`

    - `payment_method_details.sofort.verified_name` (nullable string)
      Owner’s verified full name. Values are verified or provided by SOFORT directly
      (if supported) at the time of authorization or settlement. They cannot be set or mutated.

  - `payment_method_details.stripe_account` (nullable object)
    If this is a `stripe_account` payment, this hash contains a snapshot of the transaction specific details of the `stripe_account` payment method.

  - `payment_method_details.swish` (nullable object)
    If this is a `swish` payment, this hash contains a snapshot of the transaction specific details of the `swish` payment method.

    - `payment_method_details.swish.fingerprint` (nullable string)
      Uniquely identifies the payer’s Swish account. You can use this attribute to check whether two Swish transactions were paid for by the same payer

    - `payment_method_details.swish.payment_reference` (nullable string)
      Payer bank reference number for the payment

    - `payment_method_details.swish.verified_phone_last4` (nullable string)
      The last four digits of the Swish account phone number

  - `payment_method_details.twint` (nullable object)
    If this is a `twint` payment, this hash contains a snapshot of the transaction specific details of the `twint` payment method.

  - `payment_method_details.type` (string)
    The type of transaction-specific details of the payment method used in the payment. See [PaymentMethod.type](https://docs.stripe.com/docs/api/payment_methods/object.md#payment_method_object-type) for the full list of possible types.
    An additional hash is included on `payment_method_details` with a name matching this value.
    It contains information specific to the payment method.

  - `payment_method_details.us_bank_account` (nullable object)
    If this is a `us_bank_account` payment, this hash contains a snapshot of the transaction specific details of the `us_bank_account` payment method.

    - `payment_method_details.us_bank_account.account_holder_type` (nullable enum)
      Account holder type: individual or company.

      Account belongs to a company

      Account belongs to an individual

    - `payment_method_details.us_bank_account.account_type` (nullable enum)
      Account type: checkings or savings. Defaults to checking if omitted.

      Bank account type is checking

      Bank account type is savings

    - `payment_method_details.us_bank_account.bank_name` (nullable string)
      Name of the bank associated with the bank account.

    - `payment_method_details.us_bank_account.fingerprint` (nullable string)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `payment_method_details.us_bank_account.last4` (nullable string)
      Last four digits of the bank account number.

    - `payment_method_details.us_bank_account.mandate` (nullable string)
      ID of the mandate used to make this payment.

    - `payment_method_details.us_bank_account.payment_reference` (nullable string)
      Reference number to locate ACH payments with customer’s bank.

    - `payment_method_details.us_bank_account.routing_number` (nullable string)
      Routing number of the bank account.

  - `payment_method_details.wechat` (nullable object)
    If this is a `wechat` payment, this hash contains a snapshot of the transaction specific details of the `wechat` payment method.

  - `payment_method_details.wechat_pay` (nullable object)
    If this is a `wechat_pay` payment, this hash contains a snapshot of the transaction specific details of the `wechat_pay` payment method.

    - `payment_method_details.wechat_pay.fingerprint` (nullable string)
      Uniquely identifies this particular WeChat Pay account. You can use this attribute to check whether two WeChat accounts are the same.

    - `payment_method_details.wechat_pay.transaction_id` (nullable string)
      Transaction ID of this particular WeChat Pay transaction.

  - `payment_method_details.zip` (nullable object)
    If this is a `zip` payment, this hash contains a snapshot of the transaction specific details of the `zip` payment method.

- `presentment_details` (nullable object)
  A hash containing information about the currency presentation to the customer, including the displayed currency and amount used for conversion from the integration currency.

  - `presentment_details.presentment_amount` (integer)
    Amount intended to be collected by this payment, denominated in presentment_currency.

  - `presentment_details.presentment_currency` (string)
    Currency presented to the customer during payment.

- `radar_options` (nullable object)
  Options to configure Radar. See [Radar Session](https://docs.stripe.com/docs/radar/radar-session.md) for more information.

  - `radar_options.session` (nullable string)
    A [Radar Session](https://docs.stripe.com/docs/radar/radar-session.md) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.

- `receipt_email` (nullable string)
  This is the email address that the receipt for this charge was sent to.

- `receipt_number` (nullable string)
  This is the transaction number that appears on email receipts sent for this charge. This attribute will be `null` until a receipt has been sent.

- `receipt_url` (nullable string)
  This is the URL to view the receipt for this charge. The receipt is kept up-to-date to the latest state of the charge, including any refunds. If the charge is for an Invoice, the receipt will be stylized as an Invoice receipt.

- `refunded` (boolean)
  Whether the charge has been fully refunded. If the charge is only partially refunded, this attribute will still be false.

- `refunds` (nullable object)
  A list of refunds that have been applied to the charge.

  - `refunds.object` (string)
    String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

  - `refunds.data` (array of objects)
    Details about each object.

    - `refunds.data.id` (string)
      Unique identifier for the object.

    - `refunds.data.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `refunds.data.amount` (integer)
      Amount, in .

    - `refunds.data.balance_transaction` (nullable string)
      Balance transaction that describes the impact on your account balance.

    - `refunds.data.charge` (nullable string)
      ID of the charge that’s refunded.

    - `refunds.data.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `refunds.data.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `refunds.data.description` (nullable string)
      An arbitrary string attached to the object. You can use this for displaying to users (available on non-card refunds only).

    - `refunds.data.destination_details` (nullable object)
      Transaction-specific details for the refund.

      - `refunds.data.destination_details.affirm` (nullable object)
        If this is a `affirm` refund, this hash contains the transaction specific details of the `affirm` refund method.

      - `refunds.data.destination_details.afterpay_clearpay` (nullable object)
        If this is a `afterpay_clearpay` refund, this hash contains the transaction specific details of the `afterpay_clearpay` refund method.

      - `refunds.data.destination_details.alipay` (nullable object)
        If this is a `alipay` refund, this hash contains the transaction specific details of the `alipay` refund method.

      - `refunds.data.destination_details.alma` (nullable object)
        If this is a `alma` refund, this hash contains the transaction specific details of the `alma` refund method.

      - `refunds.data.destination_details.amazon_pay` (nullable object)
        If this is a `amazon_pay` refund, this hash contains the transaction specific details of the `amazon_pay` refund method.

      - `refunds.data.destination_details.au_bank_transfer` (nullable object)
        If this is a `au_bank_transfer` refund, this hash contains the transaction specific details of the `au_bank_transfer` refund method.

      - `refunds.data.destination_details.br_bank_transfer` (nullable object)
        If this is a `br_bank_transfer` refund, this hash contains the transaction specific details of the `br_bank_transfer` refund method.

        - `refunds.data.destination_details.br_bank_transfer.reference` (nullable string)
          The reference assigned to the refund.

        - `refunds.data.destination_details.br_bank_transfer.reference_status` (nullable string)
          Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

      - `refunds.data.destination_details.card` (nullable object)
        If this is a `card` refund, this hash contains the transaction specific details of the `card` refund method.

        - `refunds.data.destination_details.card.reference` (nullable string)
          Value of the reference number assigned to the refund.

        - `refunds.data.destination_details.card.reference_status` (nullable string)
          Status of the reference number on the refund. This can be `pending`, `available` or `unavailable`.

        - `refunds.data.destination_details.card.reference_type` (nullable string)
          Type of the reference number assigned to the refund.

        - `refunds.data.destination_details.card.type` (enum)
          The type of refund. This can be `refund`, `reversal`, or `pending`.

          The refund is still processing and its type is not confirmed yet.

          The refund will show as a credit entry on the bank statement.

          The refund goes through as a reversal. The original charge will drop off the bank statement altogether.

      - `refunds.data.destination_details.cashapp` (nullable object)
        If this is a `cashapp` refund, this hash contains the transaction specific details of the `cashapp` refund method.

      - `refunds.data.destination_details.customer_cash_balance` (nullable object)
        If this is a `customer_cash_balance` refund, this hash contains the transaction specific details of the `customer_cash_balance` refund method.

      - `refunds.data.destination_details.eps` (nullable object)
        If this is a `eps` refund, this hash contains the transaction specific details of the `eps` refund method.

      - `refunds.data.destination_details.eu_bank_transfer` (nullable object)
        If this is a `eu_bank_transfer` refund, this hash contains the transaction specific details of the `eu_bank_transfer` refund method.

        - `refunds.data.destination_details.eu_bank_transfer.reference` (nullable string)
          The reference assigned to the refund.

        - `refunds.data.destination_details.eu_bank_transfer.reference_status` (nullable string)
          Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

      - `refunds.data.destination_details.gb_bank_transfer` (nullable object)
        If this is a `gb_bank_transfer` refund, this hash contains the transaction specific details of the `gb_bank_transfer` refund method.

        - `refunds.data.destination_details.gb_bank_transfer.reference` (nullable string)
          The reference assigned to the refund.

        - `refunds.data.destination_details.gb_bank_transfer.reference_status` (nullable string)
          Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

      - `refunds.data.destination_details.giropay` (nullable object)
        If this is a `giropay` refund, this hash contains the transaction specific details of the `giropay` refund method.

      - `refunds.data.destination_details.grabpay` (nullable object)
        If this is a `grabpay` refund, this hash contains the transaction specific details of the `grabpay` refund method.

      - `refunds.data.destination_details.jp_bank_transfer` (nullable object)
        If this is a `jp_bank_transfer` refund, this hash contains the transaction specific details of the `jp_bank_transfer` refund method.

        - `refunds.data.destination_details.jp_bank_transfer.reference` (nullable string)
          The reference assigned to the refund.

        - `refunds.data.destination_details.jp_bank_transfer.reference_status` (nullable string)
          Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

      - `refunds.data.destination_details.klarna` (nullable object)
        If this is a `klarna` refund, this hash contains the transaction specific details of the `klarna` refund method.

      - `refunds.data.destination_details.multibanco` (nullable object)
        If this is a `multibanco` refund, this hash contains the transaction specific details of the `multibanco` refund method.

        - `refunds.data.destination_details.multibanco.reference` (nullable string)
          The reference assigned to the refund.

        - `refunds.data.destination_details.multibanco.reference_status` (nullable string)
          Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

      - `refunds.data.destination_details.mx_bank_transfer` (nullable object)
        If this is a `mx_bank_transfer` refund, this hash contains the transaction specific details of the `mx_bank_transfer` refund method.

        - `refunds.data.destination_details.mx_bank_transfer.reference` (nullable string)
          The reference assigned to the refund.

        - `refunds.data.destination_details.mx_bank_transfer.reference_status` (nullable string)
          Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

      - `refunds.data.destination_details.p24` (nullable object)
        If this is a `p24` refund, this hash contains the transaction specific details of the `p24` refund method.

        - `refunds.data.destination_details.p24.reference` (nullable string)
          The reference assigned to the refund.

        - `refunds.data.destination_details.p24.reference_status` (nullable string)
          Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

      - `refunds.data.destination_details.paynow` (nullable object)
        If this is a `paynow` refund, this hash contains the transaction specific details of the `paynow` refund method.

      - `refunds.data.destination_details.paypal` (nullable object)
        If this is a `paypal` refund, this hash contains the transaction specific details of the `paypal` refund method.

        - `refunds.data.destination_details.paypal.network_decline_code` (nullable string)
          For refunds declined by the network, a decline code provided by the network which indicates the reason the refund failed.

      - `refunds.data.destination_details.revolut` (nullable object)
        If this is a `revolut` refund, this hash contains the transaction specific details of the `revolut` refund method.

      - `refunds.data.destination_details.sofort` (nullable object)
        If this is a `sofort` refund, this hash contains the transaction specific details of the `sofort` refund method.

      - `refunds.data.destination_details.swish` (nullable object)
        If this is a `swish` refund, this hash contains the transaction specific details of the `swish` refund method.

        - `refunds.data.destination_details.swish.network_decline_code` (nullable string)
          For refunds declined by the network, a decline code provided by the network which indicates the reason the refund failed.

        - `refunds.data.destination_details.swish.reference` (nullable string)
          The reference assigned to the refund.

        - `refunds.data.destination_details.swish.reference_status` (nullable string)
          Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

      - `refunds.data.destination_details.th_bank_transfer` (nullable object)
        If this is a `th_bank_transfer` refund, this hash contains the transaction specific details of the `th_bank_transfer` refund method.

        - `refunds.data.destination_details.th_bank_transfer.reference` (nullable string)
          The reference assigned to the refund.

        - `refunds.data.destination_details.th_bank_transfer.reference_status` (nullable string)
          Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

      - `refunds.data.destination_details.type` (string)
        The type of transaction-specific details of the payment method used in the refund (e.g., `card`). An additional hash is included on `destination_details` with a name matching this value. It contains information specific to the refund transaction.

      - `refunds.data.destination_details.us_bank_transfer` (nullable object)
        If this is a `us_bank_transfer` refund, this hash contains the transaction specific details of the `us_bank_transfer` refund method.

        - `refunds.data.destination_details.us_bank_transfer.reference` (nullable string)
          The reference assigned to the refund.

        - `refunds.data.destination_details.us_bank_transfer.reference_status` (nullable string)
          Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.

      - `refunds.data.destination_details.wechat_pay` (nullable object)
        If this is a `wechat_pay` refund, this hash contains the transaction specific details of the `wechat_pay` refund method.

      - `refunds.data.destination_details.zip` (nullable object)
        If this is a `zip` refund, this hash contains the transaction specific details of the `zip` refund method.

    - `refunds.data.failure_balance_transaction` (nullable string)
      After the refund fails, this balance transaction describes the adjustment made on your account balance that reverses the initial balance transaction.

    - `refunds.data.failure_reason` (nullable string)
      Provides the reason for the refund failure. Possible values are: `lost_or_stolen_card`, `expired_or_canceled_card`, `charge_for_pending_refund_disputed`, `insufficient_funds`, `declined`, `merchant_request`, or `unknown`.

    - `refunds.data.instructions_email` (nullable string)
      For payment methods without native refund support (for example, Konbini, PromptPay), provide an email address for the customer to receive refund instructions.

    - `refunds.data.metadata` (nullable object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `refunds.data.next_action` (nullable object)
      If the refund has a status of `requires_action`, this property describes what the refund needs to continue processing.

      - `refunds.data.next_action.display_details` (nullable object)
        Contains the refund details.

        - `refunds.data.next_action.display_details.email_sent` (object)
          Contains information about the email sent to the customer.

          - `refunds.data.next_action.display_details.email_sent.email_sent_at` (timestamp)
            The timestamp when the email was sent.

          - `refunds.data.next_action.display_details.email_sent.email_sent_to` (string)
            The recipient’s email address.

        - `refunds.data.next_action.display_details.expires_at` (timestamp)
          The expiry timestamp.

      - `refunds.data.next_action.type` (string)
        Type of the next action to perform.

    - `refunds.data.payment_intent` (nullable string)
      ID of the PaymentIntent that’s refunded.

    - `refunds.data.pending_reason` (nullable enum)
      Provides the reason for why the refund is pending. Possible values are: `processing`, `insufficient_funds`, or `charge_pending`.

    - `refunds.data.reason` (nullable enum)
      Reason for the refund, which is either user-provided (`duplicate`, `fraudulent`, or `requested_by_customer`) or generated by Stripe internally (`expired_uncaptured_charge`).

    - `refunds.data.receipt_number` (nullable string)
      This is the transaction number that appears on email receipts sent for this refund.

    - `refunds.data.source_transfer_reversal` (nullable string)
      The transfer reversal that’s associated with the refund. Only present if the charge came from another Stripe account.

    - `refunds.data.status` (nullable string)
      Status of the refund. This can be `pending`, `requires_action`, `succeeded`, `failed`, or `canceled`. Learn more about [failed refunds](https://docs.stripe.com/docs/refunds.md#failed-refunds).

    - `refunds.data.transfer_reversal` (nullable string)
      This refers to the transfer reversal object if the accompanying transfer reverses. This is only applicable if the charge was created using the destination parameter.

  - `refunds.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `refunds.url` (string)
    The URL where this list can be accessed.

- `review` (nullable string)
  ID of the review associated with this charge if one exists.

- `shipping` (nullable object)
  Shipping information for the charge.

  - `shipping.address` (object)
    Shipping address.

    - `shipping.address.city` (nullable string)
      City, district, suburb, town, or village.

    - `shipping.address.country` (nullable string)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `shipping.address.line1` (nullable string)
      Address line 1 (e.g., street, PO Box, or company name).

    - `shipping.address.line2` (nullable string)
      Address line 2 (e.g., apartment, suite, unit, or building).

    - `shipping.address.postal_code` (nullable string)
      ZIP or postal code.

    - `shipping.address.state` (nullable string)
      State, county, province, or region.

  - `shipping.carrier` (nullable string)
    The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc.

  - `shipping.name` (string)
    Recipient name.

  - `shipping.phone` (nullable string)
    Recipient phone (including extension).

  - `shipping.tracking_number` (nullable string)
    The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.

- `source_transfer` (nullable string)
  The transfer ID which created this charge. Only present if the charge came from another Stripe account. [See the Connect documentation](https://docs.stripe.com/connect/destination-charges) for details.

- `statement_descriptor` (nullable string)
  For a non-card charge, text that appears on the customer’s statement as the statement descriptor. This value overrides the account’s default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).

  For a card charge, this value is ignored unless you don’t specify a `statement_descriptor_suffix`, in which case this value is used as the suffix.

- `statement_descriptor_suffix` (nullable string)
  Provides information about a card charge. Concatenated to the account’s [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer’s statement. If the account has no prefix value, the suffix is concatenated to the account’s statement descriptor.

- `status` (enum)
  The status of the payment is either `succeeded`, `pending`, or `failed`.

- `transfer` (nullable string)
  ID of the transfer to the `destination` account (only applicable if the charge was created using the `destination` parameter).

- `transfer_data` (nullable object)
  An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://docs.stripe.com/docs/connect/destination-charges.md) for details.

  - `transfer_data.amount` (nullable integer)
    The amount transferred to the destination account, if specified. By default, the entire charge amount is transferred to the destination account.

  - `transfer_data.destination` (string)
    ID of an existing, connected Stripe account to transfer funds to if `transfer_data` was specified in the charge request.

- `transfer_group` (nullable string)
  A string that identifies this transaction as part of a group. See the [Connect documentation](https://docs.stripe.com/docs/connect/separate-charges-and-transfers.md#transfer-options) for details.

### The Charge object

```json
{
  "id": "ch_3MmlLrLkdIwHu7ix0snN0B15",
  "object": "charge",
  "amount": 1099,
  "amount_captured": 1099,
  "amount_refunded": 0,
  "application": null,
  "application_fee": null,
  "application_fee_amount": null,
  "balance_transaction": "txn_3MmlLrLkdIwHu7ix0uke3Ezy",
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
    "name": null,
    "phone": null
  },
  "calculated_statement_descriptor": "Stripe",
  "captured": true,
  "created": 1679090539,
  "currency": "usd",
  "customer": null,
  "description": null,
  "disputed": false,
  "failure_balance_transaction": null,
  "failure_code": null,
  "failure_message": null,
  "fraud_details": {},
  "livemode": false,
  "metadata": {},
  "on_behalf_of": null,
  "outcome": {
    "network_status": "approved_by_network",
    "reason": null,
    "risk_level": "normal",
    "risk_score": 32,
    "seller_message": "Payment complete.",
    "type": "authorized"
  },
  "paid": true,
  "payment_intent": null,
  "payment_method": "card_1MmlLrLkdIwHu7ixIJwEWSNR",
  "payment_method_details": {
    "card": {
      "brand": "visa",
      "checks": {
        "address_line1_check": null,
        "address_postal_code_check": null,
        "cvc_check": null
      },
      "country": "US",
      "exp_month": 3,
      "exp_year": 2024,
      "fingerprint": "mToisGZ01V71BCos",
      "funding": "credit",
      "installments": null,
      "last4": "4242",
      "mandate": null,
      "network": "visa",
      "three_d_secure": null,
      "wallet": null
    },
    "type": "card"
  },
  "receipt_email": null,
  "receipt_number": null,
  "receipt_url": "https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KOvG06AGMgZfBXyr1aw6LBa9vaaSRWU96d8qBwz9z2J_CObiV_H2-e8RezSK_sw0KISesp4czsOUlVKY",
  "refunded": false,
  "review": null,
  "shipping": null,
  "source_transfer": null,
  "statement_descriptor": null,
  "statement_descriptor_suffix": null,
  "status": "succeeded",
  "transfer_data": null,
  "transfer_group": null
}
```