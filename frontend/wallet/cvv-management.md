# CVV Management
![Lux Divider](../../assets/lux/divider.svg)

**What You’ll Learn**

Learn how to:

* Check CVV validity with `isCvvValid` field
* Show `FintCvvCollector` when CVV expires
* Handle backend CVV errors
* Integrate CVV re-collection into your purchase flow

**Time to complete:** 5 minutes

CVVs are stored securely for 60 minutes after collection. After this window, you must prompt users to re-enter their CVV using `FintCvvCollector`.

## Quick Start

```
import { useWallet, FintCvvCollector } from '@fint/wallet';

function Checkout() {
  const wallet = useWallet();
  const defaultCard = wallet.payments.list.find(pm => pm.isDefault);

  // Check if CVV is still valid
  if (defaultCard && !defaultCard.isCvvValid) {
    return (
      <FintCvvCollector
        cardId={defaultCard.id}
        last4={defaultCard.lastFourDigits}
        brand={defaultCard.cardType}
        holderName={defaultCard.cardHolderName}
        expiry={defaultCard.expiryDate}
        onSuccess={() => {
          console.log('CVV updated');
          // Proceed with purchase
        }}
      />
    );
  }

  return <button>Complete Purchase</button>;
}
```

## How It Works

1. **Check CVV validity**: Each payment method has an `isCvvValid` boolean
2. **Show collector if expired**: Display `FintCvvCollector` when `isCvvValid === false`
3. **User enters CVV**: Secure iframe collects only the CVV (no full card re-entry)
4. **60-minute window resets**: CVV is stored again for 60 minutes
5. **Retry purchase**: Your backend can now reveal card details with CVV

## Component Props

### Required Props

