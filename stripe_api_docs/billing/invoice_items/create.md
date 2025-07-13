# Create an invoice item

Creates an item to be added to a draft invoice (up to 250 items per invoice). If no invoice is specified, the item will be on the next invoice created for the customer specified.

The created invoice item object is returned if successful. Otherwise, this call raises [an error](#errors).

- `customer` (string, optional)
  The ID of the customer who will be billed when this invoice item is billed.

- `amount` (integer, optional)
  The integer amount in  of the charge to be applied to the upcoming invoice. Passing in a negative `amount` will reduce the `amount_due` on the invoice.

- `currency` (enum, optional)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `description` (string, optional)
  An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.

- `discountable` (boolean, optional)
  Controls whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items.

- `discounts` (array of objects, optional)
  The coupons and promotion codes to redeem into discounts for the invoice item or invoice line item.

  - `discounts.coupon` (string, optional)
    ID of the coupon to create a new discount for.

  - `discounts.discount` (string, optional)
    ID of an existing discount on the object (or one of its ancestors) to reuse.

  - `discounts.promotion_code` (string, optional)
    ID of the promotion code to create a new discount for.

- `invoice` (string, optional)
  The ID of an existing invoice to add this invoice item to. When left blank, the invoice item will be added to the next upcoming scheduled invoice. This is useful when adding invoice items in response to an invoice.created webhook. You can only add invoice items to draft invoices and there is a maximum of 250 items per invoice.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

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

  - `price_data.product` (string, required)
    The ID of the [Product](https://docs.stripe.com/api/products) that this [Price](https://docs.stripe.com/api/prices) will belong to.

  - `price_data.tax_behavior` (enum, optional)
    Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.

  - `price_data.unit_amount` (integer, optional)
    A positive integer in  (or 0 for a free price) representing how much to charge.

  - `price_data.unit_amount_decimal` (string, optional)
    Same as `unit_amount`, but accepts a decimal value in  with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

- `pricing` (object, optional)
  The pricing information for the invoice item.

  - `pricing.price` (string, optional)
    The ID of the price object.

- `quantity` (integer, optional)
  Non-negative integer. The quantity of units for the invoice item.

- `subscription` (string, optional)
  The ID of a subscription to add this invoice item to. When left blank, the invoice item is added to the next upcoming scheduled invoice. When set, scheduled invoices for subscriptions other than the specified subscription will ignore the invoice item. Use this when you want to express that an invoice item has been accrued within the context of a particular subscription.

- `tax_behavior` (enum, optional)
  Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.

- `tax_code` (string, optional)
  A [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID.

- `tax_rates` (array of strings, optional)
  The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item.

- `unit_amount_decimal` (string, optional)
  The decimal unit amount in  of the charge to be applied to the upcoming invoice. This `unit_amount_decimal` will be multiplied by the quantity to get the full amount. Passing in a negative `unit_amount_decimal` will reduce the `amount_due` on the invoice. Accepts at most 12 decimal places.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new InvoiceItemCreateOptions
{
    Customer = "cus_NeZei8imSbMVvi",
    Pricing = new InvoiceItemPricingOptions { Price = "price_1MtGUsLkdIwHu7ix1be5Ljaj" },
};
var service = new InvoiceItemService();
InvoiceItem invoiceItem = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.InvoiceItemParams{
  Customer: stripe.String("cus_NeZei8imSbMVvi"),
  Pricing: &stripe.InvoiceItemPricingParams{Price: stripe.String("price_1MtGUsLkdIwHu7ix1be5Ljaj")},
};
result, err := invoiceitem.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

InvoiceItemCreateParams params =
  InvoiceItemCreateParams.builder()
    .setCustomer("cus_NeZei8imSbMVvi")
    .setPricing(
      InvoiceItemCreateParams.Pricing.builder().setPrice("price_1MtGUsLkdIwHu7ix1be5Ljaj").build()
    )
    .build();

InvoiceItem invoiceItem = InvoiceItem.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const invoiceItem = await stripe.invoiceItems.create({
  customer: 'cus_NeZei8imSbMVvi',
  pricing: {
    price: 'price_1MtGUsLkdIwHu7ix1be5Ljaj',
  },
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

invoice_item = stripe.InvoiceItem.create(
  customer="cus_NeZei8imSbMVvi",
  pricing={"price": "price_1MtGUsLkdIwHu7ix1be5Ljaj"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$invoiceItem = $stripe->invoiceItems->create([
  'customer' => 'cus_NeZei8imSbMVvi',
  'pricing' => ['price' => 'price_1MtGUsLkdIwHu7ix1be5Ljaj'],
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

invoice_item = Stripe::InvoiceItem.create({
  customer: 'cus_NeZei8imSbMVvi',
  pricing: {price: 'price_1MtGUsLkdIwHu7ix1be5Ljaj'},
})
```

### Response

```json
{
  "id": "ii_1MtGUtLkdIwHu7ixBYwjAM00",
  "object": "invoiceitem",
  "amount": 1099,
  "currency": "usd",
  "customer": "cus_NeZei8imSbMVvi",
  "date": 1680640231,
  "description": "T-shirt",
  "discountable": true,
  "discounts": [],
  "invoice": null,
  "livemode": false,
  "metadata": {},
  "parent": null,
  "period": {
    "end": 1680640231,
    "start": 1680640231
  },
  "pricing": {
    "price_details": {
      "price": "price_1MtGUsLkdIwHu7ix1be5Ljaj",
      "product": "prod_NeZe7xbBdJT8EN"
    },
    "type": "price_details",
    "unit_amount_decimal": "1099"
  },
  "proration": false,
  "quantity": 1,
  "tax_rates": [],
  "test_clock": null
}
```