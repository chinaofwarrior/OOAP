# Add Payment Method

POST /api/v2/wallet/payment-methods
Add Payment Method

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

#### Body

application/json

Request to add a payment method.

[​](#body-payment-method)

paymentMethod

PaymentMethod · object

required

Payment method with sensitive card data (for requests only).

Show child attributes

[​](#body-billing-address)

billingAddress

BillingAddress · object

required

Billing address (same as base Address).

Show child attributes

[​](#body-metadata-one-of-0)

metadata

PaymentMethodMetadata · object

Payment method metadata flags.

Show child attributes

#### Response

Payment method created successfully

Payment method response (no sensitive data).

[​](#response-id)

id

string

required

Unique identifier for the payment method. Generated as an idempotency key based on card details to prevent duplicates.

Example:

`"pm_1234567890abcdef"`

[​](#response-card-type)

cardType

string

required

Card type

Example:

`"visa"`

[​](#response-last-four-digits)

lastFourDigits

string

required

Example:

`"1111"`

[​](#response-expiry-date)

expiryDate

string

required

Example:

`"12/25"`

[​](#response-card-holder-name)

cardHolderName

string

required

Example:

`"John Doe"`

[​](#response-is-default)

isDefault

boolean

required

Example:

`false`

[​](#response-is-active)

isActive

boolean

required

Example:

`true`

[​](#response-billing-address)

billingAddress

BillingAddress · object

required

Billing address (same as base Address).

Show child attributes

[​](#response-created-at)

createdAt

string<date-time>

required

Example:

`"2024-01-15T10:30:00Z"`

[​](#response-updated-at)

updatedAt

string<date-time>

required

Example:

`"2024-01-15T10:30:00Z"`

[​](#response-cvv-available-until-one-of-0)

cvvAvailableUntil

string<date-time> | null

ISO 8601 timestamp with timezone until CVV is available (60 min after creation/update)

Example:

`"2024-01-15T11:30:00Z"`

[​](#response-pm-type)

pmType

enum<string>

default:vgs

Vault type: 'vgs' (default VGS vault) or 'visa' (Visa VTS tokenized)

Available options:

`vgs`,

`visa`
