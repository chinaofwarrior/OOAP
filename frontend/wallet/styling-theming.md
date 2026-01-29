# Styling & Theming

## Overview

The `FintWallet` component comes with **three built-in themes** and **flexible styling options** that let you customize everything from colors to spacing to match your brand. You can use themes as-is, apply partial overrides, or take complete control with headless mode.

**No Setup Required:** Styling is built into `FintWallet` itself. Just pass `theme` and `mode` props—no separate style providers needed.

---

## Quick Start: Pick a Theme

The easiest way to style the wallet is to choose one of the three built-in themes:

```
import { WalletProvider, FintWallet } from '@fint/wallet';

function UserSettings() {
  return (
    <WalletProvider publicKey="pk_test_..." userId={userId}>
      {/* Light theme (default) */}
      <FintWallet theme="light" />

      {/* Dark theme */}
      <FintWallet theme="dark" />

      {/* Minimal theme */}
      <FintWallet theme="minimal" />
    </WalletProvider>
  );
}
```

That’s it! The wallet is styled and ready to use.

---

## Built-in Themes

### Light Theme (Default)

Professional, modern design suitable for most applications.
**Characteristics:**

* Clean white backgrounds
* Soft shadows for depth
* Gray borders and subtle accents
* System font stack
* High readability

**Best for:**

* Business applications
* Customer portals
* General-purpose web apps

```
<FintWallet theme="light" />
```

### Dark Theme

Optimized for low-light environments with warm accents.
**Characteristics:**

* Dark gray/black backgrounds (`#2d2d2d`)
* Purple accents (`#bb86fc`)
* High contrast for accessibility
* Glowing focus states
* Reduced eye strain

**Best for:**

* Dark mode interfaces
* Night-time usage
* Modern dashboards

```
<FintWallet theme="dark" />
```

### Minimal Theme

Clean, minimalist design with reduced visual elements.
**Characteristics:**

* Thin borders (1px)
* No shadows
* Subtle spacing
* Black and white palette
* Fast transitions (0.1s)

**Best for:**

* Minimalist brands
* Content-focused apps
* Mobile-first designs

```
<FintWallet theme="minimal" />
```

---

## Theme System Overview

The wallet uses a **two-layer theming system** for maximum flexibility:

1. **Theme Tokens** (`themeConfig`) - Global design tokens that cascade across all components
2. **Component Styles** (`styles`) - Fine-grained CSS overrides for specific elements

This separation lets you maintain consistent branding (via tokens) while customizing specific UI elements as needed.

---

## Styling Modes

The `mode` prop controls how styles are applied:

### `themed` Mode (Default)

Use built-in themes with no additional configuration.

```
<FintWallet mode="themed" theme="light" />
```

### `custom` Mode

Apply partial overrides on top of a theme. Your custom styles merge with the base theme.

```
<FintWallet
  mode="custom"
  theme="light"
  styles={{
    // Override specific styles
    container: { maxWidth: '800px' },
    tabButton: { fontSize: '16px' },
    cardSurface: { borderRadius: '12px' }
  }}
/>
```

### `headless` Mode

Complete control—no default styles applied. You provide all styling.

```
<FintWallet
  mode="headless"
  className="my-custom-wallet"
/>
```

Use this when you need full design control or want to integrate with your own design system.

---

## Theme Customization with `themeConfig`

For consistent branding across all wallet components, use `themeConfig` to override design tokens. These changes cascade throughout the wallet automatically.

### Quick Brand Color Change

```
<FintWallet
  mode="themed"
  theme="light"
  themeConfig={{
    accent: {
      primary: '#7C3AED',        // Your brand purple
      primaryHover: '#6D28D9'    // Darker on hover
    }
  }}
/>
```

This single change updates:

* Focus states on all inputs
* Primary button colors
* Link colors
* Active tab indicators

### Common Token Overrides

```
<FintWallet
  mode="themed"
  theme="light"
  themeConfig={{
    // Brand colors
    accent: {
      primary: '#7C3AED'
    },

    // Typography
    typography: {
      fontFamily: {
        base: 'Inter, -apple-system, sans-serif'
      },
      sizes: {
        sm: '0.875rem',
        md: '1rem',
        lg: '1.125rem'
      }
    },

    // Spacing
    spacing: {
      sm: '0.5rem',
      md: '1rem',
      lg: '1.5rem'
    },

    // Border radius
    radii: {
      sm: 4,
      md: 8,
      lg: 12,
      xl: 16
    }
  }}
/>
```

