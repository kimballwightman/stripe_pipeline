# Create a file link

Creates a new file link object.

Returns the file link object if successful and raises [an error](#errors) otherwise.

- `file` (string, required)
  The ID of the file. The file’s `purpose` must be one of the following: `business_icon`, `business_logo`, `customer_signature`, `dispute_evidence`, `finance_report_run`, `financial_account_statement`, `identity_document_downloadable`, `issuing_regulatory_reporting`, `pci_document`, `selfie`, `sigma_scheduled_query`, `tax_document_user_upload`, or `terminal_reader_splashscreen`.

- `expires_at` (timestamp, optional)
  The link isn’t usable after this future timestamp.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new FileLinkCreateOptions { File = "file_1Mr23iLkdIwHu7ixQkCV3CBR" };
var service = new FileLinkService();
FileLink fileLink = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.FileLinkParams{File: stripe.String("file_1Mr23iLkdIwHu7ixQkCV3CBR")};
result, err := filelink.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

FileLinkCreateParams params =
  FileLinkCreateParams.builder().setFile("file_1Mr23iLkdIwHu7ixQkCV3CBR").build();

FileLink fileLink = FileLink.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const fileLink = await stripe.fileLinks.create({
  file: 'file_1Mr23iLkdIwHu7ixQkCV3CBR',
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

file_link = stripe.FileLink.create(file="file_1Mr23iLkdIwHu7ixQkCV3CBR")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$fileLink = $stripe->fileLinks->create(['file' => 'file_1Mr23iLkdIwHu7ixQkCV3CBR']);
```

```ruby
Stripe.api_key = '<<secret key>>'

file_link = Stripe::FileLink.create({file: 'file_1Mr23iLkdIwHu7ixQkCV3CBR'})
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