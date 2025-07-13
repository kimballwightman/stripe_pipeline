# Update a cash balance's settings

Changes the settings on a customer’s cash balance.

The customer’s cash balance, with the updated settings.

- `settings` (object, optional)
  A hash of settings for this cash balance.

  - `settings.reconciliation_mode` (enum, optional)
    Controls how funds transferred by the customer are applied to payment intents and invoices. Valid options are `automatic`, `manual`, or `merchant_default`. For more information about these reconciliation modes, see [Reconciliation](https://docs.stripe.com/docs/payments/customer-balance/reconciliation.md).

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CustomerCashBalanceUpdateOptions
{
    Settings = new CustomerCashBalanceSettingsOptions { ReconciliationMode = "manual" },
};
var service = new CustomerCashBalanceService();
CashBalance cashBalance = service.Update("cus_Ob4Xiw8KXOqcvM", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CashBalanceParams{
  Settings: &stripe.CashBalanceSettingsParams{
    ReconciliationMode: stripe.String(string(stripe.CashBalanceSettingsReconciliationModeManual)),
  },
  Customer: stripe.String("cus_Ob4Xiw8KXOqcvM"),
};
result, err := cashbalance.Update(params);
```

```java
Stripe.apiKey = "<<secret key>>";

CashBalance resource = CashBalance.retrieve("cus_Ob4Xiw8KXOqcvM");

CashBalanceUpdateParams params =
  CashBalanceUpdateParams.builder()
    .setSettings(
      CashBalanceUpdateParams.Settings.builder()
        .setReconciliationMode(CashBalanceUpdateParams.Settings.ReconciliationMode.MANUAL)
        .build()
    )
    .build();

CashBalance cashBalance = resource.update(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const cashBalance = await stripe.customers.updateCashBalance(
  'cus_Ob4Xiw8KXOqcvM',
  {
    settings: {
      reconciliation_mode: 'manual',
    },
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

cash_balance = stripe.Customer.modify_cash_balance(
  "cus_Ob4Xiw8KXOqcvM",
  settings={"reconciliation_mode": "manual"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$cashBalance = $stripe->customers->updateCashBalance(
  'cus_Ob4Xiw8KXOqcvM',
  ['settings' => ['reconciliation_mode' => 'manual']]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

cash_balance = Stripe::Customer.update_cash_balance(
  'cus_Ob4Xiw8KXOqcvM',
  {settings: {reconciliation_mode: 'manual'}},
)
```

### Response

```json
{
  "object": "cash_balance",
  "available": null,
  "customer": "cus_Ob4Xiw8KXOqcvM",
  "livemode": false,
  "settings": {
    "reconciliation_mode": "manual",
    "using_merchant_default": false
  }
}
```