# Set Default Card

PUT /api/v2/wallet/cards/{card_id}/default

**Summary:** Set Default Card

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

PublicKeyAuth

[​](#authorization-x-public-key)

X-Public-Key

Type: `string`  
Location: `header`  
Required  
Public key for card collection operations

#### Headers

[​](#parameter-x-user-id)

x-user-id

Type: `string`  
Required  
End-user identifier within a customer organization. Required for user-scoped operations.

#### Path Parameters

[​](#parameter-card-id)

card\_id

Type: `string`  
Required

#### Response

Card set as default successfully

Response model for card operations (create/update/delete).

[​](#response-status)

status

Type: `string`  
Required  
Operation status

[​](#response-message)

message

Type: `string`  
Required  
Human-readable message

[​](#response-card-id-one-of-0)

card\_id

Type: `string | null`  
Affected card ID
