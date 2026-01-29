# Migration Guide

**Package Renamed (v0.2.0):** `@fint/react-fint-js` → `@fint/wallet`

```
npm uninstall @fint/react-fint-js
npm install @fint/wallet
```

Update all imports from `@fint/react-fint-js` to `@fint/wallet`. No API changes—only the package name.

---

## Overview

If you’re currently using the legacy components (`FintWalletProvider`, `FintPaymentForm`, `FintCardManagement`), this guide will help you migrate to the new components.**Migration time:** 5-10 minutes per component

## Step-by-Step Migration

### 1. Replace FintWalletProvider with WalletProvider

The provider has been simplified with a cleaner API.**Before:** Copy

```
import { FintWalletProvider } from '@fint/wallet';

<FintWalletProvider
  publicKey="pk_test_..."
  userId={userId}
  apiUrl="https://api.fint.io"
>
  {children}
</FintWalletProvider>
```**After:** Copy

```
import { WalletProvider } from '@fint/wallet';

<WalletProvider
  publicKey="pk_test_..."
  userId={userId}
>
  {children}
</WalletProvider>
```**Changes:**

* Component name: `FintWalletProvider` → `WalletProvider`
* `apiUrl` prop removed (auto-configured based on environment)
* Same core props: `publicKey`, `userId`, `debug`

---

### 2. Replace FintPaymentForm with FintCollectForm

The collection form has been updated with improved styling and error handling.
**Before:** Copy

```
import { FintPaymentForm } from '@fint/wallet';

<FintPaymentForm
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
import { FintCollectForm } from '@fint/wallet';

<FintCollectForm
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

* Component name: `FintPaymentForm` → `FintCollectForm`
* Callbacks: `onSave` + `onCancel` → `onSuccess` + `onError`
* Props: `defaultCardDetails` → `defaultValues`
* Styling: `styles` + `elementsConfig` → `mode` + `theme` (simpler API)
* New modes: `themed`, `headless`, `custom`

---

### 3. Replace FintCardManagement with FintWallet

The card management modal has evolved into a full-featured wallet component.
**Before:** Copy

```
import { FintCardManagement } from '@fint/wallet';

<FintCardManagement
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
import { FintWallet } from '@fint/wallet';

// No need for modal state - FintWallet is a full-page component
<FintWallet
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

* Component name: `FintCardManagement` → `FintWallet`
* **No modal** : `FintWallet` is embedded directly in your page (not a modal)
* Props removed: `open`, `onOpenChange` (no longer a modal)
* Callbacks: Individual callbacks → unified `onError` handler
* Props: `defaultCardDetails` → `defaultCollectValues`
* Styling: `walletStyles` → `styles` (consistent API)
* **New features** : Settings tab with contact & shipping info

**If you need modal behavior:**

```
// Wrap FintWallet in your own modal component
<Modal open={isOpen} onClose={() => setIsOpen(false)}>
  <FintWallet
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

### WalletProvider (formerly FintWalletProvider)

| Old Prop | New Prop | Notes |
| --- | --- | --- |
| `publicKey` | `publicKey` | Unchanged |
| `userId` | `userId` | Unchanged |
| `apiUrl` | *(removed)* | Auto-configured |
| `debug` | `debug` | Unchanged |

### FintCollectForm (formerly FintPaymentForm)

| Old Prop | New Prop | Notes |
| --- | --- | --- |
| `onSave` | `onSuccess` | Renamed for clarity |
| `onCancel` | *(removed)* | Handle in parent |
| `defaultCardDetails` | `defaultValues` | Renamed |
| `styles` | `mode` + `theme` | Simplified API |
| `elementsConfig` | *(removed)* | Use `mode` prop |
| `walletStyles` | `styles` | Renamed |

### FintWallet (formerly FintCardManagement)

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
import { FintWalletProvider, FintCardManagement } from '@fint/wallet';

function SettingsPage() {
  const [showCards, setShowCards] = useState(false);

  return (
    <FintWalletProvider publicKey="pk_test_..." userId={userId}>
      <button onClick={() => setShowCards(true)}>
        Manage Cards
      </button>

      <FintCardManagement
        open={showCards}
        onOpenChange={setShowCards}
      />
    </FintWalletProvider>
  );
}
```**After:** Copy

```
import { WalletProvider, FintWallet } from '@fint/wallet';

function SettingsPage() {
  return (
    <WalletProvider publicKey="pk_test_..." userId={userId}>
      <FintWallet />
    </WalletProvider>
  );
}
```

### Pattern 2: Checkout Flow with Card Collection **Before:** Copy

```
import { FintWalletProvider, FintPaymentForm } from '@fint/wallet';

function CheckoutPage() {
  return (
    <FintWalletProvider publicKey="pk_test_..." userId={userId}>
      <FintPaymentForm
        onSave={(card) => {
          proceedToPayment(card);
        }}
        onCancel={() => router.back()}
      />
    </FintWalletProvider>
  );
}
```**After:**

```
import { WalletProvider, FintCollectForm } from '@fint/wallet';

function CheckoutPage() {
  return (
    <WalletProvider publicKey="pk_test_..." userId={userId}>
      <FintCollectForm
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
<FintCardManagement
  styles={{ fontFamily: 'Inter' }}
  elementsConfig={{ cardNumber: { color: '#000' } }}
  walletStyles={{ modal: { backgroundColor: '#fff' } }}
/>
```** New:**

```
<FintWallet
  mode="custom"
  styles={{
    fontFamily: 'Inter',
    cardNumber: { color: '#000' },
    modal: { backgroundColor: '#fff' }
  }}
/>
```

See [Styling & Theming](styling-theming.md) for details.

I need the modal behavior of FintCardManagement

Wrap `FintWallet` in your own modal component:

```
import { Dialog } from '@headlessui/react'; // or your modal library

<Dialog open={isOpen} onClose={() => setIsOpen(false)}>
  <FintWallet
    onError={(error) => {
      handleError(error);
      setIsOpen(false);
    }}
  />
</Dialog>
```

Where did the individual callbacks go?

`FintWallet` auto-handles card operations through the wallet context. Use `useWallet()` to access card data:

```
import { useWallet } from '@fint/wallet';

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
import { FintWalletProviderLegacy } from '@fint/wallet';
```

However, they will not receive new features or bug fixes. We recommend migrating to the new components.

---

## Need Help?

If you encounter issues during migration:

1. Check the [Component API Reference](overview.md)
2. Review [Integration Patterns](integration-patterns.md)
3. Contact support at [[email protected]](../../cdn-cgi/l/email-protection.md)
