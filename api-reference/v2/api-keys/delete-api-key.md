# Delete API Key
![Lux Divider](../../../assets/lux/divider.svg)

DELETE /api/v2/api-keys/{key_id}

**Summary:** Delete API Key

```
curl --request DELETE \
  --url https://api.example.com/api/v2/api-keys/{key_id} \
  --header 'Authorization: Bearer <token>'
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

BearerAuth

[​](#authorization-authorization)

Authorization

Type: `string`  
Location: `header`  
Required  
JWT Bearer token from Auth0 authentication

#### Path Parameters

[​](#parameter-key-id)

key\_id

Type: `string`  
Required  
The unique identifier of the API key (UUID format).

Example:

`"07f5aec0-3ec3-441f-a098-912d201d067d"`

#### Response

API key successfully deleted
