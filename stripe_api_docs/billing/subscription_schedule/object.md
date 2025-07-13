# The Subscription Schedule object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `application` (nullable string)
  ID of the Connect Application that created the schedule.

- `billing_mode` (object)
  The [billing mode](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-billing_mode) that will be used to process all future operations for the subscription schedule.

  - `billing_mode.type` (enum)
    Controls how prorations and invoices for subscriptions are calculated and orchestrated.

    Calculations for subscriptions and invoices are based on legacy defaults.

    Supports more flexible calculation and orchestration options for subscriptions and invoices.

  - `billing_mode.updated_at` (nullable timestamp)
    Details on when the current billing_mode was adopted.

- `canceled_at` (nullable timestamp)
  Time at which the subscription schedule was canceled. Measured in seconds since the Unix epoch.

- `completed_at` (nullable timestamp)
  Time at which the subscription schedule was completed. Measured in seconds since the Unix epoch.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `current_phase` (nullable object)
  Object representing the start and end dates for the current phase of the subscription schedule, if it is `active`.

  - `current_phase.end_date` (timestamp)
    The end of this phase of the subscription schedule.

  - `current_phase.start_date` (timestamp)
    The start of this phase of the subscription schedule.

- `customer` (string)
  ID of the customer who owns the subscription schedule.

