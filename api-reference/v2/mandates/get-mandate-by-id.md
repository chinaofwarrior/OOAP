# Get Mandate by ID

GET /api/v2/mandate/
{mandate\_id}

Get Mandate by ID

```
curl --request GET \
  --url https://api.example.com/api/v2/mandate/{mandate_id} \
  --header 'Authorization: Bearer <token>'
```

```
{
  "id": 123,
  "request_id": "<string>",
  "org_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
  "product": "<string>",
  "product_description": "<string>",
  "price": 123,
  "currency": "<string>",
  "merchant": "<string>",
  "merchant_link": "<string>",
  "confidence_score": 123,
  "conversation_context": {},
  "human_messages": [
    "<unknown>"
  ],
  "additional_details": {},
  "created_at": "<string>",
  "updated_at": "<string>",
  "mode": "live",
  "pm_type": "vgs",
  "status": "<string>"
}
```

#### Authorizations

BearerAuthBearerAuth

[​](#authorization-authorization)

Authorization

string

header

required

JWT Bearer token from Auth0 authentication

#### Path Parameters

[​](#parameter-mandate-id)

mandate\_id

integer

required

#### Response

Mandate details including product, price, and metadata

Mandate response

[​](#response-id)

id

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

[​](#response-product-one-of-0)

product

string | null

required

[​](#response-product-description-one-of-0)

product\_description

string | null

required

[​](#response-price-one-of-0)

price

number | null

required

[​](#response-currency-one-of-0)

currency

string | null

required

[​](#response-merchant-one-of-0)

merchant

string | null

required

[​](#response-merchant-link-one-of-0)

merchant\_link

string | null

required

[​](#response-confidence-score-one-of-0)

confidence\_score

number | null

required

[​](#response-conversation-context-one-of-0)

conversation\_context

Conversation Context · object

required

[​](#response-human-messages-one-of-0)

human\_messages

any[] | null

required

[​](#response-additional-details-one-of-0)

additional\_details

Additional Details · object

required

[​](#response-created-at-one-of-0)

created\_at

string | null

required

[​](#response-updated-at-one-of-0)

updated\_at

string | null

required

[​](#response-mode)

mode

enum<string>

default:live

Mandate mode: 'live' for production, 'sandbox' for testing

Available options:

`live`,

`sandbox`

[​](#response-pm-type)

pm\_type

enum<string>

default:vgs

Vault type: 'vgs' (default) or 'visa' (Visa VTS tokenized)

Available options:

`vgs`,

`visa`

[​](#response-status-one-of-0)

status

string | null

Mandate status: 'active' or 'pending\_visa\_instruction'
