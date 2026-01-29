# Revoke API Key

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

API Keys

Revoke API Key

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

Revoke API Key

cURL

Copy

Ask AI

```
curl --request PUT \
  --url https://api.example.com/api/v2/api-keys/{key_id}/revoke \
  --header 'Authorization: Bearer <token>'
```

200

422

Copy

Ask AI

```
{
  "id": "<string>",
  "org_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
  "name": "<string>",
  "is_revoked": true,
  "created_at": "2023-11-07T05:31:56Z",
  "description": "<string>",
  "expires_at": "2023-11-07T05:31:56Z",
  "last_used_at": "2023-11-07T05:31:56Z"
}
```

API Keys

# Revoke API Key

Copy page

Revoke an API key, preventing its future use (irreversible).

**Authentication Required:** JWT Bearer Token

* Requires `Authorization: Bearer <jwt_token>` header
* Token must contain valid customer ID
* Only affects keys owned by the authenticated customer

Copy page

PUT

/

api

/

v2

/

api-keys

/

{key\_id}

/

revoke

Revoke API Key

cURL

Copy

Ask AI

```
curl --request PUT \
  --url https://api.example.com/api/v2/api-keys/{key_id}/revoke \
  --header 'Authorization: Bearer <token>'
```

200

422

Copy

Ask AI

```
{
  "id": "<string>",
  "org_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
  "name": "<string>",
  "is_revoked": true,
  "created_at": "2023-11-07T05:31:56Z",
  "description": "<string>",
  "expires_at": "2023-11-07T05:31:56Z",
  "last_used_at": "2023-11-07T05:31:56Z"
}
```

#### Authorizations

BearerAuthBearerAuthBearerAuthBearerAuth

[​](#authorization-authorization)

Authorization

string

header

required

JWT Bearer token from Auth0 authentication

#### Path Parameters

[​](#parameter-key-id)

key\_id

string

required

The unique identifier of the API key (UUID format).

Example:

`"07f5aec0-3ec3-441f-a098-912d201d067d"`

#### Response

200

application/json

Successful Response

Model for API key revocation information (V2).

[​](#response-id)

id

string

required

[​](#response-org-id)

org\_id

string<uuid>

required

[​](#response-name)

name

string

required

[​](#response-is-revoked)

is\_revoked

boolean

required

[​](#response-created-at)

created\_at

string<date-time>

required

[​](#response-description-one-of-0)

description

string | null

[​](#response-expires-at-one-of-0)

expires\_at

string<date-time> | null

[​](#response-last-used-at-one-of-0)

last\_used\_at

string<date-time> | null

[Delete API Key](/api-reference/v2/api-keys/delete-api-key)[Get All Transactions](/api-reference/v2/transactions/get-all-transactions)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)