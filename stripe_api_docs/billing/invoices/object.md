# The Invoice object

- `id` (string)
  Unique identifier for the object. For preview invoices created using the [create preview](https://stripe.com/docs/api/invoices/create_preview) endpoint, this id will be prefixed with `upcoming_in`.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `account_country` (nullable string)
  The country of the business associated with this invoice, most often the business creating the invoice.

- `account_name` (nullable string)
  The public name of the business associated with this invoice, most often the business creating the invoice.

- `account_tax_ids` (nullable array of strings)
  The account tax IDs associated with the invoice. Only editable when the invoice is a draft.

- `amount_due` (integer)
  Final amount due at this time for this invoice. If the invoice’s total is smaller than the minimum charge amount, for example, or if there is account credit that can be applied to the invoice, the `amount_due` may be 0. If there is a positive `starting_balance` for the invoice (the customer owes money), the `amount_due` will also take that into account. The charge that gets generated for the invoice will be for the amount specified in `amount_due`.

- `amount_overpaid` (integer)
  Amount that was overpaid on the invoice. The amount overpaid is credited to the customer’s credit balance.

- `amount_paid` (integer)
  The amount, in , that was paid.

- `amount_remaining` (integer)
  The difference between amount_due and amount_paid, in .

- `amount_shipping` (integer)
  This is the sum of all the shipping amounts.

- `application` (nullable string)
  ID of the Connect Application that created the invoice.

- `attempt_count` (integer)
  Number of payment attempts made for this invoice, from the perspective of the payment retry schedule. Any payment attempt counts as the first attempt, and subsequently only automatic retries increment the attempt count. In other words, manual payment attempts after the first attempt do not affect the retry schedule. If a failure is returned with a non-retryable return code, the invoice can no longer be retried unless a new payment method is obtained. Retries will continue to be scheduled, and attempt_count will continue to increment, but retries will only be executed if a new payment method is obtained.

- `attempted` (boolean)
  Whether an attempt has been made to pay the invoice. An invoice is not attempted until 1 hour after the `invoice.created` webhook, for example, so you might not want to display that invoice as unpaid to your users.

- `auto_advance` (boolean)
  Controls whether Stripe performs [automatic collection](https://docs.stripe.com/docs/invoicing/integration/automatic-advancement-collection.md) of the invoice. If `false`, the invoice’s state doesn’t automatically advance without an explicit action.

- `automatic_tax` (object)
  Settings and latest results for automatic tax lookup for this invoice.

  - `automatic_tax.disabled_reason` (nullable enum)
    If Stripe disabled automatic tax, this enum describes why.

    Stripe’s systems automatically turned off Tax for this invoice when finalizing it with a missing or incomplete location for your customer.

    Stripe’s systems automatically turned off Tax for this invoice due to an internal outage during tax calculation. We expect this to be very rare. Contact support for additional assistance.

  - `automatic_tax.enabled` (boolean)
    Whether Stripe automatically computes tax on this invoice. Note that incompatible invoice items (invoice items with manually specified [tax rates](https://docs.stripe.com/docs/api/tax_rates.md), negative amounts, or `tax_behavior=unspecified`) cannot be added to automatic tax invoices.

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
    The status of the most recent automated tax calculation for this invoice.

    The automatic tax calculation was successful.

    The tax calculation failed, please try again later.

    The location details supplied on the customer aren’t valid or don’t provide enough location information
    to accurately determine tax rates for the customer.

- `automatically_finalizes_at` (nullable timestamp)
  The time when this invoice is currently scheduled to be automatically finalized. The field will be `null` if the invoice is not scheduled to finalize in the future. If the invoice is not in the draft state, this field will always be `null` - see `finalized_at` for the time when an already-finalized invoice was finalized.

- `billing_reason` (nullable enum)
  Indicates the reason why the invoice was created.

  * `manual`: Unrelated to a subscription, for example, created via the invoice editor.
  * `subscription`: No longer in use. Applies to subscriptions from before May 2018 where no distinction was made between updates, cycles, and thresholds.
  * `subscription_create`: A new subscription was created.
  * `subscription_cycle`: A subscription advanced into a new period.
  * `subscription_threshold`: A subscription reached a billing threshold.
  * `subscription_update`: A subscription was updated.
  * `upcoming`: Reserved for simulated invoices, per the upcoming invoice endpoint.

- `collection_method` (enum)
  Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions.

  Attempt payment using the default source attached to the customer.

  Email payment instructions to the customer.

- `confirmation_secret` (nullable object)
  The confirmation secret associated with this invoice. Currently, this contains the client_secret of the PaymentIntent that Stripe creates during invoice finalization.

  - `confirmation_secret.client_secret` (string)
    The client_secret of the payment that Stripe creates for the invoice after finalization.

  - `confirmation_secret.type` (string)
    The type of client_secret. Currently this is always payment_intent, referencing the default payment_intent that Stripe creates during invoice finalization

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `custom_fields` (nullable array of objects)
  Custom fields displayed on the invoice.

  - `custom_fields.name` (string)
    The name of the custom field.

  - `custom_fields.value` (string)
    The value of the custom field.

- `customer` (string)
  The ID of the customer who will be billed.

- `customer_address` (nullable object)
  The customer’s address. Until the invoice is finalized, this field will equal `customer.address`. Once the invoice is finalized, this field will no longer be updated.

  - `customer_address.city` (nullable string)
    City, district, suburb, town, or village.

  - `customer_address.country` (nullable string)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `customer_address.line1` (nullable string)
    Address line 1 (e.g., street, PO Box, or company name).

  - `customer_address.line2` (nullable string)
    Address line 2 (e.g., apartment, suite, unit, or building).

  - `customer_address.postal_code` (nullable string)
    ZIP or postal code.

  - `customer_address.state` (nullable string)
    State, county, province, or region.

- `customer_email` (nullable string)
  The customer’s email. Until the invoice is finalized, this field will equal `customer.email`. Once the invoice is finalized, this field will no longer be updated.

- `customer_name` (nullable string)
  The customer’s name. Until the invoice is finalized, this field will equal `customer.name`. Once the invoice is finalized, this field will no longer be updated.

- `customer_phone` (nullable string)
  The customer’s phone number. Until the invoice is finalized, this field will equal `customer.phone`. Once the invoice is finalized, this field will no longer be updated.

- `customer_shipping` (nullable object)
  The customer’s shipping information. Until the invoice is finalized, this field will equal `customer.shipping`. Once the invoice is finalized, this field will no longer be updated.

  - `customer_shipping.address` (object)
    Customer shipping address.

    - `customer_shipping.address.city` (nullable string)
      City, district, suburb, town, or village.

    - `customer_shipping.address.country` (nullable string)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `customer_shipping.address.line1` (nullable string)
      Address line 1 (e.g., street, PO Box, or company name).

    - `customer_shipping.address.line2` (nullable string)
      Address line 2 (e.g., apartment, suite, unit, or building).

    - `customer_shipping.address.postal_code` (nullable string)
      ZIP or postal code.

    - `customer_shipping.address.state` (nullable string)
      State, county, province, or region.

  - `customer_shipping.name` (string)
    Customer name.

  - `customer_shipping.phone` (nullable string)
    Customer phone (including extension).

- `customer_tax_exempt` (nullable enum)
  The customer’s tax exempt status. Until the invoice is finalized, this field will equal `customer.tax_exempt`. Once the invoice is finalized, this field will no longer be updated.

- `customer_tax_ids` (nullable array of objects)
  The customer’s tax IDs. Until the invoice is finalized, this field will contain the same tax IDs as `customer.tax_ids`. Once the invoice is finalized, this field will no longer be updated.

  - `customer_tax_ids.type` (enum)
    The type of the tax ID, one of `ad_nrt`, `ar_cuit`, `eu_vat`, `bo_tin`, `br_cnpj`, `br_cpf`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eu_oss_vat`, `hr_oib`, `pe_ruc`, `ro_tin`, `rs_pib`, `sv_nit`, `uy_ruc`, `ve_rif`, `vn_tin`, `gb_vat`, `nz_gst`, `au_abn`, `au_arn`, `in_gst`, `no_vat`, `no_voec`, `za_vat`, `ch_vat`, `mx_rfc`, `sg_uen`, `ru_inn`, `ru_kpp`, `ca_bn`, `hk_br`, `es_cif`, `tw_vat`, `th_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `li_uid`, `li_vat`, `my_itn`, `us_ein`, `kr_brn`, `ca_qst`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `my_sst`, `sg_gst`, `ae_trn`, `cl_tin`, `sa_vat`, `id_npwp`, `my_frp`, `il_vat`, `ge_vat`, `ua_vat`, `is_vat`, `bg_uic`, `hu_tin`, `si_tin`, `ke_pin`, `tr_tin`, `eg_tin`, `ph_tin`, `al_tin`, `bh_vat`, `kz_bin`, `ng_tin`, `om_vat`, `de_stn`, `ch_uid`, `tz_vat`, `uz_vat`, `uz_tin`, `md_vat`, `ma_vat`, `by_tin`, `ao_tin`, `bs_tin`, `bb_tin`, `cd_nif`, `mr_nif`, `me_pib`, `zw_tin`, `ba_tin`, `gn_nif`, `mk_vat`, `sr_fin`, `sn_ninea`, `am_tin`, `np_pan`, `tj_tin`, `ug_tin`, `zm_tin`, `kh_tin`, `aw_tin`, `az_tin`, `bd_bin`, `bj_ifu`, `et_tin`, `kg_tin`, `la_tin`, `cm_niu`, `cv_nif`, `bf_ifu`, or `unknown`

  - `customer_tax_ids.value` (nullable string)
    The value of the tax ID.

- `default_payment_method` (nullable string)
  ID of the default payment method for the invoice. It must belong to the customer associated with the invoice. If not set, defaults to the subscription’s default payment method, if any, or to the default payment method in the customer’s invoice settings.

- `default_source` (nullable string)
  ID of the default payment source for the invoice. It must belong to the customer associated with the invoice and be in a chargeable state. If not set, defaults to the subscription’s default source, if any, or to the customer’s default source.

- `default_tax_rates` (array of objects)
  The tax rates applied to this invoice, if any.

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
  An arbitrary string attached to the object. Often useful for displaying to users. Referenced as ‘memo’ in the Dashboard.

- `discounts` (array of strings)
  The discounts applied to the invoice. Line item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount.

- `effective_at` (nullable timestamp)
  The date when this invoice is in effect. Same as `finalized_at` unless overwritten. When defined, this value replaces the system-generated ‘Date of issue’ printed on the invoice PDF and receipt.

- `ending_balance` (nullable integer)
  Ending customer balance after the invoice is finalized. Invoices are finalized approximately an hour after successful webhook delivery or when payment collection is attempted for the invoice. If the invoice has not been finalized yet, this will be null.

- `footer` (nullable string)
  Footer displayed on the invoice.

- `from_invoice` (nullable object)
  Details of the invoice that was cloned. See the [revision documentation](https://docs.stripe.com/docs/invoicing/invoice-revisions.md) for more details.

  - `from_invoice.action` (string)
    The relation between this invoice and the cloned invoice

  - `from_invoice.invoice` (string)
    The invoice that was cloned.

- `hosted_invoice_url` (nullable string)
  The URL for the hosted invoice page, which allows customers to view and pay an invoice. If the invoice has not been finalized yet, this will be null.

- `invoice_pdf` (nullable string)
  The link to download the PDF for the invoice. If the invoice has not been finalized yet, this will be null.

- `issuer` (object)
  The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.

  - `issuer.account` (nullable string)
    The connected account being referenced when `type` is `account`.

  - `issuer.type` (enum)
    Type of the account referenced.

    Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

    Indicates that the account being referenced is the account making the API request.

- `last_finalization_error` (nullable object)
  The error encountered during the previous attempt to finalize the invoice. This field is cleared when the invoice is successfully finalized.

  - `last_finalization_error.advice_code` (nullable string)
    For card errors resulting from a card issuer decline, a short string indicating [how to proceed with an error](https://docs.stripe.com/docs/declines.md#retrying-issuer-declines) if they provide one.

  - `last_finalization_error.code` (nullable string)
    For some errors that could be handled programmatically, a short string indicating the [error code](https://docs.stripe.com/docs/error-codes.md) reported.

  - `last_finalization_error.doc_url` (nullable string)
    A URL to more information about the [error code](https://docs.stripe.com/docs/error-codes.md) reported.

  - `last_finalization_error.message` (nullable string)
    A human-readable message providing more details about the error. For card errors, these messages can be shown to your users.

  - `last_finalization_error.network_advice_code` (nullable string)
    For card errors resulting from a card issuer decline, a 2 digit code which indicates the advice given to merchant by the card network on how to proceed with an error.

  - `last_finalization_error.network_decline_code` (nullable string)
    For card errors resulting from a card issuer decline, a brand specific 2, 3, or 4 digit code which indicates the reason the authorization failed.

  - `last_finalization_error.param` (nullable string)
    If the error is parameter-specific, the parameter related to the error. For example, you can use this to display a message near the correct form field.

  - `last_finalization_error.payment_method_type` (nullable string)
    If the error is specific to the type of payment method, the payment method type that had a problem. This field is only populated for invoice-related errors.

  - `last_finalization_error.type` (enum)
    The type of error returned. One of `api_error`, `card_error`, `idempotency_error`, or `invalid_request_error`

- `latest_revision` (nullable string)
  The ID of the most recent non-draft revision of this invoice

- `lines` (object)
  The individual line items that make up the invoice. `lines` is sorted as follows: (1) pending invoice items (including prorations) in reverse chronological order, (2) subscription items in reverse chronological order, and (3) invoice items added after invoice creation in chronological order.

  - `lines.object` (string)
    String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

  - `lines.data` (array of objects)
    Details about each object.

    - `lines.data.id` (string)
      Unique identifier for the object.

    - `lines.data.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `lines.data.amount` (integer)
      The amount, in .

    - `lines.data.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `lines.data.description` (nullable string)
      An arbitrary string attached to the object. Often useful for displaying to users.

    - `lines.data.discount_amounts` (nullable array of objects)
      The amount of discount calculated per discount for this line item.

      - `lines.data.discount_amounts.amount` (integer)
        The amount, in , of the discount.

      - `lines.data.discount_amounts.discount` (string)
        The discount that was applied to get this discount amount.

    - `lines.data.discountable` (boolean)
      If true, discounts will apply to this line item. Always false for prorations.

    - `lines.data.discounts` (array of strings)
      The discounts applied to the invoice line item. Line item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount.

    - `lines.data.invoice` (nullable string)
      The ID of the invoice that contains this line item.

    - `lines.data.livemode` (boolean)
      Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

    - `lines.data.metadata` (object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Note that for line items with `type=subscription`, `metadata` reflects the current metadata from the subscription associated with the line item, unless the invoice line was directly updated with different metadata after creation.

    - `lines.data.parent` (nullable object)
      The parent that generated this line item.

      - `lines.data.parent.invoice_item_details` (nullable object)
        Details about the invoice item that generated this line item

        - `lines.data.parent.invoice_item_details.invoice_item` (string)
          The invoice item that generated this line item

        - `lines.data.parent.invoice_item_details.proration` (boolean)
          Whether this is a proration

        - `lines.data.parent.invoice_item_details.proration_details` (nullable object)
          Additional details for proration line items

          - `lines.data.parent.invoice_item_details.proration_details.credited_items` (nullable object)
            For a credit proration `line_item`, the original debit line_items to which the credit proration applies.

            - `lines.data.parent.invoice_item_details.proration_details.credited_items.invoice` (string)
              Invoice containing the credited invoice line items

            - `lines.data.parent.invoice_item_details.proration_details.credited_items.invoice_line_items` (array of strings)
              Credited invoice line items

        - `lines.data.parent.invoice_item_details.subscription` (nullable string)
          The subscription that the invoice item belongs to

      - `lines.data.parent.subscription_item_details` (nullable object)
        Details about the subscription item that generated this line item

        - `lines.data.parent.subscription_item_details.invoice_item` (nullable string)
          The invoice item that generated this line item

        - `lines.data.parent.subscription_item_details.proration` (boolean)
          Whether this is a proration

        - `lines.data.parent.subscription_item_details.proration_details` (nullable object)
          Additional details for proration line items

          - `lines.data.parent.subscription_item_details.proration_details.credited_items` (nullable object)
            For a credit proration `line_item`, the original debit line_items to which the credit proration applies.

            - `lines.data.parent.subscription_item_details.proration_details.credited_items.invoice` (string)
              Invoice containing the credited invoice line items

            - `lines.data.parent.subscription_item_details.proration_details.credited_items.invoice_line_items` (array of strings)
              Credited invoice line items

        - `lines.data.parent.subscription_item_details.subscription` (nullable string)
          The subscription that the subscription item belongs to

        - `lines.data.parent.subscription_item_details.subscription_item` (string)
          The subscription item that generated this line item

      - `lines.data.parent.type` (enum)
        The type of parent that generated this line item

        Details of the parent can be found in the `invoice_item_details` hash.

        Details of the parent can be found in the `subscription_item_details` hash.

    - `lines.data.period` (object)
      The period this `line_item` covers. For subscription line items, this is the subscription period. For prorations, this starts when the proration was calculated, and ends at the period end of the subscription. For invoice items, this is the time at which the invoice item was created or the period of the item. If you have [Stripe Revenue Recognition](https://docs.stripe.com/docs/revenue-recognition.md) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://docs.stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing.md) for details.

      - `lines.data.period.end` (timestamp)
        The end of the period, which must be greater than or equal to the start. This value is inclusive.

      - `lines.data.period.start` (timestamp)
        The start of the period. This value is inclusive.

    - `lines.data.pretax_credit_amounts` (nullable array of objects)
      Contains pretax credit amounts (ex: discount, credit grants, etc) that apply to this line item.

      - `lines.data.pretax_credit_amounts.amount` (integer)
        The amount, in , of the pretax credit amount.

      - `lines.data.pretax_credit_amounts.credit_balance_transaction` (nullable string)
        The credit balance transaction that was applied to get this pretax credit amount.

      - `lines.data.pretax_credit_amounts.discount` (nullable string)
        The discount that was applied to get this pretax credit amount.

      - `lines.data.pretax_credit_amounts.type` (enum)
        Type of the pretax credit amount referenced.

        The pretax credit amount is from a credit balance transaction.

        The pretax credit amount is from a discount.

    - `lines.data.pricing` (nullable object)
      The pricing information of the line item.

      - `lines.data.pricing.price_details` (nullable object)
        Additional details about the price this item is associated with. This is present only when the `type` is `price_details`

        - `lines.data.pricing.price_details.price` (string)
          The ID of the price this item is associated with.

        - `lines.data.pricing.price_details.product` (string)
          The ID of the product this item is associated with.

      - `lines.data.pricing.type` (enum)
        The type of the pricing details.

      - `lines.data.pricing.unit_amount_decimal` (nullable decimal string)
        The unit amount (in the `currency` specified) of the item which contains a decimal value with at most 12 decimal places.

    - `lines.data.quantity` (nullable integer)
      The quantity of the subscription, if the line item is a subscription or a proration.

    - `lines.data.taxes` (nullable array of objects)
      The tax information of the line item.

      - `lines.data.taxes.amount` (integer)
        The amount of the tax, in .

      - `lines.data.taxes.tax_behavior` (enum)
        Whether this tax is inclusive or exclusive.

      - `lines.data.taxes.tax_rate_details` (nullable object)
        Additional details about the tax rate. Only present when `type` is `tax_rate_details`.

      - `lines.data.taxes.taxability_reason` (enum)
        The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.

        No tax is applied as the customer is exempt from tax.

        The reasoning behind this tax is not available.

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

      - `lines.data.taxes.taxable_amount` (nullable integer)
        The amount on which tax is calculated, in .

      - `lines.data.taxes.type` (enum)
        The type of tax information.

  - `lines.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `lines.url` (string)
    The URL where this list can be accessed.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (nullable object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `next_payment_attempt` (nullable timestamp)
  The time at which payment will next be attempted. This value will be `null` for invoices where `collection_method=send_invoice`.

- `number` (nullable string)
  A unique, identifying string that appears on emails sent to the customer for this invoice. This starts with the customer’s unique invoice_prefix if it is specified.

- `on_behalf_of` (nullable string)
  The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://docs.stripe.com/docs/billing/invoices/connect.md) documentation for details.

- `parent` (nullable object)
  The parent that generated this invoice

  - `parent.quote_details` (nullable object)
    Details about the quote that generated this invoice

    - `parent.quote_details.quote` (string)
      The quote that generated this invoice

  - `parent.subscription_details` (nullable object)
    Details about the subscription that generated this invoice

    - `parent.subscription_details.metadata` (nullable object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) defined as subscription metadata when an invoice is created. Becomes an immutable snapshot of the subscription metadata at the time of invoice finalization.
      *Note: This attribute is populated only for invoices created on or after June 29, 2023.*

    - `parent.subscription_details.subscription` (string)
      The subscription that generated this invoice

    - `parent.subscription_details.subscription_proration_date` (nullable timestamp)
      Only set for upcoming invoices that preview prorations. The time used to calculate prorations.

  - `parent.type` (enum)
    The type of parent that generated this invoice

    Details of the parent can be found in the `quote_details` hash.

    Details of the parent can be found in the `subscription_details` hash.

- `payment_settings` (object)
  Configuration settings for the PaymentIntent that is generated when the invoice is finalized.

  - `payment_settings.default_mandate` (nullable string)
    ID of the mandate to be used for this invoice. It must correspond to the payment method used to pay the invoice, including the invoice’s default_payment_method or default_source, if set.

  - `payment_settings.payment_method_options` (nullable object)
    Payment-method-specific configuration to provide to the invoice’s PaymentIntent.

    - `payment_settings.payment_method_options.acss_debit` (nullable object)
      If paying by `acss_debit`, this sub-hash contains details about the Canadian pre-authorized debit payment method options to pass to the invoice’s PaymentIntent.

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
      If paying by `bancontact`, this sub-hash contains details about the Bancontact payment method options to pass to the invoice’s PaymentIntent.

      - `payment_settings.payment_method_options.bancontact.preferred_language` (enum)
        Preferred language of the Bancontact authorization page that the customer is redirected to.

        German

        English

        French

        Dutch

    - `payment_settings.payment_method_options.card` (nullable object)
      If paying by `card`, this sub-hash contains details about the Card payment method options to pass to the invoice’s PaymentIntent.

      - `payment_settings.payment_method_options.card.installments` (nullable object)
        Installment details for this Invoice.

        For more information, see the [installments integration guide](https://docs.stripe.com/docs/payments/installments.md).

        - `payment_settings.payment_method_options.card.installments.enabled` (nullable boolean)
          Whether Installments are enabled for this Invoice.

      - `payment_settings.payment_method_options.card.request_three_d_secure` (nullable enum)
        We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://docs.stripe.com/docs/strong-customer-authentication.md). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Read our guide on [manually requesting 3D Secure](https://docs.stripe.com/docs/payments/3d-secure/authentication-flow.md#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.

        Use `any` to manually request 3DS with a preference for a `frictionless` flow, increasing the likelihood of the authentication being completed without any additional input from the customer.
        3DS will always be attempted if it is supported for the card, but Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow.
        To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

        (Default) Our SCA Engine automatically prompts your customers for authentication based on risk level and other requirements.

        Use `challenge` to request 3DS with a preference for a `challenge` flow, where the customer must respond to a prompt for active authentication. Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow. To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

    - `payment_settings.payment_method_options.customer_balance` (nullable object)
      If paying by `customer_balance`, this sub-hash contains details about the Bank transfer payment method options to pass to the invoice’s PaymentIntent.

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
      If paying by `konbini`, this sub-hash contains details about the Konbini payment method options to pass to the invoice’s PaymentIntent.

    - `payment_settings.payment_method_options.sepa_debit` (nullable object)
      If paying by `sepa_debit`, this sub-hash contains details about the SEPA Direct Debit payment method options to pass to the invoice’s PaymentIntent.

    - `payment_settings.payment_method_options.us_bank_account` (nullable object)
      If paying by `us_bank_account`, this sub-hash contains details about the ACH direct debit payment method options to pass to the invoice’s PaymentIntent.

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
    The list of payment method types (e.g. card) to provide to the invoice’s PaymentIntent. If not set, Stripe attempts to automatically determine the types to use by looking at the invoice’s default payment method, the subscription’s default payment method, the customer’s default payment method, and your [invoice template settings](https://dashboard.stripe.com/settings/billing/invoice).

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

- `payments` (object)
  Payments for this invoice

  - `payments.object` (string)
    String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

  - `payments.data` (array of objects)
    Details about each object.

    - `payments.data.id` (string)
      Unique identifier for the object.

    - `payments.data.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `payments.data.amount_paid` (nullable integer)
      Amount that was actually paid for this invoice, in . This field is null until the payment is `paid`. This amount can be less than the `amount_requested` if the PaymentIntent’s `amount_received` is not sufficient to pay all of the invoices that it is attached to.

    - `payments.data.amount_requested` (integer)
      Amount intended to be paid toward this invoice, in 

    - `payments.data.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `payments.data.currency` (string)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `payments.data.invoice` (string)
      The invoice that was paid.

    - `payments.data.is_default` (boolean)
      Stripe automatically creates a default InvoicePayment when the invoice is finalized, and keeps it synchronized with the invoice’s `amount_remaining`. The PaymentIntent associated with the default payment can’t be edited or canceled directly.

    - `payments.data.livemode` (boolean)
      Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

    - `payments.data.payment` (object)
      The details on the payment.

      - `payments.data.payment.charge` (nullable string)
        ID of the successful charge for this payment when `type` is `charge`.Note: charge is only surfaced if the charge object is not associated with a payment intent. If the charge object does have a payment intent, the Invoice Payment surfaces the payment intent instead.

      - `payments.data.payment.payment_intent` (nullable string)
        ID of the PaymentIntent associated with this payment when `type` is `payment_intent`. Note: This property is only populated for invoices finalized on or after March 15th, 2019.

      - `payments.data.payment.type` (enum)
        Type of payment object associated with this invoice payment.

    - `payments.data.status` (string)
      The status of the payment, one of `open`, `paid`, or `canceled`.

    - `payments.data.status_transitions` (object)
      The timestamps when the payment’s status was updated.

      - `payments.data.status_transitions.canceled_at` (nullable timestamp)
        The time that the payment was canceled.

      - `payments.data.status_transitions.paid_at` (nullable timestamp)
        The time that the payment succeeded.

  - `payments.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `payments.url` (string)
    The URL where this list can be accessed.

- `period_end` (timestamp)
  End of the usage period during which invoice items were added to this invoice. This looks back one period for a subscription invoice. Use the [line item period](https://docs.stripe.com/api/invoices/line_item.md#invoice_line_item_object-period) to get the service period for each price.

- `period_start` (timestamp)
  Start of the usage period during which invoice items were added to this invoice. This looks back one period for a subscription invoice. Use the [line item period](https://docs.stripe.com/api/invoices/line_item.md#invoice_line_item_object-period) to get the service period for each price.

- `post_payment_credit_notes_amount` (integer)
  Total amount of all post-payment credit notes issued for this invoice.

- `pre_payment_credit_notes_amount` (integer)
  Total amount of all pre-payment credit notes issued for this invoice.

- `receipt_number` (nullable string)
  This is the transaction number that appears on email receipts sent for this invoice.

- `rendering` (nullable object)
  The rendering-related settings that control how the invoice is displayed on customer-facing surfaces such as PDF and Hosted Invoice Page.

  - `rendering.amount_tax_display` (nullable string)
    How line-item prices and amounts will be displayed with respect to tax on invoice PDFs.

  - `rendering.pdf` (nullable object)
    Invoice pdf rendering options

    - `rendering.pdf.page_size` (nullable enum)
      Page size of invoice pdf. Options include a4, letter, and auto. If set to auto, page size will be switched to a4 or letter based on customer locale.

  - `rendering.template` (nullable string)
    ID of the rendering template that the invoice is formatted by.

  - `rendering.template_version` (nullable integer)
    Version of the rendering template that the invoice is using.

- `shipping_cost` (nullable object)
  The details of the cost of shipping, including the ShippingRate applied on the invoice.

  - `shipping_cost.amount_subtotal` (integer)
    Total shipping cost before any taxes are applied.

  - `shipping_cost.amount_tax` (integer)
    Total tax amount applied due to shipping costs. If no tax was applied, defaults to 0.

  - `shipping_cost.amount_total` (integer)
    Total shipping cost after taxes are applied.

  - `shipping_cost.shipping_rate` (nullable string)
    The ID of the ShippingRate for this invoice.

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

- `shipping_details` (nullable object)
  Shipping details for the invoice. The Invoice PDF will use the `shipping_details` value if it is set, otherwise the PDF will render the shipping address from the customer.

  - `shipping_details.address` (object)
    Shipping address.

    - `shipping_details.address.city` (nullable string)
      City, district, suburb, town, or village.

    - `shipping_details.address.country` (nullable string)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `shipping_details.address.line1` (nullable string)
      Address line 1 (e.g., street, PO Box, or company name).

    - `shipping_details.address.line2` (nullable string)
      Address line 2 (e.g., apartment, suite, unit, or building).

    - `shipping_details.address.postal_code` (nullable string)
      ZIP or postal code.

    - `shipping_details.address.state` (nullable string)
      State, county, province, or region.

  - `shipping_details.name` (string)
    Recipient name.

  - `shipping_details.phone` (nullable string)
    Recipient phone (including extension).

- `starting_balance` (integer)
  Starting customer balance before the invoice is finalized. If the invoice has not been finalized yet, this will be the current customer balance. For revision invoices, this also includes any customer balance that was applied to the original invoice.

- `statement_descriptor` (nullable string)
  Extra information about an invoice for the customer’s credit card statement.

- `status` (nullable enum)
  The status of the invoice, one of `draft`, `open`, `paid`, `uncollectible`, or `void`. [Learn more](https://docs.stripe.com/docs/billing/invoices/workflow.md#workflow-overview)

- `status_transitions` (object)
  The timestamps at which the invoice status was updated.

  - `status_transitions.finalized_at` (nullable timestamp)
    The time that the invoice draft was finalized.

  - `status_transitions.marked_uncollectible_at` (nullable timestamp)
    The time that the invoice was marked uncollectible.

  - `status_transitions.paid_at` (nullable timestamp)
    The time that the invoice was paid.

  - `status_transitions.voided_at` (nullable timestamp)
    The time that the invoice was voided.

- `subtotal` (integer)
  Total of all subscriptions, invoice items, and prorations on the invoice before any invoice level discount or exclusive tax is applied. Item discounts are already incorporated

- `subtotal_excluding_tax` (nullable integer)
  The integer amount in  representing the subtotal of the invoice before any invoice level discount or tax is applied. Item discounts are already incorporated

- `test_clock` (nullable string)
  ID of the test clock this invoice belongs to.

- `threshold_reason` (nullable object)
  If `billing_reason` is set to `subscription_threshold` this returns more information on which threshold rules triggered the invoice.

  - `threshold_reason.amount_gte` (nullable integer)
    The total invoice amount threshold boundary if it triggered the threshold invoice.

  - `threshold_reason.item_reasons` (array of objects)
    Indicates which line items triggered a threshold invoice.

    - `threshold_reason.item_reasons.line_item_ids` (array of strings)
      The IDs of the line items that triggered the threshold invoice.

    - `threshold_reason.item_reasons.usage_gte` (integer)
      The quantity threshold boundary that applied to the given line item.

- `total` (integer)
  Total after discounts and taxes.

- `total_discount_amounts` (nullable array of objects)
  The aggregate amounts calculated per discount across all line items.

  - `total_discount_amounts.amount` (integer)
    The amount, in , of the discount.

  - `total_discount_amounts.discount` (string)
    The discount that was applied to get this discount amount.

- `total_excluding_tax` (nullable integer)
  The integer amount in  representing the total amount of the invoice including all discounts but excluding all tax.

- `total_pretax_credit_amounts` (nullable array of objects)
  Contains pretax credit amounts (ex: discount, credit grants, etc) that apply to this invoice. This is a combined list of total_pretax_credit_amounts across all invoice line items.

  - `total_pretax_credit_amounts.amount` (integer)
    The amount, in , of the pretax credit amount.

  - `total_pretax_credit_amounts.credit_balance_transaction` (nullable string)
    The credit balance transaction that was applied to get this pretax credit amount.

  - `total_pretax_credit_amounts.discount` (nullable string)
    The discount that was applied to get this pretax credit amount.

  - `total_pretax_credit_amounts.type` (enum)
    Type of the pretax credit amount referenced.

    The pretax credit amount is from a credit balance transaction.

    The pretax credit amount is from a discount.

- `total_taxes` (nullable array of objects)
  The aggregate tax information of all line items.

  - `total_taxes.amount` (integer)
    The amount of the tax, in .

  - `total_taxes.tax_behavior` (enum)
    Whether this tax is inclusive or exclusive.

  - `total_taxes.tax_rate_details` (nullable object)
    Additional details about the tax rate. Only present when `type` is `tax_rate_details`.

  - `total_taxes.taxability_reason` (enum)
    The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.

    No tax is applied as the customer is exempt from tax.

    The reasoning behind this tax is not available.

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

  - `total_taxes.taxable_amount` (nullable integer)
    The amount on which tax is calculated, in .

  - `total_taxes.type` (enum)
    The type of tax information.

- `webhooks_delivered_at` (nullable timestamp)
  Invoices are automatically paid or sent 1 hour after webhooks are delivered, or until all webhook delivery attempts have [been exhausted](https://docs.stripe.com/docs/billing/webhooks.md#understand). This field tracks the time when webhooks for this invoice were successfully delivered. If the invoice had no webhooks to deliver, this will be set while the invoice is being created.

### The Invoice object

```json
{
  "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",
  "object": "invoice",
  "account_country": "US",
  "account_name": "Stripe Docs",
  "account_tax_ids": null,
  "amount_due": 0,
  "amount_paid": 0,
  "amount_overpaid": 0,
  "amount_remaining": 0,
  "amount_shipping": 0,
  "application": null,
  "attempt_count": 0,
  "attempted": false,
  "auto_advance": false,
  "automatic_tax": {
    "enabled": false,
    "liability": null,
    "status": null
  },
  "billing_reason": "manual",
  "collection_method": "charge_automatically",
  "created": 1680644467,
  "currency": "usd",
  "custom_fields": null,
  "customer": "cus_NeZwdNtLEOXuvB",
  "customer_address": null,
  "customer_email": "jennyrosen@example.com",
  "customer_name": "Jenny Rosen",
  "customer_phone": null,
  "customer_shipping": null,
  "customer_tax_exempt": "none",
  "customer_tax_ids": [],
  "confirmation_secret": null,
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discounts": [],
  "due_date": null,
  "ending_balance": null,
  "footer": null,
  "from_invoice": null,
  "hosted_invoice_url": null,
  "invoice_pdf": null,
  "issuer": {
    "type": "self"
  },
  "last_finalization_error": null,
  "latest_revision": null,
  "lines": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"
  },
  "payments": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/invoice_payments"
  },
  "livemode": false,
  "metadata": {},
  "next_payment_attempt": null,
  "number": null,
  "on_behalf_of": null,
  "parent": null,
  "payment_settings": {
    "default_mandate": null,
    "payment_method_options": null,
    "payment_method_types": null
  },
  "period_end": 1680644467,
  "period_start": 1680644467,
  "post_payment_credit_notes_amount": 0,
  "pre_payment_credit_notes_amount": 0,
  "receipt_number": null,
  "shipping_cost": null,
  "shipping_details": null,
  "starting_balance": 0,
  "statement_descriptor": null,
  "status": "draft",
  "status_transitions": {
    "finalized_at": null,
    "marked_uncollectible_at": null,
    "paid_at": null,
    "voided_at": null
  },
  "subtotal": 0,
  "subtotal_excluding_tax": 0,
  "test_clock": null,
  "total": 0,
  "total_discount_amounts": [],
  "total_excluding_tax": 0,
  "total_taxes": [],
  "transfer_data": null,
  "webhooks_delivered_at": 1680644467
}
```