# Get Default Card

GET /api/v2/wallet/cards/default
Get Default Card

```
curl --request GET \
  --url https://api.example.com/api/v2/wallet/cards/default \
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

PublicKeyAuthPublicKeyAuthApiKeyAuth

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

Default card retrieved successfully

Response model for card details (no sensitive data).

[​](#response-id)

id

string

required

Unique card identifier

[​](#response-card-holder)

card\_holder

string

required

Card holder name

Required string length: `1 - 255`

[​](#response-card-exp)

card\_exp

string

required

Card expiration (MM/YY)

[​](#response-email)

email

string<email>

required

Cardholder email

[​](#response-phone-number)

phone\_number

string<phone>

required

Phone number in E.164 format

Examples:

`"+12125551234"`

`"+442071234567"`

`"+972547828353"`

[​](#response-billing-address)

billing\_address

string

required

Billing address

Minimum string length: `1`

[​](#response-zip-code)

zip\_code

string

required

ZIP code

[​](#response-is-default)

is\_default

boolean

default:false

Default payment method flag

[​](#response-is-active)

is\_active

boolean

default:true

Active status (soft delete flag)

[​](#response-created-at-one-of-0)

created\_at

string<date-time> | null

Creation timestamp

[​](#response-updated-at-one-of-0)

updated\_at

string<date-time> | null

Last update timestamp

[​](#response-last4-digits-one-of-0)

last4\_digits

string | null

Last 4 digits

[​](#response-city-one-of-0)

city

string | null

City

Minimum string length: `1`

[​](#response-state-one-of-0)

state

string | null

State/province code

[​](#response-card-brand-one-of-0)

card\_brand

string | null

Card network (visa, mastercard, amex, discover, diners, jcb, unionpay, maestro, mir, verve, dankort, troy, other)
