# The Customer object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `address` (nullable object)
  The customer’s address.

  - `address.city` (nullable string)
    City, district, suburb, town, or village.

  - `address.country` (nullable string)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `address.line1` (nullable string)
    Address line 1 (e.g., street, PO Box, or company name).

  - `address.line2` (nullable string)
    Address line 2 (e.g., apartment, suite, unit, or building).

  - `address.postal_code` (nullable string)
    ZIP or postal code.

  - `address.state` (nullable string)
    State, county, province, or region.

- `balance` (integer)
  The current balance, if any, that’s stored on the customer in their default currency. If negative, the customer has credit to apply to their next invoice. If positive, the customer has an amount owed that’s added to their next invoice. The balance only considers amounts that Stripe hasn’t successfully applied to any invoice. It doesn’t reflect unpaid invoices. This balance is only taken into account after invoices finalize. For multi-currency balances, see [invoice_credit_balance](https://docs.stripe.com/docs/api/customers/object.md#customer_object-invoice_credit_balance).

- `cash_balance` (nullable object)
  The current funds being held by Stripe on behalf of the customer. You can apply these funds towards payment intents when the source is “cash_balance”. The `settings[reconciliation_mode]` field describes if these funds apply to these payment intents manually or automatically.

  - `cash_balance.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `cash_balance.available` (nullable object)
    A hash of all cash balances available to this customer. You cannot delete a customer with any cash balances, even if the balance is 0. Amounts are represented in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

  - `cash_balance.customer` (string)
    The ID of the customer whose cash balance this object represents.

  - `cash_balance.livemode` (boolean)
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

  - `cash_balance.settings` (object)
    A hash of settings for this cash balance.

    - `cash_balance.settings.reconciliation_mode` (enum)
      The configuration for how funds that land in the customer cash balance are reconciled.

    - `cash_balance.settings.using_merchant_default` (boolean)
      A flag to indicate if reconciliation mode returned is the user’s default or is specific to this customer cash balance

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (nullable string)
  Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) the customer can be charged in for recurring billing purposes.

- `default_source` (nullable string)
  ID of the default payment source for the customer.

  If you use payment methods created through the PaymentMethods API, see the [invoice_settings.default_payment_method](https://docs.stripe.com/docs/api/customers/object.md#customer_object-invoice_settings-default_payment_method) field instead.

- `delinquent` (nullable boolean)
  Tracks the most recent state change on any invoice belonging to the customer. Paying an invoice or marking it uncollectible via the API will set this field to false. An automatic payment failure or passing the `invoice.due_date` will set this field to `true`.

  If an invoice becomes uncollectible by [dunning](https://docs.stripe.com/docs/billing/automatic-collection.md), `delinquent` doesn’t reset to `false`.

  If you care whether the customer has paid their most recent subscription invoice, use `subscription.status` instead. Paying or marking uncollectible any customer invoice regardless of whether it is the latest invoice for a subscription will always set this field to `false`.

- `description` (nullable string)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `discount` (nullable object)
  Describes the current discount active on the customer, if there is one.

  - `discount.id` (string)
    The ID of the discount object. Discounts cannot be fetched by ID. Use `expand[]=discounts` in API calls to expand discount IDs in an array.

  - `discount.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `discount.checkout_session` (nullable string)
    The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode.

  - `discount.coupon` (object)
    Hash describing the coupon applied to create this discount.

    - `discount.coupon.id` (string)
      Unique identifier for the object.

    - `discount.coupon.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `discount.coupon.amount_off` (nullable integer)
      Amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer.

    - `discount.coupon.applies_to` (nullable object)
      Contains information about what this coupon applies to.

      - `discount.coupon.applies_to.products` (array of strings)
        A list of product IDs this coupon applies to

    - `discount.coupon.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `discount.coupon.currency` (nullable enum)
      If `amount_off` has been set, the three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the amount to take off.

    - `discount.coupon.currency_options` (nullable object)
      Coupons defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

      - `discount.coupon.currency_options.<currency>.amount_off` (integer)
        Amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer.

    - `discount.coupon.duration` (enum)
      One of `forever`, `once`, or `repeating`. Describes how long a customer who applies this coupon will get the discount.

      Applies to all charges from a subscription with this coupon applied.

      Applies to the first charge from a subscription with this coupon applied.

      Applies to charges in the first `duration_in_months` months from a subscription with this coupon applied. This value is deprecated and will be replaced in future versions of the API.

    - `discount.coupon.duration_in_months` (nullable integer)
      If `duration` is `repeating`, the number of months the coupon applies. Null if coupon `duration` is `forever` or `once`.

    - `discount.coupon.livemode` (boolean)
      Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

    - `discount.coupon.max_redemptions` (nullable integer)
      Maximum number of times this coupon can be redeemed, in total, across all customers, before it is no longer valid.

    - `discount.coupon.metadata` (nullable object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `discount.coupon.name` (nullable string)
      Name of the coupon displayed to customers on for instance invoices or receipts.

    - `discount.coupon.percent_off` (nullable float)
      Percent that will be taken off the subtotal of any invoices for this customer for the duration of the coupon. For example, a coupon with percent_off of 50 will make a 100 invoice 50 instead.

    - `discount.coupon.redeem_by` (nullable timestamp)
      Date after which the coupon can no longer be redeemed.

    - `discount.coupon.times_redeemed` (integer)
      Number of times this coupon has been applied to a customer.

    - `discount.coupon.valid` (boolean)
      Taking account of the above properties, whether this coupon can still be applied to a customer.

  - `discount.customer` (nullable string)
    The ID of the customer associated with this discount.

  - `discount.end` (nullable timestamp)
    If the coupon has a duration of `repeating`, the date that this discount will end. If the coupon has a duration of `once` or `forever`, this attribute will be null.

  - `discount.invoice` (nullable string)
    The invoice that the discount’s coupon was applied to, if it was applied directly to a particular invoice.

  - `discount.invoice_item` (nullable string)
    The invoice item `id` (or invoice line item `id` for invoice line items of type=‘subscription’) that the discount’s coupon was applied to, if it was applied directly to a particular invoice item or invoice line item.

  - `discount.promotion_code` (nullable string)
    The promotion code applied to create this discount.

  - `discount.start` (timestamp)
    Date that the coupon was applied.

  - `discount.subscription` (nullable string)
    The subscription that this coupon is applied to, if it is applied to a particular subscription.

  - `discount.subscription_item` (nullable string)
    The subscription item that this coupon is applied to, if it is applied to a particular subscription item.

- `email` (nullable string)
  The customer’s email address.

- `invoice_credit_balance` (object)
  The current multi-currency balances, if any, that’s stored on the customer. If positive in a currency, the customer has a credit to apply to their next invoice denominated in that currency. If negative, the customer has an amount owed that’s added to their next invoice denominated in that currency. These balances don’t apply to unpaid invoices. They solely track amounts that Stripe hasn’t successfully applied to any invoice. Stripe only applies a balance in a specific currency to an invoice after that invoice (which is in the same currency) finalizes.

- `invoice_prefix` (nullable string)
  The prefix for the customer used to generate unique invoice numbers.

- `invoice_settings` (object)
  The customer’s default invoice settings.

  - `invoice_settings.custom_fields` (nullable array of objects)
    Default custom fields to be displayed on invoices for this customer.

    - `invoice_settings.custom_fields.name` (string)
      The name of the custom field.

    - `invoice_settings.custom_fields.value` (string)
      The value of the custom field.

  - `invoice_settings.default_payment_method` (nullable string)
    ID of a payment method that’s attached to the customer, to be used as the customer’s default payment method for subscriptions and invoices.

  - `invoice_settings.footer` (nullable string)
    Default footer to be displayed on invoices for this customer.

  - `invoice_settings.rendering_options` (nullable object)
    Default options for invoice PDF rendering for this customer.

    - `invoice_settings.rendering_options.amount_tax_display` (nullable string)
      How line-item prices and amounts will be displayed with respect to tax on invoice PDFs.

    - `invoice_settings.rendering_options.template` (nullable string)
      ID of the invoice rendering template to be used for this customer’s invoices. If set, the template will be used on all invoices for this customer unless a template is set directly on the invoice.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `name` (nullable string)
  The customer’s full name or business name.

- `next_invoice_sequence` (nullable integer)
  The suffix of the customer’s next invoice number (for example, 0001). When the account uses account level sequencing, this parameter is ignored in API requests and the field omitted in API responses.

- `phone` (nullable string)
  The customer’s phone number.

- `preferred_locales` (nullable array of strings)
  The customer’s preferred locales (languages), ordered by preference.

- `shipping` (nullable object)
  Mailing and shipping address for the customer. Appears on invoices emailed to this customer.

  - `shipping.address` (object)
    Customer shipping address.

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

  - `shipping.name` (string)
    Customer name.

  - `shipping.phone` (nullable string)
    Customer phone (including extension).

- `sources` (nullable object)
  The customer’s payment sources, if any.

  - `sources.object` (string)
    String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

  - `sources.data` (array of objects)
    Details about each object.

    - `sources.data.id` (string)
      Unique identifier for the object.

    - `sources.data.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `sources.data.account` (nullable string)
      The account this bank account belongs to. Only applicable on Accounts (not customers or recipients) This property is only available when returned as an [External Account](https://docs.stripe.com/api/external_account_bank_accounts/object.md) where [controller.is_controller](https://docs.stripe.com/api/accounts/object.md#account_object-controller-is_controller) is `true`.

    - `sources.data.account_holder_name` (nullable string)
      The name of the person or business that owns the bank account.

    - `sources.data.account_holder_type` (nullable string)
      The type of entity that holds the account. This can be either `individual` or `company`.

    - `sources.data.account_type` (nullable string)
      The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`.

    - `sources.data.available_payout_methods` (nullable array of enums)
      A set of available payout methods for this bank account. Only values from this set should be passed as the `method` when creating a payout.

    - `sources.data.bank_name` (nullable string)
      Name of the bank associated with the routing number (e.g., `WELLS FARGO`).

    - `sources.data.country` (string)
      Two-letter ISO code representing the country the bank account is located in.

    - `sources.data.currency` (enum)
      Three-letter [ISO code for the currency](https://stripe.com/docs/payouts) paid out to the bank account.

    - `sources.data.customer` (nullable string)
      The ID of the customer that the bank account is associated with.

    - `sources.data.fingerprint` (nullable string)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `sources.data.last4` (string)
      The last four digits of the bank account number.

    - `sources.data.metadata` (nullable object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `sources.data.routing_number` (nullable string)
      The routing transit number for the bank account.

    - `sources.data.status` (string)
      For bank accounts, possible values are `new`, `validated`, `verified`, `verification_failed`, or `errored`. A bank account that hasn’t had any activity or validation performed is `new`. If Stripe can determine that the bank account exists, its status will be `validated`. Note that there often isn’t enough information to know (e.g., for smaller credit unions), and the validation is not always run. If customer bank account verification has succeeded, the bank account status will be `verified`. If the verification failed for any reason, such as microdeposit failure, the status will be `verification_failed`. If a payout sent to this bank account fails, we’ll set the status to `errored` and will not continue to send [scheduled payouts](https://stripe.com/docs/payouts#payout-schedule) until the bank details are updated.

      For external accounts, possible values are `new`, `errored` and `verification_failed`. If a payout fails, the status is set to `errored` and scheduled payouts are stopped until account details are updated. In the US and India, if we can’t [verify the owner of the bank account](https://support.stripe.com/questions/bank-account-ownership-verification), we’ll set the status to `verification_failed`. Other validations aren’t run against external accounts because they’re only used for payouts. This means the other statuses don’t apply.

  - `sources.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `sources.url` (string)
    The URL where this list can be accessed.

- `subscriptions` (nullable object)
  The customer’s current subscriptions, if any.

  - `subscriptions.object` (string)
    String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

  - `subscriptions.data` (array of objects)
    Details about each object.

    - `subscriptions.data.id` (string)
      Unique identifier for the object.

    - `subscriptions.data.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `subscriptions.data.application` (nullable string)
      ID of the Connect Application that created the subscription.

    - `subscriptions.data.application_fee_percent` (nullable float)
      A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner’s Stripe account.

    - `subscriptions.data.automatic_tax` (object)
      Automatic tax settings for this subscription.

      - `subscriptions.data.automatic_tax.disabled_reason` (nullable enum)
        If Stripe disabled automatic tax, this enum describes why.

        Stripe’s systems automatically turned off Tax for this subscription when finalizing one of its invoices with a missing or incomplete location for your customer.

      - `subscriptions.data.automatic_tax.enabled` (boolean)
        Whether Stripe automatically computes tax on this subscription.

      - `subscriptions.data.automatic_tax.liability` (nullable object)
        The account that’s liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.

        - `subscriptions.data.automatic_tax.liability.account` (nullable string)
          The connected account being referenced when `type` is `account`.

        - `subscriptions.data.automatic_tax.liability.type` (enum)
          Type of the account referenced.

          Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

          Indicates that the account being referenced is the account making the API request.

    - `subscriptions.data.billing_cycle_anchor` (timestamp)
      The reference point that aligns future [billing cycle](https://docs.stripe.com/docs/subscriptions/billing-cycle.md) dates. It sets the day of week for `week` intervals, the day of month for `month` and `year` intervals, and the month of year for `year` intervals. The timestamp is in UTC format.

    - `subscriptions.data.billing_cycle_anchor_config` (nullable object)
      The fixed values used to calculate the `billing_cycle_anchor`.

      - `subscriptions.data.billing_cycle_anchor_config.day_of_month` (integer)
        The day of the month of the billing_cycle_anchor.

      - `subscriptions.data.billing_cycle_anchor_config.hour` (nullable integer)
        The hour of the day of the billing_cycle_anchor.

      - `subscriptions.data.billing_cycle_anchor_config.minute` (nullable integer)
        The minute of the hour of the billing_cycle_anchor.

      - `subscriptions.data.billing_cycle_anchor_config.month` (nullable integer)
        The month to start full cycle billing periods.

      - `subscriptions.data.billing_cycle_anchor_config.second` (nullable integer)
        The second of the minute of the billing_cycle_anchor.

    - `subscriptions.data.billing_mode` (object)
      Controls how prorations and invoices for subscriptions are calculated and orchestrated.

      - `subscriptions.data.billing_mode.type` (enum)
        Controls how prorations and invoices for subscriptions are calculated and orchestrated.

        Calculations for subscriptions and invoices are based on legacy defaults.

        Supports more flexible calculation and orchestration options for subscriptions and invoices.

      - `subscriptions.data.billing_mode.updated_at` (nullable timestamp)
        Details on when the current billing_mode was adopted.

    - `subscriptions.data.billing_thresholds` (nullable object)
      Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period

      - `subscriptions.data.billing_thresholds.amount_gte` (nullable integer)
        Monetary threshold that triggers the subscription to create an invoice

      - `subscriptions.data.billing_thresholds.reset_billing_cycle_anchor` (nullable boolean)
        Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged. This value may not be `true` if the subscription contains items with plans that have `aggregate_usage=last_ever`.

    - `subscriptions.data.cancel_at` (nullable timestamp)
      A date in the future at which the subscription will automatically get canceled

    - `subscriptions.data.cancel_at_period_end` (boolean)
      Whether this subscription will (if `status=active`) or did (if `status=canceled`) cancel at the end of the current billing period.

    - `subscriptions.data.canceled_at` (nullable timestamp)
      If the subscription has been canceled, the date of that cancellation. If the subscription was canceled with `cancel_at_period_end`, `canceled_at` will reflect the time of the most recent update request, not the end of the subscription period when the subscription is automatically moved to a canceled state.

    - `subscriptions.data.cancellation_details` (nullable object)
      Details about why this subscription was cancelled

      - `subscriptions.data.cancellation_details.comment` (nullable string)
        Additional comments about why the user canceled the subscription, if the subscription was canceled explicitly by the user.

      - `subscriptions.data.cancellation_details.feedback` (nullable enum)
        The customer submitted reason for why they canceled, if the subscription was canceled explicitly by the user.

        Customer service was less than expected

        Quality was less than expected

        Some features are missing

        Other reason

        I’m switching to a different service

        Ease of use was less than expected

        It’s too expensive

        I don’t use the service enough

      - `subscriptions.data.cancellation_details.reason` (nullable enum)
        Why this subscription was canceled.

    - `subscriptions.data.collection_method` (enum)
      Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`.

    - `subscriptions.data.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `subscriptions.data.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `subscriptions.data.customer` (string)
      ID of the customer who owns the subscription.

    - `subscriptions.data.default_payment_method` (nullable string)
      ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer’s [invoice_settings.default_payment_method](https://docs.stripe.com/docs/api/customers/object.md#customer_object-invoice_settings-default_payment_method) or [default_source](https://docs.stripe.com/docs/api/customers/object.md#customer_object-default_source).

    - `subscriptions.data.default_source` (nullable string)
      ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer’s [invoice_settings.default_payment_method](https://docs.stripe.com/docs/api/customers/object.md#customer_object-invoice_settings-default_payment_method) or [default_source](https://docs.stripe.com/docs/api/customers/object.md#customer_object-default_source).

    - `subscriptions.data.default_tax_rates` (nullable array of objects)
      The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription.

      - `subscriptions.data.default_tax_rates.id` (string)
        Unique identifier for the object.

      - `subscriptions.data.default_tax_rates.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `subscriptions.data.default_tax_rates.active` (boolean)
        Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

      - `subscriptions.data.default_tax_rates.country` (nullable string)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `subscriptions.data.default_tax_rates.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `subscriptions.data.default_tax_rates.description` (nullable string)
        An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

      - `subscriptions.data.default_tax_rates.display_name` (string)
        The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

      - `subscriptions.data.default_tax_rates.effective_percentage` (nullable float)
        Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true,
        this percentage reflects the rate actually used to calculate tax based on the product’s taxability
        and whether the user is registered to collect taxes in the corresponding jurisdiction.

      - `subscriptions.data.default_tax_rates.flat_amount` (nullable object)
        The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

        - `subscriptions.data.default_tax_rates.flat_amount.amount` (integer)
          Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

        - `subscriptions.data.default_tax_rates.flat_amount.currency` (string)
          Three-letter ISO currency code, in lowercase.

      - `subscriptions.data.default_tax_rates.inclusive` (boolean)
        This specifies if the tax rate is inclusive or exclusive.

      - `subscriptions.data.default_tax_rates.jurisdiction` (nullable string)
        The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

      - `subscriptions.data.default_tax_rates.jurisdiction_level` (nullable enum)
        The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.

      - `subscriptions.data.default_tax_rates.livemode` (boolean)
        Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

      - `subscriptions.data.default_tax_rates.metadata` (nullable object)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `subscriptions.data.default_tax_rates.percentage` (float)
        Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

      - `subscriptions.data.default_tax_rates.rate_type` (nullable enum)
        Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.

        A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

        A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

      - `subscriptions.data.default_tax_rates.state` (nullable string)
        [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

      - `subscriptions.data.default_tax_rates.tax_type` (nullable enum)
        The high-level tax type, such as `vat` or `sales_tax`.

        Amusement Tax

        Communications Tax

        Goods and Services Tax

        Harmonized Sales Tax

        Integrated Goods and Services Tax

        Japanese Consumption Tax

        Chicago Lease Tax

        Provincial Sales Tax

        Quebec Sales Tax

        Retail Delivery Fee

        Retail Sales Tax

        Sales Tax

        Service Tax

        Value-Added Tax

    - `subscriptions.data.description` (nullable string)
      The subscription’s description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.

    - `subscriptions.data.discounts` (array of strings)
      The discounts applied to the subscription. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount.

    - `subscriptions.data.ended_at` (nullable timestamp)
      If the subscription has ended, the date the subscription ended.

    - `subscriptions.data.invoice_settings` (object)
      All invoices will be billed using the specified settings.

      - `subscriptions.data.invoice_settings.account_tax_ids` (nullable array of strings)
        The account tax IDs associated with the subscription. Will be set on invoices generated by the subscription.

      - `subscriptions.data.invoice_settings.issuer` (object)
        The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.

        - `subscriptions.data.invoice_settings.issuer.account` (nullable string)
          The connected account being referenced when `type` is `account`.

        - `subscriptions.data.invoice_settings.issuer.type` (enum)
          Type of the account referenced.

          Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

          Indicates that the account being referenced is the account making the API request.

    - `subscriptions.data.items` (object)
      List of subscription items, each with an attached price.

      - `subscriptions.data.items.object` (string)
        String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

      - `subscriptions.data.items.data` (array of objects)
        Details about each object.

        - `subscriptions.data.items.data.id` (string)
          Unique identifier for the object.

        - `subscriptions.data.items.data.object` (string)
          String representing the object’s type. Objects of the same type share the same value.

        - `subscriptions.data.items.data.billing_thresholds` (nullable object)
          Define thresholds at which an invoice will be sent, and the related subscription advanced to a new billing period

          - `subscriptions.data.items.data.billing_thresholds.usage_gte` (nullable integer)
            Usage threshold that triggers the subscription to create an invoice

        - `subscriptions.data.items.data.created` (integer)
          Time at which the object was created. Measured in seconds since the Unix epoch.

        - `subscriptions.data.items.data.current_period_end` (timestamp)
          The end time of this subscription item’s current billing period.

        - `subscriptions.data.items.data.current_period_start` (timestamp)
          The start time of this subscription item’s current billing period.

        - `subscriptions.data.items.data.discounts` (array of strings)
          The discounts applied to the subscription item. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount.

        - `subscriptions.data.items.data.metadata` (object)
          Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

        - `subscriptions.data.items.data.price` (object)
          The price the customer is subscribed to.

          - `subscriptions.data.items.data.price.id` (string)
            Unique identifier for the object.

          - `subscriptions.data.items.data.price.object` (string)
            String representing the object’s type. Objects of the same type share the same value.

          - `subscriptions.data.items.data.price.active` (boolean)
            Whether the price can be used for new purchases.

          - `subscriptions.data.items.data.price.billing_scheme` (enum)
            Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.

          - `subscriptions.data.items.data.price.created` (timestamp)
            Time at which the object was created. Measured in seconds since the Unix epoch.

          - `subscriptions.data.items.data.price.currency` (enum)
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

          - `subscriptions.data.items.data.price.currency_options` (nullable object)
            Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

            - `subscriptions.data.items.data.price.currency_options.<currency>.custom_unit_amount` (nullable object)
              When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

              - `subscriptions.data.items.data.price.currency_options.<currency>.custom_unit_amount.maximum` (nullable integer)
                The maximum unit amount the customer can specify for this item.

              - `subscriptions.data.items.data.price.currency_options.<currency>.custom_unit_amount.minimum` (nullable integer)
                The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

              - `subscriptions.data.items.data.price.currency_options.<currency>.custom_unit_amount.preset` (nullable integer)
                The starting unit amount which can be updated by the customer.

            - `subscriptions.data.items.data.price.currency_options.<currency>.tax_behavior` (nullable enum)
              Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.

            - `subscriptions.data.items.data.price.currency_options.<currency>.tiers` (nullable array of objects)
              Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

              - `subscriptions.data.items.data.price.currency_options.<currency>.tiers.flat_amount` (nullable integer)
                Price for the entire tier.

              - `subscriptions.data.items.data.price.currency_options.<currency>.tiers.flat_amount_decimal` (nullable decimal string)
                Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

              - `subscriptions.data.items.data.price.currency_options.<currency>.tiers.unit_amount` (nullable integer)
                Per unit price for units relevant to the tier.

              - `subscriptions.data.items.data.price.currency_options.<currency>.tiers.unit_amount_decimal` (nullable decimal string)
                Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

              - `subscriptions.data.items.data.price.currency_options.<currency>.tiers.up_to` (nullable integer)
                Up to and including to this quantity will be contained in the tier.

            - `subscriptions.data.items.data.price.currency_options.<currency>.unit_amount` (nullable integer)
              The unit amount in  to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

            - `subscriptions.data.items.data.price.currency_options.<currency>.unit_amount_decimal` (nullable decimal string)
              The unit amount in  to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

          - `subscriptions.data.items.data.price.custom_unit_amount` (nullable object)
            When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

            - `subscriptions.data.items.data.price.custom_unit_amount.maximum` (nullable integer)
              The maximum unit amount the customer can specify for this item.

            - `subscriptions.data.items.data.price.custom_unit_amount.minimum` (nullable integer)
              The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

            - `subscriptions.data.items.data.price.custom_unit_amount.preset` (nullable integer)
              The starting unit amount which can be updated by the customer.

          - `subscriptions.data.items.data.price.livemode` (boolean)
            Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

          - `subscriptions.data.items.data.price.lookup_key` (nullable string)
            A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters.

          - `subscriptions.data.items.data.price.metadata` (object)
            Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

          - `subscriptions.data.items.data.price.nickname` (nullable string)
            A brief description of the price, hidden from customers.

          - `subscriptions.data.items.data.price.product` (string)
            The ID of the product this price is associated with.

          - `subscriptions.data.items.data.price.recurring` (nullable object)
            The recurring components of a price such as `interval` and `usage_type`.

            - `subscriptions.data.items.data.price.recurring.interval` (enum)
              The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`.

            - `subscriptions.data.items.data.price.recurring.interval_count` (integer)
              The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months.

            - `subscriptions.data.items.data.price.recurring.meter` (nullable string)
              The meter tracking the usage of a metered price

            - `subscriptions.data.items.data.price.recurring.usage_type` (enum)
              Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`.

          - `subscriptions.data.items.data.price.tax_behavior` (nullable enum)
            Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.

          - `subscriptions.data.items.data.price.tiers` (nullable array of objects)
            Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

            - `subscriptions.data.items.data.price.tiers.flat_amount` (nullable integer)
              Price for the entire tier.

            - `subscriptions.data.items.data.price.tiers.flat_amount_decimal` (nullable decimal string)
              Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

            - `subscriptions.data.items.data.price.tiers.unit_amount` (nullable integer)
              Per unit price for units relevant to the tier.

            - `subscriptions.data.items.data.price.tiers.unit_amount_decimal` (nullable decimal string)
              Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

            - `subscriptions.data.items.data.price.tiers.up_to` (nullable integer)
              Up to and including to this quantity will be contained in the tier.

          - `subscriptions.data.items.data.price.tiers_mode` (nullable enum)
            Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price. In `graduated` tiering, pricing can change as the quantity grows.

          - `subscriptions.data.items.data.price.transform_quantity` (nullable object)
            Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`.

            - `subscriptions.data.items.data.price.transform_quantity.divide_by` (integer)
              Divide usage by this number.

            - `subscriptions.data.items.data.price.transform_quantity.round` (enum)
              After division, either round the result `up` or `down`.

          - `subscriptions.data.items.data.price.type` (enum)
            One of `one_time` or `recurring` depending on whether the price is for a one-time purchase or a recurring (subscription) purchase.

          - `subscriptions.data.items.data.price.unit_amount` (nullable integer)
            The unit amount in  to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

          - `subscriptions.data.items.data.price.unit_amount_decimal` (nullable decimal string)
            The unit amount in  to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

        - `subscriptions.data.items.data.quantity` (nullable integer)
          The [quantity](https://docs.stripe.com/docs/subscriptions/quantities.md) of the plan to which the customer should be subscribed.

        - `subscriptions.data.items.data.subscription` (string)
          The `subscription` this `subscription_item` belongs to.

        - `subscriptions.data.items.data.tax_rates` (nullable array of objects)
          The tax rates which apply to this `subscription_item`. When set, the `default_tax_rates` on the subscription do not apply to this `subscription_item`.

          - `subscriptions.data.items.data.tax_rates.id` (string)
            Unique identifier for the object.

          - `subscriptions.data.items.data.tax_rates.object` (string)
            String representing the object’s type. Objects of the same type share the same value.

          - `subscriptions.data.items.data.tax_rates.active` (boolean)
            Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

          - `subscriptions.data.items.data.tax_rates.country` (nullable string)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `subscriptions.data.items.data.tax_rates.created` (timestamp)
            Time at which the object was created. Measured in seconds since the Unix epoch.

          - `subscriptions.data.items.data.tax_rates.description` (nullable string)
            An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

          - `subscriptions.data.items.data.tax_rates.display_name` (string)
            The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

          - `subscriptions.data.items.data.tax_rates.effective_percentage` (nullable float)
            Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true,
            this percentage reflects the rate actually used to calculate tax based on the product’s taxability
            and whether the user is registered to collect taxes in the corresponding jurisdiction.

          - `subscriptions.data.items.data.tax_rates.flat_amount` (nullable object)
            The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

            - `subscriptions.data.items.data.tax_rates.flat_amount.amount` (integer)
              Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

            - `subscriptions.data.items.data.tax_rates.flat_amount.currency` (string)
              Three-letter ISO currency code, in lowercase.

          - `subscriptions.data.items.data.tax_rates.inclusive` (boolean)
            This specifies if the tax rate is inclusive or exclusive.

          - `subscriptions.data.items.data.tax_rates.jurisdiction` (nullable string)
            The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

          - `subscriptions.data.items.data.tax_rates.jurisdiction_level` (nullable enum)
            The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.

          - `subscriptions.data.items.data.tax_rates.livemode` (boolean)
            Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

          - `subscriptions.data.items.data.tax_rates.metadata` (nullable object)
            Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

          - `subscriptions.data.items.data.tax_rates.percentage` (float)
            Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

          - `subscriptions.data.items.data.tax_rates.rate_type` (nullable enum)
            Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.

            A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

            A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

          - `subscriptions.data.items.data.tax_rates.state` (nullable string)
            [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

          - `subscriptions.data.items.data.tax_rates.tax_type` (nullable enum)
            The high-level tax type, such as `vat` or `sales_tax`.

            Amusement Tax

            Communications Tax

            Goods and Services Tax

            Harmonized Sales Tax

            Integrated Goods and Services Tax

            Japanese Consumption Tax

            Chicago Lease Tax

            Provincial Sales Tax

            Quebec Sales Tax

            Retail Delivery Fee

            Retail Sales Tax

            Sales Tax

            Service Tax

            Value-Added Tax

      - `subscriptions.data.items.has_more` (boolean)
        True if this list has another page of items after this one that can be fetched.

      - `subscriptions.data.items.url` (string)
        The URL where this list can be accessed.

    - `subscriptions.data.latest_invoice` (nullable string)
      The most recent invoice this subscription has generated.

    - `subscriptions.data.livemode` (boolean)
      Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

    - `subscriptions.data.metadata` (object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `subscriptions.data.next_pending_invoice_item_invoice` (nullable timestamp)
      Specifies the approximate timestamp on which any pending invoice items will be billed according to the schedule provided at `pending_invoice_item_interval`.

    - `subscriptions.data.on_behalf_of` (nullable string)
      The account (if any) the charge was made on behalf of for charges associated with this subscription. See the [Connect documentation](https://docs.stripe.com/docs/connect/subscriptions.md#on-behalf-of) for details.

    - `subscriptions.data.pause_collection` (nullable object)
      If specified, payment collection for this subscription will be paused. Note that the subscription status will be unchanged and will not be updated to `paused`. Learn more about [pausing collection](https://docs.stripe.com/docs/billing/subscriptions/pause-payment.md).

      - `subscriptions.data.pause_collection.behavior` (enum)
        The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.

      - `subscriptions.data.pause_collection.resumes_at` (nullable timestamp)
        The time after which the subscription will resume collecting payments.

    - `subscriptions.data.payment_settings` (nullable object)
      Payment settings passed on to invoices created by the subscription.

      - `subscriptions.data.payment_settings.payment_method_options` (nullable object)
        Payment-method-specific configuration to provide to invoices created by the subscription.

        - `subscriptions.data.payment_settings.payment_method_options.acss_debit` (nullable object)
          This sub-hash contains details about the Canadian pre-authorized debit payment method options to pass to invoices created by the subscription.

          - `subscriptions.data.payment_settings.payment_method_options.acss_debit.mandate_options` (nullable object)
            Additional fields for Mandate creation

            - `subscriptions.data.payment_settings.payment_method_options.acss_debit.mandate_options.transaction_type` (nullable enum)
              Transaction type of the mandate.

              Transactions are made for business reasons

              Transactions are made for personal reasons

          - `subscriptions.data.payment_settings.payment_method_options.acss_debit.verification_method` (nullable enum)
            Bank account verification method.

            Instant verification with fallback to microdeposits.

            Instant verification.

            Verification using microdeposits.

        - `subscriptions.data.payment_settings.payment_method_options.bancontact` (nullable object)
          This sub-hash contains details about the Bancontact payment method options to pass to invoices created by the subscription.

          - `subscriptions.data.payment_settings.payment_method_options.bancontact.preferred_language` (enum)
            Preferred language of the Bancontact authorization page that the customer is redirected to.

            German

            English

            French

            Dutch

        - `subscriptions.data.payment_settings.payment_method_options.card` (nullable object)
          This sub-hash contains details about the Card payment method options to pass to invoices created by the subscription.

          - `subscriptions.data.payment_settings.payment_method_options.card.mandate_options` (nullable object)
            Configuration options for setting up an eMandate for cards issued in India.

            - `subscriptions.data.payment_settings.payment_method_options.card.mandate_options.amount` (nullable integer)
              Amount to be charged for future payments.

            - `subscriptions.data.payment_settings.payment_method_options.card.mandate_options.amount_type` (nullable enum)
              One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param.

              If `fixed`, the `amount` param refers to the exact amount to be charged in future payments.

              If `maximum`, the amount charged can be up to the value passed for the `amount` param.

            - `subscriptions.data.payment_settings.payment_method_options.card.mandate_options.description` (nullable string)
              A description of the mandate or subscription that is meant to be displayed to the customer.

          - `subscriptions.data.payment_settings.payment_method_options.card.network` (nullable enum)
            Selected network to process this Subscription on. Depends on the available networks of the card attached to the Subscription. Can be only set confirm-time.

          - `subscriptions.data.payment_settings.payment_method_options.card.request_three_d_secure` (nullable enum)
            We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://docs.stripe.com/docs/strong-customer-authentication.md). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Read our guide on [manually requesting 3D Secure](https://docs.stripe.com/docs/payments/3d-secure/authentication-flow.md#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.

            Use `any` to manually request 3DS with a preference for a `frictionless` flow, increasing the likelihood of the authentication being completed without any additional input from the customer.
            3DS will always be attempted if it is supported for the card, but Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow.
            To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

            (Default) Our SCA Engine automatically prompts your customers for authentication based on risk level and other requirements.

            Use `challenge` to request 3DS with a preference for a `challenge` flow, where the customer must respond to a prompt for active authentication. Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow. To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

        - `subscriptions.data.payment_settings.payment_method_options.customer_balance` (nullable object)
          This sub-hash contains details about the Bank transfer payment method options to pass to invoices created by the subscription.

          - `subscriptions.data.payment_settings.payment_method_options.customer_balance.bank_transfer` (nullable object)
            Configuration for the bank transfer funding type, if the `funding_type` is set to `bank_transfer`.

            - `subscriptions.data.payment_settings.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer` (nullable object)
              Configuration for eu_bank_transfer funding type.

              - `subscriptions.data.payment_settings.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer.country` (enum)
                The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.

            - `subscriptions.data.payment_settings.payment_method_options.customer_balance.bank_transfer.type` (nullable enum)
              The bank transfer type that can be used for funding. Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.

          - `subscriptions.data.payment_settings.payment_method_options.customer_balance.funding_type` (nullable enum)
            The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`.

        - `subscriptions.data.payment_settings.payment_method_options.konbini` (nullable object)
          This sub-hash contains details about the Konbini payment method options to pass to invoices created by the subscription.

        - `subscriptions.data.payment_settings.payment_method_options.sepa_debit` (nullable object)
          This sub-hash contains details about the SEPA Direct Debit payment method options to pass to invoices created by the subscription.

        - `subscriptions.data.payment_settings.payment_method_options.us_bank_account` (nullable object)
          This sub-hash contains details about the ACH direct debit payment method options to pass to invoices created by the subscription.

          - `subscriptions.data.payment_settings.payment_method_options.us_bank_account.financial_connections` (nullable object)
            Additional fields for Financial Connections Session creation

            - `subscriptions.data.payment_settings.payment_method_options.us_bank_account.financial_connections.filters` (nullable object)
              Filter the list of accounts that are allowed to be linked.

              - `subscriptions.data.payment_settings.payment_method_options.us_bank_account.financial_connections.filters.account_subcategories` (nullable array of enums)
                The account subcategories to use to filter for possible accounts to link. Valid subcategories are `checking` and `savings`.

                Bank account subcategory is checking

                Bank account subcategory is savings

            - `subscriptions.data.payment_settings.payment_method_options.us_bank_account.financial_connections.permissions` (nullable array of enums)
              The list of permissions to request. The `payment_method` permission must be included.

              Allows accessing balance data from the account.

              Allows accessing ownership data from the account.

              Allows the creation of a payment method from the account.

              Allows accessing transactions data from the account.

            - `subscriptions.data.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch` (nullable array of enums)
              Data features requested to be retrieved upon account creation.

              Requests to prefetch balance data on accounts collected in this session.

              Requests to prefetch ownership data on accounts collected in this session.

              Requests to prefetch transaction data on accounts collected in this session.

          - `subscriptions.data.payment_settings.payment_method_options.us_bank_account.verification_method` (nullable enum)
            Bank account verification method.

            Instant verification with fallback to microdeposits.

            Instant verification only.

            Verification using microdeposits. Cannot be used with Stripe Checkout, Hosted Invoices, or Payment Element.

      - `subscriptions.data.payment_settings.payment_method_types` (nullable array of enums)
        The list of payment method types to provide to every invoice created by the subscription. If not set, Stripe attempts to automatically determine the types to use by looking at the invoice’s default payment method, the subscription’s default payment method, the customer’s default payment method, and your [invoice template settings](https://dashboard.stripe.com/settings/billing/invoice).

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

      - `subscriptions.data.payment_settings.save_default_payment_method` (nullable enum)
        Configure whether Stripe updates `subscription.default_payment_method` when payment succeeds. Defaults to `off`.

        Stripe never sets `subscription.default_payment_method`.

        Stripe sets `subscription.default_payment_method` when a subscription payment succeeds.

    - `subscriptions.data.pending_invoice_item_interval` (nullable object)
      Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://docs.stripe.com/docs/api.md#create_invoice) for the given subscription at the specified interval.

      - `subscriptions.data.pending_invoice_item_interval.interval` (enum)
        Specifies invoicing frequency. Either `day`, `week`, `month` or `year`.

      - `subscriptions.data.pending_invoice_item_interval.interval_count` (integer)
        The number of intervals between invoices. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks).

    - `subscriptions.data.pending_setup_intent` (nullable string)
      You can use this [SetupIntent](https://docs.stripe.com/docs/api/setup_intents.md) to collect user authentication when creating a subscription without immediate payment or updating a subscription’s payment method, allowing you to optimize for off-session payments. Learn more in the [SCA Migration Guide](https://docs.stripe.com/docs/billing/migration/strong-customer-authentication.md#scenario-2).

    - `subscriptions.data.pending_update` (nullable object)
      If specified, [pending updates](https://docs.stripe.com/docs/billing/subscriptions/pending-updates.md) that will be applied to the subscription once the `latest_invoice` has been paid.

      - `subscriptions.data.pending_update.billing_cycle_anchor` (nullable timestamp)
        If the update is applied, determines the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices. The timestamp is in UTC format.

      - `subscriptions.data.pending_update.expires_at` (timestamp)
        The point after which the changes reflected by this update will be discarded and no longer applied.

      - `subscriptions.data.pending_update.subscription_items` (nullable array of objects)
        List of subscription items, each with an attached plan, that will be set if the update is applied.

        - `subscriptions.data.pending_update.subscription_items.id` (string)
          Unique identifier for the object.

        - `subscriptions.data.pending_update.subscription_items.object` (string)
          String representing the object’s type. Objects of the same type share the same value.

        - `subscriptions.data.pending_update.subscription_items.billing_thresholds` (nullable object)
          Define thresholds at which an invoice will be sent, and the related subscription advanced to a new billing period

          - `subscriptions.data.pending_update.subscription_items.billing_thresholds.usage_gte` (nullable integer)
            Usage threshold that triggers the subscription to create an invoice

        - `subscriptions.data.pending_update.subscription_items.created` (integer)
          Time at which the object was created. Measured in seconds since the Unix epoch.

        - `subscriptions.data.pending_update.subscription_items.current_period_end` (timestamp)
          The end time of this subscription item’s current billing period.

        - `subscriptions.data.pending_update.subscription_items.current_period_start` (timestamp)
          The start time of this subscription item’s current billing period.

        - `subscriptions.data.pending_update.subscription_items.discounts` (array of strings)
          The discounts applied to the subscription item. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount.

        - `subscriptions.data.pending_update.subscription_items.metadata` (object)
          Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

        - `subscriptions.data.pending_update.subscription_items.price` (object)
          The price the customer is subscribed to.

          - `subscriptions.data.pending_update.subscription_items.price.id` (string)
            Unique identifier for the object.

          - `subscriptions.data.pending_update.subscription_items.price.object` (string)
            String representing the object’s type. Objects of the same type share the same value.

          - `subscriptions.data.pending_update.subscription_items.price.active` (boolean)
            Whether the price can be used for new purchases.

          - `subscriptions.data.pending_update.subscription_items.price.billing_scheme` (enum)
            Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.

          - `subscriptions.data.pending_update.subscription_items.price.created` (timestamp)
            Time at which the object was created. Measured in seconds since the Unix epoch.

          - `subscriptions.data.pending_update.subscription_items.price.currency` (enum)
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

          - `subscriptions.data.pending_update.subscription_items.price.currency_options` (nullable object)
            Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

            - `subscriptions.data.pending_update.subscription_items.price.currency_options.<currency>.custom_unit_amount` (nullable object)
              When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

              - `subscriptions.data.pending_update.subscription_items.price.currency_options.<currency>.custom_unit_amount.maximum` (nullable integer)
                The maximum unit amount the customer can specify for this item.

              - `subscriptions.data.pending_update.subscription_items.price.currency_options.<currency>.custom_unit_amount.minimum` (nullable integer)
                The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

              - `subscriptions.data.pending_update.subscription_items.price.currency_options.<currency>.custom_unit_amount.preset` (nullable integer)
                The starting unit amount which can be updated by the customer.

            - `subscriptions.data.pending_update.subscription_items.price.currency_options.<currency>.tax_behavior` (nullable enum)
              Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.

            - `subscriptions.data.pending_update.subscription_items.price.currency_options.<currency>.tiers` (nullable array of objects)
              Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

              - `subscriptions.data.pending_update.subscription_items.price.currency_options.<currency>.tiers.flat_amount` (nullable integer)
                Price for the entire tier.

              - `subscriptions.data.pending_update.subscription_items.price.currency_options.<currency>.tiers.flat_amount_decimal` (nullable decimal string)
                Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

              - `subscriptions.data.pending_update.subscription_items.price.currency_options.<currency>.tiers.unit_amount` (nullable integer)
                Per unit price for units relevant to the tier.

              - `subscriptions.data.pending_update.subscription_items.price.currency_options.<currency>.tiers.unit_amount_decimal` (nullable decimal string)
                Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

              - `subscriptions.data.pending_update.subscription_items.price.currency_options.<currency>.tiers.up_to` (nullable integer)
                Up to and including to this quantity will be contained in the tier.

            - `subscriptions.data.pending_update.subscription_items.price.currency_options.<currency>.unit_amount` (nullable integer)
              The unit amount in  to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

            - `subscriptions.data.pending_update.subscription_items.price.currency_options.<currency>.unit_amount_decimal` (nullable decimal string)
              The unit amount in  to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

          - `subscriptions.data.pending_update.subscription_items.price.custom_unit_amount` (nullable object)
            When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

            - `subscriptions.data.pending_update.subscription_items.price.custom_unit_amount.maximum` (nullable integer)
              The maximum unit amount the customer can specify for this item.

            - `subscriptions.data.pending_update.subscription_items.price.custom_unit_amount.minimum` (nullable integer)
              The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

            - `subscriptions.data.pending_update.subscription_items.price.custom_unit_amount.preset` (nullable integer)
              The starting unit amount which can be updated by the customer.

          - `subscriptions.data.pending_update.subscription_items.price.livemode` (boolean)
            Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

          - `subscriptions.data.pending_update.subscription_items.price.lookup_key` (nullable string)
            A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters.

          - `subscriptions.data.pending_update.subscription_items.price.metadata` (object)
            Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

          - `subscriptions.data.pending_update.subscription_items.price.nickname` (nullable string)
            A brief description of the price, hidden from customers.

          - `subscriptions.data.pending_update.subscription_items.price.product` (string)
            The ID of the product this price is associated with.

          - `subscriptions.data.pending_update.subscription_items.price.recurring` (nullable object)
            The recurring components of a price such as `interval` and `usage_type`.

            - `subscriptions.data.pending_update.subscription_items.price.recurring.interval` (enum)
              The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`.

            - `subscriptions.data.pending_update.subscription_items.price.recurring.interval_count` (integer)
              The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months.

            - `subscriptions.data.pending_update.subscription_items.price.recurring.meter` (nullable string)
              The meter tracking the usage of a metered price

            - `subscriptions.data.pending_update.subscription_items.price.recurring.usage_type` (enum)
              Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`.

          - `subscriptions.data.pending_update.subscription_items.price.tax_behavior` (nullable enum)
            Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.

          - `subscriptions.data.pending_update.subscription_items.price.tiers` (nullable array of objects)
            Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

            - `subscriptions.data.pending_update.subscription_items.price.tiers.flat_amount` (nullable integer)
              Price for the entire tier.

            - `subscriptions.data.pending_update.subscription_items.price.tiers.flat_amount_decimal` (nullable decimal string)
              Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

            - `subscriptions.data.pending_update.subscription_items.price.tiers.unit_amount` (nullable integer)
              Per unit price for units relevant to the tier.

            - `subscriptions.data.pending_update.subscription_items.price.tiers.unit_amount_decimal` (nullable decimal string)
              Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

            - `subscriptions.data.pending_update.subscription_items.price.tiers.up_to` (nullable integer)
              Up to and including to this quantity will be contained in the tier.

          - `subscriptions.data.pending_update.subscription_items.price.tiers_mode` (nullable enum)
            Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price. In `graduated` tiering, pricing can change as the quantity grows.

          - `subscriptions.data.pending_update.subscription_items.price.transform_quantity` (nullable object)
            Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`.

            - `subscriptions.data.pending_update.subscription_items.price.transform_quantity.divide_by` (integer)
              Divide usage by this number.

            - `subscriptions.data.pending_update.subscription_items.price.transform_quantity.round` (enum)
              After division, either round the result `up` or `down`.

          - `subscriptions.data.pending_update.subscription_items.price.type` (enum)
            One of `one_time` or `recurring` depending on whether the price is for a one-time purchase or a recurring (subscription) purchase.

          - `subscriptions.data.pending_update.subscription_items.price.unit_amount` (nullable integer)
            The unit amount in  to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

          - `subscriptions.data.pending_update.subscription_items.price.unit_amount_decimal` (nullable decimal string)
            The unit amount in  to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

        - `subscriptions.data.pending_update.subscription_items.quantity` (nullable integer)
          The [quantity](https://docs.stripe.com/docs/subscriptions/quantities.md) of the plan to which the customer should be subscribed.

        - `subscriptions.data.pending_update.subscription_items.subscription` (string)
          The `subscription` this `subscription_item` belongs to.

        - `subscriptions.data.pending_update.subscription_items.tax_rates` (nullable array of objects)
          The tax rates which apply to this `subscription_item`. When set, the `default_tax_rates` on the subscription do not apply to this `subscription_item`.

          - `subscriptions.data.pending_update.subscription_items.tax_rates.id` (string)
            Unique identifier for the object.

          - `subscriptions.data.pending_update.subscription_items.tax_rates.object` (string)
            String representing the object’s type. Objects of the same type share the same value.

          - `subscriptions.data.pending_update.subscription_items.tax_rates.active` (boolean)
            Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

          - `subscriptions.data.pending_update.subscription_items.tax_rates.country` (nullable string)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `subscriptions.data.pending_update.subscription_items.tax_rates.created` (timestamp)
            Time at which the object was created. Measured in seconds since the Unix epoch.

          - `subscriptions.data.pending_update.subscription_items.tax_rates.description` (nullable string)
            An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

          - `subscriptions.data.pending_update.subscription_items.tax_rates.display_name` (string)
            The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

          - `subscriptions.data.pending_update.subscription_items.tax_rates.effective_percentage` (nullable float)
            Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true,
            this percentage reflects the rate actually used to calculate tax based on the product’s taxability
            and whether the user is registered to collect taxes in the corresponding jurisdiction.

          - `subscriptions.data.pending_update.subscription_items.tax_rates.flat_amount` (nullable object)
            The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

            - `subscriptions.data.pending_update.subscription_items.tax_rates.flat_amount.amount` (integer)
              Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

            - `subscriptions.data.pending_update.subscription_items.tax_rates.flat_amount.currency` (string)
              Three-letter ISO currency code, in lowercase.

          - `subscriptions.data.pending_update.subscription_items.tax_rates.inclusive` (boolean)
            This specifies if the tax rate is inclusive or exclusive.

          - `subscriptions.data.pending_update.subscription_items.tax_rates.jurisdiction` (nullable string)
            The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

          - `subscriptions.data.pending_update.subscription_items.tax_rates.jurisdiction_level` (nullable enum)
            The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.

          - `subscriptions.data.pending_update.subscription_items.tax_rates.livemode` (boolean)
            Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

          - `subscriptions.data.pending_update.subscription_items.tax_rates.metadata` (nullable object)
            Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

          - `subscriptions.data.pending_update.subscription_items.tax_rates.percentage` (float)
            Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

          - `subscriptions.data.pending_update.subscription_items.tax_rates.rate_type` (nullable enum)
            Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.

            A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

            A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

          - `subscriptions.data.pending_update.subscription_items.tax_rates.state` (nullable string)
            [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

          - `subscriptions.data.pending_update.subscription_items.tax_rates.tax_type` (nullable enum)
            The high-level tax type, such as `vat` or `sales_tax`.

            Amusement Tax

            Communications Tax

            Goods and Services Tax

            Harmonized Sales Tax

            Integrated Goods and Services Tax

            Japanese Consumption Tax

            Chicago Lease Tax

            Provincial Sales Tax

            Quebec Sales Tax

            Retail Delivery Fee

            Retail Sales Tax

            Sales Tax

            Service Tax

            Value-Added Tax

      - `subscriptions.data.pending_update.trial_end` (nullable timestamp)
        Unix timestamp representing the end of the trial period the customer will get before being charged for the first time, if the update is applied.

      - `subscriptions.data.pending_update.trial_from_plan` (nullable boolean)
        Indicates if a plan’s `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://docs.stripe.com/docs/billing/subscriptions/trials.md) to learn more.

    - `subscriptions.data.schedule` (nullable string)
      The schedule attached to the subscription

    - `subscriptions.data.start_date` (timestamp)
      Date when the subscription was first created. The date might differ from the `created` date due to backdating.

    - `subscriptions.data.status` (enum)
      Possible values are `incomplete`, `incomplete_expired`, `trialing`, `active`, `past_due`, `canceled`, `unpaid`, or `paused`.

      For `collection_method=charge_automatically` a subscription moves into `incomplete` if the initial payment attempt fails. A subscription in this status can only have metadata and default_source updated. Once the first invoice is paid, the subscription moves into an `active` status. If the first invoice is not paid within 23 hours, the subscription transitions to `incomplete_expired`. This is a terminal status, the open invoice will be voided and no further invoices will be generated.

      A subscription that is currently in a trial period is `trialing` and moves to `active` when the trial period is over.

      A subscription can only enter a `paused` status [when a trial ends without a payment method](https://docs.stripe.com/docs/billing/subscriptions/trials.md#create-free-trials-without-payment). A `paused` subscription doesn’t generate invoices and can be resumed after your customer adds their payment method. The `paused` status is different from [pausing collection](https://docs.stripe.com/docs/billing/subscriptions/pause-payment.md), which still generates invoices and leaves the subscription’s status unchanged.

      If subscription `collection_method=charge_automatically`, it becomes `past_due` when payment is required but cannot be paid (due to failed payment or awaiting additional user actions). Once Stripe has exhausted all payment retry attempts, the subscription will become `canceled` or `unpaid` (depending on your subscriptions settings).

      If subscription `collection_method=send_invoice` it becomes `past_due` when its invoice is not paid by the due date, and `canceled` or `unpaid` if it is still not paid by an additional deadline after that. Note that when a subscription has a status of `unpaid`, no subsequent invoices will be attempted (invoices will be created, but then immediately automatically closed). After receiving updated payment information from a customer, you may choose to reopen and pay their closed invoices.

    - `subscriptions.data.test_clock` (nullable string)
      ID of the test clock this subscription belongs to.

    - `subscriptions.data.transfer_data` (nullable object)
      The account (if any) the subscription’s payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the subscription’s invoices.

      - `subscriptions.data.transfer_data.amount_percent` (nullable float)
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.

      - `subscriptions.data.transfer_data.destination` (string)
        The account where funds from the payment will be transferred to upon payment success.

    - `subscriptions.data.trial_end` (nullable timestamp)
      If the subscription has a trial, the end of that trial.

    - `subscriptions.data.trial_settings` (nullable object)
      Settings related to subscription trials.

      - `subscriptions.data.trial_settings.end_behavior` (object)
        Defines how the subscription should behave when the user’s free trial ends.

        - `subscriptions.data.trial_settings.end_behavior.missing_payment_method` (enum)
          Indicates how the subscription should change when the trial ends if the user did not provide a payment method.

          Cancel the subscription if a payment method is not attached when the trial ends.

          Create an invoice when the trial ends, even if the user did not set up a payment method.

          Pause the subscription if a payment method is not attached when the trial ends.

    - `subscriptions.data.trial_start` (nullable timestamp)
      If the subscription has a trial, the beginning of that trial.

  - `subscriptions.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `subscriptions.url` (string)
    The URL where this list can be accessed.

- `tax` (object)
  Tax details for the customer.

  - `tax.automatic_tax` (enum)
    Surfaces if automatic tax computation is possible given the current customer location information.

    There was an error determining the customer’s location. This is usually caused by a temporary issue. Retrieve the customer to try again.

    The customer is located in a country or state where you’re [not registered to collect tax](https://stripe.com/docs/tax/zero-tax#not-registered).
    Also returned when automatic tax calculation is not supported in the customer’s location.

    The customer is located in a country or state where you’re collecting tax.

    The customer’s location couldn’t be determined.
    Make sure the provided address information is valid and [supported in the customer’s country](https://stripe.com/docs/tax/customer-locations#supported-formats).

  - `tax.ip_address` (nullable string)
    A recent IP address of the customer used for tax reporting and tax location inference.

  - `tax.location` (nullable object)
    The identified tax location of the customer.

    - `tax.location.country` (string)
      The identified tax country of the customer.

    - `tax.location.source` (enum)
      The data source used to infer the customer’s location.

    - `tax.location.state` (nullable string)
      The identified tax state, county, province, or region of the customer.

- `tax_exempt` (nullable enum)
  Describes the customer’s tax exemption status, which is `none`, `exempt`, or `reverse`. When set to `reverse`, invoice and receipt PDFs include the following text: **“Reverse charge”**.

- `tax_ids` (nullable object)
  The customer’s tax IDs.

  - `tax_ids.object` (string)
    String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

  - `tax_ids.data` (array of objects)
    Details about each object.

    - `tax_ids.data.id` (string)
      Unique identifier for the object.

    - `tax_ids.data.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `tax_ids.data.country` (nullable string)
      Two-letter ISO code representing the country of the tax ID.

    - `tax_ids.data.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `tax_ids.data.customer` (nullable string)
      ID of the customer.

    - `tax_ids.data.livemode` (boolean)
      Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

    - `tax_ids.data.owner` (nullable object)
      The account or customer the tax ID belongs to.

      - `tax_ids.data.owner.account` (nullable string)
        The account being referenced when `type` is `account`.

      - `tax_ids.data.owner.application` (nullable string)
        The Connect Application being referenced when `type` is `application`.

      - `tax_ids.data.owner.customer` (nullable string)
        The customer being referenced when `type` is `customer`.

      - `tax_ids.data.owner.type` (enum)
        Type of owner referenced.

        Indicates an account is being referenced.

        Indicates an application is being referenced.

        Indicates a customer is being referenced.

        Indicates that the account being referenced is the account making the API request.

    - `tax_ids.data.type` (enum)
      Type of the tax ID, one of `ad_nrt`, `ae_trn`, `al_tin`, `am_tin`, `ao_tin`, `ar_cuit`, `au_abn`, `au_arn`, `aw_tin`, `az_tin`, `ba_tin`, `bb_tin`, `bd_bin`, `bf_ifu`, `bg_uic`, `bh_vat`, `bj_ifu`, `bo_tin`, `br_cnpj`, `br_cpf`, `bs_tin`, `by_tin`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `cd_nif`, `ch_uid`, `ch_vat`, `cl_tin`, `cm_niu`, `cn_tin`, `co_nit`, `cr_tin`, `cv_nif`, `de_stn`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `et_tin`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `gn_nif`, `hk_br`, `hr_oib`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kg_tin`, `kh_tin`, `kr_brn`, `kz_bin`, `la_tin`, `li_uid`, `li_vat`, `ma_vat`, `md_vat`, `me_pib`, `mk_vat`, `mr_nif`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `ng_tin`, `no_vat`, `no_voec`, `np_pan`, `nz_gst`, `om_vat`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sn_ninea`, `sr_fin`, `sv_nit`, `th_vat`, `tj_tin`, `tr_tin`, `tw_vat`, `tz_vat`, `ua_vat`, `ug_tin`, `us_ein`, `uy_ruc`, `uz_tin`, `uz_vat`, `ve_rif`, `vn_tin`, `za_vat`, `zm_tin`, or `zw_tin`. Note that some legacy tax IDs have type `unknown`

    - `tax_ids.data.value` (string)
      Value of the tax ID.

    - `tax_ids.data.verification` (nullable object)
      Tax ID verification information.

      - `tax_ids.data.verification.status` (enum)
        Verification status, one of `pending`, `verified`, `unverified`, or `unavailable`.

      - `tax_ids.data.verification.verified_address` (nullable string)
        Verified address.

      - `tax_ids.data.verification.verified_name` (nullable string)
        Verified name.

  - `tax_ids.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `tax_ids.url` (string)
    The URL where this list can be accessed.

- `test_clock` (nullable string)
  ID of the test clock that this customer belongs to.

### The Customer object

```json
{
  "id": "cus_NffrFeUfNV2Hib",
  "object": "customer",
  "address": null,
  "balance": 0,
  "created": 1680893993,
  "currency": null,
  "default_source": null,
  "delinquent": false,
  "description": null,
  "email": "jennyrosen@example.com",
  "invoice_prefix": "0759376C",
  "invoice_settings": {
    "custom_fields": null,
    "default_payment_method": null,
    "footer": null,
    "rendering_options": null
  },
  "livemode": false,
  "metadata": {},
  "name": "Jenny Rosen",
  "next_invoice_sequence": 1,
  "phone": null,
  "preferred_locales": [],
  "shipping": null,
  "tax_exempt": "none",
  "test_clock": null
}
```