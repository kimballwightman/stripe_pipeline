# The Credit Note object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  The integer amount in  representing the total amount of the credit note, including tax.

- `amount_shipping` (integer)
  This is the sum of all the shipping amounts.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `customer` (string)
  ID of the customer.

- `customer_balance_transaction` (nullable string)
  Customer balance transaction related to this credit note.

- `discount_amount` (integer)
  The integer amount in  representing the total amount of discount that was credited.

- `discount_amounts` (array of objects)
  The aggregate amounts calculated per discount for all line items.

  - `discount_amounts.amount` (integer)
    The amount, in , of the discount.

  - `discount_amounts.discount` (string)
    The discount that was applied to get this discount amount.

- `effective_at` (nullable timestamp)
  The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated ‘Date of issue’ printed on the credit note PDF.

- `invoice` (string)
  ID of the invoice.

- `lines` (object)
  Line items that make up the credit note

  - `lines.object` (string)
    String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

  - `lines.data` (array of objects)
    Details about each object.

    - `lines.data.id` (string)
      Unique identifier for the object.

    - `lines.data.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `lines.data.amount` (integer)
      The integer amount in  representing the gross amount being credited for this line item, excluding (exclusive) tax and discounts.

    - `lines.data.description` (nullable string)
      Description of the item being credited.

    - `lines.data.discount_amount` (integer)
      The integer amount in  representing the discount being credited for this line item.

    - `lines.data.discount_amounts` (array of objects)
      The amount of discount calculated per discount for this line item

      - `lines.data.discount_amounts.amount` (integer)
        The amount, in , of the discount.

      - `lines.data.discount_amounts.discount` (string)
        The discount that was applied to get this discount amount.

    - `lines.data.invoice_line_item` (nullable string)
      ID of the invoice line item being credited

    - `lines.data.livemode` (boolean)
      Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

    - `lines.data.pretax_credit_amounts` (array of objects)
      The pretax credit amounts (ex: discount, credit grants, etc) for this line item.

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

    - `lines.data.quantity` (nullable integer)
      The number of units of product being credited.

    - `lines.data.tax_rates` (array of objects)
      The tax rates which apply to the line item.

      - `lines.data.tax_rates.id` (string)
        Unique identifier for the object.

      - `lines.data.tax_rates.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `lines.data.tax_rates.active` (boolean)
        Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

      - `lines.data.tax_rates.country` (nullable string)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `lines.data.tax_rates.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `lines.data.tax_rates.description` (nullable string)
        An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

      - `lines.data.tax_rates.display_name` (string)
        The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

      - `lines.data.tax_rates.effective_percentage` (nullable float)
        Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true,
        this percentage reflects the rate actually used to calculate tax based on the product’s taxability
        and whether the user is registered to collect taxes in the corresponding jurisdiction.

      - `lines.data.tax_rates.flat_amount` (nullable object)
        The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

        - `lines.data.tax_rates.flat_amount.amount` (integer)
          Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

        - `lines.data.tax_rates.flat_amount.currency` (string)
          Three-letter ISO currency code, in lowercase.

      - `lines.data.tax_rates.inclusive` (boolean)
        This specifies if the tax rate is inclusive or exclusive.

      - `lines.data.tax_rates.jurisdiction` (nullable string)
        The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

      - `lines.data.tax_rates.jurisdiction_level` (nullable enum)
        The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.

      - `lines.data.tax_rates.livemode` (boolean)
        Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

      - `lines.data.tax_rates.metadata` (nullable object)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `lines.data.tax_rates.percentage` (float)
        Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

      - `lines.data.tax_rates.rate_type` (nullable enum)
        Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.

        A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

        A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

      - `lines.data.tax_rates.state` (nullable string)
        [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

      - `lines.data.tax_rates.tax_type` (nullable enum)
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

    - `lines.data.type` (enum)
      The type of the credit note line item, one of `invoice_line_item` or `custom_line_item`. When the type is `invoice_line_item` there is an additional `invoice_line_item` property on the resource the value of which is the id of the credited line item on the invoice.

    - `lines.data.unit_amount` (nullable integer)
      The cost of each unit of product being credited.

    - `lines.data.unit_amount_decimal` (nullable decimal string)
      Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

  - `lines.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `lines.url` (string)
    The URL where this list can be accessed.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `memo` (nullable string)
  Customer-facing text that appears on the credit note PDF.