### Surface Colors (Background Layers)

Control the color hierarchy for proper depth:

```
<FintWallet
  themeConfig={{
    surfaces: {
      app: {
        background: '#f9fafb'     // Page background
      },
      card: {
        background: '#ffffff',     // Card containers
        foreground: '#111827'      // Text on cards
      },
      sunken: {
        background: '#f3f4f6'     // Input fields (recessed)
      }
    }
  }}
/>
```

**Rule of thumb:** App → Card → Sunken should progressively get darker (light mode) or lighter (dark mode) for proper visual hierarchy.

### When to Use `themeConfig` vs `styles`

**Use `themeConfig` when:**

* Applying brand colors consistently
* Changing typography or spacing globally
* Maintaining design system consistency
* Switching between light/dark modes

**Use `styles` when:**

* Targeting specific components (tabs, buttons, dialogs)
* One-off adjustments to layout
* Overriding default positioning or dimensions

**Use both together:** Copy

```
<FintWallet
  mode="themed"
  theme="light"
  themeConfig={{
    // Global tokens
    accent: { primary: '#7C3AED' },
    typography: { fontFamily: { base: 'Inter' } }
  }}
  styles={{
    // Specific overrides
    container: { maxWidth: '900px' },
    tabButton: { textTransform: 'uppercase' }
  }}
/>
```

---

## Customization Layers

The wallet styling system has three layers you can customize:

### Layer 1: Wallet UI Styles

Controls the wallet-specific interface elements.

**Available Properties:**

* **Tabs:** `tabList`, `tabButton`, `tabButtonSelected`, `tabIndicator`
* **Card List:** `cardSurface`, `cardItemContainer`, `cardItemBadge`
* **Settings:** `settingsCard`, `settingsContainer`, `settingsDivider`
* **Dialogs:** `dialogOverlay`, `dialogPanel`, `dialogActions`
* **Empty State:** `emptyState`

```
<FintWallet
  mode="custom"
  theme="light"
  styles={{
    // Wallet-level customization
    container: {
      maxWidth: '900px',
      margin: '0 auto',
      borderRadius: '16px'
    },
    tabButton: {
      fontSize: '15px',
      fontWeight: '600',
      textTransform: 'uppercase',
      letterSpacing: '0.5px'
    },
    cardSurface: {
      borderRadius: '12px',
      boxShadow: '0 2px 8px rgba(0,0,0,0.1)'
    },
    emptyState: {
      padding: '4rem',
      fontSize: '18px',
      color: '#666'
    }
  }}
/>
```

### Layer 2: Form Styles

Controls forms within the wallet (contact info, shipping address, add card form).

**Available Properties:**

* **Structure:** `form`, `fieldset`, `button`, `field`, `label`
* **Input States:** `input`, `inputFocus`, `inputHover`, `inputValid`, `inputInvalid`
* **Special:** `error`, `sectionHeader`, `placesDropdown`

```
<FintWallet
  mode="custom"
  theme="light"
  styles={{
    // Form-level customization
    form: {
      padding: '2rem',
      gap: '1.5rem'
    },
    label: {
      fontSize: '14px',
      fontWeight: '600',
      color: '#333',
      marginBottom: '8px'
    },
    input: {
      fontSize: '16px',
      padding: '12px 16px',
      border: '2px solid #e0e0e0',
      borderRadius: '8px'
    },
    inputFocus: {
      borderColor: '#0066ff',
      boxShadow: '0 0 0 3px rgba(0,102,255,0.1)'
    },
    button: {
      backgroundColor: '#0066ff',
      color: 'white',
      fontSize: '16px',
      fontWeight: '600',
      padding: '14px 24px',
      borderRadius: '8px'
    }
  }}
/>
```

### Layer 3: Secure Element Styles (Iframe)

Controls secure card input fields (card number, CVV, expiry) rendered in iframes.

**How it works:**

* Form styles are automatically converted to iframe element styles
* You can override with specific iframe styles if needed
* Styles are applied via `FormStyleProvider` context

