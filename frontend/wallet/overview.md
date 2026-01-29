# Wallet Overview

**Package Update (v0.2.0):** The SDK has been renamed from `@fint/react-fint-js` to `@fint/wallet`.

```
npm install @fint/wallet
```

Update your imports:

```
import { WalletProvider, FintWallet } from '@fint/wallet';
```

All functionality remains the same—only the package name changed.

**First time using the Wallet?** Start with the Wallet Wizard for a quick, interactive walkthrough that shows you how to set up and use the wallet—ideal for visual learners or first-time users.

## Data Collected by the Wallet

The wallet organizes user data into three main groups:

1. **Payment Methods** - Credit/debit cards with billing addresses (tokenized, PCI-compliant)
2. **Contact Information** - Name, email, phone number
3. **Shipping Details** - Full shipping address

This structure gives your AI agent a complete set of credentials to handle purchases across different merchant sites without requiring users to re-enter information.

**What You’ll Learn**

In this guide, you’ll learn:

* Three integration approaches (Prebuilt, Styled, Custom)
* How to set up `FintWallet` in 3 minutes
* When to use FintWallet vs FintCollectForm
* Component props and customization options
* How to access payment method metadata with `useWallet()`

**Time to complete:** 10 minutes

## Choose Your Integration Approach

The Fint React SDK provides three ways to integrate payment collection into your application. Choose based on your needs:

