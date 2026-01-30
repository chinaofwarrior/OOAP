# Add Payment Method
![Lux Divider](../../../assets/lux/divider.svg)

POST /api/v2/wallet/payment-methods

**Summary:** Add Payment Method

```
curl --request POST \
  --url https://api.example.com/api/v2/wallet/payment-methods \
  --header 'Content-Type: application/json' \
  --header 'X-Public-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>' \
  --data '
{
  "paymentMethod": {
    "cardNumber": "<string>",
    "cvv": "<string>",
    "expiryDate": "<string>",
    "cardHolderName": "<string>"
  },
  "billingAddress": {
    "addressLine1": "<string>",
    "city": "<string>",
    "state": "<string>",
    "zipCode": "<string>",
    "addressLine2": "Apt 4B",
    "county": "New York County",
    "country": "US"
  },
  "metadata": {
    "isDefault": true,
    "isActive": true,
    "billingSameAsShipping": false
  }
}
'
```

```
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

Request to add a payment method.

[​](#body-payment-method)

paymentMethod

Type: `PaymentMethod` (object)  
Required  
Payment method with sensitive card data (for requests only).

Show child attributes

[​](#body-billing-address)

billingAddress

Type: `BillingAddress` (object)  
Required  
Billing address (same as base Address).

Show child attributes

[​](#body-metadata-one-of-0)

metadata

Type: `PaymentMethodMetadata` (object)  
Payment method metadata flags.

Show child attributes

#### Response

Payment method created successfully

Payment method response (no sensitive data).

[​](#response-id)

id

Type: `string`  
Required  
Unique identifier for the payment method. Generated as an idempotency key based on card details to prevent duplicates.

Example:

`"pm_1234567890abcdef"`

[​](#response-card-type)

cardType

Type: `string`  
Required  
Card type

Example:

`"visa"`

[​](#response-last-four-digits)

lastFourDigits

Type: `string`  
Required  
Example:

`"1111"`

[​](#response-expiry-date)

expiryDate

Type: `string`  
Required  
Example:

`"12/25"`

[​](#response-card-holder-name)

cardHolderName

Type: `string`  
Required  
Example:

`"John Doe"`

[​](#response-is-default)

isDefault

Type: `boolean`  
Required  
Example:

`false`

[​](#response-is-active)

isActive

Type: `boolean`  
Required  
Example:

`true`

[​](#response-billing-address)

billingAddress

Type: `BillingAddress` (object)  
Required  
Billing address (same as base Address).

Show child attributes

[​](#response-created-at)

createdAt

Type: `string<date-time>`  
Required  
Example:

`"2024-01-15T10:30:00Z"`

[​](#response-updated-at)

updatedAt

Type: `string<date-time>`  
Required  
Example:

`"2024-01-15T10:30:00Z"`

[​](#response-cvv-available-until-one-of-0)

cvvAvailableUntil

Type: `string<date-time> | null`  
ISO 8601 timestamp with timezone until CVV is available (60 min after creation/update)

Example:

`"2024-01-15T11:30:00Z"`

[​](#response-pm-type)

pmType

Type: `enum<string>`  
Default: `vgs`  
Vault type: 'vgs' (default VGS vault) or 'visa' (Visa VTS tokenized)

Available options:

`vgs`,

`visa`
