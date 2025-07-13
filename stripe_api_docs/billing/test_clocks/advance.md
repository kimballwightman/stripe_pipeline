# Advance a test clock

Starts advancing a test clock to a specified time in the future. Advancement is done when status changes to `Ready`.

A `TestClock` object with status `Advancing` is returned upon success. Otherwise, this call raises [an error](#errors).

- `frozen_time` (timestamp, required)
  The time to advance the test clock. Must be after the test clock’s current frozen time. Cannot be more than two intervals in the future from the shortest subscription in this test clock. If there are no subscriptions in this test clock, it cannot be more than two years in the future.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new Stripe.TestHelpers.TestClockAdvanceOptions
{
    FrozenTime = DateTimeOffset.FromUnixTimeSeconds(1680199613).UtcDateTime,
};
var service = new Stripe.TestHelpers.TestClockService();
Stripe.TestHelpers.TestClock testClock = service.Advance("clock_1Mr3I22eZvKYlo2Ck0rgMqd7", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TestHelpersTestClockAdvanceParams{FrozenTime: stripe.Int64(1680199613)};
result, err := testclock.Advance("clock_1Mr3I22eZvKYlo2Ck0rgMqd7", params);
```

```java
Stripe.apiKey = "<<secret key>>";

TestClock resource = TestClock.retrieve("clock_1Mr3I22eZvKYlo2Ck0rgMqd7");

TestClockAdvanceParams params = TestClockAdvanceParams.builder().setFrozenTime(1680199613L).build();

TestClock testClock = resource.advance(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const testClock = await stripe.testHelpers.testClocks.advance(
  'clock_1Mr3I22eZvKYlo2Ck0rgMqd7',
  {
    frozen_time: 1680199613,
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

test_clock = stripe.test_helpers.TestClock.advance(
  "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",
  frozen_time=1680199613,
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$testClock = $stripe->testHelpers->testClocks->advance(
  'clock_1Mr3I22eZvKYlo2Ck0rgMqd7',
  ['frozen_time' => 1680199613]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

test_clock = Stripe::TestHelpers::TestClock.advance(
  'clock_1Mr3I22eZvKYlo2Ck0rgMqd7',
  {frozen_time: 1680199613},
)
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
  "status": "advancing"
}
```