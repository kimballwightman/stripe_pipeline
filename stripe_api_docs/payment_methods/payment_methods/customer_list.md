# List a Customer's PaymentMethods

Returns a list of PaymentMethods for a given Customer

A dictionary with a `data` property that contains an array of up to `limit` PaymentMethods of type `type`, starting after PaymentMethods `starting_after`. Each entry in the array is a separate PaymentMethod object. If no more PaymentMethods are available, the resulting array will be empty.

- `allow_redisplay` (enum, optional)
  This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow.

  Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

  Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

  This is the default value for payment methods where `allow_redisplay` wasn’t set.

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

var options = new CustomerPaymentMethodListOptions { Limit = 3 };
var service = new CustomerPaymentMethodService();
StripeList<PaymentMethod> paymentMethods = service.List("cus_9s6XKzkNRiz8i3", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CustomerListPaymentMethodsParams{Customer: stripe.String("cus_9s6XKzkNRiz8i3")};
params.Limit = stripe.Int64(3)
result := customer.ListPaymentMethods(params);
```

```java
Stripe.apiKey = "<<secret key>>";

Customer resource = Customer.retrieve("cus_9s6XKzkNRiz8i3");

CustomerListPaymentMethodsParams params =
  CustomerListPaymentMethodsParams.builder().setLimit(3L).build();

PaymentMethodCollection paymentMethods = resource.listPaymentMethods(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const paymentMethods = await stripe.customers.listPaymentMethods(
  'cus_9s6XKzkNRiz8i3',
  {
    limit: 3,
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_methods = stripe.Customer.list_payment_methods(
  "cus_9s6XKzkNRiz8i3",
  limit=3,
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentMethods = $stripe->customers->allPaymentMethods('cus_9s6XKzkNRiz8i3', ['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_methods = Stripe::Customer.list_payment_methods('cus_9s6XKzkNRiz8i3', {limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/customers/cus_9s6XKzkNRiz8i3/payment_methods",
  "has_more": false,
  "data": [
    {
      "id": "pm_1NVChw2eZvKYlo2CHxiM5E2E",
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
          "cvc_check": "pass"
        },
        "country": "US",
        "exp_month": 12,
        "exp_year": 2034,
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
      "created": 1689682128,
      "customer": "cus_9s6XKzkNRiz8i3",
      "livemode": false,
      "metadata": {},
      "redaction": null,
      "type": "card"
    }
  ]
}
```