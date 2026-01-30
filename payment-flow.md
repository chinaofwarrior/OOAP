# Payment Flow
![Lux Divider](assets/lux/divider.svg)

**What You’ll Learn**

This guide covers:

* The three-stage payment flow (Collection → Mandate → Reveal)
* CVV expiration rules (60-minute window)
* Frontend CVV validation with `useWallet()` and `isCvvValid`
* Backend CVV error handling
* Mandate requirements (one per purchase)
* Common flow scenarios and troubleshooting

**Time to read:** 15 minutes

This guide walks through the complete payment flow in the Fint system, from initial card collection to final card reveal. Understanding this flow is critical for building reliable payment integrations.

## Overview

The Fint payment system follows a secure three-stage flow. **Critical: One Mandate Per Purchase.** Every purchase requires a **new mandate** and **new reveal token**. You cannot reuse mandates or reveal tokens across multiple purchases. Each transaction must follow the complete flow: Create Mandate → Request Token → Reveal Card.

## The Three Stages

### Stage 1: Card Collection (Frontend)

Users add their payment methods through the **FintWallet** component. This happens once when they set up their wallet.

![Collect Payment Info](assets/Collect%20Payment%20Info.png)

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
```

**What happens:**

* User enters card details in secure iframe
* Card is tokenized and stored in Fint vault
* Linked to the `userId` you provided
* CVV is stored securely with timestamp

---

### Stage 2: Mandate Creation (Backend)

When your user instructs their AI agent to make a purchase, your backend creates a **mandate** - a record of the user’s intent to purchase.

![Mandate Capture](assets/Mandate%20Capture.png)

* Python
* TypeScript

```
from fint import FintClient, MandateData

client = FintClient.from_env()
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

```
import { FintClient, MandateData } from '@fint/fint-js';

const client = FintClient.fromEnv();
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

### Stage 3: Card Reveal (Backend)

Using the mandate, request a reveal token and exchange it for the actual card details.

![Reveal Token Generation & Usage](assets/Reveal%20Token%20Generation%20%26%20Usage.png)

* Python
* TypeScript

```
# Request reveal token
reveal_response = user.request_card_reveal_token(
    mandate_id=mandate_response.mandate_id
)

# Reveal card details
card = user.reveal_card_details(reveal_response.reveal_token)

print(f"Card: **** ** ** ****{card.card_number[-4:]}")
print(f"Expiry: {card.card_expiry_date}")
print(f"CVV: {card.cvv}")
print(f"Name: {card.cardholder_name}")
```

```
// Request reveal token
const revealResponse = await user.requestCardRevealToken(
  mandateResponse.mandateId
);

// Reveal card details
const card = await user.revealCardDetails(revealResponse.revealToken);

console.log(`Card:** ** **** ** **${card.cardNumber.slice(-4)}`);
console.log(`Expiry: ${card.cardExpiryDate}`);
console.log(`CVV: ${card.cvv}`);
console.log(`Name: ${card.cardholderName}`);
```

**What happens:**

* Reveal token is generated (short-lived, single-use)
* Token is exchanged for card details
* Returns card number, expiry, CVV\*, and cardholder name

---

## 🔑 Mandate Requirements

**Every Purchase = New Mandate + New Reveal Token.** You **cannot** reuse mandates or reveal tokens. Each purchase requires:

1. Create a **new mandate** with the purchase details
2. Request a **new reveal token** using that mandate ID
3. Reveal card details using that reveal token

### Why Mandates Are Required

Mandates serve multiple critical purposes:

- **Authorization record:** Each mandate documents the user’s explicit intent to make a specific purchase, creating an audit trail.
- **Security:** Single-use tokens prevent replay attacks and unauthorized card reveals.
- **Compliance:** Card networks require proof of user authorization for each transaction.
- **Transparency:** Users can review their purchase history through mandate records.

### Token Lifecycle

1. Create Mandate
2. `mandate_id`
3. Request Reveal Token
4. `reveal_token`
5. Reveal Card
6. Card Details
7. Complete Purchase
8. Token Consumed

**Key Points:**

* **Reveal tokens are single-use** - once you reveal card details, the token is consumed
* **Mandates are tied to specific purchases** - you cannot use mandate #1 for purchase #2
* **New purchase = complete new flow** - even if it’s the same user and same card

---

## ⚠️ Critical: CVV Validation

**CVV is only available for 60 minutes after collection.** CVV validation happens when you **request a reveal token**. If the CVV has expired (>60 minutes since collection), `request_card_reveal_token()` will raise a `CardCvvExpiredError`. You must prompt the user to re-enter their CVV before proceeding.

CVVs are stored securely with a timestamp. For PCI compliance, they cannot be stored long-term. The 60-minute window allows for immediate purchases while maintaining security standards.

**Key behavior:**

* CVV validation occurs at `request_card_reveal_token()` time
* If CVV is expired, the token request fails with an error
* If token request succeeds, `reveal_card_details()` always returns a valid CVV

### Frontend: Check CVV Validity Before Purchase

Use `useWallet()` to check if the default card has a valid CVV **before** calling your backend:

```
import { useWallet, FintCvvCollector } from '@fint/wallet';

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

