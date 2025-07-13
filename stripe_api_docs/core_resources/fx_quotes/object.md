# The FX Quote object

## Attributes

### id
**string**  
Unique identifier for the object.

### lock_duration
**enum**  
The duration the exchange rate quote remains valid from creation time. Allowed values are `none`, `hour`, and `day`. Note that for the test mode API available in alpha, you can request an extended quote, but it won't be usable for any transactions.

**Possible enum values:**
- `day` - Requests a quote valid for one day
- `five_minutes` - Requests a quote valid for five minutes
- `hour` - Requests a quote valid for one hour
- `none` - Requests a quote valid without lock rate

### rates
**object**  
Information about the rates.

#### rates.<from_currency>.exchange_rate
**float**  
The rate that includes the FX fee rate.

#### rates.<from_currency>.rate_details
**object**  
The breakdown of the rates.

##### rates.<from_currency>.rate_details.base_rate
**float**  
The rate for the currency pair.

##### rates.<from_currency>.rate_details.duration_premium
**float**  
The fee for locking the conversion rates.

##### rates.<from_currency>.rate_details.fx_fee_rate
**float**  
The FX fee for the currency pair.

##### rates.<from_currency>.rate_details.reference_rate
**nullable float**  
A reference rate for the currency pair provided by the reference rate provider.

##### rates.<from_currency>.rate_details.reference_rate_provider
**nullable enum**  
The reference rate provider.

**Possible enum values:**
- `ecb` - The European Central Bank is reference rate provider.

We provide the reference rate when both the `from_currency` and `to_currency` are in the following list:

`eur`, `usd`, `jpy`, `bgn`, `czk`, `dkk`, `gbp`, `huf`, `pln`, `ron`, `sek`, `chf`, `isk`, `nok`, `try`, `aud`, `brl`, `cad`, `cny`, `hkd`, `idr`, `ils`, `inr`, `krw`, `mxn`, `myr`, `nzd`, `php`, `sgd`, `thb`, `zar`

## The FX Quote object

```json
{
  "id": "fxq_1QKf8UET9NELqCotgW6CNTnm",
  "object": "fx_quote",
  "created": 1731498806.6424642,
  "lock_duration": "hour",
  "lock_expires_at": 1731502406.5579598,
  "lock_status": "active",
  "rates": {
    "gbp": {
      "exchange_rate": 1.10167,
      "rate_details": {
        "base_rate": 1.12415,
        "fx_fee_rate": 0.02,
        "reference_rate": 1.12437,
        "reference_rate_provider": "ecb"
      }
    },
    "krw": {
      "exchange_rate": 0.000617274,
      "rate_details": {
        "base_rate": 0.000629871,
        "fx_fee_rate": 0.02,
        "reference_rate": 0.000629997,
        "reference_rate_provider": "ecb"
      }
    }
  },
  "to_currency": "chf",
  "usage": {
    "payment": null,
    "transfer": null,
    "type": "payment"
  }
}
``` 