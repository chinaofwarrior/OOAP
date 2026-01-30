# API Reference

Complete reference for all classes, methods, and response models in the Fint SDKs.

## FintClient

The main client for interacting with the Fint API. It should be instantiated once and reused.
It uses `https://api.fint.io` as the default `base_url`.

### Constructor

* Python
* TypeScript

```
from fint import FintClient

client = FintClient(
    api_key="sk_live_your_api_key",  # Replace with your actual secret API key
    # base_url="https://api.fint.io",  # Default, usually not needed
    timeout=30,  # Optional: request timeout in seconds
    max_retries=3,  # Optional: max retries for retryable errors (429, 5xx)
    backoff_factor=0.5,  # Optional: backoff factor for retries
)
```

```
import { FintClient } from '@fint/fint-js';

const client = new FintClient(
    "sk_live_your_api_key",  // Replace with your actual secret API key
    {
        baseUrl: "https://api.fint.io",  // Default, usually not needed
        timeout: 30000,  // Optional: request timeout in milliseconds
        maxRetries: 3,  // Optional: max retries for retryable errors (429, 5xx)
        backoffFactor: 0.5,  // Optional: backoff factor for retries
    }
);
```

* Python
* TypeScript

#### Python Parameters

[​](#param-api-key)

**api_key**

Type: `string`  
Required  
Your Fint Secret API key (starts with `sk_live_` or `sk_test_`). Must be provided either directly or via the `FINT_API_KEY` environment variable.

[​](#param-base-url)

**base_url**

Type: `string`  
Default: `https://api.fint.io`  
The base URL for the Fint API. Defaults to production. Only change this for staging/testing (e.g., `https://staging-api.fint.io`) or if using a mock server. The SDK normalizes this URL.

[​](#param-timeout)

**timeout**

Type: `int`  
Default: `30`  
Request timeout in seconds for HTTP calls.

[​](#param-max-retries)

**max_retries**

Type: `int`  
Default: `3`  
Maximum number of retry attempts for retryable errors (HTTP 429, 5xx).

[​](#param-backoff-factor)

**backoff_factor**

Type: `float`  
Default: `0.5`  
Multiplier for exponential backoff between retries. `sleep = (2 ** (retry_attempt - 1)) * backoff_factor`.

#### TypeScript Parameters

[​](#param-api-key)

**apiKey**

Type: `string`  
Required  
Your Fint Secret API key (starts with `sk_live_` or `sk_test_`). Must be provided either directly or via the `FINT_API_KEY` environment variable.

[​](#param-base-url)

**baseUrl**

Type: `string`  
Default: `https://api.fint.io`  
The base URL for the Fint API. Defaults to production. Only change this for staging/testing (e.g., `https://staging-api.fint.io`) or if using a mock server. The SDK normalizes this URL.

[​](#param-timeout-1)

**timeout**

Type: `number`  
Default: `30000`  
Request timeout in milliseconds for HTTP calls.

[​](#param-max-retries)

**maxRetries**

Type: `number`  
Default: `3`  
Maximum number of retry attempts for retryable errors (HTTP 429, 5xx).

[​](#param-backoff-factor)

**backoffFactor**

Type: `number`  
Default: `0.5`  
Multiplier for exponential backoff between retries. `sleep = (2 ** (retryAttempt - 1)) * backoffFactor`.

### Class Methods

## from\_env() / fromEnv()

Factory method to create a client instance configured from environment variables.

* Python
* TypeScript

```
from fint import FintClient

# Reads FINT_API_KEY for the API key.
# Reads FINT_BASE_URL (optional) for the base URL, defaults to https://api.fint.io.
# Allows overriding other client parameters too.
client = FintClient.from_env(
    # api_key_var="CUSTOM_API_KEY_ENV_VAR_NAME", # Default: "FINT_API_KEY"
    # base_url_var="CUSTOM_BASE_URL_ENV_VAR_NAME", # Default: "FINT_BASE_URL"
    timeout=45 # Example: override default timeout
)
```

```
import { FintClient } from '@fint/fint-js';

// Reads FINT_API_KEY for the API key.
// Reads FINT_BASE_URL (optional) for the base URL, defaults to https://api.fint.io.
// Allows overriding other client parameters too.
const client = FintClient.fromEnv({
    timeout: 45000 // Example: override default timeout in ms
});
```

This is the recommended way to initialize the client for most applications.

### Instance Methods

user(userId) -> UserContext

Creates a `UserContext` for a specific user. This context automatically includes the user ID in subsequent API calls made through it. **A user ID is a mandatory string that uniquely identifies your end-user.**

* Python
* TypeScript

```
from fint import FintClient

client = FintClient.from_env()
user_identifier = "unique_user_abc_123"
user_context = client.user(user_identifier)

# Now use methods on user_context:
# mandate_response = user_context.create_mandate(...)
# reveal_token_response = user_context.request_card_reveal_token(...)
# card_details = user_context.reveal_card_details(...)
```

```
import { FintClient } from '@fint/fint-js';

const client = FintClient.fromEnv();
const userIdentifier = "unique_user_abc_123";
const userContext = client.user(userIdentifier);

// Now use methods on userContext:
// const mandateResponse = await userContext.createMandate(...);
// const revealTokenResponse = await userContext.requestCardRevealToken(...);
// const cardDetails = await userContext.revealCardDetails(...);
```

Using `UserContext` is preferred over passing user ID to each client method directly.

createMandate / create\_mandate

*Note: It is recommended to use `userContext.createMandate(mandateData)` instead.*Creates a purchase mandate (intent to buy) for a given user. This is a required first step before a card reveal token can be requested.

* Python
* TypeScript

```
from fint import FintClient, MandateData

client = FintClient.from_env()
user_identifier = "user_for_mandate_creation"

mandate_info = MandateData(
    product="Deluxe Widget",
    price=199.99,
    currency="USD",
    merchant="My Test Shop"
)

# Optional idempotency key for safe retries of this specific request
# custom_request_id = "my_unique_mandate_request_001"

try:
    response = client.create_mandate(
        user_id=user_identifier,
        mandate_data=mandate_info,
        # request_id=custom_request_id
    )
    print(f"Mandate Created: {response.mandate_id} for user: {user_identifier}")
    # The response.mandate_id is then used for request_card_reveal_token
except FintError as e:
    print(f"Error creating mandate: {e}")
```

```
import { FintClient, MandateData } from '@fint/fint-js';

const client = FintClient.fromEnv();
const userIdentifier = "user_for_mandate_creation";

const mandateInfo = new MandateData({
    product: "Deluxe Widget",
    price: 199.99,
    currency: "USD",
    merchant: "My Test Shop"
});

try {
    const response = await client.createMandate(
        userIdentifier,
        mandateInfo
    );
    console.log(`Mandate Created: ${response.mandateId} for user: ${userIdentifier}`);
    // The response.mandateId is then used for requestCardRevealToken
} catch (error) {
    if (error instanceof FintError) {
        console.log(`Error creating mandate: ${error}`);
    }
}
```

requestCardRevealToken / request\_card\_reveal\_token

*Note: It is recommended to use `userContext.requestCardRevealToken(mandateId)` instead.*Requests a one-time, short-lived token to reveal card details for a specific mandate. **A mandate must have been successfully created first to obtain a mandate ID.**

* Python
* TypeScript

```
from fint import FintClient

client = FintClient.from_env()
user_identifier = "user_for_token_request"
existing_mandate_id = 12345 # Obtained from a previous create_mandate call

try:
    response = client.request_card_reveal_token(
        user_id=user_identifier,
        mandate_id=existing_mandate_id
    )
    print(f"Reveal Token: {response.token} for user: {user_identifier}")
    # This response.token is then used for reveal_card_details
except FintError as e:
    print(f"Error requesting reveal token: {e}")
```

```
import { FintClient } from '@fint/fint-js';

const client = FintClient.fromEnv();
const userIdentifier = "user_for_token_request";
const existingMandateId = 12345; // Obtained from a previous createMandate call

try {
    const response = await client.requestCardRevealToken(
        userIdentifier,
        existingMandateId
    );
    console.log(`Reveal Token: ${response.revealToken} for user: ${userIdentifier}`);
    // This response.revealToken is then used for revealCardDetails
} catch (error) {
    if (error instanceof FintError) {
        console.log(`Error requesting reveal token: ${error}`);
    }
}
```

revealCardDetails / reveal\_card\_details

*Note: It is recommended to use `userContext.revealCardDetails(revealToken)` instead.*Reveals actual card details using a valid reveal token.

* Python
* TypeScript

```
from fint import FintClient

client = FintClient.from_env()
user_identifier = "user_for_card_reveal"
valid_reveal_token = "rvl_tok_from_previous_step"

try:
    card = client.reveal_card_details(
        user_id=user_identifier,
        reveal_token=valid_reveal_token
    )
    print(f"Card Number (last 4): {card.card_number[-4:]} for user: {user_identifier}")
    print(f"Card Expiry: {card.card_expiry_date}")
except FintError as e:
    print(f"Error revealing card details: {e}")
```

```
import { FintClient } from '@fint/fint-js';

const client = FintClient.fromEnv();
const userIdentifier = "user_for_card_reveal";
const validRevealToken = "rvl_tok_from_previous_step";

try {
    const card = await client.revealCardDetails(
        userIdentifier,
        validRevealToken
    );
    console.log(`Card Number (last 4): ${card.cardNumber.slice(-4)} for user: ${userIdentifier}`);
    console.log(`Card Expiry: ${card.cardExpiryDate}`);
} catch (error) {
    if (error instanceof FintError) {
        console.log(`Error revealing card details: ${error}`);
    }
}
```

## UserContext

A convenience wrapper returned by `client.user(userId)` that automatically includes the user ID in all its API calls. **This is the recommended way to interact with user-specific endpoints.**

* Python
* TypeScript

```
from fint import FintClient, MandateData

client = FintClient.from_env()
user_context = client.user("unique_user_id_789")

# Example mandate creation using UserContext
mandate_details = MandateData(
    product="Super Plan", price=29.00, currency="EUR", merchant="My Service"
)
try:
    mandate_response = user_context.create_mandate(mandate_details)
    print(f"Mandate ID from UserContext: {mandate_response.mandate_id}")

    # Request reveal token using UserContext and the new mandate_id
    reveal_token_response = user_context.request_card_reveal_token(mandate_response.mandate_id)
    print(f"Reveal Token from UserContext: {reveal_token_response.token[:10]}...")

    # Reveal card details using UserContext and the new token
    card_object = user_context.reveal_card_details(reveal_token_response.token)
    print(f"Cardholder via UserContext: {card_object.cardholder_name}")
except FintError as e:
    print(f"UserContext operation failed: {e}")
```

The `UserContext` object has the following methods:

* `create_mandate(mandate_data: MandateData, request_id: Optional[str] = None) -> MandateCreateResponse`
* `request_card_reveal_token(mandate_id: Union[str, int]) -> CardRevealTokenResponse`
* `reveal_card_details(reveal_token: str) -> CardDetailsResponse`

```
import { FintClient, MandateData, FintError } from '@fint/fint-js';

const client = FintClient.fromEnv();
const userContext = client.user("unique_user_id_789");

// Example mandate creation using UserContext
const mandateDetails = new MandateData({
    product: "Super Plan", 
    price: 29.00, 
    currency: "EUR", 
    merchant: "My Service"
});

try {
    const mandateResponse = await userContext.createMandate(mandateDetails);
    console.log(`Mandate ID from UserContext: ${mandateResponse.mandateId}`);

    // Request reveal token using UserContext and the new mandateId
    const revealTokenResponse = await userContext.requestCardRevealToken(mandateResponse.mandateId);
    console.log(`Reveal Token from UserContext: ${revealTokenResponse.revealToken.slice(0, 10)}...`);

    // Reveal card details using UserContext and the new token
    const cardObject = await userContext.revealCardDetails(revealTokenResponse.revealToken);
    console.log(`Cardholder via UserContext: ${cardObject.cardholderName}`);
} catch (error) {
    if (error instanceof FintError) {
        console.log(`UserContext operation failed: ${error}`);
    }
}
```

The `UserContext` object has the following methods:

* `createMandate(mandateData: MandateData): Promise<MandateCreateResponse>`
* `requestCardRevealToken(mandateId: string | number): Promise<CardRevealTokenResponse>`
* `revealCardDetails(revealToken: string): Promise<CardDetailsResponse>`

## Data Models

### MandateData

Represents the user’s intent to purchase. This data is sent when creating a mandate.

* Python
* TypeScript

```
from fint import MandateData, FintValidationError

try:
    mandate = MandateData(
        # Required fields
        product="Premium Subscription",     # Name of the product/service
        price=49.99,                       # Price (must be > 0)
        currency="USD",                    # 3-letter ISO currency code

        # Optional fields
        merchant="Your Company LLC",       # Your merchant name displayed to user
        merchant_link="https://yourcompany.com/premium", # Link to product/merchant
        product_description="Monthly access to all premium features and support.",
        confidence_score=0.95,             # Your system's confidence (0.0 to 1.0) that this is a legitimate user intent
        # request_id: Optional[str] = None # Auto-generated UUID if not provided for create_mandate idempotency
    )
except FintValidationError as e:
    print(f"Invalid MandateData: {e}")
```

```
import { MandateData, FintValidationError } from '@fint/fint-js';

try {
    const mandate = new MandateData({
        // Required fields
        product: "Premium Subscription",     // Name of the product/service
        price: 49.99,                       // Price (must be > 0)
        currency: "USD",                    // 3-letter ISO currency code

        // Optional fields
        merchant: "Your Company LLC",       // Your merchant name displayed to user
        merchantLink: "https://yourcompany.com/premium", // Link to product/merchant
        productDescription: "Monthly access to all premium features and support.",
        confidenceScore: 0.95,             // Your system's confidence (0.0 to 1.0) that this is a legitimate user intent
        requestId: "optional-idempotency-key" // Auto-generated UUID if not provided
    });
} catch (error) {
    if (error instanceof FintValidationError) {
        console.log(`Invalid MandateData: ${error}`);
    }
}
```

* Python
* TypeScript

#### Python Parameters

[​](#param-product)

**product**

Type: `string`  
Required  
Name of the product or service being purchased.

[​](#param-price)

**price**

Type: `float`  
Required  
Price of the product. Must be a positive number.

[​](#param-currency)

**currency**

Type: `string`  
Required  
3-letter ISO currency code (e.g., “USD”, “EUR”).

[​](#param-merchant)

**merchant**

Type: `string`  
Name of the merchant or store.

[​](#param-merchant-link)

**merchant_link**

Type: `string`  
URL related to the merchant or product.

[​](#param-product-description)

**product_description**

Type: `string`  
A more detailed description of the product or service.

[​](#param-confidence-score)

**confidence_score**

Type: `float`  
A score (0.0 to 1.0) indicating your system’s confidence in this purchase intent.

[​](#param-request-id)

**request_id**

Type: `Optional[str]`  
An optional idempotency key for the `create_mandate` call. If not provided, the SDK generates one.

#### TypeScript Parameters

[​](#param-product-1)

**product**

Type: `string`  
Required  
Name of the product or service being purchased.

[​](#param-price-1)

**price**

Type: `number`  
Required  
Price of the product. Must be a positive number.

[​](#param-currency-1)

**currency**

Type: `string`  
Required  
3-letter ISO currency code (e.g., “USD”, “EUR”).

[​](#param-merchant-1)

**merchant**

Type: `string`  
Name of the merchant or store.

[​](#param-merchant-link)

**merchantLink**

Type: `string`  
URL related to the merchant or product.

[​](#param-product-description)

**productDescription**

Type: `string`  
A more detailed description of the product or service.

[​](#param-confidence-score)

**confidenceScore**

Type: `number`  
A score (0.0 to 1.0) indicating your system’s confidence in this purchase intent.

[​](#param-request-id)

**requestId**

Type: `string`  
An optional idempotency key. If not provided, the SDK generates one.

## Response Models

All SDK API methods return typed models with automatic validation.

* MandateCreateResponse
* CardRevealTokenResponse
* CardDetailsResponse

Response from mandate creation.

* Python
* TypeScript

```
class MandateCreateResponse:
    mandate_id: int                    # Unique ID for the created mandate
    request_id: str                    # Request tracking ID (idempotency key used or generated)
    customer_id: str                   # The user_id you provided for this mandate
    created_at: datetime               # Timestamp of mandate creation (UTC)
    updated_at: Optional[datetime]     # Timestamp of last update (UTC), if any
```

**Example Usage:**

```
# mandate_resp = user_context.create_mandate(...)
# print(f"New Mandate ID: {mandate_resp.mandate_id}")
# print(f"Associated User (Customer ID): {mandate_resp.customer_id}")
```

```
interface MandateCreateResponse {
    mandateId: number;                 // Unique ID for the created mandate
    requestId: string;                 // Request tracking ID
    customerId: string;                // The userId you provided for this mandate
    createdAt: Date;                   // Timestamp of mandate creation
    updatedAt?: Date;                  // Timestamp of last update, if any
}
```

**Example Usage:**

```
// const mandateResp = await userContext.createMandate(...);
// console.log(`New Mandate ID: ${mandateResp.mandateId}`);
// console.log(`Associated User (Customer ID): ${mandateResp.customerId}`);
```

Response from requesting a card reveal token.

* Python
* TypeScript

```
class CardRevealTokenResponse:
    reveal_token: str                  # The single-use token for revealing card details
    reveal_path: str                   # API endpoint path where this token can be used (for info only)
    expires_at: Optional[datetime]     # Timestamp when this token expires (UTC), if applicable
```

**Example Usage:**

```
# reveal_resp = user_context.request_card_reveal_token(...)
# print(f"Reveal Token obtained: {reveal_resp.token[:15]}...")
# if reveal_resp.expires_at:
#     print(f"Token expires at: {reveal_resp.expires_at}")
```

```
interface CardRevealTokenResponse {
    revealToken: string;               // The single-use token for revealing card details
    expiresAt?: Date;                  // Optional expiration timestamp
}
```

**Example Usage:**

```
// const revealResp = await userContext.requestCardRevealToken(...);
// console.log(`Reveal Token obtained: ${revealResp.revealToken.slice(0, 15)}...`);
// if (revealResp.expiresAt) {
//     console.log(`Token expires at: ${revealResp.expiresAt}`);
// }
```

Response from revealing card details.

* Python
* TypeScript

```
class CardDetailsResponse:
    # Required fields
    card_number: str                   # Full card number (PAN). Validated by SDK to be 13-19 digits.
    card_expiry_date: str              # Expiry date in MM/YY format. Validated by SDK.
    cardholder_name: str               # Name on the card as collected.

    # Optional fields (availability depends on what was collected/stored)
    last4_digits: Optional[str]        # Last 4 digits of the card number.
    email: Optional[str]               # Email address associated with the card/user.
    billing_address: Optional[str]     # Billing address lines.
    zip_code: Optional[str]            # Billing address ZIP or postal code.
    phone_number: Optional[str]        # Phone number associated.
```

**Validation by SDK:**

* `card_number` is validated to be a string of 13-19 digits.
* `card_expiry_date` is validated to be in MM/YY format.

**Example Usage:**

```
# card = user_context.reveal_card_details(...)
# print(f"Retrieved Card:**** ** ** ****{card.card_number[-4:]}")
# print(f"Card Expiry Date: {card.card_expiry_date}")
# print(f"Cardholder's Name: {card.cardholder_name}")
```

```
interface CardDetailsResponse {
    // Required fields
    cardNumber: string;                // Full card number (validated)
    cardExpiryDate: string;           // MM/YY format (validated)
    cardholderName: string;           // Name on card

    // Optional fields
    last4Digits?: string;
    email?: string;
    billingAddress?: string;
    city?: string;
    state?: string;
    zipCode?: string;
    phoneNumber?: string;
}
```

**Validation:**

* Card number must be 13-19 digits
* Expiry date must be MM/YY format

**Example Usage:**

```
// const card = await userContext.revealCardDetails(...);
// console.log(`Retrieved Card:**** ** ** **** ${card.cardNumber.slice(-4)}`);
// console.log(`Card Expiry Date: ${card.cardExpiryDate}`);
// console.log(`Cardholder's Name: ${card.cardholderName}`);
```

## Exceptions

All exceptions raised by the SDKs inherit from a base `FintError` class.
Refer to the [Error Handling guide](Errors.md) for a detailed hierarchy and usage patterns.

### Key Exception Classes

* Python
* TypeScript

* `FintError` (Base class)
* `FintApiError` (Base for API-returned errors)
  + `AuthenticationError` (401 - Invalid API key)
  + `InvalidRequestError` (4xx - e.g., bad parameters, resource not found)
    - `CardNotFoundError` (Specific 404 for card not found)
  + `RateLimitError` (429 - Rate limit exceeded, SDK retries these)
  + `ServerError` (5xx - Server-side issue at Fint, SDK retries these)
* `FintConnectionError` (Network issues like DNS or TCP errors)
* `FintValidationError` (Client-side or response data validation failure against Pydantic models)

* `FintError` (Base class)
* `FintApiError` (Base for API-returned errors)
  + `AuthenticationError` (401 - Invalid API key)
  + `InvalidRequestError` (4xx - e.g., bad parameters, resource not found)
    - `CardNotFoundError` (Specific 404 for card not found)
  + `RateLimitError` (429 - Rate limit exceeded, SDK retries these)
  + `ServerError` (5xx - Server-side issue at Fint, SDK retries these)
* `FintConnectionError` (Network issues like DNS or TCP errors)
* `FintValidationError` (Client-side validation failed)

### Common Exception Attributes

* Python
* TypeScript

[​](#param-message)

message

str

Human-readable error message.

[​](#param-code)

code

Optional[str]

A machine-readable error code string from the API, if available (e.g.,
`invalid_api_key`, `mandate_not_found`).

[​](#param-status-code)

status\_code

Optional[int]

The HTTP status code returned by the API (e.g., 401, 404, 500).

[​](#param-message-1)

message

string

Human-readable error message.

[​](#param-code-1)

code

string

Machine-readable error code.

[​](#param-status-code)

statusCode

number

HTTP status code returned by the API.

## Usage Examples

### Complete Payment Flow (using UserContext - Recommended)

This example shows the end-to-end flow: creating a client, getting a user context, creating a mandate, requesting a reveal token, and revealing card details.

* Python
* TypeScript

```
from fint import FintClient, MandateData, FintError, CardNotFoundError, InvalidRequestError, AuthenticationError, FintValidationError, FintApiError
import os # For environment variables

# Best practice: Initialize client from environment variables
# Ensure FINT_API_KEY is set in your environment.
# FINT_BASE_URL defaults to https://api.fint.io if not set.
client = FintClient.from_env()

# Each of your users must have a unique identifier string.
user_identifier = "example_user_e2e_flow_001"
user = client.user(user_identifier)

try:
    # Step 1: Create a mandate (intent to purchase)
    print(f"Creating mandate for user '{user_identifier}'...")
    mandate_payload = MandateData(
        product="Ultimate Gadget X",
        price=299.99,
        currency="USD",
        merchant="Future Tech Inc.",
        product_description="The latest and greatest gadget with all new features."
    )
    mandate_resp = user.create_mandate(mandate_payload)
    print(f"✅ Mandate created successfully! ID: {mandate_resp.mandate_id}")

    # Step 2: Request a card reveal token using the mandate_id from Step 1
    print(f"Requesting card reveal token for mandate ID '{mandate_resp.mandate_id}'...")
    reveal_token_resp = user.request_card_reveal_token(
        mandate_id=mandate_resp.mandate_id
    )
    print(f"🔑 Reveal token received: {reveal_token_resp.token[:15]}...")

    # Step 3: Reveal the actual card details using the token from Step 2
    print(f"Revealing card details with token...")
    card_details = user.reveal_card_details(reveal_token_resp.token)

    # Now you have the card details to use to complete the purchase
    print(f"💳 Card details revealed for user '{user_identifier}':")
    print(f"   Card Number: **** ** ** ****{card_details.card_number[-4:]}") # Only print last 4 for security
    print(f"   Expiry Date: {card_details.card_expiry_date}")
    print(f"   Cardholder Name: {card_details.cardholder_name}")
    print("🎉 Full flow completed successfully!")

except CardNotFoundError as e:
    print(f"Card Not Found for user '{e.user_id}': {e.message}")
    print("This often means payment details were not collected or user_id mismatch.")
except InvalidRequestError as e:
    print(f"Invalid Request: {e.message} (Code: {e.code}, HTTP Status: {e.status_code})")
    print("Check your parameters, like mandate_id format or if it exists.")
except AuthenticationError as e:
    print(f"Authentication Failed: {e.message}. Check your FINT_API_KEY.")
except FintValidationError as e:
    print(f"Data Validation Error: {e}. This could be an issue with data sent or received.")
except FintApiError as e:
    print(f"Fint API Error: {e.message} (Code: {e.code}, HTTP Status: {e.status_code})")
except FintError as e: # Catch any other Fint SDK-specific errors
    print(f"A Fint SDK error occurred: {e}")
except Exception as e: # Fallback for unexpected errors
    print(f"An unexpected error occurred: {e}")
```

```
import { FintClient, MandateData, FintError, CardNotFoundError, InvalidRequestError, AuthenticationError, FintValidationError, FintApiError } from '@fint/fint-js';

// Best practice: Initialize client from environment variables
// Ensure FINT_API_KEY is set in your environment.
// FINT_BASE_URL defaults to https://api.fint.io if not set.
const client = FintClient.fromEnv();

// Each of your users must have a unique identifier string.
const userIdentifier = "example_user_e2e_flow_001";
const user = client.user(userIdentifier);

(async () => {
  try {
    // Step 1: Create a mandate (intent to purchase)
    console.log(`Creating mandate for user '${userIdentifier}'...`);
    const mandatePayload = new MandateData({
      product: "Ultimate Gadget X",
      price: 299.99,
      currency: "USD",
      merchant: "Future Tech Inc.",
      productDescription: "The latest and greatest gadget with all new features."
    });
    const mandateResp = await user.createMandate(mandatePayload);
    console.log(`✅ Mandate created successfully! ID: ${mandateResp.mandateId}`);

    // Step 2: Request a card reveal token using the mandateId from Step 1
    console.log(`Requesting card reveal token for mandate ID '${mandateResp.mandateId}'...`);
    const revealTokenResp = await user.requestCardRevealToken(mandateResp.mandateId);
    console.log(`🔑 Reveal token received: ${revealTokenResp.revealToken.slice(0, 15)}...`);

    // Step 3: Reveal the actual card details using the token from Step 2
    console.log("Revealing card details with token...");
    const cardDetails = await user.revealCardDetails(revealTokenResp.revealToken);

    // Now you have the card details to use to complete the purchase
    console.log(`💳 Card details revealed for user '${userIdentifier}':`);
    console.log(`   Card Number:** ** **** ** ** ${cardDetails.cardNumber.slice(-4)}`); // Only print last 4 for security
    console.log(`   Expiry Date: ${cardDetails.cardExpiryDate}`);
    console.log(`   Cardholder Name: ${cardDetails.cardholderName}`);
    console.log("🎉 Full flow completed successfully!");

  } catch (error) {
    if (error instanceof CardNotFoundError) {
      console.log(`Card Not Found for user '${error.userId}': ${error.message}`);
      console.log("This often means payment details were not collected or user_id mismatch.");
    } else if (error instanceof InvalidRequestError) {
      console.log(`Invalid Request: ${error.message} (Code: ${error.code}, HTTP Status: ${error.statusCode})`);
      console.log("Check your parameters, like mandateId format or if it exists.");
    } else if (error instanceof AuthenticationError) {
      console.log(`Authentication Failed: ${error.message}. Check your FINT_API_KEY.`);
    } else if (error instanceof FintValidationError) {
      console.log(`Data Validation Error: ${error}. This could be an issue with data sent or received.`);
    } else if (error instanceof FintApiError) {
      console.log(`Fint API Error: ${error.message} (Code: ${error.code}, HTTP Status: ${error.statusCode})`);
    } else if (error instanceof FintError) {
      console.log(`A Fint SDK error occurred: ${error}`);
    } else {
      console.log(`An unexpected error occurred: ${error}`);
    }
  }
})();
```

### Global Default Client Pattern

For simpler scripts or applications where dependency injection is overkill.

* Python
* TypeScript

```
from fint import set_default_client, get_default_client, FintClient, MandateData, FintError

# Set once at startup (e.g., in your main script or app initialization)
set_default_client(FintClient.from_env()) # Configured from environment

def some_business_logic_function(user_id: str, product_details: dict):
    client_instance = get_default_client() # Retrieve the globally set client
    user_context = client_instance.user(user_id)

    mandate_info = MandateData(
        product=product_details["name"],
        price=product_details["price"],
        currency=product_details["currency"],
        merchant="Global Client Store"
    )
    try:
        mandate_response = user_context.create_mandate(mandate_info)
        # ... continue with reveal token and card details ...
        print(f"Mandate {mandate_response.mandate_id} created via global client for {user_id}")
    except FintError as e:
        print(f"Error in business logic with global client: {e}")

# Example call
# some_business_logic_function("user_global_client_test", {"name": "Test Product", "price": 1.00, "currency": "USD"})
```

```
import { setDefaultClient, getDefaultClient, FintClient, MandateData, FintError } from '@fint/fint-js';

// Set once at startup (e.g., in your main script or app initialization)
setDefaultClient(FintClient.fromEnv()); // Configured from environment

async function someBusinessLogicFunction(userId: string, productDetails: any) {
    const clientInstance = getDefaultClient(); // Retrieve the globally set client
    const userContext = clientInstance.user(userId);

    const mandateInfo = new MandateData({
        product: productDetails.name,
        price: productDetails.price,
        currency: productDetails.currency,
        merchant: "Global Client Store"
    });
    
    try {
        const mandateResponse = await userContext.createMandate(mandateInfo);
        // ... continue with reveal token and card details ...
        console.log(`Mandate ${mandateResponse.mandateId} created via global client for ${userId}`);
    } catch (error) {
        if (error instanceof FintError) {
            console.log(`Error in business logic with global client: ${error}`);
        }
    }
}

// Example call
// await someBusinessLogicFunction("user_global_client_test", {name: "Test Product", price: 1.00, currency: "USD"});
```

While convenient, the global client pattern can make it harder to manage
configurations and test components in isolation in larger applications. Use
with discretion.

## What’s Next?
