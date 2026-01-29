# Delete payment method

DELETE /api/v2/wallet/payment-methods/
{paymentMethodId}

Delete payment method

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

PublicKeyAuthPublicKeyAuth

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

[​](#parameter-payment-method-id)

paymentMethodId

string<uuid>

required

#### Response

Payment method deleted successfully
