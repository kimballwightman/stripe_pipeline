# List all disputes

Returns a list of your disputes.

A dictionary with a `data` property that contains an array of up to `limit` disputes, starting after dispute `starting_after`. Each entry in the array is a separate dispute object. If no more disputes are available, the resulting array will be empty.

- `charge` (string, optional)
  Only return disputes associated to the charge specified by this charge ID.

- `created` (object, optional)
  Only return disputes that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `payment_intent` (string, optional)
  Only return disputes associated to the PaymentIntent specified by this PaymentIntent ID.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new DisputeListOptions { Limit = 3 };
var service = new DisputeService();
StripeList<Dispute> disputes = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.DisputeListParams{};
params.Limit = stripe.Int64(3)
result := dispute.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

DisputeListParams params = DisputeListParams.builder().setLimit(3L).build();

DisputeCollection disputes = Dispute.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const disputes = await stripe.disputes.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

disputes = stripe.Dispute.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$disputes = $stripe->disputes->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

disputes = Stripe::Dispute.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/disputes",
  "has_more": false,
  "data": [
    {
      "id": "du_1MtJUT2eZvKYlo2CNaw2HvEv",
      "object": "dispute",
      "amount": 1000,
      "balance_transactions": [],
      "charge": "ch_1AZtxr2eZvKYlo2CJDX8whov",
      "created": 1680651737,
      "currency": "usd",
      "evidence": {
        "access_activity_log": null,
        "billing_address": null,
        "cancellation_policy": null,
        "cancellation_policy_disclosure": null,
        "cancellation_rebuttal": null,
        "customer_communication": null,
        "customer_email_address": null,
        "customer_name": null,
        "customer_purchase_ip": null,
        "customer_signature": null,
        "duplicate_charge_documentation": null,
        "duplicate_charge_explanation": null,
        "duplicate_charge_id": null,
        "product_description": null,
        "receipt": null,
        "refund_policy": null,
        "refund_policy_disclosure": null,
        "refund_refusal_explanation": null,
        "service_date": null,
        "service_documentation": null,
        "shipping_address": null,
        "shipping_carrier": null,
        "shipping_date": null,
        "shipping_documentation": null,
        "shipping_tracking_number": null,
        "uncategorized_file": null,
        "uncategorized_text": null
      },
      "evidence_details": {
        "due_by": 1682294399,
        "has_evidence": false,
        "past_due": false,
        "submission_count": 0
      },
      "is_charge_refundable": true,
      "livemode": false,
      "metadata": {},
      "payment_intent": null,
      "reason": "general",
      "status": "warning_needs_response"
    }
  ]
}
```