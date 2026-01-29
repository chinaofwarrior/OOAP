# Introduction

### Key Capabilities

* Securely collect and store payment credentials for AI agents and apps.
* Record user mandates (authorization) and retrieve cards just-in-time for transactions.
* Support network tokens and other agentic payment requirements from card networks.
* No PCI burden — drop in the SDK and start transacting.

### Select Use Cases

* **Browser assistant** that navigates to commerce sites and buys on command (e.g. “go ahead and pay for this flight”).
* **In-app “Buy Now”** buttons powered by automation agents that drive checkout flows.
* **In-chat agents** that buy on command using text instructions.
* **Voice-driven purchases** without manually entering payment details.

### Getting Started

1. Read the [System Overview](system-overview.md) for a clear description of how the Fint SDK works, covering the full payment flow and components of the system.
2. Follow the [Quickstart guide](fint-sdk/Quickstart.md) to get your agent making payments in minutes.
3. Check out our agent demo repository for complete implementation examples.

### Fint + Fintechain Combined Stack

Fint is a developer-first stablecoin payment gateway that exposes a unified multi-chain API and SDK. Fintechain provides the underlying multi-chain payment execution and on-chain confirmation layer. Together, they deliver a single integration surface while abstracting chain-level differences in confirmations, fees, and settlement.

**Highlights**
* Unified access across chains and stablecoins with a consistent REST API
* Server-side API key authentication for payment creation and status queries
* Webhook-driven status updates for finality and reconciliation

**Quick Start**
* Install SDK

```bash
pip install fint
```

* API base URL: https://api.fint.io
