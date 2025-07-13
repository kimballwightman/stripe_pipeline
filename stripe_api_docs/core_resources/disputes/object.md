# The Dispute object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  Disputed amount. Usually the amount of the charge, but it can differ (usually because of currency fluctuation or because only part of the order is disputed).

- `balance_transactions` (array of objects)
  List of zero, one, or two balance transactions that show funds withdrawn and reinstated to your Stripe account as a result of this dispute.

  - `balance_transactions.id` (string)
    Unique identifier for the object.

  - `balance_transactions.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `balance_transactions.amount` (integer)
    Gross amount of this transaction (in ). A positive value represents funds charged to another party, and a negative value represents funds sent to another party.

  - `balance_transactions.available_on` (timestamp)
    The date that the transaction’s net funds become available in the Stripe balance.

  - `balance_transactions.created` (timestamp)
    Time at which the object was created. Measured in seconds since the Unix epoch.

  - `balance_transactions.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `balance_transactions.description` (nullable string)
    An arbitrary string attached to the object. Often useful for displaying to users.

  - `balance_transactions.exchange_rate` (nullable float)
    If applicable, this transaction uses an exchange rate. If money converts from currency A to currency B, then the `amount` in currency A, multipled by the `exchange_rate`, equals the `amount` in currency B. For example, if you charge a customer 10.00 EUR, the PaymentIntent’s `amount` is `1000` and `currency` is `eur`. If this converts to 12.34 USD in your Stripe account, the BalanceTransaction’s `amount` is `1234`, its `currency` is `usd`, and the `exchange_rate` is `1.234`.

  - `balance_transactions.fee` (integer)
    Fees (in ) paid for this transaction. Represented as a positive integer when assessed.

  - `balance_transactions.fee_details` (array of objects)
    Detailed breakdown of fees (in ) paid for this transaction.

    - `balance_transactions.fee_details.amount` (integer)
      Amount of the fee, in cents.

    - `balance_transactions.fee_details.application` (nullable string)
      ID of the Connect application that earned the fee.

    - `balance_transactions.fee_details.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `balance_transactions.fee_details.description` (nullable string)
      An arbitrary string attached to the object. Often useful for displaying to users.

    - `balance_transactions.fee_details.type` (string)
      Type of the fee, one of: `application_fee`, `payment_method_passthrough_fee`, `stripe_fee` or `tax`.

  - `balance_transactions.net` (integer)
    Net impact to a Stripe balance (in ). A positive value represents incrementing a Stripe balance, and a negative value decrementing a Stripe balance. You can calculate the net impact of a transaction on a balance by `amount` - `fee`

  - `balance_transactions.reporting_category` (string)
    Learn more about how [reporting categories](https://stripe.com/docs/reports/reporting-categories) can help you understand balance transactions from an accounting perspective.

  - `balance_transactions.source` (nullable string)
    This transaction relates to the Stripe object.

  - `balance_transactions.status` (string)
    The transaction’s net funds status in the Stripe balance, which are either `available` or `pending`.

  - `balance_transactions.type` (enum)
    Transaction type: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `obligation_outbound`, `obligation_reversal_inbound`, `payment`, `payment_failure_refund`, `payment_network_reserve_hold`, `payment_network_reserve_release`, `payment_refund`, `payment_reversal`, `payment_unreconciled`, `payout`, `payout_cancel`, `payout_failure`, `payout_minimum_balance_hold`, `payout_minimum_balance_release`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `stripe_balance_payment_debit`, `stripe_balance_payment_debit_reversal`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`. Learn more about [balance transaction types and what they represent](https://stripe.com/docs/reports/balance-transaction-types). To classify transactions for accounting purposes, consider `reporting_category` instead.

- `charge` (string)
  ID of the charge that’s disputed.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `enhanced_eligibility_types` (array of enums)
  List of eligibility types that are included in `enhanced_evidence`.

  Dispute is eligible for Visa Compelling Evidence 3.0 evidence submission.

  Dispute is eligible for Visa compliance evidence submission.

- `evidence` (object)
  Evidence provided to respond to a dispute. Updating any field in the hash submits all fields in the hash for review.

  - `evidence.access_activity_log` (nullable string)
    Any server or activity logs showing proof that the customer accessed or downloaded the purchased digital product. This information should include IP addresses, corresponding timestamps, and any detailed recorded activity.

  - `evidence.billing_address` (nullable string)
    The billing address provided by the customer.

  - `evidence.cancellation_policy` (nullable string)
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Your subscription cancellation policy, as shown to the customer.

  - `evidence.cancellation_policy_disclosure` (nullable string)
    An explanation of how and when the customer was shown your refund policy prior to purchase.

  - `evidence.cancellation_rebuttal` (nullable string)
    A justification for why the customer’s subscription was not canceled.

  - `evidence.customer_communication` (nullable string)
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any communication with the customer that you feel is relevant to your case. Examples include emails proving that the customer received the product or service, or demonstrating their use of or satisfaction with the product or service.

  - `evidence.customer_email_address` (nullable string)
    The email address of the customer.

  - `evidence.customer_name` (nullable string)
    The name of the customer.

  - `evidence.customer_purchase_ip` (nullable string)
    The IP address that the customer used when making the purchase.

  - `evidence.customer_signature` (nullable string)
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A relevant document or contract showing the customer’s signature.

  - `evidence.duplicate_charge_documentation` (nullable string)
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation for the prior charge that can uniquely identify the charge, such as a receipt, shipping label, work order, etc. This document should be paired with a similar document from the disputed payment that proves the two payments are separate.

  - `evidence.duplicate_charge_explanation` (nullable string)
    An explanation of the difference between the disputed charge versus the prior charge that appears to be a duplicate.

  - `evidence.duplicate_charge_id` (nullable string)
    The Stripe ID for the prior charge which appears to be a duplicate of the disputed charge.

  - `evidence.enhanced_evidence` (object)
    Additional evidence for qualifying evidence programs.

    - `evidence.enhanced_evidence.visa_compelling_evidence_3` (nullable object)
      Evidence provided for Visa Compelling Evidence 3.0 evidence submission.

      - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction` (nullable object)
        Disputed transaction details for Visa Compelling Evidence 3.0 evidence submission.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.customer_account_id` (nullable string)
          User Account ID used to log into business platform. Must be recognizable by the user.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.customer_device_fingerprint` (nullable string)
          Unique identifier of the cardholder’s device derived from a combination of at least two hardware and software attributes. Must be at least 20 characters.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.customer_device_id` (nullable string)
          Unique identifier of the cardholder’s device such as a device serial number (e.g., International Mobile Equipment Identity [IMEI]). Must be at least 15 characters.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.customer_email_address` (nullable string)
          The email address of the customer.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.customer_purchase_ip` (nullable string)
          The IP address that the customer used when making the purchase.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.merchandise_or_services` (nullable enum)
          Categorization of disputed payment.

          Disputed payment was for a physical product.

          Disputed payment was for a service.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.product_description` (nullable string)
          A description of the product or service that was sold.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.shipping_address` (nullable object)
          The address to which a physical product was shipped. All fields are required for Visa Compelling Evidence 3.0 evidence submission.

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.shipping_address.city` (nullable string)
            City, district, suburb, town, or village.

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.shipping_address.country` (nullable string)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.shipping_address.line1` (nullable string)
            Address line 1 (e.g., street, PO Box, or company name).

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.shipping_address.line2` (nullable string)
            Address line 2 (e.g., apartment, suite, unit, or building).

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.shipping_address.postal_code` (nullable string)
            ZIP or postal code.

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.shipping_address.state` (nullable string)
            State, county, province, or region.

      - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions` (array of objects)
        List of exactly two prior undisputed transaction objects for Visa Compelling Evidence 3.0 evidence submission.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.charge` (string)
          Stripe charge ID for the Visa Compelling Evidence 3.0 eligible prior charge.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.customer_account_id` (nullable string)
          User Account ID used to log into business platform. Must be recognizable by the user.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.customer_device_fingerprint` (nullable string)
          Unique identifier of the cardholder’s device derived from a combination of at least two hardware and software attributes. Must be at least 20 characters.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.customer_device_id` (nullable string)
          Unique identifier of the cardholder’s device such as a device serial number (e.g., International Mobile Equipment Identity [IMEI]). Must be at least 15 characters.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.customer_email_address` (nullable string)
          The email address of the customer.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.customer_purchase_ip` (nullable string)
          The IP address that the customer used when making the purchase.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.product_description` (nullable string)
          A description of the product or service that was sold.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.shipping_address` (nullable object)
          The address to which a physical product was shipped. All fields are required for Visa Compelling Evidence 3.0 evidence submission.

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.shipping_address.city` (nullable string)
            City, district, suburb, town, or village.

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.shipping_address.country` (nullable string)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.shipping_address.line1` (nullable string)
            Address line 1 (e.g., street, PO Box, or company name).

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.shipping_address.line2` (nullable string)
            Address line 2 (e.g., apartment, suite, unit, or building).

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.shipping_address.postal_code` (nullable string)
            ZIP or postal code.

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.shipping_address.state` (nullable string)
            State, county, province, or region.

    - `evidence.enhanced_evidence.visa_compliance` (nullable object)
      Evidence provided for Visa compliance evidence submission.

      - `evidence.enhanced_evidence.visa_compliance.fee_acknowledged` (boolean)
        A field acknowledging the fee incurred when countering a Visa compliance dispute. If this field is set to true, evidence can be submitted for the compliance dispute. Stripe collects a 500 USD (or local equivalent) amount to cover the network costs associated with resolving compliance disputes. Stripe refunds the 500 USD network fee if you win the dispute.

  - `evidence.product_description` (nullable string)
    A description of the product or service that was sold.

  - `evidence.receipt` (nullable string)
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any receipt or message sent to the customer notifying them of the charge.

  - `evidence.refund_policy` (nullable string)
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Your refund policy, as shown to the customer.

  - `evidence.refund_policy_disclosure` (nullable string)
    Documentation demonstrating that the customer was shown your refund policy prior to purchase.

  - `evidence.refund_refusal_explanation` (nullable string)
    A justification for why the customer is not entitled to a refund.

  - `evidence.service_date` (nullable string)
    The date on which the customer received or began receiving the purchased service, in a clear human-readable format.

  - `evidence.service_documentation` (nullable string)
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation showing proof that a service was provided to the customer. This could include a copy of a signed contract, work order, or other form of written agreement.

  - `evidence.shipping_address` (nullable string)
    The address to which a physical product was shipped. You should try to include as complete address information as possible.

  - `evidence.shipping_carrier` (nullable string)
    The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc. If multiple carriers were used for this purchase, please separate them with commas.

  - `evidence.shipping_date` (nullable string)
    The date on which a physical product began its route to the shipping address, in a clear human-readable format.

  - `evidence.shipping_documentation` (nullable string)
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation showing proof that a product was shipped to the customer at the same address the customer provided to you. This could include a copy of the shipment receipt, shipping label, etc. It should show the customer’s full shipping address, if possible.

  - `evidence.shipping_tracking_number` (nullable string)
    The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.

  - `evidence.uncategorized_file` (nullable string)
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any additional evidence or statements.

  - `evidence.uncategorized_text` (nullable string)
    Any additional evidence or statements.

- `evidence_details` (object)
  Information about the evidence submission.

  - `evidence_details.due_by` (nullable timestamp)
    Date by which evidence must be submitted in order to successfully challenge dispute. Will be 0 if the customer’s bank or credit card company doesn’t allow a response for this particular dispute.

  - `evidence_details.enhanced_eligibility` (object)
    Eligibility details for qualifying evidence programs.

    - `evidence_details.enhanced_eligibility.visa_compelling_evidence_3` (nullable object)
      Eligibility details for Visa Compelling Evidence 3.0 evidence submission.

      - `evidence_details.enhanced_eligibility.visa_compelling_evidence_3.required_actions` (array of enums)
        List of actions required to qualify dispute for Visa Compelling Evidence 3.0 evidence submission.

        `disputed_transaction` and `prior_undisputed_transactions` fields should include a minimum of two customer identifiers. These identifiers can be chosen from the following: `customer_account_id`, `customer_email_address`, `shipping_address`, `customer_purchase_ip`, `customer_device_id`, or `customer_device_fingerprint`. At least one of the chosen identifiers must be either `customer_purchase_ip`, `customer_device_id`, or `customer_device_fingerprint`.
        Note that `customer_device_id` and `customer_device_fingerprint` cannot be the only identifiers provided; they must be accompanied by at least one other identifier.

        Missing `product_description` for `disputed_transaction`.

        Missing `merchandise_or_services` selection for `disputed_transaction`.

        Missing `product_description` for one or more `prior_undisputed_transactions`.

        No Visa Compelling Evidence 3.0 eligible prior transactions have been provided.

      - `evidence_details.enhanced_eligibility.visa_compelling_evidence_3.status` (enum)
        Visa Compelling Evidence 3.0 eligibility status.

        Evidence was not qualified to be submitted to Visa as Compelling Evidence 3.0. Evidence was submitted through the standard dispute flow to Visa.

        Evidence will be submitted to Visa as Compelling Evidence 3.0.

        Transactions provided are potentially eligible, but require further action to be submitted as Compelling Evidence 3.0. See `required_action_details`.

    - `evidence_details.enhanced_eligibility.visa_compliance` (nullable object)
      Eligibility details for Visa compliance evidence submission.

      - `evidence_details.enhanced_eligibility.visa_compliance.status` (enum)
        Visa compliance eligibility status.

        The network fee for submitting evidence for Visa compliance disputes has been acknowledged. Submitting evidence for this dispute is permitted.

        The network fee for submitting evidence for Visa compliance disputes has not been acknowledged. Submitting evidence for this dispute is not permitted.

  - `evidence_details.has_evidence` (boolean)
    Whether evidence has been staged for this dispute.

  - `evidence_details.past_due` (boolean)
    Whether the last evidence submission was submitted past the due date. Defaults to `false` if no evidence submissions have occurred. If `true`, then delivery of the latest evidence is *not* guaranteed.

  - `evidence_details.submission_count` (integer)
    The number of times evidence has been submitted. Typically, you may only submit evidence once.

- `is_charge_refundable` (boolean)
  If true, it’s still possible to refund the disputed payment. After the payment has been fully refunded, no further funds are withdrawn from your Stripe account as a result of this dispute.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `payment_intent` (nullable string)
  ID of the PaymentIntent that’s disputed.

- `payment_method_details` (nullable object)
  Additional dispute information specific to the payment method type.

  - `payment_method_details.amazon_pay` (nullable object)
    AmazonPay specific dispute details.

    - `payment_method_details.amazon_pay.dispute_type` (nullable enum)
      The AmazonPay dispute type, chargeback or claim

      Disputes triggered via card network or issuing bank

      Disputes triggered via Amazon Pay A-to-z guarantee program

  - `payment_method_details.card` (nullable object)
    Card specific dispute details.

    - `payment_method_details.card.brand` (string)
      Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.

    - `payment_method_details.card.case_type` (enum)
      The type of dispute opened. Different case types may have varying fees and financial impact.

      The action taken by a cardholder’s bank to debit a business’s account in response to a dispute from the cardholder. The debited funds are held until the dispute is resolved.

      An action taken by the card network when they believe the merchant does not conform to network rules.

      A pre-dispute request from a card issuer, asking for information about a charge. Based on the response from the business, an inquiry might or might not escalate to a full chargeback. Inquiries are sometimes called retrievals or requests for information.

    - `payment_method_details.card.network_reason_code` (nullable string)
      The card network’s specific dispute reason code, which maps to one of Stripe’s primary dispute categories to simplify response guidance. The [Network code map](https://stripe.com/docs/disputes/categories#network-code-map) lists all available dispute reason codes by network.

  - `payment_method_details.klarna` (nullable object)
    Klarna specific dispute details.

    - `payment_method_details.klarna.reason_code` (nullable string)
      The reason for the dispute as defined by Klarna

  - `payment_method_details.paypal` (nullable object)
    Paypal specific dispute details.

    - `payment_method_details.paypal.case_id` (nullable string)
      The ID of the dispute in PayPal.

    - `payment_method_details.paypal.reason_code` (nullable string)
      The reason for the dispute as defined by PayPal

  - `payment_method_details.type` (enum)
    Payment method type.

    The dispute corresponds to a AmazonPay payment

    The dispute corresponds to a card payment

    The dispute corresponds to a Klarna payment

    The dispute corresponds to a PayPal payment

- `reason` (string)
  Reason given by cardholder for dispute. Possible values are `bank_cannot_process`, `check_returned`, `credit_not_processed`, `customer_initiated`, `debit_not_authorized`, `duplicate`, `fraudulent`, `general`, `incorrect_account_details`, `insufficient_funds`, `noncompliant`, `product_not_received`, `product_unacceptable`, `subscription_canceled`, or `unrecognized`. Learn more about [dispute reasons](https://docs.stripe.com/docs/disputes/categories.md).

- `status` (enum)
  Current status of dispute. Possible values are `warning_needs_response`, `warning_under_review`, `warning_closed`, `needs_response`, `under_review`, `won`, or `lost`.

### The Dispute object

```json
{
  "id": "du_1MtJUT2eZvKYlo2CNaw2HvEv",
  "object": "dispute",
  "amount": 1000,
  "balance_transactions": [],
  "charge": "ch_1AZtxr2eZvKYlo2CJDX8whov",
  "created": 1680651737,
  "currency": "usd",
  "evidence": {
    "access_activity_log": null,
    "billing_address": null,
    "cancellation_policy": null,
    "cancellation_policy_disclosure": null,
    "cancellation_rebuttal": null,
    "customer_communication": null,
    "customer_email_address": null,
    "customer_name": null,
    "customer_purchase_ip": null,
    "customer_signature": null,
    "duplicate_charge_documentation": null,
    "duplicate_charge_explanation": null,
    "duplicate_charge_id": null,
    "product_description": null,
    "receipt": null,
    "refund_policy": null,
    "refund_policy_disclosure": null,
    "refund_refusal_explanation": null,
    "service_date": null,
    "service_documentation": null,
    "shipping_address": null,
    "shipping_carrier": null,
    "shipping_date": null,
    "shipping_documentation": null,
    "shipping_tracking_number": null,
    "uncategorized_file": null,
    "uncategorized_text": null
  },
  "evidence_details": {
    "due_by": 1682294399,
    "has_evidence": false,
    "past_due": false,
    "submission_count": 0
  },
  "is_charge_refundable": true,
  "livemode": false,
  "metadata": {},
  "payment_intent": null,
  "reason": "general",
  "status": "warning_needs_response"
}
```