# The Subscription object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `application` (nullable string)
  ID of the Connect Application that created the subscription.

- `application_fee_percent` (nullable float)
  A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner’s Stripe account.

- `automatic_tax` (object)
  Automatic tax settings for this subscription.

  - `automatic_tax.disabled_reason` (nullable enum)
    If Stripe disabled automatic tax, this enum describes why.

    Stripe’s systems automatically turned off Tax for this subscription when finalizing one of its invoices with a missing or incomplete location for your customer.

  - `automatic_tax.enabled` (boolean)
    Whether Stripe automatically computes tax on this subscription.

  - `automatic_tax.liability` (nullable object)
    The account that’s liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.

    - `automatic_tax.liability.account` (nullable string)
      The connected account being referenced when `type` is `account`.

    - `automatic_tax.liability.type` (enum)
      Type of the account referenced.

      Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

      Indicates that the account being referenced is the account making the API request.

- `billing_cycle_anchor` (timestamp)
  The reference point that aligns future [billing cycle](https://docs.stripe.com/docs/subscriptions/billing-cycle.md) dates. It sets the day of week for `week` intervals, the day of month for `month` and `year` intervals, and the month of year for `year` intervals. The timestamp is in UTC format.

- `billing_cycle_anchor_config` (nullable object)
  The fixed values used to calculate the `billing_cycle_anchor`.

  - `billing_cycle_anchor_config.day_of_month` (integer)
    The day of the month of the billing_cycle_anchor.

  - `billing_cycle_anchor_config.hour` (nullable integer)
    The hour of the day of the billing_cycle_anchor.

  - `billing_cycle_anchor_config.minute` (nullable integer)
    The minute of the hour of the billing_cycle_anchor.

  - `billing_cycle_anchor_config.month` (nullable integer)
    The month to start full cycle billing periods.

  - `billing_cycle_anchor_config.second` (nullable integer)
    The second of the minute of the billing_cycle_anchor.

- `billing_mode` (object)
  Controls how prorations and invoices for subscriptions are calculated and orchestrated.

  - `billing_mode.type` (enum)
    Controls how prorations and invoices for subscriptions are calculated and orchestrated.

    Calculations for subscriptions and invoices are based on legacy defaults.

    Supports more flexible calculation and orchestration options for subscriptions and invoices.

  - `billing_mode.updated_at` (nullable timestamp)
    Details on when the current billing_mode was adopted.

- `billing_thresholds` (nullable object)
  Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period

  - `billing_thresholds.amount_gte` (nullable integer)
    Monetary threshold that triggers the subscription to create an invoice

  - `billing_thresholds.reset_billing_cycle_anchor` (nullable boolean)
    Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged. This value may not be `true` if the subscription contains items with plans that have `aggregate_usage=last_ever`.

- `cancel_at` (nullable timestamp)
  A date in the future at which the subscription will automatically get canceled

- `cancel_at_period_end` (boolean)
  Whether this subscription will (if `status=active`) or did (if `status=canceled`) cancel at the end of the current billing period.

- `canceled_at` (nullable timestamp)
  If the subscription has been canceled, the date of that cancellation. If the subscription was canceled with `cancel_at_period_end`, `canceled_at` will reflect the time of the most recent update request, not the end of the subscription period when the subscription is automatically moved to a canceled state.

- `cancellation_details` (nullable object)
  Details about why this subscription was cancelled

  - `cancellation_details.comment` (nullable string)
    Additional comments about why the user canceled the subscription, if the subscription was canceled explicitly by the user.

  - `cancellation_details.feedback` (nullable enum)
    The customer submitted reason for why they canceled, if the subscription was canceled explicitly by the user.

    Customer service was less than expected

    Quality was less than expected

    Some features are missing

    Other reason

    I’m switching to a different service

    Ease of use was less than expected

    It’s too expensive

    I don’t use the service enough

  - `cancellation_details.reason` (nullable enum)
    Why this subscription was canceled.

- `collection_method` (enum)
  Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `customer` (string)
  ID of the customer who owns the subscription.

- `default_payment_method` (nullable string)
  ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer’s [invoice_settings.default_payment_method](https://docs.stripe.com/docs/api/customers/object.md#customer_object-invoice_settings-default_payment_method) or [default_source](https://docs.stripe.com/docs/api/customers/object.md#customer_object-default_source).

- `default_source` (nullable string)
  ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer’s [invoice_settings.default_payment_method](https://docs.stripe.com/docs/api/customers/object.md#customer_object-invoice_settings-default_payment_method) or [default_source](https://docs.stripe.com/docs/api/customers/object.md#customer_object-default_source).

- `default_tax_rates` (nullable array of objects)
  The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription.

  - `default_tax_rates.id` (string)
    Unique identifier for the object.

  - `default_tax_rates.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `default_tax_rates.active` (boolean)
    Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

  - `default_tax_rates.country` (nullable string)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `default_tax_rates.created` (timestamp)
    Time at which the object was created. Measured in seconds since the Unix epoch.

  - `default_tax_rates.description` (nullable string)
    An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

  - `default_tax_rates.display_name` (string)
    The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

  - `default_tax_rates.effective_percentage` (nullable float)
    Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true,
    this percentage reflects the rate actually used to calculate tax based on the product’s taxability
    and whether the user is registered to collect taxes in the corresponding jurisdiction.

  - `default_tax_rates.flat_amount` (nullable object)
    The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

    - `default_tax_rates.flat_amount.amount` (integer)
      Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

    - `default_tax_rates.flat_amount.currency` (string)
      Three-letter ISO currency code, in lowercase.

  - `default_tax_rates.inclusive` (boolean)
    This specifies if the tax rate is inclusive or exclusive.

  - `default_tax_rates.jurisdiction` (nullable string)
    The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

  - `default_tax_rates.jurisdiction_level` (nullable enum)
    The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.

  - `default_tax_rates.livemode` (boolean)
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

  - `default_tax_rates.metadata` (nullable object)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

  - `default_tax_rates.percentage` (float)
    Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

  - `default_tax_rates.rate_type` (nullable enum)
    Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.

    A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

    A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

  - `default_tax_rates.state` (nullable string)
    [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

  - `default_tax_rates.tax_type` (nullable enum)
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

- `description` (nullable string)
  The subscription’s description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.

- `discounts` (array of strings)
  The discounts applied to the subscription. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount.

- `ended_at` (nullable timestamp)
  If the subscription has ended, the date the subscription ended.

- `invoice_settings` (object)
  All invoices will be billed using the specified settings.

  - `invoice_settings.account_tax_ids` (nullable array of strings)
    The account tax IDs associated with the subscription. Will be set on invoices generated by the subscription.

  - `invoice_settings.issuer` (object)
    The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.

    - `invoice_settings.issuer.account` (nullable string)
      The connected account being referenced when `type` is `account`.

    - `invoice_settings.issuer.type` (enum)
      Type of the account referenced.

      Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

      Indicates that the account being referenced is the account making the API request.

- `items` (object)
  List of subscription items, each with an attached price.

  - `items.object` (string)
    String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

  - `items.data` (array of objects)
    Details about each object.

    - `items.data.id` (string)
      Unique identifier for the object.

    - `items.data.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `items.data.billing_thresholds` (nullable object)
      Define thresholds at which an invoice will be sent, and the related subscription advanced to a new billing period

      - `items.data.billing_thresholds.usage_gte` (nullable integer)
        Usage threshold that triggers the subscription to create an invoice

    - `items.data.created` (integer)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `items.data.current_period_end` (timestamp)
      The end time of this subscription item’s current billing period.

    - `items.data.current_period_start` (timestamp)
      The start time of this subscription item’s current billing period.

    - `items.data.discounts` (array of strings)
      The discounts applied to the subscription item. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount.

    - `items.data.metadata` (object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `items.data.price` (object)
      The price the customer is subscribed to.

      - `items.data.price.id` (string)
        Unique identifier for the object.

      - `items.data.price.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `items.data.price.active` (boolean)
        Whether the price can be used for new purchases.

      - `items.data.price.billing_scheme` (enum)
        Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.

      - `items.data.price.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `items.data.price.currency` (enum)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `items.data.price.currency_options` (nullable object)
        Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

        - `items.data.price.currency_options.<currency>.custom_unit_amount` (nullable object)
          When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

          - `items.data.price.currency_options.<currency>.custom_unit_amount.maximum` (nullable integer)
            The maximum unit amount the customer can specify for this item.

          - `items.data.price.currency_options.<currency>.custom_unit_amount.minimum` (nullable integer)
            The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

          - `items.data.price.currency_options.<currency>.custom_unit_amount.preset` (nullable integer)
            The starting unit amount which can be updated by the customer.

        - `items.data.price.currency_options.<currency>.tax_behavior` (nullable enum)
          Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.

        - `items.data.price.currency_options.<currency>.tiers` (nullable array of objects)
          Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

          - `items.data.price.currency_options.<currency>.tiers.flat_amount` (nullable integer)
            Price for the entire tier.

          - `items.data.price.currency_options.<currency>.tiers.flat_amount_decimal` (nullable decimal string)
            Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

          - `items.data.price.currency_options.<currency>.tiers.unit_amount` (nullable integer)
            Per unit price for units relevant to the tier.

          - `items.data.price.currency_options.<currency>.tiers.unit_amount_decimal` (nullable decimal string)
            Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

          - `items.data.price.currency_options.<currency>.tiers.up_to` (nullable integer)
            Up to and including to this quantity will be contained in the tier.

        - `items.data.price.currency_options.<currency>.unit_amount` (nullable integer)
          The unit amount in  to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

        - `items.data.price.currency_options.<currency>.unit_amount_decimal` (nullable decimal string)
          The unit amount in  to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

      - `items.data.price.custom_unit_amount` (nullable object)
        When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

        - `items.data.price.custom_unit_amount.maximum` (nullable integer)
          The maximum unit amount the customer can specify for this item.

        - `items.data.price.custom_unit_amount.minimum` (nullable integer)
          The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

        - `items.data.price.custom_unit_amount.preset` (nullable integer)
          The starting unit amount which can be updated by the customer.

      - `items.data.price.livemode` (boolean)
        Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

      - `items.data.price.lookup_key` (nullable string)
        A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters.

      - `items.data.price.metadata` (object)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `items.data.price.nickname` (nullable string)
        A brief description of the price, hidden from customers.

      - `items.data.price.product` (string)
        The ID of the product this price is associated with.

      - `items.data.price.recurring` (nullable object)
        The recurring components of a price such as `interval` and `usage_type`.

        - `items.data.price.recurring.interval` (enum)
          The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`.

        - `items.data.price.recurring.interval_count` (integer)
          The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months.

        - `items.data.price.recurring.meter` (nullable string)
          The meter tracking the usage of a metered price

        - `items.data.price.recurring.usage_type` (enum)
          Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`.

      - `items.data.price.tax_behavior` (nullable enum)
        Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.

      - `items.data.price.tiers` (nullable array of objects)
        Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

        - `items.data.price.tiers.flat_amount` (nullable integer)
          Price for the entire tier.

        - `items.data.price.tiers.flat_amount_decimal` (nullable decimal string)
          Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

        - `items.data.price.tiers.unit_amount` (nullable integer)
          Per unit price for units relevant to the tier.

        - `items.data.price.tiers.unit_amount_decimal` (nullable decimal string)
          Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

        - `items.data.price.tiers.up_to` (nullable integer)
          Up to and including to this quantity will be contained in the tier.

      - `items.data.price.tiers_mode` (nullable enum)
        Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price. In `graduated` tiering, pricing can change as the quantity grows.

      - `items.data.price.transform_quantity` (nullable object)
        Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`.

        - `items.data.price.transform_quantity.divide_by` (integer)
          Divide usage by this number.

        - `items.data.price.transform_quantity.round` (enum)
          After division, either round the result `up` or `down`.

      - `items.data.price.type` (enum)
        One of `one_time` or `recurring` depending on whether the price is for a one-time purchase or a recurring (subscription) purchase.

      - `items.data.price.unit_amount` (nullable integer)
        The unit amount in  to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

      - `items.data.price.unit_amount_decimal` (nullable decimal string)
        The unit amount in  to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

    - `items.data.quantity` (nullable integer)
      The [quantity](https://docs.stripe.com/docs/subscriptions/quantities.md) of the plan to which the customer should be subscribed.

    - `items.data.subscription` (string)
      The `subscription` this `subscription_item` belongs to.

    - `items.data.tax_rates` (nullable array of objects)
      The tax rates which apply to this `subscription_item`. When set, the `default_tax_rates` on the subscription do not apply to this `subscription_item`.

      - `items.data.tax_rates.id` (string)
        Unique identifier for the object.

      - `items.data.tax_rates.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `items.data.tax_rates.active` (boolean)
        Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

      - `items.data.tax_rates.country` (nullable string)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `items.data.tax_rates.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `items.data.tax_rates.description` (nullable string)
        An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

      - `items.data.tax_rates.display_name` (string)
        The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

      - `items.data.tax_rates.effective_percentage` (nullable float)
        Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true,
        this percentage reflects the rate actually used to calculate tax based on the product’s taxability
        and whether the user is registered to collect taxes in the corresponding jurisdiction.

      - `items.data.tax_rates.flat_amount` (nullable object)
        The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

        - `items.data.tax_rates.flat_amount.amount` (integer)
          Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

        - `items.data.tax_rates.flat_amount.currency` (string)
          Three-letter ISO currency code, in lowercase.

      - `items.data.tax_rates.inclusive` (boolean)
        This specifies if the tax rate is inclusive or exclusive.

      - `items.data.tax_rates.jurisdiction` (nullable string)
        The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

      - `items.data.tax_rates.jurisdiction_level` (nullable enum)
        The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.

      - `items.data.tax_rates.livemode` (boolean)
        Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

      - `items.data.tax_rates.metadata` (nullable object)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `items.data.tax_rates.percentage` (float)
        Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

      - `items.data.tax_rates.rate_type` (nullable enum)
        Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.

        A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

        A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

      - `items.data.tax_rates.state` (nullable string)
        [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

      - `items.data.tax_rates.tax_type` (nullable enum)
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

  - `items.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `items.url` (string)
    The URL where this list can be accessed.

- `latest_invoice` (nullable string)
  The most recent invoice this subscription has generated.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `next_pending_invoice_item_invoice` (nullable timestamp)
  Specifies the approximate timestamp on which any pending invoice items will be billed according to the schedule provided at `pending_invoice_item_interval`.

- `on_behalf_of` (nullable string)
  The account (if any) the charge was made on behalf of for charges associated with this subscription. See the [Connect documentation](https://docs.stripe.com/docs/connect/subscriptions.md#on-behalf-of) for details.

- `pause_collection` (nullable object)
  If specified, payment collection for this subscription will be paused. Note that the subscription status will be unchanged and will not be updated to `paused`. Learn more about [pausing collection](https://docs.stripe.com/docs/billing/subscriptions/pause-payment.md).

  - `pause_collection.behavior` (enum)
    The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.

  - `pause_collection.resumes_at` (nullable timestamp)
    The time after which the subscription will resume collecting payments.

- `payment_settings` (nullable object)
  Payment settings passed on to invoices created by the subscription.

  - `payment_settings.payment_method_options` (nullable object)
    Payment-method-specific configuration to provide to invoices created by the subscription.

    - `payment_settings.payment_method_options.acss_debit` (nullable object)
      This sub-hash contains details about the Canadian pre-authorized debit payment method options to pass to invoices created by the subscription.

      - `payment_settings.payment_method_options.acss_debit.mandate_options` (nullable object)
        Additional fields for Mandate creation

        - `payment_settings.payment_method_options.acss_debit.mandate_options.transaction_type` (nullable enum)
          Transaction type of the mandate.

          Transactions are made for business reasons

          Transactions are made for personal reasons

      - `payment_settings.payment_method_options.acss_debit.verification_method` (nullable enum)
        Bank account verification method.

        Instant verification with fallback to microdeposits.

        Instant verification.

        Verification using microdeposits.

    - `payment_settings.payment_method_options.bancontact` (nullable object)
      This sub-hash contains details about the Bancontact payment method options to pass to invoices created by the subscription.

      - `payment_settings.payment_method_options.bancontact.preferred_language` (enum)
        Preferred language of the Bancontact authorization page that the customer is redirected to.

        German

        English

        French

        Dutch

    - `payment_settings.payment_method_options.card` (nullable object)
      This sub-hash contains details about the Card payment method options to pass to invoices created by the subscription.

      - `payment_settings.payment_method_options.card.mandate_options` (nullable object)
        Configuration options for setting up an eMandate for cards issued in India.

        - `payment_settings.payment_method_options.card.mandate_options.amount` (nullable integer)
          Amount to be charged for future payments.

        - `payment_settings.payment_method_options.card.mandate_options.amount_type` (nullable enum)
          One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param.

          If `fixed`, the `amount` param refers to the exact amount to be charged in future payments.

          If `maximum`, the amount charged can be up to the value passed for the `amount` param.

        - `payment_settings.payment_method_options.card.mandate_options.description` (nullable string)
          A description of the mandate or subscription that is meant to be displayed to the customer.

      - `payment_settings.payment_method_options.card.network` (nullable enum)
        Selected network to process this Subscription on. Depends on the available networks of the card attached to the Subscription. Can be only set confirm-time.

      - `payment_settings.payment_method_options.card.request_three_d_secure` (nullable enum)
        We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://docs.stripe.com/docs/strong-customer-authentication.md). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Read our guide on [manually requesting 3D Secure](https://docs.stripe.com/docs/payments/3d-secure/authentication-flow.md#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.

        Use `any` to manually request 3DS with a preference for a `frictionless` flow, increasing the likelihood of the authentication being completed without any additional input from the customer.
        3DS will always be attempted if it is supported for the card, but Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow.
        To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

        (Default) Our SCA Engine automatically prompts your customers for authentication based on risk level and other requirements.

        Use `challenge` to request 3DS with a preference for a `challenge` flow, where the customer must respond to a prompt for active authentication. Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow. To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

    - `payment_settings.payment_method_options.customer_balance` (nullable object)
      This sub-hash contains details about the Bank transfer payment method options to pass to invoices created by the subscription.

      - `payment_settings.payment_method_options.customer_balance.bank_transfer` (nullable object)
        Configuration for the bank transfer funding type, if the `funding_type` is set to `bank_transfer`.

        - `payment_settings.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer` (nullable object)
          Configuration for eu_bank_transfer funding type.

          - `payment_settings.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer.country` (enum)
            The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.

        - `payment_settings.payment_method_options.customer_balance.bank_transfer.type` (nullable enum)
          The bank transfer type that can be used for funding. Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.

      - `payment_settings.payment_method_options.customer_balance.funding_type` (nullable enum)
        The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`.

    - `payment_settings.payment_method_options.konbini` (nullable object)
      This sub-hash contains details about the Konbini payment method options to pass to invoices created by the subscription.

    - `payment_settings.payment_method_options.sepa_debit` (nullable object)
      This sub-hash contains details about the SEPA Direct Debit payment method options to pass to invoices created by the subscription.

    - `payment_settings.payment_method_options.us_bank_account` (nullable object)
      This sub-hash contains details about the ACH direct debit payment method options to pass to invoices created by the subscription.

      - `payment_settings.payment_method_options.us_bank_account.financial_connections` (nullable object)
        Additional fields for Financial Connections Session creation

        - `payment_settings.payment_method_options.us_bank_account.financial_connections.filters` (nullable object)
          Filter the list of accounts that are allowed to be linked.

          - `payment_settings.payment_method_options.us_bank_account.financial_connections.filters.account_subcategories` (nullable array of enums)
            The account subcategories to use to filter for possible accounts to link. Valid subcategories are `checking` and `savings`.

            Bank account subcategory is checking

            Bank account subcategory is savings

        - `payment_settings.payment_method_options.us_bank_account.financial_connections.permissions` (nullable array of enums)
          The list of permissions to request. The `payment_method` permission must be included.

          Allows accessing balance data from the account.

          Allows accessing ownership data from the account.

          Allows the creation of a payment method from the account.

          Allows accessing transactions data from the account.

        - `payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch` (nullable array of enums)
          Data features requested to be retrieved upon account creation.

          Requests to prefetch balance data on accounts collected in this session.

          Requests to prefetch ownership data on accounts collected in this session.

          Requests to prefetch transaction data on accounts collected in this session.

      - `payment_settings.payment_method_options.us_bank_account.verification_method` (nullable enum)
        Bank account verification method.

        Instant verification with fallback to microdeposits.

        Instant verification only.

        Verification using microdeposits. Cannot be used with Stripe Checkout, Hosted Invoices, or Payment Element.

  - `payment_settings.payment_method_types` (nullable array of enums)
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

  - `payment_settings.save_default_payment_method` (nullable enum)
    Configure whether Stripe updates `subscription.default_payment_method` when payment succeeds. Defaults to `off`.

    Stripe never sets `subscription.default_payment_method`.

    Stripe sets `subscription.default_payment_method` when a subscription payment succeeds.

- `pending_invoice_item_interval` (nullable object)
  Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://docs.stripe.com/docs/api.md#create_invoice) for the given subscription at the specified interval.

  - `pending_invoice_item_interval.interval` (enum)
    Specifies invoicing frequency. Either `day`, `week`, `month` or `year`.

  - `pending_invoice_item_interval.interval_count` (integer)
    The number of intervals between invoices. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks).

- `pending_setup_intent` (nullable string)
  You can use this [SetupIntent](https://docs.stripe.com/docs/api/setup_intents.md) to collect user authentication when creating a subscription without immediate payment or updating a subscription’s payment method, allowing you to optimize for off-session payments. Learn more in the [SCA Migration Guide](https://docs.stripe.com/docs/billing/migration/strong-customer-authentication.md#scenario-2).

- `pending_update` (nullable object)
  If specified, [pending updates](https://docs.stripe.com/docs/billing/subscriptions/pending-updates.md) that will be applied to the subscription once the `latest_invoice` has been paid.

  - `pending_update.billing_cycle_anchor` (nullable timestamp)
    If the update is applied, determines the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices. The timestamp is in UTC format.

  - `pending_update.expires_at` (timestamp)
    The point after which the changes reflected by this update will be discarded and no longer applied.

  - `pending_update.subscription_items` (nullable array of objects)
    List of subscription items, each with an attached plan, that will be set if the update is applied.

    - `pending_update.subscription_items.id` (string)
      Unique identifier for the object.

    - `pending_update.subscription_items.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `pending_update.subscription_items.billing_thresholds` (nullable object)
      Define thresholds at which an invoice will be sent, and the related subscription advanced to a new billing period

      - `pending_update.subscription_items.billing_thresholds.usage_gte` (nullable integer)
        Usage threshold that triggers the subscription to create an invoice

    - `pending_update.subscription_items.created` (integer)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `pending_update.subscription_items.current_period_end` (timestamp)
      The end time of this subscription item’s current billing period.

    - `pending_update.subscription_items.current_period_start` (timestamp)
      The start time of this subscription item’s current billing period.

    - `pending_update.subscription_items.discounts` (array of strings)
      The discounts applied to the subscription item. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount.

    - `pending_update.subscription_items.metadata` (object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `pending_update.subscription_items.price` (object)
      The price the customer is subscribed to.

      - `pending_update.subscription_items.price.id` (string)
        Unique identifier for the object.

      - `pending_update.subscription_items.price.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `pending_update.subscription_items.price.active` (boolean)
        Whether the price can be used for new purchases.

      - `pending_update.subscription_items.price.billing_scheme` (enum)
        Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.

      - `pending_update.subscription_items.price.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `pending_update.subscription_items.price.currency` (enum)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `pending_update.subscription_items.price.currency_options` (nullable object)
        Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

        - `pending_update.subscription_items.price.currency_options.<currency>.custom_unit_amount` (nullable object)
          When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

          - `pending_update.subscription_items.price.currency_options.<currency>.custom_unit_amount.maximum` (nullable integer)
            The maximum unit amount the customer can specify for this item.

          - `pending_update.subscription_items.price.currency_options.<currency>.custom_unit_amount.minimum` (nullable integer)
            The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

          - `pending_update.subscription_items.price.currency_options.<currency>.custom_unit_amount.preset` (nullable integer)
            The starting unit amount which can be updated by the customer.

        - `pending_update.subscription_items.price.currency_options.<currency>.tax_behavior` (nullable enum)
          Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.

        - `pending_update.subscription_items.price.currency_options.<currency>.tiers` (nullable array of objects)
          Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

          - `pending_update.subscription_items.price.currency_options.<currency>.tiers.flat_amount` (nullable integer)
            Price for the entire tier.

          - `pending_update.subscription_items.price.currency_options.<currency>.tiers.flat_amount_decimal` (nullable decimal string)
            Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

          - `pending_update.subscription_items.price.currency_options.<currency>.tiers.unit_amount` (nullable integer)
            Per unit price for units relevant to the tier.

          - `pending_update.subscription_items.price.currency_options.<currency>.tiers.unit_amount_decimal` (nullable decimal string)
            Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

          - `pending_update.subscription_items.price.currency_options.<currency>.tiers.up_to` (nullable integer)
            Up to and including to this quantity will be contained in the tier.

        - `pending_update.subscription_items.price.currency_options.<currency>.unit_amount` (nullable integer)
          The unit amount in  to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

        - `pending_update.subscription_items.price.currency_options.<currency>.unit_amount_decimal` (nullable decimal string)
          The unit amount in  to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

      - `pending_update.subscription_items.price.custom_unit_amount` (nullable object)
        When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

        - `pending_update.subscription_items.price.custom_unit_amount.maximum` (nullable integer)
          The maximum unit amount the customer can specify for this item.

        - `pending_update.subscription_items.price.custom_unit_amount.minimum` (nullable integer)
          The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

        - `pending_update.subscription_items.price.custom_unit_amount.preset` (nullable integer)
          The starting unit amount which can be updated by the customer.

      - `pending_update.subscription_items.price.livemode` (boolean)
        Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

      - `pending_update.subscription_items.price.lookup_key` (nullable string)
        A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters.

      - `pending_update.subscription_items.price.metadata` (object)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `pending_update.subscription_items.price.nickname` (nullable string)
        A brief description of the price, hidden from customers.

      - `pending_update.subscription_items.price.product` (string)
        The ID of the product this price is associated with.

      - `pending_update.subscription_items.price.recurring` (nullable object)
        The recurring components of a price such as `interval` and `usage_type`.

        - `pending_update.subscription_items.price.recurring.interval` (enum)
          The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`.

        - `pending_update.subscription_items.price.recurring.interval_count` (integer)
          The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months.

        - `pending_update.subscription_items.price.recurring.meter` (nullable string)
          The meter tracking the usage of a metered price

        - `pending_update.subscription_items.price.recurring.usage_type` (enum)
          Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`.

      - `pending_update.subscription_items.price.tax_behavior` (nullable enum)
        Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.

      - `pending_update.subscription_items.price.tiers` (nullable array of objects)
        Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

        - `pending_update.subscription_items.price.tiers.flat_amount` (nullable integer)
          Price for the entire tier.

        - `pending_update.subscription_items.price.tiers.flat_amount_decimal` (nullable decimal string)
          Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

        - `pending_update.subscription_items.price.tiers.unit_amount` (nullable integer)
          Per unit price for units relevant to the tier.

        - `pending_update.subscription_items.price.tiers.unit_amount_decimal` (nullable decimal string)
          Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

        - `pending_update.subscription_items.price.tiers.up_to` (nullable integer)
          Up to and including to this quantity will be contained in the tier.

      - `pending_update.subscription_items.price.tiers_mode` (nullable enum)
        Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price. In `graduated` tiering, pricing can change as the quantity grows.

      - `pending_update.subscription_items.price.transform_quantity` (nullable object)
        Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`.

        - `pending_update.subscription_items.price.transform_quantity.divide_by` (integer)
          Divide usage by this number.

        - `pending_update.subscription_items.price.transform_quantity.round` (enum)
          After division, either round the result `up` or `down`.

      - `pending_update.subscription_items.price.type` (enum)
        One of `one_time` or `recurring` depending on whether the price is for a one-time purchase or a recurring (subscription) purchase.

      - `pending_update.subscription_items.price.unit_amount` (nullable integer)
        The unit amount in  to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

      - `pending_update.subscription_items.price.unit_amount_decimal` (nullable decimal string)
        The unit amount in  to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

    - `pending_update.subscription_items.quantity` (nullable integer)
      The [quantity](https://docs.stripe.com/docs/subscriptions/quantities.md) of the plan to which the customer should be subscribed.

    - `pending_update.subscription_items.subscription` (string)
      The `subscription` this `subscription_item` belongs to.

    - `pending_update.subscription_items.tax_rates` (nullable array of objects)
      The tax rates which apply to this `subscription_item`. When set, the `default_tax_rates` on the subscription do not apply to this `subscription_item`.

      - `pending_update.subscription_items.tax_rates.id` (string)
        Unique identifier for the object.

      - `pending_update.subscription_items.tax_rates.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `pending_update.subscription_items.tax_rates.active` (boolean)
        Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

      - `pending_update.subscription_items.tax_rates.country` (nullable string)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `pending_update.subscription_items.tax_rates.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `pending_update.subscription_items.tax_rates.description` (nullable string)
        An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

      - `pending_update.subscription_items.tax_rates.display_name` (string)
        The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

      - `pending_update.subscription_items.tax_rates.effective_percentage` (nullable float)
        Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true,
        this percentage reflects the rate actually used to calculate tax based on the product’s taxability
        and whether the user is registered to collect taxes in the corresponding jurisdiction.

      - `pending_update.subscription_items.tax_rates.flat_amount` (nullable object)
        The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

        - `pending_update.subscription_items.tax_rates.flat_amount.amount` (integer)
          Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

        - `pending_update.subscription_items.tax_rates.flat_amount.currency` (string)
          Three-letter ISO currency code, in lowercase.

      - `pending_update.subscription_items.tax_rates.inclusive` (boolean)
        This specifies if the tax rate is inclusive or exclusive.

      - `pending_update.subscription_items.tax_rates.jurisdiction` (nullable string)
        The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

      - `pending_update.subscription_items.tax_rates.jurisdiction_level` (nullable enum)
        The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.

      - `pending_update.subscription_items.tax_rates.livemode` (boolean)
        Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

      - `pending_update.subscription_items.tax_rates.metadata` (nullable object)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `pending_update.subscription_items.tax_rates.percentage` (float)
        Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

      - `pending_update.subscription_items.tax_rates.rate_type` (nullable enum)
        Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.

        A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

        A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

      - `pending_update.subscription_items.tax_rates.state` (nullable string)
        [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

      - `pending_update.subscription_items.tax_rates.tax_type` (nullable enum)
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

  - `pending_update.trial_end` (nullable timestamp)
    Unix timestamp representing the end of the trial period the customer will get before being charged for the first time, if the update is applied.

  - `pending_update.trial_from_plan` (nullable boolean)
    Indicates if a plan’s `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://docs.stripe.com/docs/billing/subscriptions/trials.md) to learn more.

- `schedule` (nullable string)
  The schedule attached to the subscription

- `start_date` (timestamp)
  Date when the subscription was first created. The date might differ from the `created` date due to backdating.

- `status` (enum)
  Possible values are `incomplete`, `incomplete_expired`, `trialing`, `active`, `past_due`, `canceled`, `unpaid`, or `paused`.

  For `collection_method=charge_automatically` a subscription moves into `incomplete` if the initial payment attempt fails. A subscription in this status can only have metadata and default_source updated. Once the first invoice is paid, the subscription moves into an `active` status. If the first invoice is not paid within 23 hours, the subscription transitions to `incomplete_expired`. This is a terminal status, the open invoice will be voided and no further invoices will be generated.

  A subscription that is currently in a trial period is `trialing` and moves to `active` when the trial period is over.

  A subscription can only enter a `paused` status [when a trial ends without a payment method](https://docs.stripe.com/docs/billing/subscriptions/trials.md#create-free-trials-without-payment). A `paused` subscription doesn’t generate invoices and can be resumed after your customer adds their payment method. The `paused` status is different from [pausing collection](https://docs.stripe.com/docs/billing/subscriptions/pause-payment.md), which still generates invoices and leaves the subscription’s status unchanged.

  If subscription `collection_method=charge_automatically`, it becomes `past_due` when payment is required but cannot be paid (due to failed payment or awaiting additional user actions). Once Stripe has exhausted all payment retry attempts, the subscription will become `canceled` or `unpaid` (depending on your subscriptions settings).

  If subscription `collection_method=send_invoice` it becomes `past_due` when its invoice is not paid by the due date, and `canceled` or `unpaid` if it is still not paid by an additional deadline after that. Note that when a subscription has a status of `unpaid`, no subsequent invoices will be attempted (invoices will be created, but then immediately automatically closed). After receiving updated payment information from a customer, you may choose to reopen and pay their closed invoices.

- `test_clock` (nullable string)
  ID of the test clock this subscription belongs to.

- `transfer_data` (nullable object)
  The account (if any) the subscription’s payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the subscription’s invoices.

  - `transfer_data.amount_percent` (nullable float)
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.

  - `transfer_data.destination` (string)
    The account where funds from the payment will be transferred to upon payment success.

- `trial_end` (nullable timestamp)
  If the subscription has a trial, the end of that trial.

- `trial_settings` (nullable object)
  Settings related to subscription trials.

  - `trial_settings.end_behavior` (object)
    Defines how the subscription should behave when the user’s free trial ends.

    - `trial_settings.end_behavior.missing_payment_method` (enum)
      Indicates how the subscription should change when the trial ends if the user did not provide a payment method.

      Cancel the subscription if a payment method is not attached when the trial ends.

      Create an invoice when the trial ends, even if the user did not set up a payment method.

      Pause the subscription if a payment method is not attached when the trial ends.

- `trial_start` (nullable timestamp)
  If the subscription has a trial, the beginning of that trial.

### The Subscription object

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
  "metadata": {},
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