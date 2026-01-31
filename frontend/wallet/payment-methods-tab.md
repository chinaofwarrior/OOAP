# Payment Methods Tab

## Overview

The Payment Methods tab lets users add, edit, and manage their saved cards. Your AI agent uses the default card when making purchases.

**Default Card:** When your backend retrieves payment details, it gets the default card. This is either:

* The card the user marked as default, OR
* The most recently added card if no default is set

---

## Quick Start

```
import { WalletProvider, FintWallet } from '@fint/wallet';

<WalletProvider publicKey="pk_test_..." userId={userId}>
  <FintWallet theme="light" />
</WalletProvider>
```

---

## Adding Cards

### Pre-fill the Add Card Form

Reduce friction by pre-filling information you already have:

```
<FintWallet
  defaultContact={{
    firstName: user.firstName,
    lastName: user.lastName,
    email: user.email,
    phone: user.phone
  }}
  defaultBilling={{
    addressLine1: user.billingAddress.street,
    city: user.billingAddress.city,
    state: user.billingAddress.state,
    zipCode: user.billingAddress.zip,
    country: 'United States'
  }}
/>
```

### Streamline for Existing Users

Show only payment and billing fields if you already have contact and shipping info:

```
import { CollectionSection } from '@fint/wallet';

{% raw %}
```
<FintWallet
  collectFormVisibleSections={[
    CollectionSection.Payment,
    CollectionSection.Billing
  ]}
  collectFormCollectionData={{
    contactInfo: user.contact,
    shippingAddress: user.shipping
  }}
/>
```
{% endraw %}
```

See [Collection Form](collect-form.md) for more details on section control.

---

## Editing Cards

Users can edit:

* **Cardholder name** - Updates the name on the card
* **Billing address** - Updates where the card is billed

Card number, expiry, and CVV cannot be edited for security. Users need to add a new card instead.

---

## Setting Default Card

Users set a default by checking “Set as default payment method” on any card.

**Why it matters:** Your AI agent uses the default card for purchases. Only one card can be default at a time.

**Backend retrieval:**

```
# Your AI agent gets the default card
card = user_context.reveal_card_details(reveal_token)
```

---

## Deleting Cards

Users can delete any saved card. If they delete the default card, the most recent remaining card becomes the new default automatically.

---

## Custom Empty State

Show your own message when users have no cards:

```
<FintWallet
  renderEmptyState={() => (
    <div style={{ textAlign: 'center', padding: '3rem' }}>
      <h3>No payment methods yet</h3>
      <p>Add a card so your AI assistant can make purchases.</p>
    </div>
  )}
/>
```

**Use for:** Onboarding messaging, value propositions, or branding.

---

## Accessing Card Data

Check card information in your app using `useWallet()`:

```
import { useWallet } from '@fint/wallet';

function Dashboard() {
  const wallet = useWallet();
  const cards = wallet.payments.list;
  const defaultCard = cards.find(c => c.isDefault);

  return (
    <div>
      <p>{cards.length} cards saved</p>
      {defaultCard && (
        <p>Default: {defaultCard.cardType} •••• {defaultCard.lastFourDigits}</p>
      )}
    </div>
  );
}
```

**Available fields:** `id`, `lastFourDigits`, `expiryDate`, `cardType`, `cardHolderName`, `isDefault`, `billingAddress`

This is metadata only - no full card numbers or CVVs. Only your backend SDK can retrieve sensitive details.

---

## Example: Payment Settings Page

```
import { WalletProvider, FintWallet } from '@fint/wallet';

function PaymentSettingsPage() {
  const { user } = useAuth();

  return (
    <div>
      <h1>Payment Methods</h1>
      <p>Manage cards for your AI shopping assistant</p>

      <WalletProvider publicKey="pk_test_..." userId={user.id}>
        <FintWallet
          theme="light"
          defaultBilling={user.billingAddress}
          renderEmptyState={() => (
            <div>
              <h3>Add your first payment method</h3>
              <p>Your AI assistant needs a card to make purchases.</p>
            </div>
          )}
          onError={(error) => console.error('Wallet error:', error)}
        />
      </WalletProvider>
    </div>
  );
}
```

---

## What’s Next?

- [Settings Tab](settings-tab.md) — Manage contact info and shipping address
- [Collection Form](collect-form.md) — Customize the add card flow
- [Styling & Theming](styling-theming.md) — Customize appearance
- [Integration Patterns](integration-patterns.md) — Real-world examples

---

## FAQ

What happens if a user deletes their default card?

The most recent remaining card automatically becomes the new default.

How do I know which card my AI agent will use?

Your AI agent uses the default card. Check `useWallet().payments.list` and find the card where `isDefault` is `true`.

Can I get notified when a user adds or deletes a card?

Use `useWallet()` to access the current card list in your components. The list updates automatically when cards change.
