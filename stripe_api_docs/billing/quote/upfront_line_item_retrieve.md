# Retrieve a quote's upfront line items

When retrieving a quote, there is an includable [**computed.upfront.line\_items**](https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items) property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.

A dictionary with a `data` property that contains an array of up to `limit` upfront line items, starting after Line Item `starting_after`. Each entry in the array is a separate Line Item object. If no more upfront line items are available, the resulting array will be empty.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new QuoteComputedUpfrontLineItemsService();
StripeList<LineItem> lineItems = service.List("qt_1Mr7wVLkdIwHu7ixJYSiPTGq");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.QuoteListComputedUpfrontLineItemsParams{
  Quote: stripe.String("qt_1Mr7wVLkdIwHu7ixJYSiPTGq"),
};
result := quote.ListComputedUpfrontLineItems(params);
```

```java
Stripe.apiKey = "<<secret key>>";

Quote resource = Quote.retrieve("qt_1Mr7wVLkdIwHu7ixJYSiPTGq");

QuoteListComputedUpfrontLineItemsParams params =
  QuoteListComputedUpfrontLineItemsParams.builder().build();

LineItemCollection lineItems = resource.listComputedUpfrontLineItems(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const lineItems = await stripe.quotes.listComputedUpfrontLineItems('qt_1Mr7wVLkdIwHu7ixJYSiPTGq');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

line_items = stripe.Quote.list_computed_upfront_line_items("qt_1Mr7wVLkdIwHu7ixJYSiPTGq")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$lineItems = $stripe->quotes->allComputedUpfrontLineItems('qt_1Mr7wVLkdIwHu7ixJYSiPTGq', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

line_items = Stripe::Quote.list_computed_upfront_line_items('qt_1Mr7wVLkdIwHu7ixJYSiPTGq')
```

### Response

```json
{
  "object": "list",
  "data": [
    {
      "id": "li_1Mr7wVLkdIwHu7ixMMjVsIUH",
      "object": "item",
      "amount_discount": 0,
      "amount_subtotal": 2198,
      "amount_tax": 0,
      "amount_total": 2198,
      "currency": "usd",
      "description": "T-shirt",
      "price": {
        "id": "price_1Mr7wULkdIwHu7ixhPkIEN2w",
        "object": "price",
        "active": true,
        "billing_scheme": "per_unit",
        "created": 1680130690,
        "currency": "usd",
        "custom_unit_amount": null,
        "livemode": false,
        "lookup_key": null,
        "metadata": {},
        "nickname": null,
        "product": "prod_NcMfZX1FelgpZm",
        "recurring": null,
        "tax_behavior": "unspecified",
        "tiers_mode": null,
        "transform_quantity": null,
        "type": "one_time",
        "unit_amount": 1099,
        "unit_amount_decimal": "1099"
      },
      "quantity": 2
    }
  ],
  "has_more": false,
  "url": "/v1/quotes/qt_1Mr7wVLkdIwHu7ixJYSiPTGq/computed_upfront_line_items"
}
```