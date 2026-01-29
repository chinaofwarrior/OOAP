# Payment Methods Tab

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Frontend SDK

Payment Methods Tab

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
* [Adding Cards](#adding-cards)
* [Pre-fill the Add Card Form](#pre-fill-the-add-card-form)
* [Streamline for Existing Users](#streamline-for-existing-users)
* [Editing Cards](#editing-cards)
* [Setting Default Card](#setting-default-card)
* [Deleting Cards](#deleting-cards)
* [Custom Empty State](#custom-empty-state)
* [Accessing Card Data](#accessing-card-data)
* [Example: Payment Settings Page](#example%3A-payment-settings-page)
* [What’s Next?](#what%E2%80%99s-next)
* [FAQ](#faq)

Frontend SDK

# Payment Methods Tab

Copy page

Let users manage their saved payment methods

Copy page

## [​](#overview) Overview

The Payment Methods tab lets users add, edit, and manage their saved cards. Your AI agent uses the default card when making purchases.

**Default Card**: When your backend retrieves payment details, it gets the default card. This is either:

* The card the user marked as default, OR
* The most recently added card if no default is set

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

## [​](#adding-cards) Adding Cards

### [​](#pre-fill-the-add-card-form) Pre-fill the Add Card Form

Reduce friction by pre-filling information you already have:

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
  defaultBilling={{
    addressLine1: user.billingAddress.street,
    city: user.billingAddress.city,
    state: user.billingAddress.state,
    zipCode: user.billingAddress.zip,
    country: 'United States'
  }}
/>
```

### [​](#streamline-for-existing-users) Streamline for Existing Users

Show only payment and billing fields if you already have contact and shipping info:

Copy

Ask AI

```
import { CollectionSection } from '@nekuda/wallet';

<NekudaWallet
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

See [Collection Form](/frontend/wallet/collect-form) for more details on section control.


---

## [​](#editing-cards) Editing Cards

Users can edit:

* **Cardholder name** - Updates the name on the card
* **Billing address** - Updates where the card is billed

Card number, expiry, and CVV cannot be edited for security. Users need to add a new card instead.

---

## [​](#setting-default-card) Setting Default Card

Users set a default by checking “Set as default payment method” on any card.
**Why it matters**: Your AI agent uses the default card for purchases. Only one card can be default at a time.
**Backend retrieval**:

Copy

Ask AI

```
# Your AI agent gets the default card
card = user_context.reveal_card_details(reveal_token)
```

---

## [​](#deleting-cards) Deleting Cards

Users can delete any saved card. If they delete the default card, the most recent remaining card becomes the new default automatically.


---

## [​](#custom-empty-state) Custom Empty State

Show your own message when users have no cards:

Copy

Ask AI

```
<NekudaWallet
  renderEmptyState={() => (
    <div style={{ textAlign: 'center', padding: '3rem' }}>
      <h3>No payment methods yet</h3>
      <p>Add a card so your AI assistant can make purchases.</p>
    </div>
  )}
/>
```

**Use for**: Onboarding messaging, value propositions, or branding.


---

## [​](#accessing-card-data) Accessing Card Data

Check card information in your app using `useWallet()`:

Copy

Ask AI

```
import { useWallet } from '@nekuda/wallet';

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

**Available fields**: `id`, `lastFourDigits`, `expiryDate`, `cardType`, `cardHolderName`, `isDefault`, `billingAddress`

This is metadata only - no full card numbers or CVVs. Only your backend SDK can retrieve sensitive details.

---

## [​](#example:-payment-settings-page) Example: Payment Settings Page

Copy

Ask AI

```
import { WalletProvider, NekudaWallet } from '@nekuda/wallet';

function PaymentSettingsPage() {
  const { user } = useAuth();

  return (
    <div>
      <h1>Payment Methods</h1>
      <p>Manage cards for your AI shopping assistant</p>

      <WalletProvider publicKey="pk_test_..." userId={user.id}>
        <NekudaWallet
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

## [​](#what’s-next) What’s Next?

[## Settings Tab

Manage contact info and shipping address](/frontend/wallet/settings-tab)[## Collection Form

Customize the add card flow](/frontend/wallet/collect-form)[## Styling & Theming

Customize appearance](/frontend/wallet/styling-theming)[## Integration Patterns

Real-world examples](/frontend/wallet/integration-patterns)

---

## [​](#faq) FAQ

What happens if a user deletes their default card?

The most recent remaining card automatically becomes the new default.

How do I know which card my AI agent will use?

Your AI agent uses the default card. Check `useWallet().payments.list` and find the card where `isDefault` is `true`.

Can I get notified when a user adds or deletes a card?

Use `useWallet()` to access the current card list in your components. The list updates automatically when cards change.

[Wallet Overview](/frontend/wallet/overview)[Settings Tab](/frontend/wallet/settings-tab)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)