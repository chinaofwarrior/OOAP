# Revoke API Key
![Lux Divider](../../../assets/lux/divider.svg)

PUT /api/v2/api-keys/{key_id}/revoke

**Summary:** Revoke API Key

```
curl --request PUT \
  --url https://api.example.com/api/v2/api-keys/{key_id}/revoke \
  --header 'Authorization: Bearer <token>'
```

```
{
  "id": "<string>",
  "org_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
  "name": "<string>",
  "is_revoked": true,
  "created_at": "2023-11-07T05:31:56Z",
  "description": "<string>",
  "expires_at": "2023-11-07T05:31:56Z",
  "last_used_at": "2023-11-07T05:31:56Z"
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

Model for API key revocation information (V2).

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

[​](#response-is-revoked)

is\_revoked

Type: `boolean`  
Required

[​](#response-created-at)

created\_at

Type: `string<date-time>`  
Required

[​](#response-description-one-of-0)

description

Type: `string | null`

[​](#response-expires-at-one-of-0)

expires\_at

Type: `string<date-time> | null`

[​](#response-last-used-at-one-of-0)

last\_used\_at

Type: `string<date-time> | null`
