# Testing Cards

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Testing

Testing Cards

[Guides](/introduction)[API Reference](/api-reference/v2/cards/get-card-analytics)

* [Website](https://nekuda.ai)
* [X](https://x.com/nekuda_ai)
* [Blog](https://nekuda.substack.com/)

##### Get Started

* [Introduction](/introduction)
* [Quickstart](/nekuda-sdk/Quickstart)
* [System Overview](/system-overview)
* [Payment Flow](/payment-flow)
* [Payment Flow Scenarios](/payment-flow-scenarios)
* [Support](/support)

##### Frontend SDK

* [Wallet Overview](/frontend/wallet/overview)
* [Payment Methods Tab](/frontend/wallet/payment-methods-tab)
* [Settings Tab](/frontend/wallet/settings-tab)
* [CVV Management](/frontend/wallet/cvv-management)
* [Collection Form](/frontend/wallet/collect-form)
* [Styling & Theming](/frontend/wallet/styling-theming)
* [Integration Patterns](/frontend/wallet/integration-patterns)
* [Migration Guide](/frontend/wallet/migration-guide)

##### Backend SDK

* [Getting Started](/nekuda-sdk/getting-started)
* [Core Concepts](/nekuda-sdk/core-concepts)
* [Usage Guide](/nekuda-sdk/usage-guide)
* [Configuration](/nekuda-sdk/Configuration)
* [Error Handling](/nekuda-sdk/Errors)

##### Security

* [Best practices](/best-practices)
* [Policy Engine & Safety](/policy-engine-safety)

##### Testing

* [Testing Cards](/testing/testing-cards)

On this page

* [Overview](#overview)
* [Cards by brand](#cards-by-brand)
* [International cards](#international-cards)
* [Americas](#americas)
* [Europe and Middle East](#europe-and-middle-east)
* [Asia Pacific](#asia-pacific)

Testing

# Testing Cards

Copy page

Test card numbers and testing guidelines for nekuda SDK integration

Copy page

## [​](#overview) Overview

When testing your nekuda SDK integration, use these test card numbers to simulate different payment scenarios.

## [​](#cards-by-brand) Cards by brand

Use these test card numbers to test successful payments with different card brands:

| Brand | Number | CVC |
| --- | --- | --- |
| Visa | `4242 4242 4242 4242` | Any 3 digits |
| Visa (debit) | `4000 0566 5566 5556` | Any 3 digits |
| Mastercard | `5555 5555 5555 4444` | Any 3 digits |
| Mastercard (2-series) | `2223 0031 2200 3222` | Any 3 digits |
| Mastercard (debit) | `5200 8282 8282 8210` | Any 3 digits |
| Mastercard (prepaid) | `5105 1051 0510 5100` | Any 3 digits |
| American Express | `3782 8224 6310 005` | Any 4 digits |
| American Express | `3714 4963 5398 431` | Any 4 digits |
| Discover | `6011 1111 1111 1117` | Any 3 digits |
| Discover | `6011 0009 9013 9424` | Any 3 digits |
| Discover (debit) | `6011 9811 1111 1113` | Any 3 digits |
| Diners Club | `3056 9300 0902 0004` | Any 3 digits |
| Diners Club (14-digit) | `3622 7206 2716 67` | Any 3 digits |
| BCcard/DinaCard | `6555 9000 0060 4105` | Any 3 digits |
| JCB | `3566 0020 2036 0505` | Any 3 digits |
| UnionPay | `6200 0000 0000 005` | Any 3 digits |
| UnionPay (debit) | `6200 0000 0000 047` | Any 3 digits |
| UnionPay (19-digit) | `6205 5000 0000 0000 004` | Any 3 digits |

## [​](#international-cards) International cards

Use these test card numbers to test payments from specific countries and regions:

### [​](#americas) Americas

| Country | Number | Brand |
| --- | --- | --- |
| United States (US) | `4242 4242 4242 4242` | Visa |
| Argentina (AR) | `4000 0003 2000 0021` | Visa |
| Brazil (BR) | `4000 0007 6000 0002` | Visa |
| Canada (CA) | `4000 0012 4000 0000` | Visa |
| Chile (CL) | `4000 0015 2000 0001` | Visa |
| Colombia (CO) | `4000 0017 0000 0003` | Visa |
| Costa Rica (CR) | `4000 0018 8000 0005` | Visa |
| Ecuador (EC) | `4000 0021 8000 0000` | Visa |
| Mexico | `4000 0048 4000 8001` | Visa |
| Mexico | `5062 2100 0000 0009` | Carnet |
| Panama (PA) | `4000 0059 1000 0000` | Visa |
| Paraguay (PY) | `4000 0060 0000 0066` | Visa |
| Peru (PE) | `4000 0060 4000 0068` | Visa |
| Uruguay (UY) | `4000 0085 8000 0003` | Visa |

### [​](#europe-and-middle-east) Europe and Middle East

| Country | Number | Brand |
| --- | --- | --- |
| United Arab Emirates | `4000 0078 4000 0001` | Visa |
| United Arab Emirates | `5200 0078 4000 0022` | Mastercard |
| Austria (AT) | `4000 0004 0000 0008` | Visa |
| Belgium (BE) | `4000 0005 6000 0004` | Visa |
| Bulgaria (BG) | `4000 0010 0000 0000` | Visa |
| Belarus (BY) | `4000 0011 2000 0005` | Visa |
| Croatia (HR) | `4000 0019 1000 0009` | Visa |
| Cyprus (CY) | `4000 0019 6000 0008` | Visa |
| Czech Republic (CZ) | `4000 0020 3000 0002` | Visa |
| Denmark (DK) | `4000 0020 8000 0001` | Visa |
| Estonia (EE) | `4000 0023 3000 0009` | Visa |
| Finland (FI) | `4000 0024 6000 0001` | Visa |
| France (FR) | `4000 0025 0000 0003` | Visa |
| Germany (DE) | `4000 0027 6000 0016` | Visa |
| Gibraltar (GI) | `4000 0029 2000 0005` | Visa |
| Greece (GR) | `4000 0030 0000 0030` | Visa |
| Hungary (HU) | `4000 0034 8000 0005` | Visa |
| Ireland (IE) | `4000 0037 2000 0005` | Visa |
| Italy (IT) | `4000 0038 0000 0008` | Visa |
| Latvia (LV) | `4000 0042 8000 0003` | Visa |
| Liechtenstein (LI) | `4000 0043 8000 0001` | Visa |
| Lithuania (LT) | `4000 0044 0000 0000` | Visa |
| Luxembourg (LU) | `4000 0044 2000 0006` | Visa |
| Malta (MT) | `4000 0047 0000 0007` | Visa |
| Netherlands (NL) | `4000 0052 8000 0008` | Visa |
| Norway (NO) | `4000 0057 8000 0007` | Visa |
| Poland (PL) | `4000 0061 6000 0005` | Visa |
| Portugal (PT) | `4000 0062 0000 0002` | Visa |
| Romania (RO) | `4000 0064 2000 0001` | Visa |
| Slovakia (SK) | `4000 0070 3000 0001` | Visa |
| Slovenia (SI) | `4000 0070 5000 0006` | Visa |
| Spain (ES) | `4000 0072 4000 0007` | Visa |
| Sweden (SE) | `4000 0075 2000 0008` | Visa |
| Switzerland (CH) | `4000 0075 6000 0009` | Visa |
| United Kingdom (GB) | `4000 0082 6000 0000` | Visa |
| United Kingdom (debit) | `4000 0582 6000 0005` | Visa (debit) |
| United Kingdom | `5555 5582 8555 5557` | Mastercard |

### [​](#asia-pacific) Asia Pacific

| Country | Number | Brand |
| --- | --- | --- |
| Australia (AU) | `4000 0003 6000 0006` | Visa |
| China (CN) | `4000 0015 6000 0002` | Visa |
| Hong Kong (HK) | `4000 0034 4000 0004` | Visa |
| India (IN) | `4000 0035 6000 0008` | Visa |
| Indonesia (ID) | `4000 0036 0000 0000` | Visa |
| Japan (JP) | `4000 0039 2000 0003` | Visa |
| Japan | `3530 1113 3330 0000` | JCB |
| Malaysia (MY) | `4000 0045 8000 0002` | Visa |
| New Zealand (NZ) | `4000 0055 4000 0008` | Visa |
| Philippines (PH) | `4000 0060 8000 0001` | Visa |
| Singapore (SG) | `4000 0070 2000 0003` | Visa |
| South Korea (KR) | `4000 0041 0000 0006` | Visa |
| Taiwan (TW) | `4000 0015 8000 0002` | Visa |
| Thailand (TH) | `4000 0076 4000 0003` | Visa |
| Vietnam (VN) | `4000 0070 4000 0000` | Visa |

[Policy Engine & Safety](/policy-engine-safety)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)