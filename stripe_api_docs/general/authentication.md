# Authentication

The Stripe API uses [API keys](https://docs.stripe.com/keys.md) to authenticate requests. You can view and manage your API keys in [the Stripe Dashboard](https://dashboard.stripe.com/login?redirect=/apikeys).

Test mode secret keys have the prefix `sk_test_` and live mode secret keys have the prefix `sk_live_`. Alternatively, you can use [restricted API keys](https://docs.stripe.com/keys.md#limit-access) for granular permissions.

Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, and so forth.

All API requests must be made over [HTTPS](http://en.wikipedia.org/wiki/HTTP_Secure). Calls made over plain HTTP will fail. API requests without authentication will also fail.

```sh
curl https://api.stripe.com/v1/charges \
  -u <<secret key>>:
# The colon prevents curl from asking for a password.
```

### Global API Key

```javascript
const Stripe = require('stripe');
const stripe = Stripe('<<secret key>>');
```

### Per-Request API Key

```javascript
var charge = await stripe.charges.retrieve(
  'ch_3LiiC52eZvKYlo2C1da66ZSQ',
  {
    apiKey: '<<secret key>>'
  }
);
```

```
stripe login
```

### Global API Key

```ruby
require 'stripe'
Stripe.api_key = '<<secret key>>'
```

### Per-Request API Key

```ruby
require 'stripe'
charge = Stripe::Charge.retrieve(
  'ch_3Ln3cj2eZvKYlo2C1lcnB8f6',
  {
    api_key: '<<secret key>>',
  }
)
charge.capture # Uses the same API Key.
```

### Global API Key

```python
import stripe
stripe.api_key = "<<secret key>>"
```

### Per-Request API Key

```python
import stripe
charge = stripe.Charge.retrieve(
  "ch_3Ln3e92eZvKYlo2C0eUfv7bi",
  api_key="<<secret key>>"
)
charge.capture() # Uses the same API Key.
```

### Global API Key

```php
$stripe = new \Stripe\StripeClient("<<secret key>>");
```

### Per-Request API Key

```php
$ch = $stripe->charges->retrieve(
  'ch_3Ln3fO2eZvKYlo2C1kqP3AMr',
  [],
  ['api_key' => '<<secret key>>']
);
$ch->capture(); // Uses the same API Key.
```

### Global API Key

```java
Stripe.apiKey = "<<secret key>>";
```

### Per-Request API Key

```java
RequestOptions requestOptions = RequestOptions.builder()
  .setApiKey("<<secret key>>")
  .build();

Charge charge = Charge.retrieve(
  "ch_3Ln3ga2eZvKYlo2C11iwHdxy",
  requestOptions,
);

```

### Global API Key

```go
stripe.Key = "<<secret key>>"
```

### Per-Request API Key

```go
params := &stripe.ChargeParams{}
sc := &client.API{}
sc.Init("<<secret key>>", nil)
sc.Charges.Get("ch_3Ln3j02eZvKYlo2C0d5IZWuG", params)
```

### Global API Key

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";
```

### Per-Request API Key

```dotnet
var options = new RequestOptions
{
  ApiKey = "<<secret key>>"
};
var service = new ChargeService();
Charge charge = service.Get(
  "ch_3Ln3kB2eZvKYlo2C1YRBr0Ll",
  options
);
```