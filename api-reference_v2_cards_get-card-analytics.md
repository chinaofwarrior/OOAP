# Get Card Analytics

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Cards

Get Card Analytics

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

Get Card Analytics

cURL

Copy

Ask AI

```
curl --request GET \
  --url https://api.example.com/api/v2/card-analytics \
  --header 'Authorization: Bearer <token>'
```

200

422

Copy

Ask AI

```
{
  "items": [
    {
      "user_id": "<string>",
      "masked_card_number": "<string>",
      "registration_date": "<string>",
      "card_type": "<string>",
      "last_updated": "<string>",
      "total_charges": 123,
      "status": "<string>",
      "is_deleted": true,
      "last_used": "<string>",
      "insights": "<string>"
    }
  ],
  "total": 123,
  "page": 123,
  "limit": 123,
  "total_pages": 123,
  "has_next": true,
  "has_previous": true
}
```

Cards

# Get Card Analytics

Copy page

Retrieve paginated card analytics data showing transaction statistics per card.

**Authentication Required:** JWT Bearer Token (signed-in user)

* Requires `Authorization: Bearer <jwt_token>` header
* Token must contain valid customer ID

**Features:**

* One row per card (users with multiple cards get multiple rows)
* Only shows users who have stored at least one card
* Card numbers are properly masked (\*\*\*1234)
* Status based on usage in last 3 months (active/inactive)
* Risk flags for new users (registered in last 2 weeks)
* Pagination support with configurable page size
* Search by user ID

**Performance:** Optimized with database indexes for large datasets

Copy page

GET

/

api

/

v2

/

card-analytics

Get Card Analytics

cURL

Copy

Ask AI

```
curl --request GET \
  --url https://api.example.com/api/v2/card-analytics \
  --header 'Authorization: Bearer <token>'
```

200

422

Copy

Ask AI

```
{
  "items": [
    {
      "user_id": "<string>",
      "masked_card_number": "<string>",
      "registration_date": "<string>",
      "card_type": "<string>",
      "last_updated": "<string>",
      "total_charges": 123,
      "status": "<string>",
      "is_deleted": true,
      "last_used": "<string>",
      "insights": "<string>"
    }
  ],
  "total": 123,
  "page": 123,
  "limit": 123,
  "total_pages": 123,
  "has_next": true,
  "has_previous": true
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

#### Query Parameters

[​](#parameter-page)

page

integer

default:1

Page number (1-based)

Required range: `x >= 1`

[​](#parameter-limit)

limit

integer

default:50

Items per page

Required range: `1 <= x <= 1000`

[​](#parameter-one-of-0)

search

string | null

Search by user ID

#### Response

200

application/json

Paginated card analytics data with transaction statistics

V2 Card Analytics paginated response - matches dot-service response format.

[​](#response-items)

items

CardAnalyticsItem · object[]

required

List of card analytics items

Show child attributes

[​](#response-total)

total

integer

required

Total number of items across all pages

[​](#response-page)

page

integer

required

Current page number (1-based)

[​](#response-limit)

limit

integer

required

Items per page limit

[​](#response-total-pages)

total\_pages

integer

required

Total number of pages

[​](#response-has-next)

has\_next

boolean

required

Whether there is a next page

[​](#response-has-previous)

has\_previous

boolean

required

Whether there is a previous page

[Get Stored Card Details (Legacy)](/api-reference/v2/cards/get-stored-card-details-legacy)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)