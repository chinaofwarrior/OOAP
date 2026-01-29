# Delete payment method

DELETE /api/v2/wallet/payment-methods/{paymentMethodId}

**Summary:** Delete payment method

```
curl --request DELETE \
  --url https://api.example.com/api/v2/wallet/payment-methods/{paymentMethodId} \
  --header 'X-Public-Key: <api-key>' \
  --header 'x-user-id: <x-user-id>'
```

```
{
  "detail": [
    {
      "loc": [
        "<string>"
      ],
      "msg": "<string>",
      "type": "<string>"
    }
  ]
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

#### Path Parameters

[​](#parameter-payment-method-id)

paymentMethodId

Type: `string<uuid>`  
Required

#### Response

Payment method deleted successfully
