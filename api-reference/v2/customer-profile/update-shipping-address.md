# Update Shipping Address

PUT /api/v2/wallet/shipping-address

**Summary:** Update Shipping Address

```
curl --request PUT \
  --url https://api.example.com/api/v2/wallet/shipping-address \
  --header 'Content-Type: application/json' \
  --header 'X-Public-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>' \
  --data '
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
'
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

#### Body

application/json

Shipping address with default flag.

[​](#body-address-line1)

addressLine1

Type: `string`  
Required  
Required string length: `1 - 200`

Example:

`"123 Main St"`

[​](#body-city)

city

Type: `string`  
Required  
Required string length: `1 - 100`

Example:

`"New York"`

[​](#body-state)

state

Type: `string`  
Required  
Required string length: `2 - 50`

Example:

`"NY"`

[​](#body-zip-code)

zipCode

Type: `string`  
Required  
Example:

`"10001"`

[​](#body-address-line2-one-of-0)

addressLine2

Type: `string | null`  
Maximum string length: `200`

Example:

`"Apt 4B"`

[​](#body-county-one-of-0)

county

Type: `string | null`  
Maximum string length: `100`

Example:

`"New York County"`

[​](#body-country)

country

Type: `string`  
Default: `US`  
ISO 3166-1 alpha-2 country code

Required string length: `2`

Example:

`"US"`

[​](#body-is-default)

isDefault

Type: `boolean`  
Default: `true`  
Whether this is the default shipping address

#### Response

Shipping address created or updated successfully

Shipping address with default flag.

[​](#response-address-line1)

addressLine1

Type: `string`  
Required  
Required string length: `1 - 200`

Example:

`"123 Main St"`

[​](#response-city)

city

Type: `string`  
Required  
Required string length: `1 - 100`

Example:

`"New York"`

[​](#response-state)

state

Type: `string`  
Required  
Required string length: `2 - 50`

Example:

`"NY"`

[​](#response-zip-code)

zipCode

Type: `string`  
Required  
Example:

`"10001"`

[​](#response-address-line2-one-of-0)

addressLine2

Type: `string | null`  
Maximum string length: `200`

Example:

`"Apt 4B"`

[​](#response-county-one-of-0)

county

Type: `string | null`  
Maximum string length: `100`

Example:

`"New York County"`

[​](#response-country)

country

Type: `string`  
Default: `US`  
ISO 3166-1 alpha-2 country code

Required string length: `2`

Example:

`"US"`

[​](#response-is-default)

isDefault

Type: `boolean`  
Default: `true`  
Whether this is the default shipping address
