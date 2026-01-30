# List API Keys
![Lux Divider](../../../assets/lux/divider.svg)

GET /api/v2/api-keys

**Summary:** List API Keys

```
curl --request GET \
  --url https://api.example.com/api/v2/api-keys/ \
  --header 'Authorization: Bearer <token>'
```

```
[
  {
    "id": "<string>",
    "org_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
    "name": "<string>",
    "public_key": "<string>",
    "private_key_display": "<string>",
    "created_at": "2023-11-07T05:31:56Z",
    "description": "<string>",
    "is_revoked": false,
    "revoked_at": "2023-11-07T05:31:56Z",
    "last_used_at": "2023-11-07T05:31:56Z",
    "environment": "<string>"
  }
]
```

#### Authorizations

BearerAuth

[​](#authorization-authorization)

Authorization

Type: `string`  
Location: `header`  
Required  
JWT Bearer token from Auth0 authentication

#### Response

Successful Response

[​](#response-items-id)

id

Type: `string`  
Required

[​](#response-items-org-id)

org\_id

Type: `string<uuid>`  
Required

[​](#response-items-name)

name

Type: `string`  
Required

[​](#response-items-public-key)

public\_key

Type: `string`  
Required

[​](#response-items-private-key-display)

private\_key\_display

Type: `string`  
Required

[​](#response-items-created-at)

created\_at

Type: `string<date-time>`  
Required

[​](#response-items-description-one-of-0)

description

Type: `string | null`

[​](#response-items-is-revoked)

is\_revoked

Type: `boolean`  
Default: `false`

[​](#response-items-revoked-at-one-of-0)

revoked\_at

Type: `string<date-time> | null`

[​](#response-items-last-used-at-one-of-0)

last\_used\_at

Type: `string<date-time> | null`

[​](#response-items-environment-one-of-0)

environment

Type: `string | null`
