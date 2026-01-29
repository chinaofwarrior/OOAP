# Best practices

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

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

* [TL;DR](#tl%3Bdr)
* [Core Principles](#core-principles)
* [Data Flow](#data-flow)
* [Key Management](#key-management)
* [Quick Checklist](#quick-checklist)

Security

# Best practices

Copy page

Copy page

### [​](#tl;dr) TL;DR

* **nekuda** supplies PCI‑compliant iframes + token APIs; raw card data never hits your servers.
* **You** keep tokens and logs safe and isolate card data from AI.

---

### [​](#core-principles) Core Principles

* Never commit or log `sk_live_*` keys.
* Card‑reveal tokens are single‑use; invoke them at checkout and discard.
* Treat PAN as toxic; hold it only in RAM during the payment call.
* AI isolation: do **not** pass PAN or tokens to LLM prompts, outputs, or screenshots.
* When in doubt, delete the data.

---

### [​](#data-flow) Data Flow

1. **Frontend** – Use `@nekuda/react-nekuda-js`; iframes keep card data off your origin.
2. **Backend** – Store only `{user_id ↔ nekuda_token}` + `mandate_id`, `request_id`.
3. **Checkout** – Call `revealCardDetails`, pay immediately, forget the PAN.

---

### [​](#key-management) Key Management

* Store secret keys in env vars only.
* Separate keys per env (dev, staging, prod).
* Rotate keys every 90 days or after any incident.

---

### [​](#quick-checklist) Quick Checklist

* Frontend uses **only** `pk_live_*`.
* Backend secrets live in env vars, not source.
* `user_id` is consistent across FE/BE.
* No PAN or tokens in logs, errors, or AI prompts.
* `mandate_id` + `request_id` logged for audit.
* HTTPS enforced by default (SDK).
* Secret key rotation scheduled.

*Ship this and you’re done.*

[Error Handling](/nekuda-sdk/Errors)[Policy Engine & Safety](/policy-engine-safety)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)