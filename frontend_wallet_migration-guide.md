# Migration Guide

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Frontend SDK

Migration Guide

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
* [Step-by-Step Migration](#step-by-step-migration)
* [1. Replace NekudaWalletProvider with WalletProvider](#1-replace-nekudawalletprovider-with-walletprovider)
* [2. Replace NekudaPaymentForm with NekudaCollectForm](#2-replace-nekudapaymentform-with-nekudacollectform)
* [3. Replace NekudaCardManagement with NekudaWallet](#3-replace-nekudacardmanagement-with-nekudawallet)
* [Props Mapping Reference](#props-mapping-reference)
* [WalletProvider (formerly NekudaWalletProvider)](#walletprovider-formerly-nekudawalletprovider)
* [NekudaCollectForm (formerly NekudaPaymentForm)](#nekudacollectform-formerly-nekudapaymentform)
* [NekudaWallet (formerly NekudaCardManagement)](#nekudawallet-formerly-nekudacardmanagement)
* [Common Migration Patterns](#common-migration-patterns)
* [Pattern 1: Settings Page with Card Management](#pattern-1%3A-settings-page-with-card-management)
* [Pattern 2: Checkout Flow with Card Collection](#pattern-2%3A-checkout-flow-with-card-collection)
* [Troubleshooting](#troubleshooting)
* [Need Help?](#need-help)

Frontend SDK

# Migration Guide

Copy page

Migrate from legacy components to the new Wallet component

Copy page

**Package Renamed (v0.2.0):** `@nekuda/react-nekuda-js` → `@nekuda/wallet`

Copy

Ask AI

```
npm uninstall @nekuda/react-nekuda-js
npm install @nekuda/wallet
```

Update all imports from `@nekuda/react-nekuda-js` to `@nekuda/wallet`. No API changes—only the package name.

---

## [​](#overview) Overview

If you’re currently using the legacy components (`NekudaWalletProvider`, `NekudaPaymentForm`, `NekudaCardManagement`), this guide will help you migrate to the new components.
**Migration time:** 5-10 minutes per component

## [​](#step-by-step-migration) Step-by-Step Migration

### [​](#1-replace-nekudawalletprovider-with-walletprovider) 1. Replace NekudaWalletProvider with WalletProvider

The provider has been simplified with a cleaner API.
**Before:**

Copy

Ask AI

```
import { NekudaWalletProvider } from '@nekuda/wallet';

<NekudaWalletProvider
  publicKey="pk_test_..."
  userId={userId}
  apiUrl="https://api.nekuda.ai"
>
  {children}
</NekudaWalletProvider>
```

**After:**

Copy

Ask AI

```
import { WalletProvider } from '@nekuda/wallet';

<WalletProvider
  publicKey="pk_test_..."
  userId={userId}
>
  {children}
</WalletProvider>
```

**Changes:**

* Component name: `NekudaWalletProvider` → `WalletProvider`
* `apiUrl` prop removed (auto-configured based on environment)
* Same core props: `publicKey`, `userId`, `debug`

---

### [​](#2-replace-nekudapaymentform-with-nekudacollectform) 2. Replace NekudaPaymentForm with NekudaCollectForm

The collection form has been updated with improved styling and error handling.
**Before:**

Copy

Ask AI

```
import { NekudaPaymentForm } from '@nekuda/wallet';

<NekudaPaymentForm
  onSave={(formData) => console.log('Card saved:', formData)}
  onCancel={() => setShowForm(false)}
  defaultCardDetails={{
    email: user.email,
    billing_address: user.address
  }}
  styles={{
    fontFamily: 'Inter, sans-serif'
  }}
  elementsConfig={{
    cardNumber: {
      placeholder: 'Enter card number'
    }
  }}
/>
```

**After:**

Copy

Ask AI

```
import { NekudaCollectForm } from '@nekuda/wallet';

<NekudaCollectForm
  onSuccess={(response) => {
    console.log('Card saved:', response);
    setShowForm(false);
  }}
  onError={(error) => console.error('Error:', error)}
  defaultValues={{
    email: user.email,
    addressLine1: user.address
  }}
  mode="themed"
  theme="light"
/>
```

**Changes:**

* Component name: `NekudaPaymentForm` → `NekudaCollectForm`
* Callbacks: `onSave` + `onCancel` → `onSuccess` + `onError`
* Props: `defaultCardDetails` → `defaultValues`
* Styling: `styles` + `elementsConfig` → `mode` + `theme` (simpler API)
* New modes: `themed`, `headless`, `custom`

---

### [​](#3-replace-nekudacardmanagement-with-nekudawallet) 3. Replace NekudaCardManagement with NekudaWallet

The card management modal has evolved into a full-featured wallet component.
**Before:**

Copy

Ask AI

```
import { NekudaCardManagement } from '@nekuda/wallet';

<NekudaCardManagement
  open={isOpen}
  onOpenChange={setIsOpen}
  onCardSave={(card) => console.log('Card saved:', card)}
  onCardDelete={(cardId) => console.log('Card deleted:', cardId)}
  onDefaultCardSet={(cardId) => console.log('Default set:', cardId)}
  defaultCardDetails={{
    email: user.email,
    zip_code: user.zipCode
  }}
  walletStyles={{
    modal: { backgroundColor: '#fff' },
    button: {
      primary: { backgroundColor: '#3b82f6' }
    }
  }}
/>
```

**After:**

Copy

Ask AI

```
import { NekudaWallet } from '@nekuda/wallet';

// No need for modal state - NekudaWallet is a full-page component
<NekudaWallet
  defaultCollectValues={{
    email: user.email,
    zipCode: user.zipCode
  }}
  onError={(error) => console.error('Error:', error)}
  mode="themed"
  theme="light"
  styles={{
    tabs: { backgroundColor: '#fff' },
    button: { backgroundColor: '#3b82f6' }
  }}
/>
```

**Changes:**

* Component name: `NekudaCardManagement` → `NekudaWallet`
* **No modal**: `NekudaWallet` is embedded directly in your page (not a modal)
* Props removed: `open`, `onOpenChange` (no longer a modal)
* Callbacks: Individual callbacks → unified `onError` handler
* Props: `defaultCardDetails` → `defaultCollectValues`
* Styling: `walletStyles` → `styles` (consistent API)
* **New features**: Settings tab with contact & shipping info

**If you need modal behavior:**

Copy

Ask AI

```
// Wrap NekudaWallet in your own modal component
<Modal open={isOpen} onClose={() => setIsOpen(false)}>
  <NekudaWallet
    defaultCollectValues={defaultValues}
    onError={(error) => {
      console.error('Error:', error);
      setIsOpen(false);
    }}
  />
</Modal>
```

---

## [​](#props-mapping-reference) Props Mapping Reference

### [​](#walletprovider-formerly-nekudawalletprovider) WalletProvider (formerly NekudaWalletProvider)

| Old Prop | New Prop | Notes |
| --- | --- | --- |
| `publicKey` | `publicKey` | Unchanged |
| `userId` | `userId` | Unchanged |
| `apiUrl` | *(removed)* | Auto-configured |
| `debug` | `debug` | Unchanged |

### [​](#nekudacollectform-formerly-nekudapaymentform) NekudaCollectForm (formerly NekudaPaymentForm)

| Old Prop | New Prop | Notes |
| --- | --- | --- |
| `onSave` | `onSuccess` | Renamed for clarity |
| `onCancel` | *(removed)* | Handle in parent |
| `defaultCardDetails` | `defaultValues` | Renamed |
| `styles` | `mode` + `theme` | Simplified API |
| `elementsConfig` | *(removed)* | Use `mode` prop |
| `walletStyles` | `styles` | Renamed |

### [​](#nekudawallet-formerly-nekudacardmanagement) NekudaWallet (formerly NekudaCardManagement)

| Old Prop | New Prop | Notes |
| --- | --- | --- |
| `open` | *(removed)* | No longer a modal |
| `onOpenChange` | *(removed)* | No longer a modal |
| `onCardSave` | *(removed)* | Auto-handled |
| `onCardDelete` | *(removed)* | Auto-handled |
| `onDefaultCardSet` | *(removed)* | Auto-handled |
| `defaultCardDetails` | `defaultCollectValues` | Renamed |
| `walletStyles` | `styles` | Renamed |
| N/A | `defaultContact` | **New** |
| N/A | `defaultShipping` | **New** |
| N/A | `onContactChange` | **New** |
| N/A | `onShippingChange` | **New** |
| N/A | `showSettings` | **New** |

---

## [​](#common-migration-patterns) Common Migration Patterns

### [​](#pattern-1:-settings-page-with-card-management) Pattern 1: Settings Page with Card Management

**Before:**

Copy

Ask AI

```
import { NekudaWalletProvider, NekudaCardManagement } from '@nekuda/wallet';

function SettingsPage() {
  const [showCards, setShowCards] = useState(false);

  return (
    <NekudaWalletProvider publicKey="pk_test_..." userId={userId}>
      <button onClick={() => setShowCards(true)}>
        Manage Cards
      </button>

      <NekudaCardManagement
        open={showCards}
        onOpenChange={setShowCards}
      />
    </NekudaWalletProvider>
  );
}
```

**After:**

Copy

Ask AI

```
import { WalletProvider, NekudaWallet } from '@nekuda/wallet';

function SettingsPage() {
  return (
    <WalletProvider publicKey="pk_test_..." userId={userId}>
      <NekudaWallet />
    </WalletProvider>
  );
}
```

### [​](#pattern-2:-checkout-flow-with-card-collection) Pattern 2: Checkout Flow with Card Collection

**Before:**

Copy

Ask AI

```
import { NekudaWalletProvider, NekudaPaymentForm } from '@nekuda/wallet';

function CheckoutPage() {
  return (
    <NekudaWalletProvider publicKey="pk_test_..." userId={userId}>
      <NekudaPaymentForm
        onSave={(card) => {
          proceedToPayment(card);
        }}
        onCancel={() => router.back()}
      />
    </NekudaWalletProvider>
  );
}
```

**After:**

Copy

Ask AI

```
import { WalletProvider, NekudaCollectForm } from '@nekuda/wallet';

function CheckoutPage() {
  return (
    <WalletProvider publicKey="pk_test_..." userId={userId}>
      <NekudaCollectForm
        onSuccess={(response) => {
          proceedToPayment(response);
        }}
        onError={(error) => {
          console.error('Collection failed:', error);
          router.back();
        }}
      />
    </WalletProvider>
  );
}
```

---

## [​](#troubleshooting) Troubleshooting

I'm using custom styling - how do I migrate?

The new components use a simpler styling API:**Old:**

Copy

Ask AI

```
<NekudaCardManagement
  styles={{ fontFamily: 'Inter' }}
  elementsConfig={{ cardNumber: { color: '#000' } }}
  walletStyles={{ modal: { backgroundColor: '#fff' } }}
/>
```

**New:**

Copy

Ask AI

```
<NekudaWallet
  mode="custom"
  styles={{
    fontFamily: 'Inter',
    cardNumber: { color: '#000' },
    modal: { backgroundColor: '#fff' }
  }}
/>
```

See [Styling & Theming](/frontend/wallet/styling-theming) for details.

I need the modal behavior of NekudaCardManagement

Wrap `NekudaWallet` in your own modal component:

Copy

Ask AI

```
import { Dialog } from '@headlessui/react'; // or your modal library

<Dialog open={isOpen} onClose={() => setIsOpen(false)}>
  <NekudaWallet
    onError={(error) => {
      handleError(error);
      setIsOpen(false);
    }}
  />
</Dialog>
```

Where did the individual callbacks go?

`NekudaWallet` auto-handles card operations through the wallet context. Use `useWallet()` to access card data:

Copy

Ask AI

```
import { useWallet } from '@nekuda/wallet';

function MyComponent() {
  const wallet = useWallet();

  useEffect(() => {
    console.log('Cards:', wallet.payments.list);
    console.log('Default card:', wallet.payments.list.find(p => p.isDefault));
  }, [wallet.payments.list]);
}
```

Can I still use the legacy components?

Yes, the legacy components are still exported for backward compatibility:

Copy

Ask AI

```
import { NekudaWalletProviderLegacy } from '@nekuda/wallet';
```

However, they will not receive new features or bug fixes. We recommend migrating to the new components.

---

## [​](#need-help) Need Help?

If you encounter issues during migration:

1. Check the [Component API Reference](/frontend/wallet/overview#component-api-reference)
2. Review [Integration Patterns](/frontend/wallet/integration-patterns)
3. Contact support at [[email protected]](/cdn-cgi/l/email-protection#2a595f5a5a45585e6a444f415f4e4b044b43)

[Integration Patterns](/frontend/wallet/integration-patterns)[Getting Started](/nekuda-sdk/getting-started)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)