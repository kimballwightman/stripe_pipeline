# Search subscriptions

Search for subscriptions you’ve previously created using Stripe’s [Search Query Language](https://docs.stripe.com/docs/search.md#search-query-language).
Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
to an hour behind during outages. Search functionality is not available to merchants in India.

A dictionary with a `data` property that contains an array of up to `limit` subscriptions. If no objects match the
query, the resulting array will be empty. See the related guide on [expanding properties in lists](https://docs.stripe.com/docs/expand.md#lists).

- `query` (string, required)
  The search query string. See [search query language](https://docs.stripe.com/docs/search.md#search-query-language) and the list of supported [query fields for subscriptions](https://docs.stripe.com/docs/search.md#query-fields-for-subscriptions).

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `page` (string, optional)
  A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new SubscriptionSearchOptions
{
    Query = "status:'active' AND metadata['order_id']:'6735'",
};
var service = new SubscriptionService();
StripeSearchResult<Subscription> subscriptions = service.Search(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.SubscriptionSearchParams{
  SearchParams: stripe.SearchParams{Query: "status:'active' AND metadata['order_id']:'6735'"},
};
result := subscription.Search(params);
```

```java
Stripe.apiKey = "<<secret key>>";

SubscriptionSearchParams params =
  SubscriptionSearchParams.builder()
    .setQuery("status:'active' AND metadata['order_id']:'6735'")
    .build();

SubscriptionSearchResult subscriptions = Subscription.search(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const subscriptions = await stripe.subscriptions.search({
  query: 'status:\'active\' AND metadata[\'order_id\']:\'6735\'',
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

subscriptions = stripe.Subscription.search(query="status:'active' AND metadata['order_id']:'6735'")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$subscriptions = $stripe->subscriptions->search([
  'query' => 'status:\'active\' AND metadata[\'order_id\']:\'6735\'',
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

subscriptions = Stripe::Subscription.search({
  query: 'status:\'active\' AND metadata[\'order_id\']:\'6735\'',
})
```

### Response

```json
{
  "object": "search_result",
  "url": "/v1/subscriptions/search",
  "has_more": false,
  "data": [
    {
      "id": "sub_1MoG3CLkdIwHu7ixd86qvAfe",
      "object": "subscription",
      "application": null,
      "application_fee_percent": null,
      "automatic_tax": {
        "enabled": false,
        "liability": null
      },
      "billing_cycle_anchor": 1679446874,
      "cancel_at": null,
      "cancel_at_period_end": false,
      "canceled_at": null,
      "cancellation_details": {
        "comment": null,
        "feedback": null,
        "reason": null
      },
      "collection_method": "charge_automatically",
      "created": 1679446874,
      "currency": "usd",
      "customer": "cus_NZOq6LNU39H6ZI",
      "days_until_due": null,
      "default_payment_method": null,
      "default_source": null,
      "default_tax_rates": [],
      "description": null,
      "discounts": null,
      "ended_at": null,
      "invoice_settings": {
        "issuer": {
          "type": "self"
        }
      },
      "items": {
        "object": "list",
        "data": [
          {
            "id": "si_NZOqmziODmZt2v",
            "object": "subscription_item",
            "created": 1679446875,
            "current_period_end": 1682125274,
            "current_period_start": 1679446874,
            "metadata": {},
            "plan": {
              "id": "price_1MoG3BLkdIwHu7ixrHMcmj3f",
              "object": "plan",
              "active": true,
              "amount": 1099,
              "amount_decimal": "1099",
              "billing_scheme": "per_unit",
              "created": 1679446873,
              "currency": "usd",
              "interval": "month",
              "interval_count": 1,
              "livemode": false,
              "metadata": {},
              "nickname": null,
              "product": "prod_NZOqsBJfaRYI1M",
              "tiers_mode": null,
              "transform_usage": null,
              "trial_period_days": null,
              "usage_type": "licensed"
            },
            "price": {
              "id": "price_1MoG3BLkdIwHu7ixrHMcmj3f",
              "object": "price",
              "active": true,
              "billing_scheme": "per_unit",
              "created": 1679446873,
              "currency": "usd",
              "custom_unit_amount": null,
              "livemode": false,
              "lookup_key": null,
              "metadata": {},
              "nickname": null,
              "product": "prod_NZOqsBJfaRYI1M",
              "recurring": {
                "interval": "month",
                "interval_count": 1,
                "trial_period_days": null,
                "usage_type": "licensed"
              },
              "tax_behavior": "unspecified",
              "tiers_mode": null,
              "transform_quantity": null,
              "type": "recurring",
              "unit_amount": 1099,
              "unit_amount_decimal": "1099"
            },
            "quantity": 1,
            "subscription": "sub_1MoG3CLkdIwHu7ixd86qvAfe",
            "tax_rates": []
          }
        ],
        "has_more": false,
        "total_count": 1,
        "url": "/v1/subscription_items?subscription=sub_1MoG3CLkdIwHu7ixd86qvAfe"
      },
      "latest_invoice": "in_1MoG3CLkdIwHu7ixuBm2QIyW",
      "livemode": false,
      "metadata": {
        "order_id": "6735"
      },
      "next_pending_invoice_item_invoice": null,
      "on_behalf_of": null,
      "pause_collection": null,
      "payment_settings": {
        "payment_method_options": null,
        "payment_method_types": null,
        "save_default_payment_method": "off"
      },
      "pending_invoice_item_interval": null,
      "pending_setup_intent": null,
      "pending_update": null,
      "plan": {
        "id": "price_1MoG3BLkdIwHu7ixrHMcmj3f",
        "object": "plan",
        "active": true,
        "amount": 1099,
        "amount_decimal": "1099",
        "billing_scheme": "per_unit",
        "created": 1679446873,
        "currency": "usd",
        "interval": "month",
        "interval_count": 1,
        "livemode": false,
        "metadata": {},
        "nickname": null,
        "product": "prod_NZOqsBJfaRYI1M",
        "tiers_mode": null,
        "transform_usage": null,
        "trial_period_days": null,
        "usage_type": "licensed"
      },
      "quantity": 1,
      "schedule": null,
      "start_date": 1679446874,
      "status": "active",
      "test_clock": null,
      "transfer_data": null,
      "trial_end": null,
      "trial_settings": {
        "end_behavior": {
          "missing_payment_method": "create_invoice"
        }
      },
      "trial_start": null
    }
  ]
}
```