- `default_settings` (object)
  Object representing the subscription schedule’s default settings.

  - `default_settings.application_fee_percent` (nullable float)
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner’s Stripe account during this phase of the schedule.

  - `default_settings.automatic_tax` (object)
    Default settings for automatic tax computation.

    - `default_settings.automatic_tax.disabled_reason` (nullable enum)
      If Stripe disabled automatic tax, this enum describes why.

      Stripe’s systems automatically turned off Tax for this subscription schedule when finalizing one of its invoices with a missing or incomplete location for your customer.

    - `default_settings.automatic_tax.enabled` (boolean)
      Whether Stripe automatically computes tax on invoices created during this phase.

    - `default_settings.automatic_tax.liability` (nullable object)
      The account that’s liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.

      - `default_settings.automatic_tax.liability.account` (nullable string)
        The connected account being referenced when `type` is `account`.

      - `default_settings.automatic_tax.liability.type` (enum)
        Type of the account referenced.

        Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

        Indicates that the account being referenced is the account making the API request.

  - `default_settings.billing_cycle_anchor` (enum)
    Possible values are `phase_start` or `automatic`. If `phase_start` then billing cycle anchor of the subscription is set to the start of the phase when entering the phase. If `automatic` then the billing cycle anchor is automatically modified as needed when entering the phase. For more information, see the billing cycle [documentation](https://docs.stripe.com/docs/billing/subscriptions/billing-cycle.md).

  - `default_settings.billing_thresholds` (nullable object)
    Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period

    - `default_settings.billing_thresholds.amount_gte` (nullable integer)
      Monetary threshold that triggers the subscription to create an invoice

    - `default_settings.billing_thresholds.reset_billing_cycle_anchor` (nullable boolean)
      Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged. This value may not be `true` if the subscription contains items with plans that have `aggregate_usage=last_ever`.

  - `default_settings.collection_method` (nullable enum)
    Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`.

    Attempt payment using the default source attached to the customer.

    Email payment instructions to the customer.

  - `default_settings.default_payment_method` (nullable string)
    ID of the default payment method for the subscription schedule. If not set, invoices will use the default payment method in the customer’s invoice settings.

  - `default_settings.description` (nullable string)
    Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.

  - `default_settings.invoice_settings` (object)
    The subscription schedule’s default invoice settings.

    - `default_settings.invoice_settings.account_tax_ids` (nullable array of strings)
      The account tax IDs associated with the subscription schedule. Will be set on invoices generated by the subscription schedule.

    - `default_settings.invoice_settings.issuer` (object)
      The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.

      - `default_settings.invoice_settings.issuer.account` (nullable string)
        The connected account being referenced when `type` is `account`.

      - `default_settings.invoice_settings.issuer.type` (enum)
        Type of the account referenced.

        Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

        Indicates that the account being referenced is the account making the API request.

  - `default_settings.on_behalf_of` (nullable string)
    The account (if any) the charge was made on behalf of for charges associated with the schedule’s subscription. See the Connect documentation for details.

  - `default_settings.transfer_data` (nullable object)
    The account (if any) the associated subscription’s payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the subscription’s invoices.

    - `default_settings.transfer_data.amount_percent` (nullable float)
      A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.

    - `default_settings.transfer_data.destination` (string)
      The account where funds from the payment will be transferred to upon payment success.

- `end_behavior` (enum)
  Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running. `cancel` will end the subscription schedule and cancel the underlying subscription.

  Cancel the underlying subscription when the subscription schedule ends.

  Persist the underlying subscription in its current state when the subscription schedule ends.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (nullable object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `phases` (array of objects)
  Configuration for the subscription schedule’s phases.

  - `phases.add_invoice_items` (array of objects)
    A list of prices and quantities that will generate invoice items appended to the next invoice for this phase.

    - `phases.add_invoice_items.discounts` (array of objects)
      The stackable discounts that will be applied to the item.

      - `phases.add_invoice_items.discounts.coupon` (nullable string)
        ID of the coupon to create a new discount for.

      - `phases.add_invoice_items.discounts.discount` (nullable string)
        ID of an existing discount on the object (or one of its ancestors) to reuse.

      - `phases.add_invoice_items.discounts.promotion_code` (nullable string)
        ID of the promotion code to create a new discount for.

    - `phases.add_invoice_items.price` (string)
      ID of the price used to generate the invoice item.

    - `phases.add_invoice_items.quantity` (nullable integer)
      The quantity of the invoice item.

    - `phases.add_invoice_items.tax_rates` (nullable array of objects)
      The tax rates which apply to the item. When set, the `default_tax_rates` do not apply to this item.

      - `phases.add_invoice_items.tax_rates.id` (string)
        Unique identifier for the object.

      - `phases.add_invoice_items.tax_rates.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `phases.add_invoice_items.tax_rates.active` (boolean)
        Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

      - `phases.add_invoice_items.tax_rates.country` (nullable string)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `phases.add_invoice_items.tax_rates.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `phases.add_invoice_items.tax_rates.description` (nullable string)
        An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

      - `phases.add_invoice_items.tax_rates.display_name` (string)
        The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

      - `phases.add_invoice_items.tax_rates.effective_percentage` (nullable float)
        Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true,
        this percentage reflects the rate actually used to calculate tax based on the product’s taxability
        and whether the user is registered to collect taxes in the corresponding jurisdiction.

      - `phases.add_invoice_items.tax_rates.flat_amount` (nullable object)
        The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

        - `phases.add_invoice_items.tax_rates.flat_amount.amount` (integer)
          Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

        - `phases.add_invoice_items.tax_rates.flat_amount.currency` (string)
          Three-letter ISO currency code, in lowercase.

      - `phases.add_invoice_items.tax_rates.inclusive` (boolean)
        This specifies if the tax rate is inclusive or exclusive.

      - `phases.add_invoice_items.tax_rates.jurisdiction` (nullable string)
        The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

      - `phases.add_invoice_items.tax_rates.jurisdiction_level` (nullable enum)
        The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.

      - `phases.add_invoice_items.tax_rates.livemode` (boolean)
        Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

      - `phases.add_invoice_items.tax_rates.metadata` (nullable object)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `phases.add_invoice_items.tax_rates.percentage` (float)
        Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

      - `phases.add_invoice_items.tax_rates.rate_type` (nullable enum)
        Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.

        A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

        A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

      - `phases.add_invoice_items.tax_rates.state` (nullable string)
        [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

      - `phases.add_invoice_items.tax_rates.tax_type` (nullable enum)
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

  - `phases.application_fee_percent` (nullable float)
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner’s Stripe account during this phase of the schedule.

  - `phases.automatic_tax` (nullable object)
    Automatic tax settings for this phase.

    - `phases.automatic_tax.disabled_reason` (nullable enum)
      If Stripe disabled automatic tax, this enum describes why.

      Stripe’s systems automatically turned off Tax for this subscription schedule when finalizing one of its invoices with a missing or incomplete location for your customer.

    - `phases.automatic_tax.enabled` (boolean)
      Whether Stripe automatically computes tax on invoices created during this phase.

    - `phases.automatic_tax.liability` (nullable object)
      The account that’s liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.

      - `phases.automatic_tax.liability.account` (nullable string)
        The connected account being referenced when `type` is `account`.

      - `phases.automatic_tax.liability.type` (enum)
        Type of the account referenced.

        Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

        Indicates that the account being referenced is the account making the API request.

  - `phases.billing_cycle_anchor` (nullable enum)
    Possible values are `phase_start` or `automatic`. If `phase_start` then billing cycle anchor of the subscription is set to the start of the phase when entering the phase. If `automatic` then the billing cycle anchor is automatically modified as needed when entering the phase. For more information, see the billing cycle [documentation](https://docs.stripe.com/docs/billing/subscriptions/billing-cycle.md).

  - `phases.billing_thresholds` (nullable object)
    Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period

    - `phases.billing_thresholds.amount_gte` (nullable integer)
      Monetary threshold that triggers the subscription to create an invoice

    - `phases.billing_thresholds.reset_billing_cycle_anchor` (nullable boolean)
      Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged. This value may not be `true` if the subscription contains items with plans that have `aggregate_usage=last_ever`.

  - `phases.collection_method` (nullable enum)
    Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`.

  - `phases.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `phases.default_payment_method` (nullable string)
    ID of the default payment method for the subscription schedule. It must belong to the customer associated with the subscription schedule. If not set, invoices will use the default payment method in the customer’s invoice settings.

  - `phases.default_tax_rates` (nullable array of objects)
    The default tax rates to apply to the subscription during this phase of the subscription schedule.

    - `phases.default_tax_rates.id` (string)
      Unique identifier for the object.

    - `phases.default_tax_rates.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `phases.default_tax_rates.active` (boolean)
      Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

    - `phases.default_tax_rates.country` (nullable string)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `phases.default_tax_rates.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `phases.default_tax_rates.description` (nullable string)
      An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

    - `phases.default_tax_rates.display_name` (string)
      The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

    - `phases.default_tax_rates.effective_percentage` (nullable float)
      Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true,
      this percentage reflects the rate actually used to calculate tax based on the product’s taxability
      and whether the user is registered to collect taxes in the corresponding jurisdiction.

    - `phases.default_tax_rates.flat_amount` (nullable object)
      The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

      - `phases.default_tax_rates.flat_amount.amount` (integer)
        Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

      - `phases.default_tax_rates.flat_amount.currency` (string)
        Three-letter ISO currency code, in lowercase.

    - `phases.default_tax_rates.inclusive` (boolean)
      This specifies if the tax rate is inclusive or exclusive.

    - `phases.default_tax_rates.jurisdiction` (nullable string)
      The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

    - `phases.default_tax_rates.jurisdiction_level` (nullable enum)
      The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.

    - `phases.default_tax_rates.livemode` (boolean)
      Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

    - `phases.default_tax_rates.metadata` (nullable object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `phases.default_tax_rates.percentage` (float)
      Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

    - `phases.default_tax_rates.rate_type` (nullable enum)
      Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.

      A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

      A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

    - `phases.default_tax_rates.state` (nullable string)
      [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

    - `phases.default_tax_rates.tax_type` (nullable enum)
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

  - `phases.description` (nullable string)
    Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.

  - `phases.discounts` (array of objects)
    The stackable discounts that will be applied to the subscription on this phase. Subscription item discounts are applied before subscription discounts.

    - `phases.discounts.coupon` (nullable string)
      ID of the coupon to create a new discount for.

    - `phases.discounts.discount` (nullable string)
      ID of an existing discount on the object (or one of its ancestors) to reuse.

    - `phases.discounts.promotion_code` (nullable string)
      ID of the promotion code to create a new discount for.

  - `phases.end_date` (timestamp)
    The end of this phase of the subscription schedule.

  - `phases.invoice_settings` (nullable object)
    The invoice settings applicable during this phase.

    - `phases.invoice_settings.account_tax_ids` (nullable array of strings)
      The account tax IDs associated with this phase of the subscription schedule. Will be set on invoices generated by this phase of the subscription schedule.

    - `phases.invoice_settings.issuer` (nullable object)
      The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.

      - `phases.invoice_settings.issuer.account` (nullable string)
        The connected account being referenced when `type` is `account`.

      - `phases.invoice_settings.issuer.type` (enum)
        Type of the account referenced.

        Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

        Indicates that the account being referenced is the account making the API request.

  - `phases.items` (array of objects)
    Subscription items to configure the subscription to during this phase of the subscription schedule.

    - `phases.items.billing_thresholds` (nullable object)
      Define thresholds at which an invoice will be sent, and the related subscription advanced to a new billing period

      - `phases.items.billing_thresholds.usage_gte` (nullable integer)
        Usage threshold that triggers the subscription to create an invoice

    - `phases.items.discounts` (array of objects)
      The discounts applied to the subscription item. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount.

      - `phases.items.discounts.coupon` (nullable string)
        ID of the coupon to create a new discount for.

      - `phases.items.discounts.discount` (nullable string)
        ID of an existing discount on the object (or one of its ancestors) to reuse.

      - `phases.items.discounts.promotion_code` (nullable string)
        ID of the promotion code to create a new discount for.

    - `phases.items.metadata` (nullable object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an item. Metadata on this item will update the underlying subscription item’s `metadata` when the phase is entered.

    - `phases.items.price` (string)
      ID of the price to which the customer should be subscribed.

    - `phases.items.quantity` (nullable integer)
      Quantity of the plan to which the customer should be subscribed.

    - `phases.items.tax_rates` (nullable array of objects)
      The tax rates which apply to this `phase_item`. When set, the `default_tax_rates` on the phase do not apply to this `phase_item`.

      - `phases.items.tax_rates.id` (string)
        Unique identifier for the object.

      - `phases.items.tax_rates.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `phases.items.tax_rates.active` (boolean)
        Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

      - `phases.items.tax_rates.country` (nullable string)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `phases.items.tax_rates.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `phases.items.tax_rates.description` (nullable string)
        An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

      - `phases.items.tax_rates.display_name` (string)
        The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

      - `phases.items.tax_rates.effective_percentage` (nullable float)
        Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true,
        this percentage reflects the rate actually used to calculate tax based on the product’s taxability
        and whether the user is registered to collect taxes in the corresponding jurisdiction.

      - `phases.items.tax_rates.flat_amount` (nullable object)
        The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

        - `phases.items.tax_rates.flat_amount.amount` (integer)
          Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

        - `phases.items.tax_rates.flat_amount.currency` (string)
          Three-letter ISO currency code, in lowercase.

      - `phases.items.tax_rates.inclusive` (boolean)
        This specifies if the tax rate is inclusive or exclusive.

      - `phases.items.tax_rates.jurisdiction` (nullable string)
        The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

      - `phases.items.tax_rates.jurisdiction_level` (nullable enum)
        The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.

      - `phases.items.tax_rates.livemode` (boolean)
        Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

      - `phases.items.tax_rates.metadata` (nullable object)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `phases.items.tax_rates.percentage` (float)
        Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

      - `phases.items.tax_rates.rate_type` (nullable enum)
        Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.

        A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

        A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

      - `phases.items.tax_rates.state` (nullable string)
        [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

      - `phases.items.tax_rates.tax_type` (nullable enum)
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

  - `phases.metadata` (nullable object)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to a phase. Metadata on a schedule’s phase will update the underlying subscription’s `metadata` when the phase is entered. Updating the underlying subscription’s `metadata` directly will not affect the current phase’s `metadata`.

  - `phases.on_behalf_of` (nullable string)
    The account (if any) the charge was made on behalf of for charges associated with the schedule’s subscription. See the Connect documentation for details.

  - `phases.proration_behavior` (enum)
    When transitioning phases, controls how prorations are handled (if any). Possible values are `create_prorations`, `none`, and `always_invoice`.

  - `phases.start_date` (timestamp)
    The start of this phase of the subscription schedule.

  - `phases.transfer_data` (nullable object)
    The account (if any) the associated subscription’s payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the subscription’s invoices.

    - `phases.transfer_data.amount_percent` (nullable float)
      A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.

    - `phases.transfer_data.destination` (string)
      The account where funds from the payment will be transferred to upon payment success.

  - `phases.trial_end` (nullable timestamp)
    When the trial ends within the phase.

- `released_at` (nullable timestamp)
  Time at which the subscription schedule was released. Measured in seconds since the Unix epoch.

- `released_subscription` (nullable string)
  ID of the subscription once managed by the subscription schedule (if it is released).

- `status` (enum)
  The present status of the subscription schedule. Possible values are `not_started`, `active`, `completed`, `released`, and `canceled`. You can read more about the different states in our [behavior guide](https://docs.stripe.com/docs/billing/subscriptions/subscription-schedules.md).

- `subscription` (nullable string)
  ID of the subscription managed by the subscription schedule.

- `test_clock` (nullable string)
  ID of the test clock this subscription schedule belongs to.