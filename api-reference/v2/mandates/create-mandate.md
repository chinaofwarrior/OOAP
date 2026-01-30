# Create Mandate
![Lux Divider](../../../assets/lux/divider.svg)

POST /api/v2/mandate/create

**Summary:** Create Mandate

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

ApiKeyAuth

[​](#authorization-x-api-key)

X-API-Key

Type: `string`  
Location: `header`  
Required  
Private API key for full access to SDK operations

#### Headers

[​](#parameter-one-of-0)

x-request-id

Type: `string | null`  
Unique request identifier for tracing and debugging. Auto-generated if not provided.

[​](#parameter-x-user-id)

x-user-id

Type: `string`  
Required  
End-user identifier within a customer organization. Required for user-scoped operations.

#### Body

application/json

Request body for creating a mandate record.
All fields are optional to allow flexibility in mandate creation.

[​](#body-product-one-of-0)

product

Type: `string | null`  
Product name or identifier

[​](#body-product-description-one-of-0)

product\_description

Type: `string | null`  
Detailed description of the product

[​](#body-price-one-of-0)

price

Type: `number | null`  
Product price

[​](#body-currency-one-of-0)

currency

Type: `string | null`  
Currency code (ISO 4217)

[​](#body-merchant-one-of-0)

merchant

Type: `string | null`  
Merchant name

[​](#body-merchant-link-one-of-0)

merchant\_link

Type: `string | null`  
Link to merchant website

[​](#body-confidence-score-one-of-0)

confidence\_score

Type: `number | null`  
AI confidence score for the transaction (0-1)

[​](#body-conversation-context-one-of-0)

conversation\_context

Type: `Conversation Context` (object)  
Context from the conversation that led to this mandate

[​](#body-human-messages-one-of-0)

human\_messages

Type: `string[] | null`  
List of human messages from the conversation

[​](#body-additional-details-one-of-0)

additional\_details

Type: `Additional Details` (object)  
Any additional details relevant to the mandate

[​](#body-mode)

mode

Type: `enum<string>`  
Default: `live`  
Mandate mode: 'live' for production, 'sandbox' for testing

Available options:

`live`,

`sandbox`

[​](#body-payment-method-id-one-of-0)

payment\_method\_id

Type: `string | null`  
Payment method ID for Visa flow integration

#### Response

Successfully created mandate with unique ID and metadata

Mandate create response

[​](#response-mandate-id)

mandate\_id

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

[​](#response-created-at)

created\_at

Type: `string<date-time>`  
Required

[​](#response-updated-at-one-of-0)

updated\_at

Type: `string<date-time> | null`  
Required

[​](#response-pm-type)

pm\_type

Type: `enum<string>`  
Default: `vgs`  
Vault type: 'vgs' (default) or 'visa' (requires Visa instruction flow)

Available options:

`vgs`,

`visa`

[​](#response-status-one-of-0)

status

Type: `string | null`  
Mandate status: 'active' or 'pending_visa_instruction'
