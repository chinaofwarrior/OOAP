# System Overview

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Get Started

System Overview

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

* [Agent wallet examples](#agent-wallet-examples)
* [Main Workflows](#main-workflows)
* [1. Collect Payment Information](#1-collect-payment-information)
* [2. Capture Payment Mandate](#2-capture-payment-mandate)
* [3. Retrieve Card](#3-retrieve-card)
* [Architecture Overview](#architecture-overview)
* [Frontend SDK](#frontend-sdk)
* [Backend SDKs](#backend-sdks)
* [Core Concepts](#core-concepts)
* [Users](#users)
* [Mandates](#mandates)
* [Reveal Tokens](#reveal-tokens)
* [Credit Cards](#credit-cards)
* [Network tokens](#network-tokens)
* [Information Flow](#information-flow)
* [Integration Points](#integration-points)
* [Checkout Agents / APIs](#checkout-agents-%2F-apis)
* [Next Steps](#next-steps)

Get Started

# System Overview

Copy page

Understand how nekuda’s wallet works for AI agents and applications.

Copy page

**What You’ll Learn**This page explains:

* How nekuda’s architecture separates frontend and backend operations
* The role of mandates, reveal tokens, and network tokens
* How users, cards, and API keys work together
* Integration points with AI agents and checkout systems

**Time to read:** 10 minutes

nekuda SDK provides a wallet designed specifically for AI agents and applications. It provides a secure way to collect, store, and reveal payment information when needed, enabling AI agents to complete transactions on behalf of users.
It also supports specific nuances of agentic payments required by card networks, such as recording user-specific authorization (mandate) and utilizing network tokens for payments.
The wallet has two main components: a frontend to create a beautiful wallet experience and securely collect payment credentials (removing PCI friction from the agent developer), and a backend to retrieve card details just-in-time and handle specific requirements of agentic payments, such as mandates.
As agentic payments evolve quickly, some underlying details may change, but we always stay aligned with the latest requirements.

## [​](#agent-wallet-examples) Agent wallet examples

![nekuda Wallet showing payment methods](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/images/nekuda-wallet-1.png?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=a1c1a4069cf699a48122b7c7f309c896)![nekuda Wallet add payment method form](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/images/nekuda-wallet-2.png?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=711041337059f685059474f40d53dc8a)

## [​](#main-workflows) Main Workflows

The wallet is built around three main workflows:

### [​](#1-collect-payment-information) 1. Collect Payment Information

The **Frontend SDK** renders a wallet within the agent GUI, enabling you to securely collect credit card and shipping information from users. It uses customizable iframes to keep you out of PCI scope while matching the wallet’s appearance to your design preferences. Users can store multiple cards in the wallet and update their information at any time.

### [​](#2-capture-payment-mandate) 2. Capture Payment Mandate

Because users give permission to an agent to make purchases on their behalf, it is important to record the user mandate for that action. A mandate can take many forms (e.g. click a “buy” button, voice, text etc.) and the **Backend SDK** supports capturing it and storing it for future use. Once you record the mandate in our system, you’ll receive ‘reveal token’ that can be used to reveal the payment credentials when needed.

### [​](#3-retrieve-card) 3. Retrieve Card

Using the reveal token and then retrieve the actual card details just-in-time for payment. This ensures card information is only accessed when explicitly authorized and needed. The card details can appear in two forms: either as a network token (a 16-digit number that looks and behaves like a credit card) when supported by the card network (for example Visa), or as a PAN when not. You can read about our [security best practices](/best-practices) to handle this stage properly.

## [​](#architecture-overview) Architecture Overview

The nekuda system consists of two main components that work together:

### [​](#frontend-sdk) Frontend SDK

The **Frontend SDK** (`@nekuda/wallet`) runs in the user’s browser and handles:

* Secure collection of credit card, contact info, billing address, and shipping details
* User interface components for the wallet
* Client-side validation and error handling

**API Key**: Uses your **public key** (`pk_*`) - safe to expose in client-side code. Only allows card collection, never retrieval.

### [​](#backend-sdks) Backend SDKs

The **Backend SDKs** (`nekuda` for Python and `@nekuda/nekuda-js` for TypeScript) run on your server and handle:

* Recording the user mandate
* Card details / network token retrieve
* Policy engine for security (coming soon)

**API Key**: Uses your **secret key** (`sk_*`) - must be kept private on your server. Allows card retrieval for your AI agent.

## [​](#core-concepts) Core Concepts

### [​](#users) Users

Each user in the nekuda system is identified by a unique `userId` that you provide and manage. This identifier connects frontend payment data collection with backend information handling. The `userId` is needed whenever the backend wants to retrieve the payment credentials for payments.

![userId](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/images/diagram-1.png?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=269d8bd524e1576a4afcbfa0c7aa2541)

### [​](#mandates) Mandates

A **mandate** represents a user’s intent to make a purchase. It contains:

* Product information
* Price and currency
* Merchant details
* Associated user context (such as prompts or other proof of delegated payment permission)

Mandates must be created before revealing card details, ensuring proper authorization for each transaction.

### [​](#reveal-tokens) Reveal Tokens

**Reveal tokens** are short-lived, single-use tokens that authorize the revelation of card details. They are:

* Generated for specific mandates
* Time-limited for security
* Required to access actual payment information

### [​](#credit-cards) Credit Cards

Each user can store multiple credit cards in their nekuda wallet, identified by unique `cardId` values. This allows users to manage multiple payment methods:

* **Multiple Cards**: Users can store several credit cards under the same `userId`
* **Card Identification**: Each card is assigned a unique `cardId` for reference
* **Default Card**: Users can set one card as their default payment method
* **Automatic Selection**: When revealing card details, the default card is automatically retrieved unless a specific `cardId` is requested
* **Card Management**: Users can add, update, or remove cards through the frontend SDK

The wallet interface displays all stored cards with their masked numbers and allows users to easily select or change their default payment method.

![user_id](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/images/diagram-2.png?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=8aad2f83db1b41571acd3024cd8a9dcf)

### [​](#network-tokens) Network tokens

* Different card networks, like Visa and Mastercard, are developing agentic payment solutions that include network tokens. Network tokens have 16 digits like regular PANs and can be passed through GUI or human checkout interfaces. They look and feel like PANs but offer stronger security because they are scoped per transaction (hence the exposure of the network token is less risky than a PAN). They also come with a dynamic CVV (DTVV) generated by the card network for each transaction, and can be injected into guest checkouts.

![Network Tokens vs Traditional PANs comparison](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/images/network_tokens_vs_pan.png?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=e49885bc47bcee5210a4fec6f70dab94)

## [​](#information-flow) Information Flow

1

Frontend Collection

User provides payment and shipping details through the nekuda frontend SDK, which securely stores the information associated with their `userId`.

2

Mandate Creation

Your backend captures a mandate using the backend SDK, specifying the purchase details and user context.

3

Token Request

Using the mandate ID, your backend requests a reveal token that authorizes access to the user’s payment information.

4

Information Revelation

The reveal token is used to securely retrieve the actual card details, which can then be used with the payment.

## [​](#integration-points) Integration Points

### [​](#checkout-agents-/-apis) Checkout Agents / APIs

A commerce agent can build its own stack to complete purchases or use a third-party checkout agent, which usually receives SKUs or an order intent and executes purchases across different merchants. nekuda can be easily integrated into these agents by delegating the retrieval functionality to them. You can pass the `userId` to them, and if they have access to your account, they can call the payment credentials just-in-time. Contact us for help with integration.

![user_id](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/images/integration_example.png?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=82b747feaa6be3a535f1df73873b8603)

## [​](#next-steps) Next Steps

[## Payment Flow

Understand the complete flow from collection to card reveal](/payment-flow)[## Quickstart Guide

Get started with a complete integration example](/nekuda-sdk/Quickstart)[## Wallet Component

Complete wallet UI for collecting and managing payment methods](/frontend/wallet/overview)[## Backend SDK

Discover server-side payment information handling](/nekuda-sdk/getting-started)[## Security Best Practices

Implement secure payment workflows](/best-practices)

[Quickstart](/nekuda-sdk/Quickstart)[Payment Flow](/payment-flow)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)