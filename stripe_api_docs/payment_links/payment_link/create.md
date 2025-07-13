# Create a payment link

Creates a payment link.

Returns the payment link.

- `line_items` (array of objects, required)
  The line items representing what is being sold. Each line item represents an item being sold. Up to 20 line items are supported.

  - `line_items.price` (string, optional)
    The ID of the [Price](https://docs.stripe.com/docs/api/prices.md) or [Plan](https://docs.stripe.com/docs/api/plans.md) object.

  - `line_items.quantity` (integer, required)
    The quantity of the line item being purchased.

  - `line_items.adjustable_quantity` (object, optional)
    When set, provides configuration for this item’s quantity to be adjusted by the customer during checkout.

    - `line_items.adjustable_quantity.enabled` (boolean, required)
      Set to true if the quantity can be adjusted to any non-negative Integer.

    - `line_items.adjustable_quantity.maximum` (integer, optional)
      The maximum quantity the customer can purchase. By default this value is 99. You can specify a value up to 999.

    - `line_items.adjustable_quantity.minimum` (integer, optional)
      The minimum quantity the customer can purchase. By default this value is 0. If there is only one item in the cart then that item’s quantity cannot go down to 0.

- `after_completion` (object, optional)
  Behavior after the purchase is complete.

  - `after_completion.type` (enum, required)
    The specified behavior after the purchase is complete. Either `redirect` or `hosted_confirmation`.

    Displays a message on the hosted surface after the purchase is complete.

    Redirects the customer to the specified `url` after the purchase is complete.

  - `after_completion.hosted_confirmation` (object, optional)
    Configuration when `type=hosted_confirmation`.

    - `after_completion.hosted_confirmation.custom_message` (string, optional)
      A custom message to display to the customer after the purchase is complete.

  - `after_completion.redirect` (object, optional)
    Configuration when `type=redirect`.

    - `after_completion.redirect.url` (string, required)
      The URL the customer will be redirected to after the purchase is complete. You can embed `{CHECKOUT_SESSION_ID}` into the URL to have the `id` of the completed [checkout session](https://docs.stripe.com/docs/api/checkout/sessions/object.md#checkout_session_object-id) included.

- `allow_promotion_codes` (boolean, optional)
  Enables user redeemable promotion codes.

- `application_fee_amount` (integer, optional)
  The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner’s Stripe account. Can only be applied when there are no line items with recurring prices.

- `application_fee_percent` (float, optional)
  A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner’s Stripe account. There must be at least 1 line item with a recurring price to use this field.

- `automatic_tax` (object, optional)
  Configuration for automatic tax collection.

  - `automatic_tax.enabled` (boolean, required)
    Set to `true` to [calculate tax automatically](https://docs.stripe.com/tax) using the customer’s location.

    Enabling this parameter causes the payment link to collect any billing address information necessary for tax calculation.

  - `automatic_tax.liability` (object, optional)
    The account that’s liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.

    - `automatic_tax.liability.type` (enum, required)
      Type of the account referenced in the request.

      Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

      Indicates that the account being referenced is the account making the API request.

    - `automatic_tax.liability.account` (string, optional)
      The connected account being referenced when `type` is `account`.

- `billing_address_collection` (enum, optional)
  Configuration for collecting the customer’s billing address. Defaults to `auto`.

  Checkout will only collect the billing address when necessary. When using [automatic_tax](https://docs.stripe.com/docs/api/checkout/sessions/object.md#checkout_session_object-automatic_tax-enabled), Checkout will collect the minimum number of fields required for tax calculation.

  Checkout will always collect the customer’s billing address.

- `consent_collection` (object, optional)
  Configure fields to gather active consent from customers.

  - `consent_collection.payment_method_reuse_agreement` (object, optional)
    Determines the display of payment method reuse agreement text in the UI. If set to `hidden`, it will hide legal text related to the reuse of a payment method.

    - `consent_collection.payment_method_reuse_agreement.position` (enum, required)
      Determines the position and visibility of the payment method reuse agreement in the UI. When set to `auto`, Stripe’s
      defaults will be used. When set to `hidden`, the payment method reuse agreement text will always be hidden in the UI.

      Uses Stripe defaults to determine the visibility and position of the payment method reuse agreement.

      Hides the payment method reuse agreement.

  - `consent_collection.promotions` (enum, optional)
    If set to `auto`, enables the collection of customer consent for promotional communications. The Checkout
    Session will determine whether to display an option to opt into promotional communication
    from the merchant depending on the customer’s locale. Only available to US merchants.

    Enable the collection of customer consent for promotional communications.
    The Checkout Session will determine whether to display an option to opt into promotional
    communication from the merchant depending on if a customer is provided, and if that customer
    has consented to receiving promotional communications from the merchant in the past.

    Checkout will not collect customer consent for promotional communications.

  - `consent_collection.terms_of_service` (enum, optional)
    If set to `required`, it requires customers to check a terms of service checkbox before being able to pay.
    There must be a valid terms of service URL set in your [Dashboard settings](https://dashboard.stripe.com/settings/public).

    Does not display checkbox for the terms of service agreement.

    Displays a checkbox for the terms of service agreement which requires customer to check before being able to pay.

- `currency` (enum, optional)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies) and supported by each line item’s price.

- `custom_fields` (array of objects, optional)
  Collect additional information from your customer using custom fields. Up to 3 fields are supported.

  - `custom_fields.key` (string, required)
    String of your choice that your integration can use to reconcile this field. Must be unique to this field, alphanumeric, and up to 200 characters.

  - `custom_fields.label` (object, required)
    The label for the field, displayed to the customer.

    - `custom_fields.label.custom` (string, required)
      Custom text for the label, displayed to the customer. Up to 50 characters.

    - `custom_fields.label.type` (enum, required)
      The type of the label.

      Set a custom label for the field.

  - `custom_fields.type` (enum, required)
    The type of the field.

    Provide a list of options for your customer to select.

    Collect a numbers-only field from your customer.

    Collect a string field from your customer.

  - `custom_fields.dropdown` (object, optional)
    Configuration for `type=dropdown` fields.

    - `custom_fields.dropdown.options` (array of objects, required)
      The options available for the customer to select. Up to 200 options allowed.

      - `custom_fields.dropdown.options.label` (string, required)
        The label for the option, displayed to the customer. Up to 100 characters.

      - `custom_fields.dropdown.options.value` (string, required)
        The value for this option, not displayed to the customer, used by your integration to reconcile the option selected by the customer. Must be unique to this option, alphanumeric, and up to 100 characters.

    - `custom_fields.dropdown.default_value` (string, optional)
      The value that will pre-fill the field on the payment page.Must match a `value` in the `options` array.

  - `custom_fields.numeric` (object, optional)
    Configuration for `type=numeric` fields.

    - `custom_fields.numeric.default_value` (string, optional)
      The value that will pre-fill the field on the payment page.

    - `custom_fields.numeric.maximum_length` (integer, optional)
      The maximum character length constraint for the customer’s input.

    - `custom_fields.numeric.minimum_length` (integer, optional)
      The minimum character length requirement for the customer’s input.

  - `custom_fields.optional` (boolean, optional)
    Whether the customer is required to complete the field before completing the Checkout Session. Defaults to `false`.

  - `custom_fields.text` (object, optional)
    Configuration for `type=text` fields.

    - `custom_fields.text.default_value` (string, optional)
      The value that will pre-fill the field on the payment page.

    - `custom_fields.text.maximum_length` (integer, optional)
      The maximum character length constraint for the customer’s input.

    - `custom_fields.text.minimum_length` (integer, optional)
      The minimum character length requirement for the customer’s input.

- `custom_text` (object, optional)
  Display additional text for your customers using custom text.

  - `custom_text.after_submit` (object, optional)
    Custom text that should be displayed after the payment confirmation button.

    - `custom_text.after_submit.message` (string, required)
      Text may be up to 1200 characters in length.

  - `custom_text.shipping_address` (object, optional)
    Custom text that should be displayed alongside shipping address collection.

    - `custom_text.shipping_address.message` (string, required)
      Text may be up to 1200 characters in length.

  - `custom_text.submit` (object, optional)
    Custom text that should be displayed alongside the payment confirmation button.

    - `custom_text.submit.message` (string, required)
      Text may be up to 1200 characters in length.

  - `custom_text.terms_of_service_acceptance` (object, optional)
    Custom text that should be displayed in place of the default terms of service agreement text.

    - `custom_text.terms_of_service_acceptance.message` (string, required)
      Text may be up to 1200 characters in length.

- `customer_creation` (enum, optional)
  Configures whether [checkout sessions](https://docs.stripe.com/docs/api/checkout/sessions.md) created by this payment link create a [Customer](https://docs.stripe.com/docs/api/customers.md).

  The Checkout Session will always create a [Customer](https://docs.stripe.com/docs/api/customers.md) when a Session confirmation is attempted.

  The Checkout Session will only create a [Customer](https://docs.stripe.com/docs/api/customers.md) if it is required for Session confirmation.
  Currently, only `subscription` mode Sessions and `payment` mode Sessions with [post-purchase invoices enabled](https://docs.stripe.com/docs/receipts.md?payment-ui=checkout#paid-invoices) require a Customer.

- `inactive_message` (string, optional)
  The custom message to be displayed to a customer when a payment link is no longer active.

- `invoice_creation` (object, optional)
  Generate a post-purchase Invoice for one-time payments.

  - `invoice_creation.enabled` (boolean, required)
    Whether the feature is enabled

  - `invoice_creation.invoice_data` (object, optional)
    Invoice PDF configuration.

    - `invoice_creation.invoice_data.account_tax_ids` (array of strings, optional)
      The account tax IDs associated with the invoice.

    - `invoice_creation.invoice_data.custom_fields` (array of objects, optional)
      Default custom fields to be displayed on invoices for this customer.

      - `invoice_creation.invoice_data.custom_fields.name` (string, required)
        The name of the custom field. This may be up to 40 characters.

      - `invoice_creation.invoice_data.custom_fields.value` (string, required)
        The value of the custom field. This may be up to 140 characters.

    - `invoice_creation.invoice_data.description` (string, optional)
      An arbitrary string attached to the object. Often useful for displaying to users.

    - `invoice_creation.invoice_data.footer` (string, optional)
      Default footer to be displayed on invoices for this customer.

    - `invoice_creation.invoice_data.issuer` (object, optional)
      The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.

      - `invoice_creation.invoice_data.issuer.type` (enum, required)
        Type of the account referenced in the request.

        Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

        Indicates that the account being referenced is the account making the API request.

      - `invoice_creation.invoice_data.issuer.account` (string, optional)
        The connected account being referenced when `type` is `account`.

    - `invoice_creation.invoice_data.metadata` (object, optional)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

    - `invoice_creation.invoice_data.rendering_options` (object, optional)
      Default options for invoice PDF rendering for this customer.

      - `invoice_creation.invoice_data.rendering_options.amount_tax_display` (enum, optional)
        How line-item prices and amounts will be displayed with respect to tax on invoice PDFs. One of `exclude_tax` or `include_inclusive_tax`. `include_inclusive_tax` will include inclusive tax (and exclude exclusive tax) in invoice PDF amounts. `exclude_tax` will exclude all tax (inclusive and exclusive alike) from invoice PDF amounts.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. Metadata associated with this Payment Link will automatically be copied to [checkout sessions](https://docs.stripe.com/docs/api/checkout/sessions.md) created by this payment link.

- `on_behalf_of` (string, optional)
  The account on behalf of which to charge.

- `optional_items` (array of objects, optional)
  A list of optional items the customer can add to their order at checkout. Use this parameter to pass one-time or recurring [Prices](https://docs.stripe.com/docs/api/prices.md).
  There is a maximum of 10 optional items allowed on a payment link, and the existing limits on the number of line items allowed on a payment link apply to the combined number of line items and optional items.
  There is a maximum of 20 combined line items and optional items.

  - `optional_items.price` (string, required)
    The ID of the [Price](https://docs.stripe.com/docs/api/prices.md) or [Plan](https://docs.stripe.com/docs/api/plans.md) object.

  - `optional_items.quantity` (integer, required)
    The initial quantity of the line item created when a customer chooses to add this optional item to their order.

  - `optional_items.adjustable_quantity` (object, optional)
    When set, provides configuration for the customer to adjust the quantity of the line item created when a customer chooses to add this optional item to their order.

    - `optional_items.adjustable_quantity.enabled` (boolean, required)
      Set to true if the quantity can be adjusted to any non-negative integer.

    - `optional_items.adjustable_quantity.maximum` (integer, optional)
      The maximum quantity of this item the customer can purchase. By default this value is 99.

    - `optional_items.adjustable_quantity.minimum` (integer, optional)
      The minimum quantity of this item the customer must purchase, if they choose to purchase it. Because this item is optional, the customer will always be able to remove it from their order, even if the `minimum` configured here is greater than 0. By default this value is 0.

- `payment_intent_data` (object, optional)
  A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode.

  - `payment_intent_data.capture_method` (enum, optional)
    Controls when the funds will be captured from the customer’s account.

    Stripe automatically captures funds when the customer authorizes the payment.

    (Default) Stripe asynchronously captures funds when the customer authorizes the payment. Recommended over `capture_method=automatic` due to improved latency. Read the [integration guide](https://docs.stripe.com/docs/payments/payment-intents/asynchronous-capture.md) for more information.

    Place a hold on the funds when the customer authorizes the payment, but [don’t capture the funds until later](https://docs.stripe.com/docs/payments/capture-later.md). (Not all payment methods support this.)

  - `payment_intent_data.description` (string, optional)
    An arbitrary string attached to the object. Often useful for displaying to users.

  - `payment_intent_data.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that will declaratively set metadata on [Payment Intents](https://docs.stripe.com/docs/api/payment_intents.md) generated from this payment link. Unlike object-level metadata, this field is declarative. Updates will clear prior values.

  - `payment_intent_data.setup_future_usage` (enum, optional)
    Indicates that you intend to [make future payments](https://docs.stripe.com/docs/payments/payment-intents.md#future-usage) with the payment method collected by this Checkout Session.

    When setting this to `on_session`, Checkout will show a notice to the customer that their payment details will be saved.

    When setting this to `off_session`, Checkout will show a notice to the customer that their payment details will be saved and used for future payments.

    If a Customer has been provided or Checkout creates a new Customer,Checkout will attach the payment method to the Customer.

    If Checkout does not create a Customer, the payment method is not attached to a Customer. To reuse the payment method, you can retrieve it from the Checkout Session’s PaymentIntent.

    When processing card payments, Checkout also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as SCA.

    Use `off_session` if your customer may or may not be present in your checkout flow.

    Use `on_session` if you intend to only reuse the payment method when your customer is present in your checkout flow.

  - `payment_intent_data.statement_descriptor` (string, optional)
    Text that appears on the customer’s statement as the statement descriptor for a non-card charge. This value overrides the account’s default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).

    Setting this value for a card charge returns an error. For card charges, set the [statement_descriptor_suffix](https://docs.stripe.com/get-started/account/statement-descriptors#dynamic) instead.

  - `payment_intent_data.statement_descriptor_suffix` (string, optional)
    Provides information about a card charge. Concatenated to the account’s [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer’s statement.

  - `payment_intent_data.transfer_group` (string, optional)
    A string that identifies the resulting payment as part of a group. See the PaymentIntents [use case for connected accounts](https://docs.stripe.com/docs/connect/separate-charges-and-transfers.md) for details.

- `payment_method_collection` (enum, optional)
  Specify whether Checkout should collect a payment method. When set to `if_required`, Checkout will not collect a payment method when the total due for the session is 0.This may occur if the Checkout Session includes a free trial or a discount.

  Can only be set in `subscription` mode. Defaults to `always`.

  If you’d like information on how to collect a payment method outside of Checkout, read the guide on [configuring subscriptions with a free trial](https://docs.stripe.com/docs/payments/checkout/free-trials.md).

  The Checkout Session will always collect a PaymentMethod.

  The Checkout Session will only collect a PaymentMethod if there is an amount due.

- `payment_method_types` (array of enums, optional)
  The list of payment method types that customers can use. If no value is passed, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods) (20+ payment methods [supported](https://docs.stripe.com/docs/payments/payment-methods/integration-options.md#payment-method-product-support)).

- `phone_number_collection` (object, optional)
  Controls phone number collection settings during checkout.

  We recommend that you review your privacy policy and check with your legal contacts.

  - `phone_number_collection.enabled` (boolean, required)
    Set to `true` to enable phone number collection.

- `restrictions` (object, optional)
  Settings that restrict the usage of a payment link.

  - `restrictions.completed_sessions` (object, required)
    Configuration for the `completed_sessions` restriction type.

    - `restrictions.completed_sessions.limit` (integer, required)
      The maximum number of checkout sessions that can be completed for the `completed_sessions` restriction to be met.

- `shipping_address_collection` (object, optional)
  Configuration for collecting the customer’s shipping address.

  - `shipping_address_collection.allowed_countries` (array of enums, required)
    An array of two-letter ISO country codes representing which countries Checkout should provide as options for
    shipping locations.

- `shipping_options` (array of objects, optional)
  The shipping rate options to apply to [checkout sessions](https://docs.stripe.com/docs/api/checkout/sessions.md) created by this payment link.

  - `shipping_options.shipping_rate` (string, optional)
    The ID of the Shipping Rate to use for this shipping option.

- `submit_type` (enum, optional)
  Describes the type of transaction being performed in order to customize relevant text on the page, such as the submit button. Changing this value will also affect the hostname in the [url](https://docs.stripe.com/docs/api/payment_links/payment_links/object.md#url) property (example: `donate.stripe.com`).

  Default value. `pay` will used in all scenarios

  Recommended when offering bookings. Submit button includes a ‘Book’ label and URLs use the `book.stripe.com` hostname

  Recommended when accepting donations. Submit button includes a ‘Donate’ label and URLs use the `donate.stripe.com` hostname

  Submit button includes a ‘Buy’ label and URLs use the `buy.stripe.com` hostname

  Submit button includes a ‘Subscribe’ label and URLs use the `buy.stripe.com` hostname

- `subscription_data` (object, optional)
  When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`.

  - `subscription_data.description` (string, optional)
    The subscription’s description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.

  - `subscription_data.invoice_settings` (object, optional)
    All invoices will be billed using the specified settings.

    - `subscription_data.invoice_settings.issuer` (object, optional)
      The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.

      - `subscription_data.invoice_settings.issuer.type` (enum, required)
        Type of the account referenced in the request.

        Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

        Indicates that the account being referenced is the account making the API request.

      - `subscription_data.invoice_settings.issuer.account` (string, optional)
        The connected account being referenced when `type` is `account`.

  - `subscription_data.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that will declaratively set metadata on [Subscriptions](https://docs.stripe.com/docs/api/subscriptions.md) generated from this payment link. Unlike object-level metadata, this field is declarative. Updates will clear prior values.

  - `subscription_data.trial_period_days` (integer, optional)
    Integer representing the number of trial period days before the customer is charged for the first time. Has to be at least 1.

  - `subscription_data.trial_settings` (object, optional)
    Settings related to subscription trials.

    - `subscription_data.trial_settings.end_behavior` (object, required)
      Defines how the subscription should behave when the user’s free trial ends.

      - `subscription_data.trial_settings.end_behavior.missing_payment_method` (enum, required)
        Indicates how the subscription should change when the trial ends if the user did not provide a payment method.

        Cancel the subscription if a payment method is not attached when the trial ends.

        Create an invoice when the trial ends, even if the user did not set up a payment method.

        Pause the subscription if a payment method is not attached when the trial ends.

- `tax_id_collection` (object, optional)
  Controls tax ID collection during checkout.

  - `tax_id_collection.enabled` (boolean, required)
    Enable tax ID collection during checkout. Defaults to `false`.

  - `tax_id_collection.required` (enum, optional)
    Describes whether a tax ID is required during checkout. Defaults to `never`.

    A tax ID will be required if collection is [supported](https://docs.stripe.com/tax/checkout/tax-ids#supported-types) for the selected billing address country.

    Tax ID collection is never required.

- `transfer_data` (object, optional)
  The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to.

  - `transfer_data.destination` (string, required)
    If specified, successful charges will be attributed to the destination
    account for tax reporting, and the funds from charges will be transferred
    to the destination account. The ID of the resulting transfer will be
    returned on the successful charge’s `transfer` field.

  - `transfer_data.amount` (integer, optional)
    The amount that will be transferred automatically when a charge succeeds.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new PaymentLinkCreateOptions
{
    LineItems = new List<PaymentLinkLineItemOptions>
    {
        new PaymentLinkLineItemOptions { Price = "price_1MoC3TLkdIwHu7ixcIbKelAC", Quantity = 1 },
    },
};
var service = new PaymentLinkService();
PaymentLink paymentLink = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentLinkParams{
  LineItems: []*stripe.PaymentLinkLineItemParams{
    &stripe.PaymentLinkLineItemParams{
      Price: stripe.String("price_1MoC3TLkdIwHu7ixcIbKelAC"),
      Quantity: stripe.Int64(1),
    },
  },
};
result, err := paymentlink.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

PaymentLinkCreateParams params =
  PaymentLinkCreateParams.builder()
    .addLineItem(
      PaymentLinkCreateParams.LineItem.builder()
        .setPrice("price_1MoC3TLkdIwHu7ixcIbKelAC")
        .setQuantity(1L)
        .build()
    )
    .build();

PaymentLink paymentLink = PaymentLink.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const paymentLink = await stripe.paymentLinks.create({
  line_items: [
    {
      price: 'price_1MoC3TLkdIwHu7ixcIbKelAC',
      quantity: 1,
    },
  ],
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_link = stripe.PaymentLink.create(
  line_items=[{"price": "price_1MoC3TLkdIwHu7ixcIbKelAC", "quantity": 1}],
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentLink = $stripe->paymentLinks->create([
  'line_items' => [
    [
      'price' => 'price_1MoC3TLkdIwHu7ixcIbKelAC',
      'quantity' => 1,
    ],
  ],
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_link = Stripe::PaymentLink.create({
  line_items: [
    {
      price: 'price_1MoC3TLkdIwHu7ixcIbKelAC',
      quantity: 1,
    },
  ],
})
```

### Response

```json
{
  "id": "plink_1MoC3ULkdIwHu7ixZjtGpVl2",
  "object": "payment_link",
  "active": true,
  "after_completion": {
    "hosted_confirmation": {
      "custom_message": null
    },
    "type": "hosted_confirmation"
  },
  "allow_promotion_codes": false,
  "application_fee_amount": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null
  },
  "billing_address_collection": "auto",
  "consent_collection": null,
  "currency": "usd",
  "custom_fields": [],
  "custom_text": {
    "shipping_address": null,
    "submit": null
  },
  "customer_creation": "if_required",
  "invoice_creation": {
    "enabled": false,
    "invoice_data": {
      "account_tax_ids": null,
      "custom_fields": null,
      "description": null,
      "footer": null,
      "issuer": null,
      "metadata": {},
      "rendering_options": null
    }
  },
  "livemode": false,
  "metadata": {},
  "on_behalf_of": null,
  "payment_intent_data": null,
  "payment_method_collection": "always",
  "payment_method_types": null,
  "phone_number_collection": {
    "enabled": false
  },
  "shipping_address_collection": null,
  "shipping_options": [],
  "submit_type": "auto",
  "subscription_data": {
    "description": null,
    "invoice_settings": {
      "issuer": {
        "type": "self"
      }
    },
    "trial_period_days": null
  },
  "tax_id_collection": {
    "enabled": false
  },
  "transfer_data": null,
  "url": "https://buy.stripe.com/test_cN25nr0iZ7bUa7meUY"
}
```