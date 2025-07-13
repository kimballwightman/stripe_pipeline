# Handling errors

Our Client libraries raise exceptions for many reasons, such as a failed charge, invalid parameters, authentication errors, and network unavailability. We recommend writing code that gracefully handles all possible API exceptions.

```sh
\# Select a client library to see examples of
# handling different kinds of errors.
```

```ruby
begin
  # Use Stripe's library to make requests...
rescue Stripe::CardError => e
  puts "Status is: #{e.http_status}"
  puts "Type is: #{e.error.type}"
  puts "Charge ID is: #{e.error.charge}"
  # The following fields are optional
  puts "Code is: #{e.error.code}" if e.error.code
  puts "Decline code is: #{e.error.decline_code}" if e.error.decline_code
  puts "Param is: #{e.error.param}" if e.error.param
  puts "Message is: #{e.error.message}" if e.error.message
rescue Stripe::RateLimitError => e
  # Too many requests made to the API too quickly
rescue Stripe::InvalidRequestError => e
  # Invalid parameters were supplied to Stripe's API
rescue Stripe::AuthenticationError => e
  # Authentication with Stripe's API failed
  # (maybe you changed API keys recently)
rescue Stripe::APIConnectionError => e
  # Network communication with Stripe failed
rescue Stripe::StripeError => e
  # Display a very generic error to the user, and maybe send
  # yourself an email
rescue => e
  # Something else happened, completely unrelated to Stripe
end
```

```sh
\# Select a client library to see examples of
# handling different kinds of errors.
```

```python
try:
  # Use Stripe's library to make requests...
  pass
except stripe.error.CardError as e:
  # Since it's a decline, stripe.error.CardError will be caught

  print('Status is: %s' % e.http_status)
  print('Code is: %s' % e.code)
  # param is '' in this case
  print('Param is: %s' % e.param)
  print('Message is: %s' % e.user_message)
except stripe.error.RateLimitError as e:
  # Too many requests made to the API too quickly
  pass
except stripe.error.InvalidRequestError as e:
  # Invalid parameters were supplied to Stripe's API
  pass
except stripe.error.AuthenticationError as e:
  # Authentication with Stripe's API failed
  # (maybe you changed API keys recently)
  pass
except stripe.error.APIConnectionError as e:
  # Network communication with Stripe failed
  pass
except stripe.error.StripeError as e:
  # Display a very generic error to the user, and maybe send
  # yourself an email
  pass
except Exception as e:
  # Something else happened, completely unrelated to Stripe
  pass
```

```php
try {
  // Use Stripe's library to make requests...
} catch(\Stripe\Exception\CardException $e) {
  // Since it's a decline, \Stripe\Exception\CardException will be caught
  echo 'Status is:' . $e->getHttpStatus() . '\n';
  echo 'Type is:' . $e->getError()->type . '\n';
  echo 'Code is:' . $e->getError()->code . '\n';
  // param is '' in this case
  echo 'Param is:' . $e->getError()->param . '\n';
  echo 'Message is:' . $e->getError()->message . '\n';
} catch (\Stripe\Exception\RateLimitException $e) {
  // Too many requests made to the API too quickly
} catch (\Stripe\Exception\InvalidRequestException $e) {
  // Invalid parameters were supplied to Stripe's API
} catch (\Stripe\Exception\AuthenticationException $e) {
  // Authentication with Stripe's API failed
  // (maybe you changed API keys recently)
} catch (\Stripe\Exception\ApiConnectionException $e) {
  // Network communication with Stripe failed
} catch (\Stripe\Exception\ApiErrorException $e) {
  // Display a very generic error to the user, and maybe send
  // yourself an email
} catch (Exception $e) {
  // Something else happened, completely unrelated to Stripe
}
```

```java
try {
  // Use Stripe's library to make requests...
} catch (CardException e) {
  // Since it's a decline, CardException will be caught
  System.out.println("Status is: " + e.getCode());
  System.out.println("Message is: " + e.getMessage());
} catch (RateLimitException e) {
  // Too many requests made to the API too quickly
} catch (InvalidRequestException e) {
  // Invalid parameters were supplied to Stripe's API
} catch (AuthenticationException e) {
  // Authentication with Stripe's API failed
  // (maybe you changed API keys recently)
} catch (APIConnectionException e) {
  // Network communication with Stripe failed
} catch (StripeException e) {
  // Display a very generic error to the user, and maybe send
  // yourself an email
} catch (Exception e) {
  // Something else happened, completely unrelated to Stripe
}
```

```javascript
// Note: Node.js API does not throw exceptions, and instead prefers the
// asynchronous style of error handling described below.
//
// An error from the Stripe API or an otherwise asynchronous error
// will be available as the first argument of any Stripe method's callback:
// E.g. stripe.customers.create({...}, function(err, result) {});
//
// Or in the form of a rejected promise.
// E.g. stripe.customers.create({...}).then(
//        function(result) {},
//        function(err) {}
//      );

switch (err.type) {
  case 'StripeCardError':
    // A declined card error
    err.message; // => e.g. "Your card's expiration year is invalid."
    break;
  case 'StripeRateLimitError':
    // Too many requests made to the API too quickly
    break;
  case 'StripeInvalidRequestError':
    // Invalid parameters were supplied to Stripe's API
    break;
  case 'StripeAPIError':
    // An error occurred internally with Stripe's API
    break;
  case 'StripeConnectionError':
    // Some kind of error occurred during the HTTPS communication
    break;
  case 'StripeAuthenticationError':
    // You probably used an incorrect API key
    break;
  default:
    // Handle any other types of unexpected errors
    break;
}
```

```go
_, err := // Go library call

if err != nil {
  // Try to safely cast a generic error to a stripe.Error so that we can get at
  // some additional Stripe-specific information about what went wrong.
  if stripeErr, ok := err.(*stripe.Error); ok {
    // The Code field will contain a basic identifier for the failure.
    switch stripeErr.Code {
      case stripe.ErrorCodeCardDeclined:
      case stripe.ErrorCodeExpiredCard:
      case stripe.ErrorCodeIncorrectCVC:
      case stripe.ErrorCodeIncorrectZip:
      // etc.
    }

    // The Err field can be coerced to a more specific error type with a type
    // assertion. This technique can be used to get more specialized
    // information for certain errors.
    if cardErr, ok := stripeErr.Err.(*stripe.CardError); ok {
      fmt.Printf("Card was declined with code: %v\n", cardErr.DeclineCode)
    } else {
      fmt.Printf("Other Stripe error occurred: %v\n", stripeErr.Error())
    }
  } else {
    fmt.Printf("Other error occurred: %v\n", err.Error())
  }
}
```

```dotnet
try {
  // Use Stripe's library to make request
} catch (StripeException e) {
  switch (e.StripeError.Type)
  {
    case "card_error":
      Console.WriteLine("Code: " + e.StripeError.Code);
      Console.WriteLine("Message: " + e.StripeError.Message);
      break;
    case "api_connection_error":
      break;
    case "api_error":
      break;
    case "authentication_error":
      break;
    case "invalid_request_error":
      break;
    case "rate_limit_error":
      break;
    case "validation_error":
      break;
    default:
      // Unknown Error Type
      break;
  }
}
```