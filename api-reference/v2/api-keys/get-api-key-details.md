# Get API Key Details

GET /api/v2/api-keys/
{key\_id}

Get API Key Details

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

Model for API key information (V2).

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

[​](#response-public-key)

public\_key

string

required

[​](#response-private-key-display)

private\_key\_display

string

required

[​](#response-created-at)

created\_at

string<date-time>

required

[​](#response-description-one-of-0)

description

string | null

[​](#response-is-revoked)

is\_revoked

boolean

default:false

[​](#response-revoked-at-one-of-0)

revoked\_at

string<date-time> | null

[​](#response-last-used-at-one-of-0)

last\_used\_at

string<date-time> | null

[​](#response-environment-one-of-0)

environment

string | null
