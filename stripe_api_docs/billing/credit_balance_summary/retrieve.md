# Retrieve the credit balance summary for a customer

Retrieves the credit balance summary for a customer.

Returns the credit balance summary.

- `customer` (string, optional)
  The customer for which to fetch credit balance summary.

- `filter` (object, required)
  The filter criteria for the credit balance summary.

  - `filter.type` (enum, required)
    Specify the type of this filter.

    The balance summary for a given applicability scope.

    The balance summary for a given credit grant.

  - `filter.applicability_scope` (object, optional)
    The billing credit applicability scope for which to fetch credit balance summary.

    - `filter.applicability_scope.price_type` (enum, optional)
      The price type that credit grants can apply to. We currently only support the `metered` price type. Cannot be used in combination with `prices`.

      Credit grants being created can only apply to metered prices.

  - `filter.credit_grant` (string, optional)
    The credit grant for which to fetch credit balance summary.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new Stripe.Billing.CreditBalanceSummaryGetOptions
{
    Customer = "cus_QsEHa3GKweMwih",
    Filter = new Stripe.Billing.CreditBalanceSummaryFilterOptions
    {
        Type = "credit_grant",
        CreditGrant = "credgr_test_61R9rvFh1HgrFIoCp41L6nFOS1ekDCeW",
    },
};
var service = new Stripe.Billing.CreditBalanceSummaryService();
Stripe.Billing.CreditBalanceSummary creditBalanceSummary = service.Get(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BillingCreditBalanceSummaryParams{
  Customer: stripe.String("cus_QsEHa3GKweMwih"),
  Filter: &stripe.BillingCreditBalanceSummaryFilterParams{
    Type: stripe.String("credit_grant"),
    CreditGrant: stripe.String("credgr_test_61R9rvFh1HgrFIoCp41L6nFOS1ekDCeW"),
  },
};
result, err := creditbalancesummary.Get(params);
```

```java
Stripe.apiKey = "<<secret key>>";

CreditBalanceSummaryRetrieveParams params =
  CreditBalanceSummaryRetrieveParams.builder()
    .setCustomer("cus_QsEHa3GKweMwih")
    .setFilter(
      CreditBalanceSummaryRetrieveParams.Filter.builder()
        .setType(CreditBalanceSummaryRetrieveParams.Filter.Type.CREDIT_GRANT)
        .setCreditGrant("credgr_test_61R9rvFh1HgrFIoCp41L6nFOS1ekDCeW")
        .build()
    )
    .build();

CreditBalanceSummary creditBalanceSummary = CreditBalanceSummary.retrieve(params, null);
```

```node
const stripe = require('stripe')('<<secret key>>');

const creditBalanceSummary = await stripe.billing.creditBalanceSummary.retrieve({
  customer: 'cus_QsEHa3GKweMwih',
  filter: {
    type: 'credit_grant',
    credit_grant: 'credgr_test_61R9rvFh1HgrFIoCp41L6nFOS1ekDCeW',
  },
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

credit_balance_summary = stripe.billing.CreditBalanceSummary.retrieve(
  customer="cus_QsEHa3GKweMwih",
  filter={"type": "credit_grant", "credit_grant": "credgr_test_61R9rvFh1HgrFIoCp41L6nFOS1ekDCeW"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$creditBalanceSummary = $stripe->billing->creditBalanceSummary->retrieve([
  'customer' => 'cus_QsEHa3GKweMwih',
  'filter' => [
    'type' => 'credit_grant',
    'credit_grant' => 'credgr_test_61R9rvFh1HgrFIoCp41L6nFOS1ekDCeW',
  ],
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

credit_balance_summary = Stripe::Billing::CreditBalanceSummary.retrieve({
  customer: 'cus_QsEHa3GKweMwih',
  filter: {
    type: 'credit_grant',
    credit_grant: 'credgr_test_61R9rvFh1HgrFIoCp41L6nFOS1ekDCeW',
  },
})
```

### Response

```json
{
  "object": "billing.credit_balance_summary",
  "balances": [
    {
      "available_balance": {
        "monetary": {
          "currency": "usd",
          "value": 1000
        },
        "type": "monetary"
      },
      "ledger_balance": {
        "monetary": {
          "currency": "usd",
          "value": 1000
        },
        "type": "monetary"
      }
    }
  ],
  "customer": "cus_QsEHa3GKweMwih",
  "livemode": false
}
```