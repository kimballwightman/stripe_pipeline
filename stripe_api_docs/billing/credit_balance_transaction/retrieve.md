# Retrieve a credit balance transaction

Retrieves a credit balance transaction.

Returns a credit balance transaction.

- `id` (string, required)
  Unique identifier for the object.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new Stripe.Billing.CreditBalanceTransactionService();
Stripe.Billing.CreditBalanceTransaction creditBalanceTransaction = service.Get(
    "cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.BillingCreditBalanceTransactionParams{};
result, err := creditbalancetransaction.Get("cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue", params);
```

```java
Stripe.apiKey = "<<secret key>>";

CreditBalanceTransaction creditBalanceTransaction =
  CreditBalanceTransaction.retrieve("cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue");
```

```node
const stripe = require('stripe')('<<secret key>>');

const creditBalanceTransaction = await stripe.billing.creditBalanceTransactions.retrieve(
  'cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue'
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

credit_balance_transaction = stripe.billing.CreditBalanceTransaction.retrieve(
  "cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$creditBalanceTransaction = $stripe->billing->creditBalanceTransactions->retrieve(
  'cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue',
  []
);
```

```ruby
Stripe.api_key = '<<secret key>>'

credit_balance_transaction = Stripe::Billing::CreditBalanceTransaction.retrieve('cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue')
```

### Response

```json
{
  "id": "cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue",
  "object": "billing.credit_balance_transaction",
  "created": 1726619524,
  "credit": null,
  "credit_grant": "credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE",
  "debit": {
    "amount": {
      "monetary": {
        "currency": "usd",
        "value": 1000
      },
      "type": "monetary"
    },
    "credits_applied": {
      "invoice": "in_1Q0BoLL6nFOS1ekDbwBM5ER1",
      "invoice_line_item": "il_1QB443L6nFOS1ekDwRiN3Z4n"
    },
    "type": "credits_applied"
  },
  "effective_at": 1729211351,
  "livemode": false,
  "test_clock": "clock_1Q0BoJL6nFOS1ekDbyYYuseM",
  "type": "debit"
}
```