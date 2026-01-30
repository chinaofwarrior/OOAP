# Create API Key
![Lux Divider](../../../assets/lux/divider.svg)

POST /api/v2/api-keys

**Summary:** Create API Key

```
curl --request POST \
  --url https://api.example.com/api/v2/api-keys/ \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "name": "<string>",
  "description": "<string>"
}
'
```

```
{
  "id": "<string>",
  "org_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
  "name": "<string>",
  "public_key": "<string>",
  "private_key_display": "<string>",
  "created_at": "2023-11-07T05:31:56Z",
  "private_key": "<string>",
  "description": "<string>",
  "is_revoked": false,
  "revoked_at": "2023-11-07T05:31:56Z",
  "last_used_at": "2023-11-07T05:31:56Z",
  "environment": "<string>"
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

#### Body

application/json

Request model for creating a new API key (V2).

[​](#body-name)

name

Type: `string`  
Required  
A user-friendly name for the API key.

Required string length: `1 - 100`

[​](#body-description-one-of-0)

description

Type: `string | null`  
An optional description for the API key.

Maximum string length: `255`

#### Response

Successful Response

V2 API Key Create Response - uses private\_key field name (same as V1).
V2 may include additional validation or fields in the future.

[​](#response-id)

id

Type: `string`  
Required

[​](#response-org-id)

org\_id

Type: `string<uuid>`  
Required

[​](#response-name)

name

Type: `string`  
Required

[​](#response-public-key)

public\_key

Type: `string`  
Required

[​](#response-private-key-display)

private\_key\_display

Type: `string`  
Required

[​](#response-created-at)

created\_at

Type: `string<date-time>`  
Required

[​](#response-private-key)

private\_key

Type: `string`  
Required  
The private key for authentication

[​](#response-description-one-of-0)

description

Type: `string | null`

[​](#response-is-revoked)

is\_revoked

Type: `boolean`  
Default: `false`

[​](#response-revoked-at-one-of-0)

revoked\_at

Type: `string<date-time> | null`

[​](#response-last-used-at-one-of-0)

last\_used\_at

Type: `string<date-time> | null`

[​](#response-environment-one-of-0)

environment

Type: `string | null`
