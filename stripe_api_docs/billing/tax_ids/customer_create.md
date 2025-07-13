# Create a Customer tax ID

Creates a new `tax_id` object for a customer.

The created `tax_id` object.

- `type` (string, required)
  Type of the tax ID, one of `ad_nrt`, `ae_trn`, `al_tin`, `am_tin`, `ao_tin`, `ar_cuit`, `au_abn`, `au_arn`, `aw_tin`, `az_tin`, `ba_tin`, `bb_tin`, `bd_bin`, `bf_ifu`, `bg_uic`, `bh_vat`, `bj_ifu`, `bo_tin`, `br_cnpj`, `br_cpf`, `bs_tin`, `by_tin`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `cd_nif`, `ch_uid`, `ch_vat`, `cl_tin`, `cm_niu`, `cn_tin`, `co_nit`, `cr_tin`, `cv_nif`, `de_stn`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `et_tin`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `gn_nif`, `hk_br`, `hr_oib`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kg_tin`, `kh_tin`, `kr_brn`, `kz_bin`, `la_tin`, `li_uid`, `li_vat`, `ma_vat`, `md_vat`, `me_pib`, `mk_vat`, `mr_nif`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `ng_tin`, `no_vat`, `no_voec`, `np_pan`, `nz_gst`, `om_vat`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sn_ninea`, `sr_fin`, `sv_nit`, `th_vat`, `tj_tin`, `tr_tin`, `tw_vat`, `tz_vat`, `ua_vat`, `ug_tin`, `us_ein`, `uy_ruc`, `uz_tin`, `uz_vat`, `ve_rif`, `vn_tin`, `za_vat`, `zm_tin`, or `zw_tin`

- `value` (string, required)
  Value of the tax ID.

```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var options = new CustomerTaxIdCreateOptions { Type = "eu_vat", Value = "DE123456789" };
var service = new CustomerTaxIdService();
TaxId taxId = service.Create("cus_NZKoSNZZ58qtO0", options);
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.TaxIDParams{
  Type: stripe.String(string(stripe.TaxIDTypeEUVAT)),
  Value: stripe.String("DE123456789"),
  Customer: stripe.String("cus_NZKoSNZZ58qtO0"),
};
result, err := taxid.New(params);
```

```java
Stripe.apiKey = "<<secret key>>";

TaxIdCollectionCreateParams params =
  TaxIdCollectionCreateParams.builder()
    .setType(TaxIdCollectionCreateParams.Type.EU_VAT)
    .setValue("DE123456789")
    .build();

TaxId taxId = TaxId.create("cus_NZKoSNZZ58qtO0", params);
```

```node
const stripe = require('stripe')('<<secret key>>');

const taxId = await stripe.customers.createTaxId(
  'cus_NZKoSNZZ58qtO0',
  {
    type: 'eu_vat',
    value: 'DE123456789',
  }
);
```

```python
import stripe
stripe.api_key = "<<secret key>>"

tax_id = stripe.Customer.create_tax_id(
  "cus_NZKoSNZZ58qtO0",
  type="eu_vat",
  value="DE123456789",
)
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$taxId = $stripe->customers->createTaxId(
  'cus_NZKoSNZZ58qtO0',
  [
    'type' => 'eu_vat',
    'value' => 'DE123456789',
  ]
);
```

```ruby
Stripe.api_key = '<<secret key>>'

tax_id = Stripe::Customer.create_tax_id(
  'cus_NZKoSNZZ58qtO0',
  {
    type: 'eu_vat',
    value: 'DE123456789',
  },
)
```

### Response

```json
{
  "id": "txi_1MoC8zLkdIwHu7ixEhgWcHzJ",
  "object": "tax_id",
  "country": "DE",
  "created": 1679431857,
  "customer": "cus_NZKoSNZZ58qtO0",
  "livemode": false,
  "type": "eu_vat",
  "value": "DE123456789",
  "verification": {
    "status": "pending",
    "verified_address": null,
    "verified_name": null
  }
}
```