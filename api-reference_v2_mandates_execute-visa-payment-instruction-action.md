# Execute Visa Payment Instruction Action

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Mandates

Execute Visa Payment Instruction Action

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

Execute Visa Payment Instruction Action

cURL

Copy

Ask AI

```
curl --request POST \
  --url https://api.example.com/api/v2/mandate/action \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>' \
  --data '
{
  "action": "check",
  "payment_method_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
  "mandate_id": "<string>",
  "session_context": {},
  "browser_data": {},
  "otp_value": "<string>",
  "otp_identifier": "<string>",
  "assurance_identifier": "<string>",
  "fido_assertion_data": "<string>",
  "dfp_session_id": "<string>",
  "conversation_context": "<string>",
  "mandate": {
    "mandate_id": "<string>",
    "amount": "<string>",
    "currency_code": "<string>",
    "currency_code_numeric": "<string>",
    "merchant_category_code": "<string>",
    "description": "<string>",
    "quantity": 123,
    "effective_until_time": 123,
    "decline_threshold": {
      "amount": "<string>",
      "currency_code": "<string>"
    }
  },
  "transaction_id": "<string>"
}
'
```

422

Copy

Ask AI

```
{
  "detail": [
    {
      "loc": [
        "<string>"
      ],
      "msg": "<string>",
      "type": "<string>"
    }
  ]
}
```

Mandates

# Execute Visa Payment Instruction Action

Copy page

Execute a Visa payment instruction action (check, bind, validate\_otp, attestation, complete, update, cancel).

**Authentication Required:** Public OR Private API Key

* Requires `X-API-Key: <private_key>` (backend SDK) OR
* `X-Public-Key: <public_key>` (frontend SDK)
* If both headers are provided, private key takes priority
* Key validates customer and grants access

**Feature Flag Required:**

* Customer must have Visa enabled via feature flag
* Returns 403 if Visa is not enabled for the customer

**Additional Requirements:**

* `X-User-ID` and `X-Request-ID` headers required
* Action-specific data in request body

Copy page

POST

/

api

/

v2

/

mandate

/

action

Execute Visa Payment Instruction Action

cURL

Copy

Ask AI

```
curl --request POST \
  --url https://api.example.com/api/v2/mandate/action \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>' \
  --data '
{
  "action": "check",
  "payment_method_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
  "mandate_id": "<string>",
  "session_context": {},
  "browser_data": {},
  "otp_value": "<string>",
  "otp_identifier": "<string>",
  "assurance_identifier": "<string>",
  "fido_assertion_data": "<string>",
  "dfp_session_id": "<string>",
  "conversation_context": "<string>",
  "mandate": {
    "mandate_id": "<string>",
    "amount": "<string>",
    "currency_code": "<string>",
    "currency_code_numeric": "<string>",
    "merchant_category_code": "<string>",
    "description": "<string>",
    "quantity": 123,
    "effective_until_time": 123,
    "decline_threshold": {
      "amount": "<string>",
      "currency_code": "<string>"
    }
  },
  "transaction_id": "<string>"
}
'
```

422

Copy

Ask AI

```
{
  "detail": [
    {
      "loc": [
        "<string>"
      ],
      "msg": "<string>",
      "type": "<string>"
    }
  ]
}
```

#### Authorizations

ApiKeyAuthPublicKeyAuthApiKeyAuthPublicKeyAuthApiKeyAuthPublicKeyAuthApiKeyAuthPublicKeyAuth

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

Request for /mandate/action endpoint.

[​](#body-action)

action

enum<string>

required

Available options:

`check`,

`bind`,

`validate_otp`,

`attestation`,

`complete`,

`update`,

`cancel`

[​](#body-payment-method-id)

payment\_method\_id

string<uuid>

required

[​](#body-mandate-id-one-of-0)

mandate\_id

string | null

[​](#body-session-context-one-of-0)

session\_context

Session Context · object

[​](#body-browser-data-one-of-0)

browser\_data

Browser Data · object

[​](#body-otp-value-one-of-0)

otp\_value

string | null

[​](#body-otp-identifier-one-of-0)

otp\_identifier

string | null

[​](#body-assurance-identifier-one-of-0)

assurance\_identifier

string | null

[​](#body-fido-assertion-data-one-of-0)

fido\_assertion\_data

string | null

[​](#body-dfp-session-id-one-of-0)

dfp\_session\_id

string | null

[​](#body-conversation-context-one-of-0)

conversation\_context

string | null

[​](#body-mandate-one-of-0)

mandate

MandateData · object

Mandate data for payment instruction.

Show child attributes

[​](#body-transaction-id-one-of-0)

transaction\_id

string | null

#### Response

200

application/json

Stage-specific response from Visa service

[Get Mandate by ID](/api-reference/v2/mandates/get-mandate-by-id)[List API Keys](/api-reference/v2/api-keys/list-api-keys)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)