# Bulk update invoice line items

Updates multiple line items on an invoice. This is only possible when an invoice is still a draft.

The updated invoice is returned upon success. Otherwise, this call raises [an error](#errors).

- `lines` (array of objects, required)
  The line items to update.

  - `lines.id` (string, required)
    ID of an existing line item on the invoice.

  - `lines.amount` (integer, optional)
    The integer amount in  of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer’s account, pass a negative amount.

  - `lines.description` (string, optional)
    An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.

  - `lines.discountable` (boolean, optional)
    Controls whether discounts apply to this line item. Defaults to false for prorations or negative line items, and true for all other line items. Cannot be set to true for prorations.

  - `lines.discounts` (array of objects, optional)
    The coupons, promotion codes & existing discounts which apply to the line item. Item discounts are applied before invoice discounts. Pass an empty string to remove previously-defined discounts.

    - `lines.discounts.coupon` (string, optional)
      ID of the coupon to create a new discount for.

    - `lines.discounts.discount` (string, optional)
      ID of an existing discount on the object (or one of its ancestors) to reuse.

    - `lines.discounts.promotion_code` (string, optional)
      ID of the promotion code to create a new discount for.

  - `lines.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. For [type=subscription](https://docs.stripe.com/docs/api/invoices/line_item.md#invoice_line_item_object-type) line items, the incoming metadata specified on the request is directly used to set this value, in contrast to [type=invoiceitem](api/invoices/line_item#invoice_line_item_object-type) line items, where any existing metadata on the invoice line is merged with the incoming data.

  - `lines.period` (object, optional)
    The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://docs.stripe.com/docs/revenue-recognition.md) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://docs.stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing.md) for details.

    - `lines.period.end` (timestamp, required)
      The end of the period, which must be greater than or equal to the start. This value is inclusive.

    - `lines.period.start` (timestamp, required)
      The start of the period. This value is inclusive.

  - `lines.price_data` (object, optional)
    Data used to generate a new [Price](https://docs.stripe.com/docs/api/prices.md) object inline.

    - `lines.price_data.currency` (enum, required)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `lines.price_data.product` (string, optional)
      The ID of the [Product](https://docs.stripe.com/api/products) that this [Price](https://docs.stripe.com/api/prices) will belong to. One of `product` or `product_data` is required.

    - `lines.price_data.product_data` (object, optional)
      Data used to generate a new [Product](https://docs.stripe.com/api/products) object inline. One of `product` or `product_data` is required.

      - `lines.price_data.product_data.name` (string, required)
        The product’s name, meant to be displayable to the customer.

      - `lines.price_data.product_data.description` (string, optional)
        The product’s description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.

      - `lines.price_data.product_data.images` (array of strings, optional)
        A list of up to 8 URLs of images for this product, meant to be displayable to the customer.

      - `lines.price_data.product_data.metadata` (object, optional)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

      - `lines.price_data.product_data.tax_code` (string, optional)
        A [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID.

    - `lines.price_data.tax_behavior` (enum, optional)
      Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.

    - `lines.price_data.unit_amount` (integer, optional)
      A non-negative integer in  representing how much to charge. One of `unit_amount` or `unit_amount_decimal` is required.

    - `lines.price_data.unit_amount_decimal` (string, optional)
      Same as `unit_amount`, but accepts a decimal value in  with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

  - `lines.pricing` (object, optional)
    The pricing information for the invoice item.

    - `lines.pricing.price` (string, optional)
      The ID of the price object.

  - `lines.quantity` (integer, optional)
    Non-negative integer. The quantity of units for the line item.

  - `lines.tax_amounts` (array of objects, optional)
    A list of up to 10 tax amounts for this line item. This can be useful if you calculate taxes on your own or use a third-party to calculate them. You cannot set tax amounts if any line item has [tax_rates](https://docs.stripe.com/docs/api/invoices/line_item.md#invoice_line_item_object-tax_rates) or if the invoice has [default_tax_rates](https://docs.stripe.com/docs/api/invoices/object.md#invoice_object-default_tax_rates) or uses [automatic tax](https://docs.stripe.com/docs/tax/invoicing.md). Pass an empty string to remove previously defined tax amounts.

    - `lines.tax_amounts.amount` (integer, required)
      The amount, in , of the tax.

    - `lines.tax_amounts.tax_rate_data` (object, required)
      Data to find or create a TaxRate object.

      Stripe automatically creates or reuses a TaxRate object for each tax amount. If the `tax_rate_data` exactly matches a previous value, Stripe will reuse the TaxRate object. TaxRate objects created automatically by Stripe are immediately archived, do not appear in the line item’s `tax_rates`, and cannot be directly added to invoices, payments, or line items.

      - `lines.tax_amounts.tax_rate_data.display_name` (string, required)
        The display name of the tax rate, which will be shown to users.

      - `lines.tax_amounts.tax_rate_data.inclusive` (boolean, required)
        This specifies if the tax rate is inclusive or exclusive.

      - `lines.tax_amounts.tax_rate_data.percentage` (float, required)
        The statutory tax rate percent. This field accepts decimal values between 0 and 100 inclusive with at most 4 decimal places. To accommodate fixed-amount taxes, set the percentage to zero. Stripe will not display zero percentages on the invoice unless the `amount` of the tax is also zero.

      - `lines.tax_amounts.tax_rate_data.country` (string, optional)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `lines.tax_amounts.tax_rate_data.description` (string, optional)
        An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

      - `lines.tax_amounts.tax_rate_data.jurisdiction` (string, optional)
        The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

      - `lines.tax_amounts.tax_rate_data.jurisdiction_level` (enum, optional)
        The level of the jurisdiction that imposes this tax rate.

        This value indicates that the jurisdiction imposing the tax rate is at the `city` level.

        This value indicates that the jurisdiction imposing the tax rate is at the `country` level.

        This value indicates that the jurisdiction imposing the tax rate is at the `county` level.

        This value indicates that the jurisdiction imposing the tax rate is at the `district` level.

        This value indicates that the jurisdictions imposing the tax rate are at `multiple` different jurisdiction levels.

        This value indicates that the jurisdiction imposing the tax rate is at the `state` level.

      - `lines.tax_amounts.tax_rate_data.state` (string, optional)
        [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2:US), without country prefix. For example, “NY” for New York, United States.

      - `lines.tax_amounts.tax_rate_data.tax_type` (enum, optional)
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

    - `lines.tax_amounts.taxable_amount` (integer, required)
      The amount on which tax is calculated, in .

    - `lines.tax_amounts.taxability_reason` (enum, optional)
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

  - `lines.tax_rates` (array of strings, optional)
    The tax rates which apply to the line item. When set, the `default_tax_rates` on the invoice do not apply to this line item. Pass an empty string to remove previously-defined tax rates.

- `invoice_metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. For [type=subscription](https://docs.stripe.com/docs/api/invoices/line_item.md#invoice_line_item_object-type) line items, the incoming metadata specified on the request is directly used to set this value, in contrast to [type=invoiceitem](api/invoices/line_item#invoice_line_item_object-type) line items, where any existing metadata on the invoice line is merged with the incoming data.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new InvoiceUpdateLinesOptions
{
    Lines = new List<InvoiceLineOptions>
    {
        new InvoiceLineOptions
        {
            Id = "il_1NuhUa2eZvKYlo2CC98Fg3Bo",
            Description = "test description",
        },
    },
};
var service = new InvoiceService();
Invoice invoice = service.UpdateLines("in_1NuhUa2eZvKYlo2CWYVhyvD9", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.InvoiceUpdateLinesParams{
  Lines: []*stripe.InvoiceUpdateLinesLineParams{
    &stripe.InvoiceUpdateLinesLineParams{
      ID: stripe.String("il_1NuhUa2eZvKYlo2CC98Fg3Bo"),
      Description: stripe.String("test description"),
    },
  },
};
result, err := invoice.UpdateLines("in_1NuhUa2eZvKYlo2CWYVhyvD9", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Invoice resource = Invoice.retrieve("in_1NuhUa2eZvKYlo2CWYVhyvD9");

InvoiceUpdateLinesParams params =
  InvoiceUpdateLinesParams.builder()
    .addLine(
      InvoiceUpdateLinesParams.Line.builder()
        .setId("il_1NuhUa2eZvKYlo2CC98Fg3Bo")
        .setDescription("test description")
        .build()
    )
    .build();

Invoice invoice = resource.updateLines(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const invoice = await stripe.invoices.updateLines(
  'in_1NuhUa2eZvKYlo2CWYVhyvD9',
  {
    lines: [
      {
        id: 'il_1NuhUa2eZvKYlo2CC98Fg3Bo',
        description: 'test description',
      },
    ],
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

invoice = stripe.Invoice.update_lines(
  "in_1NuhUa2eZvKYlo2CWYVhyvD9",
  lines=[{"id": "il_1NuhUa2eZvKYlo2CC98Fg3Bo", "description": "test description"}],
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$invoice = $stripe->invoices->updateLines(
  'in_1NuhUa2eZvKYlo2CWYVhyvD9',
  [
    'lines' => [
      [
        'id' => 'il_1NuhUa2eZvKYlo2CC98Fg3Bo',
        'description' => 'test description',
      ],
    ],
  ]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

invoice = Stripe::Invoice.update_lines(
  'in_1NuhUa2eZvKYlo2CWYVhyvD9',
  {
    lines: [
      {
        id: 'il_1NuhUa2eZvKYlo2CC98Fg3Bo',
        description: 'test description',
      },
    ],
  },
)
```

### Response

```json
{
  "id": "in_1NuhUa2eZvKYlo2CWYVhyvD9",
  "object": "invoice",
  "account_country": "US",
  "account_name": "Stripe.com",
  "account_tax_ids": null,
  "amount_due": 998,
  "amount_paid": 0,
  "amount_overpaid": 0,
  "amount_remaining": 998,
  "amount_shipping": 0,
  "application": null,
  "application_fee_amount": null,
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
  "created": 1695758664,
  "currency": "usd",
  "custom_fields": null,
  "customer": "cus_9s6XKzkNRiz8i3",
  "customer_address": null,
  "customer_email": "test@test.com",
  "customer_name": null,
  "customer_phone": null,
  "customer_shipping": null,
  "customer_tax_exempt": "none",
  "customer_tax_ids": [],
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discounts": [],
  "due_date": null,
  "effective_at": null,
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
    "data": [
      {
        "id": "il_1NuhUa2eZvKYlo2CC98Fg3Bo",
        "object": "line_item",
        "amount": 799,
        "currency": "usd",
        "description": "test description",
        "discount_amounts": [],
        "discountable": true,
        "discounts": [],
        "invoice_item": "ii_1NuhUa2eZvKYlo2CGeF7Qgx0",
        "livemode": false,
        "metadata": {},
        "period": {
          "end": 1695758664,
          "start": 1695758664
        },
        "pricing": {
          "price_details": {
            "price": "price_1NuhLA2eZvKYlo2Cq1tIGEBp",
            "product": "prod_Oi7aO1GPi1dWX7"
          },
          "type": "price_details",
          "unit_amount_decimal": "799"
        },
        "proration": false,
        "proration_details": {
          "credited_items": null
        },
        "quantity": 1,
        "subscription": null,
        "taxes": []
      },
      {
        "id": "il_1NuLVe2eZvKYlo2Canh35EfU",
        "object": "line_item",
        "amount": 199,
        "currency": "usd",
        "description": "Canned Coffee",
        "discount_amounts": [],
        "discountable": true,
        "discounts": [],
        "invoice_item": "ii_1NuLVd2eZvKYlo2CRWY0Hqgi",
        "livemode": false,
        "metadata": {},
        "period": {
          "end": 1695674161,
          "start": 1695674161
        },
        "pricing": {
          "price_details": {
            "price": "price_1NuI212eZvKYlo2CWgdD8kET",
            "product": "prod_OhhQNWDYdIbXYv"
          },
          "type": "price_details",
          "unit_amount_decimal": "199"
        },
        "proration": false,
        "proration_details": {
          "credited_items": null
        },
        "quantity": 1,
        "subscription": null,
        "taxes": [],
        "type": "invoiceitem"
      }
    ],
    "has_more": false,
    "url": "/v1/invoices/upcoming/lines?customer=cus_9s6XKzkNRiz8i3"
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
  "period_end": 1688482163,
  "period_start": 1688395763,
  "post_payment_credit_notes_amount": 0,
  "pre_payment_credit_notes_amount": 0,
  "receipt_number": null,
  "redaction": null,
  "rendering": null,
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
  "subtotal": 998,
  "subtotal_excluding_tax": 998,
  "test_clock": null,
  "total": 998,
  "total_discount_amounts": [],
  "total_excluding_tax": 998,
  "total_taxes": [],
  "webhooks_delivered_at": null
}
```