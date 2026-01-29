# Configuration

This page lists every **knob & switch ** exposed by the nekuda SDK and how to tweak them for production workloads.

## Configuration Consistency 🎯**Important** : Configure your `NekudaClient` **once** and reuse it throughout your application. Creating multiple clients with different configurations leads to confusion and bugs.

* Python
* TypeScript

```
from nekuda import NekudaClient

# Configure once at startup, typically using environment variables
client = NekudaClient.from_env()
# Or explicitly:
# client = NekudaClient(api_key="sk_live_...", base_url="https://api.nekuda.ai")

# Use everywhere
user_id_alice = "alice_123"
user_alice = client.user(user_id_alice)

user_id_bob = "bob_456"
user_bob = client.user(user_id_bob)
```

```
import { NekudaClient } from '@nekuda/nekuda-js';

// Configure once at startup
const client = NekudaClient.fromEnv();
// Or explicitly:
// const client = new NekudaClient('sk_live_...', { baseUrl: 'https://api.nekuda.ai' });

// Use everywhere
const userAlice = client.user('alice_123');
const userBob = client.user('bob_456');
```

## Environment Variables

These are the primary way to configure the nekuda SDK.

| Variable | Description | Default |
| --- | --- | --- |
| `NEKUDA_API_KEY` | **Required** – Secret key identifying your nekuda account. Get this from the [nekuda customer portal](https://app.nekuda.ai). | – |
| `NEKUDA_BASE_URL` | Override the API host. Defaults to production. Useful for pointing to staging or local mock servers. | `https://api.nekuda.ai` |

Both variables are consumed by `NekudaClient.from_env()`.

### Example .env file

.env

```
NEKUDA_API_KEY=sk_live_your_secret_key_here
# NEKUDA_BASE_URL=https://staging-api.nekuda.ai  # Uncomment for staging
```

## Client Constructor Options

While environment variables are recommended, you can also configure the client directly.

* Python
* TypeScript

```
from nekuda import NekudaClient

client = NekudaClient(
    api_key: str, # Your NEKUDA_API_KEY
    base_url: str = "https://api.nekuda.ai",
    timeout: int = 30,
    *,
    max_retries: int = 3,
    backoff_factor: float = 0.5,
)
```

[​](#param-api-key)

api\_key

string

required

Your nekuda API key (starts with `sk_live_` or `sk_test_`). This is mandatory.

[​](#param-base-url)

base\_url

string

default:"https://api.nekuda.ai"

API endpoint. The SDK automatically normalizes this (e.g., adds `https://`, removes trailing `/`). Only change this if you need to point to a non-production environment like staging.

[​](#param-timeout)

timeout

int

default:"30"

Network timeout in seconds passed to the underlying `httpx` client.

[​](#param-max-retries)

max\_retries

int

default:"3"

How many times to automatically retry on 5xx (server errors) or 429 (rate limit) responses.

[​](#param-backoff-factor)

backoff\_factor

float

default:"0.5"

Exponential sleep multiplier between retries. `sleep = (2 ** (retry_attempt - 1)) * backoff_factor`.

```
import { NekudaClient } from '@nekuda/nekuda-js';

const client = new NekudaClient(
  apiKey: string,
  options?: {
    baseUrl?: string,      // Default: "https://api.nekuda.ai"
    timeout?: number,      // Default: 30000 (30 seconds)
    maxRetries?: number,   // Default: 3
    backoffFactor?: number // Default: 0.5
  }
)
```

[​](#param-api-key)

apiKey

string

required

Your nekuda API key (starts with `sk_live_` or `sk_test_`). This is mandatory.

[​](#param-base-url)

baseUrl

string

default:"https://api.nekuda.ai"

API endpoint. The SDK automatically normalizes this (e.g., adds `https://`, removes trailing `/`).

[​](#param-timeout-1)

timeout

number

default:"30000"

Network timeout in **milliseconds** passed to `axios`.

[​](#param-max-retries)

maxRetries

number

default:"3"

How many times to automatically retry on 5xx (server errors) or 429 (rate limit) responses.

[​](#param-backoff-factor)

backoffFactor

number

default:"0.5"

Exponential sleep multiplier between retries.

## URL Normalization 🎯

The SDK automatically normalizes the `base_url`. The default is `https://api.nekuda.ai`.

URL Normalization Features

The SDK will:

* Add `https://` if no protocol specified (assuming `api.nekuda.ai` or similar public TLDs).
* Remove trailing slashes.
* Validate the URL format.
  For local development URLs like `localhost:8000`, ensure you include `http://` if not using HTTPS.

## Configuration Examples

* Python
* TypeScript

Production (Recommended)

Uses `NekudaClient.from_env()`. Ensure `NEKUDA_API_KEY` is set.

```
from nekuda import NekudaClient
# Reads NEKUDA_API_KEY and optionally NEKUDA_BASE_URL
client = NekudaClient.from_env()
```

Explicit Production

```
from nekuda import NekudaClient
client = NekudaClient(
    api_key="sk_live_your_actual_key", # Replace with your key
    base_url="https://api.nekuda.ai",   # Default, usually not needed to set
    timeout=30,
    max_retries=3,
    backoff_factor=0.5,
)
```

Staging/Testing

```
from nekuda import NekudaClient
# Best to use environment variables for this:
# export NEKUDA_API_KEY="sk_test_your_staging_key"
# export NEKUDA_BASE_URL="https://staging-api.nekuda.ai"
# client = NekudaClient.from_env()

# Or explicitly:
client_staging = NekudaClient(
    api_key="sk_test_your_staging_key",
    base_url="https://staging-api.nekuda.ai",
    timeout=10,
    max_retries=1,
)
```

Production (Recommended)

```
import { NekudaClient } from '@nekuda/nekuda-js';

// From environment variables
const client = NekudaClient.fromEnv();

// Or explicitly
const client = new NekudaClient('sk_live_...', {
  timeout: 30000,
  maxRetries: 5,
  backoffFactor: 1.0,
});
```

Development

```
import { NekudaClient } from '@nekuda/nekuda-js';

const client = new NekudaClient('sk_test_...', {
  baseUrl: 'localhost:8000',  // Will become http://localhost:8000
  timeout: 10000,
  maxRetries: 1,
});
```

High-throughput

```
import { NekudaClient } from '@nekuda/nekuda-js';

const client = new NekudaClient('sk_live_...', {
  timeout: 60000,  // Longer timeout for complex operations
  maxRetries: 10,  // More aggressive retries
  backoffFactor: 0.3,  // Faster initial retries
});
```

## Configuration Patterns

### Pattern 1: Environment Variables (Recommended)

This is the most flexible for different deployment environments (dev, staging, prod).

.env example

```
# For production
NEKUDA_API_KEY=sk_live_xxxxxxxxxxxx
NEKUDA_BASE_URL=https://api.nekuda.ai

# For staging
# NEKUDA_API_KEY=sk_test_yyyyyyyyyyyy
# NEKUDA_BASE_URL=https://staging-api.nekuda.ai
```

Python Code

```
from nekuda import NekudaClient
client = NekudaClient.from_env()
```

### Pattern 2: Explicit Configuration

Useful if environment variables are not an option, or for quick local tests.

```
from nekuda import NekudaClient
client = NekudaClient(
    api_key="sk_live_your_api_key",
    base_url="https://api.nekuda.ai",
    timeout=30
)
```

### Pattern 3: Mixed Configuration (Overrides)

You can use `from_env()` and override specific parameters.

```
from nekuda import NekudaClient
# Assumes NEKUDA_API_KEY and NEKUDA_BASE_URL are set in environment
client = NekudaClient.from_env(
    timeout=60,      # Override default timeout
    max_retries=5    # Override default retries
)
```

## Global Default Client

For quick scripts or simple applications, you can register a single global client.

* Python
* TypeScript

```
from nekuda import NekudaClient, set_default_client, get_default_client

# Set once at startup, typically using environment configuration
set_default_client(NekudaClient.from_env())

# Use anywhere in your code without passing the client instance
def some_function():
    client = get_default_client()
    # user_id must still be provided to client.user()
    user_context = client.user("some_user_id")
    # ... use user_context.create_mandate(...)
```

```
import { NekudaClient, setDefaultClient, getDefaultClient } from '@nekuda/nekuda-js';

// Set once at startup
setDefaultClient(NekudaClient.fromEnv());

// Use anywhere in your code
async function someFunction() {
    const client = getDefaultClient();
    const user = client.user('some_user_id');
    // ... use user.createMandate(...)
}
```

Using a global client can make testing and managing configurations in larger applications more complex. Be mindful of where and how the client is configured. Never share secrets (API key) across process boundaries unless you understand the security implications.

## Advanced Features (Built-in)

These features are enabled by default in the nekuda SDK.

### Response Validation

The SDK automatically validates all API responses.

Automatic Response Validation Details

* Python
* TypeScript

* Detects HTML error pages (e.g., nginx errors, gateway timeouts) and raises `NekudaApiError`.
* Validates JSON structure and raises `NekudaApiError` if parsing fails.
* Validates response data against expected Pydantic models (e.g., for card numbers, dates) and raises `NekudaValidationError` if data is malformed or missing.
* Provides clear error messages pinpointing the validation issue.

* Detects HTML error pages (e.g., nginx errors, gateway timeouts) and throws `NekudaApiError`.
* Validates JSON structure and throws `NekudaApiError` if parsing fails.
* Validates response data against TypeScript interfaces.
* Provides clear error messages with details about the validation issue.

### Type Safety

All methods return typed response models, enabling IDE autocompletion and static analysis.

* Python
* TypeScript

```
from nekuda import NekudaClient
client = NekudaClient.from_env()
user_context = client.user("test_user_123")
# Assume mandate_id is obtained
# reveal_response = user_context.request_card_reveal_token(mandate_id=...)
# print(reveal_response.token)  # Autocomplete works!
# print(reveal_response.expires_at)    # Optional[datetime]
```

```
import { NekudaClient } from '@nekuda/nekuda-js';
const client = NekudaClient.fromEnv();
const user = client.user('test_user_123');
// IDE knows all available fields
// const revealResponse = await user.requestCardRevealToken(mandateId);
// console.log(revealResponse.revealToken);  // Autocomplete works!
// console.log(revealResponse.expiresAt);    // Date | undefined
```

## Proxy Support

The SDK supports standard proxy environment variables (`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`).

Example Proxy Configuration

```
export HTTP_PROXY=http://proxy.yourcompany.com:8080
export HTTPS_PROXY=http://proxy.yourcompany.com:8080
export NO_PROXY=localhost,127.0.0.1,internal.service
```

No special SDK configuration is needed for proxies if these environment variables are set before your script runs.

## Logging & Debugging

Enable detailed logging from the SDK to troubleshoot issues.

* Python
* TypeScript

```
import logging

# To see all SDK debug messages, including request/response details:
logging.basicConfig(level=logging.DEBUG) # Set root logger to DEBUG
# Or more targeted:
# logging.getLogger("nekuda").setLevel(logging.DEBUG)

# Example output you might see:
# DEBUG:nekuda.client:Making POST request to https://api.nekuda.ai/v1/mandates with headers: ..., payload: ...
# DEBUG:nekuda.client:Received 201 response from https://api.nekuda.ai/v1/mandates with data: {"mandate_id": ...}
```

```
// Set environment variable before creating client
process.env.NEKUDA_DEBUG = 'true';

const client = new NekudaClient('sk_...', { debug: true });

// Example output:
// DEBUG:nekuda:Making POST request to https://api.nekuda.ai/api/v1/mandate/create
// DEBUG:nekuda:Response status: 200
// DEBUG:nekuda:Response data: {'mandateId': 123, ...}
```

## Configuration FAQ

Can I disable retries entirely?

Yes – pass `max_retries=0` to the `NekudaClient` constructor.

Does the SDK support async calls?

* Python
* TypeScript

Currently, the Python SDK only supports **synchronous ** calls. An async variant (`AsyncNekudaClient`) is on the roadmap.

The TypeScript SDK only supports **asynchronous ** calls. All methods return Promises and should be used with async/await or .then().

How do I handle different environments (dev/staging/prod)?**Recommended** : Use environment variables (`NEKUDA_API_KEY`, `NEKUDA_BASE_URL`) and `NekudaClient.from_env()`. Your deployment process can set these variables appropriately for each environment.Alternatively, you can explicitly instantiate `NekudaClient` with different parameters based on an environment flag:

```
import os
from nekuda import NekudaClient

if os.getenv("APP_ENV") == "production":
    client = NekudaClient(api_key=os.getenv("PROD_NEKUDA_API_KEY"), base_url="https://api.nekuda.ai")
elif os.getenv("APP_ENV") == "staging":
    client = NekudaClient(api_key=os.getenv("STAGING_NEKUDA_API_KEY"), base_url="https://staging-api.nekuda.ai")
else:
    # Default to a local or test setup
    client = NekudaClient(api_key="sk_test_local_key", base_url="http://localhost:8000")
```
