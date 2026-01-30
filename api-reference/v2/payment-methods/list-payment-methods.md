# List Payment Methods
![Lux Divider](../../../assets/lux/divider.svg)

GET /api/v2/wallet/payment-methods

**Summary:** List Payment Methods

```
curl --request GET \
  --url https://api.example.com/api/v2/wallet/payment-methods \
  --header 'X-Public-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>'
```

```
[
  {
    "id": "<string>",
    "cardType": "<string>",
    "lastFourDigits": "<string>",
    "expiryDate": "<string>",
    "cardHolderName": "<string>",
    "isDefault": true,
    "isActive": true,
    "billingAddress": {
      "addressLine1": "<string>",
      "city": "<string>",
      "state": "<string>",
      "zipCode": "<string>",
      "addressLine2": "Apt 4B",
      "county": "New York County",
      "country": "US"
    },
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "cvvAvailableUntil": "2024-01-15T11:30:00Z",
    "pmType": "vgs"
  }
]
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

#### Query Parameters

[​](#parameter-include-inactive)

includeInactive

Type: `boolean`  
Default: `false`

#### Response

Payment methods retrieved successfully

[​](#response-items-id)

id

Type: `string`  
Required  
Unique identifier for the payment method. Generated as an idempotency key based on card details to prevent duplicates.

Example:

`"pm_1234567890abcdef"`

[​](#response-items-card-type)

cardType

Type: `string`  
Required  
Card type

Example:

`"visa"`

[​](#response-items-last-four-digits)

lastFourDigits

Type: `string`  
Required  
Example:

`"1111"`

[​](#response-items-expiry-date)

expiryDate

Type: `string`  
Required  
Example:

`"12/25"`

[​](#response-items-card-holder-name)

cardHolderName

Type: `string`  
Required  
Example:

`"John Doe"`

[​](#response-items-is-default)

isDefault

Type: `boolean`  
Required  
Example:

`false`

[​](#response-items-is-active)

isActive

Type: `boolean`  
Required  
Example:

`true`

[​](#response-items-billing-address)

billingAddress

Type: `BillingAddress` (object)  
Required  
Billing address (same as base Address).

Show child attributes

[​](#response-items-created-at)

createdAt

Type: `string<date-time>`  
Required  
Example:

`"2024-01-15T10:30:00Z"`

[​](#response-items-updated-at)

updatedAt

Type: `string<date-time>`  
Required  
Example:

`"2024-01-15T10:30:00Z"`

[​](#response-items-cvv-available-until-one-of-0)

cvvAvailableUntil

Type: `string<date-time> | null`  
ISO 8601 timestamp with timezone until CVV is available (60 min after creation/update)

Example:

`"2024-01-15T11:30:00Z"`

[​](#response-items-pm-type)

pmType

Type: `enum<string>`  
Default: `vgs`  
Vault type: 'vgs' (default VGS vault) or 'visa' (Visa VTS tokenized)

Available options:

`vgs`,

`visa`
