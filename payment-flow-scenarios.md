# Payment Flow Scenarios

**What You’ll Learn ** This guide covers:

* Timeline visualization of the complete payment flow
* Immediate purchase scenario (within 60-minute window)
* Delayed purchase scenario (CVV expired)
* Multiple purchases with the same card
* Best practices for timing-sensitive flows

**Time to read:** 10 minutes

This page provides concrete examples of how the payment flow works in real-world scenarios, with focus on timing and CVV expiration handling.

## Complete Flow Timeline

Understanding when each step happens helps prevent CVV expiration issues:**Key Insights:**

* **0:00-0:05** - User adds card via FintWallet (CVV timer starts)
* **0:05-1:05** - 60-minute window where CVV is available
* **1:05+** - CVV expires, `request_card_reveal_token()` raises `CardCvvExpiredError`
* **Best Practice:** Complete purchases within 60 minutes of card collection

---

## Scenario 1: Immediate Purchase ✅

User adds card and immediately makes a purchase.

### Flow

1.**00:00** - User adds card via FintWallet
2.**00:02** - User says “Buy this item”
3.**00:02** - Backend flow:
   * Create mandate #1
   * Request reveal token #1
   * Reveal card
   * CVV is available ✓
4. **00:03** - Purchase completes successfully

### Outcome **Timeline** : 3 minutes (well within 60-minute window)
**Result** : Success - CVV is fresh and available

### Code Example

* Frontend
* Backend

```
// User adds card
<FintWallet />

// Immediately trigger purchase
const handlePurchase = async () => {
  const response = await fetch('/api/purchase', {
    method: 'POST',
    body: JSON.stringify({ userId: currentUser.id })
  });
};
```

```
from fint import FintClient, MandateData

client = FintClient.from_env()
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

## Scenario 2: Delayed Purchase ⚠️

User adds card but doesn’t make a purchase until later.

### Flow

1. **00:00** - User adds card via FintWallet
2. *User closes app, comes back next day*
3. **24:00** - User says “Buy this item”
4.**24:00** - Backend flow:
   * Create mandate #1
   * Request reveal token #1 → **Raises `CardCvvExpiredError`** ❌ (60-minute window expired)
5.**24:01** - Backend signals frontend to collect CVV
6.**24:01** - User re-enters CVV via `FintCvvCollector`

### Outcome **Timeline** : 24 hours (beyond 60-minute window)
**Result** : CVV expired - must collect again

### Code Example

* Frontend
* Backend

```
import { useWallet, FintCvvCollector } from '@fint/react-fint-js';

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
      <FintCvvCollector
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

```
from fint import FintClient, MandateData

client = FintClient.from_env()
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

## Scenario 3: Multiple Purchases ✅

User makes multiple purchases with the same card.

### Flow

1. **00:00** - User adds card via FintWallet
2.**00:05** - Purchase #1:
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
6.**01:31** - Backend signals frontend; user re-enters CVV via `FintCvvCollector`
7.**01:32** - Purchase #4 retry:
   * Create mandate #5 (NEW!) → Request token #5 (NEW!) → Reveal card
   * CVV available ✓
   * Purchase completes

### Outcome

**Key Insight** : Each purchase requires a new mandate and reveal token, even when using the same card. The card is stored once, but each transaction requires fresh authorization.
**Best Practice** : If users make frequent purchases, consider prompting them to refresh CVV proactively before the 60-minute window expires.

### Code Example

```
from fint import FintClient, MandateData

client = FintClient.from_env()
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

## Best Practices

## Check CVV Before Backend Call

Use `isCvvValid` field in frontend to catch expiration early

## Handle Expired CVV Gracefully

Show `FintCvvCollector` with clear messaging when CVV expires

## Proactive CVV Refresh

For frequent purchases, prompt CVV re-entry before 60-minute window expires

## New Mandate Per Purchase

Never reuse mandates or reveal tokens across multiple purchases

---

## Timing Considerations

### When CVV is Fresh (< 60 minutes)

* ✅ Immediate purchases work seamlessly
* ✅ Multiple purchases within window work
* ✅ No user interruption needed

### When CVV Expires (> 60 minutes)

* ❌ Backend `request_card_reveal_token()` raises `CardCvvExpiredError`
* ⚠️ Backend signals frontend to show `FintCvvCollector`
* ⏱️ User re-enters CVV (30 seconds)
* ✅ Retry token request with fresh CVV

### Optimization Strategies

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

## Related

- [Payment Flow Core](payment-flow.md) — Understand the three-stage payment flow
- [CVV Management](frontend/wallet/cvv-management.md) — Learn about FintCvvCollector component
- [Troubleshooting](payment-flow.md) — Common issues and solutions
- [Backend SDK](fint-sdk/getting-started.md) — Implement mandate and reveal logic
