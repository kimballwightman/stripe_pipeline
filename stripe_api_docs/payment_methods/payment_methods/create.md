# Create a PaymentMethod

Creates a PaymentMethod object. Read the [Stripe.js reference](https://docs.stripe.com/docs/stripe-js/reference.md#stripe-create-payment-method) to learn how to create PaymentMethods via Stripe.js.

Instead of creating a PaymentMethod directly, we recommend using the [PaymentIntents](https://docs.stripe.com/docs/payments/accept-a-payment.md) API to accept a payment immediately or the [SetupIntent](https://docs.stripe.com/docs/payments/save-and-reuse.md) API to collect payment method details ahead of a future payment.

Returns a PaymentMethod object.

- `type` (enum, optional)
  The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.

  [Pre-authorized debit payments](https://docs.stripe.com/docs/payments/acss-debit.md) are used to debit Canadian bank accounts through the Automated Clearing Settlement System (ACSS).

  [Affirm](https://docs.stripe.com/docs/payments/affirm.md) is a buy now, pay later payment method in the US.

  [Afterpay / Clearpay](https://docs.stripe.com/docs/payments/afterpay-clearpay.md) is a buy now, pay later payment method used in Australia, Canada, France, New Zealand, Spain, the UK, and the US.

  [Alipay](https://docs.stripe.com/docs/payments/alipay.md) is a digital wallet payment method used in China.

  [Alma](https://docs.stripe.com/docs/payments/alma.md) is a Buy Now, Pay Later payment method that lets customers pay in 2, 3, or 4 installments.

  [Amazon Pay](https://docs.stripe.com/docs/payments/amazon-pay.md) is a Wallet payment method that lets hundreds of millions of Amazon customers pay their way, every day.

  [BECS Direct Debit](https://docs.stripe.com/docs/payments/au-becs-debit.md) is used to debit Australian bank accounts through the Bulk Electronic Clearing System (BECS).

  [Bacs Direct Debit](https://docs.stripe.com/docs/payments/payment-methods/bacs-debit.md) is used to debit UK bank accounts.

  [Bancontact](https://docs.stripe.com/docs/payments/bancontact.md) is a bank redirect payment method used in Belgium.

  [Billie](https://docs.stripe.com/docs/payments/billie.md) is a payment method.

  [BLIK](https://docs.stripe.com/docs/payments/blik.md) is a single-use payment method common in Poland.

  [Boleto](https://docs.stripe.com/docs/payments/boleto.md) is a voucher-based payment method used in Brazil.

  [Card payments](https://docs.stripe.com/docs/payments/payment-methods/overview.md#cards) are supported through many networks, card brands, and select Link funding sources.

  [Stripe Terminal](https://docs.stripe.com/docs/terminal/payments/collect-card-payment.md) is used to collect in-person card payments.

  [Cash App Pay](https://docs.stripe.com/docs/payments/cash-app-pay.md) enables customers to frictionlessly authenticate payments in the Cash App using their stored balance or linked card.

  Crypto is a payment method.

  Uses a customer’s [cash balance](https://docs.stripe.com/docs/payments/customer-balance.md) for the payment.

  [EPS](https://docs.stripe.com/docs/payments/eps.md) is an Austria-based bank redirect payment method.

  [FPX](https://docs.stripe.com/docs/payments/fpx.md) is a Malaysia-based bank redirect payment method.

  [giropay](https://docs.stripe.com/docs/payments/giropay.md) is a German bank redirect payment method.

  [GrabPay](https://docs.stripe.com/docs/payments/grabpay.md) is a digital wallet payment method used in Southeast Asia.

  [iDEAL](https://docs.stripe.com/docs/payments/ideal.md) is a Netherlands-based bank redirect payment method.

  [Kakao Pay](https://docs.stripe.com/docs/payments/kakao-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  [Klarna](https://docs.stripe.com/docs/payments/klarna.md) is a global buy now, pay later payment method.

  [Konbini](https://docs.stripe.com/docs/payments/konbini.md) is a cash-based voucher payment method used in Japan.

  [Korean cards](https://docs.stripe.com/docs/payments/kr-card/accept-a-payment.md) enables customers to accept local credit and debit cards in South Korea.

  [Link](https://docs.stripe.com/docs/payments/link.md) allows customers to pay with their saved payment details.

  [MobilePay](https://docs.stripe.com/docs/payments/mobilepay.md) is a Nordic card-passthrough wallet payment method where customers authorize the payment in the MobilePay application.

  [Multibanco](https://docs.stripe.com/docs/payments/multibanco.md) is a voucher payment method

  [Naver Pay](https://docs.stripe.com/docs/payments/naver-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  [New Zealand BECS Direct Debit](https://docs.stripe.com/docs/payments/nz-bank-account.md) is used to debit New Zealand bank accounts through the Bulk Electronic Clearing System (BECS).

  [OXXO](https://docs.stripe.com/docs/payments/oxxo.md) is a cash-based voucher payment method used in Mexico.

  [Przelewy24](https://docs.stripe.com/docs/payments/p24.md) is a bank redirect payment method used in Poland.

  [Pay By Bank](https://docs.stripe.com/docs/payments/pay-by-bank.md) is an open banking payment method in the UK.

  [PAYCO](https://docs.stripe.com/docs/payments/payco/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  [PayNow](https://docs.stripe.com/docs/payments/paynow.md) is a QR code payment method used in Singapore.

  [PayPal](https://docs.stripe.com/docs/payments/paypal.md) is an online wallet and redirect payment method commonly used in Europe.

  [Pix](https://docs.stripe.com/docs/payments/pix.md) is an instant bank transfer payment method in Brazil.

  [PromptPay](https://docs.stripe.com/docs/payments/promptpay.md) is an instant funds transfer service popular in Thailand.

  [Revolut Pay](https://docs.stripe.com/docs/payments/revolut-pay.md) is a digital wallet payment method used in the United Kingdom.

  [Samsung Pay](https://docs.stripe.com/docs/payments/samsung-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  [Satispay](https://docs.stripe.com/docs/payments/satispay.md) is a payment method.

  [SEPA Direct Debit](https://docs.stripe.com/docs/payments/sepa-debit.md) is used to debit bank accounts within the Single Euro Payments Area (SEPA) region.

  [Sofort](https://docs.stripe.com/docs/payments/sofort.md) is a bank redirect payment method used in Europe.

  [Swish](https://docs.stripe.com/docs/payments/swish.md) is a Swedish wallet payment method where customers authorize the payment in the Swish application.

  [TWINT](https://docs.stripe.com/docs/payments/twint.md) is a single-use payment method used in Switzerland.

  [ACH Direct Debit](https://docs.stripe.com/docs/payments/ach-direct-debit.md) is used to debit US bank accounts through the Automated Clearing House (ACH) payments system.

  [WeChat Pay](https://docs.stripe.com/docs/payments/wechat-pay.md) is a digital wallet payment method based in China.

  [Zip](https://docs.stripe.com/docs/payments/zip.md) is a Buy now, pay later Payment Method

- `acss_debit` (object, optional)
  If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method.

  - `acss_debit.account_number` (string, optional)
    Customer’s bank account number.

  - `acss_debit.institution_number` (string, optional)
    Institution number of the customer’s bank.

  - `acss_debit.transit_number` (string, optional)
    Transit number of the customer’s bank.

- `affirm` (object, optional)
  If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method.

- `afterpay_clearpay` (object, optional)
  If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method.

- `alipay` (object, optional)
  If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method.

- `allow_redisplay` (enum, optional)
  This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to `unspecified`.

  Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

  Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

  This is the default value for payment methods where `allow_redisplay` wasn’t set.

- `alma` (object, optional)
  If this is a Alma PaymentMethod, this hash contains details about the Alma payment method.

- `amazon_pay` (object, optional)
  If this is a AmazonPay PaymentMethod, this hash contains details about the AmazonPay payment method.

- `au_becs_debit` (object, optional)
  If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account.

  - `au_becs_debit.account_number` (string, required)
    The account number for the bank account.

  - `au_becs_debit.bsb_number` (string, required)
    Bank-State-Branch number of the bank account.

- `bacs_debit` (object, optional)
  If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account.

  - `bacs_debit.account_number` (string, optional)
    Account number of the bank account that the funds will be debited from.

  - `bacs_debit.sort_code` (string, optional)
    Sort code of the bank account. (e.g., `10-20-30`)

- `bancontact` (object, optional)
  If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method.

- `billie` (object, optional)
  If this is a `billie` PaymentMethod, this hash contains details about the Billie payment method.

- `billing_details` (object, optional)
  Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.

  - `billing_details.address` (object, optional)
    Billing address.

    - `billing_details.address.city` (string, optional)
      City, district, suburb, town, or village.

    - `billing_details.address.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `billing_details.address.line1` (string, optional)
      Address line 1 (e.g., street, PO Box, or company name).

    - `billing_details.address.line2` (string, optional)
      Address line 2 (e.g., apartment, suite, unit, or building).

    - `billing_details.address.postal_code` (string, optional)
      ZIP or postal code.

    - `billing_details.address.state` (string, optional)
      State, county, province, or region.

  - `billing_details.email` (string, optional)
    Email address.

  - `billing_details.name` (string, optional)
    Full name.

  - `billing_details.phone` (string, optional)
    Billing phone number (including extension).

  - `billing_details.tax_id` (string, optional)
    Taxpayer identification number. Used only for transactions between LATAM buyers and non-LATAM sellers.

- `blik` (object, optional)
  If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method.

- `boleto` (object, optional)
  If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method.

  - `boleto.tax_id` (string, required)
    The tax ID of the customer (CPF for individual consumers or CNPJ for businesses consumers)

- `card` (object, optional)
  If this is a `card` PaymentMethod, this hash contains the user’s card details. For backwards compatibility, you can alternatively provide a Stripe token (e.g., for Apple Pay, Amex Express Checkout, or legacy Checkout) into the card hash with format `card: {token: "tok_visa"}`. When providing a card number, you must meet the requirements for [PCI compliance](https://stripe.com/docs/security#validating-pci-compliance). We strongly recommend using Stripe.js instead of interacting with this API directly.

  - `card.exp_month` (integer, required)
    Two-digit number representing the card’s expiration month.

  - `card.exp_year` (integer, required)
    Four-digit number representing the card’s expiration year.

  - `card.number` (string, optional)
    The card number, as a string without any separators.

  - `card.cvc` (string, optional)
    The card’s CVC. It is highly recommended to always include this value.

  - `card.networks` (object, optional)
    Contains information about card networks used to process the payment.

    - `card.networks.preferred` (enum, optional)
      The customer’s preferred card network for co-branded cards. Supports `cartes_bancaires`, `mastercard`, or `visa`. Selection of a network that does not apply to the card will be stored as `invalid_preference` on the card.

- `cashapp` (object, optional)
  If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method.

- `crypto` (object, optional)
  If this is a Crypto PaymentMethod, this hash contains details about the Crypto payment method.

- `customer_balance` (object, optional)
  If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method.

- `eps` (object, optional)
  If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method.

  - `eps.bank` (string, optional)
    The customer’s bank.

- `fpx` (object, optional)
  If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method.

  - `fpx.bank` (string, required)
    The customer’s bank.

- `giropay` (object, optional)
  If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method.

- `grabpay` (object, optional)
  If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method.

- `ideal` (object, optional)
  If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method.

  - `ideal.bank` (string, optional)
    The customer’s bank. Only use this parameter for existing customers. Don’t use it for new customers.

- `kakao_pay` (object, optional)
  If this is a `kakao_pay` PaymentMethod, this hash contains details about the Kakao Pay payment method.

- `klarna` (object, optional)
  If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method.

  - `klarna.dob` (object, optional)
    Customer’s date of birth

    - `klarna.dob.day` (integer, required)
      The day of birth, between 1 and 31.

    - `klarna.dob.month` (integer, required)
      The month of birth, between 1 and 12.

    - `klarna.dob.year` (integer, required)
      The four-digit year of birth.

- `konbini` (object, optional)
  If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method.

- `kr_card` (object, optional)
  If this is a `kr_card` PaymentMethod, this hash contains details about the Korean Card payment method.

- `link` (object, optional)
  If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `mobilepay` (object, optional)
  If this is a `mobilepay` PaymentMethod, this hash contains details about the MobilePay payment method.

- `multibanco` (object, optional)
  If this is a `multibanco` PaymentMethod, this hash contains details about the Multibanco payment method.

- `naver_pay` (object, optional)
  If this is a `naver_pay` PaymentMethod, this hash contains details about the Naver Pay payment method.

  - `naver_pay.funding` (enum, optional)
    Whether to use Naver Pay points or a card to fund this transaction. If not provided, this defaults to `card`.

    Use a card to fund this transaction.

    Use Naver Pay points to fund this transaction.

- `nz_bank_account` (object, optional)
  If this is an nz_bank_account PaymentMethod, this hash contains details about the nz_bank_account payment method.

  - `nz_bank_account.account_number` (string, required)
    The account number for the bank account.

  - `nz_bank_account.bank_code` (string, required)
    The numeric code for the bank account’s bank.

  - `nz_bank_account.branch_code` (string, required)
    The numeric code for the bank account’s bank branch.

  - `nz_bank_account.suffix` (string, required)
    The suffix of the bank account number.

  - `nz_bank_account.account_holder_name` (string, optional)
    The name on the bank account. Only required if the account holder name is different from the name of the authorized signatory collected in the PaymentMethod’s billing details.

- `oxxo` (object, optional)
  If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method.

- `p24` (object, optional)
  If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method.

  - `p24.bank` (enum, optional)
    The customer’s bank.

- `pay_by_bank` (object, optional)
  If this is a `pay_by_bank` PaymentMethod, this hash contains details about the PayByBank payment method.

- `payco` (object, optional)
  If this is a `payco` PaymentMethod, this hash contains details about the PAYCO payment method.

- `paynow` (object, optional)
  If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method.

- `paypal` (object, optional)
  If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method.

- `pix` (object, optional)
  If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method.

- `promptpay` (object, optional)
  If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method.

- `radar_options` (object, optional)
  Options to configure Radar. See [Radar Session](https://docs.stripe.com/docs/radar/radar-session.md) for more information.

  - `radar_options.session` (string, optional)
    A [Radar Session](https://docs.stripe.com/docs/radar/radar-session.md) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.

- `revolut_pay` (object, optional)
  If this is a `revolut_pay` PaymentMethod, this hash contains details about the Revolut Pay payment method.

- `samsung_pay` (object, optional)
  If this is a `samsung_pay` PaymentMethod, this hash contains details about the SamsungPay payment method.

- `satispay` (object, optional)
  If this is a `satispay` PaymentMethod, this hash contains details about the Satispay payment method.

- `sepa_debit` (object, optional)
  If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account.

  - `sepa_debit.iban` (string, required)
    IBAN of the bank account.

- `sofort` (object, optional)
  If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method.

  - `sofort.country` (enum, required)
    Two-letter ISO code representing the country the bank account is located in.

    Austria

    Belgium

    Germany

    Spain

    Italy

    Netherlands

- `swish` (object, optional)
  If this is a `swish` PaymentMethod, this hash contains details about the Swish payment method.

- `twint` (object, optional)
  If this is a TWINT PaymentMethod, this hash contains details about the TWINT payment method.

- `us_bank_account` (object, optional)
  If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.

  - `us_bank_account.account_holder_type` (enum, optional)
    Account holder type: individual or company.

    Account belongs to a company

    Account belongs to an individual

  - `us_bank_account.account_number` (string, optional)
    Account number of the bank account.

  - `us_bank_account.account_type` (enum, optional)
    Account type: checkings or savings. Defaults to checking if omitted.

    Bank account type is checking

    Bank account type is savings

  - `us_bank_account.financial_connections_account` (string, optional)
    The ID of a Financial Connections Account to use as a payment method.

  - `us_bank_account.routing_number` (string, optional)
    Routing number of the bank account.

- `wechat_pay` (object, optional)
  If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method.

- `zip` (object, optional)
  If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new PaymentMethodCreateOptions
{
    Type = "us_bank_account",
    UsBankAccount = new PaymentMethodUsBankAccountOptions
    {
        AccountHolderType = "individual",
        AccountNumber = "000123456789",
        RoutingNumber = "110000000",
    },
    BillingDetails = new PaymentMethodBillingDetailsOptions { Name = "John Doe" },
};
var service = new PaymentMethodService();
PaymentMethod paymentMethod = service.Create(options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentMethodParams{
  Type: stripe.String(string(stripe.PaymentMethodTypeUSBankAccount)),
  USBankAccount: &stripe.PaymentMethodUSBankAccountParams{
    AccountHolderType: stripe.String(string(stripe.PaymentMethodUSBankAccountAccountHolderTypeIndividual)),
    AccountNumber: stripe.String("000123456789"),
    RoutingNumber: stripe.String("110000000"),
  },
  BillingDetails: &stripe.PaymentMethodBillingDetailsParams{Name: stripe.String("John Doe")},
};
result, err := paymentmethod.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

PaymentMethodCreateParams params =
  PaymentMethodCreateParams.builder()
    .setType(PaymentMethodCreateParams.Type.US_BANK_ACCOUNT)
    .setUsBankAccount(
      PaymentMethodCreateParams.UsBankAccount.builder()
        .setAccountHolderType(PaymentMethodCreateParams.UsBankAccount.AccountHolderType.INDIVIDUAL)
        .setAccountNumber("000123456789")
        .setRoutingNumber("110000000")
        .build()
    )
    .setBillingDetails(
      PaymentMethodCreateParams.BillingDetails.builder().setName("John Doe").build()
    )
    .build();

PaymentMethod paymentMethod = PaymentMethod.create(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const paymentMethod = await stripe.paymentMethods.create({
  type: 'us_bank_account',
  us_bank_account: {
    account_holder_type: 'individual',
    account_number: '000123456789',
    routing_number: '110000000',
  },
  billing_details: {
    name: 'John Doe',
  },
});
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_method = stripe.PaymentMethod.create(
  type="us_bank_account",
  us_bank_account={
    "account_holder_type": "individual",
    "account_number": "000123456789",
    "routing_number": "110000000",
  },
  billing_details={"name": "John Doe"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentMethod = $stripe->paymentMethods->create([
  'type' => 'us_bank_account',
  'us_bank_account' => [
    'account_holder_type' => 'individual',
    'account_number' => '000123456789',
    'routing_number' => '110000000',
  ],
  'billing_details' => ['name' => 'John Doe'],
]);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_method = Stripe::PaymentMethod.create({
  type: 'us_bank_account',
  us_bank_account: {
    account_holder_type: 'individual',
    account_number: '000123456789',
    routing_number: '110000000',
  },
  billing_details: {name: 'John Doe'},
})
```

### Response

```json
{
  "id": "pm_1Q0PsIJvEtkwdCNYMSaVuRz6",
  "object": "payment_method",
  "allow_redisplay": "unspecified",
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
    "name": "John Doe",
    "phone": null
  },
  "created": 1726673582,
  "customer": null,
  "livemode": false,
  "metadata": {},
  "type": "us_bank_account",
  "us_bank_account": {
    "account_holder_type": "individual",
    "account_type": "checking",
    "bank_name": "STRIPE TEST BANK",
    "financial_connections_account": null,
    "fingerprint": "LstWJFsCK7P349Bg",
    "last4": "6789",
    "networks": {
      "preferred": "ach",
      "supported": [
        "ach"
      ]
    },
    "routing_number": "110000000",
    "status_details": {}
  }
}
```