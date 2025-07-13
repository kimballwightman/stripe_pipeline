# The Source object

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `allow_redisplay` (nullable enum)
  This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to “unspecified”.

  Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

  Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

  This is the default value for payment methods where `allow_redisplay` wasn’t set.

- `amount` (nullable integer)
  A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for `single_use` sources.

- `client_secret` (string)
  The client secret of the source. Used for client-side retrieval using a publishable key.

- `code_verification` (nullable object)
  Information related to the code verification flow. Present if the source is authenticated by a verification code (`flow` is `code_verification`).

  - `code_verification.attempts_remaining` (integer)
    The number of attempts remaining to authenticate the source object with a verification code.

  - `code_verification.status` (string)
    The status of the code verification, either `pending` (awaiting verification, `attempts_remaining` should be greater than 0), `succeeded` (successful verification) or `failed` (failed verification, cannot be verified anymore as `attempts_remaining` should be 0).

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (nullable enum)
  Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) associated with the source. This is the currency for which the source will be chargeable once ready. Required for `single_use` sources.

- `customer` (nullable string)
  The ID of the customer to which this source is attached. This will not be present when the source has not been attached to a customer.

- `flow` (string)
  The authentication `flow` of the source. `flow` is one of `redirect`, `receiver`, `code_verification`, `none`.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (nullable object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `owner` (nullable object)
  Information about the owner of the payment instrument that may be used or required by particular source types.

  - `owner.address` (nullable object)
    Owner’s address.

    - `owner.address.city` (nullable string)
      City, district, suburb, town, or village.

    - `owner.address.country` (nullable string)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `owner.address.line1` (nullable string)
      Address line 1 (e.g., street, PO Box, or company name).

    - `owner.address.line2` (nullable string)
      Address line 2 (e.g., apartment, suite, unit, or building).

    - `owner.address.postal_code` (nullable string)
      ZIP or postal code.

    - `owner.address.state` (nullable string)
      State, county, province, or region.

  - `owner.email` (nullable string)
    Owner’s email address.

  - `owner.name` (nullable string)
    Owner’s full name.

  - `owner.phone` (nullable string)
    Owner’s phone number (including extension).

  - `owner.verified_address` (nullable object)
    Verified owner’s address. Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated.

    - `owner.verified_address.city` (nullable string)
      City, district, suburb, town, or village.

    - `owner.verified_address.country` (nullable string)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `owner.verified_address.line1` (nullable string)
      Address line 1 (e.g., street, PO Box, or company name).

    - `owner.verified_address.line2` (nullable string)
      Address line 2 (e.g., apartment, suite, unit, or building).

    - `owner.verified_address.postal_code` (nullable string)
      ZIP or postal code.

    - `owner.verified_address.state` (nullable string)
      State, county, province, or region.

  - `owner.verified_email` (nullable string)
    Verified owner’s email address. Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated.

  - `owner.verified_name` (nullable string)
    Verified owner’s full name. Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated.

  - `owner.verified_phone` (nullable string)
    Verified owner’s phone number (including extension). Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated.

- `receiver` (nullable object)
  Information related to the receiver flow. Present if the source is a receiver (`flow` is `receiver`).

  - `receiver.address` (nullable string)
    The address of the receiver source. This is the value that should be communicated to the customer to send their funds to.

  - `receiver.amount_charged` (integer)
    The total amount that was moved to your balance. This is almost always equal to the amount charged. In rare cases when customers deposit excess funds and we are unable to refund those, those funds get moved to your balance and show up in amount_charged as well. The amount charged is expressed in the source’s currency.

  - `receiver.amount_received` (integer)
    The total amount received by the receiver source. `amount_received = amount_returned + amount_charged` should be true for consumed sources unless customers deposit excess funds. The amount received is expressed in the source’s currency.

  - `receiver.amount_returned` (integer)
    The total amount that was returned to the customer. The amount returned is expressed in the source’s currency.

  - `receiver.refund_attributes_method` (string)
    Type of refund attribute method, one of `email`, `manual`, or `none`.

  - `receiver.refund_attributes_status` (string)
    Type of refund attribute status, one of `missing`, `requested`, or `available`.

- `redirect` (nullable object)
  Information related to the redirect flow. Present if the source is authenticated by a redirect (`flow` is `redirect`).

  - `redirect.failure_reason` (nullable string)
    The failure reason for the redirect, either `user_abort` (the customer aborted or dropped out of the redirect flow), `declined` (the authentication failed or the transaction was declined), or `processing_error` (the redirect failed due to a technical error). Present only if the redirect status is `failed`.

  - `redirect.return_url` (string)
    The URL you provide to redirect the customer to after they authenticated their payment.

  - `redirect.status` (string)
    The status of the redirect, either `pending` (ready to be used by your customer to authenticate the transaction), `succeeded` (succesful authentication, cannot be reused) or `not_required` (redirect should not be used) or `failed` (failed authentication, cannot be reused).

  - `redirect.url` (string)
    The URL provided to you to redirect a customer to as part of a `redirect` authentication flow.

- `source_order` (nullable object)
  Information about the items and shipping associated with the source. Required for transactional credit (for example Klarna) sources before you can charge it.

  - `source_order.amount` (integer)
    A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount for the order.

  - `source_order.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `source_order.email` (nullable string)
    The email address of the customer placing the order.

  - `source_order.items` (nullable array of objects)
    List of items constituting the order.

    - `source_order.items.amount` (nullable integer)
      The amount (price) for this order item.

    - `source_order.items.currency` (nullable string)
      This currency of this order item. Required when `amount` is present.

    - `source_order.items.description` (nullable string)
      Human-readable description for this order item.

    - `source_order.items.parent` (nullable string)
      The ID of the associated object for this line item. Expandable if not null (e.g., expandable to a SKU).

    - `source_order.items.quantity` (nullable integer)
      The quantity of this order item. When type is `sku`, this is the number of instances of the SKU to be ordered.

    - `source_order.items.type` (nullable string)
      The type of this order item. Must be `sku`, `tax`, or `shipping`.

  - `source_order.shipping` (nullable object)
    The shipping address for the order. Present if the order is for goods to be shipped.

    - `source_order.shipping.address` (nullable object)
      Shipping address.

      - `source_order.shipping.address.city` (nullable string)
        City, district, suburb, town, or village.

      - `source_order.shipping.address.country` (nullable string)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `source_order.shipping.address.line1` (nullable string)
        Address line 1 (e.g., street, PO Box, or company name).

      - `source_order.shipping.address.line2` (nullable string)
        Address line 2 (e.g., apartment, suite, unit, or building).

      - `source_order.shipping.address.postal_code` (nullable string)
        ZIP or postal code.

      - `source_order.shipping.address.state` (nullable string)
        State, county, province, or region.

    - `source_order.shipping.carrier` (nullable string)
      The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc.

    - `source_order.shipping.name` (nullable string)
      Recipient name.

    - `source_order.shipping.phone` (nullable string)
      Recipient phone (including extension).

    - `source_order.shipping.tracking_number` (nullable string)
      The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.

- `statement_descriptor` (nullable string)
  Extra information about a source. This will appear on your customer’s statement every time you charge the source.

- `status` (string)
  The status of the source, one of `canceled`, `chargeable`, `consumed`, `failed`, or `pending`. Only `chargeable` sources can be used to create a charge.

- `type` (enum)
  The `type` of the source. The `type` is a payment method, one of `ach_credit_transfer`, `ach_debit`, `alipay`, `bancontact`, `card`, `card_present`, `eps`, `giropay`, `ideal`, `multibanco`, `klarna`, `p24`, `sepa_debit`, `sofort`, `three_d_secure`, or `wechat`. An additional hash is included on the source with a name matching this value. It contains additional information specific to the [payment method](https://docs.stripe.com/docs/sources.md) used.

- `usage` (nullable string)
  Either `reusable` or `single_use`. Whether this source should be reusable or not. Some source types may or may not be reusable by construction, while others may leave the option at creation. If an incompatible value is passed, an error will be returned.

### The Source object

```json
{
  "id": "src_1N3lxdLkdIwHu7ixPHXy8UcI",
  "object": "source",
  "ach_credit_transfer": {
    "account_number": "test_eb829353ed79",
    "bank_name": "TEST BANK",
    "fingerprint": "kBQsBk9KtfCgjEYK",
    "refund_account_holder_name": null,
    "refund_account_holder_type": null,
    "refund_routing_number": null,
    "routing_number": "110000000",
    "swift_code": "TSTEZ122"
  },
  "amount": null,
  "client_secret": "src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr",
  "created": 1683144457,
  "currency": "usd",
  "flow": "receiver",
  "livemode": false,
  "metadata": {},
  "owner": {
    "address": null,
    "email": "jenny.rosen@example.com",
    "name": null,
    "phone": null,
    "verified_address": null,
    "verified_email": null,
    "verified_name": null,
    "verified_phone": null
  },
  "receiver": {
    "address": "110000000-test_eb829353ed79",
    "amount_charged": 0,
    "amount_received": 0,
    "amount_returned": 0,
    "refund_attributes_method": "email",
    "refund_attributes_status": "missing"
  },
  "statement_descriptor": null,
  "status": "pending",
  "type": "ach_credit_transfer",
  "usage": "reusable"
}
```