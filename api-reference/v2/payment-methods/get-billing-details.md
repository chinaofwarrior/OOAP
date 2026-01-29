# Get Billing Details

GET /api/v2/wallet/
get\_billing\_details

Get Billing Details

```
curl --request GET \
  --url https://api.example.com/api/v2/wallet/get_billing_details \
  --header 'X-API-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>'
```

```
{
  "billing_address": "123 Main Street",
  "card_holder": "John Doe",
  "city": "New York",
  "phone_number": "+12125551234",
  "state": "NY",
  "user_id": "user_12345",
  "zip_code": "10001"
}
```

#### Authorizations

ApiKeyAuthApiKeyAuth

[​](#authorization-x-api-key)

X-API-Key

string

header

required

Private API key for full access to SDK operations

#### Headers

[​](#parameter-x-user-id)

x-user-id

string

required

End-user identifier within a customer organization. Required for user-scoped operations.

#### Response

Billing address and customer contact information (no sensitive card data)

Response model for billing details (no sensitive card data).

[​](#response-user-id)

user\_id

string

required

User identifier

[​](#response-card-holder)

card\_holder

string

required

Card holder name

[​](#response-phone-number)

phone\_number

string

required

Phone number in E.164 format

[​](#response-billing-address)

billing\_address

string

required

Billing address

[​](#response-zip-code)

zip\_code

string

required

ZIP code

[​](#response-city-one-of-0)

city

string | null

City

[​](#response-state-one-of-0)

state

string | null

State/province code
