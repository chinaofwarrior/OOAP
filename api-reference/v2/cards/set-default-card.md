# Set Default Card

PUT /api/v2/wallet/cards/
{card\_id}

default

Set Default Card

```
curl --request PUT \
  --url https://api.example.com/api/v2/wallet/cards/{card_id}/default \
  --header 'X-Public-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>'
```

```
{
  "card_id": "card_12345",
  "message": "Card created successfully",
  "status": "success"
}
```

#### Authorizations

PublicKeyAuthPublicKeyAuthApiKeyAuth

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

#### Path Parameters

[​](#parameter-card-id)

card\_id

string

required

#### Response

Card set as default successfully

Response model for card operations (create/update/delete).

[​](#response-status)

status

string

required

Operation status

[​](#response-message)

message

string

required

Human-readable message

[​](#response-card-id-one-of-0)

card\_id

string | null

Affected card ID
