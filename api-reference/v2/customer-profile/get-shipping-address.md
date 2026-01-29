# Get Shipping Address

GET /api/v2/wallet/shipping-address
Get Shipping Address

```
curl --request GET \
  --url https://api.example.com/api/v2/wallet/shipping-address \
  --header 'X-Public-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>'
```

```
{
  "addressLine1": "<string>",
  "city": "<string>",
  "state": "<string>",
  "zipCode": "<string>",
  "addressLine2": "Apt 4B",
  "county": "New York County",
  "country": "US",
  "isDefault": true
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

Shipping address retrieved successfully

Shipping address with default flag.

[​](#response-address-line1)

addressLine1

string

required

Required string length: `1 - 200`

Example:

`"123 Main St"`

[​](#response-city)

city

string

required

Required string length: `1 - 100`

Example:

`"New York"`

[​](#response-state)

state

string

required

Required string length: `2 - 50`

Example:

`"NY"`

[​](#response-zip-code)

zipCode

string

required

Example:

`"10001"`

[​](#response-address-line2-one-of-0)

addressLine2

string | null

Maximum string length: `200`

Example:

`"Apt 4B"`

[​](#response-county-one-of-0)

county

string | null

Maximum string length: `100`

Example:

`"New York County"`

[​](#response-country)

country

string

default:US

ISO 3166-1 alpha-2 country code

Required string length: `2`

Example:

`"US"`

[​](#response-is-default)

isDefault

boolean

default:true

Whether this is the default shipping address
