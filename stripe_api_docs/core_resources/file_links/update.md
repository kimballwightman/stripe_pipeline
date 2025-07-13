# Update a file link

Updates an existing file link object. Expired links can no longer be updated.

Returns the file link object if successful, and raises [an error](#errors) otherwise.

- `expires_at` (string | timestamp, optional)
  A future timestamp after which the link will no longer be usable, or `now` to expire the link immediately.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new FileLinkUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var service = new FileLinkService();
FileLink fileLink = service.Update("link_1Mr23jLkdIwHu7ix65betcoo", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.FileLinkParams{};
params.AddMetadata("order_id", "6735")
result, err := filelink.Update("link_1Mr23jLkdIwHu7ix65betcoo", params);
```

```java
Stripe.apiKey = "<<secret key>>";

FileLink resource = FileLink.retrieve("link_1Mr23jLkdIwHu7ix65betcoo");

FileLinkUpdateParams params =
  FileLinkUpdateParams.builder().putMetadata("order_id", "6735").build();

FileLink fileLink = resource.update(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const fileLink = await stripe.fileLinks.update(
  'link_1Mr23jLkdIwHu7ix65betcoo',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

file_link = stripe.FileLink.modify(
  "link_1Mr23jLkdIwHu7ix65betcoo",
  metadata={"order_id": "6735"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$fileLink = $stripe->fileLinks->update(
  'link_1Mr23jLkdIwHu7ix65betcoo',
  ['metadata' => ['order_id' => '6735']]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

file_link = Stripe::FileLink.update('link_1Mr23jLkdIwHu7ix65betcoo', {metadata: {order_id: '6735'}})
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
  "metadata": {
    "order_id": "6735"
  },
  "url": "https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"
}
```