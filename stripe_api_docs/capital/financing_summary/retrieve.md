# Retrieve financing summary

Retrieve the financing state for the account that was authenticated in the request.

Returns a financing summary for the account


### Response

```json
{
  "object": "capital.financing_summary",
  "details": {
    "advance_amount": 100000,
    "advance_paid_out_at": 1688424277.0578003,
    "currency": "usd",
    "current_repayment_interval": null,
    "fee_amount": 10000,
    "paid_amount": 100263,
    "remaining_amount": 9737,
    "repayments_begin_at": 1688424277.0577993,
    "withhold_rate": 0.05
  },
  "financing_offer": "financingoffer_1NPvU12eZvKYlo2CotjdGRzu",
  "status": "accepted"
}
```