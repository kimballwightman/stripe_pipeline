# The Mandate object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `customer_acceptance` (object)
  Details about the customer’s acceptance of the mandate.

  - `customer_acceptance.accepted_at` (nullable timestamp)
    The time that the customer accepts the mandate.

  - `customer_acceptance.offline` (nullable object)
    If this mandate is accepted offline, this hash provides details about the offline acceptance.

  - `customer_acceptance.online` (nullable object)
    If this mandate is accepted online, this hash provides details about the online acceptance.

    - `customer_acceptance.online.ip_address` (nullable string)
      The customer accepts the mandate from this IP address.

    - `customer_acceptance.online.user_agent` (nullable string)
      The customer accepts the mandate using the user agent of the browser.

  - `customer_acceptance.type` (enum)
    The mandate includes the type of customer acceptance information, such as: `online` or `offline`.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `multi_use` (nullable object)
  If this is a `multi_use` mandate, this hash contains details about the mandate.

- `on_behalf_of` (nullable string)
  The account (if any) that the mandate is intended for.

- `payment_method` (string)
  ID of the payment method associated with this mandate.

- `payment_method_details` (object)
  Additional mandate information specific to the payment method type.

  - `payment_method_details.acss_debit` (nullable object)
    If this mandate associates with a `acss_debit` payment method, this hash contains mandate information specific to the `acss_debit` payment method.

    - `payment_method_details.acss_debit.default_for` (nullable array of enums)
      List of Stripe products where this mandate can be selected automatically.

      Enables payments for Stripe Invoices. ‘subscription’ must also be provided.

      Enables payments for Stripe Subscriptions. ‘invoice’ must also be provided.

    - `payment_method_details.acss_debit.interval_description` (nullable string)
      Description of the interval. Only required if the ‘payment_schedule’ parameter is ‘interval’ or ‘combined’.

    - `payment_method_details.acss_debit.payment_schedule` (enum)
      Payment schedule for the mandate.

      Payments can be initiated at a pre-defined interval or sporadically

      Payments are initiated at a regular pre-defined interval

      Payments are initiated sporadically

    - `payment_method_details.acss_debit.transaction_type` (enum)
      Transaction type of the mandate.

      Transactions are made for business reasons

      Transactions are made for personal reasons

  - `payment_method_details.amazon_pay` (nullable object)
    If this mandate associates with a `amazon_pay` payment method, this hash contains mandate information specific to the `amazon_pay` payment method.

  - `payment_method_details.au_becs_debit` (nullable object)
    If this mandate associates with a `au_becs_debit` payment method, this hash contains mandate information specific to the `au_becs_debit` payment method.

    - `payment_method_details.au_becs_debit.url` (string)
      The URL of the mandate. This URL generally contains sensitive information about the customer and should be shared with them exclusively.

  - `payment_method_details.bacs_debit` (nullable object)
    If this mandate associates with a `bacs_debit` payment method, this hash contains mandate information specific to the `bacs_debit` payment method.

    - `payment_method_details.bacs_debit.network_status` (enum)
      The status of the mandate on the Bacs network. Can be one of `pending`, `revoked`, `refused`, or `accepted`.

    - `payment_method_details.bacs_debit.reference` (string)
      The unique reference identifying the mandate on the Bacs network.

    - `payment_method_details.bacs_debit.revocation_reason` (nullable enum)
      When the mandate is revoked on the Bacs network this field displays the reason for the revocation.

      The bank account has been closed. Refer to the customer to collect a new mandate.

      The bank account has restrictions on either the type or the number of payouts allowed. This normally indicates that the bank account is a savings or other non-checking account. Refer to the customer to collect a new mandate.

      The destination bank account is no longer valid because it has been transferred to a new bank or to a new branch. A new mandate with the updated account details has been submitted on your behalf and you will be notified when it is accepted.

      The bank could not process this payout. Refer to the customer to collect a new mandate.

      Debit transactions are not approved on this bank account. Refer to the customer to collect a new mandate.

    - `payment_method_details.bacs_debit.url` (string)
      The URL that will contain the mandate that the customer has signed.

  - `payment_method_details.card` (nullable object)
    If this mandate associates with a `card` payment method, this hash contains mandate information specific to the `card` payment method.

  - `payment_method_details.cashapp` (nullable object)
    If this mandate associates with a `cashapp` payment method, this hash contains mandate information specific to the `cashapp` payment method.

  - `payment_method_details.kakao_pay` (nullable object)
    If this mandate associates with a `kakao_pay` payment method, this hash contains mandate information specific to the `kakao_pay` payment method.

  - `payment_method_details.klarna` (nullable object)
    If this mandate associates with a `klarna` payment method, this hash contains mandate information specific to the `klarna` payment method.

  - `payment_method_details.kr_card` (nullable object)
    If this mandate associates with a `kr_card` payment method, this hash contains mandate information specific to the `kr_card` payment method.

  - `payment_method_details.link` (nullable object)
    If this mandate associates with a `link` payment method, this hash contains mandate information specific to the `link` payment method.

  - `payment_method_details.naver_pay` (nullable object)
    If this mandate associates with a `naver_pay` payment method, this hash contains mandate information specific to the `naver_pay` payment method.

  - `payment_method_details.nz_bank_account` (nullable object)
    If this mandate associates with a `nz_bank_account` payment method, this hash contains mandate information specific to the `nz_bank_account` payment method.

  - `payment_method_details.paypal` (nullable object)
    If this mandate associates with a `paypal` payment method, this hash contains mandate information specific to the `paypal` payment method.

    - `payment_method_details.paypal.billing_agreement_id` (nullable string)
      The PayPal Billing Agreement ID (BAID). This is an ID generated by PayPal which represents the mandate between the merchant and the customer.

    - `payment_method_details.paypal.payer_id` (nullable string)
      PayPal account PayerID. This identifier uniquely identifies the PayPal customer.

  - `payment_method_details.revolut_pay` (nullable object)
    If this mandate associates with a `revolut_pay` payment method, this hash contains mandate information specific to the `revolut_pay` payment method.

  - `payment_method_details.sepa_debit` (nullable object)
    If this mandate associates with a `sepa_debit` payment method, this hash contains mandate information specific to the `sepa_debit` payment method.

    - `payment_method_details.sepa_debit.reference` (string)
      The unique reference of the mandate.

    - `payment_method_details.sepa_debit.url` (string)
      The URL of the mandate. This URL generally contains sensitive information about the customer and should be shared with them exclusively.

  - `payment_method_details.type` (string)
    This mandate corresponds with a specific payment method type. The `payment_method_details` includes an additional hash with the same name and contains mandate information that’s specific to that payment method.

  - `payment_method_details.us_bank_account` (nullable object)
    If this mandate associates with a `us_bank_account` payment method, this hash contains mandate information specific to the `us_bank_account` payment method.

    - `payment_method_details.us_bank_account.collection_method` (nullable enum)
      Mandate collection method

      Mandate customer acceptance was collected using a paper document

- `single_use` (nullable object)
  If this is a `single_use` mandate, this hash contains details about the mandate.

  - `single_use.amount` (integer)
    The amount of the payment on a single use mandate.

  - `single_use.currency` (enum)
    The currency of the payment on a single use mandate.

- `status` (enum)
  The mandate status indicates whether or not you can use it to initiate a payment.

  The mandate can be used to initiate a payment.

  The mandate was rejected, revoked, or previously used, and may not be used to initiate future payments.

  The mandate is newly created and is not yet active or inactive.

- `type` (enum)
  The type of the mandate.

  Represents permission given for multiple payments.

  Represents a one-time permission given for a single payment.

### The Mandate object

```json
{
  "id": "mandate_1MvojA2eZvKYlo2CvqTABjZs",
  "object": "mandate",
  "customer_acceptance": {
    "accepted_at": 123456789,
    "online": {
      "ip_address": "127.0.0.0",
      "user_agent": "device"
    },
    "type": "online"
  },
  "livemode": false,
  "multi_use": {},
  "payment_method": "pm_123456789",
  "payment_method_details": {
    "sepa_debit": {
      "reference": "123456789",
      "url": ""
    },
    "type": "sepa_debit"
  },
  "status": "active",
  "type": "multi_use"
}
```