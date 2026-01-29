# Update Card Information

PATCH /api/v2/wallet/cards/
{card\_id}

Update Card Information

```
curl --request PATCH \
  --url https://api.example.com/api/v2/wallet/cards/{card_id} \
  --header 'Content-Type: application/json' \
  --header 'X-Public-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>' \
  --data '
{
  "billing_address": "456 New Street",
  "card_holder": "Jane Doe",
  "city": "San Francisco",
  "email": "[email protected]",
  "phone_number": "+14155551234",
  "state": "CA",
  "zip_code": "94105"
}
'
```

```
{
  "card_id": "card_12345",
  "message": "Card created successfully",
  "status": "success"
}
```

#### Authorizations

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

#### Path Parameters

[​](#parameter-card-id)

card\_id

string

required

#### Body

application/json

Request model for updating card information - all fields optional.

[​](#body-email-one-of-0)

email

string<email> | null

Update cardholder email

[​](#body-card-holder-one-of-0)

card\_holder

string | null

Update cardholder name

Required string length: `1 - 255`

[​](#body-phone-number-one-of-0)

phone\_number

string<phone> | null

Phone number in E.164 format (e.g., +12125551234)

Example:

`"+12125551234"`

[​](#body-billing-address-one-of-0)

billing\_address

string | null

Update billing address

Minimum string length: `1`

[​](#body-city-one-of-0)

city

string | null

Update city

Minimum string length: `1`

[​](#body-state-one-of-0)

state

string | null

Update state

[​](#body-zip-code-one-of-0)

zip\_code

string | null

Update ZIP code

#### Response

Card billing info updated successfully

Response model for card operations (create/update/delete).

[​](#response-status)

status

string

required

Operation status

[​](#response-message)

message

string

required

Human-readable message

[​](#response-card-id-one-of-0)

card\_id

string | null

Affected card ID
