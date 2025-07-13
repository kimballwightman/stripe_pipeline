# Types of events

This is a list of all public snapshot events we currently send for /v1 resources, which is continually evolving and expanding.

Stripe events use the `resource.event` naming convention. Events that occur on subresources like `customer.subscription.updated` don't trigger a corresponding event for the parent resource (`customer.updated`).

Stripe creates event types marked as **Selection required** only when at least one [webhook](https://docs.stripe.com/webhooks.md) is listening for it. A webhook set to listen to all events doesn't satisfy this requirement and won't generate **Selection required** event types.

## Event types

### account.application.authorized
**data.object is an application**  
Occurs whenever a user authorizes an application. Sent to the related application only.

### account.application.deauthorized
**data.object is an application**  
Occurs whenever a user deauthorizes an application. Sent to the related application only.

### account.external_account.created
**data.object is an external account (e.g., card or bank account)**  
Occurs whenever an external account is created.

### account.external_account.deleted
**data.object is an external account (e.g., card or bank account)**  
Occurs whenever an external account is deleted.

### account.external_account.updated
**data.object is an external account (e.g., card or bank account)**  
Occurs whenever an external account is updated.

### account.updated
**data.object is an account**  
Occurs whenever an account status or property has changed.

### application_fee.created
**data.object is an application fee**  
Occurs whenever an application fee is created on a charge.

### application_fee.refund.updated
**data.object is a fee refund**  
Occurs whenever an application fee refund is updated.

### application_fee.refunded
**data.object is an application fee**  
Occurs whenever an application fee is refunded, whether from refunding a charge or from [refunding the application fee directly](#fee_refunds). This includes partial refunds.

### balance.available
**data.object is a balance**  
Occurs whenever your Stripe balance has been updated (e.g., when a charge is available to be paid out). By default, Stripe automatically transfers funds in your balance to your bank account on a daily basis. This event is not fired for negative transactions.

### billing_portal.configuration.created
**data.object is a billing portal configuration**  
Occurs whenever a portal configuration is created.

### billing_portal.configuration.updated
**data.object is a billing portal configuration**  
Occurs whenever a portal configuration is updated.

### billing_portal.session.created
**data.object is a billing portal session**  
Occurs whenever a portal session is created.

### billing.alert.triggered
**data.object is a billing alert triggered**  
Occurs whenever your custom alert threshold is met.

### billing.credit_balance_transaction.created
**data.object is a billing credit balance transaction**  
Occurs when a credit balance transaction is created

### billing.credit_grant.created
**data.object is a billing credit grant**  
Occurs when a credit grant is created

### billing.credit_grant.updated
**data.object is a billing credit grant**  
Occurs when a credit grant is updated

### billing.meter.created
**data.object is a billing meter**  
Occurs when a meter is created

### billing.meter.deactivated
**data.object is a billing meter**  
Occurs when a meter is deactivated

### billing.meter.reactivated
**data.object is a billing meter**  
Occurs when a meter is reactivated

### billing.meter.updated
**data.object is a billing meter**  
Occurs when a meter is updated

### capability.updated
**data.object is a capability**  
Occurs whenever a capability has new requirements or a new status.

### cash_balance.funds_available
**data.object is a cash balance**  
Occurs whenever there is a positive remaining cash balance after Stripe automatically reconciles new funds into the cash balance. If you enabled manual reconciliation, this webhook will fire whenever there are new funds into the cash balance.

### charge.captured
**data.object is a charge**  
Occurs whenever a previously uncaptured charge is captured.

### charge.dispute.closed
**data.object is a dispute**  
Occurs when a dispute is closed and the dispute status changes to `lost`, `warning_closed`, or `won`.

### charge.dispute.created
**data.object is a dispute**  
Occurs whenever a customer disputes a charge with their bank.

### charge.dispute.funds_reinstated
**data.object is a dispute**  
Occurs when funds are reinstated to your account after a dispute is closed. This includes [partially refunded payments](https://docs.stripe.com/disputes#disputes-on-partially-refunded-payments).

### charge.dispute.funds_withdrawn
**data.object is a dispute**  
Occurs when funds are removed from your account due to a dispute.

### charge.dispute.updated
**data.object is a dispute**  
Occurs when the dispute is updated (usually with evidence).

### charge.expired
**data.object is a charge**  
Occurs whenever an uncaptured charge expires.

### charge.failed
**data.object is a charge**  
Occurs whenever a failed charge attempt occurs.

### charge.pending
**data.object is a charge**  
Occurs whenever a pending charge is created.

### charge.refund.updated
**data.object is a refund**  
Occurs whenever a refund is updated on selected payment methods. For updates on all refunds, listen to `refund.updated` instead.

### charge.refunded
**data.object is a charge**  
Occurs whenever a charge is refunded, including partial refunds. Listen to `refund.created` for information about the refund.

### charge.succeeded
**data.object is a charge**  
Occurs whenever a charge is successful.

### charge.updated
**data.object is a charge**  
Occurs whenever a charge description or metadata is updated, or upon an asynchronous capture.

### checkout.session.async_payment_failed
**data.object is a checkout session**  
Occurs when a payment intent using a delayed payment method fails.

### checkout.session.async_payment_succeeded
**data.object is a checkout session**  
Occurs when a payment intent using a delayed payment method finally succeeds.

### checkout.session.completed
**data.object is a checkout session**  
Occurs when a Checkout Session has been successfully completed.

### checkout.session.expired
**data.object is a checkout session**  
Occurs when a Checkout Session is expired.

### climate.order.canceled
**data.object is a climate order**  
Occurs when a Climate order is canceled.

### climate.order.created
**data.object is a climate order**  
Occurs when a Climate order is created.

### climate.order.delayed
**data.object is a climate order**  
Occurs when a Climate order is delayed.

### climate.order.delivered
**data.object is a climate order**  
Occurs when a Climate order is delivered.

### climate.order.product_substituted
**data.object is a climate order**  
Occurs when a Climate order's product is substituted for another.

### climate.product.created
**data.object is a climate product**  
Occurs when a Climate product is created.

### climate.product.pricing_updated
**data.object is a climate product**  
Occurs when a Climate product is updated.

### coupon.created
**data.object is a coupon**  
Occurs whenever a coupon is created.

### coupon.deleted
**data.object is a coupon**  
Occurs whenever a coupon is deleted.

### coupon.updated
**data.object is a coupon**  
Occurs whenever a coupon is updated.

### credit_note.created
**data.object is a credit note**  
Occurs whenever a credit note is created.

### credit_note.updated
**data.object is a credit note**  
Occurs whenever a credit note is updated.

### credit_note.voided
**data.object is a credit note**  
Occurs whenever a credit note is voided.

### customer_cash_balance_transaction.created
**data.object is a customer cash balance transaction**  
Occurs whenever a new customer cash balance transactions is created.

### customer.created
**data.object is a customer**  
Occurs whenever a new customer is created.

### customer.deleted
**data.object is a customer**  
Occurs whenever a customer is deleted.

### customer.discount.created
**data.object is a discount**  
Occurs whenever a coupon is attached to a customer.

### customer.discount.deleted
**data.object is a discount**  
Occurs whenever a coupon is removed from a customer.

### customer.discount.updated
**data.object is a discount**  
Occurs whenever a customer is switched from one coupon to another.

### customer.source.created
**data.object is a source (e.g., card)**  
Occurs whenever a new source is created for a customer.

### customer.source.deleted
**data.object is a source (e.g., card)**  
Occurs whenever a source is removed from a customer.

### customer.source.expiring
**data.object is a source (e.g., card)**  
Occurs whenever a card or source will expire at the end of the month. This event only works with legacy integrations using Card or Source objects. If you use the PaymentMethod API, this event won't occur.

### customer.source.updated
**data.object is a source (e.g., card)**  
Occurs whenever a source's details are changed.

### customer.subscription.created
**data.object is a subscription**  
Occurs whenever a customer is signed up for a new plan.

### customer.subscription.deleted
**data.object is a subscription**  
Occurs whenever a customer's subscription ends.

### customer.subscription.paused
**data.object is a subscription**  
Occurs whenever a customer's subscription is paused. Only applies when subscriptions enter `status=paused`, not when [payment collection](https://docs.stripe.com/billing/subscriptions/pause) is paused.

### customer.subscription.pending_update_applied
**data.object is a subscription**  
Occurs whenever a customer's subscription's pending update is applied, and the subscription is updated.

### customer.subscription.pending_update_expired
**data.object is a subscription**  
Occurs whenever a customer's subscription's pending update expires before the related invoice is paid.

### customer.subscription.resumed
**data.object is a subscription**  
Occurs whenever a customer's subscription is no longer paused. Only applies when a `status=paused` subscription is [resumed](https://docs.stripe.com/api/subscriptions/resume), not when [payment collection](https://docs.stripe.com/billing/subscriptions/pause) is resumed.

### customer.subscription.trial_will_end
**data.object is a subscription**  
Occurs three days before a subscription's trial period is scheduled to end, or when a trial is ended immediately (using `trial_end=now`).

### customer.subscription.updated
**data.object is a subscription**  
Occurs whenever a subscription changes (e.g., switching from one plan to another, or changing the status from trial to active).

### customer.tax_id.created
**data.object is a tax id**  
Occurs whenever a tax ID is created for a customer.

### customer.tax_id.deleted
**data.object is a tax id**  
Occurs whenever a tax ID is deleted from a customer.

### customer.tax_id.updated
**data.object is a tax id**  
Occurs whenever a customer's tax ID is updated.

### customer.updated
**data.object is a customer**  
Occurs whenever any property of a customer changes.

### entitlements.active_entitlement_summary.updated
**data.object is an entitlements active entitlement summary**  
Occurs whenever a customer's entitlements change.

### file.created
**data.object is a file**  
Occurs whenever a new Stripe-generated file is available for your account.

### financial_connections.account.created
**data.object is a financial connections account**  
Occurs when a new Financial Connections account is created.

### financial_connections.account.deactivated
**data.object is a financial connections account**  
Occurs when a Financial Connections account's status is updated from `active` to `inactive`.

### financial_connections.account.disconnected
**data.object is a financial connections account**  
Occurs when a Financial Connections account is disconnected.

### financial_connections.account.reactivated
**data.object is a financial connections account**  
Occurs when a Financial Connections account's status is updated from `inactive` to `active`.

### financial_connections.account.refreshed_balance
**data.object is a financial connections account**  
Occurs when an Account's `balance_refresh` status transitions from `pending` to either `succeeded` or `failed`.

### financial_connections.account.refreshed_ownership
**data.object is a financial connections account**  
Occurs when an Account's `ownership_refresh` status transitions from `pending` to either `succeeded` or `failed`.

### financial_connections.account.refreshed_transactions
**data.object is a financial connections account**  
Occurs when an Account's `transaction_refresh` status transitions from `pending` to either `succeeded` or `failed`.

### identity.verification_session.canceled
**data.object is an identity verification session**  
Occurs whenever a VerificationSession is canceled

### identity.verification_session.created
**data.object is an identity verification session**  
Occurs whenever a VerificationSession is created

### identity.verification_session.processing
**data.object is an identity verification session**  
Occurs whenever a VerificationSession transitions to processing

### identity.verification_session.redacted
**data.object is an identity verification session**  
**Selection required**  
Occurs whenever a VerificationSession is redacted.

### identity.verification_session.requires_input
**data.object is an identity verification session**  
Occurs whenever a VerificationSession transitions to require user input

### identity.verification_session.verified
**data.object is an identity verification session**  
Occurs whenever a VerificationSession transitions to verified

### invoice_payment.paid
**data.object is an invoice payment**  
Occurs when an InvoicePayment is successfully paid.

### invoice.created
**data.object is an invoice**  
Occurs whenever a new invoice is created. To learn how webhooks can be used with this event, and how they can affect it, see [Using Webhooks with Subscriptions](https://docs.stripe.com/subscriptions/webhooks).

### invoice.deleted
**data.object is an invoice**  
Occurs whenever a draft invoice is deleted. Note: This event is not sent for [invoice previews](https://docs.stripe.com/api/invoices/create_preview).

### invoice.finalization_failed
**data.object is an invoice**  
Occurs whenever a draft invoice cannot be finalized. See the invoice's [last finalization error](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error) for details.

### invoice.finalized
**data.object is an invoice**  
Occurs whenever a draft invoice is finalized and updated to be an open invoice.

### invoice.marked_uncollectible
**data.object is an invoice**  
Occurs whenever an invoice is marked uncollectible.

### invoice.overdue
**data.object is an invoice**  
Occurs X number of days after an invoice becomes due—where X is determined by Automations

### invoice.overpaid
**data.object is an invoice**  
Occurs when an invoice transitions to paid with a non-zero amount_overpaid.

### invoice.paid
**data.object is an invoice**  
Occurs whenever an invoice payment attempt succeeds or an invoice is marked as paid out-of-band.

### invoice.payment_action_required
**data.object is an invoice**  
Occurs whenever an invoice payment attempt requires further user action to complete.

### invoice.payment_failed
**data.object is an invoice**  
Occurs whenever an invoice payment attempt fails, due to either a declined payment, including soft decline, or to the lack of a stored payment method.

### invoice.payment_succeeded
**data.object is an invoice**  
Occurs whenever an invoice payment attempt succeeds.

### invoice.sent
**data.object is an invoice**  
Occurs whenever an invoice email is sent out.

### invoice.upcoming
**data.object is an invoice**  
Occurs X number of days before a subscription is scheduled to create an invoice that is automatically charged—where X is determined by your [subscriptions settings](https://dashboard.stripe.com/account/billing/automatic). Note: The received `Invoice` object will not have an invoice ID.

### invoice.updated
**data.object is an invoice**  
Occurs whenever an invoice changes (e.g., the invoice amount).

### invoice.voided
**data.object is an invoice**  
Occurs whenever an invoice is voided.

### invoice.will_be_due
**data.object is an invoice**  
Occurs X number of days before an invoice becomes due—where X is determined by Automations

### invoiceitem.created
**data.object is an invoiceitem**  
Occurs whenever an invoice item is created.

### invoiceitem.deleted
**data.object is an invoiceitem**  
Occurs whenever an invoice item is deleted.

### issuing_authorization.created
**data.object is an issuing authorization**  
Occurs whenever an authorization is created.

### issuing_authorization.request
**data.object is an issuing authorization**  
**Selection required**  
Represents a synchronous request for authorization, see [Using your integration to handle authorization requests](https://docs.stripe.com/issuing/purchases/authorizations#authorization-handling).

### issuing_authorization.updated
**data.object is an issuing authorization**  
Occurs whenever an authorization is updated.

### issuing_card.created
**data.object is an issuing card**  
Occurs whenever a card is created.

### issuing_card.updated
**data.object is an issuing card**  
Occurs whenever a card is updated.

### issuing_cardholder.created
**data.object is an issuing cardholder**  
Occurs whenever a cardholder is created.

### issuing_cardholder.updated
**data.object is an issuing cardholder**  
Occurs whenever a cardholder is updated.

### issuing_dispute.closed
**data.object is an issuing dispute**  
Occurs whenever a dispute is won, lost or expired.

### issuing_dispute.created
**data.object is an issuing dispute**  
Occurs whenever a dispute is created.

### issuing_dispute.funds_reinstated
**data.object is an issuing dispute**  
Occurs whenever funds are reinstated to your account for an Issuing dispute.

### issuing_dispute.funds_rescinded
**data.object is an issuing dispute**  
Occurs whenever funds are deducted from your account for an Issuing dispute.

### issuing_dispute.submitted
**data.object is an issuing dispute**  
Occurs whenever a dispute is submitted.

### issuing_dispute.updated
**data.object is an issuing dispute**  
Occurs whenever a dispute is updated.

### issuing_personalization_design.activated
**data.object is an issuing personalization design**  
Occurs whenever a personalization design is activated following the activation of the physical bundle that belongs to it.

### issuing_personalization_design.deactivated
**data.object is an issuing personalization design**  
Occurs whenever a personalization design is deactivated following the deactivation of the physical bundle that belongs to it.

### issuing_personalization_design.rejected
**data.object is an issuing personalization design**  
Occurs whenever a personalization design is rejected by design review.

### issuing_personalization_design.updated
**data.object is an issuing personalization design**  
Occurs whenever a personalization design is updated.

### issuing_token.created
**data.object is an issuing token**  
Occurs whenever an issuing digital wallet token is created.

### issuing_token.updated
**data.object is an issuing token**  
Occurs whenever an issuing digital wallet token is updated.

### issuing_transaction.created
**data.object is an issuing transaction**  
Occurs whenever an issuing transaction is created.

### issuing_transaction.purchase_details_receipt_updated
**data.object is an issuing transaction**  
Occurs whenever an issuing transaction is updated with receipt data.

### issuing_transaction.updated
**data.object is an issuing transaction**  
Occurs whenever an issuing transaction is updated.

### mandate.updated
**data.object is a mandate**  
Occurs whenever a Mandate is updated.

### payment_intent.amount_capturable_updated
**data.object is a payment intent**  
Occurs when a PaymentIntent has funds to be captured. Check the `amount_capturable` property on the PaymentIntent to determine the amount that can be captured. You may capture the PaymentIntent with an `amount_to_capture` value up to the specified amount. [Learn more about capturing PaymentIntents.](https://docs.stripe.com/api/payment_intents/capture)

### payment_intent.canceled
**data.object is a payment intent**  
Occurs when a PaymentIntent is canceled.

### payment_intent.created
**data.object is a payment intent**  
Occurs when a new PaymentIntent is created.

### payment_intent.partially_funded
**data.object is a payment intent**  
Occurs when funds are applied to a customer_balance PaymentIntent and the 'amount_remaining' changes.

### payment_intent.payment_failed
**data.object is a payment intent**  
Occurs when a PaymentIntent has failed the attempt to create a payment method or a payment.

### payment_intent.processing
**data.object is a payment intent**  
Occurs when a PaymentIntent has started processing.

### payment_intent.requires_action
**data.object is a payment intent**  
Occurs when a PaymentIntent transitions to requires_action state

### payment_intent.succeeded
**data.object is a payment intent**  
Occurs when a PaymentIntent has successfully completed payment.

### payment_link.created
**data.object is a payment link**  
Occurs when a payment link is created.

### payment_link.updated
**data.object is a payment link**  
Occurs when a payment link is updated.

### payment_method.attached
**data.object is a payment method**  
Occurs whenever a new payment method is attached to a customer.

### payment_method.automatically_updated
**data.object is a payment method**  
Occurs whenever a payment method's details are automatically updated by the network.

### payment_method.detached
**data.object is a payment method**  
Occurs whenever a payment method is detached from a customer.

### payment_method.updated
**data.object is a payment method**  
Occurs whenever a payment method is updated via the [PaymentMethod update API](https://docs.stripe.com/api/payment_methods/update).

### payout.canceled
**data.object is a payout**  
Occurs whenever a payout is canceled.

### payout.created
**data.object is a payout**  
Occurs whenever a payout is created.

### payout.failed
**data.object is a payout**  
Occurs whenever a payout attempt fails.

### payout.paid
**data.object is a payout**  
Occurs whenever a payout is *expected* to be available in the destination account. If the payout fails, a `payout.failed` notification is also sent, at a later time.

### payout.reconciliation_completed
**data.object is a payout**  
Occurs whenever balance transactions paid out in an automatic payout can be queried.

### payout.updated
**data.object is a payout**  
Occurs whenever a payout is updated.

### person.created
**data.object is a person**  
Occurs whenever a person associated with an account is created.

### person.deleted
**data.object is a person**  
Occurs whenever a person associated with an account is deleted.

### person.updated
**data.object is a person**  
Occurs whenever a person associated with an account is updated.

### plan.created
**data.object is a plan**  
Occurs whenever a plan is created.

### plan.deleted
**data.object is a plan**  
Occurs whenever a plan is deleted.

### plan.updated
**data.object is a plan**  
Occurs whenever a plan is updated.

### price.created
**data.object is a price**  
Occurs whenever a price is created.

### price.deleted
**data.object is a price**  
Occurs whenever a price is deleted.

### price.updated
**data.object is a price**  
Occurs whenever a price is updated.

### product.created
**data.object is a product**  
Occurs whenever a product is created.

### product.deleted
**data.object is a product**  
Occurs whenever a product is deleted.

### product.updated
**data.object is a product**  
Occurs whenever a product is updated.

### promotion_code.created
**data.object is a promotion code**  
Occurs whenever a promotion code is created.

### promotion_code.updated
**data.object is a promotion code**  
Occurs whenever a promotion code is updated.

### quote.accepted
**data.object is a quote**  
Occurs whenever a quote is accepted.

### quote.canceled
**data.object is a quote**  
Occurs whenever a quote is canceled.

### quote.created
**data.object is a quote**  
Occurs whenever a quote is created.

### quote.finalized
**data.object is a quote**  
Occurs whenever a quote is finalized.

### quote.will_expire
**data.object is a quote**  
Occurs X number of days before a quote is scheduled to expire—where X is determined by Automations

### radar.early_fraud_warning.created
**data.object is a radar early fraud warning**  
Occurs whenever an early fraud warning is created.

### radar.early_fraud_warning.updated
**data.object is a radar early fraud warning**  
Occurs whenever an early fraud warning is updated.

### refund.created
**data.object is a refund**  
Occurs whenever a refund is created.

### refund.failed
**data.object is a refund**  
Occurs whenever a refund has failed.

### refund.updated
**data.object is a refund**  
Occurs whenever a refund is updated.

### reporting.report_run.failed
**data.object is a reporting report run**  
Occurs whenever a requested `ReportRun` failed to complete.

### reporting.report_run.succeeded
**data.object is a reporting report run**  
Occurs whenever a requested `ReportRun` completed successfully.

### reporting.report_type.updated
**data.object is a reporting report type**  
**Selection required**  
Occurs whenever a `ReportType` is updated (typically to indicate that a new day's data has come available).

### review.closed
**data.object is a review**  
Occurs whenever a review is closed. The review's `reason` field indicates why: `approved`, `disputed`, `refunded`, `refunded_as_fraud`, or `canceled`.

### review.opened
**data.object is a review**  
Occurs whenever a review is opened.

### setup_intent.canceled
**data.object is a setup intent**  
Occurs when a SetupIntent is canceled.

### setup_intent.created
**data.object is a setup intent**  
Occurs when a new SetupIntent is created.

### setup_intent.requires_action
**data.object is a setup intent**  
Occurs when a SetupIntent is in requires_action state.

### setup_intent.setup_failed
**data.object is a setup intent**  
Occurs when a SetupIntent has failed the attempt to setup a payment method.

### setup_intent.succeeded
**data.object is a setup intent**  
Occurs when an SetupIntent has successfully setup a payment method.

### sigma.scheduled_query_run.created
**data.object is a scheduled query run**  
Occurs whenever a Sigma scheduled query run finishes.

### source.canceled
**data.object is a source (e.g., card)**  
Occurs whenever a source is canceled.

### source.chargeable
**data.object is a source (e.g., card)**  
Occurs whenever a source transitions to chargeable.

### source.failed
**data.object is a source (e.g., card)**  
Occurs whenever a source fails.

### source.mandate_notification
**data.object is a source (e.g., card)**  
Occurs whenever a source mandate notification method is set to manual.

### source.refund_attributes_required
**data.object is a source (e.g., card)**  
Occurs whenever the refund attributes are required on a receiver source to process a refund or a mispayment.

### source.transaction.created
**data.object is a source transaction**  
Occurs whenever a source transaction is created.

### source.transaction.updated
**data.object is a source transaction**  
Occurs whenever a source transaction is updated.

### subscription_schedule.aborted
**data.object is a subscription schedule**  
Occurs whenever a subscription schedule is canceled due to the underlying subscription being canceled because of delinquency.

### subscription_schedule.canceled
**data.object is a subscription schedule**  
Occurs whenever a subscription schedule is canceled.

### subscription_schedule.completed
**data.object is a subscription schedule**  
Occurs whenever a new subscription schedule is completed.

### subscription_schedule.created
**data.object is a subscription schedule**  
Occurs whenever a new subscription schedule is created.

### subscription_schedule.expiring
**data.object is a subscription schedule**  
Occurs 7 days before a subscription schedule will expire.

### subscription_schedule.released
**data.object is a subscription schedule**  
Occurs whenever a new subscription schedule is released.

### subscription_schedule.updated
**data.object is a subscription schedule**  
Occurs whenever a subscription schedule is updated.

### tax_rate.created
**data.object is a tax rate**  
Occurs whenever a new tax rate is created.

### tax_rate.updated
**data.object is a tax rate**  
Occurs whenever a tax rate is updated.

### tax.settings.updated
**data.object is a tax settings**  
Occurs whenever tax settings is updated.

### terminal.reader.action_failed
**data.object is a terminal reader**  
Occurs whenever an action sent to a Terminal reader failed.

### terminal.reader.action_succeeded
**data.object is a terminal reader**  
Occurs whenever an action sent to a Terminal reader was successful.

### terminal.reader.action_updated
**data.object is a terminal reader**  
Occurs whenever an action sent to a Terminal reader is updated.

### test_helpers.test_clock.advancing
**data.object is a test helpers test clock**  
Occurs whenever a test clock starts advancing.

### test_helpers.test_clock.created
**data.object is a test helpers test clock**  
Occurs whenever a test clock is created.

### test_helpers.test_clock.deleted
**data.object is a test helpers test clock**  
Occurs whenever a test clock is deleted.

### test_helpers.test_clock.internal_failure
**data.object is a test helpers test clock**  
Occurs whenever a test clock fails to advance its frozen time.

### test_helpers.test_clock.ready
**data.object is a test helpers test clock**  
Occurs whenever a test clock transitions to a ready status.

### topup.canceled
**data.object is a topup**  
Occurs whenever a top-up is canceled.

### topup.created
**data.object is a topup**  
Occurs whenever a top-up is created.

### topup.failed
**data.object is a topup**  
Occurs whenever a top-up fails.

### topup.reversed
**data.object is a topup**  
Occurs whenever a top-up is reversed.

### topup.succeeded
**data.object is a topup**  
Occurs whenever a top-up succeeds.

### transfer.created
**data.object is a transfer**  
Occurs whenever a transfer is created.

### transfer.reversed
**data.object is a transfer**  
Occurs whenever a transfer is reversed, including partial reversals.

### transfer.updated
**data.object is a transfer**  
Occurs whenever a transfer's description or metadata is updated.