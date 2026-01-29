# Settings Tab

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Frontend SDK

Settings Tab

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
* [Quick Start](#quick-start)
* [Contact Information](#contact-information)
* [Pre-fill Contact Data](#pre-fill-contact-data)
* [Sync Changes to Your Database](#sync-changes-to-your-database)
* [Shipping Address](#shipping-address)
* [Pre-fill Shipping Data](#pre-fill-shipping-data)
* [Sync Changes](#sync-changes)
* [Accessing Settings in Your App](#accessing-settings-in-your-app)
* [Hide Settings Tab](#hide-settings-tab)
* [What’s Next?](#what%E2%80%99s-next)
* [FAQ](#faq)

Frontend SDK

# Settings Tab

Copy page

Let users manage contact information and shipping address

Copy page

## [​](#overview) Overview

The Settings tab lets users save their contact info and shipping address. Your AI agent uses this information when filling out checkout forms on merchant sites.

Saved settings ensure your AI agent fills forms consistently across all purchases.

---

## [​](#quick-start) Quick Start

Copy

Ask AI

```
import { WalletProvider, NekudaWallet } from '@nekuda/wallet';

<WalletProvider publicKey="pk_test_..." userId={userId}>
  <NekudaWallet theme="light" />
</WalletProvider>
```

---

## [​](#contact-information) Contact Information

### [​](#pre-fill-contact-data) Pre-fill Contact Data

Reduce friction by pre-filling information from your user database:

Copy

Ask AI

```
<NekudaWallet
  defaultContact={{
    firstName: user.firstName,
    lastName: user.lastName,
    email: user.email,
    phone: user.phone
  }}
/>
```

### [​](#sync-changes-to-your-database) Sync Changes to Your Database

Get notified when users update their contact info:

Copy

Ask AI

```
<NekudaWallet
  defaultContact={user.contact}
  onContactChange={(contactData) => {
    // Update your database
    updateUser(user.id, { contact: contactData });
  }}
/>
```

**Fields**: `firstName`, `lastName`, `email`, `phone` (optional)


---

## [​](#shipping-address) Shipping Address

### [​](#pre-fill-shipping-data) Pre-fill Shipping Data

Copy

Ask AI

```
<NekudaWallet
  defaultShipping={{
    addressLine1: user.address.street,
    addressLine2: user.address.apt,
    city: user.address.city,
    state: user.address.state,
    zipCode: user.address.zip,
    country: 'United States'
  }}
/>
```

### [​](#sync-changes) Sync Changes

Copy

Ask AI

```
<NekudaWallet
  defaultShipping={user.shippingAddress}
  onShippingChange={(shippingData) => {
    updateUser(user.id, { shipping: shippingData });
  }}
/>
```

**Fields**: `addressLine1`, `addressLine2` (optional), `city`, `state`, `zipCode`, `country`


---

## [​](#accessing-settings-in-your-app) Accessing Settings in Your App

Display user settings elsewhere in your app:

Copy

Ask AI

```
import { useWallet } from '@nekuda/wallet';

function UserProfile() {
  const wallet = useWallet();
  const contact = wallet.contact.data;
  const shipping = wallet.shipping.data;

  return (
    <div>
      {contact && (
        <p>{contact.firstName} {contact.lastName} - {contact.email}</p>
      )}
      {shipping && (
        <p>{shipping.city}, {shipping.state}</p>
      )}
    </div>
  );
}
```

---

## [​](#hide-settings-tab) Hide Settings Tab

If you don’t need contact and shipping management, hide the Settings tab:

Copy

Ask AI

```
<NekudaWallet showSettings={false} />
```

This shows only the Payment Methods view.


---

## [​](#what’s-next) What’s Next?

[## Payment Methods Tab

Manage saved cards](/frontend/wallet/payment-methods-tab)[## Styling & Theming

Customize appearance](/frontend/wallet/styling-theming)[## Integration Patterns

Real-world examples](/frontend/wallet/integration-patterns)[## Wallet Overview

Back to wallet overview](/frontend/wallet/overview)

---

## [​](#faq) FAQ

Do I need to sync data to my database?

No, it’s optional. nekuda stores this data and your backend SDK can retrieve it. Use callbacks if you need this data elsewhere in your app.

Can users have multiple shipping addresses?

No, one shipping address per user in the wallet. For multiple addresses, build custom UI.

Are settings required for purchases?

No. Your AI agent can make purchases with just card data, but checkouts requiring contact/shipping info may fail without it.

[Payment Methods Tab](/frontend/wallet/payment-methods-tab)[CVV Management](/frontend/wallet/cvv-management)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)