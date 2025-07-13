# Versioning

Each major release, such as [Acacia](https://docs.stripe.com/changelog/acacia.md), includes changes that aren’t [backward-compatible](https://docs.stripe.com/upgrades.md#what-changes-does-stripe-consider-to-be-backward-compatible) with previous releases. Upgrading to a new major release can require updates to existing code. Each monthly release includes only backward-compatible changes, and uses the same name as the last major release. You can safely upgrade to a new monthly release without breaking any existing code. The current version is 2025-06-30.basil. For information on all API versions, view our [API changelog](https://docs.stripe.com/changelog.md).

You can upgrade your API version in [Workbench](https://dashboard.stripe.com/workbench). As a precaution, use API versioning to test a new API version before committing to an upgrade.

```sh
curl https://api.stripe.com/v1/charges \
  -u <<secret key>>: \
  -H "Stripe-Version: 2025-06-30.basil"
```

```ruby
require 'stripe'
Stripe.api_key = '<<secret key>>'
Stripe.api_version = '2025-06-30.basil'
```

```sh
stripe charges create --stripe-version 2025-06-30.basil
```

```python
import stripe
stripe.api_key = "<<secret key>>"
stripe.api_version = "2025-06-30.basil"
```

```php
$stripe = new \Stripe\StripeClient([
  "api_key" => "<<secret key>>",
  "stripe_version" => "2025-06-30.basil"
]);
```

```java
Stripe.apiKey = "<<secret key>>";
// Since Java is strongly typed,
// the version is fixed in the library.
```

```javascript
const stripe = require('stripe')('<<secret key>>', {
  apiVersion: '2025-06-30.basil',
});
```

```go
stripe.Key = "<<secret key>>"
// Since Go is strongly typed,
// the version is fixed in the library.
```

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";
// Since C# is strongly typed,
// the version is fixed in the library.
```