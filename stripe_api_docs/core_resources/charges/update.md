# Update a charge

Updates the specified charge by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

Returns the charge object if the update succeeded. This call will raise [an error](#errors) if update parameters are invalid.

- `customer` (string, optional)
  The ID of an existing customer that will be associated with this request. This field may only be updated if there is no existing associated customer with this charge.

- `description` (string, optional)
  An arbitrary string which you can attach to a charge object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the `description` of the charge(s) that they are describing.

- `fraud_details` (object, optional)
  A set of key-value pairs you can attach to a charge giving information about its riskiness. If you believe a charge is fraudulent, include a `user_report` key with a value of `fraudulent`. If you believe a charge is safe, include a `user_report` key with a value of `safe`. Stripe will use the information you send to improve our fraud detection algorithms.

  - `fraud_details.user_report` (string, required)
    Either `safe` or `fraudulent`.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `receipt_email` (string, optional)
  This is the email address that the receipt for this charge will be sent to. If this field is updated, then a new email receipt will be sent to the updated address.

- `shipping` (object, optional)
  Shipping information for the charge. Helps prevent fraud on charges for physical goods.

  - `shipping.address` (object, required)
    Shipping address.

    - `shipping.address.city` (string, optional)
      City, district, suburb, town, or village.

    - `shipping.address.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `shipping.address.line1` (string, optional)
      Address line 1 (e.g., street, PO Box, or company name).

    - `shipping.address.line2` (string, optional)
      Address line 2 (e.g., apartment, suite, unit, or building).

    - `shipping.address.postal_code` (string, optional)
      ZIP or postal code.

    - `shipping.address.state` (string, optional)
      State, county, province, or region.

  - `shipping.name` (string, required)
    Recipient name.

  - `shipping.carrier` (string, optional)
    The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc.

  - `shipping.phone` (string, optional)
    Recipient phone (including extension).

  - `shipping.tracking_number` (string, optional)
    The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.

- `transfer_group` (string, optional)
  A string that identifies this transaction as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](https://docs.stripe.com/docs/connect/separate-charges-and-transfers.md#transfer-options) for details.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new ChargeUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "shipping", "express" } },
};
var service = new ChargeService();
Charge charge = service.Update("ch_3MmlLrLkdIwHu7ix0snN0B15", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.ChargeParams{};
params.AddMetadata("shipping", "express")
result, err := charge.Update("ch_3MmlLrLkdIwHu7ix0snN0B15", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Charge resource = Charge.retrieve("ch_3MmlLrLkdIwHu7ix0snN0B15");

ChargeUpdateParams params = ChargeUpdateParams.builder().putMetadata("shipping", "express").build();

Charge charge = resource.update(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const charge = await stripe.charges.update(
  'ch_3MmlLrLkdIwHu7ix0snN0B15',
  {
    metadata: {
      shipping: 'express',
    },
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

charge = stripe.Charge.modify(
  "ch_3MmlLrLkdIwHu7ix0snN0B15",
  metadata={"shipping": "express"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$charge = $stripe->charges->update(
  'ch_3MmlLrLkdIwHu7ix0snN0B15',
  ['metadata' => ['shipping' => 'express']]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

charge = Stripe::Charge.update('ch_3MmlLrLkdIwHu7ix0snN0B15', {metadata: {shipping: 'express'}})
```

### Response

```json
{
  "id": "ch_3MmlLrLkdIwHu7ix0snN0B15",
  "object": "charge",
  "amount": 1099,
  "amount_captured": 1099,
  "amount_refunded": 0,
  "application": null,
  "application_fee": null,
  "application_fee_amount": null,
  "balance_transaction": "txn_3MmlLrLkdIwHu7ix0uke3Ezy",
  "billing_details": {
    "address": {
      "city": null,
      "country": null,
      "line1": null,
      "line2": null,
      "postal_code": null,
      "state": null
    },
    "email": null,
    "name": null,
    "phone": null
  },
  "calculated_statement_descriptor": "Stripe",
  "captured": true,
  "created": 1679090539,
  "currency": "usd",
  "customer": null,
  "description": null,
  "disputed": false,
  "failure_balance_transaction": null,
  "failure_code": null,
  "failure_message": null,
  "fraud_details": {},
  "livemode": false,
  "metadata": {
    "shipping": "express"
  },
  "on_behalf_of": null,
  "outcome": {
    "network_status": "approved_by_network",
    "reason": null,
    "risk_level": "normal",
    "risk_score": 32,
    "seller_message": "Payment complete.",
    "type": "authorized"
  },
  "paid": true,
  "payment_intent": null,
  "payment_method": "card_1MmlLrLkdIwHu7ixIJwEWSNR",
  "payment_method_details": {
    "card": {
      "brand": "visa",
      "checks": {
        "address_line1_check": null,
        "address_postal_code_check": null,
        "cvc_check": null
      },
      "country": "US",
      "exp_month": 3,
      "exp_year": 2024,
      "fingerprint": "mToisGZ01V71BCos",
      "funding": "credit",
      "installments": null,
      "last4": "4242",
      "mandate": null,
      "network": "visa",
      "network_token": {
        "used": false
      },
      "three_d_secure": null,
      "wallet": null
    },
    "type": "card"
  },
  "receipt_email": null,
  "receipt_number": null,
  "receipt_url": "https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KPDLl6UGMgawkab5iK86LBYtkq0XrhiQf1RsA2ubesH4GHiixEU8_1-Wp7h4oQEdfSUGiZpJwtQHBErT",
  "refunded": false,
  "refunds": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/charges/ch_3MmlLrLkdIwHu7ix0snN0B15/refunds"
  },
  "review": null,
  "shipping": null,
  "source_transfer": null,
  "statement_descriptor": null,
  "statement_descriptor_suffix": null,
  "status": "succeeded",
  "transfer_data": null,
  "transfer_group": null
}
```