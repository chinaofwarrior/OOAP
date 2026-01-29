# Request Card Reveal Token

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Card Reveal

Request Card Reveal Token

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

Request Card Reveal Token

cURL

Copy

Ask AI

```
curl --request POST \
  --url https://api.example.com/api/v2/wallet/request_card_reveal_token \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: <api-key>' \
  --header 'headers: <headers>' \
  --data '
{
  "mandate_id": "<string>"
}
'
```

201

422

Copy

Ask AI

```
{
  "token": "<string>",
  "expires_at": "2023-11-07T05:31:56Z"
}
```

Card Reveal

# Request Card Reveal Token

Copy page

Request a short-lived token to reveal card details for a specific user.

**Authentication Required:** Private API Key

* Requires `X-API-Key: <private_key>` header
* Private key validates customer and grants full access

**Additional Requirements:**

* `X-User-ID` header required
* Valid `mandate_id` in request body
* Mandate validation performed automatically
* Wallet completeness validation performed before token generation

Copy page

POST

/

api

/

v2

/

wallet

/

request\_card\_reveal\_token

Request Card Reveal Token

cURL

Copy

Ask AI

```
curl --request POST \
  --url https://api.example.com/api/v2/wallet/request_card_reveal_token \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: <api-key>' \
  --header 'headers: <headers>' \
  --data '
{
  "mandate_id": "<string>"
}
'
```

201

422

Copy

Ask AI

```
{
  "token": "<string>",
  "expires_at": "2023-11-07T05:31:56Z"
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

[​](#parameter-headers)

headers

UserHeader · object

required

User header for all requests.

Show child attributes

#### Body

application/json

Request model for card reveal token generation.

[​](#body-mandate-id)

mandate\_id

string

required

Mandate identifier for authorization

#### Response

201

application/json

Short-lived token for card reveal operation

Response from validating a short-lived token.

[​](#response-token)

token

string

required

[​](#response-expires-at)

expires\_at

string<date-time>

required

[PAN Metadata Webhook](/api-reference/v2/visa-webhooks/pan-metadata-webhook)[Reveal Card Details](/api-reference/v2/card-reveal/reveal-card-details)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)