# List all invoice rendering templates

List all templates, ordered by creation date, with the most recently created template appearing first.

A dictionary with a `data` property that contains an array of up to `limit` templates, starting after template `starting_after`. Each entry in the array is a separate template object. If no more templates are available, the resulting array will be empty.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new InvoiceRenderingTemplateListOptions { Limit = 3 };
var service = new InvoiceRenderingTemplateService();
StripeList<InvoiceRenderingTemplate> invoiceRenderingTemplates = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.InvoiceRenderingTemplateListParams{};
params.Limit = stripe.Int64(3)
result := invoicerenderingtemplate.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

InvoiceRenderingTemplateListParams params =
  InvoiceRenderingTemplateListParams.builder().setLimit(3L).build();

InvoiceRenderingTemplateCollection invoiceRenderingTemplates =
  InvoiceRenderingTemplate.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const invoiceRenderingTemplates = await stripe.invoiceRenderingTemplates.list({
  limit: 3,
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

invoice_rendering_templates = stripe.InvoiceRenderingTemplate.list(limit=3)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$invoiceRenderingTemplates = $stripe->invoiceRenderingTemplates->all(['limit' => 3]);
```

```ruby
Stripe.api_key = '<<secret key>>'

invoice_rendering_templates = Stripe::InvoiceRenderingTemplate.list({limit: 3})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/invoice_rendering_templates",
  "has_more": false,
  "data": [
    {
      "id": "inrtem_abc",
      "object": "invoice_rendering_template",
      "nickname": "My Invoice Template",
      "status": "active",
      "version": 1,
      "created": 1678942624,
      "livemode": false
    }
  ]
}
```