[​](#param-card-id)

cardId

string

required

Payment method ID from `wallet.payments.list[].id`

[​](#param-last4)

last4

string

required

Last 4 digits to display. From `wallet.payments.list[].lastFourDigits`

[​](#param-brand)

**brand**

Type: `string`  
Required  
Card brand. From `wallet.payments.list[].cardType`

[​](#param-holder-name)

**holderName**

Type: `string`  
Required  
Cardholder name. From `wallet.payments.list[].cardHolderName`

[​](#param-expiry)

**expiry**

Type: `string`  
Required  
Expiry date (MM/YY). From `wallet.payments.list[].expiryDate`

### Optional Props

[​](#param-on-success)

**onSuccess**

Type: `(response: PaymentMethodResponse) => void`  
Called after successful CVV update

[​](#param-on-error)

**onError**

Type: `(error: Error) => void`  
Called if CVV collection fails

[​](#param-mode)

**mode**

Type: `'themed' | 'headless' | 'custom'`  
Default: `'themed'`  
Styling mode. See [Styling & Theming](styling-theming.md)

[​](#param-theme)

**theme**

Type: `'light' | 'dark' | 'minimal'`  
Default: `'light'`  
Pre-built theme when using `mode="themed"`

[​](#param-theme-config)

**themeConfig**

Type: `Partial<ThemeContract>`  
Theme token overrides for brand customization.

Example:

```
<FintCvvCollector
  themeConfig={{
    accent: { primary: '#7C3AED' },
    typography: { fontFamily: { base: 'Inter' } }
  }}
/>
```

[​](#param-styles)

styles

FormStyles

Component-level style overrides. Use for fine-grained control over specific elements.

[​](#param-submit-label)

submitLabel

string

default:"'Update CVV'"

Button text

## Complete Example

```
import { useState } from 'react';
import { WalletProvider, useWallet, FintCvvCollector } from '@fint/wallet';

function PurchaseFlow() {
  const [step, setStep] = useState('review'); // 'review' | 'cvv' | 'processing'
  const wallet = useWallet();

  const handlePurchase = () => {
    const defaultCard = wallet.payments.list.find(pm => pm.isDefault);

    if (!defaultCard) {
      alert('No payment method saved');
      return;
    }

    // Check CVV validity before proceeding
    if (!defaultCard.isCvvValid) {
      setStep('cvv');
      return;
    }

    // CVV is valid, proceed with backend purchase
    setStep('processing');
    completePurchase(defaultCard.id);
  };

  if (step === 'cvv') {
    const defaultCard = wallet.payments.list.find(pm => pm.isDefault);

    return (
      <div>
        <h2>CVV Expired</h2>
        <p>Please re-enter your CVV to continue</p>

        <FintCvvCollector
          cardId={defaultCard.id}
          last4={defaultCard.lastFourDigits}
          brand={defaultCard.cardType}
          holderName={defaultCard.cardHolderName}
          expiry={defaultCard.expiryDate}
          onSuccess={() => {
            // CVV updated, retry purchase
            setStep('processing');
            completePurchase(defaultCard.id);
          }}
          onError={(error) => {
            console.error('CVV collection failed:', error);
            setStep('review');
          }}
        />
      </div>
    );
  }

  if (step === 'processing') {
    return <div>Processing purchase...</div>;
  }

  return (
    <div>
      <h2>Review Purchase</h2>
      <button onClick={handlePurchase}>Complete Purchase</button>
    </div>
  );
}

function App() {
  return (
    <WalletProvider publicKey="pk_test_..." userId={currentUser.id}>
      <PurchaseFlow />
    </WalletProvider>
  );
}
```

## Backend Integration

When CVV expires, your backend’s `reveal_card_details()` call will return an error indicating missing CVV:

* Python
* TypeScript

```
from fint import FintClient, FintError

client = FintClient.from_env()
user = client.user("user_123")

try:
    reveal_resp = user.request_card_reveal_token(mandate_id)
    card = user.reveal_card_details(reveal_resp.reveal_token)
    print(f"Card: {card.card_number}")
    print(f"CVV: {card.cvv}")  # Always present after successful reveal

except CardCvvExpiredError:
    # CVV expired - frontend must collect it again
    return {"error": "CVV_EXPIRED", "action": "collect_cvv"}
except FintError as e:
    print(f"Error: {e}")
```

```
import { FintClient, FintError, CardCvvExpiredError } from '@fint/fint-js';

const client = FintClient.fromEnv();
const user = client.user('user_123');

try {
  const revealResp = await user.requestCardRevealToken(mandateId);
  const card = await user.revealCardDetails(revealResp.revealToken);
  console.log(`Card: ${card.cardNumber}`);
  console.log(`CVV: ${card.cvv}`); // Always present after successful reveal

} catch (error) {
  if (error instanceof CardCvvExpiredError) {
    // CVV expired - frontend must collect it again
    return { error: 'CVV_EXPIRED', action: 'collect_cvv' };
  }
  if (error instanceof FintError) {
    console.error(`Error: ${error.message}`);
  }
}
```

Your frontend should listen for this error and show `FintCvvCollector` to re-collect the CVV.

## FAQ

Why 60 minutes?

PCI compliance standards prohibit long-term CVV storage. The 60-minute window balances security with user experience for immediate purchases.

Can I extend the CVV validity period?

No. The 60-minute limit is a security requirement and cannot be extended.

Do users need to re-enter the full card?

No. `FintCvvCollector` only collects the CVV. The card number, expiry, and other details remain saved.

What if the user enters the wrong CVV?

The component validates the CVV format (3-4 digits based on card brand) but cannot verify correctness until used. Your AI agent will receive an error from the merchant if the CVV is incorrect during purchase.

How do I check CVV validity without useWallet?

The `isCvvValid` field is computed automatically in `wallet.payments.list`. If you need to check manually, use `isCvvAvailable(payment.cvvAvailableUntil)` helper from the SDK.

## Related

- [Payment Flow](../../payment-flow.md) — Understand CVV timing in the complete payment flow
- [Wallet Overview](overview.md) — Learn about the main wallet component
