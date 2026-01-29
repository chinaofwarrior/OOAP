# Get All Cards

GET /api/v2/wallet/cards
Get All Cards

```
curl --request GET \
  --url https://api.example.com/api/v2/wallet/cards \
  --header 'X-Public-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>'
```

```
{
  "cards": [
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
  ],
  "total": 1
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

List of cards retrieved successfully

Response model for listing multiple cards.

[​](#response-cards)

cards

CardDetailsResponse · object[]

required

List of cards

Show child attributes

[​](#response-total)

total

integer

required

Total number of cards

Required range: `x >= 0`
