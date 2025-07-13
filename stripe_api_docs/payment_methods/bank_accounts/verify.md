# Verify a bank account

Verify a specified bank account for a given customer.

- `amounts` (array of integers, optional)
  Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account.

### Response

```json
{
  "id": "ba_1NAiwl2eZvKYlo2CRdCLZSxO",
  "object": "bank_account",
  "account_holder_name": "Jane Austen",
  "account_holder_type": "company",
  "account_type": null,
  "bank_name": "STRIPE TEST BANK",
  "country": "US",
  "currency": "usd",
  "customer": "cus_9s6XGDTHzA66Po",
  "fingerprint": "1JWtPxqbdX5Gamtc",
  "last4": "6789",
  "metadata": {},
  "routing_number": "110000000",
  "status": "new",
  "name": "Jenny Rosen"
}
```