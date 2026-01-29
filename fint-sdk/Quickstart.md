# Quickstart

Complete your first end-to-end payment flow: collect a card on the frontend, reveal it on the backend.

**What You’ll Learn**\n\nIn this guide, you’ll:

* Install frontend and backend SDKs
* Collect a payment method with `FintWallet`
* Retrieve card details securely on your backend
* Understand key concepts (userId, mandate, reveal token)

**Time to complete:** 5 minutes

## Install

* Frontend (React)
* Backend (Python)
* Backend (TypeScript)

```
npm install @fint/wallet
```

```
pip install fint
```

```
npm install @fint/fint-js
```

## Get API Keys

1. Sign up at [app.fint.io](https://app.fint.io)
2. Generate your keys:
   * **Public key** (`pk_test_...`) - for frontend card collection
   * **Secret key** (`sk_test_...`) - for backend card reveal

```
# Backend only - never expose this in frontend
export FINT_API_KEY="sk_test_..."
```

## Frontend: Collect Card

Add the wallet component where users manage payment methods (e.g., settings page):

```
import { WalletProvider, FintWallet } from '@fint/wallet';

function UserSettings() {
  const userId = currentUser.id; // Your user's ID

  return (
    <WalletProvider publicKey="pk_test_..." userId={userId}>
      <FintWallet />
    </WalletProvider>
  );
}
```\n\n**What this does:**

* Users can add/manage payment methods
* Cards are tokenized and stored securely
* Linked to the `userId` you provide

## Backend: Reveal Card

When your AI agent needs to make a purchase, retrieve the card details:

* Python
* TypeScript

```
from fint import FintClient, MandateData

# Initialize client (reads FINT_API_KEY from env)
client = FintClient.from_env()
user = client.user("user_123")  # Same userId as frontend

# 1. Create mandate (user's intent to purchase)
mandate_response = user.create_mandate(MandateData(
    product="Wireless Headphones",
    price=99.99,
    currency="USD",
    merchant="BestBuy"
))

# 2. Request reveal token
reveal_response = user.request_card_reveal_token(
    mandate_response.mandate_id
)

# 3. Reveal card details
card = user.reveal_card_details(reveal_response.reveal_token)

# 4. Your AI agent now has:
print(f"Card: {card.card_number}")
print(f"Expiry: {card.card_expiry_date}")
print(f"CVV: {card.cvv}")  # Valid for 60 minutes
print(f"Name: {card.cardholder_name}")
```

```
import { FintClient, MandateData } from '@fint/fint-js';

// Initialize client (reads FINT_API_KEY from env)
const client = FintClient.fromEnv();
const user = client.user('user_123'); // Same userId as frontend

// 1. Create mandate (user's intent to purchase)
const mandateResponse = await user.createMandate(new MandateData({
  product: 'Wireless Headphones',
  price: 99.99,
  currency: 'USD',
  merchant: 'BestBuy'
}));

// 2. Request reveal token
const revealResponse = await user.requestCardRevealToken(
  mandateResponse.mandateId
);

// 3. Reveal card details
const card = await user.revealCardDetails(revealResponse.revealToken);

// 4. Your AI agent now has:
console.log(`Card: ${card.cardNumber}`);
console.log(`Expiry: ${card.cardExpiryDate}`);
console.log(`CVV: ${card.cvv}`); // Valid for 60 minutes
console.log(`Name: ${card.cardholderName}`);
```

**What this does:**

* Creates a mandate (proof of user’s purchase intent)
* Generates a short-lived reveal token
* Retrieves the actual card details
* Your AI agent can now fill merchant checkout forms

**Important:** Each purchase requires a new mandate and reveal token. You cannot reuse tokens across purchases.

## Complete Flow

## Key Concepts

### userId

Links frontend and backend operations. Use your own user identifier (e.g., database user ID). Must be consistent across frontend and backend.

### Mandate

Records the user’s intent to purchase. Required before revealing card details. Contains product info, price, and merchant.

### Reveal Token

Short-lived, single-use token that authorizes card reveal. Generated per mandate.

### CVV Expiration

CVVs are valid for 60 minutes after collection. If expired, prompt user to re-enter using `FintCvvCollector`. See [CVV Management](../frontend/wallet/cvv-management.md).

## Next Steps

- [System Overview](../system-overview.md) — Understand how Fint works end-to-end
- [Payment Flow](../payment-flow.md) — Detailed walkthrough of the complete payment flow
- [Wallet Component](../frontend/wallet/overview.md) — Customize the wallet UI and behavior
- [Backend SDK](getting-started.md) — Explore advanced backend SDK features
