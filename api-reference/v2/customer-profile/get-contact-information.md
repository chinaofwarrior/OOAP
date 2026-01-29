# Get Contact Information

GET /api/v2/wallet/contact
Get Contact Information

```
curl --request GET \
  --url https://api.example.com/api/v2/wallet/contact \
  --header 'X-Public-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>'
```

```
{
  "firstName": "<string>",
  "email": "[email protected]",
  "phone": "<string>",
  "lastName": "Doe"
}
```

#### Authorizations

PublicKeyAuthPublicKeyAuth

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

#### Response

Contact information retrieved successfully

Customer contact information for responses - backward compatible.

[​](#response-first-name)

firstName

string

required

Required string length: `1 - 100`

Example:

`"John"`

[​](#response-email)

email

string<email>

required

Example:

`"[email protected]"`

[​](#response-phone)

phone

string<phone>

required

Phone number in E.164 format

Example:

`"+1-555-123-4567"`

[​](#response-last-name-one-of-0)

lastName

string | null

Maximum string length: `100`

Example:

`"Doe"`
