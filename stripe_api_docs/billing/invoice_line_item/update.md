# Update an invoice's line item

Updates an invoice’s line item. Some fields, such as `tax_amounts`, only live on the invoice line item,
so they can only be updated through this endpoint. Other fields, such as `amount`, live on both the invoice
item and the invoice line item, so updates on this endpoint will propagate to the invoice item as well.
Updating an invoice’s line item is only possible before the invoice is finalized.

The updated invoice’s line item object is returned upon success. Otherwise, this call raises [an error](#errors).

- `invoice` (string, required)
  Invoice ID of line item

- `line_item_id` (string, required)
  Invoice line item ID

- `amount` (integer, optional)
  The integer amount in  of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer’s account, pass a negative amount.

- `description` (string, optional)
  An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.

- `discountable` (boolean, optional)
  Controls whether discounts apply to this line item. Defaults to false for prorations or negative line items, and true for all other line items. Cannot be set to true for prorations.

- `discounts` (array of objects, optional)
  The coupons, promotion codes & existing discounts which apply to the line item. Item discounts are applied before invoice discounts. Pass an empty string to remove previously-defined discounts.

  - `discounts.coupon` (string, optional)
    ID of the coupon to create a new discount for.

  - `discounts.discount` (string, optional)
    ID of an existing discount on the object (or one of its ancestors) to reuse.

  - `discounts.promotion_code` (string, optional)
    ID of the promotion code to create a new discount for.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. For [type=subscription](https://docs.stripe.com/docs/api/invoices/line_item.md#invoice_line_item_object-type) line items, the incoming metadata specified on the request is directly used to set this value, in contrast to [type=invoiceitem](api/invoices/line_item#invoice_line_item_object-type) line items, where any existing metadata on the invoice line is merged with the incoming data.

- `period` (object, optional)
  The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://docs.stripe.com/docs/revenue-recognition.md) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://docs.stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing.md) for details.

  - `period.end` (timestamp, required)
    The end of the period, which must be greater than or equal to the start. This value is inclusive.

  - `period.start` (timestamp, required)
    The start of the period. This value is inclusive.

- `price_data` (object, optional)
  Data used to generate a new [Price](https://docs.stripe.com/docs/api/prices.md) object inline.

  - `price_data.currency` (enum, required)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `price_data.product` (string, optional)
    The ID of the [Product](https://docs.stripe.com/api/products) that this [Price](https://docs.stripe.com/api/prices) will belong to. One of `product` or `product_data` is required.

  - `price_data.product_data` (object, optional)
    Data used to generate a new [Product](https://docs.stripe.com/api/products) object inline. One of `product` or `product_data` is required.

    - `price_data.product_data.name` (string, required)
      The product’s name, meant to be displayable to the customer.

    - `price_data.product_data.description` (string, optional)
      The product’s description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.

    - `price_data.product_data.images` (array of strings, optional)
      A list of up to 8 URLs of images for this product, meant to be displayable to the customer.

    - `price_data.product_data.metadata` (object, optional)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

    - `price_data.product_data.tax_code` (string, optional)
      A [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID.

  - `price_data.tax_behavior` (enum, optional)
    Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.

  - `price_data.unit_amount` (integer, optional)
    A non-negative integer in  representing how much to charge. One of `unit_amount` or `unit_amount_decimal` is required.

  - `price_data.unit_amount_decimal` (string, optional)
    Same as `unit_amount`, but accepts a decimal value in  with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

- `pricing` (object, optional)
  The pricing information for the invoice item.

  - `pricing.price` (string, optional)
    The ID of the price object.

- `quantity` (integer, optional)
  Non-negative integer. The quantity of units for the line item.

- `tax_amounts` (array of objects, optional)
  A list of up to 10 tax amounts for this line item. This can be useful if you calculate taxes on your own or use a third-party to calculate them. You cannot set tax amounts if any line item has [tax_rates](https://docs.stripe.com/docs/api/invoices/line_item.md#invoice_line_item_object-tax_rates) or if the invoice has [default_tax_rates](https://docs.stripe.com/docs/api/invoices/object.md#invoice_object-default_tax_rates) or uses [automatic tax](https://docs.stripe.com/docs/tax/invoicing.md). Pass an empty string to remove previously defined tax amounts.

  - `tax_amounts.amount` (integer, required)
    The amount, in , of the tax.

  - `tax_amounts.tax_rate_data` (object, required)
    Data to find or create a TaxRate object.

    Stripe automatically creates or reuses a TaxRate object for each tax amount. If the `tax_rate_data` exactly matches a previous value, Stripe will reuse the TaxRate object. TaxRate objects created automatically by Stripe are immediately archived, do not appear in the line item’s `tax_rates`, and cannot be directly added to invoices, payments, or line items.

    - `tax_amounts.tax_rate_data.display_name` (string, required)
      The display name of the tax rate, which will be shown to users.

    - `tax_amounts.tax_rate_data.inclusive` (boolean, required)
      This specifies if the tax rate is inclusive or exclusive.

    - `tax_amounts.tax_rate_data.percentage` (float, required)
      The statutory tax rate percent. This field accepts decimal values between 0 and 100 inclusive with at most 4 decimal places. To accommodate fixed-amount taxes, set the percentage to zero. Stripe will not display zero percentages on the invoice unless the `amount` of the tax is also zero.

    - `tax_amounts.tax_rate_data.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `tax_amounts.tax_rate_data.description` (string, optional)
      An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

    - `tax_amounts.tax_rate_data.jurisdiction` (string, optional)
      The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

    - `tax_amounts.tax_rate_data.jurisdiction_level` (enum, optional)
      The level of the jurisdiction that imposes this tax rate.

      This value indicates that the jurisdiction imposing the tax rate is at the `city` level.

      This value indicates that the jurisdiction imposing the tax rate is at the `country` level.

      This value indicates that the jurisdiction imposing the tax rate is at the `county` level.

      This value indicates that the jurisdiction imposing the tax rate is at the `district` level.

      This value indicates that the jurisdictions imposing the tax rate are at `multiple` different jurisdiction levels.

      This value indicates that the jurisdiction imposing the tax rate is at the `state` level.

    - `tax_amounts.tax_rate_data.state` (string, optional)
      [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2:US), without country prefix. For example, “NY” for New York, United States.

    - `tax_amounts.tax_rate_data.tax_type` (enum, optional)
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

  - `tax_amounts.taxable_amount` (integer, required)
    The amount on which tax is calculated, in .

  - `tax_amounts.taxability_reason` (enum, optional)
    The reasoning behind this tax, for example, if the product is tax exempt.

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

- `tax_rates` (array of strings, optional)
  The tax rates which apply to the line item. When set, the `default_tax_rates` on the invoice do not apply to this line item. Pass an empty string to remove previously-defined tax rates.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new InvoiceLineItemUpdateOptions();
var service = new InvoiceLineItemService();
InvoiceLineItem invoiceLineItem = service.Update(
    "in_1NuhUa2eZvKYlo2CWYVhyvD9",
    "il_tmp_1Nzo1ZGgdF1VjufLzD1UUn9R",
    options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.InvoiceLineItemParams{Invoice: stripe.String("in_1NuhUa2eZvKYlo2CWYVhyvD9")};
result, err := invoicelineitem.Update("il_tmp_1Nzo1ZGgdF1VjufLzD1UUn9R", params);
```

```java
Stripe.apiKey = "<<secret key>>";

InvoiceLineItem resource =
  InvoiceLineItem.retrieve("in_1NuhUa2eZvKYlo2CWYVhyvD9", "il_tmp_1Nzo1ZGgdF1VjufLzD1UUn9R");

InvoiceLineItemUpdateParams params = InvoiceLineItemUpdateParams.builder().build();

InvoiceLineItem invoiceLineItem = resource.update(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const invoiceLineItem = await stripe.invoices.updateLineItem(
  'in_1NuhUa2eZvKYlo2CWYVhyvD9',
  'il_tmp_1Nzo1ZGgdF1VjufLzD1UUn9R'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

invoice_line_item = stripe.InvoiceLineItem.modify(
  "in_1NuhUa2eZvKYlo2CWYVhyvD9",
  "il_tmp_1Nzo1ZGgdF1VjufLzD1UUn9R",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$invoiceLineItem = $stripe->invoices->updateLine(
  'in_1NuhUa2eZvKYlo2CWYVhyvD9',
  'il_tmp_1Nzo1ZGgdF1VjufLzD1UUn9R',
  []
);
```

```ruby
Stripe.api_key = '<<secret key>>'

invoice_line_item = Stripe::InvoiceLineItem.update(
  'in_1NuhUa2eZvKYlo2CWYVhyvD9',
  'il_tmp_1Nzo1ZGgdF1VjufLzD1UUn9R',
)
```

### Response

```json
{
  "id": "il_tmp_1Nzo1ZGgdF1VjufLzD1UUn9R",
  "object": "line_item",
  "amount": 1000,
  "currency": "usd",
  "description": "My First Invoice Item (created for API docs)",
  "discount_amounts": [],
  "discountable": true,
  "discounts": [],
  "livemode": false,
  "metadata": {},
  "parent": {
    "type": "invoice_item_details",
    "invoice_item_details": {
      "invoice_item": "ii_1Nzo1ZGgdF1VjufLzD1UUn9R",
      "proration": false,
      "proration_details": {
        "credited_items": null
      },
      "subscription": null
    }
  },
  "period": {
    "end": 1696975413,
    "start": 1696975413
  },
  "pricing": {
    "price_details": {
      "price": "price_1NzlYfGgdF1VjufL0cVjLJVI",
      "product": "prod_OnMHDH6VBmYlTr"
    },
    "type": "price_details",
    "unit_amount_decimal": "1000"
  },
  "quantity": 1,
  "taxes": []
}
```