**Important:** Secure elements inherit styling from the `input*` properties in the form styles.

```
<FintWallet
  mode="custom"
  theme="light"
  styles={{
    // These input styles apply to both regular inputs AND secure iframe elements
    input: {
      fontSize: '16px',
      padding: '14px 16px',
      border: '2px solid #d0d0d0',
      borderRadius: '6px',
      backgroundColor: 'white'
    },
    inputFocus: {
      borderColor: '#0066ff',
      outline: 'none',
      boxShadow: '0 0 0 3px rgba(0,102,255,0.15)'
    },
    inputInvalid: {
      borderColor: '#e53e3e',
      boxShadow: '0 0 0 3px rgba(229,62,62,0.15)'
    }
  }}
/>
```

---

## Common Customizations

### Brand Colors

Match the wallet to your brand colors:

```
<FintWallet
  mode="custom"
  theme="light"
  styles={{
    // Primary brand color for buttons, focus states, badges
    button: { backgroundColor: '#ff5722' },
    inputFocus: { borderColor: '#ff5722', boxShadow: '0 0 0 3px rgba(255,87,34,0.15)' },
    tabButtonSelected: { color: '#ff5722', borderBottomColor: '#ff5722' },
    cardItemBadge: { backgroundColor: '#ff5722', color: 'white' },

    // Secondary color for accents
    linkButton: { color: '#ff5722' }
  }}
/>
```

### Custom Focus States

Create distinctive focus states for accessibility:

```
<FintWallet
  mode="custom"
  theme="light"
  styles={{
    inputFocus: {
      borderColor: '#4a90e2',
      boxShadow: '0 0 0 4px rgba(74,144,226,0.2)',
      transform: 'scale(1.01)',
      transition: 'all 0.2s ease'
    },
    buttonFocus: {
      outline: '3px solid #4a90e2',
      outlineOffset: '2px'
    }
  }}
/>
```

### Rounded vs Sharp Corners

Adjust border radius to match your design system:

```
// Rounded design
<FintWallet
  mode="custom"
  theme="light"
  styles={{
    container: { borderRadius: '16px' },
    cardSurface: { borderRadius: '12px' },
    input: { borderRadius: '8px' },
    button: { borderRadius: '8px' },
    dialogPanel: { borderRadius: '12px' }
  }}
/>

// Sharp design
<FintWallet
  mode="custom"
  theme="light"
  styles={{
    container: { borderRadius: '0' },
    cardSurface: { borderRadius: '0' },
    input: { borderRadius: '2px' },
    button: { borderRadius: '2px' },
    dialogPanel: { borderRadius: '0' }
  }}
/>
```

### Spacing Adjustments

Tighten or loosen spacing throughout:

```
<FintWallet
  mode="custom"
  theme="light"
  styles={{
    container: { padding: '32px' },
    form: { gap: '20px' },
    field: { marginBottom: '16px' },
    button: { padding: '16px 32px' },
    tabList: { gap: '12px' }
  }}
/>
```

### Typography Customization

Use your brand fonts and sizing:

```
<FintWallet
  mode="custom"
  theme="light"
  styles={{
    container: { fontFamily: 'Inter, sans-serif' },
    label: {
      fontFamily: 'Inter, sans-serif',
      fontSize: '13px',
      fontWeight: '600',
      letterSpacing: '0.3px',
      textTransform: 'uppercase'
    },
    input: {
      fontFamily: 'Inter, sans-serif',
      fontSize: '15px'
    },
    button: {
      fontFamily: 'Inter, sans-serif',
      fontSize: '15px',
      fontWeight: '600'
    }
  }}
/>
```

---

## Responsive Design

The wallet is mobile-responsive by default. You can customize behavior with CSS media queries:

```
<FintWallet
  mode="custom"
  theme="light"
  styles={{
    container: {
      maxWidth: '1000px',
      padding: '24px',
      // Use CSS custom properties for responsive values
      '@media (max-width: 768px)': {
        padding: '16px'
      }
    },
    tabButton: {
      fontSize: '16px',
      padding: '12px 24px',
      '@media (max-width: 768px)': {
        fontSize: '14px',
        padding: '10px 16px'
      }
    }
  }}
/>
```

