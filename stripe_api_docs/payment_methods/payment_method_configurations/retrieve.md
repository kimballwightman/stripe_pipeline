# Retrieve payment method configuration

Retrieve payment method configuration

A payment method configuration object.


```dotnet
StripeConfiguration.ApiKey = "<<secret key>>";

var service = new PaymentMethodConfigurationService();
PaymentMethodConfiguration paymentMethodConfiguration = service.Get("pmc_abcdef");
```

```go
stripe.Key = "<<secret key>>"

params := &stripe.PaymentMethodConfigurationParams{};
result, err := paymentmethodconfiguration.Get("pmc_abcdef", params);
```

```java
Stripe.apiKey = "<<secret key>>";

PaymentMethodConfiguration paymentMethodConfiguration =
  PaymentMethodConfiguration.retrieve("pmc_abcdef");
```

```node
const stripe = require('stripe')('<<secret key>>');

const paymentMethodConfiguration = await stripe.paymentMethodConfigurations.retrieve('pmc_abcdef');
```

```python
import stripe
stripe.api_key = "<<secret key>>"

payment_method_configuration = stripe.PaymentMethodConfiguration.retrieve("pmc_abcdef")
```

```php
$stripe = new \Stripe\StripeClient('<<secret key>>');

$paymentMethodConfiguration = $stripe->paymentMethodConfigurations->retrieve('pmc_abcdef', []);
```

```ruby
Stripe.api_key = '<<secret key>>'

payment_method_configuration = Stripe::PaymentMethodConfiguration.retrieve('pmc_abcdef')
```

### Response

```json
{
  "id": "pmc_abcdef",
  "object": "payment_method_configuration",
  "acss_debit": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "active": true,
  "affirm": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "afterpay_clearpay": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "alipay": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "apple_pay": {
    "available": true,
    "display_preference": {
      "overridable": null,
      "preference": "on",
      "value": "on"
    }
  },
  "bancontact": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "card": {
    "available": true,
    "display_preference": {
      "overridable": null,
      "preference": "on",
      "value": "on"
    }
  },
  "cartes_bancaires": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "eps": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "giropay": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "google_pay": {
    "available": true,
    "display_preference": {
      "overridable": null,
      "preference": "on",
      "value": "on"
    }
  },
  "ideal": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "is_default": true,
  "klarna": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "link": {
    "available": true,
    "display_preference": {
      "overridable": null,
      "preference": "on",
      "value": "on"
    }
  },
  "livemode": false,
  "name": "Default",
  "p24": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "sepa_debit": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "sofort": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "us_bank_account": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  },
  "wechat_pay": {
    "available": false,
    "display_preference": {
      "overridable": null,
      "preference": "off",
      "value": "off"
    }
  }
}
```