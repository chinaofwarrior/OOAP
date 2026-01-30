# Get API Key Details
![Lux Divider](../../../assets/lux/divider.svg)

GET /api/v2/api-keys/{key_id}

**Summary:** Get API Key Details

```
curl --request GET \
  --url https://api.example.com/api/v2/api-keys/{key_id} \
  --header 'Authorization: Bearer <token>'
```

```
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

[​](#parameter-key-id)

key\_id

Type: `string`  
Required  
The unique identifier of the API key (UUID format).

Example:

`"07f5aec0-3ec3-441f-a098-912d201d067d"`

#### Response

Successful Response

Model for API key information (V2).

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
