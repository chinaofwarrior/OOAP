# List Payment Methods

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Payment Methods

List Payment Methods

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

List Payment Methods

cURL

Copy

Ask AI

```
curl --request GET \
  --url https://api.example.com/api/v2/wallet/payment-methods \
  --header 'X-Public-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>'
```

200

422

Copy

Ask AI

```
[
  {
    "id": "<string>",
    "cardType": "<string>",
    "lastFourDigits": "<string>",
    "expiryDate": "<string>",
    "cardHolderName": "<string>",
    "isDefault": true,
    "isActive": true,
    "billingAddress": {
      "addressLine1": "<string>",
      "city": "<string>",
      "state": "<string>",
      "zipCode": "<string>",
      "addressLine2": "Apt 4B",
      "county": "New York County",
      "country": "US"
    },
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "cvvAvailableUntil": "2024-01-15T11:30:00Z",
    "pmType": "vgs"
  }
]
```

Payment Methods

# List Payment Methods

Copy page

Retrieve all payment methods for the customer. Users can have multiple payment methods, but duplicate cards are prevented through idempotency keys.

Copy page

GET

/

api

/

v2

/

wallet

/

payment-methods

List Payment Methods

cURL

Copy

Ask AI

```
curl --request GET \
  --url https://api.example.com/api/v2/wallet/payment-methods \
  --header 'X-Public-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>'
```

200

422

Copy

Ask AI

```
[
  {
    "id": "<string>",
    "cardType": "<string>",
    "lastFourDigits": "<string>",
    "expiryDate": "<string>",
    "cardHolderName": "<string>",
    "isDefault": true,
    "isActive": true,
    "billingAddress": {
      "addressLine1": "<string>",
      "city": "<string>",
      "state": "<string>",
      "zipCode": "<string>",
      "addressLine2": "Apt 4B",
      "county": "New York County",
      "country": "US"
    },
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "cvvAvailableUntil": "2024-01-15T11:30:00Z",
    "pmType": "vgs"
  }
]
```

#### Authorizations

PublicKeyAuthPublicKeyAuthPublicKeyAuthPublicKeyAuth

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

#### Query Parameters

[​](#parameter-include-inactive)

includeInactive

boolean

default:false

#### Response

200

application/json

Payment methods retrieved successfully

[​](#response-items-id)

id

string

required

Unique identifier for the payment method. Generated as an idempotency key based on card details to prevent duplicates.

Example:

`"pm_1234567890abcdef"`

[​](#response-items-card-type)

cardType

string

required

Card type

Example:

`"visa"`

[​](#response-items-last-four-digits)

lastFourDigits

string

required

Example:

`"1111"`

[​](#response-items-expiry-date)

expiryDate

string

required

Example:

`"12/25"`

[​](#response-items-card-holder-name)

cardHolderName

string

required

Example:

`"John Doe"`

[​](#response-items-is-default)

isDefault

boolean

required

Example:

`false`

[​](#response-items-is-active)

isActive

boolean

required

Example:

`true`

[​](#response-items-billing-address)

billingAddress

BillingAddress · object

required

Billing address (same as base Address).

Show child attributes

[​](#response-items-created-at)

createdAt

string<date-time>

required

Example:

`"2024-01-15T10:30:00Z"`

[​](#response-items-updated-at)

updatedAt

string<date-time>

required

Example:

`"2024-01-15T10:30:00Z"`

[​](#response-items-cvv-available-until-one-of-0)

cvvAvailableUntil

string<date-time> | null

ISO 8601 timestamp with timezone until CVV is available (60 min after creation/update)

Example:

`"2024-01-15T11:30:00Z"`

[​](#response-items-pm-type)

pmType

enum<string>

default:vgs

Vault type: 'vgs' (default VGS vault) or 'visa' (Visa VTS tokenized)

Available options:

`vgs`,

`visa`

[Get Billing Details](/api-reference/v2/payment-methods/get-billing-details)[Add Payment Method](/api-reference/v2/payment-methods/add-payment-method)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)