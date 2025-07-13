# Retrieve an InvoicePayment

Retrieves the invoice payment with the given ID.

Returns an [invoice_payment](https://docs.stripe.com/docs/api/invoices/payments.md) object if a valid invoice payment ID was provided. Otherwise, this call raises [an error](#errors).


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new InvoicePaymentService();
InvoicePayment invoicePayment = service.Get("inpay_1M3USa2eZvKYlo2CBjuwbq0N");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.InvoicePaymentParams{};
result, err := invoicepayment.Get("inpay_1M3USa2eZvKYlo2CBjuwbq0N", params);
```

```java
Stripe.apiKey = "<<secret key>>";

InvoicePayment invoicePayment = InvoicePayment.retrieve("inpay_1M3USa2eZvKYlo2CBjuwbq0N");
```

```node
const stripe = require('stripe')('<<secret key>>');

const invoicePayment = await stripe.invoicePayments.retrieve('inpay_1M3USa2eZvKYlo2CBjuwbq0N');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

invoice_payment = stripe.InvoicePayment.retrieve("inpay_1M3USa2eZvKYlo2CBjuwbq0N")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$invoicePayment = $stripe->invoicePayments->retrieve('inpay_1M3USa2eZvKYlo2CBjuwbq0N', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

invoice_payment = Stripe::InvoicePayment.retrieve('inpay_1M3USa2eZvKYlo2CBjuwbq0N')
```

### Response

```json
{
  "id": "inpay_1M3USa2eZvKYlo2CBjuwbq0N",
  "object": "invoice_payment",
  "amount_paid": 2000,
  "amount_requested": 2000,
  "created": 1391288554,
  "currency": "usd",
  "invoice": "in_103Q0w2eZvKYlo2C5PYwf6Wf",
  "is_default": true,
  "livemode": false,
  "payment": {
    "type": "payment_intent",
    "payment_intent": "pi_103Q0w2eZvKYlo2C364X582Z"
  },
  "status": "paid",
  "status_transitions": {
    "canceled_at": null,
    "paid_at": 1391288554
  }
}
```