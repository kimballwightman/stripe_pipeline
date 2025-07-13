# Retrieve a test clock

Retrieves a test clock.

Returns the `TestClock` object. Otherwise, this call raises [an error](#errors).


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new Stripe.TestHelpers.TestClockService();
Stripe.TestHelpers.TestClock testClock = service.Get("clock_1Mr3I22eZvKYlo2Ck0rgMqd7");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TestHelpersTestClockParams{};
result, err := testclock.Get("clock_1Mr3I22eZvKYlo2Ck0rgMqd7", params);
```

```java
Stripe.apiKey = "<<secret key>>";

TestClock testClock = TestClock.retrieve("clock_1Mr3I22eZvKYlo2Ck0rgMqd7");
```

```node
const stripe = require('stripe')('<<secret key>>');

const testClock = await stripe.testHelpers.testClocks.retrieve('clock_1Mr3I22eZvKYlo2Ck0rgMqd7');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

test_clock = stripe.test_helpers.TestClock.retrieve("clock_1Mr3I22eZvKYlo2Ck0rgMqd7")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$testClock = $stripe->testHelpers->testClocks->retrieve('clock_1Mr3I22eZvKYlo2Ck0rgMqd7', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

test_clock = Stripe::TestHelpers::TestClock.retrieve('clock_1Mr3I22eZvKYlo2Ck0rgMqd7')
```

### Response

```json
{
  "id": "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",
  "object": "test_helpers.test_clock",
  "created": 1680112806,
  "deletes_after": 1680717606,
  "frozen_time": 1577836800,
  "livemode": false,
  "name": null,
  "status": "ready"
}
```