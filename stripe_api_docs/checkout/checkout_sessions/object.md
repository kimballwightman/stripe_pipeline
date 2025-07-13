# The Checkout Session object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `adaptive_pricing` (nullable object)
  Settings for price localization with [Adaptive Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing).

  - `adaptive_pricing.enabled` (boolean)
    Whether Adaptive Pricing is enabled.

- `after_expiration` (nullable object)
  When set, provides configuration for actions to take if this Checkout Session expires.

  - `after_expiration.recovery` (nullable object)
    When set, configuration used to recover the Checkout Session on expiry.

    - `after_expiration.recovery.allow_promotion_codes` (boolean)
      Enables user redeemable promotion codes on the recovered Checkout Sessions. Defaults to `false`

    - `after_expiration.recovery.enabled` (boolean)
      If `true`, a recovery url will be generated to recover this Checkout Session if it
      expires before a transaction is completed. It will be attached to the
      Checkout Session object upon expiration.

    - `after_expiration.recovery.expires_at` (nullable timestamp)
      The timestamp at which the recovery URL will expire.

    - `after_expiration.recovery.url` (nullable string)
      URL that creates a new Checkout Session when clicked that is a copy of this expired Checkout Session

- `allow_promotion_codes` (nullable boolean)
  Enables user redeemable promotion codes.

- `amount_subtotal` (nullable integer)
  Total of all items before discounts or taxes are applied.

- `amount_total` (nullable integer)
  Total of all items after discounts and taxes are applied.

- `automatic_tax` (object)
  Details on the state of automatic tax for the session, including the status of the latest tax calculation.

  - `automatic_tax.enabled` (boolean)
    Indicates whether automatic tax is enabled for the session

  - `automatic_tax.liability` (nullable object)
    The account that’s liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.

    - `automatic_tax.liability.account` (nullable string)
      The connected account being referenced when `type` is `account`.

    - `automatic_tax.liability.type` (enum)
      Type of the account referenced.

      Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

      Indicates that the account being referenced is the account making the API request.

  - `automatic_tax.provider` (nullable string)
    The tax provider powering automatic tax.

  - `automatic_tax.status` (nullable enum)
    The status of the most recent automated tax calculation for this session.

    The automatic tax calculation was successful.

    The tax calculation failed, please try again later.

    The location details supplied on the customer aren’t valid or don’t provide enough location information
    to accurately determine tax rates for the customer.

