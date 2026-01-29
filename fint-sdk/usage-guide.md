# Usage Guide

This guide walks you through the typical payment flow lifecycle with **type-safe responses** at every step using the Fint SDK.

## Overview

The Fint payment flow for backend processing consists of these main steps:

1

Initialize Client

Set up the `FintClient` with your API key.

2

Create User Context

Obtain a `UserContext` by providing a unique `user_id` for your end-user.

3

Create Mandate

Describe the purchase intent by creating a `MandateData` object. This action
returns a `mandate_id`.

4

Request Reveal Token

Use the `mandate_id` to get a short-lived, single-use token to access card
details.

5

Reveal Card Details

Exchange the token for actual card information to complete the purchase
(e.g., to complete the purchase).\n\n**Important Workflow**: A `user_id` is **required** to create a user context.
A `MandateData` object **must be created and submitted** to the API via
`user.create_mandate()` to obtain a `mandate_id`. This `mandate_id` is then **required** to request a `reveal_token`.

## Complete Example

Here’s a full working example demonstrating the complete payment flow with the Fint SDK:

* Python
* TypeScript

payment\_flow.py

```
from fint import MandateData, FintClient, FintError
import os

# Initialize client - uses FINT_API_KEY from environment by default.
# Default base_url is https://api.fint.io
client = FintClient.from_env()

# Or with explicit config (not needed if FINT_API_KEY is set):
# client = FintClient(
#     api_key="sk_live_your_api_key",
#     # base_url="https://api.fint.io", # Default, no need to specify for production
#     timeout=30,
#     max_retries=3
# )

# 1️⃣ Provide a unique user_id for your end-user.
user_id = "user_integration_test_123"
user = client.user(user_id)

try:
    # 2️⃣ Create a mandate (describes the purchase intent)
    mandate = MandateData(
        product="Premium Gold Subscription",
        price=99.99,
        currency="USD",
        merchant="Fint Demo Store",
        merchant_link="https://app.fint.io/demostore",
        product_description="Monthly access to all gold features"
    )

    # The user_id (user_integration_test_123) is implicitly passed.
    mandate_response = user.create_mandate(mandate)

    # Type-safe access to all fields!
    print(f"✅ Mandate Created: {mandate_response.mandate_id} for user: {user_id}")
    print(f"   Request ID: {mandate_response.request_id}")
    print(f"   Created At: {mandate_response.created_at}")

    # 3️⃣ Request reveal token using the mandate_id from the previous step.
    reveal_response = user.request_card_reveal_token(
        mandate_id=mandate_response.mandate_id  # Can use int or string
    )

    print(f"🔑 Reveal Token Generated: {reveal_response.token[:20]}...")
    print(f"   API Path for Reveal: {reveal_response.reveal_path}")

    # Check expiration if available
    if reveal_response.expires_at:
        print(f"   Token expires at: {reveal_response.expires_at}")

    # 4️⃣ Reveal card details using the single-use reveal_token.
    # The user_id is also implicitly passed here.
    card = user.reveal_card_details(reveal_response.token)

    # All fields are typed and validated!
    print(f"💳 Card Revealed: **** ** ** ****{card.card_number[-4:]}")
    print(f"   Expiry: {card.card_expiry_date}")  # Guaranteed MM/YY format
    print(f"   Name: {card.cardholder_name}")

    # Optional fields are properly typed
    if card.email:
        print(f"   Email: {card.email}")
    if card.billing_address:
        print(f"   Address: {card.billing_address}")

    print("🎉 Successfully completed the card reveal flow!")

except FintError as e:
    # Structured error handling
    print(f"❌ An error occurred: {e}")
    if hasattr(e, 'status_code'):
        print(f"   HTTP Status: {e.status_code}")
    if hasattr(e, 'code'):
        print(f"   Error Code: {e.code}")
    # For more details on error handling, see the Errors guide.
```

payment\_flow.ts

