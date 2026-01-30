# PAN Metadata Webhook
![Lux Divider](../../../assets/lux/divider.svg)

POST /api/v2/webhooks/visa/panMetadata

**Summary:** PAN Metadata Webhook

```
curl --request POST \
  --url https://api.example.com/api/v2/webhooks/visa/panMetadata \
  --header 'Content-Type: application/json' \
  --data '
{
  "vPanEnrollmentID": "enroll_xyz789",
  "date": 1733875200
}
'
```

#### Query Parameters

[​](#parameter-api-key)

apiKey

Type: `string`  
Required

#### Body

application/json

The body is of type `Payload · object`.

#### Response

Webhook successfully processed
