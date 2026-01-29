# Migration Guide

**Package Renamed (v0.2.0):** `@nekuda/react-nekuda-js` → `@nekuda/wallet`

```
npm uninstall @nekuda/react-nekuda-js
npm install @nekuda/wallet
```

Update all imports from `@nekuda/react-nekuda-js` to `@nekuda/wallet`. No API changes—only the package name.

---

## Overview

If you’re currently using the legacy components (`NekudaWalletProvider`, `NekudaPaymentForm`, `NekudaCardManagement`), this guide will help you migrate to the new components.**Migration time:** 5-10 minutes per component

## Step-by-Step Migration

### 1. Replace NekudaWalletProvider with WalletProvider

The provider has been simplified with a cleaner API.**Before:** Copy

```
import { NekudaWalletProvider } from '@nekuda/wallet';

<NekudaWalletProvider
  publicKey="pk_test_..."
  userId={userId}
  apiUrl="https://api.nekuda.ai"
>
  {children}
</NekudaWalletProvider>
```**After:** Copy

```
import { WalletProvider } from '@nekuda/wallet';

<WalletProvider
  publicKey="pk_test_..."
  userId={userId}
>
  {children}
</WalletProvider>
```**Changes:**

* Component name: `NekudaWalletProvider` → `WalletProvider`
* `apiUrl` prop removed (auto-configured based on environment)
* Same core props: `publicKey`, `userId`, `debug`

---

### 2. Replace NekudaPaymentForm with NekudaCollectForm

The collection form has been updated with improved styling and error handling.
**Before:** Copy

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
```**After:** Copy

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
```**Changes:**

* Component name: `NekudaPaymentForm` → `NekudaCollectForm`
* Callbacks: `onSave` + `onCancel` → `onSuccess` + `onError`
* Props: `defaultCardDetails` → `defaultValues`
* Styling: `styles` + `elementsConfig` → `mode` + `theme` (simpler API)
* New modes: `themed`, `headless`, `custom`

---

### 3. Replace NekudaCardManagement with NekudaWallet

The card management modal has evolved into a full-featured wallet component.
**Before:** Copy

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
```**After:** Copy

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
```**Changes:**

* Component name: `NekudaCardManagement` → `NekudaWallet`
* **No modal** : `NekudaWallet` is embedded directly in your page (not a modal)
* Props removed: `open`, `onOpenChange` (no longer a modal)
* Callbacks: Individual callbacks → unified `onError` handler
* Props: `defaultCardDetails` → `defaultCollectValues`
* Styling: `walletStyles` → `styles` (consistent API)
* **New features** : Settings tab with contact & shipping info

**If you need modal behavior:**

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

## Props Mapping Reference

### WalletProvider (formerly NekudaWalletProvider)

| Old Prop | New Prop | Notes |
| --- | --- | --- |
| `publicKey` | `publicKey` | Unchanged |
| `userId` | `userId` | Unchanged |
| `apiUrl` | *(removed)* | Auto-configured |
| `debug` | `debug` | Unchanged |

### NekudaCollectForm (formerly NekudaPaymentForm)

| Old Prop | New Prop | Notes |
| --- | --- | --- |
| `onSave` | `onSuccess` | Renamed for clarity |
| `onCancel` | *(removed)* | Handle in parent |
| `defaultCardDetails` | `defaultValues` | Renamed |
| `styles` | `mode` + `theme` | Simplified API |
| `elementsConfig` | *(removed)* | Use `mode` prop |
| `walletStyles` | `styles` | Renamed |

### NekudaWallet (formerly NekudaCardManagement)

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
| N/A | `defaultShipping` |**New** |
| N/A | `onContactChange` |**New** |
| N/A | `onShippingChange` |**New** |
| N/A | `showSettings` |**New** |

---

## Common Migration Patterns

### Pattern 1: Settings Page with Card Management **Before:** Copy

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
```**After:** Copy

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

### Pattern 2: Checkout Flow with Card Collection **Before:** Copy

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
```**After:**

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

## Troubleshooting

I'm using custom styling - how do I migrate?

The new components use a simpler styling API:** Old:**Copy

```
<NekudaCardManagement
  styles={{ fontFamily: 'Inter' }}
  elementsConfig={{ cardNumber: { color: '#000' } }}
  walletStyles={{ modal: { backgroundColor: '#fff' } }}
/>
```** New:**

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

See [Styling & Theming](styling-theming.md) for details.

I need the modal behavior of NekudaCardManagement

Wrap `NekudaWallet` in your own modal component:

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

```
import { NekudaWalletProviderLegacy } from '@nekuda/wallet';
```

However, they will not receive new features or bug fixes. We recommend migrating to the new components.

---

## Need Help?

If you encounter issues during migration:

1. Check the [Component API Reference](overview.md)
2. Review [Integration Patterns](integration-patterns.md)
3. Contact support at [[email protected]](../../cdn-cgi/l/email-protection.md)