```
import { FintClient, MandateData, FintError } from '@fint/fint-js';

async function paymentFlow() {
  // Initialize client with automatic URL normalization
  const client = FintClient.fromEnv(); // Uses FINT_API_KEY env var
  // Or with explicit config:
  // const client = new FintClient('sk_live_...', {
  //   baseUrl: 'api.fint.io',  // No need for https:// prefix!
  //   timeout: 30000,
  //   maxRetries: 5
  // });

  const user = client.user('user_integration_test_123');

  try {
    // 1️⃣ Create a mandate (returns MandateCreateResponse)
    const mandate = new MandateData({
      product: 'Premium Gold Subscription',
      price: 99.99,
      currency: 'USD',
      merchant: 'Fint Demo Store',
      merchantLink: 'https://app.fint.io/demostore',
      productDescription: 'Monthly access to all gold features'
    });

    const mandateResponse = await user.createMandate(mandate);

    // Type-safe access to all fields!
    console.log(`✅ Mandate Created: ${mandateResponse.mandateId} for user: user_integration_test_123`);
    console.log(`   Request ID: ${mandateResponse.requestId}`);
    console.log(`   Created at: ${mandateResponse.createdAt}`);

    // 2️⃣ Request reveal token (returns CardRevealTokenResponse)
    const revealResponse = await user.requestCardRevealToken(
      mandateResponse.mandateId // Can use number or string
    );

    console.log(`🔑 Reveal Token Generated: ${revealResponse.revealToken.slice(0, 20)}...`);

    // Check expiration if available
    if (revealResponse.expiresAt) {
      console.log(`   Token expires at: ${revealResponse.expiresAt}`);
    }

    // 3️⃣ Reveal card details (returns CardDetailsResponse)
    const card = await user.revealCardDetails(revealResponse.revealToken);

    // All fields are typed and validated!
    console.log(`💳 Card Revealed:** ** **** ** ** ${card.cardNumber.slice(-4)}`);
    console.log(`   Expiry: ${card.cardExpiryDate}`); // Guaranteed MM/YY format
    console.log(`   Name: ${card.cardholderName}`);

    // Optional fields are properly typed
    if (card.email) {
      console.log(`   Email: ${card.email}`);
    }
    if (card.billingAddress) {
      console.log(`   Address: ${card.billingAddress}`);
    }

    console.log('🎉 Successfully completed the card reveal flow!');

  } catch (error) {
    if (error instanceof FintError) {
      // Structured error handling
      console.log(`❌ An error occurred: ${error.message}`);
      if ('statusCode' in error) {
        console.log(`   HTTP Status: ${(error as any).statusCode}`);
      }
      if ('code' in error) {
        console.log(`   Error Code: ${(error as any).code}`);
      }
    } else {
      console.log(`❌ Unexpected error: ${error}`);
    }
  }
}

paymentFlow().catch(console.error);
```

## Response Models

All API methods return strongly-typed response models:

* Python
* TypeScript

MandateCreateResponse

```
class MandateCreateResponse:
    mandate_id: int           # Unique mandate identifier
    request_id: str          # Idempotency key
    customer_id: str         # This is the user_id you provided
    created_at: datetime     # Creation timestamp
    updated_at: datetime?    # Last update (optional)
```

CardRevealTokenResponse

```
class CardRevealTokenResponse:
    reveal_token: str        # One-time use token
    reveal_path: str         # API endpoint for reveal
    expires_at: datetime?    # Token expiration (optional)
```

CardDetailsResponse

```
class CardDetailsResponse:
    card_number: str         # Full card number (validated)
    card_expiry_date: str    # MM/YY format (validated)
    cardholder_name: str     # Name on card
    last4_digits: str?       # Last 4 digits (optional)
    email: str?              # Associated email (optional)
    billing_address: str?    # Billing address (optional)
    zip_code: str?           # ZIP code (optional)
    phone_number: str?       # Phone number (optional)
```

MandateCreateResponse

```
interface MandateCreateResponse {
  mandateId: number;       // Unique mandate identifier
  requestId: string;       // Idempotency key
  customerId: string;      // Customer identifier
  createdAt: Date;         // Creation timestamp
  updatedAt?: Date;        // Last update (optional)
}
```

CardRevealTokenResponse

```
interface CardRevealTokenResponse {
  revealToken: string;     // One-time use token
  expiresAt?: Date;        // Token expiration (optional)
}
```

CardDetailsResponse

```
interface CardDetailsResponse {
  cardNumber: string;         // Full card number (validated)
  cardExpiryDate: string;     // MM/YY format (validated)
  cardholderName: string;     // Name on card
  last4Digits?: string;       // Last 4 digits (optional)
  email?: string;             // Associated email (optional)
  billingAddress?: string;    // Billing address (optional)
  zipCode?: string;           // ZIP code (optional)
  phoneNumber?: string;       // Phone number (optional)
}
```

