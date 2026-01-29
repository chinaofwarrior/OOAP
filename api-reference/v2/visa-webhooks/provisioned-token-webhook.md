# Provisioned Token Webhook

POST /api/v2/webhooks/visa/provisionedToken
Provisioned Token Webhook

```
curl --request POST \
  --url https://api.example.com/api/v2/webhooks/visa/provisionedToken \
  --header 'Content-Type: application/json' \
  --data '
{
  "date": 1733875200,
  "relationshipID": "rel_123456",
  "vProvisionedTokenID": "tok_abcdef123456"
}
'
```

#### Query Parameters

[​](#parameter-api-key)

apiKey

string

required

[​](#parameter-event-type)

eventType

string

required

#### Body

application/json

The body is of type `Payload · object`.

#### Response

Webhook successfully processed
