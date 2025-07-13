# The Payment Link object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `active` (boolean)
  Whether the payment link’s `url` is active. If `false`, customers visiting the URL will be shown a page saying that the link has been deactivated.

- `after_completion` (object)
  Behavior after the purchase is complete.

  - `after_completion.hosted_confirmation` (nullable object)
    Configuration when `type=hosted_confirmation`.

    - `after_completion.hosted_confirmation.custom_message` (nullable string)
      The custom message that is displayed to the customer after the purchase is complete.

  - `after_completion.redirect` (nullable object)
    Configuration when `type=redirect`.

    - `after_completion.redirect.url` (string)
      The URL the customer will be redirected to after the purchase is complete.

  - `after_completion.type` (enum)
    The specified behavior after the purchase is complete.

    Displays a message on the hosted surface after the purchase is complete.

    Redirects the customer to the specified `url` after the purchase is complete.

- `allow_promotion_codes` (boolean)
  Whether user redeemable promotion codes are enabled.

- `application` (nullable string)
  The ID of the Connect application that created the Payment Link.

- `application_fee_amount` (nullable integer)
  The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner’s Stripe account.

- `application_fee_percent` (nullable float)
  This represents the percentage of the subscription invoice total that will be transferred to the application owner’s Stripe account.

- `automatic_tax` (object)
  Configuration details for automatic tax collection.

  - `automatic_tax.enabled` (boolean)
    If `true`, tax will be calculated automatically using the customer’s location.

  - `automatic_tax.liability` (nullable object)
    The account that’s liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.

    - `automatic_tax.liability.account` (nullable string)
      The connected account being referenced when `type` is `account`.

    - `automatic_tax.liability.type` (enum)
      Type of the account referenced.

      Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

      Indicates that the account being referenced is the account making the API request.

