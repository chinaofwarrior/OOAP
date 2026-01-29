# Core Concepts

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Backend SDK

Core Concepts

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

* [NekudaClient](#nekudaclient)
* [UserContext](#usercontext)
* [MandateData](#mandatedata)
* [Response Models 🎯](#response-models-%F0%9F%8E%AF)
* [Key Response Models](#key-response-models)
* [Example with Type Safety](#example-with-type-safety)
* [Error Hierarchy](#error-hierarchy)
* [Advanced Features 🚀](#advanced-features-%F0%9F%9A%80)
* [Response Validation](#response-validation)
* [URL Normalization](#url-normalization)
* [Performance & Re-usability](#performance-%26-re-usability)
* [What’s Next?](#what%E2%80%99s-next)

Backend SDK

# Core Concepts

Copy page

Understand the key building blocks of the nekuda SDK.

Copy page

Before jumping into advanced usage, it’s worth getting familiar with the **building blocks** that form the nekuda SDK public surface.

## [​](#nekudaclient) NekudaClient

The **single entry-point** to all network operations that:

* Manages an internal persistent HTTP client with automatic **retry & back-off** for 5xx / 429 responses
* Can be instantiated directly or via the convenience constructor from environment variables
* **Automatically normalizes URLs** (adds `https://`, removes trailing slashes). The default base URL is `https://api.nekuda.ai`

* Python
* TypeScript

Direct Instantiation

Environment Variables

Copy

Ask AI

```
from nekuda import NekudaClient

# Production client
client = NekudaClient(api_key="sk_live_...")

# Client pointing to a different API endpoint (e.g. staging)
# client = NekudaClient(api_key="sk_test_...", base_url="https://staging-api.nekuda.ai")
```

Direct Instantiation

Environment Variables

Copy

Ask AI

```
import { NekudaClient } from '@nekuda/nekuda-js';

// All of these work the same way:
const client = new NekudaClient('sk_...', { baseUrl: 'api.nekuda.ai' });
const client = new NekudaClient('sk_...', { baseUrl: 'https://api.nekuda.ai/' });
```

## [​](#usercontext) UserContext

A lightweight wrapper returned by `client.user(user_id)` that automatically injects the `user_id` header on every call.
**A `user_id` is mandatory for all user-specific operations like creating mandates or revealing cards.**

* Python
* TypeScript

Copy

Ask AI

```
from nekuda import NekudaClient, MandateData

client = NekudaClient.from_env()

# You must provide a unique user_id for each of your users.
user_id = "user_unique_identifier_123"
user = client.user(user_id)

# Example MandateData (details below)
mandate_details = MandateData(
    product="Example Product",
    price=10.99,
    currency="USD",
    merchant="YourStore"
)

# The user_id is now automatically included in the following calls:
# 1. Create a mandate (intent to purchase)
mandate_response = user.create_mandate(mandate_details)

# 2. A mandate must be created first to obtain a mandate_id.
# This mandate_id is then used to request a card reveal token.
reveal_response = user.request_card_reveal_token(mandate_response.mandate_id)

# 3. Exchange the token for card details
card_details_response = user.reveal_card_details(reveal_response.token)
```

Copy

Ask AI

```
import { NekudaClient, MandateData } from '@nekuda/nekuda-js';

const client = NekudaClient.fromEnv();
const user = client.user('user_unique_identifier_123');

// Example MandateData (details below)
const mandate = new MandateData({
  product: 'Example Product',
  price: 10.99,
  currency: 'USD',
  merchant: 'YourStore'
});

// All methods return typed response interfaces!
// 1. Create a mandate (intent to purchase)
const mandateResponse = await user.createMandate(mandate);

// 2. Request reveal token using mandate_id
const revealResponse = await user.requestCardRevealToken(mandateResponse.mandateId);

// 3. Exchange the token for card details
const cardDetails = await user.revealCardDetails(revealResponse.revealToken);
```

Behind the scenes **no extra network round-trip** happens for
`client.user(user_id)` – `UserContext` is just a convenience object that
stores the `user_id`.

## [​](#mandatedata) MandateData

A data class that represents the **user’s intent to purchase**.
It must be successfully submitted via `user.create_mandate(mandate_data)` to obtain a `mandate_id` before you can request a card reveal token.

* Python
* TypeScript

Copy

Ask AI

```
from nekuda import MandateData

mandate = MandateData(
    product="Premium Subscription",
    price=49.99,
    currency="USD",
    merchant="nekuda Corp",
    # Optional fields:
    merchant_link="https://app.nekuda.ai/premium",
    product_description="Access to all premium features",
    confidence_score=0.95
)
```

Client-side validation runs in `__post_init__`. Invalid payloads raise `NekudaValidationError` **before** any HTTP request is made.

Copy

Ask AI

```
import { MandateData } from '@nekuda/nekuda-js';

const mandate = new MandateData({
  product: 'Premium Subscription',
  price: 49.99,
  currency: 'USD',
  merchant: 'nekuda Corp',
  // Optional fields:
  merchantLink: 'https://nekuda.ai/premium',
  productDescription: 'Access to all premium features',
  confidenceScore: 0.95
});
```

Client-side validation runs in the constructor. Invalid payloads throw `NekudaValidationError` **before** any HTTP request is made.

## [​](#response-models-🎯) Response Models 🎯

All API methods return **strongly-typed response models**. This provides:

* **Type safety** - Your IDE knows exactly what fields are available
* **Validation** - Card numbers, expiry dates, etc. are automatically validated
* **Better errors** - Clear messages when API returns unexpected data

### [​](#key-response-models) Key Response Models

* Python
* TypeScript

CardRevealTokenResponse

Copy

Ask AI

```
class CardRevealTokenResponse:
    reveal_token: str         # The one-time token
    reveal_path: str          # API endpoint for reveal
    expires_at: datetime?     # Optional expiration
```

CardDetailsResponse

Copy

Ask AI

```
class CardDetailsResponse:
    card_number: str         # Validated 13-19 digits
    card_expiry_date: str    # Validated MM/YY format
    cardholder_name: str     # Name on card
    # ... plus optional fields
```

MandateCreateResponse

Copy

Ask AI

```
class MandateCreateResponse:
    mandate_id: int
    request_id: str
    customer_id: str  # This is the user_id you provided
    created_at: datetime
```

CardRevealTokenResponse

Copy

Ask AI

```
interface CardRevealTokenResponse {
  revealToken: string;         // The one-time token
  expiresAt?: Date;           // Optional expiration
}
```

CardDetailsResponse

Copy

Ask AI

```
interface CardDetailsResponse {
  cardNumber: string;          // Validated 13-19 digits
  cardExpiryDate: string;     // Validated MM/YY format
  cardholderName: string;     // Name on card
  // ... plus optional fields
}
```

MandateCreateResponse

Copy

Ask AI

```
interface MandateCreateResponse {
  mandateId: number;
  requestId: string;
  customerId: string;
  createdAt: Date;
}
```

### [​](#example-with-type-safety) Example with Type Safety

* Python
* TypeScript

Before (raw dicts) - prone to KeyError

After (typed models) - IDE autocomplete!

Copy

Ask AI

```
# user_id had to be passed in each call
token_dict = client.request_card_reveal_token(user_id="some_user", mandate_id="m_123")
token = token_dict["reveal_token"]  # 😟 Hope the key exists!
```

Before (untyped) - prone to runtime errors

After (typed interfaces) - IDE autocomplete!

Copy

Ask AI

```
const token = (await client.requestCardRevealToken(...)). token; // 😟
```

## [​](#error-hierarchy) Error Hierarchy

All exceptions inherit from a common `NekudaError` base class so a single error handler can catch everything:

Copy

Ask AI

```
NekudaError
 ├─ NekudaApiError
 │   ├─ AuthenticationError     # 401
 │   ├─ InvalidRequestError     # 4xx / 404
 │   ├─ CardNotFoundError       # 404 (specific case)
 │   ├─ RateLimitError          # 429 (retry-able)
 │   └─ ServerError             # 5xx (retry-able)
 ├─ NekudaConnectionError       # network issues
 └─ NekudaValidationError       # client-side validation failed
```

The SDK detects and properly handles HTML error pages (nginx
errors, gateway timeouts) that sometimes occur during infrastructure issues.

For a deep-dive see the dedicated [Error Handling](/nekuda-sdk/Errors) page.

## [​](#advanced-features-🚀) Advanced Features 🚀

### [​](#response-validation) Response Validation

The SDK automatically validates all API responses:


Response Validation Features

* HTML error pages (502 Bad Gateway, nginx errors) - Invalid JSON responses -
  Missing required fields - Invalid field formats

### [​](#url-normalization) URL Normalization

The default base URL is `https://api.nekuda.ai`. You generally don’t need to set this unless using a staging or mock server.

* Python
* TypeScript

Copy

Ask AI

```
# Client uses https://api.nekuda.ai by default
client_prod = NekudaClient(api_key="sk_live_...")

# Example for staging (if needed)
# client_staging = NekudaClient(api_key="sk_test_...", base_url="https://staging-api.nekuda.ai")
```

Copy

Ask AI

```
// All valid:
new NekudaClient('sk_...', { baseUrl: 'api.nekuda.ai' });
new NekudaClient('sk_...', { baseUrl: 'http://localhost:8000/' });
new NekudaClient('sk_...', { baseUrl: 'staging.api.nekuda.ai/v1/' });
```

## [​](#performance-&-re-usability) Performance & Re-usability

The SDK client is designed to be **cheap to instantiate** but you can (and should) reuse a single instance across the lifetime of your process for maximum performance. Internally it lazily creates the underlying HTTP session the first time you make a request.

* Python
* TypeScript

### [​](#thread-safety) Thread-safety

`NekudaClient` is thread-safe and can be shared across threads.

### [​](#future-roadmap) Future Roadmap

**Async Support Coming Soon** 🔮 The public API has been designed with parity
in mind, so an `AsyncNekudaClient` will drop in without breaking changes.

### [​](#async-first-design) Async-First Design

The TypeScript SDK is built with modern async/await patterns:

Copy

Ask AI

```
// All methods return Promises
const mandate = await user.createMandate(mandateData);
const token = await user.requestCardRevealToken(mandate.mandateId);
const card = await user.revealCardDetails(token.revealToken);
```

## [​](#what’s-next) What’s Next?

[## Usage Guide

Learn the complete payment flow step-by-step](/nekuda-sdk/usage-guide)[## Configuration

Customize the SDK for your production environment](/nekuda-sdk/Configuration)

[Getting Started](/nekuda-sdk/getting-started)[Usage Guide](/nekuda-sdk/usage-guide)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)