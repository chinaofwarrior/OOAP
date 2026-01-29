# Reveal Card Details

GET /api/v2/wallet/
reveal\_card\_details

Reveal Card Details

```
curl --request GET \
  --url https://api.example.com/api/v2/wallet/reveal_card_details \
  --header 'Authorization: Bearer <token>'
```

```
{
  "billing_address": "123 Main Street",
  "card_cvv": "123",
  "card_exp": "12/25",
  "card_holder": "John Doe",
  "card_number": "4111111111111111",
  "city": "New York",
  "email": "[email protected]",
  "id": "card_12345",
  "is_active": true,
  "is_default": true,
  "last4_digits": "1111",
  "phone_number": "+12125551234",
  "state": "NY",
  "zip_code": "10001"
}
```

#### Authorizations

ShortLivedTokenAuthShortLivedTokenAuth

[​](#authorization-authorization)

Authorization

string

header

required

Short-lived token obtained from /request\_card\_reveal\_token endpoint

#### Response

Full card details including card number (sensitive data)

* CardRevealResponse
* VisaCardRevealResponse

Response model for revealed card data (contains sensitive information).

[​](#response-one-of-0-card-number)

card\_number

string

required

Card number

Required string length: `12 - 19`

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

[​](#response-one-of-0-card-cvv-one-of-0)

card\_cvv

string | null

CVV code

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

[​](#response-one-of-0-id-one-of-0)

id

string | null

Card identifier

[​](#response-one-of-0-is-default-one-of-0)

is\_default

boolean | null

Default flag

[​](#response-one-of-0-is-active-one-of-0)

is\_active

boolean | null

Active status

[​](#response-one-of-0-is-visa-payment)

is\_visa\_payment

boolean

default:false

Whether this is a Visa-tokenized payment
