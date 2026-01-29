# Get Card Analytics

GET /api/v2/card-analytics

**Summary:** Get Card Analytics

```
curl --request GET \
  --url https://api.example.com/api/v2/card-analytics \
  --header 'Authorization: Bearer <token>'
```

```
{
  "items": [
    {
      "user_id": "<string>",
      "masked_card_number": "<string>",
      "registration_date": "<string>",
      "card_type": "<string>",
      "last_updated": "<string>",
      "total_charges": 123,
      "status": "<string>",
      "is_deleted": true,
      "last_used": "<string>",
      "insights": "<string>"
    }
  ],
  "total": 123,
  "page": 123,
  "limit": 123,
  "total_pages": 123,
  "has_next": true,
  "has_previous": true
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

#### Query Parameters

[​](#parameter-page)

page

Type: `integer`  
Default: `1`

Page number (1-based)

Required range: `x >= 1`

[​](#parameter-limit)

limit

Type: `integer`  
Default: `50`

Items per page

Required range: `1 <= x <= 1000`

[​](#parameter-one-of-0)

search

Type: `string | null`  
Search by user ID

#### Response

Paginated card analytics data with transaction statistics

V2 Card Analytics paginated response - matches dot-service response format.

[​](#response-items)

items

Type: `CardAnalyticsItem` (object[])  
Required  
List of card analytics items

Show child attributes

[​](#response-total)

total

Type: `integer`  
Required  
Total number of items across all pages

[​](#response-page)

page

Type: `integer`  
Required  
Current page number (1-based)

[​](#response-limit)

limit

Type: `integer`  
Required  
Items per page limit

[​](#response-total-pages)

total\_pages

Type: `integer`  
Required  
Total number of pages

[​](#response-has-next)

has\_next

Type: `boolean`  
Required  
Whether there is a next page

[​](#response-has-previous)

has\_previous

Type: `boolean`  
Required  
Whether there is a previous page
