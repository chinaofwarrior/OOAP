# Getting Started

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Backend SDK

Getting Started

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

* [Installation](#installation)
* [Authentication](#authentication)
* [Your First Call](#your-first-call)
* [What’s Next?](#what%E2%80%99s-next)

Backend SDK

# Getting Started

Copy page

Install the nekuda SDK, set your API key and make your first authenticated call.

Copy page

## [​](#installation) Installation

* Python
* TypeScript

Install the SDK with **UV** (recommended) or pip:

UV (Recommended)

pip

Copy

Ask AI

```
uv pip install nekuda
```

The SDK ships as a single, pure-Python wheel with minimal dependencies -
installation takes ~1 second.

Install the SDK with your preferred package manager:

npm

yarn

pnpm

Copy

Ask AI

```
npm install @nekuda/nekuda-js
```

The SDK ships as a modern TypeScript package with minimal dependencies and
full tree-shaking support.

## [​](#authentication) Authentication

Grab your secret key from the [nekuda customer portal](https://app.nekuda.ai) and set it as an environment variable:

Copy

Ask AI

```
export NEKUDA_API_KEY="sk_live_..."
# The SDK defaults to the production API: https://api.nekuda.ai
# For staging or local testing, you can override the base URL:
# export NEKUDA_BASE_URL="https://staging-api.nekuda.ai"
```

Always keep your secret key secure on your backend. Never expose it in
client-side code.

## [​](#your-first-call) Your First Call

Create your first script to test authentication:

* Python
* TypeScript

hello.py

Copy

Ask AI

```
from nekuda import NekudaClient

client = NekudaClient.from_env()
print("🚀 Authenticated! Your account ID is:", client.api_key[:8] + "…")
```

Run it:

Copy

Ask AI

```
python hello.py
```

hello.ts

Copy

Ask AI

```
import { NekudaClient } from '@nekuda/nekuda-js';

async function main() {
  // Initialize client
  const client = NekudaClient.fromEnv();
  
  // Test the connection
  try {
    const user = client.user('test_user');
    console.log('✅ Connected to nekuda API!');
    console.log(`   Base URL: ${(client as any).baseUrl}`);
    console.log(`   API Key: ${(client as any).apiKey.slice(0, 8)}...`);
  } catch (error) {
    console.log(`❌ Connection failed: ${error}`);
  }
}

main().catch(console.error);
```

Run it:

Copy

Ask AI

```
npx ts-node hello.ts
```

If everything is set up correctly, you should see:

Copy

Ask AI

```
🚀 Authenticated! Your account ID is: sk_live_12…
```

## [​](#what’s-next) What’s Next?

[## Quickstart

Complete your first payment flow in under 5 minutes](/nekuda-sdk/Quickstart-backend-sdk)[## Core Concepts

Understand the key building blocks of the SDK](/nekuda-sdk/core-concepts)

[Migration Guide](/frontend/wallet/migration-guide)[Core Concepts](/nekuda-sdk/core-concepts)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)