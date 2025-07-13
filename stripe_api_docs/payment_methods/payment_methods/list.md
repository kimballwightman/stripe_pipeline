# List PaymentMethods

Returns a list of PaymentMethods for Treasury flows. If you want to list the PaymentMethods attached to a Customer for payments, you should use the [List a Customer’s PaymentMethods](https://docs.stripe.com/docs/api/payment_methods/customer_list.md) API instead.

A dictionary with a `data` property that contains an array of up to `limit` PaymentMethods of type `type`, starting after PaymentMethods `starting_after`. Each entry in the array is a separate PaymentMethod object. If no more PaymentMethods are available, the resulting array will be empty.

- `customer` (string, optional)
  The ID of the customer whose PaymentMethods will be retrieved.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `type` (enum, optional)
  An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new PaymentMethodListOptions
{
    Type = "card",
    Limit = 3,
    Customer = "cus_9s6XKzkNRiz8i3",
};
var service = new PaymentMethodService();
StripeList<PaymentMethod> paymentMethods = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentMethodListParams{
  Type: stripe.String(string(stripe.PaymentMethodTypeCard)),
  Customer: stripe.String("cus_9s6XKzkNRiz8i3"),
};
params.Limit = stripe.Int64(3)
result := paymentmethod.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

PaymentMethodListParams params =
  PaymentMethodListParams.builder()
    .setType(PaymentMethodListParams.Type.CARD)
    .setLimit(3L)
    .setCustomer("cus_9s6XKzkNRiz8i3")
    .build();

PaymentMethodCollection paymentMethods = PaymentMethod.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const paymentMethods = await stripe.paymentMethods.list({
  type: 'card',
  limit: 3,
  customer: 'cus_9s6XKzkNRiz8i3',
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_methods = stripe.PaymentMethod.list(
  type="card",
  limit=3,
  customer="cus_9s6XKzkNRiz8i3",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentMethods = $stripe->paymentMethods->all([
  'type' => 'card',
  'limit' => 3,
  'customer' => 'cus_9s6XKzkNRiz8i3',
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_methods = Stripe::PaymentMethod.list({
  type: 'card',
  limit: 3,
  customer: 'cus_9s6XKzkNRiz8i3',
})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/payment_methods",
  "has_more": false,
  "data": [
    {
      "id": "pm_1NO6mA2eZvKYlo2CEydeHsKT",
      "object": "payment_method",
      "billing_details": {
        "address": {
          "city": null,
          "country": null,
          "line1": null,
          "line2": null,
          "postal_code": null,
          "state": null
        },
        "email": null,
        "name": null,
        "phone": null
      },
      "card": {
        "brand": "visa",
        "checks": {
          "address_line1_check": null,
          "address_postal_code_check": null,
          "cvc_check": "unchecked"
        },
        "country": "US",
        "exp_month": 8,
        "exp_year": 2024,
        "fingerprint": "Xt5EWLLDS7FJjR1c",
        "funding": "credit",
        "generated_from": null,
        "last4": "4242",
        "networks": {
          "available": [
            "visa"
          ],
          "preferred": null
        },
        "three_d_secure_usage": {
          "supported": true
        },
        "wallet": null
      },
      "created": 1687991030,
      "customer": "cus_9s6XKzkNRiz8i3",
      "livemode": false,
      "metadata": {},
      "type": "card"
    }
  ]
}
```