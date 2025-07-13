# Download quote PDF

Download the PDF for a finalized quote. Explanation for special handling can be found [here](https://docs.stripe.com/quotes/overview#quote_pdf)

The PDF file for the quote.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new QuoteService();
service.Pdf("qt_0J1EnX589O8KAxCGEdmhZY3r");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.QuotePDFParams{};
result, err := quote.PDF("qt_0J1EnX589O8KAxCGEdmhZY3r", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Quote resource = Quote.retrieve("qt_0J1EnX589O8KAxCGEdmhZY3r");

QuotePdfParams params = QuotePdfParams.builder().build();

java.io.InputStream file = resource.pdf(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const file = await stripe.quotes.pdf('qt_0J1EnX589O8KAxCGEdmhZY3r');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

file = stripe.Quote.pdf("qt_0J1EnX589O8KAxCGEdmhZY3r")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$file = $stripe->quotes->pdf('qt_0J1EnX589O8KAxCGEdmhZY3r', function () {}, []);
```

```ruby
Stripe.api_key = '<<secret key>>'

block_handler = {}
file = Stripe::Quote.pdf('qt_0J1EnX589O8KAxCGEdmhZY3r', &block_handler)
```

### Response

```json
{}
```