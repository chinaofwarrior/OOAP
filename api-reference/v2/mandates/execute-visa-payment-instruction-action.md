# Execute Visa Payment Instruction Action

POST /api/v2/mandate/action

**Summary:** Execute Visa Payment Instruction Action

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

Request for /mandate/action endpoint.

[​](#body-action)

action

Type: `enum<string>`  
Required

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

Type: `string<uuid>`  
Required

[​](#body-mandate-id-one-of-0)

mandate\_id

Type: `string | null`

[​](#body-session-context-one-of-0)

session\_context

Type: `Session Context` (object)

[​](#body-browser-data-one-of-0)

browser\_data

Type: `Browser Data` (object)

[​](#body-otp-value-one-of-0)

otp\_value

Type: `string | null`

[​](#body-otp-identifier-one-of-0)

otp\_identifier

Type: `string | null`

[​](#body-assurance-identifier-one-of-0)

assurance\_identifier

Type: `string | null`

[​](#body-fido-assertion-data-one-of-0)

fido\_assertion\_data

Type: `string | null`

[​](#body-dfp-session-id-one-of-0)

dfp\_session\_id

Type: `string | null`

[​](#body-conversation-context-one-of-0)

conversation\_context

Type: `string | null`

[​](#body-mandate-one-of-0)

mandate

Type: `MandateData` (object)  
Mandate data for payment instruction.

Show child attributes

[​](#body-transaction-id-one-of-0)

transaction\_id

Type: `string | null`

#### Response

Stage-specific response from Visa service
