# Create a test clock

Creates a new test clock that can be attached to new customers and quotes.

The newly created `TestClock` object is returned upon success. Otherwise, this call raises [an error](#errors).

- `frozen_time` (timestamp, required)
  The initial frozen time for this test clock.

- `name` (string, optional)
  The name for this test clock.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new Stripe.TestHelpers.TestClockCreateOptions
{
    FrozenTime = DateTimeOffset.FromUnixTimeSeconds(1577836800).UtcDateTime,
};
var service = new Stripe.TestHelpers.TestClockService();
Stripe.TestHelpers.TestClock testClock = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TestHelpersTestClockParams{FrozenTime: stripe.Int64(1577836800)};
result, err := testclock.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

TestClockCreateParams params = TestClockCreateParams.builder().setFrozenTime(1577836800L).build();

TestClock testClock = TestClock.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const testClock = await stripe.testHelpers.testClocks.create({
  frozen_time: 1577836800,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

test_clock = stripe.test_helpers.TestClock.create(frozen_time=1577836800)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$testClock = $stripe->testHelpers->testClocks->create(['frozen_time' => 1577836800]);
```

```ruby
Stripe.api_key = '<<secret key>>'

test_clock = Stripe::TestHelpers::TestClock.create({frozen_time: 1577836800})
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