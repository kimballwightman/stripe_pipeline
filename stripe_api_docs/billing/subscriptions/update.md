# Update a subscription

Updates an existing subscription to match the specified parameters.
When changing prices or quantities, we optionally prorate the price we charge next month to make up for any price changes.
To preview how the proration is calculated, use the [create preview](https://docs.stripe.com/docs/api/invoices/create_preview.md) endpoint.

By default, we prorate subscription changes. For example, if a customer signs up on May 1 for a  price, they’ll be billed  immediately. If on May 15 they switch to a  price, then on June 1 they’ll be billed  ( for a renewal of her subscription, plus a  prorating adjustment for half of the previous month’s  difference). Similarly, a downgrade generates a credit that is applied to the next invoice. We also prorate when you make quantity changes.

Switching prices does not normally change the billing date or generate an immediate charge unless:

- The billing interval is changed (for example, from monthly to yearly).
- The subscription moves from free to paid.
- A trial starts or ends.

In these cases, we apply a credit for the unused time on the previous price, immediately charge the customer using the new price, and reset the billing date. Learn about how [Stripe immediately attempts payment for subscription changes](https://docs.stripe.com/docs/billing/subscriptions/upgrade-downgrade.md#immediate-payment).

If you want to charge for an upgrade immediately, pass `proration_behavior` as `always_invoice` to create prorations, automatically invoice the customer for those proration adjustments, and attempt to collect payment. If you pass `create_prorations`, the prorations are created but not automatically invoiced. If you want to bill the customer for the prorations before the subscription’s renewal date, you need to manually [invoice the customer](https://docs.stripe.com/docs/api/invoices/create.md).

If you don’t want to prorate, set the `proration_behavior` option to `none`. With this option, the customer is billed  on May 1 and  on June 1. Similarly, if you set `proration_behavior` to `none` when switching between different billing intervals (for example, from monthly to yearly), we don’t generate any credits for the old subscription’s unused time. We still reset the billing date and bill immediately for the new subscription.

Updating the quantity on a subscription many times in an hour may result in [rate limiting](https://docs.stripe.com/docs/rate-limits.md). If you need to bill for a frequently changing quantity, consider integrating [usage-based billing](https://docs.stripe.com/docs/billing/subscriptions/usage-based.md) instead.

The newly updated `Subscription` object, if the call succeeded.
If `payment_behavior` is `error_if_incomplete` and a charge is required for the update and it fails, this call raises [an error](https://docs.stripe.com/docs/api/errors.md), and the subscription update does not go into effect.

- `add_invoice_items` (array of objects, optional)
  A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items.

  - `add_invoice_items.discounts` (array of objects, optional)
    The coupons to redeem into discounts for the item.

    - `add_invoice_items.discounts.coupon` (string, optional)
      ID of the coupon to create a new discount for.

    - `add_invoice_items.discounts.discount` (string, optional)
      ID of an existing discount on the object (or one of its ancestors) to reuse.

    - `add_invoice_items.discounts.promotion_code` (string, optional)
      ID of the promotion code to create a new discount for.

  - `add_invoice_items.price` (string, optional)
    The ID of the price object. One of `price` or `price_data` is required.

  - `add_invoice_items.price_data` (object, optional)
    Data used to generate a new [Price](https://docs.stripe.com/docs/api/prices.md) object inline. One of `price` or `price_data` is required.

    - `add_invoice_items.price_data.currency` (enum, required)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `add_invoice_items.price_data.product` (string, required)
      The ID of the [Product](https://docs.stripe.com/api/products) that this [Price](https://docs.stripe.com/api/prices) will belong to.

    - `add_invoice_items.price_data.tax_behavior` (enum, optional)
      Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.

    - `add_invoice_items.price_data.unit_amount` (integer, optional)
      A positive integer in  (or 0 for a free price) representing how much to charge or a negative integer representing the amount to credit to the customer.

    - `add_invoice_items.price_data.unit_amount_decimal` (string, optional)
      Same as `unit_amount`, but accepts a decimal value in  with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

  - `add_invoice_items.quantity` (integer, optional)
    Quantity for this item. Defaults to 1.

  - `add_invoice_items.tax_rates` (array of strings, optional)
    The tax rates which apply to the item. When set, the `default_tax_rates` do not apply to this item.

- `application_fee_percent` (float, optional)
  A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner’s Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).

- `automatic_tax` (object, optional)
  Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed.

  - `automatic_tax.enabled` (boolean, required)
    Enabled automatic tax calculation which will automatically compute tax rates on all invoices generated by the subscription.

  - `automatic_tax.liability` (object, optional)
    The account that’s liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.

    - `automatic_tax.liability.type` (enum, required)
      Type of the account referenced in the request.

      Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

      Indicates that the account being referenced is the account making the API request.

    - `automatic_tax.liability.account` (string, optional)
      The connected account being referenced when `type` is `account`.

- `billing_cycle_anchor` (string, optional)
  Either `now` or `unchanged`. Setting the value to `now` resets the subscription’s billing cycle anchor to the current time (in UTC). For more information, see the billing cycle [documentation](https://docs.stripe.com/docs/billing/subscriptions/billing-cycle.md).

- `billing_thresholds` (object, optional)
  Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds.

  - `billing_thresholds.amount_gte` (integer, optional)
    Monetary threshold that triggers the subscription to advance to a new billing period

  - `billing_thresholds.reset_billing_cycle_anchor` (boolean, optional)
    Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged.

- `cancel_at` (timestamp, optional)
  A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period.

- `cancel_at_period_end` (boolean, optional)
  Indicate whether this subscription should cancel at the end of the current period (`current_period_end`). Defaults to `false`.

- `cancellation_details` (object, optional)
  Details about why this subscription was cancelled

  - `cancellation_details.comment` (string, optional)
    Additional comments about why the user canceled the subscription, if the subscription was canceled explicitly by the user.

  - `cancellation_details.feedback` (enum, optional)
    The customer submitted reason for why they canceled, if the subscription was canceled explicitly by the user.

    Customer service was less than expected

    Quality was less than expected

    Some features are missing

    Other reason

    I’m switching to a different service

    Ease of use was less than expected

    It’s too expensive

    I don’t use the service enough

- `collection_method` (enum, optional)
  Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.

- `default_payment_method` (string, optional)
  ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer’s [invoice_settings.default_payment_method](https://docs.stripe.com/docs/api/customers/object.md#customer_object-invoice_settings-default_payment_method) or [default_source](https://docs.stripe.com/docs/api/customers/object.md#customer_object-default_source).

- `default_source` (string, optional)
  ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer’s [invoice_settings.default_payment_method](https://docs.stripe.com/docs/api/customers/object.md#customer_object-invoice_settings-default_payment_method) or [default_source](https://docs.stripe.com/docs/api/customers/object.md#customer_object-default_source).

- `default_tax_rates` (array of strings, optional)
  The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription. Pass an empty string to remove previously-defined tax rates.

- `description` (string, optional)
  The subscription’s description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.

- `discounts` (array of objects, optional)
  The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription’s customer.

  - `discounts.coupon` (string, optional)
    ID of the coupon to create a new discount for.

  - `discounts.discount` (string, optional)
    ID of an existing discount on the object (or one of its ancestors) to reuse.

  - `discounts.promotion_code` (string, optional)
    ID of the promotion code to create a new discount for.

- `invoice_settings` (object, optional)
  All invoices will be billed using the specified settings.

  - `invoice_settings.account_tax_ids` (array of strings, optional)
    The account tax IDs associated with the subscription. Will be set on invoices generated by the subscription.

  - `invoice_settings.issuer` (object, optional)
    The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.

    - `invoice_settings.issuer.type` (enum, required)
      Type of the account referenced in the request.

      Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

      Indicates that the account being referenced is the account making the API request.

    - `invoice_settings.issuer.account` (string, optional)
      The connected account being referenced when `type` is `account`.

- `items` (array of objects, optional)
  A list of up to 20 subscription items, each with an attached price.

  - `items.billing_thresholds` (object, optional)
    Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.

    - `items.billing_thresholds.usage_gte` (integer, required)
      Number of units that meets the billing threshold to advance the subscription to a new billing period (e.g., it takes 10 $5 units to meet a $50 [monetary threshold](https://docs.stripe.com/docs/api/subscriptions/update.md#update_subscription-billing_thresholds-amount_gte))

  - `items.clear_usage` (boolean, optional)
    Delete all usage for a given subscription item. You must pass this when deleting a usage records subscription item. `clear_usage` has no effect if the plan has a billing meter attached.

  - `items.deleted` (boolean, optional)
    A flag that, if set to `true`, will delete the specified item.

  - `items.discounts` (array of objects, optional)
    The coupons to redeem into discounts for the subscription item.

    - `items.discounts.coupon` (string, optional)
      ID of the coupon to create a new discount for.

    - `items.discounts.discount` (string, optional)
      ID of an existing discount on the object (or one of its ancestors) to reuse.

    - `items.discounts.promotion_code` (string, optional)
      ID of the promotion code to create a new discount for.

  - `items.id` (string, optional)
    Subscription item to update.

  - `items.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

  - `items.price` (string, optional)
    The ID of the price object. One of `price` or `price_data` is required. When changing a subscription item’s price, `quantity` is set to 1 unless a `quantity` parameter is provided.

  - `items.price_data` (object, optional)
    Data used to generate a new [Price](https://docs.stripe.com/docs/api/prices.md) object inline. One of `price` or `price_data` is required.

    - `items.price_data.currency` (enum, required)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `items.price_data.product` (string, required)
      The ID of the [Product](https://docs.stripe.com/api/products) that this [Price](https://docs.stripe.com/api/prices) will belong to.

    - `items.price_data.recurring` (object, required)
      The recurring components of a price such as `interval` and `interval_count`.

      - `items.price_data.recurring.interval` (enum, required)
        Specifies billing frequency. Either `day`, `week`, `month` or `year`.

      - `items.price_data.recurring.interval_count` (integer, optional)
        The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).

    - `items.price_data.tax_behavior` (enum, optional)
      Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.

    - `items.price_data.unit_amount` (integer, optional)
      A positive integer in  (or 0 for a free price) representing how much to charge.

    - `items.price_data.unit_amount_decimal` (string, optional)
      Same as `unit_amount`, but accepts a decimal value in  with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

  - `items.quantity` (integer, optional)
    Quantity for this item.

  - `items.tax_rates` (array of strings, optional)
    A list of [Tax Rate](https://docs.stripe.com/docs/api/tax_rates.md) ids. These Tax Rates will override the [`default_tax_rates`](https://docs.stripe.com/docs/api/subscriptions/create.md#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `off_session` (boolean, optional)
  Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `false` (on-session).

- `on_behalf_of` (string, optional)
  The account on behalf of which to charge, for each of the subscription’s invoices.

- `pause_collection` (object, optional)
  If specified, payment collection for this subscription will be paused. Note that the subscription status will be unchanged and will not be updated to `paused`. Learn more about [pausing collection](https://docs.stripe.com/docs/billing/subscriptions/pause-payment.md).

  - `pause_collection.behavior` (enum, required)
    The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.

  - `pause_collection.resumes_at` (timestamp, optional)
    The time after which the subscription will resume collecting payments.

- `payment_behavior` (enum, optional)
  Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription’s invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://docs.stripe.com/docs/billing/migration/strong-customer-authentication.md) for Billing to learn more. This is the default behavior.

  Use `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice’s payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, [SCA regulation](https://docs.stripe.com/docs/billing/migration/strong-customer-authentication.md), or collecting a mandate for a bank debit payment method.

  Use `pending_if_incomplete` to update the subscription using [pending updates](https://docs.stripe.com/docs/billing/subscriptions/pending-updates.md). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://docs.stripe.com/docs/billing/pending-updates-reference.md#supported-attributes).

  Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription’s invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://docs.stripe.com/docs/upgrades.md#2019-03-14) to learn more.

- `payment_settings` (object, optional)
  Payment settings to pass to invoices created by the subscription.

  - `payment_settings.payment_method_options` (object, optional)
    Payment-method-specific configuration to provide to invoices created by the subscription.

    - `payment_settings.payment_method_options.acss_debit` (object, optional)
      This sub-hash contains details about the Canadian pre-authorized debit payment method options to pass to the invoice’s PaymentIntent.

      - `payment_settings.payment_method_options.acss_debit.mandate_options` (object, optional)
        Additional fields for Mandate creation

        - `payment_settings.payment_method_options.acss_debit.mandate_options.transaction_type` (enum, optional)
          Transaction type of the mandate.

          Transactions are made for business reasons

          Transactions are made for personal reasons

      - `payment_settings.payment_method_options.acss_debit.verification_method` (enum, optional)
        Verification method for the intent

        Instant verification with fallback to microdeposits.

        Instant verification.

        Verification using microdeposits.

    - `payment_settings.payment_method_options.bancontact` (object, optional)
      This sub-hash contains details about the Bancontact payment method options to pass to the invoice’s PaymentIntent.

      - `payment_settings.payment_method_options.bancontact.preferred_language` (enum, optional)
        Preferred language of the Bancontact authorization page that the customer is redirected to.

        German

        English

        French

        Dutch

    - `payment_settings.payment_method_options.card` (object, optional)
      This sub-hash contains details about the Card payment method options to pass to the invoice’s PaymentIntent.

      - `payment_settings.payment_method_options.card.mandate_options` (object, optional)
        Configuration options for setting up an eMandate for cards issued in India.

        - `payment_settings.payment_method_options.card.mandate_options.amount` (integer, optional)
          Amount to be charged for future payments.

        - `payment_settings.payment_method_options.card.mandate_options.amount_type` (enum, optional)
          One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param.

          If `fixed`, the `amount` param refers to the exact amount to be charged in future payments.

          If `maximum`, the amount charged can be up to the value passed for the `amount` param.

        - `payment_settings.payment_method_options.card.mandate_options.description` (string, optional)
          A description of the mandate or subscription that is meant to be displayed to the customer.

      - `payment_settings.payment_method_options.card.network` (string, optional)
        Selected network to process this Subscription on. Depends on the available networks of the card attached to the Subscription. Can be only set confirm-time.

      - `payment_settings.payment_method_options.card.request_three_d_secure` (enum, optional)
        We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://docs.stripe.com/docs/strong-customer-authentication.md). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Read our guide on [manually requesting 3D Secure](https://docs.stripe.com/docs/payments/3d-secure/authentication-flow.md#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.

        Use `any` to manually request 3DS with a preference for a `frictionless` flow, increasing the likelihood of the authentication being completed without any additional input from the customer.
        3DS will always be attempted if it is supported for the card, but Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow.
        To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

        (Default) Our SCA Engine automatically prompts your customers for authentication based on risk level and other requirements.

        Use `challenge` to request 3DS with a preference for a `challenge` flow, where the customer must respond to a prompt for active authentication. Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow. To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

    - `payment_settings.payment_method_options.customer_balance` (object, optional)
      This sub-hash contains details about the Bank transfer payment method options to pass to the invoice’s PaymentIntent.

      - `payment_settings.payment_method_options.customer_balance.bank_transfer` (object, optional)
        Configuration for the bank transfer funding type, if the `funding_type` is set to `bank_transfer`.

        - `payment_settings.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer` (object, optional)
          Configuration for eu_bank_transfer funding type.

          - `payment_settings.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer.country` (string, required)
            The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.

        - `payment_settings.payment_method_options.customer_balance.bank_transfer.type` (enum, optional)
          The bank transfer type that can be used for funding. Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.

      - `payment_settings.payment_method_options.customer_balance.funding_type` (enum, optional)
        The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`.

    - `payment_settings.payment_method_options.konbini` (object, optional)
      This sub-hash contains details about the Konbini payment method options to pass to the invoice’s PaymentIntent.

    - `payment_settings.payment_method_options.sepa_debit` (object, optional)
      This sub-hash contains details about the SEPA Direct Debit payment method options to pass to the invoice’s PaymentIntent.

    - `payment_settings.payment_method_options.us_bank_account` (object, optional)
      This sub-hash contains details about the ACH direct debit payment method options to pass to the invoice’s PaymentIntent.

      - `payment_settings.payment_method_options.us_bank_account.financial_connections` (object, optional)
        Additional fields for Financial Connections Session creation

        - `payment_settings.payment_method_options.us_bank_account.financial_connections.filters` (object, optional)
          Provide filters for the linked accounts that the customer can select for the payment method.

          - `payment_settings.payment_method_options.us_bank_account.financial_connections.filters.account_subcategories` (array of enums, optional)
            The account subcategories to use to filter for selectable accounts. Valid subcategories are `checking` and `savings`.

            Bank account subcategory is checking

            Bank account subcategory is savings

        - `payment_settings.payment_method_options.us_bank_account.financial_connections.permissions` (array of strings, optional)
          The list of permissions to request. If this parameter is passed, the `payment_method` permission must be included. Valid permissions include: `balances`, `ownership`, `payment_method`, and `transactions`.

        - `payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch` (array of enums, optional)
          List of data features that you would like to retrieve upon account creation.

          Requests to prefetch balance data on accounts collected in this session.

          Requests to prefetch ownership data on accounts collected in this session.

          Requests to prefetch transaction data on accounts collected in this session.

      - `payment_settings.payment_method_options.us_bank_account.verification_method` (enum, optional)
        Verification method for the intent

        Instant verification with fallback to microdeposits.

        Instant verification only.

        Verification using microdeposits. Cannot be used with Stripe Checkout, Hosted Invoices, or Payment Element.

  - `payment_settings.payment_method_types` (array of enums, optional)
    The list of payment method types (e.g. card) to provide to the invoice’s PaymentIntent. If not set, Stripe attempts to automatically determine the types to use by looking at the invoice’s default payment method, the subscription’s default payment method, the customer’s default payment method, and your [invoice template settings](https://dashboard.stripe.com/settings/billing/invoice). Should not be specified with payment_method_configuration

    ACH

    Canadian pre-authorized debit

    Affirm

    If set, the Subscription `collection_method` must be `send_invoice`.

    Amazon Pay

    BECS Direct Debit

    Bacs Direct Debit

    Bancontact

    If set, the Subscription `collection_method` must be `send_invoice`.

    Boleto

    Card

    Cash App Pay

    Crypto

    If set, the Subscription `collection_method` must be `send_invoice`.

    Bank transfer

    If set, the Subscription `collection_method` must be `send_invoice`.

    EPS

    If set, the Subscription `collection_method` must be `send_invoice`.

    FPX

    If set, the Subscription `collection_method` must be `send_invoice`.

    giropay

    If set, the Subscription `collection_method` must be `send_invoice`.

    GrabPay

    If set, the Subscription `collection_method` must be `send_invoice`.

    iDEAL

    If set, the Subscription `collection_method` must be `send_invoice`.

    Kakao Pay

    Klarna

    If set, the Subscription `collection_method` must be `send_invoice`.

    Konbini

    If set, the Subscription `collection_method` must be `send_invoice`.

    Korean card

    Link

    Multibanco

    If set, the Subscription `collection_method` must be `send_invoice`.

    Naver Pay

    NZ BECS Direct Debit

    Przelewy24

    If set, the Subscription `collection_method` must be `send_invoice`.

    PAYCO

    If set, the Subscription `collection_method` must be `send_invoice`.

    PayNow

    If set, the Subscription `collection_method` must be `send_invoice`.

    PayPal

    PromptPay

    If set, the Subscription `collection_method` must be `send_invoice`.

    Revolut Pay

    SEPA Direct Debit

    SOFORT

    If set, the Subscription `collection_method` must be `send_invoice`.

    ACH direct debit

    WeChat Pay

    If set, the Subscription `collection_method` must be `send_invoice`.

  - `payment_settings.save_default_payment_method` (enum, optional)
    Configure whether Stripe updates `subscription.default_payment_method` when payment succeeds. Defaults to `off` if unspecified.

    Stripe never sets `subscription.default_payment_method`.

    Stripe sets `subscription.default_payment_method` when a subscription payment succeeds.

- `pending_invoice_item_interval` (object, optional)
  Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://docs.stripe.com/docs/api.md#create_invoice) for the given subscription at the specified interval.

  - `pending_invoice_item_interval.interval` (enum, required)
    Specifies invoicing frequency. Either `day`, `week`, `month` or `year`.

  - `pending_invoice_item_interval.interval_count` (integer, optional)
    The number of intervals between invoices. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks).

- `proration_behavior` (enum, optional)
  Determines how to handle [prorations](https://docs.stripe.com/docs/billing/subscriptions/prorations.md) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item’s `quantity` changes. The default value is `create_prorations`.

  Always invoice immediately for prorations.

  Will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under [certain conditions](https://docs.stripe.com/docs/subscriptions/upgrading-downgrading.md#immediate-payment).

  Disable creating prorations in this request.

- `proration_date` (timestamp, optional)
  If set, prorations will be calculated as though the subscription was updated at the given time. This can be used to apply exactly the same prorations that were previewed with the [create preview](https://stripe.com/docs/api/invoices/create_preview) endpoint. `proration_date` can also be used to implement custom proration logic, such as prorating by day instead of by second, by providing the time that you wish to use for proration calculations.

- `transfer_data` (object, optional)
  If specified, the funds from the subscription’s invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges. This will be unset if you POST an empty value.

  - `transfer_data.destination` (string, required)
    ID of an existing, connected Stripe account.

  - `transfer_data.amount_percent` (float, optional)
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.

- `trial_end` (string | timestamp, optional)
  Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. If set, `trial_end` will override the default trial period of the plan the customer is being subscribed to. The `billing_cycle_anchor` will be updated to the `trial_end` value. The special value `now` can be provided to end the customer’s trial immediately. Can be at most two years from `billing_cycle_anchor`.

- `trial_from_plan` (boolean, optional)
  Indicates if a plan’s `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://docs.stripe.com/docs/billing/subscriptions/trials.md) to learn more.

- `trial_settings` (object, optional)
  Settings related to subscription trials.

  - `trial_settings.end_behavior` (object, required)
    Defines how the subscription should behave when the user’s free trial ends.

    - `trial_settings.end_behavior.missing_payment_method` (enum, required)
      Indicates how the subscription should change when the trial ends if the user did not provide a payment method.

      Cancel the subscription if a payment method is not attached when the trial ends.

      Create an invoice when the trial ends, even if the user did not set up a payment method.

      Pause the subscription if a payment method is not attached when the trial ends.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new SubscriptionUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var service = new SubscriptionService();
Subscription subscription = service.Update("sub_1MowQVLkdIwHu7ixeRlqHVzs", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.SubscriptionParams{};
params.AddMetadata("order_id", "6735")
result, err := subscription.Update("sub_1MowQVLkdIwHu7ixeRlqHVzs", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Subscription resource = Subscription.retrieve("sub_1MowQVLkdIwHu7ixeRlqHVzs");

SubscriptionUpdateParams params =
  SubscriptionUpdateParams.builder().putMetadata("order_id", "6735").build();

Subscription subscription = resource.update(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const subscription = await stripe.subscriptions.update(
  'sub_1MowQVLkdIwHu7ixeRlqHVzs',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

subscription = stripe.Subscription.modify(
  "sub_1MowQVLkdIwHu7ixeRlqHVzs",
  metadata={"order_id": "6735"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$subscription = $stripe->subscriptions->update(
  'sub_1MowQVLkdIwHu7ixeRlqHVzs',
  ['metadata' => ['order_id' => '6735']]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

subscription = Stripe::Subscription.update(
  'sub_1MowQVLkdIwHu7ixeRlqHVzs',
  {metadata: {order_id: '6735'}},
)
```

### Response

```json
{
  "id": "sub_1MowQVLkdIwHu7ixeRlqHVzs",
  "object": "subscription",
  "application": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null
  },
  "billing_cycle_anchor": 1679609767,
  "cancel_at": null,
  "cancel_at_period_end": false,
  "canceled_at": null,
  "cancellation_details": {
    "comment": null,
    "feedback": null,
    "reason": null
  },
  "collection_method": "charge_automatically",
  "created": 1679609767,
  "currency": "usd",
  "customer": "cus_Na6dX7aXxi11N4",
  "days_until_due": null,
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discounts": null,
  "ended_at": null,
  "invoice_settings": {
    "issuer": {
      "type": "self"
    }
  },
  "items": {
    "object": "list",
    "data": [
      {
        "id": "si_Na6dzxczY5fwHx",
        "object": "subscription_item",
        "created": 1679609768,
        "current_period_end": 1682288167,
        "current_period_start": 1679609767,
        "metadata": {},
        "plan": {
          "id": "price_1MowQULkdIwHu7ixraBm864M",
          "object": "plan",
          "active": true,
          "amount": 1000,
          "amount_decimal": "1000",
          "billing_scheme": "per_unit",
          "created": 1679609766,
          "currency": "usd",
          "discounts": null,
          "interval": "month",
          "interval_count": 1,
          "livemode": false,
          "metadata": {},
          "nickname": null,
          "product": "prod_Na6dGcTsmU0I4R",
          "tiers_mode": null,
          "transform_usage": null,
          "trial_period_days": null,
          "usage_type": "licensed"
        },
        "price": {
          "id": "price_1MowQULkdIwHu7ixraBm864M",
          "object": "price",
          "active": true,
          "billing_scheme": "per_unit",
          "created": 1679609766,
          "currency": "usd",
          "custom_unit_amount": null,
          "livemode": false,
          "lookup_key": null,
          "metadata": {},
          "nickname": null,
          "product": "prod_Na6dGcTsmU0I4R",
          "recurring": {
            "interval": "month",
            "interval_count": 1,
            "trial_period_days": null,
            "usage_type": "licensed"
          },
          "tax_behavior": "unspecified",
          "tiers_mode": null,
          "transform_quantity": null,
          "type": "recurring",
          "unit_amount": 1000,
          "unit_amount_decimal": "1000"
        },
        "quantity": 1,
        "subscription": "sub_1MowQVLkdIwHu7ixeRlqHVzs",
        "tax_rates": []
      }
    ],
    "has_more": false,
    "total_count": 1,
    "url": "/v1/subscription_items?subscription=sub_1MowQVLkdIwHu7ixeRlqHVzs"
  },
  "latest_invoice": "in_1MowQWLkdIwHu7ixuzkSPfKd",
  "livemode": false,
  "metadata": {
    "order_id": "6735"
  },
  "next_pending_invoice_item_invoice": null,
  "on_behalf_of": null,
  "pause_collection": null,
  "payment_settings": {
    "payment_method_options": null,
    "payment_method_types": null,
    "save_default_payment_method": "off"
  },
  "pending_invoice_item_interval": null,
  "pending_setup_intent": null,
  "pending_update": null,
  "schedule": null,
  "start_date": 1679609767,
  "status": "active",
  "test_clock": null,
  "transfer_data": null,
  "trial_end": null,
  "trial_settings": {
    "end_behavior": {
      "missing_payment_method": "create_invoice"
    }
  },
  "trial_start": null
}
```