**Mobile-First:** The wallet automatically adjusts layouts for mobile screens (single-column forms, larger touch targets, optimized spacing). You can override with custom styles if needed.

---

## Complete Customization Example

Real-world example showing comprehensive brand styling:

```
import { WalletProvider, FintWallet } from '@fint/wallet';

function BrandedWallet() {
  const brandStyles = {
    // Container
    container: {
      maxWidth: '900px',
      margin: '0 auto',
      padding: '32px',
      borderRadius: '16px',
      boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
      fontFamily: 'Inter, -apple-system, sans-serif'
    },

    // Tabs
    tabList: {
      backgroundColor: '#f8f9fa',
      borderRadius: '12px',
      padding: '6px',
      gap: '8px'
    },
    tabButton: {
      fontSize: '15px',
      fontWeight: '600',
      padding: '12px 24px',
      borderRadius: '8px',
      transition: 'all 0.2s ease'
    },
    tabButtonSelected: {
      backgroundColor: 'white',
      color: '#ff5722',
      boxShadow: '0 2px 8px rgba(0,0,0,0.1)'
    },

    // Cards
    cardSurface: {
      borderRadius: '12px',
      border: '1px solid #e0e0e0',
      boxShadow: '0 2px 8px rgba(0,0,0,0.05)',
      transition: 'all 0.2s ease'
    },
    cardItemBadge: {
      backgroundColor: '#ff5722',
      color: 'white',
      fontSize: '12px',
      fontWeight: '600',
      padding: '4px 12px',
      borderRadius: '12px'
    },

    // Forms
    label: {
      fontSize: '13px',
      fontWeight: '600',
      color: '#333',
      marginBottom: '8px',
      letterSpacing: '0.3px'
    },
    input: {
      fontSize: '15px',
      padding: '14px 16px',
      border: '2px solid #e0e0e0',
      borderRadius: '8px',
      transition: 'all 0.2s ease'
    },
    inputFocus: {
      borderColor: '#ff5722',
      boxShadow: '0 0 0 3px rgba(255,87,34,0.1)',
      outline: 'none'
    },
    inputInvalid: {
      borderColor: '#e53e3e',
      boxShadow: '0 0 0 3px rgba(229,62,62,0.1)'
    },
    button: {
      backgroundColor: '#ff5722',
      color: 'white',
      fontSize: '15px',
      fontWeight: '600',
      padding: '14px 24px',
      borderRadius: '8px',
      border: 'none',
      cursor: 'pointer',
      transition: 'all 0.2s ease'
    },
    buttonHover: {
      backgroundColor: '#f4511e',
      transform: 'translateY(-1px)',
      boxShadow: '0 4px 12px rgba(255,87,34,0.3)'
    },

    // Settings
    settingsCard: {
      borderRadius: '12px',
      border: '1px solid #e0e0e0',
      padding: '24px',
      boxShadow: '0 2px 8px rgba(0,0,0,0.05)'
    },

    // Dialogs
    dialogOverlay: {
      backgroundColor: 'rgba(0,0,0,0.5)',
      backdropFilter: 'blur(4px)'
    },
    dialogPanel: {
      borderRadius: '16px',
      boxShadow: '0 8px 32px rgba(0,0,0,0.2)',
      maxWidth: '500px'
    },

    // Empty state
    emptyState: {
      padding: '48px 24px',
      textAlign: 'center',
      color: '#666',
      fontSize: '16px',
      borderRadius: '12px',
      border: '2px dashed #e0e0e0'
    }
  };

  return (
    <WalletProvider publicKey="pk_test_..." userId={userId}>
      <FintWallet
        mode="custom"
        theme="light"
        styles={brandStyles}
      />
    </WalletProvider>
  );
}
```

---

## Headless Mode (Complete Control)

For complete design control, use headless mode and provide your own styles via `className`:

```
import './my-wallet-styles.css';

<FintWallet
  mode="headless"
  className="my-custom-wallet"
/>
```

**Your CSS:**

```
/* my-wallet-styles.css */
.my-custom-wallet {
  /* Your custom container styles */
  max-width: 1000px;
  margin: 0 auto;
}

.my-custom-wallet .wallet-tab-button {
  /* Style tab buttons */
  font-size: 16px;
  padding: 12px 24px;
}

.my-custom-wallet [data-testid="card-surface"] {
  /* Style card items */
  border: 1px solid #ccc;
  border-radius: 8px;
}
```

