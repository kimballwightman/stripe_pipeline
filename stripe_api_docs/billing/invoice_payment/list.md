# List all payments for an invoice

When retrieving an invoice, there is an includable payments property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of payments.

A dictionary with a `data` property that contains an array of up to `limit` invoice payments, starting after invoice payment `starting_after`. Each entry in the array is a separate [invoice_payment object](https://docs.stripe.com/docs/api/invoices/payments.md). If no more invoice payments are available, the resulting array will be empty.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `invoice` (string, optional)
  The identifier of the invoice whose payments to return.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `payment` (object, optional)
  The payment details of the invoice payments to return.

  - `payment.type` (enum, required)
    Only return invoice payments associated by this payment type.

    Indicates that a `PaymentIntent` object is being associated with this invoice payment.

  - `payment.payment_intent` (string, optional)
    Only return invoice payments associated by this payment intent ID.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  The status of the invoice payments to return.

  The payment has been canceled; it will not be credited to the invoice.

  The payment is incomplete and isn’t credited to the invoice. More fine-grained information available on the payment intent

  The payment is complete and has been credited to the invoice.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new InvoicePaymentListOptions { Invoice = "in_103Q0w2eZvKYlo2C5PYwf6Wf" };
var service = new InvoicePaymentService();
StripeList<InvoicePayment> invoicePayments = service.List(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.InvoicePaymentListParams{Invoice: stripe.String("in_103Q0w2eZvKYlo2C5PYwf6Wf")};
result := invoicepayment.List(params);
```

```java
Stripe.apiKey = "<<secret key>>";

InvoicePaymentListParams params =
  InvoicePaymentListParams.builder().setInvoice("in_103Q0w2eZvKYlo2C5PYwf6Wf").build();

InvoicePaymentCollection invoicePayments = InvoicePayment.list(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const invoicePayments = await stripe.invoicePayments.list({
  invoice: 'in_103Q0w2eZvKYlo2C5PYwf6Wf',
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

invoice_payments = stripe.InvoicePayment.list(invoice="in_103Q0w2eZvKYlo2C5PYwf6Wf")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$invoicePayments = $stripe->invoicePayments->all(['invoice' => 'in_103Q0w2eZvKYlo2C5PYwf6Wf']);
```

```ruby
Stripe.api_key = '<<secret key>>'

invoice_payments = Stripe::InvoicePayment.list({invoice: 'in_103Q0w2eZvKYlo2C5PYwf6Wf'})
```

### Response

```json
{
  "object": "list",
  "url": "/v1/invoice_payments",
  "has_more": false,
  "data": [
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
  ]
}
```