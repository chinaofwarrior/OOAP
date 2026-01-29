# Payment Flow Scenarios

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Get Started

Payment Flow Scenarios

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

* [Complete Flow Timeline](#complete-flow-timeline)
* [Scenario 1: Immediate Purchase ✅](#scenario-1%3A-immediate-purchase-%E2%9C%85)
* [Flow](#flow)
* [Outcome](#outcome)
* [Code Example](#code-example)
* [Scenario 2: Delayed Purchase ⚠️](#scenario-2%3A-delayed-purchase-%E2%9A%A0%EF%B8%8F)
* [Flow](#flow-2)
* [Outcome](#outcome-2)
* [Code Example](#code-example-2)
* [Scenario 3: Multiple Purchases ✅](#scenario-3%3A-multiple-purchases-%E2%9C%85)
* [Flow](#flow-3)
* [Outcome](#outcome-3)
* [Code Example](#code-example-3)
* [Best Practices](#best-practices)
* [Timing Considerations](#timing-considerations)
* [When CVV is Fresh (< 60 minutes)](#when-cvv-is-fresh-%3C-60-minutes)
* [When CVV Expires (> 60 minutes)](#when-cvv-expires-%3E-60-minutes)
* [Optimization Strategies](#optimization-strategies)
* [Related](#related)

Get Started

# Payment Flow Scenarios

Copy page

Real-world payment scenarios and timing considerations

Copy page

**What You’ll Learn**This guide covers:

* Timeline visualization of the complete payment flow
* Immediate purchase scenario (within 60-minute window)
* Delayed purchase scenario (CVV expired)
* Multiple purchases with the same card
* Best practices for timing-sensitive flows

**Time to read:** 10 minutes

This page provides concrete examples of how the payment flow works in real-world scenarios, with focus on timing and CVV expiration handling.

## [​](#complete-flow-timeline) Complete Flow Timeline

Understanding when each step happens helps prevent CVV expiration issues:

**Key Insights:**

* **0:00-0:05** - User adds card via NekudaWallet (CVV timer starts)
* **0:05-1:05** - 60-minute window where CVV is available
* **1:05+** - CVV expires, `request_card_reveal_token()` raises `CardCvvExpiredError`
* **Best Practice:** Complete purchases within 60 minutes of card collection

---

## [​](#scenario-1:-immediate-purchase-✅) Scenario 1: Immediate Purchase ✅

User adds card and immediately makes a purchase.

### [​](#flow) Flow

1. **00:00** - User adds card via NekudaWallet
2. **00:02** - User says “Buy this item”
3. **00:02** - Backend flow:
   * Create mandate #1
   * Request reveal token #1
   * Reveal card
   * CVV is available ✓
4. **00:03** - Purchase completes successfully

### [​](#outcome) Outcome

**Timeline**: 3 minutes (well within 60-minute window)
**Result**: Success - CVV is fresh and available

### [​](#code-example) Code Example

* Frontend
* Backend

Copy

Ask AI

```
// User adds card
<NekudaWallet />

// Immediately trigger purchase
const handlePurchase = async () => {
  const response = await fetch('/api/purchase', {
    method: 'POST',
    body: JSON.stringify({ userId: currentUser.id })
  });
};
```

Copy

Ask AI

```
from nekuda import NekudaClient, MandateData

client = NekudaClient.from_env()
user = client.user("user_123")

# Create mandate
mandate_resp = user.create_mandate(MandateData(
    product="Headphones",
    price=99.99,
    currency="USD",
    merchant="Amazon"
))

# Reveal card
reveal_resp = user.request_card_reveal_token(mandate_resp.mandate_id)
card = user.reveal_card_details(reveal_resp.reveal_token)

# CVV is guaranteed to be present after successful reveal
assert card.cvv  # Always present
```

---

## [​](#scenario-2:-delayed-purchase-⚠️) Scenario 2: Delayed Purchase ⚠️

User adds card but doesn’t make a purchase until later.

### [​](#flow-2) Flow

1. **00:00** - User adds card via NekudaWallet
2. *User closes app, comes back next day*
3. **24:00** - User says “Buy this item”
4. **24:00** - Backend flow:
   * Create mandate #1
   * Request reveal token #1 → **Raises `CardCvvExpiredError`** ❌ (60-minute window expired)
5. **24:01** - Backend signals frontend to collect CVV
6. **24:01** - User re-enters CVV via `NekudaCvvCollector`

### [​](#outcome-2) Outcome

**Timeline**: 24 hours (beyond 60-minute window)
**Result**: CVV expired - must collect again

### [​](#code-example-2) Code Example

* Frontend
* Backend

Copy

Ask AI

```
import { useWallet, NekudaCvvCollector } from '@nekuda/react-nekuda-js';

function Purchase() {
  const wallet = useWallet();
  const defaultCard = wallet.payments.list.find(pm => pm.isDefault);
  const [showCvvCollector, setShowCvvCollector] = useState(false);

  const handlePurchase = async () => {
    // Check CVV before backend call
    if (!defaultCard.isCvvValid) {
      setShowCvvCollector(true);
      return;
    }

    // Proceed with purchase
    await fetch('/api/purchase', { method: 'POST' });
  };

  if (showCvvCollector) {
    return (
      <NekudaCvvCollector
        cardId={defaultCard.id}
        last4={defaultCard.lastFourDigits}
        brand={defaultCard.cardType}
        holderName={defaultCard.cardHolderName}
        expiry={defaultCard.expiryDate}
        onSuccess={() => {
          setShowCvvCollector(false);
          handlePurchase();
        }}
      />
    );
  }

  return <button onClick={handlePurchase}>Buy Now</button>;
}
```

Copy

Ask AI

```
from nekuda import NekudaClient, MandateData

client = NekudaClient.from_env()
user = client.user("user_123")

# Create mandate
mandate_resp = user.create_mandate(MandateData(
    product="Flight to NYC",
    price=450.00,
    currency="USD",
    merchant="Delta"
))

# Reveal card
try:
    reveal_resp = user.request_card_reveal_token(mandate_resp.mandate_id)
    card = user.reveal_card_details(reveal_resp.reveal_token)
    # CVV is guaranteed to be present here
except CardCvvExpiredError:
    return {
        "error": "CVV_EXPIRED",
        "message": "Please re-enter CVV",
        "action": "collect_cvv"
    }

# CVV available, proceed
complete_purchase(card)
```

---

## [​](#scenario-3:-multiple-purchases-✅) Scenario 3: Multiple Purchases ✅

User makes multiple purchases with the same card.

### [​](#flow-3) Flow

1. **00:00** - User adds card via NekudaWallet
2. **00:05** - Purchase #1:
   * Create mandate #1 → Request token #1 → Reveal card
   * CVV available ✓
   * Purchase completes
3. **00:15** - Purchase #2:
   * Create mandate #2 (NEW!) → Request token #2 (NEW!) → Reveal card
   * CVV available ✓
   * Purchase completes
4. **00:45** - Purchase #3:
   * Create mandate #3 (NEW!) → Request token #3 (NEW!) → Reveal card
   * CVV available ✓
   * Purchase completes
5. **01:30** - Purchase #4:
   * Create mandate #4 (NEW!) → Request token #4 (NEW!) → **Raises `CardCvvExpiredError`** ❌ (60-minute window expired)
6. **01:31** - Backend signals frontend; user re-enters CVV via `NekudaCvvCollector`
7. **01:32** - Purchase #4 retry:
   * Create mandate #5 (NEW!) → Request token #5 (NEW!) → Reveal card
   * CVV available ✓
   * Purchase completes

### [​](#outcome-3) Outcome

**Key Insight**: Each purchase requires a new mandate and reveal token, even when using the same card. The card is stored once, but each transaction requires fresh authorization.
**Best Practice**: If users make frequent purchases, consider prompting them to refresh CVV proactively before the 60-minute window expires.

### [​](#code-example-3) Code Example

Copy

Ask AI

```
from nekuda import NekudaClient, MandateData

client = NekudaClient.from_env()
user = client.user("user_123")

# Purchase #1
mandate_1 = user.create_mandate(MandateData(
    product="Coffee", price=5.00, currency="USD", merchant="Starbucks"
))
reveal_1 = user.request_card_reveal_token(mandate_1.mandate_id)
card_1 = user.reveal_card_details(reveal_1.reveal_token)
# Complete purchase #1

# Purchase #2 (NEW MANDATE + TOKEN REQUIRED)
mandate_2 = user.create_mandate(MandateData(
    product="Lunch", price=15.00, currency="USD", merchant="Chipotle"
))
reveal_2 = user.request_card_reveal_token(mandate_2.mandate_id)
card_2 = user.reveal_card_details(reveal_2.reveal_token)
# Complete purchase #2

# CANNOT reuse mandate_1 or reveal_1 for purchase #2
```

---

## [​](#best-practices) Best Practices

## Check CVV Before Backend Call

Use `isCvvValid` field in frontend to catch expiration early

## Handle Expired CVV Gracefully

Show `NekudaCvvCollector` with clear messaging when CVV expires

## Proactive CVV Refresh

For frequent purchases, prompt CVV re-entry before 60-minute window expires

## New Mandate Per Purchase

Never reuse mandates or reveal tokens across multiple purchases

---

## [​](#timing-considerations) Timing Considerations

### [​](#when-cvv-is-fresh-<-60-minutes) When CVV is Fresh (< 60 minutes)

* ✅ Immediate purchases work seamlessly
* ✅ Multiple purchases within window work
* ✅ No user interruption needed

### [​](#when-cvv-expires->-60-minutes) When CVV Expires (> 60 minutes)

* ❌ Backend `request_card_reveal_token()` raises `CardCvvExpiredError`
* ⚠️ Backend signals frontend to show `NekudaCvvCollector`
* ⏱️ User re-enters CVV (30 seconds)
* ✅ Retry token request with fresh CVV

### [​](#optimization-strategies) Optimization Strategies

1. **Check `isCvvValid` before purchase**
   * Prevents wasted backend calls
   * Better UX (catch early on frontend)
2. **Show CVV age indicator**
   * “CVV expires in 45 minutes”
   * Encourage timely purchases
3. **Proactive re-collection**
   * For high-value purchases, collect CVV just before transaction
   * Minimizes risk of expiration during checkout

---

## [​](#related) Related

[## Payment Flow Core

Understand the three-stage payment flow](/payment-flow)[## CVV Management

Learn about NekudaCvvCollector component](/frontend/wallet/cvv-management)[## Troubleshooting

Common issues and solutions](/payment-flow#troubleshooting)[## Backend SDK

Implement mandate and reveal logic](/nekuda-sdk/getting-started)

[Payment Flow](/payment-flow)[Support](/support)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)