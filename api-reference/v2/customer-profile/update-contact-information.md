# Update Contact Information

PUT /api/v2/wallet/contact

**Summary:** Update Contact Information

```
curl --request PUT \
  --url https://api.example.com/api/v2/wallet/contact \
  --header 'Content-Type: application/json' \
  --header 'X-Public-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>' \
  --data '
{
  "firstName": "<string>",
  "lastName": "<string>",
  "email": "[email protected]",
  "phone": "<string>"
}
'
```

```
{
  "firstName": "<string>",
  "lastName": "<string>",
  "email": "[email protected]",
  "phone": "<string>"
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

Customer contact information.

[​](#body-first-name)

firstName

Type: `string`  
Required  
Required string length: `1 - 100`

Example:

`"John"`

[​](#body-last-name)

lastName

Type: `string`  
Required  
Required string length: `1 - 100`

Example:

`"Doe"`

[​](#body-email)

email

Type: `string<email>`  
Required  
Example:

`"[email protected]"`

[​](#body-phone)

phone

Type: `string<phone>`  
Required  
Phone number in E.164 format

Example:

`"+1-555-123-4567"`

#### Response

Contact information created or updated successfully

Customer contact information.

[​](#response-first-name)

firstName

Type: `string`  
Required  
Required string length: `1 - 100`

Example:

`"John"`

[​](#response-last-name)

lastName

Type: `string`  
Required  
Required string length: `1 - 100`

Example:

`"Doe"`

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
