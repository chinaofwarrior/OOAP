# Get Mandate by ID

GET /api/v2/mandate/{mandate_id}

**Summary:** Get Mandate by ID

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

BearerAuth

[​](#authorization-authorization)

Authorization

Type: `string`  
Location: `header`  
Required  
JWT Bearer token from Auth0 authentication

#### Path Parameters

[​](#parameter-mandate-id)

mandate\_id

Type: `integer`  
Required

#### Response

Mandate details including product, price, and metadata

Mandate response

[​](#response-id)

id

Type: `integer`  
Required

[​](#response-request-id)

request\_id

Type: `string`  
Required

[​](#response-org-id)

org\_id

Type: `string<uuid>`  
Required

[​](#response-product-one-of-0)

product

Type: `string | null`  
Required

[​](#response-product-description-one-of-0)

product\_description

Type: `string | null`  
Required

[​](#response-price-one-of-0)

price

Type: `number | null`  
Required

[​](#response-currency-one-of-0)

currency

Type: `string | null`  
Required

[​](#response-merchant-one-of-0)

merchant

Type: `string | null`  
Required

[​](#response-merchant-link-one-of-0)

merchant\_link

Type: `string | null`  
Required

[​](#response-confidence-score-one-of-0)

confidence\_score

Type: `number | null`  
Required

[​](#response-conversation-context-one-of-0)

conversation\_context

Type: `Conversation Context` (object)  
Required

[​](#response-human-messages-one-of-0)

human\_messages

Type: `any[] | null`  
Required

[​](#response-additional-details-one-of-0)

additional\_details

Type: `Additional Details` (object)  
Required

[​](#response-created-at-one-of-0)

created\_at

Type: `string | null`  
Required

[​](#response-updated-at-one-of-0)

updated\_at

Type: `string | null`  
Required

[​](#response-mode)

mode

Type: `enum<string>`  
Default: `live`  
Mandate mode: 'live' for production, 'sandbox' for testing

Available options:

`live`,

`sandbox`

[​](#response-pm-type)

pm\_type

Type: `enum<string>`  
Default: `vgs`  
Vault type: 'vgs' (default) or 'visa' (Visa VTS tokenized)

Available options:

`vgs`,

`visa`

[​](#response-status-one-of-0)

status

Type: `string | null`  
Mandate status: 'active' or 'pending_visa_instruction'
