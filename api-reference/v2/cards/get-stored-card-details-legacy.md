# Get Stored Card Details (Legacy)

GET /api/v2/wallet/
{user\_id}

card-details

Get Stored Card Details (Legacy)

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

PublicKeyAuthPublicKeyAuth

[​](#authorization-x-public-key)

X-Public-Key

string

header

required

Public key for card collection operations

#### Path Parameters

[​](#parameter-user-id)

user\_id

string

required

#### Response

CardDetailsResponse · object | null

Safe card details (last 4 digits only) or null if not found

Response model for card details (no sensitive data).

[​](#response-one-of-0-id)

id

string

required

Unique card identifier

[​](#response-one-of-0-card-holder)

card\_holder

string

required

Card holder name

Required string length: `1 - 255`

[​](#response-one-of-0-card-exp)

card\_exp

string

required

Card expiration (MM/YY)

[​](#response-one-of-0-email)

email

string<email>

required

Cardholder email

[​](#response-one-of-0-phone-number)

phone\_number

string<phone>

required

Phone number in E.164 format

Examples:

`"+12125551234"`

`"+442071234567"`

`"+972547828353"`

[​](#response-one-of-0-billing-address)

billing\_address

string

required

Billing address

Minimum string length: `1`

[​](#response-one-of-0-zip-code)

zip\_code

string

required

ZIP code

[​](#response-one-of-0-is-default)

is\_default

boolean

default:false

Default payment method flag

[​](#response-one-of-0-is-active)

is\_active

boolean

default:true

Active status (soft delete flag)

[​](#response-one-of-0-created-at-one-of-0)

created\_at

string<date-time> | null

Creation timestamp

[​](#response-one-of-0-updated-at-one-of-0)

updated\_at

string<date-time> | null

Last update timestamp

[​](#response-one-of-0-last4-digits-one-of-0)

last4\_digits

string | null

Last 4 digits

[​](#response-one-of-0-city-one-of-0)

city

string | null

City

Minimum string length: `1`

[​](#response-one-of-0-state-one-of-0)

state

string | null

State/province code

[​](#response-one-of-0-card-brand-one-of-0)

card\_brand

string | null

Card network (visa, mastercard, amex, discover, diners, jcb, unionpay, maestro, mir, verve, dankort, troy, other)
