# Request Card Reveal Token

POST /api/v2/wallet/
request\_card\_reveal\_token

Request Card Reveal Token

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

```
{
  "token": "<string>",
  "expires_at": "2023-11-07T05:31:56Z"
}
```

#### Authorizations

ApiKeyAuthApiKeyAuth

[​](#authorization-x-api-key)

X-API-Key

string

header

required

Private API key for full access to SDK operations

#### Headers

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
