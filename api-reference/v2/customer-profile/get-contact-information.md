# Get Contact Information
![Lux Divider](../../../assets/lux/divider.svg)

GET /api/v2/wallet/contact

**Summary:** Get Contact Information

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

#### Response

Contact information retrieved successfully

Customer contact information for responses - backward compatible.

[​](#response-first-name)

firstName

Type: `string`  
Required  
Required string length: `1 - 100`

Example:

`"John"`

[​](#response-email)

email

Type: `string<email>`  
Required  
Example:

`"[email protected]"`

[​](#response-phone)

phone

Type: `string<phone>`  
Required  
Phone number in E.164 format

Example:

`"+1-555-123-4567"`

[​](#response-last-name-one-of-0)

lastName

Type: `string | null`  
Maximum string length: `100`

Example:

`"Doe"`
