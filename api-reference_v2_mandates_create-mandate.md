# Create Mandate

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Mandates

Create Mandate

[Guides](/introduction)[API Reference](/api-reference/v2/cards/get-card-analytics)

v2

* [Website](https://nekuda.ai)
* [X](https://x.com/nekuda_ai)
* [Blog](https://nekuda.substack.com/)

##### Cards

* [GET

  Get Card Analytics](/api-reference/v2/cards/get-card-analytics)
* [GET

  Get Stored Card Details (Legacy)

  deprecated](/api-reference/v2/cards/get-stored-card-details-legacy)
* [GET

  Get All Cards](/api-reference/v2/cards/get-all-cards)
* [GET

  Get Default Card](/api-reference/v2/cards/get-default-card)
* [GET

  Get Stored Card Details](/api-reference/v2/cards/get-stored-card-details)
* [GET

  Get Card by ID](/api-reference/v2/cards/get-card-by-id)
* [DEL

  Delete Card](/api-reference/v2/cards/delete-card)
* [PATCH

  Update Card Information](/api-reference/v2/cards/update-card-information)
* [PUT

  Set Default Card](/api-reference/v2/cards/set-default-card)

##### Mandates

* [POST

  Create Mandate](/api-reference/v2/mandates/create-mandate)
* [GET

  Get All Mandates](/api-reference/v2/mandates/get-all-mandates)
* [GET

  Get Mandate by ID](/api-reference/v2/mandates/get-mandate-by-id)
* [POST

  Execute Visa Payment Instruction Action](/api-reference/v2/mandates/execute-visa-payment-instruction-action)

##### API Keys

* [GET

  List API Keys](/api-reference/v2/api-keys/list-api-keys)
* [POST

  Create API Key](/api-reference/v2/api-keys/create-api-key)
* [GET

  Get API Key Details](/api-reference/v2/api-keys/get-api-key-details)
* [DEL

  Delete API Key](/api-reference/v2/api-keys/delete-api-key)
* [PUT

  Revoke API Key](/api-reference/v2/api-keys/revoke-api-key)

##### Transactions

* [GET

  Get All Transactions](/api-reference/v2/transactions/get-all-transactions)

##### Visa Webhooks

* [POST

  Provisioned Token Webhook](/api-reference/v2/visa-webhooks/provisioned-token-webhook)
* [POST

  PAN Metadata Webhook](/api-reference/v2/visa-webhooks/pan-metadata-webhook)

##### Card Reveal

* [POST

  Request Card Reveal Token](/api-reference/v2/card-reveal/request-card-reveal-token)
* [GET

  Reveal Card Details](/api-reference/v2/card-reveal/reveal-card-details)

##### Payment Methods

* [GET

  Get Billing Details](/api-reference/v2/payment-methods/get-billing-details)
* [GET

  List Payment Methods](/api-reference/v2/payment-methods/list-payment-methods)
* [POST

  Add Payment Method](/api-reference/v2/payment-methods/add-payment-method)
* [GET

  Get payment method by ID](/api-reference/v2/payment-methods/get-payment-method-by-id)
* [PUT

  Update payment method](/api-reference/v2/payment-methods/update-payment-method)
* [DEL

  Delete payment method](/api-reference/v2/payment-methods/delete-payment-method)
* [PATCH

  Update payment method CVV](/api-reference/v2/payment-methods/update-payment-method-cvv)
* [POST

  Set payment method as default](/api-reference/v2/payment-methods/set-payment-method-as-default)

##### Collect

* [POST

  Collect Card Details (Legacy)

  deprecated](/api-reference/v2/collect/collect-card-details-legacy)
* [POST

  Collect customer information](/api-reference/v2/collect/collect-customer-information)

##### Customer Profile

* [GET

  Get Contact Information](/api-reference/v2/customer-profile/get-contact-information)
* [PUT

  Update Contact Information](/api-reference/v2/customer-profile/update-contact-information)
* [GET

  Get Shipping Address](/api-reference/v2/customer-profile/get-shipping-address)
* [PUT

  Update Shipping Address](/api-reference/v2/customer-profile/update-shipping-address)

Create Mandate

cURL

Copy

Ask AI

```
curl --request POST \
  --url https://api.example.com/api/v2/mandate/create \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>' \
  --data '
{
  "additional_details": {
    "promo_code": "SAVE10",
    "shipping_address": "123 Main St"
  },
  "confidence_score": 0.95,
  "conversation_context": {
    "intent": "purchase",
    "session_id": "abc123"
  },
  "currency": "USD",
  "human_messages": [
    "I want to buy the premium plan",
    "Yes, charge my card"
  ],
  "merchant": "Acme Corp",
  "merchant_link": "https://example.com",
  "price": 99.99,
  "product": "Premium Subscription",
  "product_description": "Annual premium subscription with advanced features"
}
'
```

201

422

Copy

Ask AI

```
{
  "mandate_id": 123,
  "request_id": "<string>",
  "org_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
  "created_at": "2023-11-07T05:31:56Z",
  "updated_at": "2023-11-07T05:31:56Z",
  "pm_type": "vgs",
  "status": "<string>"
}
```

Mandates

# Create Mandate

Copy page

Create a new payment mandate for a specific transaction context.

**Authentication Required:** Private API Key

* Requires `X-API-Key: <private_key>` header
* Private key validates customer and grants mandate creation access

**Additional Requirements:**

* `X-User-ID` and `X-Request-ID` headers required
* Mandate data in request body

Copy page

POST

/

api

/

v2

/

mandate

/

create

Create Mandate

cURL

Copy

Ask AI

```
curl --request POST \
  --url https://api.example.com/api/v2/mandate/create \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>' \
  --data '
{
  "additional_details": {
    "promo_code": "SAVE10",
    "shipping_address": "123 Main St"
  },
  "confidence_score": 0.95,
  "conversation_context": {
    "intent": "purchase",
    "session_id": "abc123"
  },
  "currency": "USD",
  "human_messages": [
    "I want to buy the premium plan",
    "Yes, charge my card"
  ],
  "merchant": "Acme Corp",
  "merchant_link": "https://example.com",
  "price": 99.99,
  "product": "Premium Subscription",
  "product_description": "Annual premium subscription with advanced features"
}
'
```

201

422

Copy

Ask AI

```
{
  "mandate_id": 123,
  "request_id": "<string>",
  "org_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
  "created_at": "2023-11-07T05:31:56Z",
  "updated_at": "2023-11-07T05:31:56Z",
  "pm_type": "vgs",
  "status": "<string>"
}
```

#### Authorizations

ApiKeyAuthApiKeyAuthApiKeyAuthApiKeyAuth

[​](#authorization-x-api-key)

X-API-Key

string

header

required

Private API key for full access to SDK operations

#### Headers

[​](#parameter-one-of-0)

x-request-id

string | null

Unique request identifier for tracing and debugging. Auto-generated if not provided.

[​](#parameter-x-user-id)

x-user-id

string

required

End-user identifier within a customer organization. Required for user-scoped operations.

#### Body

application/json

Request body for creating a mandate record.
All fields are optional to allow flexibility in mandate creation.

[​](#body-product-one-of-0)

product

string | null

Product name or identifier

[​](#body-product-description-one-of-0)

product\_description

string | null

Detailed description of the product

[​](#body-price-one-of-0)

price

number | null

Product price

[​](#body-currency-one-of-0)

currency

string | null

Currency code (ISO 4217)

[​](#body-merchant-one-of-0)

merchant

string | null

Merchant name

[​](#body-merchant-link-one-of-0)

merchant\_link

string | null

Link to merchant website

[​](#body-confidence-score-one-of-0)

confidence\_score

number | null

AI confidence score for the transaction (0-1)

[​](#body-conversation-context-one-of-0)

conversation\_context

Conversation Context · object

Context from the conversation that led to this mandate

[​](#body-human-messages-one-of-0)

human\_messages

string[] | null

List of human messages from the conversation

[​](#body-additional-details-one-of-0)

additional\_details

Additional Details · object

Any additional details relevant to the mandate

[​](#body-mode)

mode

enum<string>

default:live

Mandate mode: 'live' for production, 'sandbox' for testing

Available options:

`live`,

`sandbox`

[​](#body-payment-method-id-one-of-0)

payment\_method\_id

string | null

Payment method ID for Visa flow integration

#### Response

201

application/json

Successfully created mandate with unique ID and metadata

Mandate create response

[​](#response-mandate-id)

mandate\_id

integer

required

[​](#response-request-id)

request\_id

string

required

[​](#response-org-id)

org\_id

string<uuid>

required

[​](#response-created-at)

created\_at

string<date-time>

required

[​](#response-updated-at-one-of-0)

updated\_at

string<date-time> | null

required

[​](#response-pm-type)

pm\_type

enum<string>

default:vgs

Vault type: 'vgs' (default) or 'visa' (requires Visa instruction flow)

Available options:

`vgs`,

`visa`

[​](#response-status-one-of-0)

status

string | null

Mandate status: 'active' or 'pending\_visa\_instruction'

[Set Default Card](/api-reference/v2/cards/set-default-card)[Get All Mandates](/api-reference/v2/mandates/get-all-mandates)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)