- `billing_address_collection` (nullable enum)
  Describes whether Checkout should collect the customer’s billing address. Defaults to `auto`.

  Checkout will only collect the billing address when necessary. When using [automatic_tax](https://docs.stripe.com/docs/api/checkout/sessions/object.md#checkout_session_object-automatic_tax-enabled), Checkout will collect the minimum number of fields required for tax calculation.

  Checkout will always collect the customer’s billing address.

- `cancel_url` (nullable string)
  If set, Checkout displays a back button and customers will be directed to this URL if they decide to cancel payment and return to your website.

- `client_reference_id` (nullable string)
  A unique string to reference the Checkout Session. This can be a
  customer ID, a cart ID, or similar, and can be used to reconcile the
  Session with your internal systems.

- `client_secret` (nullable string)
  The client secret of your Checkout Session. Applies to Checkout Sessions with `ui_mode: embedded` or `ui_mode: custom`. For `ui_mode: embedded`, the client secret is to be used when initializing Stripe.js embedded checkout.
  For `ui_mode: custom`, use the client secret with [initCheckout](https://docs.stripe.com/docs/js/custom_checkout/init.md) on your front end.

- `collected_information` (nullable object)
  Information about the customer collected within the Checkout Session.

  - `collected_information.shipping_details` (nullable object)
    Shipping information for this Checkout Session.

    - `collected_information.shipping_details.address` (object)
      Customer address.

      - `collected_information.shipping_details.address.city` (nullable string)
        City, district, suburb, town, or village.

      - `collected_information.shipping_details.address.country` (nullable string)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `collected_information.shipping_details.address.line1` (nullable string)
        Address line 1 (e.g., street, PO Box, or company name).

      - `collected_information.shipping_details.address.line2` (nullable string)
        Address line 2 (e.g., apartment, suite, unit, or building).

      - `collected_information.shipping_details.address.postal_code` (nullable string)
        ZIP or postal code.

      - `collected_information.shipping_details.address.state` (nullable string)
        State, county, province, or region.

    - `collected_information.shipping_details.name` (string)
      Customer name.

- `consent` (nullable object)
  Results of `consent_collection` for this session.

  - `consent.promotions` (nullable enum)
    If `opt_in`, the customer consents to receiving promotional communications
    from the merchant about this Checkout Session.

  - `consent.terms_of_service` (nullable enum)
    If `accepted`, the customer in this Checkout Session has agreed to the merchant’s terms of service.

    The customer has accepted the specified terms of service agreement.

- `consent_collection` (nullable object)
  When set, provides configuration for the Checkout Session to gather active consent from customers.

  - `consent_collection.payment_method_reuse_agreement` (nullable object)
    If set to `hidden`, it will hide legal text related to the reuse of a payment method.

    - `consent_collection.payment_method_reuse_agreement.position` (enum)
      Determines the position and visibility of the payment method reuse agreement in the UI. When set to `auto`, Stripe’s defaults will be used.

      When set to `hidden`, the payment method reuse agreement text will always be hidden in the UI.

  - `consent_collection.promotions` (nullable enum)
    If set to `auto`, enables the collection of customer consent for promotional communications. The Checkout
    Session will determine whether to display an option to opt into promotional communication
    from the merchant depending on the customer’s locale. Only available to US merchants.

  - `consent_collection.terms_of_service` (nullable enum)
    If set to `required`, it requires customers to accept the terms of service before being able to pay.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (nullable enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `currency_conversion` (nullable object)
  Currency conversion details for [Adaptive Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing) sessions created before 2025-03-31.

  - `currency_conversion.amount_subtotal` (integer)
    Total of all items in source currency before discounts or taxes are applied.

  - `currency_conversion.amount_total` (integer)
    Total of all items in source currency after discounts and taxes are applied.

  - `currency_conversion.fx_rate` (decimal string)
    Exchange rate used to convert source currency amounts to customer currency amounts

  - `currency_conversion.source_currency` (string)
    Creation currency of the CheckoutSession before localization

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

    - `custom_fields.dropdown.value` (nullable string)
      The option selected by the customer. This will be the `value` for the option.

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

    - `custom_fields.numeric.value` (nullable string)
      The value entered by the customer, containing only digits.

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

    - `custom_fields.text.value` (nullable string)
      The value entered by the customer.

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

- `customer` (nullable string)
  The ID of the customer for this Session.
  For Checkout Sessions in `subscription` mode or Checkout Sessions with `customer_creation` set as `always` in `payment` mode, Checkout
  will create a new customer object based on information provided
  during the payment flow unless an existing customer was provided when
  the Session was created.

- `customer_creation` (nullable enum)
  Configure whether a Checkout Session creates a Customer when the Checkout Session completes.

  The Checkout Session will always create a [Customer](https://docs.stripe.com/docs/api/customers.md) when a Session confirmation is attempted.

  The Checkout Session will only create a [Customer](https://docs.stripe.com/docs/api/customers.md) if it is required for Session confirmation.
  Currently, only `subscription` mode Sessions and `payment` mode Sessions with [post-purchase invoices enabled](https://docs.stripe.com/docs/receipts.md?payment-ui=checkout#paid-invoices) require a Customer.

- `customer_details` (nullable object)
  The customer details including the customer’s tax exempt status and the customer’s tax IDs. Customer’s address details are not present on Sessions in `setup` mode.

  - `customer_details.address` (nullable object)
    The customer’s address after a completed Checkout Session. Note: This property is populated only for sessions on or after March 30, 2022.

    - `customer_details.address.city` (nullable string)
      City, district, suburb, town, or village.

    - `customer_details.address.country` (nullable string)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `customer_details.address.line1` (nullable string)
      Address line 1 (e.g., street, PO Box, or company name).

    - `customer_details.address.line2` (nullable string)
      Address line 2 (e.g., apartment, suite, unit, or building).

    - `customer_details.address.postal_code` (nullable string)
      ZIP or postal code.

    - `customer_details.address.state` (nullable string)
      State, county, province, or region.

  - `customer_details.email` (nullable string)
    The email associated with the Customer, if one exists, on the Checkout Session after a completed Checkout Session or at time of session expiry.
    Otherwise, if the customer has consented to promotional content, this value is the most recent valid email provided by the customer on the Checkout form.

  - `customer_details.name` (nullable string)
    The customer’s name after a completed Checkout Session. Note: This property is populated only for sessions on or after March 30, 2022.

  - `customer_details.phone` (nullable string)
    The customer’s phone number after a completed Checkout Session.

  - `customer_details.tax_exempt` (nullable enum)
    The customer’s tax exempt status after a completed Checkout Session.

  - `customer_details.tax_ids` (nullable array of objects)
    The customer’s tax IDs after a completed Checkout Session.

    - `customer_details.tax_ids.type` (enum)
      The type of the tax ID, one of `ad_nrt`, `ar_cuit`, `eu_vat`, `bo_tin`, `br_cnpj`, `br_cpf`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eu_oss_vat`, `hr_oib`, `pe_ruc`, `ro_tin`, `rs_pib`, `sv_nit`, `uy_ruc`, `ve_rif`, `vn_tin`, `gb_vat`, `nz_gst`, `au_abn`, `au_arn`, `in_gst`, `no_vat`, `no_voec`, `za_vat`, `ch_vat`, `mx_rfc`, `sg_uen`, `ru_inn`, `ru_kpp`, `ca_bn`, `hk_br`, `es_cif`, `tw_vat`, `th_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `li_uid`, `li_vat`, `my_itn`, `us_ein`, `kr_brn`, `ca_qst`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `my_sst`, `sg_gst`, `ae_trn`, `cl_tin`, `sa_vat`, `id_npwp`, `my_frp`, `il_vat`, `ge_vat`, `ua_vat`, `is_vat`, `bg_uic`, `hu_tin`, `si_tin`, `ke_pin`, `tr_tin`, `eg_tin`, `ph_tin`, `al_tin`, `bh_vat`, `kz_bin`, `ng_tin`, `om_vat`, `de_stn`, `ch_uid`, `tz_vat`, `uz_vat`, `uz_tin`, `md_vat`, `ma_vat`, `by_tin`, `ao_tin`, `bs_tin`, `bb_tin`, `cd_nif`, `mr_nif`, `me_pib`, `zw_tin`, `ba_tin`, `gn_nif`, `mk_vat`, `sr_fin`, `sn_ninea`, `am_tin`, `np_pan`, `tj_tin`, `ug_tin`, `zm_tin`, `kh_tin`, `aw_tin`, `az_tin`, `bd_bin`, `bj_ifu`, `et_tin`, `kg_tin`, `la_tin`, `cm_niu`, `cv_nif`, `bf_ifu`, or `unknown`

    - `customer_details.tax_ids.value` (nullable string)
      The value of the tax ID.

- `customer_email` (nullable string)
  If provided, this value will be used when the Customer object is created.
  If not provided, customers will be asked to enter their email address.
  Use this parameter to prefill customer data if you already have an email
  on file. To access information about the customer once the payment flow is
  complete, use the `customer` attribute.

- `discounts` (nullable array of objects)
  List of coupons and promotion codes attached to the Checkout Session.

  - `discounts.coupon` (nullable string)
    Coupon attached to the Checkout Session.

  - `discounts.promotion_code` (nullable string)
    Promotion code attached to the Checkout Session.

- `expires_at` (timestamp)
  The timestamp at which the Checkout Session will expire.

- `invoice` (nullable string)
  ID of the invoice created by the Checkout Session, if it exists.

- `invoice_creation` (nullable object)
  Details on the state of invoice creation for the Checkout Session.

  - `invoice_creation.enabled` (boolean)
    Indicates whether invoice creation is enabled for the Checkout Session.

  - `invoice_creation.invoice_data` (object)
    Parameters passed when creating invoices for payment-mode Checkout Sessions.

    - `invoice_creation.invoice_data.account_tax_ids` (nullable array of strings)
      The account tax IDs associated with the invoice.

    - `invoice_creation.invoice_data.custom_fields` (nullable array of objects)
      Custom fields displayed on the invoice.

      - `invoice_creation.invoice_data.custom_fields.name` (string)
        The name of the custom field.

      - `invoice_creation.invoice_data.custom_fields.value` (string)
        The value of the custom field.

    - `invoice_creation.invoice_data.description` (nullable string)
      An arbitrary string attached to the object. Often useful for displaying to users.

    - `invoice_creation.invoice_data.footer` (nullable string)
      Footer displayed on the invoice.

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

- `line_items` (nullable object)
  The line items purchased by the customer.

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

- `locale` (nullable enum)
  The IETF language tag of the locale Checkout is displayed in. If blank or `auto`, the browser’s locale is used.

- `metadata` (nullable object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `mode` (enum)
  The mode of the Checkout Session.

  Accept one-time payments for cards, iDEAL, and more.

  Save payment details to charge your customers later.

  Use Stripe Billing to set up fixed-price subscriptions.

- `optional_items` (nullable array of objects)
  The optional items presented to the customer at checkout.

- `payment_intent` (nullable string)
  The ID of the PaymentIntent for Checkout Sessions in `payment` mode. You can’t confirm or cancel the PaymentIntent for a Checkout Session. To cancel, [expire the Checkout Session](https://docs.stripe.com/docs/api/checkout/sessions/expire.md) instead.

- `payment_link` (nullable string)
  The ID of the Payment Link that created this Session.

- `payment_method_collection` (nullable enum)
  Configure whether a Checkout Session should collect a payment method. Defaults to `always`.

  The Checkout Session will always collect a PaymentMethod.

  The Checkout Session will only collect a PaymentMethod if there is an amount due.

- `payment_method_configuration_details` (nullable object)
  Information about the payment method configuration used for this Checkout session if using dynamic payment methods.

  - `payment_method_configuration_details.id` (string)
    ID of the payment method configuration used.

  - `payment_method_configuration_details.parent` (nullable string)
    ID of the parent payment method configuration used.

- `payment_method_options` (nullable object)
  Payment-method-specific configuration for the PaymentIntent or SetupIntent of this CheckoutSession.

  - `payment_method_options.acss_debit` (nullable object)
    If the Checkout Session’s payment_method_types includes `acss_debit`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.acss_debit.currency` (nullable enum)
      Currency supported by the bank account. Returned when the Session is in `setup` mode.

      Canadian dollars

      US dollars

    - `payment_method_options.acss_debit.mandate_options` (nullable object)
      Additional fields for Mandate creation

      - `payment_method_options.acss_debit.mandate_options.custom_mandate_url` (nullable string)
        A URL for custom mandate text

      - `payment_method_options.acss_debit.mandate_options.default_for` (nullable array of enums)
        List of Stripe products where this mandate can be selected automatically. Returned when the Session is in `setup` mode.

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

    - `payment_method_options.acss_debit.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

      Use `off_session` if your customer may or may not be present in your checkout flow.

      Use `on_session` if you intend to only reuse the payment method when your customer is present in your checkout flow.

    - `payment_method_options.acss_debit.target_date` (nullable string)
      Controls when Stripe will attempt to debit the funds from the customer’s account. The date must be a string in YYYY-MM-DD format. The date must be in the future and between 3 and 15 calendar days from now.

    - `payment_method_options.acss_debit.verification_method` (nullable enum)
      Bank account verification method.

      Instant verification with fallback to microdeposits.

      Instant verification.

      Verification using microdeposits.

  - `payment_method_options.affirm` (nullable object)
    If the Checkout Session’s payment_method_types includes `affirm`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.affirm.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

  - `payment_method_options.afterpay_clearpay` (nullable object)
    If the Checkout Session’s payment_method_types includes `afterpay_clearpay`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.afterpay_clearpay.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

  - `payment_method_options.alipay` (nullable object)
    If the Checkout Session’s payment_method_types includes `alipay`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.alipay.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

  - `payment_method_options.amazon_pay` (nullable object)
    If the Checkout Session’s payment_method_types includes `amazon_pay`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.amazon_pay.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

      Use `off_session` if your customer may or may not be present in your checkout flow.

  - `payment_method_options.au_becs_debit` (nullable object)
    If the Checkout Session’s payment_method_types includes `au_becs_debit`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.au_becs_debit.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

    - `payment_method_options.au_becs_debit.target_date` (nullable string)
      Controls when Stripe will attempt to debit the funds from the customer’s account. The date must be a string in YYYY-MM-DD format. The date must be in the future and between 3 and 15 calendar days from now.

  - `payment_method_options.bacs_debit` (nullable object)
    If the Checkout Session’s payment_method_types includes `bacs_debit`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.bacs_debit.mandate_options` (nullable object)
      Additional fields for Mandate creation

    - `payment_method_options.bacs_debit.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

      Use `off_session` if your customer may or may not be present in your checkout flow.

      Use `on_session` if you intend to only reuse the payment method when your customer is present in your checkout flow.

    - `payment_method_options.bacs_debit.target_date` (nullable string)
      Controls when Stripe will attempt to debit the funds from the customer’s account. The date must be a string in YYYY-MM-DD format. The date must be in the future and between 3 and 15 calendar days from now.

  - `payment_method_options.bancontact` (nullable object)
    If the Checkout Session’s payment_method_types includes `bancontact`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.bancontact.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

  - `payment_method_options.boleto` (nullable object)
    If the Checkout Session’s payment_method_types includes `boleto`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.boleto.expires_after_days` (integer)
      The number of calendar days before a Boleto voucher expires. For example, if you create a Boleto voucher on Monday and you set expires_after_days to 2, the Boleto voucher will expire on Wednesday at 23:59 America/Sao_Paulo time.

    - `payment_method_options.boleto.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

      Use `off_session` if your customer may or may not be present in your checkout flow.

      Use `on_session` if you intend to only reuse the payment method when your customer is present in your checkout flow.

  - `payment_method_options.card` (nullable object)
    If the Checkout Session’s payment_method_types includes `card`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.card.installments` (nullable object)
      Additional fields for Installments configuration

      - `payment_method_options.card.installments.enabled` (nullable boolean)
        Indicates if installments are enabled

    - `payment_method_options.card.request_extended_authorization` (nullable enum)
      Request ability to [capture beyond the standard authorization validity window](https://docs.stripe.com/payments/extended-authorization.md) for this CheckoutSession.

      Use `if_available` if you want to extend the capture window when eligible for extended authorization.

      Use `never` if you don’t want to extend the capture window.

    - `payment_method_options.card.request_incremental_authorization` (nullable enum)
      Request ability to [increment the authorization](https://docs.stripe.com/payments/incremental-authorization.md) for this CheckoutSession.

      Use `if_available` if you want to increment the authorization on the PaymentIntent when eligible.

      Use `never` if you don’t want to increment the authorization on the PaymentIntent.

    - `payment_method_options.card.request_multicapture` (nullable enum)
      Request ability to make [multiple captures](https://docs.stripe.com/payments/multicapture.md) for this CheckoutSession.

      Use `if_available` if you want to use multicapture when eligible.

      Use `never` if you don’t want to use multicapture.

    - `payment_method_options.card.request_overcapture` (nullable enum)
      Request ability to [overcapture](https://docs.stripe.com/payments/overcapture.md) for this CheckoutSession.

      Use `if_available` if you want to overcapture the payment when eligible.

      Use `never` if you don’t want to overcapture the payment.

    - `payment_method_options.card.request_three_d_secure` (enum)
      We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://docs.stripe.com/docs/strong-customer-authentication.md). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. If not provided, this value defaults to `automatic`. Read our guide on [manually requesting 3D Secure](https://docs.stripe.com/docs/payments/3d-secure/authentication-flow.md#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.

      Use `any` to manually request 3DS with a preference for a `frictionless` flow, increasing the likelihood of the authentication being completed without any additional input from the customer.
      3DS will always be attempted if it is supported for the card, but Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow.
      To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

      (Default) Our SCA Engine automatically prompts your customers for authentication based on risk level and other requirements.

      Use `challenge` to request 3DS with a preference for a `challenge` flow, where the customer must respond to a prompt for active authentication. Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow. To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

    - `payment_method_options.card.restrictions` (nullable object)
      Restrictions to apply to the card payment method. For example, you can block specific card brands.

      - `payment_method_options.card.restrictions.brands_blocked` (nullable array of enums)
        Specify the card brands to block in the Checkout Session. If a customer enters or selects a card belonging to a blocked brand, they can’t complete the Session.

    - `payment_method_options.card.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

      Use `off_session` if your customer may or may not be present in your checkout flow.

      Use `on_session` if you intend to only reuse the payment method when your customer is present in your checkout flow.

    - `payment_method_options.card.statement_descriptor_suffix_kana` (nullable string)
      Provides information about a card payment that customers see on their statements. Concatenated with the Kana prefix (shortened Kana descriptor) or Kana statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters. On card statements, the *concatenation* of both prefix and suffix (including separators) will appear truncated to 22 characters.

    - `payment_method_options.card.statement_descriptor_suffix_kanji` (nullable string)
      Provides information about a card payment that customers see on their statements. Concatenated with the Kanji prefix (shortened Kanji descriptor) or Kanji statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 17 characters. On card statements, the *concatenation* of both prefix and suffix (including separators) will appear truncated to 17 characters.

  - `payment_method_options.cashapp` (nullable object)
    If the Checkout Session’s payment_method_types includes `cashapp`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.cashapp.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

  - `payment_method_options.customer_balance` (nullable object)
    If the Checkout Session’s payment_method_types includes `customer_balance`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.customer_balance.bank_transfer` (nullable object)
      Configuration for the bank transfer funding type, if the `funding_type` is set to `bank_transfer`.

      - `payment_method_options.customer_balance.bank_transfer.eu_bank_transfer` (nullable object)
        Configuration for eu_bank_transfer

        - `payment_method_options.customer_balance.bank_transfer.eu_bank_transfer.country` (enum)
          The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.

      - `payment_method_options.customer_balance.bank_transfer.requested_address_types` (nullable array of enums)
        List of address types that should be returned in the financial_addresses response. If not specified, all valid types will be returned.

        Permitted values include: `sort_code`, `zengin`, `iban`, or `spei`.

        aba bank account address type

        iban bank account address type

        sepa bank account address type

        sort_code bank account address type

        spei bank account address type

        swift bank account address type

        zengin bank account address type

      - `payment_method_options.customer_balance.bank_transfer.type` (nullable enum)
        The bank transfer type that this PaymentIntent is allowed to use for funding Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.

        A bank transfer of type eu_bank_transfer

        A bank transfer of type gb_bank_transfer

        A bank transfer of type jp_bank_transfer

        A bank transfer of type mx_bank_transfer

        A bank transfer of type us_bank_transfer

    - `payment_method_options.customer_balance.funding_type` (nullable enum)
      The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`.

    - `payment_method_options.customer_balance.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

  - `payment_method_options.eps` (nullable object)
    If the Checkout Session’s payment_method_types includes `eps`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.eps.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

  - `payment_method_options.fpx` (nullable object)
    If the Checkout Session’s payment_method_types includes `fpx`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.fpx.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

  - `payment_method_options.giropay` (nullable object)
    If the Checkout Session’s payment_method_types includes `giropay`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.giropay.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

  - `payment_method_options.grabpay` (nullable object)
    If the Checkout Session’s payment_method_types includes `grabpay`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.grabpay.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

  - `payment_method_options.ideal` (nullable object)
    If the Checkout Session’s payment_method_types includes `ideal`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.ideal.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

  - `payment_method_options.kakao_pay` (nullable object)
    If the Checkout Session’s payment_method_types includes `kakao_pay`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.kakao_pay.capture_method` (nullable enum)
      Controls when the funds will be captured from the customer’s account.

      Use `manual` if you intend to place the funds on hold and want to override the top-level `capture_method` value for this payment method.

    - `payment_method_options.kakao_pay.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

      Use `off_session` if your customer may or may not be present in your checkout flow.

  - `payment_method_options.klarna` (nullable object)
    If the Checkout Session’s payment_method_types includes `klarna`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.klarna.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

      Use `off_session` if your customer may or may not be present in your checkout flow.

      Use `on_session` if you intend to only reuse the payment method when your customer is present in your checkout flow.

  - `payment_method_options.konbini` (nullable object)
    If the Checkout Session’s payment_method_types includes `konbini`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.konbini.expires_after_days` (nullable integer)
      The number of calendar days (between 1 and 60) after which Konbini payment instructions will expire. For example, if a PaymentIntent is confirmed with Konbini and `expires_after_days` set to 2 on Monday JST, the instructions will expire on Wednesday 23:59:59 JST.

    - `payment_method_options.konbini.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

  - `payment_method_options.kr_card` (nullable object)
    If the Checkout Session’s payment_method_types includes `kr_card`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.kr_card.capture_method` (nullable enum)
      Controls when the funds will be captured from the customer’s account.

      Use `manual` if you intend to place the funds on hold and want to override the top-level `capture_method` value for this payment method.

    - `payment_method_options.kr_card.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

      Use `off_session` if your customer may or may not be present in your checkout flow.

  - `payment_method_options.link` (nullable object)
    If the Checkout Session’s payment_method_types includes `link`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.link.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

      Use `off_session` if your customer may or may not be present in your checkout flow.

  - `payment_method_options.mobilepay` (nullable object)
    If the Checkout Session’s payment_method_types includes `mobilepay`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.mobilepay.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

  - `payment_method_options.multibanco` (nullable object)
    If the Checkout Session’s payment_method_types includes `multibanco`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.multibanco.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

  - `payment_method_options.naver_pay` (nullable object)
    If the Checkout Session’s payment_method_types includes `naver_pay`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.naver_pay.capture_method` (nullable enum)
      Controls when the funds will be captured from the customer’s account.

      Use `manual` if you intend to place the funds on hold and want to override the top-level `capture_method` value for this payment method.

    - `payment_method_options.naver_pay.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

      Use `off_session` if your customer may or may not be present in your checkout flow.

  - `payment_method_options.oxxo` (nullable object)
    If the Checkout Session’s payment_method_types includes `oxxo`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.oxxo.expires_after_days` (integer)
      The number of calendar days before an OXXO invoice expires. For example, if you create an OXXO invoice on Monday and you set expires_after_days to 2, the OXXO invoice will expire on Wednesday at 23:59 America/Mexico_City time.

    - `payment_method_options.oxxo.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

  - `payment_method_options.p24` (nullable object)
    If the Checkout Session’s payment_method_types includes `p24`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.p24.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

  - `payment_method_options.payco` (nullable object)
    If the Checkout Session’s payment_method_types includes `payco`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.payco.capture_method` (nullable enum)
      Controls when the funds will be captured from the customer’s account.

      Use `manual` if you intend to place the funds on hold and want to override the top-level `capture_method` value for this payment method.

  - `payment_method_options.paynow` (nullable object)
    If the Checkout Session’s payment_method_types includes `paynow`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.paynow.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

  - `payment_method_options.paypal` (nullable object)
    If the Checkout Session’s payment_method_types includes `paypal`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.paypal.capture_method` (nullable enum)
      Controls when the funds will be captured from the customer’s account.

      Use `manual` if you intend to place the funds on hold and want to override the top-level `capture_method` value for this payment method.

    - `payment_method_options.paypal.preferred_locale` (nullable string)
      Preferred locale of the PayPal checkout page that the customer is redirected to.

    - `payment_method_options.paypal.reference` (nullable string)
      A reference of the PayPal transaction visible to customer which is mapped to PayPal’s invoice ID. This must be a globally unique ID if you have configured in your PayPal settings to block multiple payments per invoice ID.

    - `payment_method_options.paypal.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

      Use `off_session` if your customer may or may not be present in your checkout flow.

  - `payment_method_options.pix` (nullable object)
    If the Checkout Session’s payment_method_types includes `pix`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.pix.expires_after_seconds` (nullable integer)
      The number of seconds after which Pix payment will expire.

  - `payment_method_options.revolut_pay` (nullable object)
    If the Checkout Session’s payment_method_types includes `revolut_pay`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.revolut_pay.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

      Use `off_session` if your customer may or may not be present in your checkout flow.

  - `payment_method_options.samsung_pay` (nullable object)
    If the Checkout Session’s payment_method_types includes `samsung_pay`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.samsung_pay.capture_method` (nullable enum)
      Controls when the funds will be captured from the customer’s account.

      Use `manual` if you intend to place the funds on hold and want to override the top-level `capture_method` value for this payment method.

  - `payment_method_options.sepa_debit` (nullable object)
    If the Checkout Session’s payment_method_types includes `sepa_debit`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.sepa_debit.mandate_options` (nullable object)
      Additional fields for Mandate creation

    - `payment_method_options.sepa_debit.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

      Use `off_session` if your customer may or may not be present in your checkout flow.

      Use `on_session` if you intend to only reuse the payment method when your customer is present in your checkout flow.

    - `payment_method_options.sepa_debit.target_date` (nullable string)
      Controls when Stripe will attempt to debit the funds from the customer’s account. The date must be a string in YYYY-MM-DD format. The date must be in the future and between 3 and 15 calendar days from now.

  - `payment_method_options.sofort` (nullable object)
    If the Checkout Session’s payment_method_types includes `sofort`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.sofort.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

  - `payment_method_options.swish` (nullable object)
    If the Checkout Session’s payment_method_types includes `swish`, this hash contains the configurations that will be applied to each payment attempt of that type.

    - `payment_method_options.swish.reference` (nullable string)
      The order reference that will be displayed to customers in the Swish application. Defaults to the `id` of the Payment Intent.

  - `payment_method_options.us_bank_account` (nullable object)
    If the Checkout Session’s payment_method_types includes `us_bank_account`, this hash contains the configurations that will be applied to each payment attempt of that type.

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

    - `payment_method_options.us_bank_account.setup_future_usage` (nullable enum)
      Indicates that you intend to make future payments with this PaymentIntent’s payment method.

      If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

      If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

      When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

      Use `none` if you do not intend to reuse this payment method and want to override the top-level `setup_future_usage` value for this payment method.

      Use `off_session` if your customer may or may not be present in your checkout flow.

      Use `on_session` if you intend to only reuse the payment method when your customer is present in your checkout flow.

    - `payment_method_options.us_bank_account.target_date` (nullable string)
      Controls when Stripe will attempt to debit the funds from the customer’s account. The date must be a string in YYYY-MM-DD format. The date must be in the future and between 3 and 15 calendar days from now.

    - `payment_method_options.us_bank_account.verification_method` (nullable enum)
      Bank account verification method.

      Instant verification with fallback to microdeposits.

      Instant verification only.

- `payment_method_types` (array of strings)
  A list of the types of payment methods (e.g. card) this Checkout
  Session is allowed to accept.

- `payment_status` (enum)
  The payment status of the Checkout Session, one of `paid`, `unpaid`, or `no_payment_required`.
  You can use this value to decide when to fulfill your customer’s order.

  The payment is delayed to a future date, or the Checkout Session is in `setup` mode and doesn’t require a payment at this time.

  The payment funds are available in your account.

  The payment funds are not yet available in your account.

- `permissions` (nullable object)
  This property is used to set up permissions for various actions (e.g., update) on the CheckoutSession object.

  For specific permissions, please refer to their dedicated subsections, such as `permissions.update_shipping_details`.

  - `permissions.update_shipping_details` (nullable enum)
    Determines which entity is allowed to update the shipping details.

    Default is `client_only`. Stripe Checkout client will automatically update the shipping details. If set to `server_only`, only your server is allowed to update the shipping details.

    When set to `server_only`, you must add the onShippingDetailsChange event handler when initializing the Stripe Checkout client and manually update the shipping details from your server using the Stripe API.

- `phone_number_collection` (nullable object)
  Details on the state of phone number collection for the session.

  - `phone_number_collection.enabled` (boolean)
    Indicates whether phone number collection is enabled for the session

- `presentment_details` (nullable object)
  A hash containing information about the currency presentation to the customer, including the displayed currency and amount used for conversion from the integration currency.

  - `presentment_details.presentment_amount` (integer)
    Amount intended to be collected by this payment, denominated in presentment_currency.

  - `presentment_details.presentment_currency` (string)
    Currency presented to the customer during payment.

- `recovered_from` (nullable string)
  The ID of the original expired Checkout Session that triggered the recovery flow.

- `redirect_on_completion` (nullable enum)
  This parameter applies to `ui_mode: embedded`. Learn more about the [redirect behavior](https://docs.stripe.com/docs/payments/checkout/custom-success-page.md?payment-ui=embedded-form) of embedded sessions. Defaults to `always`.

  The Session will always redirect to the `return_url` after successful confirmation.

  The Session will only redirect to the `return_url` after a redirect-based payment method is used.

  The Session will never redirect to the `return_url`, and redirect-based payment methods will be disabled.

- `return_url` (nullable string)
  Applies to Checkout Sessions with `ui_mode: embedded` or `ui_mode: custom`. The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method’s app or site.

- `saved_payment_method_options` (nullable object)
  Controls saved payment method settings for the session. Only available in `payment` and `subscription` mode.

  - `saved_payment_method_options.allow_redisplay_filters` (nullable array of enums)
    Uses the `allow_redisplay` value of each saved payment method to filter the set presented to a returning customer. By default, only saved payment methods with ’allow_redisplay: ‘always’ are shown in Checkout.

    When set, Checkout will show eligible saved payment methods with the `allow_redisplay` value of `always`

    When set, Checkout will show eligible saved payment methods with the `allow_redisplay` value of `limited`

    When set, Checkout will show eligible saved payment methods with the `allow_redisplay` value of `unspecified`

  - `saved_payment_method_options.payment_method_remove` (nullable enum)
    Enable customers to choose if they wish to remove their saved payment methods. Disabled by default.

    Removing payment methods will be disabled for this Checkout Session. This is the default option.

    Removing payment methods will be enabled for this Checkout Session.

  - `saved_payment_method_options.payment_method_save` (nullable enum)
    Enable customers to choose if they wish to save their payment method for future use. Disabled by default.

    Saving payment methods will be disabled for this Checkout Session. This is the default option.

    Saving payment methods will be enabled for this Checkout Session.

- `setup_intent` (nullable string)
  The ID of the SetupIntent for Checkout Sessions in `setup` mode. You can’t confirm or cancel the SetupIntent for a Checkout Session. To cancel, [expire the Checkout Session](https://docs.stripe.com/docs/api/checkout/sessions/expire.md) instead.

- `shipping_address_collection` (nullable object)
  When set, provides configuration for Checkout to collect a shipping address from a customer.

  - `shipping_address_collection.allowed_countries` (array of enums)
    An array of two-letter ISO country codes representing which countries Checkout should provide as options for
    shipping locations. Unsupported country codes: `AS, CX, CC, CU, HM, IR, KP, MH, FM, NF, MP, PW, SY, UM, VI`.

- `shipping_cost` (nullable object)
  The details of the customer cost of shipping, including the customer chosen ShippingRate.

  - `shipping_cost.amount_subtotal` (integer)
    Total shipping cost before any discounts or taxes are applied.

  - `shipping_cost.amount_tax` (integer)
    Total tax amount applied due to shipping costs. If no tax was applied, defaults to 0.

  - `shipping_cost.amount_total` (integer)
    Total shipping cost after discounts and taxes are applied.

  - `shipping_cost.shipping_rate` (nullable string)
    The ID of the ShippingRate for this order.

  - `shipping_cost.taxes` (nullable array of objects)
    The taxes applied to the shipping rate.

    - `shipping_cost.taxes.amount` (integer)
      Amount of tax applied for this rate.

    - `shipping_cost.taxes.rate` (object)
      The tax rate applied.

      - `shipping_cost.taxes.rate.id` (string)
        Unique identifier for the object.

      - `shipping_cost.taxes.rate.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `shipping_cost.taxes.rate.active` (boolean)
        Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

      - `shipping_cost.taxes.rate.country` (nullable string)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `shipping_cost.taxes.rate.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `shipping_cost.taxes.rate.description` (nullable string)
        An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

      - `shipping_cost.taxes.rate.display_name` (string)
        The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

      - `shipping_cost.taxes.rate.effective_percentage` (nullable float)
        Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true,
        this percentage reflects the rate actually used to calculate tax based on the product’s taxability
        and whether the user is registered to collect taxes in the corresponding jurisdiction.

      - `shipping_cost.taxes.rate.flat_amount` (nullable object)
        The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

        - `shipping_cost.taxes.rate.flat_amount.amount` (integer)
          Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

        - `shipping_cost.taxes.rate.flat_amount.currency` (string)
          Three-letter ISO currency code, in lowercase.

      - `shipping_cost.taxes.rate.inclusive` (boolean)
        This specifies if the tax rate is inclusive or exclusive.

      - `shipping_cost.taxes.rate.jurisdiction` (nullable string)
        The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

      - `shipping_cost.taxes.rate.jurisdiction_level` (nullable enum)
        The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.

      - `shipping_cost.taxes.rate.livemode` (boolean)
        Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

      - `shipping_cost.taxes.rate.metadata` (nullable object)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `shipping_cost.taxes.rate.percentage` (float)
        Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

      - `shipping_cost.taxes.rate.rate_type` (nullable enum)
        Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.

        A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

        A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

      - `shipping_cost.taxes.rate.state` (nullable string)
        [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

      - `shipping_cost.taxes.rate.tax_type` (nullable enum)
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

    - `shipping_cost.taxes.taxability_reason` (nullable enum)
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

    - `shipping_cost.taxes.taxable_amount` (nullable integer)
      The amount on which tax is calculated, in .

- `shipping_options` (array of objects)
  The shipping rate options applied to this Session.

  - `shipping_options.shipping_amount` (integer)
    A non-negative integer in cents representing how much to charge.

  - `shipping_options.shipping_rate` (string)
    The shipping rate.

- `status` (nullable enum)
  The status of the Checkout Session, one of `open`, `complete`, or `expired`.

  The checkout session is complete. Payment processing may still be in progress

  The checkout session has expired. No further processing will occur

  The checkout session is still in progress. Payment processing has not started

- `submit_type` (nullable enum)
  Describes the type of transaction being performed by Checkout in order to customize
  relevant text on the page, such as the submit button. `submit_type` can only be
  specified on Checkout Sessions in `payment` mode. If blank or `auto`, `pay` is used.

  `pay` will used for `payment` mode sessions and `subscribe` will be used for `subscription` mode sessions

  Recommended when offering bookings. Submit button includes a ‘Book’ label

  Recommended when accepting donations. Submit button includes a ‘Donate’ label

  Submit button includes a ‘Buy’ label

  Submit button includes a ‘Subscribe’ label

- `success_url` (nullable string)
  The URL the customer will be directed to after the payment or
  subscription creation is successful.

- `tax_id_collection` (nullable object)
  Details on the state of tax ID collection for the session.

  - `tax_id_collection.enabled` (boolean)
    Indicates whether tax ID collection is enabled for the session

  - `tax_id_collection.required` (enum)
    Indicates whether a tax ID is required on the payment page

    A tax ID will be required if collection is [supported](https://docs.stripe.com/tax/checkout/tax-ids#supported-types) for the selected billing address country.

    Tax ID collection is never required.

- `total_details` (nullable object)
  Tax and discount details for the computed total amount.

  - `total_details.amount_discount` (integer)
    This is the sum of all the discounts.

  - `total_details.amount_shipping` (nullable integer)
    This is the sum of all the shipping amounts.

  - `total_details.amount_tax` (integer)
    This is the sum of all the tax amounts.

  - `total_details.breakdown` (nullable object)
    Breakdown of individual tax and discount amounts that add up to the totals.

    - `total_details.breakdown.discounts` (array of objects)
      The aggregated discounts.

      - `total_details.breakdown.discounts.amount` (integer)
        The amount discounted.

      - `total_details.breakdown.discounts.discount` (object)
        The discount applied.

        - `total_details.breakdown.discounts.discount.id` (string)
          The ID of the discount object. Discounts cannot be fetched by ID. Use `expand[]=discounts` in API calls to expand discount IDs in an array.

        - `total_details.breakdown.discounts.discount.object` (string)
          String representing the object’s type. Objects of the same type share the same value.

        - `total_details.breakdown.discounts.discount.checkout_session` (nullable string)
          The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode.

        - `total_details.breakdown.discounts.discount.coupon` (object)
          Hash describing the coupon applied to create this discount.

          - `total_details.breakdown.discounts.discount.coupon.id` (string)
            Unique identifier for the object.

          - `total_details.breakdown.discounts.discount.coupon.object` (string)
            String representing the object’s type. Objects of the same type share the same value.

          - `total_details.breakdown.discounts.discount.coupon.amount_off` (nullable integer)
            Amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer.

          - `total_details.breakdown.discounts.discount.coupon.applies_to` (nullable object)
            Contains information about what this coupon applies to.

            - `total_details.breakdown.discounts.discount.coupon.applies_to.products` (array of strings)
              A list of product IDs this coupon applies to

          - `total_details.breakdown.discounts.discount.coupon.created` (timestamp)
            Time at which the object was created. Measured in seconds since the Unix epoch.

          - `total_details.breakdown.discounts.discount.coupon.currency` (nullable enum)
            If `amount_off` has been set, the three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the amount to take off.

          - `total_details.breakdown.discounts.discount.coupon.currency_options` (nullable object)
            Coupons defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

            - `total_details.breakdown.discounts.discount.coupon.currency_options.<currency>.amount_off` (integer)
              Amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer.

          - `total_details.breakdown.discounts.discount.coupon.duration` (enum)
            One of `forever`, `once`, or `repeating`. Describes how long a customer who applies this coupon will get the discount.

            Applies to all charges from a subscription with this coupon applied.

            Applies to the first charge from a subscription with this coupon applied.

            Applies to charges in the first `duration_in_months` months from a subscription with this coupon applied. This value is deprecated and will be replaced in future versions of the API.

          - `total_details.breakdown.discounts.discount.coupon.duration_in_months` (nullable integer)
            If `duration` is `repeating`, the number of months the coupon applies. Null if coupon `duration` is `forever` or `once`.

          - `total_details.breakdown.discounts.discount.coupon.livemode` (boolean)
            Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

          - `total_details.breakdown.discounts.discount.coupon.max_redemptions` (nullable integer)
            Maximum number of times this coupon can be redeemed, in total, across all customers, before it is no longer valid.

          - `total_details.breakdown.discounts.discount.coupon.metadata` (nullable object)
            Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

          - `total_details.breakdown.discounts.discount.coupon.name` (nullable string)
            Name of the coupon displayed to customers on for instance invoices or receipts.

          - `total_details.breakdown.discounts.discount.coupon.percent_off` (nullable float)
            Percent that will be taken off the subtotal of any invoices for this customer for the duration of the coupon. For example, a coupon with percent_off of 50 will make a 100 invoice 50 instead.

          - `total_details.breakdown.discounts.discount.coupon.redeem_by` (nullable timestamp)
            Date after which the coupon can no longer be redeemed.

          - `total_details.breakdown.discounts.discount.coupon.times_redeemed` (integer)
            Number of times this coupon has been applied to a customer.

          - `total_details.breakdown.discounts.discount.coupon.valid` (boolean)
            Taking account of the above properties, whether this coupon can still be applied to a customer.

        - `total_details.breakdown.discounts.discount.customer` (nullable string)
          The ID of the customer associated with this discount.

        - `total_details.breakdown.discounts.discount.end` (nullable timestamp)
          If the coupon has a duration of `repeating`, the date that this discount will end. If the coupon has a duration of `once` or `forever`, this attribute will be null.

        - `total_details.breakdown.discounts.discount.invoice` (nullable string)
          The invoice that the discount’s coupon was applied to, if it was applied directly to a particular invoice.

        - `total_details.breakdown.discounts.discount.invoice_item` (nullable string)
          The invoice item `id` (or invoice line item `id` for invoice line items of type=‘subscription’) that the discount’s coupon was applied to, if it was applied directly to a particular invoice item or invoice line item.

        - `total_details.breakdown.discounts.discount.promotion_code` (nullable string)
          The promotion code applied to create this discount.

        - `total_details.breakdown.discounts.discount.start` (timestamp)
          Date that the coupon was applied.

        - `total_details.breakdown.discounts.discount.subscription` (nullable string)
          The subscription that this coupon is applied to, if it is applied to a particular subscription.

        - `total_details.breakdown.discounts.discount.subscription_item` (nullable string)
          The subscription item that this coupon is applied to, if it is applied to a particular subscription item.

    - `total_details.breakdown.taxes` (array of objects)
      The aggregated tax amounts by rate.

      - `total_details.breakdown.taxes.amount` (integer)
        Amount of tax applied for this rate.

      - `total_details.breakdown.taxes.rate` (object)
        The tax rate applied.

        - `total_details.breakdown.taxes.rate.id` (string)
          Unique identifier for the object.

        - `total_details.breakdown.taxes.rate.object` (string)
          String representing the object’s type. Objects of the same type share the same value.

        - `total_details.breakdown.taxes.rate.active` (boolean)
          Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

        - `total_details.breakdown.taxes.rate.country` (nullable string)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `total_details.breakdown.taxes.rate.created` (timestamp)
          Time at which the object was created. Measured in seconds since the Unix epoch.

        - `total_details.breakdown.taxes.rate.description` (nullable string)
          An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

        - `total_details.breakdown.taxes.rate.display_name` (string)
          The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

        - `total_details.breakdown.taxes.rate.effective_percentage` (nullable float)
          Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true,
          this percentage reflects the rate actually used to calculate tax based on the product’s taxability
          and whether the user is registered to collect taxes in the corresponding jurisdiction.

        - `total_details.breakdown.taxes.rate.flat_amount` (nullable object)
          The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

          - `total_details.breakdown.taxes.rate.flat_amount.amount` (integer)
            Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

          - `total_details.breakdown.taxes.rate.flat_amount.currency` (string)
            Three-letter ISO currency code, in lowercase.

        - `total_details.breakdown.taxes.rate.inclusive` (boolean)
          This specifies if the tax rate is inclusive or exclusive.

        - `total_details.breakdown.taxes.rate.jurisdiction` (nullable string)
          The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

        - `total_details.breakdown.taxes.rate.jurisdiction_level` (nullable enum)
          The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.

        - `total_details.breakdown.taxes.rate.livemode` (boolean)
          Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

        - `total_details.breakdown.taxes.rate.metadata` (nullable object)
          Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

        - `total_details.breakdown.taxes.rate.percentage` (float)
          Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

        - `total_details.breakdown.taxes.rate.rate_type` (nullable enum)
          Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.

          A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

          A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

        - `total_details.breakdown.taxes.rate.state` (nullable string)
          [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

        - `total_details.breakdown.taxes.rate.tax_type` (nullable enum)
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

      - `total_details.breakdown.taxes.taxability_reason` (nullable enum)
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

      - `total_details.breakdown.taxes.taxable_amount` (nullable integer)
        The amount on which tax is calculated, in .

- `ui_mode` (nullable enum)
  The UI mode of the Session. Defaults to `hosted`.

  The Checkout Session will be displayed using [embedded components](https://docs.stripe.com/checkout/custom/quickstart) on your website

  The Checkout Session will be displayed as an embedded form on your website.

  The Checkout Session will be displayed on a hosted page that customers will be redirected to.

- `url` (nullable string)
  The URL to the Checkout Session. Applies to Checkout Sessions with `ui_mode: hosted`. Redirect customers to this URL to take them to Checkout. If you’re using [Custom Domains](https://docs.stripe.com/docs/payments/checkout/custom-domains.md), the URL will use your subdomain. Otherwise, it’ll use `checkout.stripe.com.`
  This value is only present when the session is active.

- `wallet_options` (nullable object)
  Wallet-specific configuration for this Checkout Session.

  - `wallet_options.link` (nullable object)
    This hash contains the configurations that will be applied to the wallet of this type.

    - `wallet_options.link.display` (nullable enum)
      Describes whether Checkout should display Link. Defaults to `auto`.

      The Checkout Session will automatically determine if Link is a supported payment option and display accordingly.

      The Checkout Session will not display Link as a payment option.

### The Checkout Session object

```json
{
  "id": "cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u",
  "object": "checkout.session",
  "after_expiration": null,
  "allow_promotion_codes": null,
  "amount_subtotal": 2198,
  "amount_total": 2198,
  "automatic_tax": {
    "enabled": false,
    "liability": null,
    "status": null
  },
  "billing_address_collection": null,
  "cancel_url": null,
  "client_reference_id": null,
  "consent": null,
  "consent_collection": null,
  "created": 1679600215,
  "currency": "usd",
  "custom_fields": [],
  "custom_text": {
    "shipping_address": null,
    "submit": null
  },
  "customer": null,
  "customer_creation": "if_required",
  "customer_details": null,
  "customer_email": null,
  "expires_at": 1679686615,
  "invoice": null,
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
  "locale": null,
  "metadata": {},
  "mode": "payment",
  "payment_intent": null,
  "payment_link": null,
  "payment_method_collection": "always",
  "payment_method_options": {},
  "payment_method_types": [
    "card"
  ],
  "payment_status": "unpaid",
  "phone_number_collection": {
    "enabled": false
  },
  "recovered_from": null,
  "setup_intent": null,
  "shipping_address_collection": null,
  "shipping_cost": null,
  "shipping_details": null,
  "shipping_options": [],
  "status": "open",
  "submit_type": null,
  "subscription": null,
  "success_url": "https://example.com/success",
  "total_details": {
    "amount_discount": 0,
    "amount_shipping": 0,
    "amount_tax": 0
  },
  "url": "https://checkout.stripe.com/c/pay/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u#fidkdWxOYHwnPyd1blpxYHZxWjA0SDdPUW5JbmFMck1wMmx9N2BLZjFEfGRUNWhqTmJ%2FM2F8bUA2SDRySkFdUV81T1BSV0YxcWJcTUJcYW5rSzN3dzBLPUE0TzRKTTxzNFBjPWZEX1NKSkxpNTVjRjN8VHE0YicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl"
}
```