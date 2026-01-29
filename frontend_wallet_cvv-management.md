# CVV Management

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Frontend SDK

CVV Management

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

* [Quick Start](#quick-start)
* [How It Works](#how-it-works)
* [Component Props](#component-props)
* [Required Props](#required-props)
* [Optional Props](#optional-props)
* [Complete Example](#complete-example)
* [Backend Integration](#backend-integration)
* [FAQ](#faq)
* [Related](#related)

Frontend SDK

# CVV Management

Copy page

Handle CVV expiration and re-collection with NekudaCvvCollector

Copy page

**What You’ll Learn**Learn how to:

* Check CVV validity with `isCvvValid` field
* Show `NekudaCvvCollector` when CVV expires
* Handle backend CVV errors
* Integrate CVV re-collection into your purchase flow

**Time to complete:** 5 minutes

CVVs are stored securely for 60 minutes after collection. After this window, you must prompt users to re-enter their CVV using `NekudaCvvCollector`.

## [​](#quick-start) Quick Start

Copy

Ask AI

```
import { useWallet, NekudaCvvCollector } from '@nekuda/wallet';

function Checkout() {
  const wallet = useWallet();
  const defaultCard = wallet.payments.list.find(pm => pm.isDefault);

  // Check if CVV is still valid
  if (defaultCard && !defaultCard.isCvvValid) {
    return (
      <NekudaCvvCollector
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

## [​](#how-it-works) How It Works

1. **Check CVV validity**: Each payment method has an `isCvvValid` boolean
2. **Show collector if expired**: Display `NekudaCvvCollector` when `isCvvValid === false`
3. **User enters CVV**: Secure iframe collects only the CVV (no full card re-entry)
4. **60-minute window resets**: CVV is stored again for 60 minutes
5. **Retry purchase**: Your backend can now reveal card details with CVV

## [​](#component-props) Component Props

### [​](#required-props) Required Props

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

brand

string

required

Card brand. From `wallet.payments.list[].cardType`

[​](#param-holder-name)

holderName

string

required

Cardholder name. From `wallet.payments.list[].cardHolderName`

[​](#param-expiry)

expiry

string

required

Expiry date (MM/YY). From `wallet.payments.list[].expiryDate`

### [​](#optional-props) Optional Props

[​](#param-on-success)

onSuccess

(response: PaymentMethodResponse) => void

Called after successful CVV update

[​](#param-on-error)

onError

(error: Error) => void

Called if CVV collection fails

[​](#param-mode)

mode

'themed' | 'headless' | 'custom'

default:"'themed'"

Styling mode. See [Styling & Theming](/frontend/wallet/styling-theming)

[​](#param-theme)

theme

'light' | 'dark' | 'minimal'

default:"'light'"

Pre-built theme when using `mode="themed"`

[​](#param-theme-config)

themeConfig

Partial<ThemeContract>

Theme token overrides for brand customization.**Example:**

Copy

Ask AI

```
<NekudaCvvCollector
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

## [​](#complete-example) Complete Example

Copy

Ask AI

```
import { useState } from 'react';
import { WalletProvider, useWallet, NekudaCvvCollector } from '@nekuda/wallet';

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

        <NekudaCvvCollector
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

## [​](#backend-integration) Backend Integration

When CVV expires, your backend’s `reveal_card_details()` call will return an error indicating missing CVV:

* Python
* TypeScript

Copy

Ask AI

```
from nekuda import NekudaClient, NekudaError

client = NekudaClient.from_env()
user = client.user("user_123")

try:
    reveal_resp = user.request_card_reveal_token(mandate_id)
    card = user.reveal_card_details(reveal_resp.reveal_token)
    print(f"Card: {card.card_number}")
    print(f"CVV: {card.cvv}")  # Always present after successful reveal

except CardCvvExpiredError:
    # CVV expired - frontend must collect it again
    return {"error": "CVV_EXPIRED", "action": "collect_cvv"}
except NekudaError as e:
    print(f"Error: {e}")
```

Copy

Ask AI

```
import { NekudaClient, NekudaError, CardCvvExpiredError } from '@nekuda/nekuda-js';

const client = NekudaClient.fromEnv();
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
  if (error instanceof NekudaError) {
    console.error(`Error: ${error.message}`);
  }
}
```

Your frontend should listen for this error and show `NekudaCvvCollector` to re-collect the CVV.

## [​](#faq) FAQ

Why 60 minutes?

PCI compliance standards prohibit long-term CVV storage. The 60-minute window balances security with user experience for immediate purchases.

Can I extend the CVV validity period?

No. The 60-minute limit is a security requirement and cannot be extended.

Do users need to re-enter the full card?

No. `NekudaCvvCollector` only collects the CVV. The card number, expiry, and other details remain saved.

What if the user enters the wrong CVV?

The component validates the CVV format (3-4 digits based on card brand) but cannot verify correctness until used. Your AI agent will receive an error from the merchant if the CVV is incorrect during purchase.

How do I check CVV validity without useWallet?

The `isCvvValid` field is computed automatically in `wallet.payments.list`. If you need to check manually, use `isCvvAvailable(payment.cvvAvailableUntil)` helper from the SDK.

## [​](#related) Related

[## Payment Flow

Understand CVV timing in the complete payment flow](/payment-flow)[## Wallet Overview

Learn about the main wallet component](/frontend/wallet/overview)

[Settings Tab](/frontend/wallet/settings-tab)[Collection Form](/frontend/wallet/collect-form)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)