 # List all files

Returns a list of the files that your account has access to. Stripe sorts and returns the files by their creation dates, placing the most recently created files at the top.

A dictionary with a `data` property that contains an array of up to `limit` files, starting after the `starting_after` file. Each entry in the array is a separate file object. If there aren’t additional available files, the resulting array is empty.

- `created` (object, optional)
  Only return files that were created during the given date interval.

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

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `purpose` (string, optional)
  Filter queries by the file purpose. If you don’t provide a purpose, the queries return unfiltered files.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new FileListOptions { Limit = 3 };
var service = new FileService();
StripeList<File> files = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.FileListParams{};
params.Limit = stripe.Int64(3)
result := file.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

FileListParams params = FileListParams.builder().setLimit(3L).build();

FileCollection files = File.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const files = await stripe.files.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

files = stripe.File.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$files = $stripe->files->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

files = Stripe::File.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/files",
  "has_more": false,
  "data": [
    {
      "id": "file_1Mr4LDLkdIwHu7ixFCz0dZiH",
      "object": "file",
      "created": 1680116847,
      "expires_at": 1703444847,
      "filename": "file.png",
      "links": {
        "object": "list",
        "data": [],
        "has_more": false,
        "url": "/v1/file_links?file=file_1Mr4LDLkdIwHu7ixFCz0dZiH"
      },
      "purpose": "dispute_evidence",
      "size": 8429,
      "title": null,
      "type": "png",
      "url": "https://files.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH/contents"
    }
  ]
}
```