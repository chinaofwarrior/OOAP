# Collection Form

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Frontend SDK

Collection Form

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
* [When to Use This Component](#when-to-use-this-component)
* [What You Can Collect](#what-you-can-collect)
* [Quick Start: Guest Checkout](#quick-start%3A-guest-checkout)
* [Collect Only Payment Details](#collect-only-payment-details)
* [Available Sections](#available-sections)
* [Using Existing User Data](#using-existing-user-data)
* [Pre-filling Visible Fields](#pre-filling-visible-fields)
* [Customizing Appearance](#customizing-appearance)
* [Pre-built Themes](#pre-built-themes)
* [Brand Customization with Theme Tokens](#brand-customization-with-theme-tokens)
* [Component-Specific Styling](#component-specific-styling)
* [Controlling Collection in NekudaWallet](#controlling-collection-in-nekudawallet)
* [Common Scenarios](#common-scenarios)
* [Scenario 1: First-Time User Onboarding](#scenario-1%3A-first-time-user-onboarding)
* [Scenario 2: Guest Checkout](#scenario-2%3A-guest-checkout)
* [Scenario 3: Add Payment Method](#scenario-3%3A-add-payment-method)
* [Key Props](#key-props)
* [Error Handling](#error-handling)
* [What’s Next?](#what%E2%80%99s-next)
* [FAQ](#faq)

Frontend SDK

# Collection Form

Copy page

Collect payment information for guest checkout and custom flows

Copy page

## [​](#overview) Overview

`NekudaCollectForm` is a flexible payment collection form that lets you choose exactly what information to collect from users. Use it for guest checkouts, adding payment methods, or any custom flow where you need payment information.

**What You’ll Learn**In this guide, you’ll learn:

* When to use NekudaCollectForm vs NekudaWallet
* How to collect only payment details (skip contact/shipping)
* How to use existing user data instead of re-collecting it
* How this component powers the “Add Card” flow in NekudaWallet
* Customizing the collection experience

**Time to complete:** 5 minutes

**NekudaCollectForm powers NekudaWallet**: When users click “Add Card” in NekudaWallet, they’re using this component. The props you learn here also work when customizing the wallet’s card collection flow.

---

## [​](#when-to-use-this-component) When to Use This Component

**Use NekudaCollectForm when you need:**

* Simple payment collection without managing multiple cards
* Guest checkout flows
* One-time payment collection
* Custom onboarding without wallet UI
* Minimal form - just collect payment, nothing else

**Use NekudaWallet when you need:**

* Payment method management (view, add, edit, delete cards)
* Contact and shipping information management
* Default card selection
* Full wallet UI for user accounts

**Key difference**: NekudaCollectForm is the building block for collecting payment information. NekudaWallet is the complete experience for managing payment methods and user information. The wallet uses this collection form internally when users click “Add Card”.
See [Wallet Overview](/frontend/wallet/overview) for the complete wallet component.


---

## [​](#what-you-can-collect) What You Can Collect

The form can collect four types of information:

1. **Contact Information** - Name, email, phone number
2. **Shipping Address** - Full shipping address
3. **Payment Details** - Card information (always required)
4. **Billing Address** - Billing address for the card

**You choose which ones to show.** If you already have contact or shipping info for your user, skip those sections and just collect payment details.


---

## [​](#quick-start:-guest-checkout) Quick Start: Guest Checkout

Collect everything from a first-time user:

Copy

Ask AI

```
import { WalletProvider, NekudaCollectForm } from '@nekuda/wallet';

function GuestCheckout() {
  return (
    <WalletProvider publicKey="pk_test_..." userId="guest-123">
      <NekudaCollectForm
        onSuccess={(data) => {
          // You get: contact, shipping, billing, and payment info
          processOrder(data);
        }}
      />
    </WalletProvider>
  );
}
```

That’s it. The form shows all four sections by default.


---

## [​](#collect-only-payment-details) Collect Only Payment Details

Your user already has an account with contact and shipping info. Just collect their payment method:

Copy

Ask AI

```
import { NekudaCollectForm, CollectionSection } from '@nekuda/wallet';

<NekudaCollectForm
  visibleSections={[CollectionSection.Payment, CollectionSection.Billing]}
  collectionData={{
    contactInfo: {
      firstName: user.firstName,
      lastName: user.lastName,
      email: user.email,
      phone: user.phone
    },
    shippingAddress: user.shippingAddress
  }}
  onSuccess={(data) => {
    alert('Payment method added!');
  }}
/>
```

**What happens:**

* User sees only payment and billing forms
* Contact and shipping data from `collectionData` is automatically included
* Response contains all four types of data (contact, shipping, billing, payment)

**Common use case:** “Add Payment Method” button in your app settings.


---

## [​](#available-sections) Available Sections

Control what to show using `visibleSections`:

Copy

Ask AI

```
import { CollectionSection } from '@nekuda/wallet';

CollectionSection.Contact   // Name, email, phone
CollectionSection.Shipping  // Shipping address
CollectionSection.Payment   // Card details (always required)
CollectionSection.Billing   // Billing address
```

**Example combinations:**

Copy

Ask AI

```
// Guest checkout - show everything (default)
visibleSections={[
  CollectionSection.Contact,
  CollectionSection.Shipping,
  CollectionSection.Payment,
  CollectionSection.Billing
]}

// Add payment method - just payment + billing
visibleSections={[CollectionSection.Payment, CollectionSection.Billing]}

// Custom order - billing before payment
visibleSections={[CollectionSection.Billing, CollectionSection.Payment]}
```

Payment section is always required - it contains secure card fields that can’t be passed as data.

---

## [​](#using-existing-user-data) Using Existing User Data

When you skip sections, provide that data via `collectionData`:

Copy

Ask AI

```
<NekudaCollectForm
  visibleSections={[CollectionSection.Payment, CollectionSection.Billing]}
  collectionData={{
    contactInfo: {
      firstName: user.firstName,
      lastName: user.lastName,
      email: user.email,
      phone: user.phone
    },
    shippingAddress: {
      addressLine1: user.address.street,
      city: user.address.city,
      state: user.address.state,
      zipCode: user.address.zip,
      country: 'US'
    }
  }}
/>
```

This data is sent to the API along with what the user fills in.


---

## [​](#pre-filling-visible-fields) Pre-filling Visible Fields

Pre-populate fields that the user will see:

Copy

Ask AI

```
<NekudaCollectForm
  defaultValues={{
    firstName: 'Jane',
    email: '[email protected]',
    addressLine1: '123 Main St',
    city: 'New York'
  }}
/>
```

User can edit these values before submitting.

Card fields (number, CVV, expiry) cannot be pre-filled for security.

---

## [​](#customizing-appearance) Customizing Appearance

### [​](#pre-built-themes) Pre-built Themes

Copy

Ask AI

```
// Dark theme
<NekudaCollectForm theme="dark" />

// Light theme (default)
<NekudaCollectForm theme="light" />

// Minimal theme
<NekudaCollectForm theme="minimal" />
```

### [​](#brand-customization-with-theme-tokens) Brand Customization with Theme Tokens

Apply your brand colors and typography consistently:

Copy

Ask AI

```
<NekudaCollectForm
  mode="themed"
  theme="light"
  themeConfig={{
    accent: {
      primary: '#7C3AED'           // Your brand color
    },
    typography: {
      fontFamily: {
        base: 'Inter, sans-serif'  // Your brand font
      }
    }
  }}
/>
```

### [​](#component-specific-styling) Component-Specific Styling

For fine-grained control, use the `styles` prop:

Copy

Ask AI

```
<NekudaCollectForm
  mode="themed"
  theme="light"
  themeConfig={{
    accent: { primary: '#7C3AED' }  // Brand color
  }}
  styles={{
    button: { padding: '14px 28px' },  // Larger button
    input: { fontSize: '16px' }        // Larger text
  }}
/>
```

See [Styling & Theming](/frontend/wallet/styling-theming) for all customization options.


---

## [​](#controlling-collection-in-nekudawallet) Controlling Collection in NekudaWallet

When users click “Add Card” in NekudaWallet, they see this collection form. Customize which sections to show:

Copy

Ask AI

```
import { NekudaWallet, CollectionSection } from '@nekuda/react-nekuda-js';

<NekudaWallet
  // Show only payment + billing when adding cards
  collectFormVisibleSections={[
    CollectionSection.Payment,
    CollectionSection.Billing
  ]}
  // Provide contact and shipping automatically
  collectFormCollectionData={{
    contactInfo: {
      firstName: user.firstName,
      lastName: user.lastName,
      email: user.email,
      phone: user.phone
    },
    shippingAddress: user.shippingAddress
  }}
  // Or pre-fill the form
  defaultCollectValues={{
    firstName: user.firstName,
    email: user.email
  }}
/>
```

This gives existing users a streamlined “Add Payment Method” experience - they only fill in payment and billing details.


---

## [​](#common-scenarios) Common Scenarios

### [​](#scenario-1:-first-time-user-onboarding) Scenario 1: First-Time User Onboarding

Copy

Ask AI

```
function Onboarding() {
  return (
    <WalletProvider publicKey="pk_test_..." userId={newUser.id}>
      <h2>Add a payment method</h2>
      <NekudaCollectForm
        visibleSections={[CollectionSection.Payment, CollectionSection.Billing]}
        collectionData={{
          contactInfo: {
            firstName: newUser.firstName,
            email: newUser.email
          }
        }}
        onSuccess={() => navigate('/dashboard')}
      />
    </WalletProvider>
  );
}
```

### [​](#scenario-2:-guest-checkout) Scenario 2: Guest Checkout

Copy

Ask AI

```
function Checkout() {
  return (
    <WalletProvider publicKey="pk_test_..." userId="guest-user">
      <NekudaCollectForm
        onSuccess={(data) => completeOrder(data)}
      />
    </WalletProvider>
  );
}
```

### [​](#scenario-3:-add-payment-method) Scenario 3: Add Payment Method

Copy

Ask AI

```
function AddPaymentMethod() {
  const { user } = useAuth();

  return (
    <WalletProvider publicKey="pk_test_..." userId={user.id}>
      <NekudaCollectForm
        visibleSections={[CollectionSection.Payment, CollectionSection.Billing]}
        collectionData={{
          contactInfo: user.contact,
          shippingAddress: user.shipping
        }}
        onSuccess={() => alert('Payment method added!')}
      />
    </WalletProvider>
  );
}
```

---

## [​](#key-props) Key Props

[​](#param-visible-sections)

visibleSections

CollectionSection[]

default:"All sections"

Choose which sections to show. Sections appear in the order you specify.**Example:**

Copy

Ask AI

```
visibleSections={[CollectionSection.Payment, CollectionSection.Billing]}
```

[​](#param-collection-data)

collectionData

CollectionData

Data for sections you’re not showing. Gets sent to API automatically.**Fields:** `contactInfo`, `shippingAddress`, `billingAddress`, `cardHolderName`, `customData`

[​](#param-default-values)

defaultValues

object

Pre-fill visible form fields. User can edit before submitting.

[​](#param-on-success)

onSuccess

(data) => void

required

Called when collection succeeds. Returns contact, shipping, billing, and payment info.

[​](#param-on-error)

onError

(error) => void

Called when collection fails (validation errors, network issues, etc).

[​](#param-theme)

theme

'light' | 'dark' | 'minimal'

default:"'light'"

Pre-built theme to use.

[​](#param-mode)

mode

'themed' | 'custom' | 'headless'

default:"'themed'"

Styling mode. Use `'custom'` to override specific styles.

[​](#param-styles)

styles

object

Custom style overrides. See [Styling & Theming](/frontend/wallet/styling-theming).

[​](#param-google-api-key)

googleApiKey

string

Google Places API key for address autocomplete.

---

## [​](#error-handling) Error Handling

Handle errors to guide users:

Copy

Ask AI

```
<NekudaCollectForm
  onError={(error) => {
    if (error.code === 'NETWORK_ERROR') {
      showMessage('Connection issue. Please try again.');
    } else if (error.code === 'CARD_DECLINED') {
      showMessage('Card declined. Try a different card.');
    } else {
      showMessage('Error occurred. Please try again.');
    }
  }}
/>
```

Validation errors appear inline automatically.


---

## [​](#what’s-next) What’s Next?

[## Wallet Overview

Full wallet component for account pages](/frontend/wallet/overview)[## Integration Patterns

Real-world examples and flows](/frontend/wallet/integration-patterns)[## Styling & Theming

Customize appearance](/frontend/wallet/styling-theming)[## Backend SDK

Retrieve payment details securely](/nekuda-sdk/getting-started)

---

## [​](#faq) FAQ

Can I skip showing payment details?

No. Payment section must always be visible because it contains secure card fields. You can skip contact, shipping, or billing sections.

What if I skip a section?

Provide that data via `collectionData`. It’s automatically sent to the API with the collected data.

Can I change the section order?

Yes. Sections appear in the order you list them in `visibleSections`.

How is this different from NekudaWallet?

NekudaCollectForm is for one-time collection. NekudaWallet manages saved payment methods with full CRUD operations. The wallet uses this component internally when users add cards.

Can I use this for returning users?

Yes. Show only payment + billing sections, and pass their existing contact/shipping data via `collectionData`.

Where does the collected data go?

Payment information is securely tokenized and stored. Your backend retrieves it using the nekuda SDK when your AI agent needs to complete a purchase.

[CVV Management](/frontend/wallet/cvv-management)[Styling & Theming](/frontend/wallet/styling-theming)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)