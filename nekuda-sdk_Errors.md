# Error Handling

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Backend SDK

Error Handling

[Guides](/introduction)[API Reference](/api-reference/v2/cards/get-card-analytics)

* [Website](https://nekuda.ai)
* [X](https://x.com/nekuda_ai)
* [Blog](https://nekuda.substack.com/)

##### Get Started

* [Introduction](/introduction)
* [Quickstart](/nekuda-sdk/Quickstart)
* [System Overview](/system-overview)
* [Payment Flow](/payment-flow)
* [Payment Flow Scenarios](/payment-flow-scenarios)
* [Support](/support)

##### Frontend SDK

* [Wallet Overview](/frontend/wallet/overview)
* [Payment Methods Tab](/frontend/wallet/payment-methods-tab)
* [Settings Tab](/frontend/wallet/settings-tab)
* [CVV Management](/frontend/wallet/cvv-management)
* [Collection Form](/frontend/wallet/collect-form)
* [Styling & Theming](/frontend/wallet/styling-theming)
* [Integration Patterns](/frontend/wallet/integration-patterns)
* [Migration Guide](/frontend/wallet/migration-guide)

##### Backend SDK

* [Getting Started](/nekuda-sdk/getting-started)
* [Core Concepts](/nekuda-sdk/core-concepts)
* [Usage Guide](/nekuda-sdk/usage-guide)
* [Configuration](/nekuda-sdk/Configuration)
* [Error Handling](/nekuda-sdk/Errors)

##### Security

* [Best practices](/best-practices)
* [Policy Engine & Safety](/policy-engine-safety)

##### Testing

* [Testing Cards](/testing/testing-cards)

On this page

* [Quick Example](#quick-example)
* [Exception Hierarchy](#exception-hierarchy)
* [New Error Features 🚀](#new-error-features-%F0%9F%9A%80)
* [Retriable Errors](#retriable-errors)
* [Best Practices](#best-practices)
* [1. Catch Specific Errors First, Then Broader Ones](#1-catch-specific-errors-first%2C-then-broader-ones)
* [2. Use Exception Attributes for Logging and Control Flow](#2-use-exception-attributes-for-logging-and-control-flow)
* [3. Don’t Retry NekudaValidationError or AuthenticationError](#3-don%E2%80%99t-retry-nekudavalidationerror-or-authenticationerror)
* [Error Response Examples](#error-response-examples)
* [Logging & Monitoring](#logging-%26-monitoring)
* [Common Scenarios & Solutions](#common-scenarios-%26-solutions)
* [Handle Missing Cards Gracefully (CardNotFoundError)](#handle-missing-cards-gracefully-cardnotfounderror)
* [Retry Logic for Flaky Networks (NekudaConnectionError, ServerError)](#retry-logic-for-flaky-networks-nekudaconnectionerror%2C-servererror)
* [Validate Mandate Data Before Sending (NekudaValidationError on input)](#validate-mandate-data-before-sending-nekudavalidationerror-on-input)
* [Error Testing](#error-testing)
* [What’s Next?](#what%E2%80%99s-next)

Backend SDK

# Error Handling

Copy page

Build resilient applications with comprehensive error handling in the nekuda SDK.

Copy page

The nekuda SDK attempts to surface **actionable** errors – no gigantic stack-traces, no generic catch-alls. Everything inherits from `NekudaError` so you can decide how granular you want your error handling to be.

## [​](#quick-example) Quick Example

* Python
* TypeScript

Copy

Ask AI

```
from nekuda import NekudaClient, NekudaError, CardNotFoundError, NekudaValidationError

client = NekudaClient.from_env()
user_id = "user_example_456"
user = client.user(user_id)

# Assume mandate_id is obtained after user.create_mandate(...)
mandate_id_example = "mand_0abc123def456"

try:
    # This call requires a valid mandate_id obtained from user.create_mandate()
    response = user.request_card_reveal_token(mandate_id=mandate_id_example)
    print(f"Token: {response.token}")

except CardNotFoundError as exc:
    # Specific error if the card associated with user_id (and potentially mandate_id) is not found
    print(f"Card not found for user {exc.user_id}. Message: {exc.message}")
    # Ensure the user_id is correct and card details were collected.

except InvalidRequestError as exc:
    # Handles 4xx errors like invalid parameters (e.g., malformed mandate_id)
    print(f"Invalid request: {exc.message} (Code: {exc.code}, Status: {exc.status_code})")

except NekudaValidationError as exc:
    # If API response doesn't match expected Pydantic model format, or input validation fails
    print(f"Validation Error: {exc}")

except AuthenticationError as exc:
    print(f"Authentication failed: {exc.message}. Check your NEKUDA_API_KEY.")

except NekudaApiError as exc:
    # Catch other API errors (5xx, rate limits if not retried, etc.)
    print(f"nekuda API Error: {exc.message} (Code: {exc.code}, Status: {exc.status_code})")

except NekudaError as exc:
    # Catch-all for other SDK-specific errors (e.g., NekudaConnectionError)
    print(f"A nekuda SDK error occurred: {exc}")
```

Copy

Ask AI

```
import { NekudaClient, NekudaError, CardNotFoundError, NekudaValidationError } from '@nekuda/nekuda-js';

const client = NekudaClient.fromEnv();
const user = client.user('user_example_456');

try {
  // Assume mandateId is obtained after user.createMandate(...)
  const response = await user.requestCardRevealToken('mand_0abc123def456');
  console.log(`Token: ${response.revealToken}`);

} catch (error) {
  if (error instanceof CardNotFoundError) {
    // Specific error for card not found
    console.log(`Card not found for user ${error.userId}`);
    console.log('Helpful message:', error.message);

  } else if (error instanceof NekudaValidationError) {
    // Response didn't match expected format
    console.log('Invalid response from API:', error);

  } else if (error instanceof NekudaApiError) {
    // Other API errors
    console.log('API Error:', error.message);
    console.log(`Status: ${error.statusCode}, Code: ${error.code}`);

  } else if (error instanceof NekudaError) {
    // Catch-all for other SDK errors
    console.log('Something went wrong:', error);
  }
}
```

## [​](#exception-hierarchy) Exception Hierarchy

All exceptions in the nekuda SDK inherit from `NekudaError`.

Copy

Ask AI

```
NekudaError                      # Base class for all SDK errors
 ├─ NekudaApiError               # Errors originating from the nekuda API (HTTP response received)
 │   ├─ AuthenticationError      # 401 – Missing or bad API key (NEKUDA_API_KEY)
 │   ├─ InvalidRequestError      # 4xx (e.g., 400, 404) – Malformed params, resource not found, etc.
 │   │   └─ CardNotFoundError    # Specific 404 when card details for a user are not found
 │   ├─ RateLimitError           # 429 – API rate limit exceeded (SDK retries these automatically based on max_retries)
 │   └─ ServerError              # 5xx – nekuda backend experienced an issue (SDK retries these automatically)
 ├─ NekudaConnectionError        # Network issues (DNS, TCP, TLS failures before API response)
 └─ NekudaValidationError        # Client-side Pydantic model validation failed (input or response data)
```

## [​](#new-error-features-🚀) New Error Features 🚀

HTML Error Detection

The SDK automatically detects if the API returns an HTML error page (e.g., 502 Bad Gateway, nginx errors) and raises a `NekudaApiError` with extracted information, instead of failing on JSON parsing.

Response Validation Errors

If an API response doesn’t match the expected schema (e.g., missing required fields, incorrect data types), a `NekudaValidationError` is raised, pinpointing the discrepancy.Example: `"Response validation failed for CardDetailsResponse: card_expiry_date: Card expiry must be in MM/YY format"`

Helpful Card Not Found Messages

`CardNotFoundError` provides a more specific message:

* Python
* TypeScript

Copy

Ask AI

```
# except CardNotFoundError as e:
#     print(e.message)
# Output example:
# Card details not found for user 'user_example_456'. This usually means:
# 1. No payment information has been collected for this user with this user_id yet.
# 2. You are using a different user_id than was used during card collection (frontend vs backend).
# 3. The card data may have expired or been cleaned up by nekuda systems.
# Ensure the user has completed card collection and the user_id matches.
```

Copy

Ask AI

```
// catch (error) {
//   if (error instanceof CardNotFoundError) {
//     console.log(error.message);
//   }
// }
// Output:
// Card details not found. This usually means:
// 1. No payment information has been collected for this user yet
// 2. You're using a different user_id than was used during card collection
// 3. The card data may have expired or been cleaned up
// → Ensure the user 'user_example_456' has completed card collection with the same user_id
```

### [​](#retriable-errors) Retriable Errors

`RateLimitError` (429) and `ServerError` (5xx) are automatically retried by the SDK based on the retry configuration. If all retries fail, the final error is raised.

## [​](#best-practices) Best Practices

### [​](#1-catch-specific-errors-first,-then-broader-ones) 1. Catch Specific Errors First, Then Broader Ones

This allows for tailored error handling logic.

* Python
* TypeScript

✅ Good Error Handling Structure

Copy

Ask AI

```
from nekuda import NekudaClient, NekudaError, CardNotFoundError, InvalidRequestError, AuthenticationError, NekudaValidationError

client = NekudaClient.from_env()
user = client.user("test_user")

try:
    # Your SDK calls, e.g., user.create_mandate(...), user.request_card_reveal_token(...)
    pass # Replace with actual calls
except CardNotFoundError as e:
    # Handle card not found: prompt user to add/update payment method
    print(f"Card not found: {e.message}")
except InvalidRequestError as e:
    # Handle bad request: check parameters, log error
    print(f"Invalid request to nekuda API: {e.message}, Code: {e.code}")
except AuthenticationError as e:
    # Handle auth failure: verify API key, alert ops
    print(f"nekuda API Key is invalid or missing: {e.message}")
except NekudaValidationError as e:
    # Handle validation issue (likely SDK or API contract mismatch): log, alert devs
    print(f"Data validation error: {e}")
except NekudaApiError as e:
    # Handle other API errors (e.g., rate limits after retries, server errors after retries)
    print(f"nekuda API Error: {e.message}, Status: {e.status_code}, Code: {e.code}")
except NekudaConnectionError as e:
    # Handle network issues: check connectivity, maybe retry later if appropriate for your app
    print(f"Could not connect to nekuda API: {e}")
except NekudaError as e: # Fallback for any other nekuda SDK specific errors
    print(f"An unexpected nekuda SDK error occurred: {e}")
except Exception as e: # General fallback for non-SDK errors
    print(f"An unexpected general error occurred: {e}")
```

✅ Good Error Handling Structure

Copy

Ask AI

```
import { NekudaClient, NekudaError, CardNotFoundError, InvalidRequestError, AuthenticationError, NekudaValidationError, NekudaApiError, NekudaConnectionError } from '@nekuda/nekuda-js';

const client = NekudaClient.fromEnv();
const user = client.user('test_user');

try {
  // Your SDK calls, e.g., user.createMandate(...), user.requestCardRevealToken(...)
  // await user.createMandate(...);
} catch (error) {
  if (error instanceof CardNotFoundError) {
    // Handle card not found: prompt user to add/update payment method
    console.log(`Card not found: ${error.message}`);
  } else if (error instanceof InvalidRequestError) {
    // Handle bad request: check parameters, log error
    console.log(`Invalid request: ${error.message}, Code: ${error.code}`);
  } else if (error instanceof AuthenticationError) {
    // Handle auth failure: verify API key, alert ops
    console.log(`API Key is invalid or missing: ${error.message}`);
  } else if (error instanceof NekudaValidationError) {
    // Handle validation issue: log, alert devs
    console.log(`Data validation error: ${error}`);
  } else if (error instanceof NekudaApiError) {
    // Handle other API errors
    console.log(`API Error: ${error.message}, Status: ${error.statusCode}, Code: ${error.code}`);
  } else if (error instanceof NekudaConnectionError) {
    // Handle network issues
    console.log(`Could not connect to nekuda API: ${error}`);
  } else if (error instanceof NekudaError) {
    // Fallback for any other SDK errors
    console.log(`An unexpected SDK error occurred: ${error}`);
  } else {
    // General fallback for non-SDK errors
    console.log(`An unexpected error occurred: ${error}`);
  }
}
```

### [​](#2-use-exception-attributes-for-logging-and-control-flow) 2. Use Exception Attributes for Logging and Control Flow

All `NekudaApiError` instances (and its children like `InvalidRequestError`, `AuthenticationError`) have consistent attributes for structured logging.

* Python
* TypeScript

Copy

Ask AI

```
# import logging_library as logger # Fictional logging library

# try:
#    # ... SDK call ...
# except NekudaApiError as e:
#     logger.error(
#         "nekuda API call failed",
#         status_code=e.status_code,
#         error_code=e.code,
#         error_message=e.message,
#         user_id=current_user_id # Add your own contextual info
#     )
#     if e.status_code == 400 and e.code == "invalid_parameter_foo":
#         # Specific handling for a known bad parameter
#         return "Please correct parameter foo."
```

Copy

Ask AI

```
// try {
//   // ... SDK call ...
// } catch (error) {
//   if (error instanceof NekudaApiError) {
//     console.error('nekuda API call failed', {
//       statusCode: error.statusCode,
//       errorCode: error.code,
//       errorMessage: error.message,
//       userId: currentUserId // Add your own contextual info
//     });
//     if (error.statusCode === 400 && error.code === 'invalid_parameter_foo') {
//       // Specific handling for a known bad parameter
//       return 'Please correct parameter foo.';
//     }
//   }
// }
```

### [​](#3-don’t-retry-nekudavalidationerror-or-authenticationerror) 3. Don’t Retry `NekudaValidationError` or `AuthenticationError`

* `NekudaValidationError`: Indicates an issue with the data sent or received, or a mismatch with the API schema. Retrying the same call will likely fail again. This usually points to a bug in your client code or an unexpected API change.
* `AuthenticationError`: Your API key is invalid. Retrying won’t help until the key is fixed.

Client-side `NekudaValidationError` on *input* (e.g., when creating `MandateData`) should be caught and fixed before making an API call. `NekudaValidationError` on *response* indicates an issue with the data returned by the API not matching the SDK’s expectations.

## [​](#error-response-examples) Error Response Examples

These show how attributes of exceptions can be accessed.

* API Error (JSON)
* HTML Error Page
* Client Validation Error
* Response Validation Error

If nekuda API returns a JSON error like: `{"error": {"code": "invalid_mandate_id", "message": "Mandate ID 'm-123' not found.", "status_code": 404}}`

Copy

Ask AI

```
# try:
#     # user.request_card_reveal_token(mandate_id="m-123")
# except InvalidRequestError as e: # Or NekudaApiError for broader catch
#     print(e.code)         # "invalid_mandate_id"
#     print(e.message)      # "Mandate ID 'm-123' not found."
#     print(e.status_code)  # 404
```

If the API or an intermediary (like a proxy) returns an HTML error page (e.g., 502 Bad Gateway):

Copy

Ask AI

```
# try:
#     # ... some SDK call ...
# except NekudaApiError as e: # Could be ServerError or a generic NekudaApiError
#     print(e.code)         # e.g., "service_unavailable" or "unknown_api_error"
#     print(e.message)      # e.g., "The server returned an HTML error page (status 502)" or similar
#     print(e.status_code)  # e.g., 502
```

If you provide invalid data to an SDK model (before any API call):

Copy

Ask AI

```
# from nekuda import MandateData, NekudaValidationError
# try:
#     mandate = MandateData(product="Test", price=-10, currency="USD") # Invalid price
# except NekudaValidationError as e:
#     print(str(e))
#     # Example output related to pydantic validation:
#     # "1 validation error for MandateData\nprice\n  Value error, Price must be positive [-10.0]"
```

If API returns data that doesn’t match the SDK’s Pydantic models:
For example, if API sends `{"card_exp_date": "2025/12"}` but SDK expects `card_expiry_date`.

Copy

Ask AI

```
# try:
#     # card_details = user.reveal_card_details(token="some_token")
# except NekudaValidationError as e:
#     print(str(e))
#     # Example output for Pydantic model validation failure on response:
#     # "Response validation failed for CardDetailsResponse: 1 validation error for CardDetailsResponse\ncard_expiry_date\n  Field required [type=missing, ... ]"
```

## [​](#logging-&-monitoring) Logging & Monitoring

Every `NekudaError` (and its children) can be easily logged. `NekudaApiError` instances also provide `code` and `status_code`.

| Attribute | Example (`NekudaApiError`) | Description |
| --- | --- | --- |
| `message` | ”Card details not found…” | Human-readable explanation |
| `code` | `card_not_found` | Stable machine token from API (if available) |
| `status_code` | `404` | HTTP status returned by backend (if API error) |

This structure makes it trivial to ship structured logs to your observability stack:

Copy

Ask AI

```
import logging # Python's built-in logging
# import structlog # Or a structured logging library like structlog

logger = logging.getLogger(__name__)

# try:
#     # ... Your SDK call ...
# except NekudaError as e:
#     log_data = {
#         "error_type": type(e).__name__,
#         "message": str(e), # Use str(e) for the full message
#     }
#     if hasattr(e, 'code') and e.code:
#         log_data["error_code"] = e.code
#     if hasattr(e, 'status_code') and e.status_code:
#         log_data["http_status_code"] = e.status_code
#
#     logger.error("nekuda SDK operation failed", extra=log_data)
```

## [​](#common-scenarios-&-solutions) Common Scenarios & Solutions

### [​](#handle-missing-cards-gracefully-cardnotfounderror) Handle Missing Cards Gracefully (`CardNotFoundError`)

Copy

Ask AI

```
# def get_user_card_for_checkout(user_id: str, mandate_id: str):
#     user = client.user(user_id)
#     try:
#         token_response = user.request_card_reveal_token(mandate_id)
#         card_details = user.reveal_card_details(token_response. token)
#         return card_details # Proceed to checkout
#     except CardNotFoundError:
#         # Card not found, guide user to add/update payment method in your frontend
#         # This might involve redirecting them or showing a message.
#         print(f"No card on file for user {user_id} for this transaction.")
#         return None # Or raise a custom application error
#     except NekudaError as e:
#         print(f"Could not retrieve card: {e}")
#         return None # Or raise
```

### [​](#retry-logic-for-flaky-networks-nekudaconnectionerror,-servererror) Retry Logic for Flaky Networks (`NekudaConnectionError`, `ServerError`)

The `nekuda` SDK handles retries for `ServerError` and `RateLimitError` automatically. You typically only need custom retry logic for `NekudaConnectionError` if you want more control than simple immediate retries, or if you want to retry application-level logic that includes SDK calls.

Copy

Ask AI

```
# import time
# from nekuda import NekudaConnectionError, ServerError

# MAX_APP_RETRIES = 3
# for attempt in range(MAX_APP_RETRIES):
#     try:
#         # Your business logic that includes one or more SDK calls
#         # result = make_payment_attempt_with_nekuda_sdk(...)
#         # if result.is_success(): break
#     except NekudaConnectionError as e:
#         if attempt == MAX_APP_RETRIES - 1:
#             # Log final failure and give up or alert
#             raise
#         print(f"Connection error (attempt {attempt + 1}), retrying in {2 ** attempt}s...")
#         time.sleep(2 ** attempt)  # Exponential backoff for connection errors
#     except ServerError as e: # SDK already retried this, this is the final one
#          print(f"nekuda server error after SDK retries: {e}. Might need to investigate.")
#          # Depending on the error, might break or schedule for later.
#          break
```

### [​](#validate-mandate-data-before-sending-nekudavalidationerror-on-input) Validate Mandate Data Before Sending (`NekudaValidationError` on input)

Copy

Ask AI

```
# from nekuda import MandateData, NekudaValidationError
#
# try:
#     # Example: Price is negative, which is invalid
#     mandate = MandateData(product="Test Item", price=-10.00, currency="USD", merchant="Test Store")
# except NekudaValidationError as e:
#     print(f"Invalid mandate data: {e}")
#     # Correct the data based on the error before attempting user.create_mandate(mandate)
```

## [​](#error-testing) Error Testing

Test your application’s error handling by simulating these scenarios with the `nekuda` SDK:


Testing Different Error Conditions

* **AuthenticationError**: Use an invalid `NEKUDA_API_KEY`.
* **InvalidRequestError (e.g., `CardNotFoundError`)**: Try to reveal a card for a `user_id` that has no card, or use an invalid `mandate_id` format.
* **NekudaValidationError (on input)**: Create `MandateData` with invalid values (e.g., negative price).
* **NekudaConnectionError**: Temporarily block network access to `api.nekuda.ai` (e.g., via firewall rule or hosts file) before an SDK call.
* **RateLimitError / ServerError**: Harder to simulate reliably against the live API. For these, trust the SDK’s retry mechanism and test how your application behaves if an error *persists* after SDK retries (i.e., the error that is eventually raised).

## [​](#what’s-next) What’s Next?

[## API Reference

Complete method documentation and examples for the `nekuda` SDK](/nekuda-sdk/api-reference)[## Configuration

Customize the `nekuda` SDK for your environment](/nekuda-sdk/Configuration)

[Configuration](/nekuda-sdk/Configuration)[Best practices](/best-practices)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)