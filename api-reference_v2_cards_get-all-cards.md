# Get All Cards

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Cards

Get All Cards

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

Get All Cards

cURL

Copy

Ask AI

```
curl --request GET \
  --url https://api.example.com/api/v2/wallet/cards \
  --header 'X-Public-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>'
```

200

422

Copy

Ask AI

```
{
  "cards": [
    {
      "billing_address": "123 Main Street",
      "card_brand": "visa",
      "card_exp": "12/25",
      "card_holder": "John Doe",
      "city": "New York",
      "created_at": "2023-01-01T00:00:00Z",
      "email": "[email protected]",
      "id": "card_12345",
      "is_active": true,
      "is_default": true,
      "last4_digits": "1111",
      "phone_number": "+12125551234",
      "state": "NY",
      "updated_at": "2023-01-02T00:00:00Z",
      "zip_code": "10001"
    }
  ],
  "total": 1
}
```

Cards

# Get All Cards

Copy page

Retrieve all cards for a user.

**Authentication Required:** Public Key or API Key

* Requires `X-Public-Key: <public_key>` header OR `X-API-Key: <api_key>` header
* Public key identifies the merchant but provides limited access
* API key provides full access

**Additional Requirements:**

* `X-User-Id` header required

**Use Case:** Get list of all cards associated with a user

Copy page

GET

/

api

/

v2

/

wallet

/

cards

Get All Cards

cURL

Copy

Ask AI

```
curl --request GET \
  --url https://api.example.com/api/v2/wallet/cards \
  --header 'X-Public-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>'
```

200

422

Copy

Ask AI

```
{
  "cards": [
    {
      "billing_address": "123 Main Street",
      "card_brand": "visa",
      "card_exp": "12/25",
      "card_holder": "John Doe",
      "city": "New York",
      "created_at": "2023-01-01T00:00:00Z",
      "email": "[email protected]",
      "id": "card_12345",
      "is_active": true,
      "is_default": true,
      "last4_digits": "1111",
      "phone_number": "+12125551234",
      "state": "NY",
      "updated_at": "2023-01-02T00:00:00Z",
      "zip_code": "10001"
    }
  ],
  "total": 1
}
```

#### Authorizations

PublicKeyAuthPublicKeyAuthApiKeyAuthPublicKeyAuthPublicKeyAuthApiKeyAuth

[​](#authorization-x-public-key)

X-Public-Key

string

header

required

Public key for card collection operations

#### Headers

[​](#parameter-x-user-id)

x-user-id

string

required

End-user identifier within a customer organization. Required for user-scoped operations.

#### Response

200

application/json

List of cards retrieved successfully

Response model for listing multiple cards.

[​](#response-cards)

cards

CardDetailsResponse · object[]

required

List of cards

Show child attributes

[​](#response-total)

total

integer

required

Total number of cards

Required range: `x >= 0`

[Get Stored Card Details (Legacy)](/api-reference/v2/cards/get-stored-card-details-legacy)[Get Default Card](/api-reference/v2/cards/get-default-card)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)