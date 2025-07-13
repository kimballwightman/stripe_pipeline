# Retrieve a file link

Retrieves the file link with the given ID.

If the identifier you provide is valid, a file link object returns. If not, Stripe raises [an error](#errors).


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new FileLinkService();
FileLink fileLink = service.Get("link_1Mr23jLkdIwHu7ix65betcoo");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.FileLinkParams{};
result, err := filelink.Get("link_1Mr23jLkdIwHu7ix65betcoo", params);
```

```java
Stripe.apiKey = "<<secret key>>";

FileLink fileLink = FileLink.retrieve("link_1Mr23jLkdIwHu7ix65betcoo");
```

```node
const stripe = require('stripe')('<<secret key>>');

const fileLink = await stripe.fileLinks.retrieve('link_1Mr23jLkdIwHu7ix65betcoo');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

file_link = stripe.FileLink.retrieve("link_1Mr23jLkdIwHu7ix65betcoo")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$fileLink = $stripe->fileLinks->retrieve('link_1Mr23jLkdIwHu7ix65betcoo', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

file_link = Stripe::FileLink.retrieve('link_1Mr23jLkdIwHu7ix65betcoo')
```

### Response

```json
{
  "id": "link_1Mr23jLkdIwHu7ix65betcoo",
  "object": "file_link",
  "created": 1680108075,
  "expired": false,
  "expires_at": null,
  "file": "file_1Mr23iLkdIwHu7ixQkCV3CBR",
  "livemode": false,
  "metadata": {},
  "url": "https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"
}
```