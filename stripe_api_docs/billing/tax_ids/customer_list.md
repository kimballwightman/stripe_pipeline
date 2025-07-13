# List all Customer tax IDs

Returns a list of tax IDs for a customer.

A dictionary with a `data` property that contains an array of up to `limit` tax IDs, starting after tax ID `starting_after`. Each entry in the array is a separate `tax_id` object. If no more tax IDs are available, the resulting array will be empty. Raises [an error](#errors) if the customer ID is invalid.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CustomerTaxIdListOptions { Limit = 3 };
var service = new CustomerTaxIdService();
StripeList<TaxId> taxIds = service.List("cus_NZKoSNZZ58qtO0", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TaxIDListParams{Customer: stripe.String("cus_NZKoSNZZ58qtO0")};
params.Limit = stripe.Int64(3)
result := taxid.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

TaxIdCollectionListParams params = TaxIdCollectionListParams.builder().setLimit(3L).build();

TaxIdCollection taxIds = TaxId.list("cus_NZKoSNZZ58qtO0", params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const taxIds = await stripe.customers.listTaxIds(
  'cus_NZKoSNZZ58qtO0',
  {
    limit: 3,
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

tax_ids = stripe.Customer.list_tax_ids(
  "cus_NZKoSNZZ58qtO0",
  limit=3,
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$taxIds = $stripe->customers->allTaxIds('cus_NZKoSNZZ58qtO0', ['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

tax_ids = Stripe::Customer.list_tax_ids('cus_NZKoSNZZ58qtO0', {limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/customers/cus_NZKoSNZZ58qtO0/tax_ids",
  "has_more": false,
  "data": [
    {
      "id": "txi_1MoC8zLkdIwHu7ixEhgWcHzJ",
      "object": "tax_id",
      "country": "DE",
      "created": 1679431857,
      "customer": "cus_NZKoSNZZ58qtO0",
      "livemode": false,
      "type": "eu_vat",
      "value": "DE123456789",
      "verification": {
        "status": "pending",
        "verified_address": null,
        "verified_name": null
      }
    }
  ]
}
```