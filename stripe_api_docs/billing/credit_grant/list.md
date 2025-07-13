# List credit grants

Retrieve a list of credit grants.

Returns a list of credit grants.

- `customer` (string, optional)
  Only return credit grants for this customer.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new Stripe.Billing.CreditGrantService();
StripeList<Stripe.Billing.CreditGrant> creditGrants = service.List();
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BillingCreditGrantListParams{};
result := creditgrant.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

CreditGrantListParams params = CreditGrantListParams.builder().build();

CreditGrantCollection creditGrants = CreditGrant.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const creditGrants = await stripe.billing.creditGrants.list();
```

```python
import stripe
stripe.api_key = "<<secret key>>"

credit_grants = stripe.billing.CreditGrant.list()
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$creditGrants = $stripe->billing->creditGrants->all([]);
```

```ruby
Stripe.api_key = '<<secret key>>'

credit_grants = Stripe::Billing::CreditGrant.list()
```

### Response

```json
{
  "object": "list",
  "data": [
    {
      "id": "credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo",
      "object": "billing.credit_grant",
      "amount": {
        "monetary": {
          "currency": "usd",
          "value": 1000
        },
        "type": "monetary"
      },
      "applicability_config": {
        "scope": {
          "price_type": "metered"
        }
      },
      "category": "paid",
      "created": 1726620803,
      "customer": "cus_QrvQguzkIK8zTj",
      "effective_at": 1729297860,
      "expires_at": null,
      "livemode": false,
      "metadata": {},
      "name": "Purchased Credits",
      "priority": 50,
      "test_clock": null,
      "updated": 1726620803,
      "voided_at": null
    }
  ],
  "has_more": false,
  "url": "/v1/billing/credit_grants"
}
```