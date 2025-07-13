# Retrieve a file

Retrieves the details of an existing file object. After you supply a unique file ID, Stripe returns the corresponding file object. Learn how to [access file contents](https://docs.stripe.com/docs/file-upload.md#download-file-contents).

If the identifier you provide is valid, a file object returns. If not, Stripe raises [an error](#errors).


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new FileService();
File file = service.Get("file_1Mr4LDLkdIwHu7ixFCz0dZiH");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.FileParams{};
result, err := file.Get("file_1Mr4LDLkdIwHu7ixFCz0dZiH", params);
```

```java
Stripe.apiKey = "<<secret key>>";

File file = File.retrieve("file_1Mr4LDLkdIwHu7ixFCz0dZiH");
```

```node
const stripe = require('stripe')('<<secret key>>');

const file = await stripe.files.retrieve('file_1Mr4LDLkdIwHu7ixFCz0dZiH');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

file = stripe.File.retrieve("file_1Mr4LDLkdIwHu7ixFCz0dZiH")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$file = $stripe->files->retrieve('file_1Mr4LDLkdIwHu7ixFCz0dZiH', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

file = Stripe::File.retrieve('file_1Mr4LDLkdIwHu7ixFCz0dZiH')
```

### Response

```json
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
```