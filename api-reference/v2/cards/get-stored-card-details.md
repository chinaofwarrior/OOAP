# Get Stored Card Details

GET /api/v2/wallet/cards/stored

**Summary:** Get Stored Card Details

```
curl --request GET \
  --url https://api.example.com/api/v2/wallet/cards/stored \
  --header 'X-Public-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>'
```

```
{
  "billing_address": "123 Main Street",
  "card_brand": "visa",
  "card_exp": "12/25",
  "card_holder": "John Doe",
  "city": "New York",
  "created_at": "2023-01-01T00:00:00Z",
  "email": "[email protected]",
  "id": "card_12345",
  "is_active": true,
  "is_default": true,
  "last4_digits": "1111",
  "phone_number": "+12125551234",
  "state": "NY",
  "updated_at": "2023-01-02T00:00:00Z",
  "zip_code": "10001"
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

Stored card retrieved successfully

Response model for card details (no sensitive data).

[​](#response-id)

id

Type: `string`  
Required  
Unique card identifier

[​](#response-card-holder)

card\_holder

Type: `string`  
Required  
Card holder name

Required string length: `1 - 255`

[​](#response-card-exp)

card\_exp

Type: `string`  
Required  
Card expiration (MM/YY)

[​](#response-email)

email

Type: `string<email>`  
Required  
Cardholder email

[​](#response-phone-number)

phone\_number

Type: `string<phone>`  
Required  
Phone number in E.164 format

Examples:

`"+12125551234"`

`"+442071234567"`

`"+972547828353"`

[​](#response-billing-address)

billing\_address

Type: `string`  
Required  
Billing address

Minimum string length: `1`

[​](#response-zip-code)

zip\_code

Type: `string`  
Required  
ZIP code

[​](#response-is-default)

is\_default

Type: `boolean`  
Default: `false`  
Default payment method flag

[​](#response-is-active)

is\_active

Type: `boolean`  
Default: `true`  
Active status (soft delete flag)

[​](#response-created-at-one-of-0)

created\_at

Type: `string<date-time> | null`  
Creation timestamp

[​](#response-updated-at-one-of-0)

updated\_at

Type: `string<date-time> | null`  
Last update timestamp

[​](#response-last4-digits-one-of-0)

last4\_digits

Type: `string | null`  
Last 4 digits

[​](#response-city-one-of-0)

city

Type: `string | null`  
City

Minimum string length: `1`

[​](#response-state-one-of-0)

state

Type: `string | null`  
State/province code

[​](#response-card-brand-one-of-0)

card\_brand

Type: `string | null`  
Card network (visa, mastercard, amex, discover, diners, jcb, unionpay, maestro, mir, verve, dankort, troy, other)