### Frontend: Re-collect CVV When Expired

When `isCvvValid === false`, show `FintCvvCollector` to prompt the user for just their CVV (not the full card):

```
import { FintCvvCollector } from '@fint/wallet';

function CvvPrompt() {
  const wallet = useWallet();
  const defaultCard = wallet.payments.list.find(pm => pm.isDefault);

  return (
    <FintCvvCollector
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

See [CVV Management](frontend/wallet/cvv-management.md) for complete documentation.

### Backend: Handle CVV Expiration Errors

When you call `request_card_reveal_token()`, the API validates the card’s CVV. If expired, it raises a `CardCvvExpiredError`:

* Python
* TypeScript

```
from fint import FintClient, MandateData, CardCvvExpiredError

client = FintClient.from_env()
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

```
import { FintClient, MandateData, CardCvvExpiredError } from '@fint/fint-js';

const client = FintClient.fromEnv();
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

Your frontend receives this error and shows `FintCvvCollector`. After the user updates their CVV, retry the token request.

### Best Practices for CVV Handling

## Do: Catch CVV Errors

Always wrap `request_card_reveal_token()` in try-catch to handle `CardCvvExpiredError`.

## Do: Check Frontend First

Use `useWallet().payments.find(pm => pm.isDefault).isCvvValid` to avoid unnecessary backend calls.

## Don't: Store CVV Yourself

Never store or log CVV values. Let Fint handle secure storage.

## Don't: Check CVV After Reveal

Once `reveal_card_details()` succeeds, the CVV is always present. No need to check for `None`/`undefined`.

---

## User ID: The Connection Point

The `userId` is what connects frontend card collection with backend retrieval:

**Critical:** Both frontend and backend must use the **exact same** `userId` string.

```
<WalletProvider
  publicKey="pk_test_..."
  userId="user_123"  // Must match backend
>
  <FintWallet />
</WalletProvider>
```

---

## Troubleshooting

Getting CardCvvExpiredError **Check:**

* Has it been more than 60 minutes since the CVV was collected?
* Did the user add the card recently?
* Is the `userId` consistent between frontend and backend?

**Solution:** Check `isCvvValid` on the frontend before calling backend, and prompt user to re-enter CVV using `FintCvvCollector`.

Can't find user's card **Check:**

* Is the `userId` exactly the same between frontend and backend?
* Did the user successfully add a card? (Check in their FintWallet UI)
* Are you using the correct API key for the environment?

**Solution:** Verify `userId` consistency and ensure card was saved successfully.

Mandate creation fails **Check:**

* Are all required mandate fields provided? (product, price, currency, merchant)
* Is the user authenticated correctly?
* Is the API key valid?

**Solution:** Review mandate data and ensure all fields are present and valid.

How to extend CVV availability?**Answer:** The 60-minute window cannot be extended for security/compliance reasons. Instead:

* Prompt users to refresh payment methods before expiration
* Implement graceful error handling when CVV is missing
* Guide users through quick re-entry flow

---

## Next Steps

- [Payment Flow Scenarios](payment-flow-scenarios.md) — See real-world examples with timing and CVV expiration
- [Wallet Component](frontend/wallet/overview.md) — Set up FintWallet for card collection
- [CVV Management](frontend/wallet/cvv-management.md) — Handle CVV expiration with FintCvvCollector
- [Backend SDK](fint-sdk/getting-started.md) — Implement mandate creation and card reveal
 
### On-chain Stablecoin Payments (Fint + Fintechain)
 
If you need stablecoin payments, create an order in your backend through Fint’s REST API and handle webhook notifications for status changes. Fintechain performs multi-chain execution and confirmation beneath Fint’s API surface, so your integration remains consistent across chains and currencies.

![Webhooks Status Push](assets/Webhooks%20Status%20Push.png)
 
**Create payment (server-side)**
 
```bash
curl -X POST https://api.fint.io/v1/payments \
  -H "Authorization: Bearer $FINT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": "25.00",
    "currency": "USDC",
    "order_id": "ORDER-1001",
    "description": "Subscription payment",
    "notify_url": "https://merchant.example.com/fint/webhook",
    "metadata": {
      "customer_id": "CUST-2001"
    }
  }'
```
 
Handle the webhook to mark orders as succeeded or failed, and persist chain metadata (e.g., `tx_hash`, `chain`) when available for audit and reconciliation.