**Headless Mode:** You’re responsible for ALL styling, including forms, inputs, buttons, and layout. Use this only if you need complete control or are integrating with a design system like Tailwind or Chakra UI.

---

## TypeScript Support

All style interfaces are fully typed for autocomplete and type safety:

```
import type { WalletStyles } from '@fint/wallet';

const customStyles: Partial<WalletStyles> = {
  container: {
    maxWidth: '900px',
    padding: '32px'
  },
  tabButton: {
    fontSize: '16px',
    fontWeight: '600'
  },
  // TypeScript will autocomplete all 150+ available style properties
  // and catch type errors
};

<FintWallet mode="custom" theme="light" styles={customStyles} />
```

**Interface Hierarchy:**

* `WalletStyles` extends `FormStyles` (~150+ properties)
* `FormStyles` covers all form components
* Each property accepts React `CSSProperties`

---

## Styling Best Practices

### 1. Start with a Theme

Don’t start from scratch. Pick a theme close to your design and customize:

```
// Good: Start with minimal theme and customize
<FintWallet
  mode="custom"
  theme="minimal"
  styles={{ /* your overrides */ }}
/>

// Avoid: Headless mode unless necessary
<FintWallet mode="headless" />
```

### 2. Override Sparingly

Only override what you need. Themes are designed to work together:

```
// Good: Override key brand elements
<FintWallet
  mode="custom"
  theme="light"
  styles={{
    button: { backgroundColor: '#ff5722' },
    inputFocus: { borderColor: '#ff5722' }
  }}
/>

// Avoid: Overriding everything
<FintWallet
  mode="custom"
  theme="light"
  styles={{ /* 100+ overrides */ }}
/>
```

### 3. Use CSS Custom Properties

For dynamic theming, use CSS custom properties:

```
<FintWallet
  mode="custom"
  theme="light"
  styles={{
    button: {
      backgroundColor: 'var(--brand-primary)',
      color: 'var(--brand-text)'
    },
    inputFocus: {
      borderColor: 'var(--brand-primary)'
    }
  }}
/>
```

### 4. Test Mobile First

Always test styling on mobile devices:

```
<FintWallet
  mode="custom"
  theme="light"
  styles={{
    // Test these values on mobile
    input: { fontSize: '16px' }, // Prevents zoom on iOS
    button: { padding: '14px 24px' }, // Large touch target
    tabButton: { padding: '12px 20px' }
  }}
/>
```

### 5. Maintain Accessibility

Ensure sufficient contrast and focus states:

```
<FintWallet
  mode="custom"
  theme="light"
  styles={{
    // Always provide clear focus states
    inputFocus: {
      outline: '3px solid #0066ff',
      outlineOffset: '2px'
    },
    buttonFocus: {
      outline: '3px solid #0066ff',
      outlineOffset: '2px'
    },
    // Ensure text contrast (WCAG AA: 4.5:1 minimum)
    label: { color: '#333' },
    mutedText: { color: '#666' }
  }}
/>
```

---

## Accessing Theme Values with `useTheme()`

Need to build custom components that match your wallet theme? Use the `useTheme()` hook to access the current theme values.

### Basic Usage

```
import { useTheme } from '@fint/wallet';

function CustomButton() {
  const theme = useTheme();

  return (
    <button style={{
      backgroundColor: theme.accent.primary,
      color: theme.accent.onPrimary,
      padding: `${theme.spacing.sm} ${theme.spacing.lg}`,
      borderRadius: theme.radii.md,
      fontFamily: theme.typography.fontFamily.base
    }}>
      Click Me
    </button>
  );
}
```

### Use Cases

**Matching wallet styling in custom components:** Copy

```
function CustomCard() {
  const theme = useTheme();

  return (
    <div style={{
      backgroundColor: theme.surfaces.card.background,
      color: theme.surfaces.card.foreground,
      borderRadius: theme.radii.lg,
      padding: theme.spacing.lg,
      boxShadow: theme.shadows.sm
    }}>
      <h3>Custom Card</h3>
      <p>This matches your wallet theme automatically</p>
    </div>
  );
}
```**Dynamic theme-aware styling:** Copy

