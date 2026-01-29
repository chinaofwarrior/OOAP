# Collection Form

## Overview

`FintCollectForm` is a flexible payment collection form that lets you choose exactly what information to collect from users. Use it for guest checkouts, adding payment methods, or any custom flow where you need payment information.

**What You’ll Learn ** In this guide, you’ll learn:

* When to use FintCollectForm vs FintWallet
* How to collect only payment details (skip contact/shipping)
* How to use existing user data instead of re-collecting it
* How this component powers the “Add Card” flow in FintWallet
* Customizing the collection experience

**Time to complete:** 5 minutes **FintCollectForm powers FintWallet** : When users click “Add Card” in FintWallet, they’re using this component. The props you learn here also work when customizing the wallet’s card collection flow.

---

## When to Use This Component

**Use FintCollectForm when you need:**

* Simple payment collection without managing multiple cards
* Guest checkout flows
* One-time payment collection
* Custom onboarding without wallet UI
* Minimal form - just collect payment, nothing else

**Use FintWallet when you need:**

* Payment method management (view, add, edit, delete cards)
* Contact and shipping information management
* Default card selection
* Full wallet UI for user accounts

**Key difference** : FintCollectForm is the building block for collecting payment information. FintWallet is the complete experience for managing payment methods and user information. The wallet uses this collection form internally when users click “Add Card”.
See [Wallet Overview](overview.md) for the complete wallet component.

---

## What You Can Collect

The form can collect four types of information:

1. **Contact Information** - Name, email, phone number
2.**Shipping Address** - Full shipping address
3.**Payment Details** - Card information (always required)
4.**Billing Address** - Billing address for the card **You choose which ones to show.** If you already have contact or shipping info for your user, skip those sections and just collect payment details.

---

## Quick Start: Guest Checkout

Collect everything from a first-time user:

```
import { WalletProvider, FintCollectForm } from '@fint/wallet';

function GuestCheckout() {
  return (
    <WalletProvider publicKey="pk_test_..." userId="guest-123">
      <FintCollectForm
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

## Collect Only Payment Details

Your user already has an account with contact and shipping info. Just collect their payment method:

```
import { FintCollectForm, CollectionSection } from '@fint/wallet';

<FintCollectForm
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
```**What happens:**

* User sees only payment and billing forms
* Contact and shipping data from `collectionData` is automatically included
* Response contains all four types of data (contact, shipping, billing, payment)

**Common use case:** “Add Payment Method” button in your app settings.

---

## Available Sections

Control what to show using `visibleSections`:

```
import { CollectionSection } from '@fint/wallet';

CollectionSection.Contact   // Name, email, phone
CollectionSection.Shipping  // Shipping address
CollectionSection.Payment   // Card details (always required)
CollectionSection.Billing   // Billing address
```**Example combinations:**

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

## Using Existing User Data

When you skip sections, provide that data via `collectionData`:

```
<FintCollectForm
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

## Pre-filling Visible Fields

Pre-populate fields that the user will see:

```
<FintCollectForm
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

## Customizing Appearance

### Pre-built Themes

```
// Dark theme
<FintCollectForm theme="dark" />

// Light theme (default)
<FintCollectForm theme="light" />

// Minimal theme
<FintCollectForm theme="minimal" />
```

### Brand Customization with Theme Tokens

Apply your brand colors and typography consistently:

```
<FintCollectForm
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

### Component-Specific Styling

For fine-grained control, use the `styles` prop:

```
<FintCollectForm
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

See [Styling & Theming](styling-theming.md) for all customization options.

---

## Controlling Collection in FintWallet

When users click “Add Card” in FintWallet, they see this collection form. Customize which sections to show:

```
import { FintWallet, CollectionSection } from '@fint/react-fint-js';

<FintWallet
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

## Common Scenarios

### Scenario 1: First-Time User Onboarding

```
function Onboarding() {
  return (
    <WalletProvider publicKey="pk_test_..." userId={newUser.id}>
      <h2>Add a payment method</h2>
      <FintCollectForm
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

### Scenario 2: Guest Checkout

```
function Checkout() {
  return (
    <WalletProvider publicKey="pk_test_..." userId="guest-user">
      <FintCollectForm
        onSuccess={(data) => completeOrder(data)}
      />
    </WalletProvider>
  );
}
```

### Scenario 3: Add Payment Method

```
function AddPaymentMethod() {
  const { user } = useAuth();

  return (
    <WalletProvider publicKey="pk_test_..." userId={user.id}>
      <FintCollectForm
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

## Key Props

[​](#param-visible-sections)

visibleSections

CollectionSection[]

default:"All sections"

Choose which sections to show. Sections appear in the order you specify.** Example:**

```
visibleSections={[CollectionSection.Payment, CollectionSection.Billing]}
```

[​](#param-collection-data)

collectionData

CollectionData

Data for sections you’re not showing. Gets sent to API automatically.** Fields:** `contactInfo`, `shippingAddress`, `billingAddress`, `cardHolderName`, `customData`

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

Custom style overrides. See [Styling & Theming](styling-theming.md).

[​](#param-google-api-key)

googleApiKey

string

Google Places API key for address autocomplete.

---

## Error Handling

Handle errors to guide users:

```
<FintCollectForm
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

## What’s Next?

- [Wallet Overview](overview.md) — Full wallet component for account pages
- [Integration Patterns](integration-patterns.md) — Real-world examples and flows
- [Styling & Theming](styling-theming.md) — Customize appearance
- [Backend SDK](../../fint-sdk/getting-started.md) — Retrieve payment details securely

---

## FAQ

Can I skip showing payment details?

No. Payment section must always be visible because it contains secure card fields. You can skip contact, shipping, or billing sections.

What if I skip a section?

Provide that data via `collectionData`. It’s automatically sent to the API with the collected data.

Can I change the section order?

Yes. Sections appear in the order you list them in `visibleSections`.

How is this different from FintWallet?

FintCollectForm is for one-time collection. FintWallet manages saved payment methods with full CRUD operations. The wallet uses this component internally when users add cards.

Can I use this for returning users?

Yes. Show only payment + billing sections, and pass their existing contact/shipping data via `collectionData`.

Where does the collected data go?

Payment information is securely tokenized and stored. Your backend retrieves it using the Fint SDK when your AI agent needs to complete a purchase.
