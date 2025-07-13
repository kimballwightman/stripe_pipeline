# Create or retrieve funding instructions for a customer cash balance

Retrieve funding instructions for a customer cash balance. If funding instructions do not yet exist for the customer, new
funding instructions will be created. If funding instructions have already been created for a given customer, the same
funding instructions will be retrieved. In other words, we will return the same funding instructions each time.

Returns funding instructions for a customer cash balance

- `bank_transfer` (object, required)
  Additional parameters for `bank_transfer` funding types

  - `bank_transfer.type` (enum, required)
    The type of the `bank_transfer`

    A bank transfer to a `eu_bank_transfer`

    A bank transfer to a `gb_bank_transfer`

    A bank transfer to a `jp_bank_transfer`

    A bank transfer to a `mx_bank_transfer`

    A bank transfer to a `us_bank_transfer`

  - `bank_transfer.eu_bank_transfer` (object, optional)
    Configuration for eu_bank_transfer funding type.

    - `bank_transfer.eu_bank_transfer.country` (string, required)
      The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.

  - `bank_transfer.requested_address_types` (array of enums, optional)
    List of address types that should be returned in the financial_addresses response. If not specified, all valid types will be returned.

    Permitted values include: `sort_code`, `zengin`, `iban`, or `spei`.

    An IBAN financial address

    A SortCode financial address

    A Spei financial address

    A Zengin financial address

- `currency` (enum, required)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `funding_type` (enum, required)
  The `funding_type` to get the instructions for.

  Use a bank_transfer hash to define the bank transfer type

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CustomerFundingInstructionsCreateOptions
{
    FundingType = "bank_transfer",
    Currency = "eur",
    BankTransfer = new CustomerFundingInstructionsBankTransferOptions
    {
        Type = "eu_bank_transfer",
        EuBankTransfer = new CustomerFundingInstructionsBankTransferEuBankTransferOptions
        {
            Country = "DE",
        },
    },
};
var service = new CustomerFundingInstructionsService();
FundingInstructions fundingInstructions = service.Create("cus_9s6XKzkNRiz8i3", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.CustomerCreateFundingInstructionsParams{
  FundingType: stripe.String("bank_transfer"),
  Currency: stripe.String(string(stripe.CurrencyEUR)),
  BankTransfer: &stripe.CustomerCreateFundingInstructionsBankTransferParams{
    Type: stripe.String("eu_bank_transfer"),
    EUBankTransfer: &stripe.CustomerCreateFundingInstructionsBankTransferEUBankTransferParams{
      Country: stripe.String("DE"),
    },
  },
};
result, err := customer.CreateFundingInstructions("cus_9s6XKzkNRiz8i3", params);
```

```java
Stripe.apiKey = "<<secret key>>";

Customer resource = Customer.retrieve("cus_9s6XKzkNRiz8i3");

CustomerCreateFundingInstructionsParams params =
  CustomerCreateFundingInstructionsParams.builder()
    .setFundingType(CustomerCreateFundingInstructionsParams.FundingType.BANK_TRANSFER)
    .setCurrency("eur")
    .setBankTransfer(
      CustomerCreateFundingInstructionsParams.BankTransfer.builder()
        .setType(CustomerCreateFundingInstructionsParams.BankTransfer.Type.EU_BANK_TRANSFER)
        .setEuBankTransfer(
          CustomerCreateFundingInstructionsParams.BankTransfer.EuBankTransfer.builder()
            .setCountry("DE")
            .build()
        )
        .build()
    )
    .build();

FundingInstructions fundingInstructions = resource.createFundingInstructions(params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const fundingInstructions = await stripe.customers.createFundingInstructions(
  'cus_9s6XKzkNRiz8i3',
  {
    funding_type: 'bank_transfer',
    currency: 'eur',
    bank_transfer: {
      type: 'eu_bank_transfer',
      eu_bank_transfer: {
        country: 'DE',
      },
    },
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

funding_instructions = stripe.Customer.create_funding_instructions(
  "cus_9s6XKzkNRiz8i3",
  funding_type="bank_transfer",
  currency="eur",
  bank_transfer={"type": "eu_bank_transfer", "eu_bank_transfer": {"country": "DE"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$fundingInstructions = $stripe->customers->createFundingInstructions(
  'cus_9s6XKzkNRiz8i3',
  [
    'funding_type' => 'bank_transfer',
    'currency' => 'eur',
    'bank_transfer' => [
      'type' => 'eu_bank_transfer',
      'eu_bank_transfer' => ['country' => 'DE'],
    ],
  ]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

funding_instructions = Stripe::Customer.create_funding_instructions(
  'cus_9s6XKzkNRiz8i3',
  {
    funding_type: 'bank_transfer',
    currency: 'eur',
    bank_transfer: {
      type: 'eu_bank_transfer',
      eu_bank_transfer: {country: 'DE'},
    },
  },
)
```

### Response

```json
{
  "object": "funding_instructions",
  "bank_transfer": {
    "country": "DE",
    "financial_addresses": [
      {
        "iban": {
          "account_holder_address": {
            "city": "Dublin",
            "country": "IE",
            "line1": "Some address",
            "line2": null,
            "postal_code": "D01H104",
            "state": "Dublin 1"
          },
          "account_holder_name": "Merchant name",
          "bank_address": {
            "city": "Dublin",
            "country": "IE",
            "line1": "1 North Wall Quay",
            "line2": null,
            "postal_code": "D01 T8Y1",
            "state": "Dublin"
          },
          "bic": "SOGEDEFFXXX",
          "country": "DE",
          "iban": "DE006847740991234567890"
        },
        "supported_networks": [
          "sepa",
          "swift"
        ],
        "type": "iban"
      }
    ],
    "type": "eu_bank_transfer"
  },
  "currency": "eur",
  "funding_type": "bank_transfer",
  "livemode": false
}
```