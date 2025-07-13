# List all file links

Returns a list of file links.

A dictionary with a `data` property that contains an array of up to `limit` file links, starting after the `starting_after` file link. Each entry in the array is a separate file link object. If there aren’t additional available file links, the resulting array is empty.

- `created` (object, optional)
  Only return links that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `expired` (boolean, optional)
  Filter links by their expiration status. By default, Stripe returns all links.

- `file` (string, optional)
  Only return links for the given file.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new FileLinkListOptions { Limit = 3 };
var service = new FileLinkService();
StripeList<FileLink> fileLinks = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.FileLinkListParams{};
params.Limit = stripe.Int64(3)
result := filelink.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

FileLinkListParams params = FileLinkListParams.builder().setLimit(3L).build();

FileLinkCollection fileLinks = FileLink.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const fileLinks = await stripe.fileLinks.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

file_links = stripe.FileLink.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$fileLinks = $stripe->fileLinks->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

file_links = Stripe::FileLink.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/file_links",
  "has_more": false,
  "data": [
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
  ]
}
```