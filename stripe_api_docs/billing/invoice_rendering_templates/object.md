# The Invoice Rendering Template object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (nullable object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `nickname` (nullable string)
  A brief description of the template, hidden from customers

- `status` (enum)
  The status of the template, one of `active` or `archived`.

- `version` (integer)
  Version of this template; version increases by one when an update on the template changes any field that controls invoice rendering

### The Invoice Rendering Template object

```json
{
  "id": "inrtem_abc",
  "object": "invoice_rendering_template",
  "nickname": "My Invoice Template",
  "status": "active",
  "version": 1,
  "created": 1678942624,
  "livemode": false
}
```