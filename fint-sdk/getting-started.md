# Getting Started

## Installation

* Python
* TypeScript

Install the SDK with **UV** (recommended) or pip:

```
uv pip install fint
```

The SDK ships as a single, pure-Python wheel with minimal dependencies -
installation takes ~1 second.

Install the SDK with your preferred package manager:

```
npm install @fint/fint-js
```

The SDK ships as a modern TypeScript package with minimal dependencies and
full tree-shaking support.

## Authentication

Grab your secret key from the [Fint customer portal](https://app.fint.io) and set it as an environment variable:

```
export FINT_API_KEY="sk_live_..."
# The SDK defaults to the production API: https://api.fint.io
# For staging or local testing, you can override the base URL:
# export FINT_BASE_URL="https://staging-api.fint.io"
```

Always keep your secret key secure on your backend. Never expose it in
client-side code.

## Your First Call

Create your first script to test authentication:

* Python
* TypeScript

hello.py

```
from fint import FintClient

client = FintClient.from_env()
print("🚀 Authenticated! Your account ID is:", client.api_key[:8] + "…")
```

Run it:

```
python hello.py
```

hello.ts

```
import { FintClient } from '@fint/fint-js';

async function main() {
  // Initialize client
  const client = FintClient.fromEnv();
  
  // Test the connection
  try {
    const user = client.user('test_user');
    console.log('✅ Connected to Fint API!');
    console.log(`   Base URL: ${(client as any).baseUrl}`);
    console.log(`   API Key: ${(client as any).apiKey.slice(0, 8)}...`);
  } catch (error) {
    console.log(`❌ Connection failed: ${error}`);
  }
}

main().catch(console.error);
```

Run it:

```
npx ts-node hello.ts
```

If everything is set up correctly, you should see:

```
🚀 Authenticated! Your account ID is: sk_live_12…
```

## What’s Next?

- [Quickstart](Quickstart-backend-sdk.md) — Complete your first payment flow in under 5 minutes
- [Core Concepts](core-concepts.md) — Understand the key building blocks of the SDK
