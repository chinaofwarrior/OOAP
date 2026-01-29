# Delete API Key

DELETE /api/v2/api-keys/
{key\_id}

Delete API Key

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

BearerAuthBearerAuth

[​](#authorization-authorization)

Authorization

string

header

required

JWT Bearer token from Auth0 authentication

#### Path Parameters

[​](#parameter-key-id)

key\_id

string

required

The unique identifier of the API key (UUID format).

Example:

`"07f5aec0-3ec3-441f-a098-912d201d067d"`

#### Response

API key successfully deleted
