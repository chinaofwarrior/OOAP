# Settings Tab

## Overview

The Settings tab lets users save their contact info and shipping address. Your AI agent uses this information when filling out checkout forms on merchant sites.

Saved settings ensure your AI agent fills forms consistently across all purchases.

---

## Quick Start

```
import { WalletProvider, NekudaWallet } from '@nekuda/wallet';

<WalletProvider publicKey="pk_test_..." userId={userId}>
  <NekudaWallet theme="light" />
</WalletProvider>
```

---

## Contact Information

### Pre-fill Contact Data

Reduce friction by pre-filling information from your user database:

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

### Sync Changes to Your Database

Get notified when users update their contact info:

```
<NekudaWallet
  defaultContact={user.contact}
  onContactChange={(contactData) => {
    // Update your database
    updateUser(user.id, { contact: contactData });
  }}
/>
```

**Fields** : `firstName`, `lastName`, `email`, `phone` (optional)

---

## Shipping Address

### Pre-fill Shipping Data

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

### Sync Changes

```
<NekudaWallet
  defaultShipping={user.shippingAddress}
  onShippingChange={(shippingData) => {
    updateUser(user.id, { shipping: shippingData });
  }}
/>
```

**Fields** : `addressLine1`, `addressLine2` (optional), `city`, `state`, `zipCode`, `country`

---

## Accessing Settings in Your App

Display user settings elsewhere in your app:

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

## Hide Settings Tab

If you don’t need contact and shipping management, hide the Settings tab:

```
<NekudaWallet showSettings={false} />
```

This shows only the Payment Methods view.

---

## What’s Next?

[## Payment Methods Tab

Manage saved cards](payment-methods-tab.md)[## Styling & Theming

Customize appearance](styling-theming.md)[## Integration Patterns

Real-world examples](integration-patterns.md)[## Wallet Overview

Back to wallet overview](overview.md)

---

## FAQ

Do I need to sync data to my database?

No, it’s optional. nekuda stores this data and your backend SDK can retrieve it. Use callbacks if you need this data elsewhere in your app.

Can users have multiple shipping addresses?

No, one shipping address per user in the wallet. For multiple addresses, build custom UI.

Are settings required for purchases?

No. Your AI agent can make purchases with just card data, but checkouts requiring contact/shipping info may fail without it.