## Benefits of Typed Responses

Your IDE knows exactly what fields are available:

* Python
* TypeScript

```
from fint import FintClient
client = FintClient.from_env()
user = client.user("some_user_id")
# Assume mandate_id is obtained
reveal_response = user.request_card_reveal_token(mandate_id=123)
reveal_response.  # IDE shows: reveal_token, reveal_path, expires_at
```

```
import { FintClient } from '@fint/fint-js';
const client = FintClient.fromEnv();
const user = client.user('some_user_id');
// Your IDE knows all available fields
const revealResponse = await user.requestCardRevealToken(123);
revealResponse. // IDE shows: revealToken, expiresAt
```

### 2. Type Safety 🛡️

* Python
* TypeScript

```
# reveal_response = user.request_card_reveal_token(mandate_id=123)
# token = reveal_response.token  # AttributeError: no 'token' field, it's 'reveal_token'
```

```
// const revealResponse = await user.requestCardRevealToken(123);
// const token = revealResponse.token;        // Property 'token' does not exist
```

### 3. Built-in Validation ✅

* Python
* TypeScript

```
# Card details are automatically validated by the Fint SDK
# card = user.reveal_card_details(reveal_token="...")
# card.card_expiry_date is guaranteed to be in MM/YY format
# card.card_number is validated to be 13-19 digits
```

```
// Card details are automatically validated
// const card = await user.revealCardDetails(token);
// card.cardExpiryDate is guaranteed to be in MM/YY format
// card.cardNumber is validated to be 13-19 digits
```

### 4. Better Error Messages 📝

If the API returns invalid data, you get clear, actionable error messages:“Response validation failed for CardDetailsResponse: card\_expiry\_date: Card expiry must be in MM/YY format”

## Advanced Features

### URL Normalization

The SDK automatically normalizes URLs. The default base URL is `https://api.fint.io`.

* Python
* TypeScript

```
from fint import FintClient
# Uses https://api.fint.io by default
client = FintClient(api_key="sk_live_...")
```

```
import { FintClient } from '@fint/fint-js';
// All of these work the same:
new FintClient('sk_...', { baseUrl: 'api.fint.io' });
new FintClient('sk_...', { baseUrl: 'https://api.fint.io' });
new FintClient('sk_...', { baseUrl: 'https://api.fint.io/' });
```

### Response Validation

Automatic Response Validation

The SDK validates all API responses and detects:

* HTML error pages (nginx errors, gateway timeouts)
* Invalid JSON structure
* Missing required fields
* Invalid field formats (card numbers, expiry dates)

### Flexible Mandate IDs

* Python
* TypeScript

```
# Both work - SDK converts to string internally if needed
# reveal_response = user.request_card_reveal_token(mandate_id=123)
# reveal_response = user.request_card_reveal_token(mandate_id="123")
```

```
// Both work - SDK converts to string internally
// const revealResponse = await user.requestCardRevealToken(123);
// const revealResponse = await user.requestCardRevealToken('123');
```

## Production Considerations

### Error Handling

Always wrap API calls in try-catch blocks. Refer to the [Error Handling](Errors.md) guide for details.

* Python
* TypeScript

```
from fint import FintError
# try:
#     card = user.reveal_card_details(token)
#     # Process payment with card details
# except FintError as e:
#     # Log error and handle gracefully
#     logger.error(f"Payment failed: {e}")
#     # Return error response to user
```

```
import { FintError } from '@fint/fint-js';
// try {
//     const card = await user.revealCardDetails(token);
//     // Process payment with card details
// } catch (error) {
//     if (error instanceof FintError) {
//         // Log error and handle gracefully
//         console.error(`Payment failed: ${error.message}`);
//         // Return error response to user
//     }
// }
```

### Token Security

Reveal tokens (`reveal_token`) are single-use and time-limited. Store them
securely if necessary, but ideally, use them immediately after generation.

### Rate Limiting

The SDK automatically handles rate limiting with exponential backoff based on `max_retries`. For very high-volume applications, monitor API usage and consider if additional client-side rate limiting logic is beneficial.

## What’s Next?

- [Error Handling](Errors.md) — Build resilient applications with proper error handling
- [Configuration](Configuration.md) — Configure advanced settings for your environment
- [API Reference](api-reference.md) — Complete method documentation and examples