```
function StatusIndicator({ status }) {
  const theme = useTheme();

  const color = status === 'success'
    ? theme.status.success.foreground
    : theme.status.danger.foreground;

  return (
    <span style={{ color, fontFamily: theme.typography.fontFamily.base }}>
      {status}
    </span>
  );
}
```**Available theme values:**

```
const theme = useTheme();

// Colors
theme.accent.primary              // Primary brand color
theme.surfaces.card.background    // Card background
theme.text.primary                // Primary text color
theme.border.subtle               // Border colors
theme.status.success.foreground   // Status colors

// Typography
theme.typography.fontFamily.base  // Font family
theme.typography.sizes.md         // Font sizes
theme.typography.weights.medium   // Font weights

// Spacing & Layout
theme.spacing.sm                  // Small spacing (rem)
theme.spacing.md                  // Medium spacing (rem)
theme.spacing.lg                  // Large spacing (rem)
theme.radii.md                    // Border radius (px)

// Effects
theme.shadows.sm                  // Box shadows
theme.transitions.base            // Transitions
```

`useTheme()` must be used within `WalletProvider`. It returns the fully resolved theme with all overrides from `themeConfig` applied.

---

## What’s Next?

- [Integration Patterns](integration-patterns.md) — See real-world examples of wallet integrations
- [Payment Methods Tab](payment-methods-tab.md) — Learn how users manage their saved cards
- [Settings Tab](settings-tab.md) — Understand contact and shipping management
- [Wallet Overview](overview.md) — Back to wallet overview and setup guide

---

## Frequently Asked Questions

Can I use a different font family?

Yes! Set `fontFamily` on the `container` style, or target specific elements like `label`, `input`, or `button`:

```
<FintWallet
  mode="custom"
  theme="light"
  styles={{
    container: { fontFamily: 'Inter, sans-serif' },
    label: { fontFamily: 'Inter, sans-serif' },
    input: { fontFamily: 'Inter, sans-serif' }
  }}
/>
```

Do custom styles apply to the secure iframe elements?

Yes! Styles defined for `input`, `inputFocus`, `inputHover`, etc. are automatically converted and applied to secure iframe elements (card number, CVV, expiry). The styling is consistent across regular inputs and secure elements.

Can I create my own theme?

Yes! Create a `WalletStyles` object with all your styles and pass it:

```
import type { WalletStyles } from '@fint/wallet';

const myTheme: WalletStyles = {
  // Define all your styles here
  container: { /* ... */ },
  input: { /* ... */ },
  // ... 150+ properties
};

<FintWallet mode="custom" theme="light" styles={myTheme} />
```

Use an existing theme as a starting point to ensure you don’t miss critical styles.

How do I match my existing design system?

Use `mode="custom"` with your design tokens:

```
<FintWallet
  mode="custom"
  theme="light"
  styles={{
    container: { fontFamily: tokens.fonts.body },
    button: {
      backgroundColor: tokens.colors.primary,
      borderRadius: tokens.radii.md,
      padding: `${tokens.space[3]} ${tokens.space[5]}`
    },
    input: {
      fontSize: tokens.fontSizes.md,
      padding: tokens.space[3],
      borderRadius: tokens.radii.sm
    }
  }}
/>
```

Can I use Tailwind CSS with the wallet?

Yes, but only in `headless` mode. Use `className` to apply Tailwind classes:

```
<FintWallet mode="headless" className="max-w-4xl mx-auto p-6" />
```

Then target elements with Tailwind classes in your CSS or via data attributes.

How do I preview different themes before choosing?

Render multiple wallets side-by-side in development:

```
<div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '32px' }}>
  <div>
    <h3>Light</h3>
    <FintWallet theme="light" />
  </div>
  <div>
    <h3>Dark</h3>
    <FintWallet theme="dark" />
  </div>
  <div>
    <h3>Minimal</h3>
    <FintWallet theme="minimal" />
  </div>
</div>
```

Will my custom styles break with SDK updates?

No. The style interfaces are stable and versioned. New style properties may be added, but existing ones won’t be removed or changed in breaking ways. Always use TypeScript for compile-time safety.
