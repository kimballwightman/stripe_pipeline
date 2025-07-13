# Retrieve an invoice rendering template

Retrieves an invoice rendering template with the given ID. It by default returns the latest version of the template. Optionally, specify a version to see previous versions.

Returns an [invoice_payment](https://docs.stripe.com/docs/api/invoices/payments.md) object if a valid invoice payment ID and matching invoice ID were provided. Otherwise, this call raises [an error](#errors).


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new InvoiceRenderingTemplateService();
InvoiceRenderingTemplate invoiceRenderingTemplate = service.Get("inrtem_abc");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.InvoiceRenderingTemplateParams{};
result, err := invoicerenderingtemplate.Get("inrtem_abc", params);
```

```java
Stripe.apiKey = "<<secret key>>";

InvoiceRenderingTemplate invoiceRenderingTemplate = InvoiceRenderingTemplate.retrieve("inrtem_abc");
```

```node
const stripe = require('stripe')('<<secret key>>');

const invoiceRenderingTemplate = await stripe.invoiceRenderingTemplates.retrieve('inrtem_abc');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

invoice_rendering_template = stripe.InvoiceRenderingTemplate.retrieve("inrtem_abc")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$invoiceRenderingTemplate = $stripe->invoiceRenderingTemplates->retrieve('inrtem_abc', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

invoice_rendering_template = Stripe::InvoiceRenderingTemplate.retrieve('inrtem_abc')
```

### Response

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