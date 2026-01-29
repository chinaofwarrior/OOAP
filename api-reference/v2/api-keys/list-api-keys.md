# List API Keys

GET /api/v2/api-keys
List API Keys

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

BearerAuthBearerAuth

[​](#authorization-authorization)

Authorization

string

header

required

JWT Bearer token from Auth0 authentication

#### Response

Successful Response

[​](#response-items-id)

id

string

required

[​](#response-items-org-id)

org\_id

string<uuid>

required

[​](#response-items-name)

name

string

required

[​](#response-items-public-key)

public\_key

string

required

[​](#response-items-private-key-display)

private\_key\_display

string

required

[​](#response-items-created-at)

created\_at

string<date-time>

required

[​](#response-items-description-one-of-0)

description

string | null

[​](#response-items-is-revoked)

is\_revoked

boolean

default:false

[​](#response-items-revoked-at-one-of-0)

revoked\_at

string<date-time> | null

[​](#response-items-last-used-at-one-of-0)

last\_used\_at

string<date-time> | null

[​](#response-items-environment-one-of-0)

environment

string | null
