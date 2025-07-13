# Create a credit grant

Creates a credit grant.

Returns a credit grant.

- `amount` (object, required)
  Amount of this credit grant.

  - `amount.type` (enum, required)
    Specify the type of this amount. We currently only support `monetary` billing credits.

    The amount is a monetary amount.

  - `amount.monetary` (object, optional)
    The monetary amount.

    - `amount.monetary.currency` (enum, required)
      Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the `value` parameter.

    - `amount.monetary.value` (integer, required)
      A positive integer representing the amount of the credit grant.

- `applicability_config` (object, required)
  Configuration specifying what this credit grant applies to. We currently only support `metered` prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter) attached to them.

  - `applicability_config.scope` (object, required)
    Specify the scope of this applicability config.

    - `applicability_config.scope.price_type` (enum, optional)
      The price type that credit grants can apply to. We currently only support the `metered` price type. Cannot be used in combination with `prices`.

      Credit grants being created can only apply to metered prices.

- `category` (enum, required)
  The category of this credit grant.

  The credit grant was purchased by the customer for some amount.

  The credit grant was given to the customer for free.

- `customer` (string, optional)
  ID of the customer to receive the billing credits.

- `effective_at` (timestamp, optional)
  The time when the billing credits become effective-when they’re eligible for use. It defaults to the current timestamp if not specified.

- `expires_at` (timestamp, optional)
  The time when the billing credits expire. If not specified, the billing credits don’t expire.

- `metadata` (object, optional)
  Set of key-value pairs that you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format.

- `name` (string, optional)
  A descriptive name shown in the Dashboard.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new Stripe.Billing.CreditGrantCreateOptions
{
    Name = "Purchased Credits",
    Customer = "cus_QrvQguzkIK8zTj",
    Amount = new Stripe.Billing.CreditGrantAmountOptions
    {
        Monetary = new Stripe.Billing.CreditGrantAmountMonetaryOptions
        {
            Currency = "usd",
            Value = 1000,
        },
        Type = "monetary",
    },
    ApplicabilityConfig = new Stripe.Billing.CreditGrantApplicabilityConfigOptions
    {
        Scope = new Stripe.Billing.CreditGrantApplicabilityConfigScopeOptions
        {
            PriceType = "metered",
        },
    },
    Category = "paid",
};
var service = new Stripe.Billing.CreditGrantService();
Stripe.Billing.CreditGrant creditGrant = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BillingCreditGrantParams{
  Name: stripe.String("Purchased Credits"),
  Customer: stripe.String("cus_QrvQguzkIK8zTj"),
  Amount: &stripe.BillingCreditGrantAmountParams{
    Monetary: &stripe.BillingCreditGrantAmountMonetaryParams{
      Currency: stripe.String(string(stripe.CurrencyUSD)),
      Value: stripe.Int64(1000),
    },
    Type: stripe.String("monetary"),
  },
  ApplicabilityConfig: &stripe.BillingCreditGrantApplicabilityConfigParams{
    Scope: &stripe.BillingCreditGrantApplicabilityConfigScopeParams{
      PriceType: stripe.String("metered"),
    },
  },
  Category: stripe.String(string(stripe.BillingCreditGrantCategoryPaid)),
};
result, err := creditgrant.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

CreditGrantCreateParams params =
  CreditGrantCreateParams.builder()
    .setName("Purchased Credits")
    .setCustomer("cus_QrvQguzkIK8zTj")
    .setAmount(
      CreditGrantCreateParams.Amount.builder()
        .setMonetary(
          CreditGrantCreateParams.Amount.Monetary.builder()
            .setCurrency("usd")
            .setValue(1000L)
            .build()
        )
        .setType(CreditGrantCreateParams.Amount.Type.MONETARY)
        .build()
    )
    .setApplicabilityConfig(
      CreditGrantCreateParams.ApplicabilityConfig.builder()
        .setScope(
          CreditGrantCreateParams.ApplicabilityConfig.Scope.builder()
            .setPriceType(CreditGrantCreateParams.ApplicabilityConfig.Scope.PriceType.METERED)
            .build()
        )
        .build()
    )
    .setCategory(CreditGrantCreateParams.Category.PAID)
    .build();

CreditGrant creditGrant = CreditGrant.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const creditGrant = await stripe.billing.creditGrants.create({
  name: 'Purchased Credits',
  customer: 'cus_QrvQguzkIK8zTj',
  amount: {
    monetary: {
      currency: 'usd',
      value: 1000,
    },
    type: 'monetary',
  },
  applicability_config: {
    scope: {
      price_type: 'metered',
    },
  },
  category: 'paid',
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

credit_grant = stripe.billing.CreditGrant.create(
  name="Purchased Credits",
  customer="cus_QrvQguzkIK8zTj",
  amount={"monetary": {"currency": "usd", "value": 1000}, "type": "monetary"},
  applicability_config={"scope": {"price_type": "metered"}},
  category="paid",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$creditGrant = $stripe->billing->creditGrants->create([
  'name' => 'Purchased Credits',
  'customer' => 'cus_QrvQguzkIK8zTj',
  'amount' => [
    'monetary' => [
      'currency' => 'usd',
      'value' => 1000,
    ],
    'type' => 'monetary',
  ],
  'applicability_config' => ['scope' => ['price_type' => 'metered']],
  'category' => 'paid',
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

credit_grant = Stripe::Billing::CreditGrant.create({
  name: 'Purchased Credits',
  customer: 'cus_QrvQguzkIK8zTj',
  amount: {
    monetary: {
      currency: 'usd',
      value: 1000,
    },
    type: 'monetary',
  },
  applicability_config: {scope: {price_type: 'metered'}},
  category: 'paid',
})
```

### Response

```json
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
  "priority": null,
  "test_clock": null,
  "updated": 1726620803
}
```