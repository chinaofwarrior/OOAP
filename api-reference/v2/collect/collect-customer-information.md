# Collect customer information

POST /api/v2/wallet/collect

**Summary:** Collect customer information

```
curl --request POST \
  --url https://api.example.com/api/v2/wallet/collect \
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
  "userId": "<string>",
  "createdAt": "2023-11-07T05:31:56Z",
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
    "id": "<string>",
    "cardType": "<string>",
    "lastFourDigits": "<string>",
    "expiryDate": "<string>",
    "cardHolderName": "<string>",
    "isDefault": true,
    "isActive": true,
    "billingAddress": {
      "addressLine1": "<string>",
      "city": "<string>",
      "state": "<string>",
      "zipCode": "<string>",
      "addressLine2": "Apt 4B",
      "county": "New York County",
      "country": "US"
    },
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "cvvAvailableUntil": "2024-01-15T11:30:00Z",
    "pmType": "vgs"
  }
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

[​](#parameter-one-of-0)

x-request-id

Type: `string | null`  
Unique request identifier for tracing and debugging. Auto-generated if not provided.

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

Customer data successfully collected

* CustomerCollectResponse
* PaymentCollectionResponse

Response from collecting customer information.

[​](#response-one-of-0-user-id)

userId

Type: `string`  
Required  
The user ID associated with this wallet data

Example:

`"user_1234567890abcdef"`

[​](#response-one-of-0-created-at)

createdAt

Type: `string<date-time>`  
Required  
Example:

`"2024-01-15T10:30:00Z"`

[​](#response-one-of-0-contact-info-one-of-0)

contactInfo

ContactInfo · object

Customer contact information.

Show child attributes

[​](#response-one-of-0-shipping-address-one-of-0)

shippingAddress

ShippingAddress · object

Shipping address with default flag.

Show child attributes

[​](#response-one-of-0-payment-method-one-of-0)

paymentMethod

PaymentMethodResponse · object

Payment method response (no sensitive data).

Show child attributes
