# Retrieve a given financing offer

Get the details of the financing offer

Returns the financing offer object


### Response

```json
{
  "id": "financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh",
  "object": "capital.financing_offer",
  "account": "acct_1NPvKgBY65lDjjDk",
  "created": 1688423699,
  "expires_after": 1690934400,
  "financing_type": "flex_loan",
  "livemode": true,
  "offered_terms": {
    "advance_amount": 10000,
    "campaign_type": "newly_eligible_user",
    "currency": "usd",
    "fee_amount": 1000,
    "previous_financing_fee_discount_rate": null,
    "withhold_rate": 0.05
  },
  "product_type": "standard",
  "status": "undelivered"
}
```