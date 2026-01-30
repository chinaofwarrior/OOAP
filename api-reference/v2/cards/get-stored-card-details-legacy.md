# Get Stored Card Details (Legacy)

GET /api/v2/wallet/{user_id}/card-details

**Summary:** Get Stored Card Details (Legacy)

```
curl --request GET \
  --url https://api.example.com/api/v2/wallet/{user_id}/card-details \
  --header 'X-Public-Key: <api-key>'
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

#### Path Parameters

[​](#parameter-user-id)

user\_id

Type: `string`  
Required

#### Response

CardDetailsResponse · object | null

Safe card details (last 4 digits only) or null if not found

Response model for card details (no sensitive data).

[​](#response-one-of-0-id)

id

Type: `string`  
Required  
Unique card identifier

[​](#response-one-of-0-card-holder)

card\_holder

Type: `string`  
Required  
Card holder name

Required string length: `1 - 255`

[​](#response-one-of-0-card-exp)

card\_exp

Type: `string`  
Required  
Card expiration (MM/YY)

[​](#response-one-of-0-email)

email

Type: `string<email>`  
Required  
Cardholder email

[​](#response-one-of-0-phone-number)

phone\_number

Type: `string<phone>`  
Required  
Phone number in E.164 format

Examples:

`"+12125551234"`

`"+442071234567"`

`"+972547828353"`

[​](#response-one-of-0-billing-address)

billing\_address

Type: `string`  
Required  
Billing address

Minimum string length: `1`

[​](#response-one-of-0-zip-code)

zip\_code

Type: `string`  
Required  
ZIP code

[​](#response-one-of-0-is-default)

is\_default

Type: `boolean`  
Default: `false`  
Default payment method flag

[​](#response-one-of-0-is-active)

is\_active

Type: `boolean`  
Default: `true`  
Active status (soft delete flag)

[​](#response-one-of-0-created-at-one-of-0)

created\_at

Type: `string<date-time> | null`  
Creation timestamp

[​](#response-one-of-0-updated-at-one-of-0)

updated\_at

Type: `string<date-time> | null`  
Last update timestamp

[​](#response-one-of-0-last4-digits-one-of-0)

last4\_digits

Type: `string | null`  
Last 4 digits

[​](#response-one-of-0-city-one-of-0)

city

Type: `string | null`  
City

Minimum string length: `1`

[​](#response-one-of-0-state-one-of-0)

state

Type: `string | null`  
State/province code

[​](#response-one-of-0-card-brand-one-of-0)

card\_brand

Type: `string | null`  
Card network (visa, mastercard, amex, discover, diners, jcb, unionpay, maestro, mir, verve, dankort, troy, other)
