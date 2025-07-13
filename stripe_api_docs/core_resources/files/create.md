# Create a file

To upload a file to Stripe, you need to send a request of type `multipart/form-data`. Include the file you want to upload in the request, and the parameters for creating a file.

All of Stripe’s officially supported Client libraries support sending `multipart/form-data`.

Returns the file object.

- `file` (object, required)
  A file to upload. Make sure that the specifications follow RFC 2388, which defines file transfers for the `multipart/form-data` protocol.

- `purpose` (enum, required)
  The [purpose](https://docs.stripe.com/docs/file-upload.md#uploading-a-file) of the uploaded file.

  Additional documentation requirements that can be requested for an account.

  Additional verification for custom accounts.

  A business icon.

  A business logo.

  Customer signature image.

  Evidence to submit with a dispute response.

  A document to verify the identity of an account owner during account provisioning.

  Additional regulatory reporting requirements for Issuing.

  A self-assessment PCI questionnaire.

  A user-uploaded tax document.

  Splashscreen to be displayed on Terminal readers.

- `file_link_data` (object, optional)
  Optional parameters that automatically create a [file link](#file_links) for the newly created file.

  - `file_link_data.create` (boolean, required)
    Set this to `true` to create a file link for the newly created file. Creating a link is only possible when the file’s `purpose` is one of the following: `business_icon`, `business_logo`, `customer_signature`, `dispute_evidence`, `issuing_regulatory_reporting`, `pci_document`, `tax_document_user_upload`, or `terminal_reader_splashscreen`.

  - `file_link_data.expires_at` (timestamp, optional)
    The link isn’t available after this future timestamp.

  - `file_link_data.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

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