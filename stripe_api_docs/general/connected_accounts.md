# Connected Accounts

To act as connected accounts, clients can issue requests using the `Stripe-Account` special header. Make sure that this header contains a Stripe account ID, which usually starts with the `acct_` prefix.

The value is set per-request as shown in the adjacent code sample. Methods on the returned object reuse the same account ID.

```sh
curl https://api.stripe.com/v1/charges/ch_3LmjFA2eZvKYlo2C09TLIsrw \
  -u <<secret key>>: \
  -H "Stripe-Account: acct_1032D82eZvKYlo2C" \
  -G
```

### Global API Key

```ruby
require 'stripe'
charge = Stripe::Charge.retrieve(
  'ch_3Lmjo22eZvKYlo2C1kuO4yZM',
  {
    stripe_account: 'acct_1032D82eZvKYlo2C',
  }
)
charge.capture # Uses the same account.
```

```sh
stripe charges retrieve ch_3LmjIH2eZvKYlo2C067UssSm \
    --stripe-account acct_1032D82eZvKYlo2C
```

```python
import stripe
charge = stripe.Charge.retrieve(
  "ch_3Lmjoz2eZvKYlo2C1rBER4Dk",
  stripe_account="acct_1032D82eZvKYlo2C"
)
charge.capture() # Uses the same account.
```

```php
$ch = $stripe->charges->retrieve(
  'ch_3Lmjrl2eZvKYlo2C1bscjw8Z',
  [],
  ['stripe_account' => 'acct_1032D82eZvKYlo2C']
);
$ch->capture(); // Uses the same account.
```

```java
RequestOptions requestOptions = RequestOptions.builder()
  .setStripeAccount("acct_1032D82eZvKYlo2C")
  .build();

Charge charge = Charge.retrieve(
  "ch_3LmjsM2eZvKYlo2C1CcKvJbn",
  requestOptions,
);

```

```javascript
stripe.charges.retrieve('ch_3LmjSR2eZvKYlo2C1cPZxlbL', {
  stripeAccount: 'acct_1032D82eZvKYlo2C'
});
```

```go
params := &stripe.ChargeParams{}
params.SetStripeAccount("acct_1032D82eZvKYlo2C")
ch, err := charge.Get("ch_3Lmjso2eZvKYlo2C0rTTv0MK", params)
```

```dotnet
var options = new RequestOptions
{
  StripeAccount = "acct_1032D82eZvKYlo2C"
};
var service = new ChargeService();
Charge charge = service.Get(
  "ch_3LmjRC2eZvKYlo2C1vvMTc1Q",
  options
);
```