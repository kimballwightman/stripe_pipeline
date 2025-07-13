# Delete a test clock

Deletes a test clock.

The deleted `TestClock` object is returned upon success. Otherwise, this call raises [an error](#errors).


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new Stripe.TestHelpers.TestClockService();
Stripe.TestHelpers.TestClock deleted = service.Delete("clock_1Mr3I22eZvKYlo2Ck0rgMqd7");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TestHelpersTestClockParams{};
result, err := testclock.Del("clock_1Mr3I22eZvKYlo2Ck0rgMqd7", params);
```

```java
Stripe.apiKey = "<<secret key>>";

TestClock resource = TestClock.retrieve("clock_1Mr3I22eZvKYlo2Ck0rgMqd7");

TestClock testClock = resource.delete();
```

```node
const stripe = require('stripe')('<<secret key>>');

const deleted = await stripe.testHelpers.testClocks.del('clock_1Mr3I22eZvKYlo2Ck0rgMqd7');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

deleted = stripe.test_helpers.TestClock.delete("clock_1Mr3I22eZvKYlo2Ck0rgMqd7")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$deleted = $stripe->testHelpers->testClocks->delete('clock_1Mr3I22eZvKYlo2Ck0rgMqd7', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

deleted = Stripe::TestHelpers::TestClock.delete('clock_1Mr3I22eZvKYlo2Ck0rgMqd7')
```

### Response

```json
{
  "id": "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",
  "object": "test_helpers.test_clock",
  "deleted": true
}
```