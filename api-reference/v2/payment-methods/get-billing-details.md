# Get Billing Details
![Lux Divider](../../../assets/lux/divider.svg)

GET /api/v2/wallet/get_billing_details

**Summary:** Get Billing Details

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

ApiKeyAuth

[​](#authorization-x-api-key)

X-API-Key

Type: `string`  
Location: `header`  
Required  
Private API key for full access to SDK operations

#### Headers

[​](#parameter-x-user-id)

x-user-id

Type: `string`  
Required  
End-user identifier within a customer organization. Required for user-scoped operations.

#### Response

Billing address and customer contact information (no sensitive card data)

Response model for billing details (no sensitive card data).

[​](#response-user-id)

user\_id

Type: `string`  
Required  
User identifier

[​](#response-card-holder)

card\_holder

Type: `string`  
Required  
Card holder name

[​](#response-phone-number)

phone\_number

Type: `string`  
Required  
Phone number in E.164 format

[​](#response-billing-address)

billing\_address

Type: `string`  
Required  
Billing address

[​](#response-zip-code)

zip\_code

Type: `string`  
Required  
ZIP code

[​](#response-city-one-of-0)

city

Type: `string | null`  
City

[​](#response-state-one-of-0)

state

Type: `string | null`  
State/province code
