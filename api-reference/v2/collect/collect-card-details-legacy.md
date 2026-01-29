# Collect Card Details (Legacy)

POST /api/v2/wallet/cards/collect

**Summary:** Collect Card Details (Legacy)

```
curl --request POST \
  --url https://api.example.com/api/v2/wallet/cards/collect \
  --header 'Content-Type: application/json' \
  --header 'X-Public-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>' \
  --data '
{
  "contactInfo": {
    "firstName": "<string>",
    "lastName": "<string>",
    "email": "[email protected]",
    "phone": "<string>"
  },
  "shippingAddress": {
    "addressLine1": "<string>",
    "city": "<string>",
    "state": "<string>",
    "zipCode": "<string>",
    "addressLine2": "Apt 4B",
    "county": "New York County",
    "country": "US",
    "isDefault": true
  },
  "paymentMethod": {
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
  },
  "_is_legacy_format": false
}
'
```

```
{
  "status": "<string>",
  "message": "<string>",
  "data": {},
  "request_id": "<string>",
  "id": "<string>"
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

#### Body

application/json

Request to collect customer information in one call.

Supports both new nested format and legacy flat format for backward compatibility.

[​](#body-contact-info)

contactInfo

Type: `ContactInfo` (object)  
Required  
Customer contact information.

Show child attributes

[​](#body-shipping-address-one-of-0)

shippingAddress

Type: `ShippingAddress` (object)  
Shipping address with default flag.

Show child attributes

[​](#body-payment-method-one-of-0)

paymentMethod

Type: `PaymentMethodRequest` (object)  
Request to add a payment method.

Show child attributes

[​](#body-is-legacy-format)

\_is\_legacy\_format

Type: `boolean`  
Default: `false`

#### Response

Confirmation of card collection with tokenized reference

Legacy payment collection response (deprecated).

[​](#response-status)

status

Type: `string`  
Required

[​](#response-message)

message

Type: `string`  
Required

[​](#response-data-one-of-0)

data

Type: `Data` (object)

[​](#response-request-id-one-of-0)

request\_id

Type: `string | null`

[​](#response-id-one-of-0)

id

Type: `string | null`
