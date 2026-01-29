# System Overview

**What You’ll Learn ** This page explains:

* How Fint’s architecture separates frontend and backend operations
* The role of mandates, reveal tokens, and network tokens
* How users, cards, and API keys work together
* Integration points with AI agents and checkout systems

**Time to read:** 10 minutes

Fint SDK provides a wallet designed specifically for AI agents and applications. It provides a secure way to collect, store, and reveal payment information when needed, enabling AI agents to complete transactions on behalf of users.
It also supports specific nuances of agentic payments required by card networks, such as recording user-specific authorization (mandate) and utilizing network tokens for payments.
The wallet has two main components: a frontend to create a beautiful wallet experience and securely collect payment credentials (removing PCI friction from the agent developer), and a backend to retrieve card details just-in-time and handle specific requirements of agentic payments, such as mandates.
As agentic payments evolve quickly, some underlying details may change, but we always stay aligned with the latest requirements.

## Agent wallet examples

## Main Workflows

The wallet is built around three main workflows:

### 1. Collect Payment Information

The **Frontend SDK** renders a wallet within the agent GUI, enabling you to securely collect credit card and shipping information from users. It uses customizable iframes to keep you out of PCI scope while matching the wallet’s appearance to your design preferences. Users can store multiple cards in the wallet and update their information at any time.

### 2. Capture Payment Mandate

Because users give permission to an agent to make purchases on their behalf, it is important to record the user mandate for that action. A mandate can take many forms (e.g. click a “buy” button, voice, text etc.) and the **Backend SDK** supports capturing it and storing it for future use. Once you record the mandate in our system, you’ll receive ‘reveal token’ that can be used to reveal the payment credentials when needed.

### 3. Retrieve Card

Using the reveal token and then retrieve the actual card details just-in-time for payment. This ensures card information is only accessed when explicitly authorized and needed. The card details can appear in two forms: either as a network token (a 16-digit number that looks and behaves like a credit card) when supported by the card network (for example Visa), or as a PAN when not. You can read about our [security best practices](best-practices.md) to handle this stage properly.

## Architecture Overview

The Fint system consists of two main components that work together:

### Frontend SDK

The **Frontend SDK** (`@fint/wallet`) runs in the user’s browser and handles:

* Secure collection of credit card, contact info, billing address, and shipping details
* User interface components for the wallet
* Client-side validation and error handling

**API Key** : Uses your **public key** (`pk_*`) - safe to expose in client-side code. Only allows card collection, never retrieval.

### Backend SDKs

The **Backend SDKs** (`fint` for Python and `@fint/fint-js` for TypeScript) run on your server and handle:

* Recording the user mandate
* Card details / network token retrieve
* Policy engine for security (coming soon)

**API Key** : Uses your **secret key** (`sk_*`) - must be kept private on your server. Allows card retrieval for your AI agent.

## Core Concepts

### Users

Each user in the Fint system is identified by a unique `userId` that you provide and manage. This identifier connects frontend payment data collection with backend information handling. The `userId` is needed whenever the backend wants to retrieve the payment credentials for payments.

### Mandates

A **mandate** represents a user’s intent to make a purchase. It contains:

* Product information
* Price and currency
* Merchant details
* Associated user context (such as prompts or other proof of delegated payment permission)

Mandates must be created before revealing card details, ensuring proper authorization for each transaction.

### Reveal Tokens

**Reveal tokens** are short-lived, single-use tokens that authorize the revelation of card details. They are:

* Generated for specific mandates
* Time-limited for security
* Required to access actual payment information

### Credit Cards

Each user can store multiple credit cards in their Fint wallet, identified by unique `cardId` values. This allows users to manage multiple payment methods:

* **Multiple Cards** : Users can store several credit cards under the same `userId`
* **Card Identification** : Each card is assigned a unique `cardId` for reference
* **Default Card** : Users can set one card as their default payment method
* **Automatic Selection** : When revealing card details, the default card is automatically retrieved unless a specific `cardId` is requested
* **Card Management** : Users can add, update, or remove cards through the frontend SDK

The wallet interface displays all stored cards with their masked numbers and allows users to easily select or change their default payment method.

### Network tokens

* Different card networks, like Visa and Mastercard, are developing agentic payment solutions that include network tokens. Network tokens have 16 digits like regular PANs and can be passed through GUI or human checkout interfaces. They look and feel like PANs but offer stronger security because they are scoped per transaction (hence the exposure of the network token is less risky than a PAN). They also come with a dynamic CVV (DTVV) generated by the card network for each transaction, and can be injected into guest checkouts.


## Information Flow

1

Frontend Collection

User provides payment and shipping details through the Fint frontend SDK, which securely stores the information associated with their `userId`.

2

Mandate Creation

Your backend captures a mandate using the backend SDK, specifying the purchase details and user context.

3

Token Request

Using the mandate ID, your backend requests a reveal token that authorizes access to the user’s payment information.

4

Information Revelation

The reveal token is used to securely retrieve the actual card details, which can then be used with the payment.

## Integration Points

### Checkout Agents / APIs

A commerce agent can build its own stack to complete purchases or use a third-party checkout agent, which usually receives SKUs or an order intent and executes purchases across different merchants. Fint can be easily integrated into these agents by delegating the retrieval functionality to them. You can pass the `userId` to them, and if they have access to your account, they can call the payment credentials just-in-time. Contact us for help with integration.

### Stablecoin Payments with Fint + Fintechain

For on-chain stablecoin payments, use Fint as the unified API/SDK surface while Fintechain handles multi-chain execution and confirmation beneath it. This keeps merchant integration simple and consistent across chains.

**How it fits:**
* Backend creates an on-chain payment via Fint REST API
* Fintechain executes the transaction and tracks confirmation/finality
* Webhooks deliver status transitions (pending → succeeded/failed) to your backend
* Reconciliation uses Fint’s identifiers and Fintechain’s on-chain metadata

**API base:** https://api.fint.io

## Next Steps

- [Payment Flow](payment-flow.md) — Understand the complete flow from collection to card reveal
- [Quickstart Guide](fint-sdk/Quickstart.md) — Get started with a complete integration example
- [Wallet Component](frontend/wallet/overview.md) — Complete wallet UI for collecting and managing payment methods
- [Backend SDK](fint-sdk/getting-started.md) — Discover server-side payment information handling
- [Security Best Practices](best-practices.md) — Implement secure payment workflows
