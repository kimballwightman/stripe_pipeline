# The Credit Note Line Item object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  The integer amount in  representing the gross amount being credited for this line item, excluding (exclusive) tax and discounts.

- `description` (nullable string)
  Description of the item being credited.

- `discount_amount` (integer)
  The integer amount in  representing the discount being credited for this line item.

- `discount_amounts` (array of objects)
  The amount of discount calculated per discount for this line item

  - `discount_amounts.amount` (integer)
    The amount, in , of the discount.

  - `discount_amounts.discount` (string)
    The discount that was applied to get this discount amount.

- `invoice_line_item` (nullable string)
  ID of the invoice line item being credited

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `pretax_credit_amounts` (array of objects)
  The pretax credit amounts (ex: discount, credit grants, etc) for this line item.

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

- `quantity` (nullable integer)
  The number of units of product being credited.

- `tax_rates` (array of objects)
  The tax rates which apply to the line item.

  - `tax_rates.id` (string)
    Unique identifier for the object.

  - `tax_rates.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `tax_rates.active` (boolean)
    Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

  - `tax_rates.country` (nullable string)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `tax_rates.created` (timestamp)
    Time at which the object was created. Measured in seconds since the Unix epoch.

  - `tax_rates.description` (nullable string)
    An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

  - `tax_rates.display_name` (string)
    The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

  - `tax_rates.effective_percentage` (nullable float)
    Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true,
    this percentage reflects the rate actually used to calculate tax based on the product’s taxability
    and whether the user is registered to collect taxes in the corresponding jurisdiction.

  - `tax_rates.flat_amount` (nullable object)
    The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

    - `tax_rates.flat_amount.amount` (integer)
      Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

    - `tax_rates.flat_amount.currency` (string)
      Three-letter ISO currency code, in lowercase.

  - `tax_rates.inclusive` (boolean)
    This specifies if the tax rate is inclusive or exclusive.

  - `tax_rates.jurisdiction` (nullable string)
    The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

  - `tax_rates.jurisdiction_level` (nullable enum)
    The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.

  - `tax_rates.livemode` (boolean)
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

  - `tax_rates.metadata` (nullable object)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

  - `tax_rates.percentage` (float)
    Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

  - `tax_rates.rate_type` (nullable enum)
    Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.

    A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

    A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

  - `tax_rates.state` (nullable string)
    [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

  - `tax_rates.tax_type` (nullable enum)
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

- `taxes` (nullable array of objects)
  The tax information of the line item.

  - `taxes.amount` (integer)
    The amount of the tax, in .

  - `taxes.tax_behavior` (enum)
    Whether this tax is inclusive or exclusive.

  - `taxes.tax_rate_details` (nullable object)
    Additional details about the tax rate. Only present when `type` is `tax_rate_details`.

  - `taxes.taxability_reason` (enum)
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

  - `taxes.taxable_amount` (nullable integer)
    The amount on which tax is calculated, in .

  - `taxes.type` (enum)
    The type of tax information.

- `type` (enum)
  The type of the credit note line item, one of `invoice_line_item` or `custom_line_item`. When the type is `invoice_line_item` there is an additional `invoice_line_item` property on the resource the value of which is the id of the credited line item on the invoice.

- `unit_amount` (nullable integer)
  The cost of each unit of product being credited.

- `unit_amount_decimal` (nullable decimal string)
  Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

### The Credit Note Line Item object

```json
{
  "id": "cnli_1NPtOx2eZvKYlo2CBH1NpUsU",
  "object": "credit_note_line_item",
  "amount": 749,
  "description": "My First Invoice Item (created for API docs)",
  "discount_amount": 0,
  "discount_amounts": [],
  "invoice_line_item": "il_1NPtOx2eZvKYlo2CAUuq0WVl",
  "livemode": false,
  "quantity": 1,
  "taxes": [],
  "tax_rates": [],
  "type": "invoice_line_item",
  "unit_amount": null,
  "unit_amount_decimal": null
}
```