# Revoke API Key

PUT /api/v2/api-keys/
{key\_id}

revoke

Revoke API Key

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

BearerAuthBearerAuth

[​](#authorization-authorization)

Authorization

string

header

required

JWT Bearer token from Auth0 authentication

#### Path Parameters

[​](#parameter-key-id)

key\_id

string

required

The unique identifier of the API key (UUID format).

Example:

`"07f5aec0-3ec3-441f-a098-912d201d067d"`

#### Response

Successful Response

Model for API key revocation information (V2).

[​](#response-id)

id

string

required

[​](#response-org-id)

org\_id

string<uuid>

required

[​](#response-name)

name

string

required

[​](#response-is-revoked)

is\_revoked

boolean

required

[​](#response-created-at)

created\_at

string<date-time>

required

[​](#response-description-one-of-0)

description

string | null

[​](#response-expires-at-one-of-0)

expires\_at

string<date-time> | null

[​](#response-last-used-at-one-of-0)

last\_used\_at

string<date-time> | null
