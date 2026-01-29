# Quickstart

Welcome to the rapid-fire tour of the nekuda SDK. In less than five minutes you will:

1. Install the package
2. Authenticate with your **API key**
3. Run your first *card-reveal* workflow with **type-safe responses**

This SDK handles the backend payment handling. You’ll also need to integrate our [frontend wallet SDK](../frontend/wallet/overview.md) to securely collect credit card details from users.

## Step 1: Installation

* Python
* TypeScript

```
uv pip install nekuda
```

The SDK ships as a single, pure-Python wheel with minimal dependencies – install is ~1 second.

```
npm install @nekuda/nekuda-js
```

The SDK ships as a modern TypeScript package with minimal dependencies and full tree-shaking support.

## Step 2: Authentication

Grab your secret key from the [nekuda customer portal](https://app.nekuda.ai) and export it as an environment variable:

```
export NEKUDA_API_KEY="sk_live_…"  # required

# The SDK defaults to the production API: https://api.nekuda.ai
# For staging or local testing, you can override the base URL:
# export NEKUDA_BASE_URL="https://staging-api.nekuda.ai"
```

That’s *all* the configuration you need for the quickstart.

## Step 3: Hello World

* Python
* TypeScript

hello.py

```
from nekuda import NekudaClient

client = NekudaClient.from_env()
print("🚀 Authenticated! Your account ID is:", client.api_key[:8] + "…")
```

```
python hello.py
```

hello.ts

```
import { NekudaClient } from '@nekuda/nekuda-js';

const client = NekudaClient.fromEnv();
console.log("🚀 Authenticated! Your account ID is:", (client as any).apiKey.slice(0, 8) + "…");
```

```
npx ts-node hello.ts
```

If everything is set up correctly you should see:

```
🚀 Authenticated! Your account ID is: sk_live_12…
```

## Step 4: End-to-End Flow with Type Safety 🎯

The snippet below walks through the **full payment flow** with type-safe responses. This flow requires a `user_id` to associate the payment with a user, and a `mandate_id` which is obtained after creating a mandate (the user’s intent to purchase).

* Python
* TypeScript

quick\_demo.py

```
from nekuda import MandateData, NekudaClient, NekudaError

client = NekudaClient.from_env()

# A unique identifier for your user is required.
user_id = "test_user_123"
user = client.user(user_id)

try:
    # 1) Describe what the user is about to purchase and create a mandate.
    # This step is crucial to get a mandate_id for token requests.
    mandate = MandateData(
        product="Premium Subscription",
        price=49.99,
        currency="USD",
        merchant="nekuda Corp"
    )

    # Create mandate - returns MandateCreateResponse
    # The user_id is implicitly passed via the user object.
    mandate_response = user.create_mandate(mandate)
    print(f"✅ Created mandate: {mandate_response.mandate_id} for user: {user_id}")

    # 2) Request a reveal token using the mandate_id.
    # This token is short-lived and single-use.
    reveal_response = user.request_card_reveal_token(mandate_response.mandate_id)
    print(f"🔑 Token: {reveal_response.token}")

    # IDE knows these fields exist! No more KeyErrors!
    if reveal_response.expires_at:
        print(f"⏰ Expires at: {reveal_response.expires_at}")

    # 3) Exchange token for card details (returns CardDetailsResponse).
    # The user_id is implicitly passed here as well.
    card = user.reveal_card_details(reveal_response.token)
    print(f"💳 **** ** ** ****{card.card_number[-4:]}")
    print(f"📅 Expiry: {card.card_expiry_date}")  # Always MM/YY format
    print(f"👤 Name: {card.cardholder_name}")

except NekudaError as e:
    print(f"❌ Error: {e}")
```

quick\_demo.ts

```
import { NekudaClient, MandateData, NekudaError } from '@nekuda/nekuda-js';

async function main() {
  const client = NekudaClient.fromEnv();
  const user = client.user('test_user_123');

  try {
    // 1) Describe what the user is about to purchase
    const mandate = new MandateData({
      product: 'Premium Subscription',
      price: 49.99,
      currency: 'USD',
      merchant: 'nekuda Corp'
    });

    // Create mandate - returns MandateCreateResponse
    const mandateResponse = await user.createMandate(mandate);
    console.log(`✅ Created mandate: ${mandateResponse.mandateId}`);

    // 2) Request a reveal token - returns CardRevealTokenResponse
    const revealResponse = await user.requestCardRevealToken(mandateResponse.mandateId);
    console.log(`🔑 Token: ${revealResponse.revealToken}`);

    // TypeScript knows these fields exist! No more undefined errors!
    if (revealResponse.expiresAt) {
      console.log(`⏰ Expires at: ${revealResponse.expiresAt}`);
    }

    // 3) Exchange token for card details - returns CardDetailsResponse
    const card = await user.revealCardDetails(revealResponse.revealToken);
    console.log(`💳** ** **** ** **${card.cardNumber.slice(-4)}`);
    console.log(`📅 Expiry: ${card.cardExpiryDate}`); // Always MM/YY format
    console.log(`👤 Name: ${card.cardholderName}`);

  } catch (error) {
    if (error instanceof NekudaError) {
      console.log(`❌ Error: ${error.message}`);
    } else {
      console.log(`❌ Unexpected error: ${error}`);
    }
  }
}

main().catch(console.error);
```

Run it and you’ll see the card details with full type safety and IDE autocomplete support!**Complete Integration:** Remember that in a real application, creating a mandate and requesting a token happen on your backend (using this SDK), while the actual card collection happens on your frontend using our [React wallet SDK](../frontend/wallet/overview.md). A `user_id` must be consistently used for both frontend and backend operations for a given user.

## Step 5: Why Type Safety Matters 🛡️

With our typed response models:

* **No more runtime errors** - IDE knows exactly what fields are available
* **Autocomplete everywhere** - Your editor suggests available fields and methods
* **Validation built-in** - Card numbers and expiry dates are validated
* **Better error messages** - Know exactly what went wrong at compile time (TypeScript) or runtime (Python)

* Python
* TypeScript

```
result = client.request_card_reveal_token(user_id="user_123", mandate_id="mand_abc") # user_id passed manually
token = result["reveal_token"]  # Hope the key exists!
```

```
const result = await client.requestCardRevealToken(...);
const token = result. token; // Hope the property exists!
```

## What’s Next?

[## Core Concepts

Understand NekudaClient, UserContext, and response models](core-concepts.md)[## Usage Guide

Deep dive into the complete payment flow](usage-guide.md)[## Configuration

Production-ready settings and customization](Configuration.md)[## Error Handling

Build resilient applications with proper error handling](Errors.md)

Happy hacking! 🎉
