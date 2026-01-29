# Quickstart

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Get Started

Quickstart

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

* [Install](#install)
* [Get API Keys](#get-api-keys)
* [Frontend: Collect Card](#frontend%3A-collect-card)
* [Backend: Reveal Card](#backend%3A-reveal-card)
* [Complete Flow](#complete-flow)
* [Key Concepts](#key-concepts)
* [userId](#userid)
* [Mandate](#mandate)
* [Reveal Token](#reveal-token)
* [CVV Expiration](#cvv-expiration)
* [Next Steps](#next-steps)

Get Started

# Quickstart

Copy page

Get started with nekuda in under 5 minutes

Copy page

Complete your first end-to-end payment flow: collect a card on the frontend, reveal it on the backend.

**What You’ll Learn**In this guide, you’ll:

* Install frontend and backend SDKs
* Collect a payment method with `NekudaWallet`
* Retrieve card details securely on your backend
* Understand key concepts (userId, mandate, reveal token)

**Time to complete:** 5 minutes

## [​](#install) Install

* Frontend (React)
* Backend (Python)
* Backend (TypeScript)

Copy

Ask AI

```
npm install @nekuda/react-nekuda-js
```

Copy

Ask AI

```
pip install nekuda
```

Copy

Ask AI

```
npm install @nekuda/nekuda-js
```

## [​](#get-api-keys) Get API Keys

1. Sign up at [app.nekuda.ai](https://app.nekuda.ai)
2. Generate your keys:
   * **Public key** (`pk_test_...`) - for frontend card collection
   * **Secret key** (`sk_test_...`) - for backend card reveal

Copy

Ask AI

```
# Backend only - never expose this in frontend
export NEKUDA_API_KEY="sk_test_..."
```

## [​](#frontend:-collect-card) Frontend: Collect Card

Add the wallet component where users manage payment methods (e.g., settings page):

Copy

Ask AI

```
import { WalletProvider, NekudaWallet } from '@nekuda/react-nekuda-js';

function UserSettings() {
  const userId = currentUser.id; // Your user's ID

  return (
    <WalletProvider publicKey="pk_test_..." userId={userId}>
      <NekudaWallet />
    </WalletProvider>
  );
}
```

**What this does:**

* Users can add/manage payment methods
* Cards are tokenized and stored securely
* Linked to the `userId` you provide

## [​](#backend:-reveal-card) Backend: Reveal Card

When your AI agent needs to make a purchase, retrieve the card details:

* Python
* TypeScript

Copy

Ask AI

```
from nekuda import NekudaClient, MandateData

# Initialize client (reads NEKUDA_API_KEY from env)
client = NekudaClient.from_env()
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

Copy

Ask AI

```
import { NekudaClient, MandateData } from '@nekuda/nekuda-js';

// Initialize client (reads NEKUDA_API_KEY from env)
const client = NekudaClient.fromEnv();
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

## [​](#complete-flow) Complete Flow

## [​](#key-concepts) Key Concepts

### [​](#userid) userId

Links frontend and backend operations. Use your own user identifier (e.g., database user ID). Must be consistent across frontend and backend.

### [​](#mandate) Mandate

Records the user’s intent to purchase. Required before revealing card details. Contains product info, price, and merchant.

### [​](#reveal-token) Reveal Token

Short-lived, single-use token that authorizes card reveal. Generated per mandate.

### [​](#cvv-expiration) CVV Expiration

CVVs are valid for 60 minutes after collection. If expired, prompt user to re-enter using `NekudaCvvCollector`. See [CVV Management](/frontend/wallet/cvv-management).

## [​](#next-steps) Next Steps

[## System Overview

Understand how nekuda works end-to-end](/system-overview)[## Payment Flow

Detailed walkthrough of the complete payment flow](/payment-flow)[## Wallet Component

Customize the wallet UI and behavior](/frontend/wallet/overview)[## Backend SDK

Explore advanced backend SDK features](/nekuda-sdk/getting-started)

[Introduction](/introduction)[System Overview](/system-overview)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)