- `metadata` (nullable object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `number` (string)
  A unique number that identifies this particular credit note and appears on the PDF of the credit note and its associated invoice.

- `out_of_band_amount` (nullable integer)
  Amount that was credited outside of Stripe.

- `pdf` (string)
  The link to download the PDF of the credit note.

- `post_payment_amount` (integer)
  The amount of the credit note that was refunded to the customer, credited to the customer’s balance, credited outside of Stripe, or any combination thereof.

- `pre_payment_amount` (integer)
  The amount of the credit note by which the invoice’s `amount_remaining` and `amount_due` were reduced.

- `pretax_credit_amounts` (array of objects)
  The pretax credit amounts (ex: discount, credit grants, etc) for all line items.

  - `pretax_credit_amounts.amount` (integer)
    The amount, in , of the pretax credit amount.

  - `pretax_credit_amounts.credit_balance_transaction` (nullable string)
    The credit balance transaction that was applied to get this pretax credit amount.

  - `pretax_credit_amounts.discount` (nullable string)
    The discount that was applied to get this pretax credit amount.

  - `pretax_credit_amounts.type` (enum)
    Type of the pretax credit amount referenced.

    The pretax credit amount is from a credit balance transaction.

    The pretax credit amount is from a discount.

- `reason` (nullable enum)
  Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`

  Credit issued for a duplicate payment or charge

  Credit note issued for fraudulent activity

  Credit note issued for order change

  Credit note issued for unsatisfactory product

- `refunds` (array of objects)
  Refunds related to this credit note.

  - `refunds.amount_refunded` (integer)
    Amount of the refund that applies to this credit note, in .

  - `refunds.refund` (string)
    ID of the refund.

- `shipping_cost` (nullable object)
  The details of the cost of shipping, including the ShippingRate applied to the invoice.

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

- `status` (enum)
  Status of this credit note, one of `issued` or `void`. Learn more about [voiding credit notes](https://docs.stripe.com/docs/billing/invoices/credit-notes.md#voiding).

  The credit note has been issued.

  The credit note has been voided.

- `subtotal` (integer)
  The integer amount in  representing the amount of the credit note, excluding exclusive tax and invoice level discounts.

- `subtotal_excluding_tax` (nullable integer)
  The integer amount in  representing the amount of the credit note, excluding all tax and invoice level discounts.

- `total` (integer)
  The integer amount in  representing the total amount of the credit note, including tax and all discount.

- `total_excluding_tax` (nullable integer)
  The integer amount in  representing the total amount of the credit note, excluding tax, but including discounts.

- `total_taxes` (nullable array of objects)
  The aggregate tax information for all line items.

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

- `type` (enum)
  Type of this credit note, one of `pre_payment` or `post_payment`. A `pre_payment` credit note means it was issued when the invoice was open. A `post_payment` credit note means it was issued when the invoice was paid.

- `voided_at` (nullable timestamp)
  The time that the credit note was voided.

### The Credit Note object

```json
{
  "id": "cn_1MxvRqLkdIwHu7ixY0xbUcxk",
  "object": "credit_note",
  "amount": 1099,
  "amount_shipping": 0,
  "created": 1681750958,
  "currency": "usd",
  "customer": "cus_NjLgPhUokHubJC",
  "customer_balance_transaction": null,
  "discount_amount": 0,
  "discount_amounts": [],
  "invoice": "in_1MxvRkLkdIwHu7ixABNtI99m",
  "lines": {
    "object": "list",
    "data": [
      {
        "id": "cnli_1MxvRqLkdIwHu7ixFpdhBFQf",
        "object": "credit_note_line_item",
        "amount": 1099,
        "description": "T-shirt",
        "discount_amount": 0,
        "discount_amounts": [],
        "invoice_line_item": "il_1MxvRlLkdIwHu7ixnkbntxUV",
        "livemode": false,
        "quantity": 1,
        "tax_rates": [],
        "taxes": [],
        "type": "invoice_line_item",
        "unit_amount": 1099,
        "unit_amount_decimal": "1099"
      }
    ],
    "has_more": false,
    "url": "/v1/credit_notes/cn_1MxvRqLkdIwHu7ixY0xbUcxk/lines"
  },
  "livemode": false,
  "memo": null,
  "metadata": {},
  "number": "C9E0C52C-0036-CN-01",
  "out_of_band_amount": null,
  "pdf": "https://pay.stripe.com/credit_notes/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9Oak9FOUtQNFlPdk52UXhFd2Z4SU45alpEd21kd0Y4LDcyMjkxNzU50200cROQsSK2/pdf?s=ap",
  "pre_payment_amount": 1099,
  "post_payment_amount": 0,
  "reason": null,
  "refunds": [],
  "shipping_cost": null,
  "status": "issued",
  "subtotal": 1099,
  "subtotal_excluding_tax": 1099,
  "total": 1099,
  "total_excluding_tax": 1099,
  "total_taxes": [],
  "type": "pre_payment",
  "voided_at": null
}
```