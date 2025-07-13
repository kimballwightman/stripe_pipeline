# Unarchive an invoice rendering template

Unarchive an invoice rendering template so it can be used on new Stripe objects again.

The updated template object is returned if successful. Otherwise, this call raises [an error](#errors).


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new InvoiceRenderingTemplateService();
InvoiceRenderingTemplate invoiceRenderingTemplate = service.Unarchive("inrtem_abc");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.InvoiceRenderingTemplateUnarchiveParams{};
result, err := invoicerenderingtemplate.Unarchive("inrtem_abc", params);
```

```java
Stripe.apiKey = "<<secret key>>";

InvoiceRenderingTemplate resource = InvoiceRenderingTemplate.retrieve("inrtem_abc");

InvoiceRenderingTemplateUnarchiveParams params =
  InvoiceRenderingTemplateUnarchiveParams.builder().build();

InvoiceRenderingTemplate invoiceRenderingTemplate = resource.unarchive(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const invoiceRenderingTemplate = await stripe.invoiceRenderingTemplates.unarchive('inrtem_abc');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

invoice_rendering_template = stripe.InvoiceRenderingTemplate.unarchive("inrtem_abc")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$invoiceRenderingTemplate = $stripe->invoiceRenderingTemplates->unarchive('inrtem_abc', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

invoice_rendering_template = Stripe::InvoiceRenderingTemplate.unarchive('inrtem_abc')
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