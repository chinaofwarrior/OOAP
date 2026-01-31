# Core Concepts

Before jumping into advanced usage, it’s worth getting familiar with the **building blocks** that form the Fint SDK public surface.

![Core Concepts](<../.gitbook/assets/Core Concepts.png>)

## FintClient

The **single entry-point** to all network operations that:

* Manages an internal persistent HTTP client with automatic **retry & back-off** for 5xx / 429 responses
* Can be instantiated directly or via the convenience constructor from environment variables
* **Automatically normalizes URLs** (adds `https://`, removes trailing slashes). The default base URL is `https://api.fint.io`
* Python
* TypeScript

```
from fint import FintClient

# Production client
client = FintClient(api_key="sk_live_...")

# Client pointing to a different API endpoint (e.g. staging)
# client = FintClient(api_key="sk_test_...", base_url="https://staging-api.fint.io")
```

```
import { FintClient } from '@fint/fint-js';

// All of these work the same way:
const client = new FintClient('sk_...', { baseUrl: 'api.fint.io' });
const client = new FintClient('sk_...', { baseUrl: 'https://api.fint.io/' });
```

## UserContext

A lightweight wrapper returned by `client.user(user_id)` that automatically injects the `user_id` header on every call. **A `user_id` is mandatory for all user-specific operations like creating mandates or revealing cards.**

* Python
* TypeScript

```
from fint import FintClient, MandateData

client = FintClient.from_env()

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

```
import { FintClient, MandateData } from '@fint/fint-js';

const client = FintClient.fromEnv();
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

Behind the scenes **no extra network round-trip** happens for `client.user(user_id)` – `UserContext` is just a convenience object that stores the `user_id`.

## MandateData

A data class that represents the **user’s intent to purchase**. It must be successfully submitted via `user.create_mandate(mandate_data)` to obtain a `mandate_id` before you can request a card reveal token.

* Python
* TypeScript

```
from fint import MandateData

mandate = MandateData(
    product="Premium Subscription",
    price=49.99,
    currency="USD",
    merchant="Fint Corp",
    # Optional fields:
    merchant_link="https://app.fint.io/premium",
    product_description="Access to all premium features",
    confidence_score=0.95
)
```

Client-side validation runs in `__post_init__`. Invalid payloads raise `FintValidationError` **before** any HTTP request is made.

```
import { MandateData } from '@fint/fint-js';

const mandate = new MandateData({
  product: 'Premium Subscription',
  price: 49.99,
  currency: 'USD',
  merchant: 'Fint Corp',
  // Optional fields:
  merchantLink: 'https://fint.io/premium',
  productDescription: 'Access to all premium features',
  confidenceScore: 0.95
});
```

Client-side validation runs in the constructor. Invalid payloads throw `FintValidationError` **before** any HTTP request is made.

## Response Models 🎯

All API methods return **strongly-typed response models**. This provides:

* **Type safety** - Your IDE knows exactly what fields are available
* **Validation** - Card numbers, expiry dates, etc. are automatically validated
* **Better errors** - Clear messages when API returns unexpected data

### Key Response Models

* Python
* TypeScript

CardRevealTokenResponse

```
class CardRevealTokenResponse:
    reveal_token: str         # The one-time token
    reveal_path: str          # API endpoint for reveal
    expires_at: datetime?     # Optional expiration
```

CardDetailsResponse

```
class CardDetailsResponse:
    card_number: str         # Validated 13-19 digits
    card_expiry_date: str    # Validated MM/YY format
    cardholder_name: str     # Name on card
    # ... plus optional fields
```

MandateCreateResponse

```
class MandateCreateResponse:
    mandate_id: int
    request_id: str
    customer_id: str  # This is the user_id you provided
    created_at: datetime
```

CardRevealTokenResponse

```
interface CardRevealTokenResponse {
  revealToken: string;         // The one-time token
  expiresAt?: Date;           // Optional expiration
}
```

CardDetailsResponse

```
interface CardDetailsResponse {
  cardNumber: string;          // Validated 13-19 digits
  cardExpiryDate: string;     // Validated MM/YY format
  cardholderName: string;     // Name on card
  // ... plus optional fields
}
```

MandateCreateResponse

```
interface MandateCreateResponse {
  mandateId: number;
  requestId: string;
  customerId: string;
  createdAt: Date;
}
```

### Example with Type Safety

* Python
* TypeScript

```
# user_id had to be passed in each call
token_dict = client.request_card_reveal_token(user_id="some_user", mandate_id="m_123")
token = token_dict["reveal_token"]  # 😟 Hope the key exists!
```

```
const token = (await client.requestCardRevealToken(...)). token; // 😟
```

## Error Hierarchy

All exceptions inherit from a common `FintError` base class so a single error handler can catch everything:

```
FintError
 ├─ FintApiError
 │   ├─ AuthenticationError     # 401
 │   ├─ InvalidRequestError     # 4xx / 404
 │   ├─ CardNotFoundError       # 404 (specific case)
 │   ├─ RateLimitError          # 429 (retry-able)
 │   └─ ServerError             # 5xx (retry-able)
 ├─ FintConnectionError       # network issues
 └─ FintValidationError       # client-side validation failed
```

The SDK detects and properly handles HTML error pages (nginx errors, gateway timeouts) that sometimes occur during infrastructure issues.

For a deep-dive see the dedicated [Error Handling](Errors.md) page.

## Advanced Features 🚀

### Response Validation

The SDK automatically validates all API responses:

Response Validation Features

* HTML error pages (502 Bad Gateway, nginx errors) - Invalid JSON responses - Missing required fields - Invalid field formats

### URL Normalization

The default base URL is `https://api.fint.io`. You generally don’t need to set this unless using a staging or mock server.

* Python
* TypeScript

```
# Client uses https://api.fint.io by default
client_prod = FintClient(api_key="sk_live_...")

# Example for staging (if needed)
# client_staging = FintClient(api_key="sk_test_...", base_url="https://staging-api.fint.io")
```

```
// All valid:
new FintClient('sk_...', { baseUrl: 'api.fint.io' });
new FintClient('sk_...', { baseUrl: 'http://localhost:8000/' });
new FintClient('sk_...', { baseUrl: 'staging.api.fint.io/v1/' });
```

## Performance & Re-usability

The SDK client is designed to be **cheap to instantiate** but you can (and should) reuse a single instance across the lifetime of your process for maximum performance. Internally it lazily creates the underlying HTTP session the first time you make a request.

* Python
* TypeScript

### Thread-safety

`FintClient` is thread-safe and can be shared across threads.

### Future Roadmap

**Async Support Coming Soon** 🔮 The public API has been designed with parity in mind, so an `AsyncFintClient` will drop in without breaking changes.

### Async-First Design

The TypeScript SDK is built with modern async/await patterns:

```
// All methods return Promises
const mandate = await user.createMandate(mandateData);
const token = await user.requestCardRevealToken(mandate.mandateId);
const card = await user.revealCardDetails(token.revealToken);
```

## What’s Next?

* [Usage Guide](usage-guide.md) — Learn the complete payment flow step-by-step
* [Configuration](Configuration.md) — Customize the SDK for your production environment