- `billing_address_collection` (enum)
  Configuration for collecting the customer’s billing address. Defaults to `auto`.

  Checkout will only collect the billing address when necessary. When using [automatic_tax](https://docs.stripe.com/docs/api/checkout/sessions/object.md#checkout_session_object-automatic_tax-enabled), Checkout will collect the minimum number of fields required for tax calculation.

  Checkout will always collect the customer’s billing address.

- `consent_collection` (nullable object)
  When set, provides configuration to gather active consent from customers.

  - `consent_collection.payment_method_reuse_agreement` (nullable object)
    Settings related to the payment method reuse text shown in the Checkout UI.

    - `consent_collection.payment_method_reuse_agreement.position` (enum)
      Determines the position and visibility of the payment method reuse agreement in the UI. When set to `auto`, Stripe’s defaults will be used.

      When set to `hidden`, the payment method reuse agreement text will always be hidden in the UI.

  - `consent_collection.promotions` (nullable enum)
    If set to `auto`, enables the collection of customer consent for promotional communications.

  - `consent_collection.terms_of_service` (nullable enum)
    If set to `required`, it requires cutomers to accept the terms of service before being able to pay. If set to `none`, customers won’t be shown a checkbox to accept the terms of service.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `custom_fields` (array of objects)
  Collect additional information from your customer using custom fields. Up to 3 fields are supported.

  - `custom_fields.dropdown` (nullable object)
    Configuration for `type=dropdown` fields.

    - `custom_fields.dropdown.default_value` (nullable string)
      The value that will pre-fill on the payment page.

    - `custom_fields.dropdown.options` (array of objects)
      The options available for the customer to select. Up to 200 options allowed.

      - `custom_fields.dropdown.options.label` (string)
        The label for the option, displayed to the customer. Up to 100 characters.

      - `custom_fields.dropdown.options.value` (string)
        The value for this option, not displayed to the customer, used by your integration to reconcile the option selected by the customer. Must be unique to this option, alphanumeric, and up to 100 characters.

  - `custom_fields.key` (string)
    String of your choice that your integration can use to reconcile this field. Must be unique to this field, alphanumeric, and up to 200 characters.

  - `custom_fields.label` (object)
    The label for the field, displayed to the customer.

    - `custom_fields.label.custom` (nullable string)
      Custom text for the label, displayed to the customer. Up to 50 characters.

    - `custom_fields.label.type` (enum)
      The type of the label.

      Set a custom label for the field.

  - `custom_fields.numeric` (nullable object)
    Configuration for `type=numeric` fields.

    - `custom_fields.numeric.default_value` (nullable string)
      The value that will pre-fill the field on the payment page.

    - `custom_fields.numeric.maximum_length` (nullable integer)
      The maximum character length constraint for the customer’s input.

    - `custom_fields.numeric.minimum_length` (nullable integer)
      The minimum character length requirement for the customer’s input.

  - `custom_fields.optional` (boolean)
    Whether the customer is required to complete the field before completing the Checkout Session. Defaults to `false`.

  - `custom_fields.text` (nullable object)
    Configuration for `type=text` fields.

    - `custom_fields.text.default_value` (nullable string)
      The value that will pre-fill the field on the payment page.

    - `custom_fields.text.maximum_length` (nullable integer)
      The maximum character length constraint for the customer’s input.

    - `custom_fields.text.minimum_length` (nullable integer)
      The minimum character length requirement for the customer’s input.

  - `custom_fields.type` (enum)
    The type of the field.

    Provide a list of options for your customer to select.

    Collect a numbers-only field from your customer.

    Collect a string field from your customer.

- `custom_text` (object)
  Display additional text for your customers using custom text.

  - `custom_text.after_submit` (nullable object)
    Custom text that should be displayed after the payment confirmation button.

    - `custom_text.after_submit.message` (string)
      Text may be up to 1200 characters in length.

  - `custom_text.shipping_address` (nullable object)
    Custom text that should be displayed alongside shipping address collection.

    - `custom_text.shipping_address.message` (string)
      Text may be up to 1200 characters in length.

  - `custom_text.submit` (nullable object)
    Custom text that should be displayed alongside the payment confirmation button.

    - `custom_text.submit.message` (string)
      Text may be up to 1200 characters in length.

  - `custom_text.terms_of_service_acceptance` (nullable object)
    Custom text that should be displayed in place of the default terms of service agreement text.

    - `custom_text.terms_of_service_acceptance.message` (string)
      Text may be up to 1200 characters in length.

- `customer_creation` (enum)
  Configuration for Customer creation during checkout.

  The Checkout Session will always create a [Customer](https://docs.stripe.com/docs/api/customers.md) when a Session confirmation is attempted.

  The Checkout Session will only create a [Customer](https://docs.stripe.com/docs/api/customers.md) if it is required for Session confirmation.
  Currently, only `subscription` mode Sessions and `payment` mode Sessions with [post-purchase invoices enabled](https://docs.stripe.com/docs/receipts.md?payment-ui=checkout#paid-invoices) require a Customer.

- `inactive_message` (nullable string)
  The custom message to be displayed to a customer when a payment link is no longer active.

- `invoice_creation` (nullable object)
  Configuration for creating invoice for payment mode payment links.

  - `invoice_creation.enabled` (boolean)
    Enable creating an invoice on successful payment.

  - `invoice_creation.invoice_data` (nullable object)
    Configuration for the invoice. Default invoice values will be used if unspecified.

    - `invoice_creation.invoice_data.account_tax_ids` (nullable array of strings)
      The account tax IDs associated with the invoice.

    - `invoice_creation.invoice_data.custom_fields` (nullable array of objects)
      A list of up to 4 custom fields to be displayed on the invoice.

      - `invoice_creation.invoice_data.custom_fields.name` (string)
        The name of the custom field.

      - `invoice_creation.invoice_data.custom_fields.value` (string)
        The value of the custom field.

    - `invoice_creation.invoice_data.description` (nullable string)
      An arbitrary string attached to the object. Often useful for displaying to users.

    - `invoice_creation.invoice_data.footer` (nullable string)
      Footer to be displayed on the invoice.

    - `invoice_creation.invoice_data.issuer` (nullable object)
      The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.

      - `invoice_creation.invoice_data.issuer.account` (nullable string)
        The connected account being referenced when `type` is `account`.

      - `invoice_creation.invoice_data.issuer.type` (enum)
        Type of the account referenced.

        Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

        Indicates that the account being referenced is the account making the API request.

    - `invoice_creation.invoice_data.metadata` (nullable object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `invoice_creation.invoice_data.rendering_options` (nullable object)
      Options for invoice PDF rendering.

      - `invoice_creation.invoice_data.rendering_options.amount_tax_display` (nullable string)
        How line-item prices and amounts will be displayed with respect to tax on invoice PDFs.

- `line_items` (object)
  The line items representing what is being sold.

  - `line_items.object` (string)
    String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

  - `line_items.data` (array of objects)
    Details about each object.

    - `line_items.data.id` (string)
      Unique identifier for the object.

    - `line_items.data.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `line_items.data.amount_discount` (integer)
      Total discount amount applied. If no discounts were applied, defaults to 0.

    - `line_items.data.amount_subtotal` (integer)
      Total before any discounts or taxes are applied.

    - `line_items.data.amount_tax` (integer)
      Total tax amount applied. If no tax was applied, defaults to 0.

    - `line_items.data.amount_total` (integer)
      Total after discounts and taxes.

    - `line_items.data.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `line_items.data.description` (nullable string)
      An arbitrary string attached to the object. Often useful for displaying to users. Defaults to product name.

    - `line_items.data.discounts` (nullable array of objects)
      The discounts applied to the line item.

      - `line_items.data.discounts.amount` (integer)
        The amount discounted.

      - `line_items.data.discounts.discount` (object)
        The discount applied.

        - `line_items.data.discounts.discount.id` (string)
          The ID of the discount object. Discounts cannot be fetched by ID. Use `expand[]=discounts` in API calls to expand discount IDs in an array.

        - `line_items.data.discounts.discount.object` (string)
          String representing the object’s type. Objects of the same type share the same value.

        - `line_items.data.discounts.discount.checkout_session` (nullable string)
          The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode.

        - `line_items.data.discounts.discount.coupon` (object)
          Hash describing the coupon applied to create this discount.

          - `line_items.data.discounts.discount.coupon.id` (string)
            Unique identifier for the object.

          - `line_items.data.discounts.discount.coupon.object` (string)
            String representing the object’s type. Objects of the same type share the same value.

          - `line_items.data.discounts.discount.coupon.amount_off` (nullable integer)
            Amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer.

          - `line_items.data.discounts.discount.coupon.applies_to` (nullable object)
            Contains information about what this coupon applies to.

            - `line_items.data.discounts.discount.coupon.applies_to.products` (array of strings)
              A list of product IDs this coupon applies to

          - `line_items.data.discounts.discount.coupon.created` (timestamp)
            Time at which the object was created. Measured in seconds since the Unix epoch.

          - `line_items.data.discounts.discount.coupon.currency` (nullable enum)
            If `amount_off` has been set, the three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the amount to take off.

          - `line_items.data.discounts.discount.coupon.currency_options` (nullable object)
            Coupons defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

            - `line_items.data.discounts.discount.coupon.currency_options.<currency>.amount_off` (integer)
              Amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer.

          - `line_items.data.discounts.discount.coupon.duration` (enum)
            One of `forever`, `once`, or `repeating`. Describes how long a customer who applies this coupon will get the discount.

            Applies to all charges from a subscription with this coupon applied.

            Applies to the first charge from a subscription with this coupon applied.

            Applies to charges in the first `duration_in_months` months from a subscription with this coupon applied. This value is deprecated and will be replaced in future versions of the API.

          - `line_items.data.discounts.discount.coupon.duration_in_months` (nullable integer)
            If `duration` is `repeating`, the number of months the coupon applies. Null if coupon `duration` is `forever` or `once`.

          - `line_items.data.discounts.discount.coupon.livemode` (boolean)
            Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

          - `line_items.data.discounts.discount.coupon.max_redemptions` (nullable integer)
            Maximum number of times this coupon can be redeemed, in total, across all customers, before it is no longer valid.

          - `line_items.data.discounts.discount.coupon.metadata` (nullable object)
            Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

          - `line_items.data.discounts.discount.coupon.name` (nullable string)
            Name of the coupon displayed to customers on for instance invoices or receipts.

          - `line_items.data.discounts.discount.coupon.percent_off` (nullable float)
            Percent that will be taken off the subtotal of any invoices for this customer for the duration of the coupon. For example, a coupon with percent_off of 50 will make a 100 invoice 50 instead.

          - `line_items.data.discounts.discount.coupon.redeem_by` (nullable timestamp)
            Date after which the coupon can no longer be redeemed.

          - `line_items.data.discounts.discount.coupon.times_redeemed` (integer)
            Number of times this coupon has been applied to a customer.

          - `line_items.data.discounts.discount.coupon.valid` (boolean)
            Taking account of the above properties, whether this coupon can still be applied to a customer.

        - `line_items.data.discounts.discount.customer` (nullable string)
          The ID of the customer associated with this discount.

        - `line_items.data.discounts.discount.end` (nullable timestamp)
          If the coupon has a duration of `repeating`, the date that this discount will end. If the coupon has a duration of `once` or `forever`, this attribute will be null.

        - `line_items.data.discounts.discount.invoice` (nullable string)
          The invoice that the discount’s coupon was applied to, if it was applied directly to a particular invoice.

        - `line_items.data.discounts.discount.invoice_item` (nullable string)
          The invoice item `id` (or invoice line item `id` for invoice line items of type=‘subscription’) that the discount’s coupon was applied to, if it was applied directly to a particular invoice item or invoice line item.

        - `line_items.data.discounts.discount.promotion_code` (nullable string)
          The promotion code applied to create this discount.

        - `line_items.data.discounts.discount.start` (timestamp)
          Date that the coupon was applied.

        - `line_items.data.discounts.discount.subscription` (nullable string)
          The subscription that this coupon is applied to, if it is applied to a particular subscription.

        - `line_items.data.discounts.discount.subscription_item` (nullable string)
          The subscription item that this coupon is applied to, if it is applied to a particular subscription item.

    - `line_items.data.price` (nullable object)
      The price used to generate the line item.

      - `line_items.data.price.id` (string)
        Unique identifier for the object.

      - `line_items.data.price.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `line_items.data.price.active` (boolean)
        Whether the price can be used for new purchases.

      - `line_items.data.price.billing_scheme` (enum)
        Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.

      - `line_items.data.price.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `line_items.data.price.currency` (enum)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `line_items.data.price.currency_options` (nullable object)
        Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

        - `line_items.data.price.currency_options.<currency>.custom_unit_amount` (nullable object)
          When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

          - `line_items.data.price.currency_options.<currency>.custom_unit_amount.maximum` (nullable integer)
            The maximum unit amount the customer can specify for this item.

          - `line_items.data.price.currency_options.<currency>.custom_unit_amount.minimum` (nullable integer)
            The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

          - `line_items.data.price.currency_options.<currency>.custom_unit_amount.preset` (nullable integer)
            The starting unit amount which can be updated by the customer.

        - `line_items.data.price.currency_options.<currency>.tax_behavior` (nullable enum)
          Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.

        - `line_items.data.price.currency_options.<currency>.tiers` (nullable array of objects)
          Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

          - `line_items.data.price.currency_options.<currency>.tiers.flat_amount` (nullable integer)
            Price for the entire tier.

          - `line_items.data.price.currency_options.<currency>.tiers.flat_amount_decimal` (nullable decimal string)
            Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

          - `line_items.data.price.currency_options.<currency>.tiers.unit_amount` (nullable integer)
            Per unit price for units relevant to the tier.

          - `line_items.data.price.currency_options.<currency>.tiers.unit_amount_decimal` (nullable decimal string)
            Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

          - `line_items.data.price.currency_options.<currency>.tiers.up_to` (nullable integer)
            Up to and including to this quantity will be contained in the tier.

        - `line_items.data.price.currency_options.<currency>.unit_amount` (nullable integer)
          The unit amount in  to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

        - `line_items.data.price.currency_options.<currency>.unit_amount_decimal` (nullable decimal string)
          The unit amount in  to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

      - `line_items.data.price.custom_unit_amount` (nullable object)
        When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

        - `line_items.data.price.custom_unit_amount.maximum` (nullable integer)
          The maximum unit amount the customer can specify for this item.

        - `line_items.data.price.custom_unit_amount.minimum` (nullable integer)
          The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

        - `line_items.data.price.custom_unit_amount.preset` (nullable integer)
          The starting unit amount which can be updated by the customer.

      - `line_items.data.price.livemode` (boolean)
        Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

      - `line_items.data.price.lookup_key` (nullable string)
        A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters.

      - `line_items.data.price.metadata` (object)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `line_items.data.price.nickname` (nullable string)
        A brief description of the price, hidden from customers.

      - `line_items.data.price.product` (string)
        The ID of the product this price is associated with.

      - `line_items.data.price.recurring` (nullable object)
        The recurring components of a price such as `interval` and `usage_type`.

        - `line_items.data.price.recurring.interval` (enum)
          The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`.

        - `line_items.data.price.recurring.interval_count` (integer)
          The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months.

        - `line_items.data.price.recurring.meter` (nullable string)
          The meter tracking the usage of a metered price

        - `line_items.data.price.recurring.usage_type` (enum)
          Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`.

      - `line_items.data.price.tax_behavior` (nullable enum)
        Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.

      - `line_items.data.price.tiers` (nullable array of objects)
        Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

        - `line_items.data.price.tiers.flat_amount` (nullable integer)
          Price for the entire tier.

        - `line_items.data.price.tiers.flat_amount_decimal` (nullable decimal string)
          Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

        - `line_items.data.price.tiers.unit_amount` (nullable integer)
          Per unit price for units relevant to the tier.

        - `line_items.data.price.tiers.unit_amount_decimal` (nullable decimal string)
          Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

        - `line_items.data.price.tiers.up_to` (nullable integer)
          Up to and including to this quantity will be contained in the tier.

      - `line_items.data.price.tiers_mode` (nullable enum)
        Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price. In `graduated` tiering, pricing can change as the quantity grows.

      - `line_items.data.price.transform_quantity` (nullable object)
        Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`.

        - `line_items.data.price.transform_quantity.divide_by` (integer)
          Divide usage by this number.

        - `line_items.data.price.transform_quantity.round` (enum)
          After division, either round the result `up` or `down`.

      - `line_items.data.price.type` (enum)
        One of `one_time` or `recurring` depending on whether the price is for a one-time purchase or a recurring (subscription) purchase.

      - `line_items.data.price.unit_amount` (nullable integer)
        The unit amount in  to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

      - `line_items.data.price.unit_amount_decimal` (nullable decimal string)
        The unit amount in  to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

    - `line_items.data.quantity` (nullable integer)
      The quantity of products being purchased.

    - `line_items.data.taxes` (nullable array of objects)
      The taxes applied to the line item.

      - `line_items.data.taxes.amount` (integer)
        Amount of tax applied for this rate.

      - `line_items.data.taxes.rate` (object)
        The tax rate applied.

        - `line_items.data.taxes.rate.id` (string)
          Unique identifier for the object.

        - `line_items.data.taxes.rate.object` (string)
          String representing the object’s type. Objects of the same type share the same value.

        - `line_items.data.taxes.rate.active` (boolean)
          Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

        - `line_items.data.taxes.rate.country` (nullable string)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `line_items.data.taxes.rate.created` (timestamp)
          Time at which the object was created. Measured in seconds since the Unix epoch.

        - `line_items.data.taxes.rate.description` (nullable string)
          An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

        - `line_items.data.taxes.rate.display_name` (string)
          The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

        - `line_items.data.taxes.rate.effective_percentage` (nullable float)
          Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true,
          this percentage reflects the rate actually used to calculate tax based on the product’s taxability
          and whether the user is registered to collect taxes in the corresponding jurisdiction.

        - `line_items.data.taxes.rate.flat_amount` (nullable object)
          The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

          - `line_items.data.taxes.rate.flat_amount.amount` (integer)
            Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

          - `line_items.data.taxes.rate.flat_amount.currency` (string)
            Three-letter ISO currency code, in lowercase.

        - `line_items.data.taxes.rate.inclusive` (boolean)
          This specifies if the tax rate is inclusive or exclusive.

        - `line_items.data.taxes.rate.jurisdiction` (nullable string)
          The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

        - `line_items.data.taxes.rate.jurisdiction_level` (nullable enum)
          The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.

        - `line_items.data.taxes.rate.livemode` (boolean)
          Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

        - `line_items.data.taxes.rate.metadata` (nullable object)
          Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

        - `line_items.data.taxes.rate.percentage` (float)
          Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

        - `line_items.data.taxes.rate.rate_type` (nullable enum)
          Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.

          A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

          A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

        - `line_items.data.taxes.rate.state` (nullable string)
          [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

        - `line_items.data.taxes.rate.tax_type` (nullable enum)
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

      - `line_items.data.taxes.taxability_reason` (nullable enum)
        The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.

        No tax is applied as the customer is exempt from tax.

        No tax is collected either because you are not registered to collect tax in this jurisdiction, or because the non-taxable product tax code (`txcd_00000000`) was used.

        No tax is imposed on this transaction.

        No tax applied. Stripe doesn’t support this jurisdiction, territory, or product.

        A portion of the price is exempt from tax.

        A portion of the price is taxed at a reduced rate.

        A portion of the price is taxed at the standard rate.

        The product or service is nontaxable or exempt from tax.

        The product or service is not taxed due to a sales tax holiday.

        The shipping cost tax rate is calculated as a weighted average of the other line items’ rates, weighted by their amounts.

        Taxed at a reduced rate.

        No tax is applied as it is the responsibility of the buyer to account for tax in this case.

        Taxed at the standard rate.

        A reduced amount of the price is subject to tax.

        The transaction is taxed at a special rate of 0% or the transaction is exempt (but these exempt transactions still let you deduct the “input VAT” paid on your business purchases).

      - `line_items.data.taxes.taxable_amount` (nullable integer)
        The amount on which tax is calculated, in .

  - `line_items.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `line_items.url` (string)
    The URL where this list can be accessed.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `on_behalf_of` (nullable string)
  The account on behalf of which to charge. See the [Connect documentation](https://support.stripe.com/questions/sending-invoices-on-behalf-of-connected-accounts) for details.

- `optional_items` (nullable array of objects)
  The optional items presented to the customer at checkout.

- `payment_intent_data` (nullable object)
  Indicates the parameters to be passed to PaymentIntent creation during checkout.

  - `payment_intent_data.capture_method` (nullable enum)
    Indicates when the funds will be captured from the customer’s account.

    Stripe automatically captures funds when the customer authorizes the payment.

    (Default) Stripe asynchronously captures funds when the customer authorizes the payment. Recommended over `capture_method=automatic` due to improved latency. Read the [integration guide](https://docs.stripe.com/docs/payments/payment-intents/asynchronous-capture.md) for more information.

    Place a hold on the funds when the customer authorizes the payment, but [don’t capture the funds until later](https://docs.stripe.com/docs/payments/capture-later.md). (Not all payment methods support this.)

  - `payment_intent_data.description` (nullable string)
    An arbitrary string attached to the object. Often useful for displaying to users.

  - `payment_intent_data.metadata` (object)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that will set metadata on [Payment Intents](https://docs.stripe.com/docs/api/payment_intents.md) generated from this payment link.

  - `payment_intent_data.setup_future_usage` (nullable enum)
    Indicates that you intend to make future payments with the payment method collected during checkout.

    Use `off_session` if your customer may or may not be present in your checkout flow.

    Use `on_session` if you intend to only reuse the payment method when your customer is present in your checkout flow.

  - `payment_intent_data.statement_descriptor` (nullable string)
    For a non-card payment, information about the charge that appears on the customer’s statement when this payment succeeds in creating a charge.

  - `payment_intent_data.statement_descriptor_suffix` (nullable string)
    For a card payment, information about the charge that appears on the customer’s statement when this payment succeeds in creating a charge. Concatenated with the account’s statement descriptor prefix to form the complete statement descriptor.

  - `payment_intent_data.transfer_group` (nullable string)
    A string that identifies the resulting payment as part of a group. See the PaymentIntents [use case for connected accounts](https://docs.stripe.com/docs/connect/separate-charges-and-transfers.md) for details.

- `payment_method_collection` (enum)
  Configuration for collecting a payment method during checkout. Defaults to `always`.

  The Checkout Session will always collect a PaymentMethod.

  The Checkout Session will only collect a PaymentMethod if there is an amount due.

- `payment_method_types` (nullable array of enums)
  The list of payment method types that customers can use. When `null`, Stripe will dynamically show relevant payment methods you’ve enabled in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods).

- `phone_number_collection` (object)
  Controls phone number collection settings during checkout.

  - `phone_number_collection.enabled` (boolean)
    If `true`, a phone number will be collected during checkout.

- `restrictions` (nullable object)
  Settings that restrict the usage of a payment link.

  - `restrictions.completed_sessions` (object)
    Configuration for the `completed_sessions` restriction type.

    - `restrictions.completed_sessions.count` (integer)
      The current number of checkout sessions that have been completed on the payment link which count towards the `completed_sessions` restriction to be met.

    - `restrictions.completed_sessions.limit` (integer)
      The maximum number of checkout sessions that can be completed for the `completed_sessions` restriction to be met.

- `shipping_address_collection` (nullable object)
  Configuration for collecting the customer’s shipping address.

  - `shipping_address_collection.allowed_countries` (array of enums)
    An array of two-letter ISO country codes representing which countries Checkout should provide as options for shipping locations. Unsupported country codes: `AS, CX, CC, CU, HM, IR, KP, MH, FM, NF, MP, PW, SD, SY, UM, VI`.

- `shipping_options` (array of objects)
  The shipping rate options applied to the session.

  - `shipping_options.shipping_amount` (integer)
    A non-negative integer in cents representing how much to charge.

  - `shipping_options.shipping_rate` (string)
    The ID of the Shipping Rate to use for this shipping option.

- `submit_type` (enum)
  Indicates the type of transaction being performed which customizes relevant text on the page, such as the submit button.

  Default value. `pay` will used in all scenarios

  Recommended when offering bookings. Submit button includes a ‘Book’ label and URLs use the `book.stripe.com` hostname

  Recommended when accepting donations. Submit button includes a ‘Donate’ label and URLs use the `donate.stripe.com` hostname

  Submit button includes a ‘Buy’ label and URLs use the `buy.stripe.com` hostname

  Submit button includes a ‘Subscribe’ label and URLs use the `buy.stripe.com` hostname

- `subscription_data` (nullable object)
  When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`.

  - `subscription_data.description` (nullable string)
    The subscription’s description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.

  - `subscription_data.invoice_settings` (object)
    All invoices will be billed using the specified settings.

    - `subscription_data.invoice_settings.issuer` (object)
      The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.

      - `subscription_data.invoice_settings.issuer.account` (nullable string)
        The connected account being referenced when `type` is `account`.

      - `subscription_data.invoice_settings.issuer.type` (enum)
        Type of the account referenced.

        Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

        Indicates that the account being referenced is the account making the API request.

  - `subscription_data.metadata` (object)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that will set metadata on [Subscriptions](https://docs.stripe.com/docs/api/subscriptions.md) generated from this payment link.

  - `subscription_data.trial_period_days` (nullable integer)
    Integer representing the number of trial period days before the customer is charged for the first time.

  - `subscription_data.trial_settings` (nullable object)
    Settings related to subscription trials.

    - `subscription_data.trial_settings.end_behavior` (object)
      Defines how the subscription should behave when the user’s free trial ends.

      - `subscription_data.trial_settings.end_behavior.missing_payment_method` (enum)
        Indicates how the subscription should change when the trial ends if the user did not provide a payment method.

        Cancel the subscription if a payment method is not attached when the trial ends.

        Create an invoice when the trial ends, even if the user did not set up a payment method.

        Pause the subscription if a payment method is not attached when the trial ends.

- `tax_id_collection` (object)
  Details on the state of tax ID collection for the payment link.

  - `tax_id_collection.enabled` (boolean)
    Indicates whether tax ID collection is enabled for the session.

- `transfer_data` (nullable object)
  The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to.

  - `transfer_data.amount` (nullable integer)
    The amount in  that will be transferred to the destination account. By default, the entire amount is transferred to the destination.

  - `transfer_data.destination` (string)
    The connected account receiving the transfer.

- `url` (string)
  The public URL that can be shared with customers.

### The Payment Link object

```json
{
  "id": "plink_1MoC3ULkdIwHu7ixZjtGpVl2",
  "object": "payment_link",
  "active": true,
  "after_completion": {
    "hosted_confirmation": {
      "custom_message": null
    },
    "type": "hosted_confirmation"
  },
  "allow_promotion_codes": false,
  "application_fee_amount": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null
  },
  "billing_address_collection": "auto",
  "consent_collection": null,
  "currency": "usd",
  "custom_fields": [],
  "custom_text": {
    "shipping_address": null,
    "submit": null
  },
  "customer_creation": "if_required",
  "invoice_creation": {
    "enabled": false,
    "invoice_data": {
      "account_tax_ids": null,
      "custom_fields": null,
      "description": null,
      "footer": null,
      "issuer": null,
      "metadata": {},
      "rendering_options": null
    }
  },
  "livemode": false,
  "metadata": {},
  "on_behalf_of": null,
  "payment_intent_data": null,
  "payment_method_collection": "always",
  "payment_method_types": null,
  "phone_number_collection": {
    "enabled": false
  },
  "shipping_address_collection": null,
  "shipping_options": [],
  "submit_type": "auto",
  "subscription_data": {
    "description": null,
    "invoice_settings": {
      "issuer": {
        "type": "self"
      }
    },
    "trial_period_days": null
  },
  "tax_id_collection": {
    "enabled": false
  },
  "transfer_data": null,
  "url": "https://buy.stripe.com/test_cN25nr0iZ7bUa7meUY"
}
```