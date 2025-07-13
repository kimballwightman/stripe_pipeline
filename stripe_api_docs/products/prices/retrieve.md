# Retrieve a price

Retrieves the price with the given ID.

Returns a price if a valid price or plan ID was provided. Raises [an error](#errors) otherwise.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new PriceService();
Price price = service.Get("price_1MoBy5LkdIwHu7ixZhnattbh");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PriceParams{};
result, err := price.Get("price_1MoBy5LkdIwHu7ixZhnattbh", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Price price = Price.retrieve("price_1MoBy5LkdIwHu7ixZhnattbh");
```

```node
const stripe = require('stripe')('<<secret key>>');

const price = await stripe.prices.retrieve('price_1MoBy5LkdIwHu7ixZhnattbh');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

price = stripe.Price.retrieve("price_1MoBy5LkdIwHu7ixZhnattbh")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$price = $stripe->prices->retrieve('price_1MoBy5LkdIwHu7ixZhnattbh', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

price = Stripe::Price.retrieve('price_1MoBy5LkdIwHu7ixZhnattbh')
```

### Response

```json
{
  "id": "price_1MoBy5LkdIwHu7ixZhnattbh",
  "object": "price",
  "active": true,
  "billing_scheme": "per_unit",
  "created": 1679431181,
  "currency": "usd",
  "custom_unit_amount": null,
  "livemode": false,
  "lookup_key": null,
  "metadata": {},
  "nickname": null,
  "product": "prod_NZKdYqrwEYx6iK",
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
  "unit_amount": 1000,
  "unit_amount_decimal": "1000"
}
```