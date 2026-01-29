# Payment Flow

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Get Started

Payment Flow

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

* [Overview](#overview)
* [The Three Stages](#the-three-stages)
* [Stage 1: Card Collection (Frontend)](#stage-1%3A-card-collection-frontend)
* [Stage 2: Mandate Creation (Backend)](#stage-2%3A-mandate-creation-backend)
* [Stage 3: Card Reveal (Backend)](#stage-3%3A-card-reveal-backend)
* [🔑 Mandate Requirements](#%F0%9F%94%91-mandate-requirements)
* [Why Mandates Are Required](#why-mandates-are-required)
* [Token Lifecycle](#token-lifecycle)
* [⚠️ Critical: CVV Validation](#%E2%9A%A0%EF%B8%8F-critical%3A-cvv-validation)
* [Frontend: Check CVV Validity Before Purchase](#frontend%3A-check-cvv-validity-before-purchase)
* [Frontend: Re-collect CVV When Expired](#frontend%3A-re-collect-cvv-when-expired)
* [Backend: Handle CVV Expiration Errors](#backend%3A-handle-cvv-expiration-errors)
* [Best Practices for CVV Handling](#best-practices-for-cvv-handling)
* [User ID: The Connection Point](#user-id%3A-the-connection-point)
* [Troubleshooting](#troubleshooting)
* [Next Steps](#next-steps)

Get Started

# Payment Flow

Copy page

Understand the complete payment flow from collection to card reveal, including critical timing considerations

Copy page

**What You’ll Learn**This guide covers:

* The three-stage payment flow (Collection → Mandate → Reveal)
* CVV expiration rules (60-minute window)
* Frontend CVV validation with `useWallet()` and `isCvvValid`
* Backend CVV error handling
* Mandate requirements (one per purchase)
* Common flow scenarios and troubleshooting

**Time to read:** 15 minutes

This guide walks through the complete payment flow in the nekuda system, from initial card collection to final card reveal. Understanding this flow is critical for building reliable payment integrations.

## [​](#overview) Overview

The nekuda payment system follows a secure three-stage flow:


**Critical: One Mandate Per Purchase**Every purchase requires a **new mandate** and **new reveal token**. You cannot reuse mandates or reveal tokens across multiple purchases. Each transaction must follow the complete flow: Create Mandate → Request Token → Reveal Card.

## [​](#the-three-stages) The Three Stages

### [​](#stage-1:-card-collection-frontend) Stage 1: Card Collection (Frontend)

Users add their payment methods through the **NekudaWallet** component. This happens once when they set up their wallet.

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

**What happens:**

* User enters card details in secure iframe
* Card is tokenized and stored in nekuda vault
* Linked to the `userId` you provided
* CVV is stored securely with timestamp

---

### [​](#stage-2:-mandate-creation-backend) Stage 2: Mandate Creation (Backend)

When your user instructs their AI agent to make a purchase, your backend creates a **mandate** - a record of the user’s intent to purchase.

* Python
* TypeScript

Copy

Ask AI

```
from nekuda import NekudaClient, MandateData

client = NekudaClient.from_env()
user = client.user("user_123")

# Create mandate with purchase details
mandate = MandateData(
    product="Wireless Headphones",
    price=99.99,
    currency="USD",
    merchant="BestBuy"
)

mandate_response = user.create_mandate(mandate)
print(f"Mandate ID: {mandate_response.mandate_id}")
```

Copy

Ask AI

```
import { NekudaClient, MandateData } from '@nekuda/nekuda-js';

const client = NekudaClient.fromEnv();
const user = client.user('user_123');

// Create mandate with purchase details
const mandate = new MandateData({
  product: 'Wireless Headphones',
  price: 99.99,
  currency: 'USD',
  merchant: 'BestBuy'
});

const mandateResponse = await user.createMandate(mandate);
console.log(`Mandate ID: ${mandateResponse.mandateId}`);
```

**What happens:**

* Records user’s purchase intent
* Validates the request
* Returns a `mandate_id` for authorization

---

### [​](#stage-3:-card-reveal-backend) Stage 3: Card Reveal (Backend)

Using the mandate, request a reveal token and exchange it for the actual card details.

* Python
* TypeScript

Copy

Ask AI

```
# Request reveal token
reveal_response = user.request_card_reveal_token(
    mandate_id=mandate_response.mandate_id
)

# Reveal card details
card = user.reveal_card_details(reveal_response.reveal_token)

print(f"Card: **** **** **** {card.card_number[-4:]}")
print(f"Expiry: {card.card_expiry_date}")
print(f"CVV: {card.cvv}")
print(f"Name: {card.cardholder_name}")
```

Copy

Ask AI

```
// Request reveal token
const revealResponse = await user.requestCardRevealToken(
  mandateResponse.mandateId
);

// Reveal card details
const card = await user.revealCardDetails(revealResponse.revealToken);

console.log(`Card: **** **** **** ${card.cardNumber.slice(-4)}`);
console.log(`Expiry: ${card.cardExpiryDate}`);
console.log(`CVV: ${card.cvv}`);
console.log(`Name: ${card.cardholderName}`);
```

**What happens:**

* Reveal token is generated (short-lived, single-use)
* Token is exchanged for card details
* Returns card number, expiry, CVV\*, and cardholder name

---

## [​](#🔑-mandate-requirements) 🔑 Mandate Requirements

**Every Purchase = New Mandate + New Reveal Token**You **cannot** reuse mandates or reveal tokens. Each purchase requires:

1. Create a **new mandate** with the purchase details
2. Request a **new reveal token** using that mandate ID
3. Reveal card details using that reveal token

### [​](#why-mandates-are-required) Why Mandates Are Required

Mandates serve multiple critical purposes:

## Authorization Record

Each mandate documents the user’s explicit intent to make a specific purchase, creating an audit trail.

## Security

Single-use tokens prevent replay attacks and unauthorized card reveals.

## Compliance

Card networks require proof of user authorization for each transaction.

## Transparency

Users can review their purchase history through mandate records.

### [​](#token-lifecycle) Token Lifecycle

**1.** Create Mandate → **2.** `mandate_id` → **3.** Request Reveal Token → **4.** `reveal_token` → **5.** Reveal Card → **6.** Card Details → **7.** Complete Purchase → **8.** Token Consumed
**Key Points:**

* **Reveal tokens are single-use** - once you reveal card details, the token is consumed
* **Mandates are tied to specific purchases** - you cannot use mandate #1 for purchase #2
* **New purchase = complete new flow** - even if it’s the same user and same card

---

## [​](#⚠️-critical:-cvv-validation) ⚠️ Critical: CVV Validation

**CVV is only available for 60 minutes after collection.**CVV validation happens when you **request a reveal token**. If the CVV has expired (>60 minutes since collection), `request_card_reveal_token()` will raise a `CardCvvExpiredError`. You must prompt the user to re-enter their CVV before proceeding.

CVVs are stored securely with a timestamp. For PCI compliance, they cannot be stored long-term. The 60-minute window allows for immediate purchases while maintaining security standards.
**Key behavior:**

* CVV validation occurs at `request_card_reveal_token()` time
* If CVV is expired, the token request fails with an error
* If token request succeeds, `reveal_card_details()` always returns a valid CVV

### [​](#frontend:-check-cvv-validity-before-purchase) Frontend: Check CVV Validity Before Purchase

Use `useWallet()` to check if the default card has a valid CVV **before** calling your backend:

Copy

Ask AI

```
import { useWallet, NekudaCvvCollector } from '@nekuda/react-nekuda-js';

function PurchaseButton() {
  const wallet = useWallet();
  const defaultCard = wallet.payments.list.find(pm => pm.isDefault);

  const handlePurchase = () => {
    // Check CVV validity
    if (!defaultCard.isCvvValid) {
      // Show CVV collector component
      showCvvCollector();
      return;
    }

    // CVV valid, proceed with backend purchase
    proceedToBackend();
  };

  return <button onClick={handlePurchase}>Complete Purchase</button>;
}
```

Each payment method has an `isCvvValid` boolean that’s automatically computed based on the `cvvAvailableUntil` timestamp.

### [​](#frontend:-re-collect-cvv-when-expired) Frontend: Re-collect CVV When Expired

When `isCvvValid === false`, show `NekudaCvvCollector` to prompt the user for just their CVV (not the full card):

Copy

Ask AI

```
import { NekudaCvvCollector } from '@nekuda/react-nekuda-js';

function CvvPrompt() {
  const wallet = useWallet();
  const defaultCard = wallet.payments.list.find(pm => pm.isDefault);

  return (
    <NekudaCvvCollector
      cardId={defaultCard.id}
      last4={defaultCard.lastFourDigits}
      brand={defaultCard.cardType}
      holderName={defaultCard.cardHolderName}
      expiry={defaultCard.expiryDate}
      onSuccess={() => {
        // CVV updated, retry purchase
        proceedToBackend();
      }}
    />
  );
}
```

See [CVV Management](/frontend/wallet/cvv-management) for complete documentation.

### [​](#backend:-handle-cvv-expiration-errors) Backend: Handle CVV Expiration Errors

When you call `request_card_reveal_token()`, the API validates the card’s CVV. If expired, it raises a `CardCvvExpiredError`:

* Python
* TypeScript

Copy

Ask AI

```
from nekuda import NekudaClient, MandateData, CardCvvExpiredError

client = NekudaClient.from_env()
user = client.user("user_123")

# Create mandate
mandate_response = user.create_mandate(MandateData(
    product="Flight to NYC",
    price=450.00,
    currency="USD",
    merchant="Delta Airlines"
))

try:
    # CVV validation happens here
    reveal_response = user.request_card_reveal_token(mandate_response.mandate_id)

    # If we reach here, CVV is valid
    card = user.reveal_card_details(reveal_response.reveal_token)

    # card.cvv is guaranteed to be present
    complete_purchase(card)

except CardCvvExpiredError:
    # CVV expired - signal frontend to collect it
    return {
        "error": "CVV_EXPIRED",
        "message": "CVV expired. Please re-enter CVV.",
        "action": "collect_cvv"
    }
```

Copy

Ask AI

```
import { NekudaClient, MandateData, CardCvvExpiredError } from '@nekuda/nekuda-js';

const client = NekudaClient.fromEnv();
const user = client.user('user_123');

// Create mandate
const mandateResponse = await user.createMandate(new MandateData({
  product: 'Flight to NYC',
  price: 450.00,
  currency: 'USD',
  merchant: 'Delta Airlines'
}));

try {
  // CVV validation happens here
  const revealResponse = await user.requestCardRevealToken(mandateResponse.mandateId);

  // If we reach here, CVV is valid
  const card = await user.revealCardDetails(revealResponse.revealToken);

  // card.cvv is guaranteed to be present
  await completePurchase(card);

} catch (error) {
  if (error instanceof CardCvvExpiredError) {
    // CVV expired - signal frontend to collect it
    return {
      error: 'CVV_EXPIRED',
      message: 'CVV expired. Please re-enter CVV.',
      action: 'collect_cvv'
    };
  }
  throw error;
}
```

Your frontend receives this error and shows `NekudaCvvCollector`. After the user updates their CVV, retry the token request.

### [​](#best-practices-for-cvv-handling) Best Practices for CVV Handling

## Do: Catch CVV Errors

Always wrap `request_card_reveal_token()` in try-catch to handle `CardCvvExpiredError`.

## Do: Check Frontend First

Use `useWallet().payments.find(pm => pm.isDefault).isCvvValid` to avoid unnecessary backend calls.

## Don't: Store CVV Yourself

Never store or log CVV values. Let nekuda handle secure storage.

## Don't: Check CVV After Reveal

Once `reveal_card_details()` succeeds, the CVV is always present. No need to check for `None`/`undefined`.

---

## [​](#user-id:-the-connection-point) User ID: The Connection Point

The `userId` is what connects frontend card collection with backend retrieval:

**Critical**: Both frontend and backend must use the **exact same** `userId` string.

Frontend

Backend

Copy

Ask AI

```
<WalletProvider
  publicKey="pk_test_..."
  userId="user_123"  // Must match backend
>
  <NekudaWallet />
</WalletProvider>
```

---

## [​](#troubleshooting) Troubleshooting

Getting CardCvvExpiredError

**Check:**

* Has it been more than 60 minutes since the CVV was collected?
* Did the user add the card recently?
* Is the `userId` consistent between frontend and backend?

**Solution:** Check `isCvvValid` on the frontend before calling backend, and prompt user to re-enter CVV using `NekudaCvvCollector`.

Can't find user's card

**Check:**

* Is the `userId` exactly the same between frontend and backend?
* Did the user successfully add a card? (Check in their NekudaWallet UI)
* Are you using the correct API key for the environment?

**Solution:** Verify `userId` consistency and ensure card was saved successfully.

Mandate creation fails

**Check:**

* Are all required mandate fields provided? (product, price, currency, merchant)
* Is the user authenticated correctly?
* Is the API key valid?

**Solution:** Review mandate data and ensure all fields are present and valid.

How to extend CVV availability?

**Answer:** The 60-minute window cannot be extended for security/compliance reasons. Instead:

* Prompt users to refresh payment methods before expiration
* Implement graceful error handling when CVV is missing
* Guide users through quick re-entry flow

---

## [​](#next-steps) Next Steps

[## Payment Flow Scenarios

See real-world examples with timing and CVV expiration](/payment-flow-scenarios)[## Wallet Component

Set up NekudaWallet for card collection](/frontend/wallet/overview)[## CVV Management

Handle CVV expiration with NekudaCvvCollector](/frontend/wallet/cvv-management)[## Backend SDK

Implement mandate creation and card reveal](/nekuda-sdk/getting-started)

[System Overview](/system-overview)[Payment Flow Scenarios](/payment-flow-scenarios)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)