- [Prebuilt Wallet](#prebuilt-wallet) — Complete wallet component with all features included. Recommended for most applications. **Best for:** Getting started quickly with full functionality
- [Styled Wallet](#styled-wallet) — Same functionality as prebuilt, with complete control over appearance and theming. **Best for:** Matching your existing design system
- [Custom Integration](#custom-integration) — Standalone collection form for guest checkouts and custom flows. **Best for:** Guest checkout without wallet UI

### Component Hierarchy

The Fint React SDK provides components at different levels of abstraction:

- **FintWallet** (highest level): Complete interface with payment methods management, contact info, and shipping address
- **FintCollectForm** (mid level): Standalone card collection form for custom onboarding or checkout flows
- **Individual Components** (lowest level): Field-level components (CardNumber, CVV, ExpiryDate) for complete control over layout and UX

---

## Prebuilt Wallet

`FintWallet` provides a complete wallet interface with payment methods, contact info, and shipping address management.

**When to use:**

* User account or settings pages requiring full wallet functionality
* Minimizing development time with pre-built UI

**Security Model:** Card data is tokenized on collection and stored server-side. Your frontend never has access to full card numbers or CVVs. Backend SDK retrieves actual card details using your secret API key when your agent needs to complete a purchase.

### Frontend-Backend Flow

**Key Points:**

* Frontend uses `publicKey` (collection only)
* Backend uses `secretKey` (retrieval only)
* Same `userId` required on both sides

---

## When to Use FintWallet

**Use FintWallet when you need:**

* Complete payment method management (add, edit, delete cards)
* Contact and shipping information management
* Full wallet UI for user account/settings pages
* Default card selection

**Use FintCollectForm when you need:**

* Minimal card collection without the wallet UI
* Guest checkout flows
* One-time payment collection
* Simple “add payment method” without managing multiple cards

**They work together:** FintWallet uses FintCollectForm internally for the “Add Card” flow. You can control which sections show in that flow using `collectFormVisibleSections` and `collectFormCollectionData` props on FintWallet. See [Collection Form](collect-form.md) for section control details.

**For custom styling:**

* Use themed mode with pre-built themes (light, dark, minimal)
* Apply custom styles via props
* See [Styling & Theming](styling-theming.md)

---

## Quick Start

```
npm install @fint/wallet
```

```
import { WalletProvider, FintWallet } from '@fint/wallet';

function UserSettings() {
  const userId = currentUser.id; // Your user's ID

  return (
    <WalletProvider publicKey="pk_test_..." userId={userId}>
      <FintWallet />
    </WalletProvider>
  );
}
```

Get your public key from app.fint.io. Users can now save and manage payment methods. Your backend can retrieve them via the backend SDK.

---

## Styled Wallet

Use the same `FintWallet` component with full control over styling and appearance.
**Styling options:**

* **Themed mode:** Choose from light, dark, or minimal themes
* **Custom mode:** Override specific style properties
* **Headless mode:** Provide your own CSS entirely

**When to use:**

* Need to match your existing design system
* Have specific brand requirements
* Want the functionality without the default appearance

**Implementation:** See the [Styling & Theming](styling-theming.md) guide for complete details on customization options.

---

## Custom Integration

For applications with specific requirements beyond the wallet UI:**`FintCollectForm` Component:**

* Standalone card collection form without wallet UI
* Flexible section control (contact, shipping, payment, billing)
* Choose which sections to show and which to send as hidden data
* Handles card tokenization securely

**When to use:**

* Guest checkout flows without saved cards
* Adding payment method for existing users
* Custom onboarding requiring only card collection
* Integration with existing payment UI

**Key features:**

* Control visible sections via `visibleSections` prop
* Send hidden data via `collectionData` prop
* Automatic phone number normalization to E.164 format
* Built-in validation with error handling

See [Collection Form](collect-form.md) for complete documentation and examples.

---

## Key Concepts

### `userId`

Your user’s unique identifier from your system (e.g., database ID). Must be consistent across frontend and backend. Fint doesn’t generate this - you provide it.

### `publicKey`

Your public API key (`pk_test_...` or `pk_live_...`) from app.fint.io. Safe to use in frontend code. Only allows card collection, not retrieval.
Never use your secret key (`sk_*`) in frontend code - it’s for backend only.

---

## Technical Architecture

**Provider Requirements:**

* `WalletProvider` must wrap `FintWallet`
* Provides authentication context for all API calls
* `userId` links cards to your user system

---

## Accessing Payment Method Metadata

Use `useWallet()` to access non-sensitive card metadata in your React components:

```
import { useWallet } from '@fint/wallet';

function Dashboard() {
  const wallet = useWallet();
  const defaultCard = wallet.payments.list.find(pm => pm.isDefault);

  return (
    <div>
      <p>{wallet.payments.list.length} cards saved</p>
      {defaultCard && (
        <p>Default: •••• {defaultCard.lastFourDigits}</p>
      )}
    </div>
  );
}
```

**Available fields:** `id`, `lastFourDigits`, `expiryDate`, `cardType`, `cardHolderName`, `isDefault`, `isCvvValid`, `billingAddress`, timestamps.
Full card numbers and CVVs are never exposed. Backend SDK only.

---

## Component Props Reference

### `<WalletProvider>`

Required wrapper that provides authentication context for all wallet operations.

[​](#param-public-key)

publicKey

string

required

Your Fint **public API key** from the Fint Portal. Safe to use in client-side code. Format: `pk_test_...` or `pk_live_...`

[​](#param-user-id)

userId

string

required

**Your user’s unique identifier** from your system. This links saved payment methods to your users. Can be your database user ID, customer ID, or any stable identifier you manage.

[​](#param-debug)

debug

boolean

default:"false"

Enable debug logging for troubleshooting API calls and iframe communication.

### `<FintWallet>`

The main wallet component. All props are optional.

[​](#param-mode)

mode

'themed' | 'headless' | 'custom'

default:"'themed'"

Styling mode:

* `themed`: Use pre-built themes (light, dark, minimal)
* `headless`: No styling, full control over appearance
* `custom`: Apply partial style overrides

[​](#param-theme)

theme

'light' | 'dark' | 'minimal'

default:"'light'"

Pre-built theme to use when `mode="themed"`.

[​](#param-theme-config)

themeConfig

Partial<ThemeContract>

Override theme tokens for brand customization. Changes cascade throughout the wallet.**Example:**

```
<FintWallet
  themeConfig={{
    accent: { primary: '#7C3AED' },
    typography: { fontFamily: { base: 'Inter, sans-serif' } },
    spacing: { md: '1rem' },
    radii: { md: 8 }
  }}
/>
```

See [Styling & Theming](styling-theming.md) for all available tokens.

[​](#param-class-name)

className

string

CSS class name for the wallet container.

[​](#param-styles)

styles

Partial<WalletStyles>

Component-level style overrides for fine-grained control. Use this to customize specific UI elements (tabs, cards, buttons, etc.).** Use with themeConfig:**

```
<FintWallet
  themeConfig={{ accent: { primary: '#7C3AED' } }}  // Global brand color
  styles={{ container: { maxWidth: '900px' } }}      // Specific override
/>
```

See [Styling & Theming](styling-theming.md) for all style properties.

[​](#param-default-contact)

defaultContact

Partial<IdentityData>

Pre-fill contact information when user first opens Settings tab.** Fields**: `firstName`, `lastName`, `email`, `phone`

[​](#param-default-shipping)

defaultShipping

Partial<AddressData>

Pre-fill shipping address when user first opens Settings tab.** Fields**: `addressLine1`, `addressLine2`, `city`, `state`, `zipCode`, `country`

[​](#param-default-billing)

defaultBilling

Partial<AddressData>

Pre-fill billing address when user adds a new card.** Fields**: `addressLine1`, `addressLine2`, `city`, `state`, `zipCode`, `country`

[​](#param-default-collect-values)

defaultCollectValues

Partial<CollectFormWithBillingData>

Pre-fill the entire “Add Card” form with contact, shipping, and billing details.

[​](#param-render-empty-state)

renderEmptyState

() => ReactNode

Custom component to render when user has no saved payment methods.

[​](#param-on-error)

onError

(error: Error) => void

Callback when any operation fails (API errors, network issues, validation failures).

[​](#param-on-contact-change)

onContactChange

(data: IdentityData) => void

Callback when user updates contact information in Settings tab.

[​](#param-on-shipping-change)

onShippingChange

(data: AddressData) => void

Callback when user updates shipping address in Settings tab.

[​](#param-show-settings)

showSettings

boolean

default:"true"

Control whether to show the Settings tab. When `false`, only the Payment Methods view is shown without tabs. Useful when you only need card management without contact/shipping information.

[​](#param-collect-form-visible-sections)

collectFormVisibleSections

CollectionSection[]

Control which sections to show when users click “Add Card”. By default, all sections are shown.

**Use case:** Streamline the add card flow for existing users by showing only payment and billing sections.

**Example:**

```
import { CollectionSection } from '@fint/wallet';

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

See [Collection Form](collect-form.md) for all available sections.

[​](#param-collect-form-collection-data)

collectFormCollectionData

CollectionData

Provide data for sections hidden from the “Add Card” form. Use with `collectFormVisibleSections` to skip collecting information you already have.** Fields**: `contactInfo`, `shippingAddress`, `billingAddress`, `cardHolderName`, `customData`** Example:**Copy

```
<FintWallet
  collectFormCollectionData={{
    contactInfo: {
      firstName: user.firstName,
      lastName: user.lastName,
      email: user.email,
      phone: user.phone
    },
    shippingAddress: user.shippingAddress
  }}
/>
```

---

## Advanced Example

### Streamlined Add Card Flow

For existing users, simplify the “Add Card” experience by showing only payment and billing sections:

```
import { WalletProvider, FintWallet, CollectionSection } from '@fint/wallet';

function PaymentSettings() {
  const { user } = useAuth();

  return (
    <WalletProvider publicKey="pk_test_..." userId={user.id}>
      <FintWallet
        theme="light"
        // Simplify "Add Card" - only show payment + billing
        collectFormVisibleSections={[
          CollectionSection.Payment,
          CollectionSection.Billing
        ]}
        collectFormCollectionData={{
          contactInfo: {
            firstName: user.firstName,
            lastName: user.lastName,
            email: user.email,
            phone: user.phone
          },
          shippingAddress: user.shippingAddress
        }}
        // Pre-fill Settings tab
        defaultContact={{
          firstName: user.firstName,
          email: user.email
        }}
        onError={(error) => console.error(error)}
      />
    </WalletProvider>
  );
}
```** Result**: When users click “Add Card”, they only fill in payment and billing details. Contact and shipping info is sent automatically from your system.
See [Integration Patterns](integration-patterns.md) for more examples.

---

## Frontend to Backend Flow

```
// Frontend: User adds card
<WalletProvider publicKey="pk_test_..." userId="user_123">
  <FintWallet />
</WalletProvider>
```

```
# Backend: Retrieve card when needed
from fint import FintClient, MandateData

client = FintClient.from_env()
user = client.user("user_123")  # Same userId

mandate_resp = user.create_mandate(MandateData(...))
reveal_resp = user.request_card_reveal_token(mandate_resp.mandate_id)
card = user.reveal_card_details(reveal_resp.reveal_token)

# AI agent now has: card.card_number, card.cvv, card.card_expiry_date
```

Frontend stores cards (tokenized). Backend retrieves cards (full details) for your AI agent. See [Quickstart](../../fint-sdk/Quickstart.md) for complete example.

---

## Security & PCI Compliance

Card inputs render in secure iframe at `collect.fint.io` - your frontend cannot access them. Wallet only shows tokenized data (last 4 digits, expiry, name). Full card numbers and CVVs are never transmitted to your frontend.
**Key separation:**

* **Public key** (`pk_*`): Frontend collection only
* **Secret key** (`sk_*`): Backend retrieval only

HTTPS required in production. This design keeps you out of PCI scope.

---

## What’s Next?

- [Payment Methods Tab](payment-methods-tab.md) — Learn how users manage saved cards
- [Settings Tab](settings-tab.md) — Understand contact and shipping management
- [Styling & Theming](styling-theming.md) — Customize appearance to match your brand
- [Integration Patterns](integration-patterns.md) — See real-world integration examples

---

## FAQ

Can I use FintWallet without WalletProvider?

No. `WalletProvider` provides authentication context (`publicKey` and `userId`) required for API requests.

What userId should I use?

Your database user ID. Must be unique per user and stable across sessions.

Can frontend access full card numbers?

No. Only backend SDK can retrieve full card details. This maintains PCI compliance.

How do I check if user has saved cards?

`const hasCards = useWallet().payments.list.length > 0`

Is it mobile-responsive?

Yes, automatically adapts to mobile screens.
