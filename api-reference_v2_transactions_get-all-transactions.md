# Get All Transactions

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Transactions

Get All Transactions

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

Get All Transactions

cURL

Copy

Ask AI

```
curl --request GET \
  --url https://api.example.com/api/v2/transactions/ \
  --header 'Authorization: Bearer <token>'
```

200

Copy

Ask AI

```
[
  {
    "org_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
    "user_id": "<string>",
    "id": "<string>",
    "private_key_id": "<string>",
    "private_key_display": "<string>",
    "allow_automatic_purchases": false,
    "spending_limit_currency": "<string>",
    "spending_limit_amount": 123,
    "allowed_merchant_category_codes": "<string>",
    "excluded_merchant_category_codes": "<string>",
    "shopping_rules": [
      "<string>"
    ],
    "human_messages": [
      "<string>"
    ],
    "conversation_context": {},
    "merchant": "<string>",
    "merchant_link": "<string>",
    "price": 123,
    "currency": "<string>",
    "product": "<string>",
    "product_description": "<string>",
    "confidence_score": 123,
    "additional_details": {},
    "last4_digits": "<string>",
    "card_exp": "<string>",
    "card_holder": "<string>",
    "email": "<string>",
    "billing_address": "<string>",
    "zip_code": "<string>",
    "phone_number": "<string>",
    "mode": "live",
    "created_at": "2023-11-07T05:31:56Z",
    "updated_at": "2023-11-07T05:31:56Z"
  }
]
```

Transactions

# Get All Transactions

Copy page

Retrieve all transactions for the authenticated customer.

**Authentication Required:** JWT Bearer Token (signed-in user)

* Requires `Authorization: Bearer <jwt_token>` header
* Token must contain valid customer ID

Copy page

GET

/

api

/

v2

/

transactions

Get All Transactions

cURL

Copy

Ask AI

```
curl --request GET \
  --url https://api.example.com/api/v2/transactions/ \
  --header 'Authorization: Bearer <token>'
```

200

Copy

Ask AI

```
[
  {
    "org_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
    "user_id": "<string>",
    "id": "<string>",
    "private_key_id": "<string>",
    "private_key_display": "<string>",
    "allow_automatic_purchases": false,
    "spending_limit_currency": "<string>",
    "spending_limit_amount": 123,
    "allowed_merchant_category_codes": "<string>",
    "excluded_merchant_category_codes": "<string>",
    "shopping_rules": [
      "<string>"
    ],
    "human_messages": [
      "<string>"
    ],
    "conversation_context": {},
    "merchant": "<string>",
    "merchant_link": "<string>",
    "price": 123,
    "currency": "<string>",
    "product": "<string>",
    "product_description": "<string>",
    "confidence_score": 123,
    "additional_details": {},
    "last4_digits": "<string>",
    "card_exp": "<string>",
    "card_holder": "<string>",
    "email": "<string>",
    "billing_address": "<string>",
    "zip_code": "<string>",
    "phone_number": "<string>",
    "mode": "live",
    "created_at": "2023-11-07T05:31:56Z",
    "updated_at": "2023-11-07T05:31:56Z"
  }
]
```

#### Authorizations

BearerAuthBearerAuthBearerAuthBearerAuth

[​](#authorization-authorization)

Authorization

string

header

required

JWT Bearer token from Auth0 authentication

#### Response

200

application/json

Successful Response

[​](#response-items-org-id)

org\_id

string<uuid>

required

The organization ID

[​](#response-items-user-id)

user\_id

string

required

The user ID

[​](#response-items-id-one-of-0)

id

string | null

The transaction ID, typically a UUID

[​](#response-items-private-key-id-one-of-0)

private\_key\_id

string | null

The private key ID used for the transaction

[​](#response-items-private-key-display-one-of-0)

private\_key\_display

string | null

Display version of the private key (masked for security)

[​](#response-items-allow-automatic-purchases-one-of-0)

allow\_automatic\_purchases

boolean | null

default:false

Allow automatic purchases

[​](#response-items-spending-limit-currency-one-of-0)

spending\_limit\_currency

string | null

Currency for spending limit (e.g., USD)

[​](#response-items-spending-limit-amount-one-of-0)

spending\_limit\_amount

number | null

Amount for spending limit

[​](#response-items-allowed-merchant-category-codes-one-of-0)

allowed\_merchant\_category\_codes

string | null

Comma-separated list of allowed MCCs

[​](#response-items-excluded-merchant-category-codes-one-of-0)

excluded\_merchant\_category\_codes

string | null

Comma-separated list of excluded MCCs

[​](#response-items-shopping-rules-one-of-0)

shopping\_rules

string[] | null

Custom shopping rules as a list of strings

[​](#response-items-human-messages-one-of-0)

human\_messages

string[] | null

Human messages in the conversation (list of strings)

[​](#response-items-conversation-context-one-of-0)

conversation\_context

Conversation Context · object

The conversation context as a JSON object

[​](#response-items-merchant-one-of-0)

merchant

string | null

The merchant name

[​](#response-items-merchant-link-one-of-0)

merchant\_link

string | null

Link to the merchant or product

[​](#response-items-price-one-of-0)

price

number | null

The product price

[​](#response-items-currency-one-of-0)

currency

string | null

The product currency (e.g., USD)

[​](#response-items-product-one-of-0)

product

string | null

The product name

[​](#response-items-product-description-one-of-0)

product\_description

string | null

The product description

[​](#response-items-confidence-score-one-of-0)

confidence\_score

number | null

The confidence score of the mandate

[​](#response-items-additional-details-one-of-0)

additional\_details

Additional Details · object

Additional details as a JSON object

[​](#response-items-last4-digits-one-of-0)

last4\_digits

string | null

The last 4 digits of the card

[​](#response-items-card-exp-one-of-0)

card\_exp

string | null

The card expiration date (e.g., MM/YY)

[​](#response-items-card-holder-one-of-0)

card\_holder

string | null

The card holder name

[​](#response-items-email-one-of-0)

email

string | null

The user's email address

[​](#response-items-billing-address-one-of-0)

billing\_address

string | null

The billing address

[​](#response-items-zip-code-one-of-0)

zip\_code

string | null

The billing zip code

[​](#response-items-phone-number-one-of-0)

phone\_number

string | null

The user's phone number

[​](#response-items-mode)

mode

enum<string>

default:live

Transaction mode: 'live' for production, 'sandbox' for testing

Available options:

`live`,

`sandbox`

[​](#response-items-created-at-one-of-0)

created\_at

string<date-time> | null

The creation date of the transaction

[​](#response-items-updated-at-one-of-0)

updated\_at

string<date-time> | null

The last update date of the transaction

[Revoke API Key](/api-reference/v2/api-keys/revoke-api-key)[Provisioned Token Webhook](/api-reference/v2/visa-webhooks/provisioned-token-webhook)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)