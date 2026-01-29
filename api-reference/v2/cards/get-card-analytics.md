# Get Card Analytics

GET /api/v2/card-analytics
Get Card Analytics

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

BearerAuthBearerAuth

[​](#authorization-authorization)

Authorization

string

header

required

JWT Bearer token from Auth0 authentication

#### Query Parameters

[​](#parameter-page)

page

integer

default:1

Page number (1-based)

Required range: `x >= 1`

[​](#parameter-limit)

limit

integer

default:50

Items per page

Required range: `1 <= x <= 1000`

[​](#parameter-one-of-0)

search

string | null

Search by user ID

#### Response

Paginated card analytics data with transaction statistics

V2 Card Analytics paginated response - matches dot-service response format.

[​](#response-items)

items

CardAnalyticsItem · object[]

required

List of card analytics items

Show child attributes

[​](#response-total)

total

integer

required

Total number of items across all pages

[​](#response-page)

page

integer

required

Current page number (1-based)

[​](#response-limit)

limit

integer

required

Items per page limit

[​](#response-total-pages)

total\_pages

integer

required

Total number of pages

[​](#response-has-next)

has\_next

boolean

required

Whether there is a next page

[​](#response-has-previous)

has\_previous

boolean

required

Whether there is a previous page
