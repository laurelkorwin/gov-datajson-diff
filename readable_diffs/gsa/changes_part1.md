# Change History for gsa.json

### Changes from dd2190f to 364647f
**Author:** Automated

**Date:** 2025-02-03 16:12:44+00:00

**Message:** Updated data: Mon Feb  3 16:12:44 UTC 2025

```diff
diff --git a/gsa.json b/gsa.json
index a8a6e88..b6ceb4a 100644
--- a/gsa.json
+++ b/gsa.json
@@ -1972,7 +1972,7 @@
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://inventory.data.gov/dataset/04247624-1d6b-4e03-84eb-9eda1a6ea638/resource/12025a4f-1538-4ecf-a01e-77e1939f2d5d/download/data_gov_bldg_rexus.csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/04247624-1d6b-4e03-84eb-9eda1a6ea638/resource/9afba991-fe99-41fa-b3b3-1c9f08ee1ee8/download/data_gov_bldg_rexus.csv",
                     "mediaType": "text/csv",
                     "title": "data_gov_bldg_rexus.csv"
                 }
@@ -2020,7 +2020,7 @@
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://inventory.data.gov/dataset/2cdc97b5-3029-4ec3-b3bf-baec7948bad1/resource/b16a0800-68dd-48c3-aa6d-8c975ed6f4ac/download/data_gov_lse_rexus.csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/2cdc97b5-3029-4ec3-b3bf-baec7948bad1/resource/b1b1baaf-ac1d-4ad5-8cf7-e04fd50bad95/download/data_gov_lse_rexus.csv",
                     "mediaType": "text/csv",
                     "title": "data_gov_lse_rexus.csv"
                 }
@@ -7578,9 +7578,9 @@
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://inventory.data.gov/dataset/acf8e47e-24d2-4e4d-a786-847643f101fd/resource/0437517d-4fbd-43eb-8453-76ece7f562a8/download/1.27.25data.json",
+                    "downloadURL": "https://inventory.data.gov/dataset/acf8e47e-24d2-4e4d-a786-847643f101fd/resource/cf5456cc-287a-42b7-839a-ccf8eacd2f4d/download/1.31.25data.json",
                     "mediaType": "application/json",
-                    "title": "1.27.25data.json"
+                    "title": "1.31.25data.json"
                 }
             ],
             "identifier": "GSA-2015-11-13-01",
```

### Changes from 29aa757 to dd2190f (Part 1/2)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
diff --git a/gsa.json b/gsa.json
index 4703177..a8a6e88 100644
--- a/gsa.json
+++ b/gsa.json
@@ -1,87 +1,81 @@
 {
-    "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
-    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json",
     "@context": "https://project-open-data.cio.gov/v1.1/schema/catalog.jsonld",
     "@type": "dcat:Catalog",
+    "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
     "dataset": [
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2013, 3rd Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume by contractor, agency, contract vehicle and month for the centralized billing account. This represents the business volume of each government agency that has ordered telecommunications services from the Networx contract.",
-            "modified": "2019-06-12",
             "accessLevel": "public",
-            "identifier": "GSA-2015-02-26-1",
-            "dataQuality": true,
-            "describedBy": "http://www.gsa.gov/networx",
-            "issued": "2015-02-27",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L. Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.gsa.gov/networx",
+            "description": "The dataset represents the Networx Universal and Enterprise business volume by contractor, agency, contract vehicle and month for the centralized billing account. This represents the business volume of each government agency that has ordered telecommunications services from the Networx contract.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/TotRevFY13_3rdQtr.xlsx",
                     "format": "xlsx",
-                    "title": "Networx Business Volume_FY2013_3rd Qtr",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/TotRevFY13_3rdQtr.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Networx Business Volume_FY2013_3rd Qtr"
                 }
             ],
+            "identifier": "GSA-2015-02-26-1",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-02-27",
             "keyword": [
                 "Networx",
                 "telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "spatial": "National",
             "theme": [
                 "Procurement"
-            ]
+            ],
+            "title": "Networx Business Volume FY2013, 3rd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "e-Buy Awards for Fiscal Year 2019",
-            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
-            "modified": "2020-04-01",
             "accessLevel": "public",
-            "identifier": "GSA-2020-04-01-01",
-            "dataQuality": true,
-            "issued": "2015-09-28",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-08-31",
+            "bureauCode": [
+                "023:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Usha Gopal",
                 "hasEmail": "mailto:usha.gopal@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "ebuy_awards_FY2019",
                     "description": "e-Buy Awards for FY 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/c0013298-52ea-4f3e-a0bc-9f68cb7f5144/resource/1b0710dc-fa8c-4837-be40-6017325607d7/download/ebuyawardsfy2019.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/c0013298-52ea-4f3e-a0bc-9f68cb7f5144/resource/1b0710dc-fa8c-4837-be40-6017325607d7/download/ebuyawardsfy2019.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ebuy_awards_FY2019"
                 }
             ],
+            "identifier": "GSA-2020-04-01-01",
+            "isPartOf": "GSA-2015-08-31",
+            "issued": "2015-09-28",
             "keyword": [
                 "Awards",
                 "Contracts",
@@ -91,98 +85,98 @@
                 "e-Buy",
                 "procurement"
             ],
-            "bureauCode": [
-                "023:10"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-04-01",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "e-Buy Awards for Fiscal Year 2019"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2016, 2nd Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
             "accessLevel": "public",
-            "identifier": "GSA-2016-05-18-01",
-            "dataQuality": true,
-            "issued": "2015-11-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://inventory.data.gov/dataset/53aebcad-db78-4871-9df5-7a909e30b1e4/resource/76deb9f1-e595-4009-8d0a-d04da481221c/download/networxtotrevfy162ndqtr.xlsx",
                     "format": "xlsx",
-                    "title": "Networx Total Revenue FY16 2nd Quarter",
-                    "downloadURL": "https://inventory.data.gov/dataset/53aebcad-db78-4871-9df5-7a909e30b1e4/resource/76deb9f1-e595-4009-8d0a-d04da481221c/download/networxtotrevfy162ndqtr.xlsx"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Networx Total Revenue FY16 2nd Quarter"
                 }
             ],
+            "identifier": "GSA-2016-05-18-01",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-11-13",
             "keyword": [
                 "Contract",
                 "Networx Telecommunications",
                 "Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Telecommunications Services"
-            ]
+            ],
+            "title": "Networx Business Volume FY2016, 2nd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions July-Sept 2019, 4th Qtr - US Bank",
-            "description": "Purchases made with the purchase card.  Files will be batched quarterly.",
-            "modified": "2020-02-04",
             "accessLevel": "public",
-            "identifier": "GSA-2020-02-04-01",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card.  Files will be batched quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "US Bank PC Qtr4 2019",
                     "description": "4th Quarter US Bank Purchase Card transactions.",
-                    "downloadURL": "https://inventory.data.gov/dataset/08a347ec-2429-41a1-9728-51e442266968/resource/58206663-fb54-4bae-a7eb-8a3aef57c2c3/download/us-bank-pc-qtr4-2019.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/08a347ec-2429-41a1-9728-51e442266968/resource/58206663-fb54-4bae-a7eb-8a3aef57c2c3/download/us-bank-pc-qtr4-2019.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "US Bank PC Qtr4 2019"
                 }
             ],
+            "identifier": "GSA-2020-02-04-01",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "august",
                 "july",
@@ -190,98 +184,98 @@
                 "september",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-02-04",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions July-Sept 2019, 4th Qtr - US Bank"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2020, 2nd Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2020-02-20",
             "accessLevel": "public",
-            "identifier": "GSA-2020-05-18-01",
-            "dataQuality": true,
-            "issued": "2015-11-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "TotRevFY20_2ndQtr",
                     "description": "2nd Quarter FY20",
-                    "downloadURL": "https://inventory.data.gov/dataset/c2095a7c-0a1c-4f2e-8e80-5f218e805213/resource/ba337757-50b9-4ce5-a43f-83fc62be35d5/download/totrevfy202ndqtr.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/c2095a7c-0a1c-4f2e-8e80-5f218e805213/resource/ba337757-50b9-4ce5-a43f-83fc62be35d5/download/totrevfy202ndqtr.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY20_2ndQtr"
                 }
             ],
+            "identifier": "GSA-2020-05-18-01",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-11-13",
             "keyword": [
                 "Contract",
                 "Networx Telecommunications",
                 "Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-02-20",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Telecommunications Services"
-            ]
+            ],
+            "title": "Networx Business Volume FY2020, 2nd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions Oct-Dec 2020, 1st Qtr - US Bank",
-            "description": "Purchases made with the purchase card.  Files will be batched quarterly.",
-            "modified": "2020-02-04",
             "accessLevel": "public",
-            "identifier": "GSA-2020-02-04-02",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card.  Files will be batched quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "US Bank PC Qtr1 2020",
                     "description": "1st Quarter US Bank Purchase Card transactions.",
-                    "downloadURL": "https://inventory.data.gov/dataset/41e9f279-c461-4c8f-a8af-57c2a3e4c4ee/resource/e9609cbc-a825-4377-a81b-768dc05dadb8/download/us-bank-pc-qtr1-2020.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/41e9f279-c461-4c8f-a8af-57c2a3e4c4ee/resource/e9609cbc-a825-4377-a81b-768dc05dadb8/download/us-bank-pc-qtr1-2020.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "US Bank PC Qtr1 2020"
                 }
             ],
+            "identifier": "GSA-2020-02-04-02",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "december",
                 "november",
@@ -289,50 +283,50 @@
                 "purchase card",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-02-04",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions Oct-Dec 2020, 1st Qtr - US Bank"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions Jan-Mar 2020, 2nd Qtr - US Bank",
-            "description": "Purchases made with the purchase card.  Files will be batched quarterly.",
-            "modified": "2020-02-04",
             "accessLevel": "public",
-            "identifier": "GSA-2020-05-26-01",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card.  Files will be batched quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "US Bank PC Qtr 2 2020",
                     "description": "Purchase Card transactions for January through March 2020.",
-                    "downloadURL": "https://inventory.data.gov/dataset/f5820775-f12d-48f3-aef2-ecf96912f7d1/resource/5b0f49fc-120a-489f-8a3d-e6dd58be24eb/download/us-bank-pc-qtr2-2020.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/f5820775-f12d-48f3-aef2-ecf96912f7d1/resource/5b0f49fc-120a-489f-8a3d-e6dd58be24eb/download/us-bank-pc-qtr2-2020.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "US Bank PC Qtr 2 2020"
                 }
             ],
+            "identifier": "GSA-2020-05-26-01",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "february",
                 "january",
@@ -340,51 +334,51 @@
                 "purchase card",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-02-04",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions Jan-Mar 2020, 2nd Qtr - US Bank"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA Jan-Mar 2020, 2nd Qtr US Bank",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2020-02-13",
             "accessLevel": "public",
-            "identifier": "GSA-2020-05-26-02",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "2020-2nd Qtr (Jan-Mar)_CBCA PC transactions_US Bank",
                     "description": "CBCA PC transactions for 2nd Qtr 2020 US Bank",
-                    "downloadURL": "https://inventory.data.gov/dataset/59757dcd-296e-4143-b267-a8d3e24ed4e3/resource/f74e792f-d28b-4ab4-ac6c-4daf2e76fe82/download/2020-2nd-qtr-jan-marcbca-pc-transactionsus-bank.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/59757dcd-296e-4143-b267-a8d3e24ed4e3/resource/f74e792f-d28b-4ab4-ac6c-4daf2e76fe82/download/2020-2nd-qtr-jan-marcbca-pc-transactionsus-bank.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "2020-2nd Qtr (Jan-Mar)_CBCA PC transactions_US Bank"
                 }
             ],
+            "identifier": "GSA-2020-05-26-02",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Contract Board",
@@ -395,51 +389,51 @@
                 "january",
                 "march"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-02-13",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA Jan-Mar 2020, 2nd Qtr US Bank"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA Oct-Dec 2020, 1st Qtr US Bank",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2020-02-13",
             "accessLevel": "public",
-            "identifier": "GSA-2020-02-13-01",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "2020-1st Qtr (Oct-Dec) CBCA PC transactions_US Bank",
                     "description": "1st Quarter CBCA Purchase Card transactions",
-                    "downloadURL": "https://inventory.data.gov/dataset/40a169df-a46e-4a02-8ced-af4971650091/resource/623b0ebe-e235-4fde-a96d-c443776597f7/download/2020-1st-qtr-oct-dec-cbca-pc-transactionsus-bank.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/40a169df-a46e-4a02-8ced-af4971650091/resource/623b0ebe-e235-4fde-a96d-c443776597f7/download/2020-1st-qtr-oct-dec-cbca-pc-transactionsus-bank.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "2020-1st Qtr (Oct-Dec) CBCA PC transactions_US Bank"
                 }
             ],
+            "identifier": "GSA-2020-02-13-01",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Contract Board",
@@ -450,88 +444,89 @@
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-02-13",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA Oct-Dec 2020, 1st Qtr US Bank"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2020, 1st Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2020-02-20",
             "accessLevel": "public",
-            "identifier": "GSA-2020-02-20-01",
-            "dataQuality": true,
-            "issued": "2015-11-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "TotRevFY20_1stQtr",
                     "description": "1st Quarter Total Revenue FY20",
-                    "downloadURL": "https://inventory.data.gov/dataset/65ddcbed-eba0-48b9-9c6f-c956c1e8deb2/resource/1c09a826-64ad-42d3-9333-f46c3dc8c4f4/download/totrevfy201stqtr.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/65ddcbed-eba0-48b9-9c6f-c956c1e8deb2/resource/1c09a826-64ad-42d3-9333-f46c3dc8c4f4/download/totrevfy201stqtr.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY20_1stQtr"
                 }
             ],
+            "identifier": "GSA-2020-02-20-01",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-11-13",
             "keyword": [
                 "Contract",
                 "Networx Telecommunications",
                 "Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-02-20",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Telecommunications Services"
-            ]
+            ],
+            "title": "Networx Business Volume FY2020, 1st Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Enterprise Infrastructure Solutions (EIS)",
-            "description": "These datasets represent the Enterprise Infrastructure Solutions (EIS), business volume of each government agency that has ordered telecommunications services from the EIS Contract.  This collection contains data from FY2019 to the present.",
-            "modified": "2020-06-26",
             "accessLevel": "public",
-            "identifier": "GSA-2020-06-26-01",
-            "dataQuality": true,
-            "issued": "2020-06-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Loren Smith",
                 "hasEmail": "mailto:loren.smith@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "These datasets represent the Enterprise Infrastructure Solutions (EIS), business volume of each government agency that has ordered telecommunications services from the EIS Contract.  This collection contains data from FY2019 to the present.",
+            "identifier": "GSA-2020-06-26-01",
+            "issued": "2020-06-26",
             "keyword": [
                 "Business Volume",
                 "EIS",
@@ -539,50 +534,50 @@
                 "GSA",
                 "Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-06-26",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Telecommunications Services"
-            ]
+            ],
+            "title": "Enterprise Infrastructure Solutions (EIS)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "FY19 Enterprise Infrastructure Solutions (EIS) Qtrly Report",
-            "description": "These datasets represent the Enterprise Infrastructure Solutions (EIS), business volume of each government agency that has ordered telecommunications services from the EIS Contract.  This collection contains data from FY2019.",
-            "modified": "2020-06-26",
             "accessLevel": "public",
-            "identifier": "GSA-2020-06-26-02",
-            "dataQuality": true,
-            "issued": "2020-06-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2020-06-26-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Loren Smith",
                 "hasEmail": "mailto:loren.smith@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "These datasets represent the Enterprise Infrastructure Solutions (EIS), business volume of each government agency that has ordered telecommunications services from the EIS Contract.  This collection contains data from FY2019.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "EISTotRevFY19_Q1_Q4",
                     "description": "This report contains the business volume of each government agency\r\nthat has ordered telecommunications services from the EIS contract for \r\nFY2019.",
-                    "downloadURL": "https://inventory.data.gov/dataset/8b1640e0-d828-4edd-81fe-8dee6b04c9c7/resource/233fc5dd-fbf5-423e-9d45-316385b2b433/download/eistotrevfy19q1q4.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/8b1640e0-d828-4edd-81fe-8dee6b04c9c7/resource/233fc5dd-fbf5-423e-9d45-316385b2b433/download/eistotrevfy19q1q4.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EISTotRevFY19_Q1_Q4"
                 }
             ],
+            "identifier": "GSA-2020-06-26-02",
+            "isPartOf": "GSA-2020-06-26-01",
+            "issued": "2020-06-26",
             "keyword": [
                 "Business Volume",
                 "EIS",
@@ -590,65 +585,64 @@
                 "GSA",
                 "Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-06-26",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Telecommunications Services"
-            ]
+            ],
+            "title": "FY19 Enterprise Infrastructure Solutions (EIS) Qtrly Report"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "FY20 Enterprise Infrastructure Solutions (EIS) Quarterly Reports",
-            "description": "These datasets represent the Enterprise Infrastructure Solutions (EIS), business volume of each government agency that has ordered telecommunications services from the EIS Contract.  This collection contains data from FY2020.",
-            "modified": "2021-03-25T16:16:05.905Z",
             "accessLevel": "public",
-            "identifier": "GSA-2020-06-26-03",
-            "dataQuality": true,
-            "issued": "2020-06-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2020-06-26-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Loren Smith",
                 "hasEmail": "mailto:loren.smith@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "These datasets represent the Enterprise Infrastructure Solutions (EIS), business volume of each government agency that has ordered telecommunications services from the EIS Contract.  This collection contains data from FY2020.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "EISTotRevFY20_Q1_Q2",
                     "description": "This report contains each government agency that has ordered telecommunications services from the EIS contract.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bf94f704-2ede-4058-955e-30b44e43b2d9/resource/0c29f996-574a-42f3-9a6f-b86c1c855a84/download/eistotrevfy20q1q2.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/bf94f704-2ede-4058-955e-30b44e43b2d9/resource/0c29f996-574a-42f3-9a6f-b86c1c855a84/download/eistotrevfy20q1q2.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EISTotRevFY20_Q1_Q2"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://inventory.data.gov/dataset/bf94f704-2ede-4058-955e-30b44e43b2d9/resource/59f0ef50-c468-4d8f-82b9-59dc2e95a536/download/eistotrevfy20_q3.xlsx",
                     "format": "xlsx",
-                    "title": "EISTotRevFY20_Q3",
-                    "downloadURL": "https://inventory.data.gov/dataset/bf94f704-2ede-4058-955e-30b44e43b2d9/resource/59f0ef50-c468-4d8f-82b9-59dc2e95a536/download/eistotrevfy20_q3.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EISTotRevFY20_Q3"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://inventory.data.gov/dataset/bf94f704-2ede-4058-955e-30b44e43b2d9/resource/417c0432-0263-4e39-85c9-0073cb1a2a1f/download/eistotrevfy20_q4.xlsx",
                     "format": "xlsx",
-                    "title": "EISTotRevFY20_Q4",
-                    "downloadURL": "https://inventory.data.gov/dataset/bf94f704-2ede-4058-955e-30b44e43b2d9/resource/417c0432-0263-4e39-85c9-0073cb1a2a1f/download/eistotrevfy20_q4.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EISTotRevFY20_Q4"
                 }
             ],
+            "identifier": "GSA-2020-06-26-03",
+            "isPartOf": "GSA-2020-06-26-01",
+            "issued": "2020-06-26",
             "keyword": [
                 "Business Volume",
                 "EIS",
@@ -656,103 +650,103 @@
                 "GSA",
                 "Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-03-25T16:16:05.905Z",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "true",
             "theme": [
                 "Telecommunications Services"
-            ]
+            ],
+            "title": "FY20 Enterprise Infrastructure Solutions (EIS) Quarterly Reports"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Fed. Data Center Consolidation Initiative (FDCCI) Data Center Closings 2010-2015",
-            "description": "Posted quarterly, using FDCCI Task Force data reported to OMB through the quarterly Integrated Data Collection (IDC) deadline. Federal Data Center Consolidation Initiative (FDCCI) Data Center Closures 2010-2015. Under the FDDCI, agencies have categorized their agency data center populations into two categories: core and non-core. The government is closing 40% of agency-identified, non-\u00adcore data centers, while optimizing agency-identified core-data centers, according to a series of total cost of ownership metrics (see OMB M-13-09 and OMB M-14-08). This dataset reflects information only for agency-identified, non-core closures. All questions or inquiries should be directed to the specific agencies. The FY2010 through FY2015 dataset provides a list of planned or closed data centers by agency and by city/state location since the FDCCI started. Please note ?OTHER? is listed for data centers in cloud, co-located or managed service data centers, where square footage is unavailable. See related information about the FDCCI, including the definition of a data center and other FAQs at http://cio.gov/fdcci.",
-            "modified": "2015-11-16",
             "accessLevel": "public",
-            "identifier": "GSA - 32830",
-            "dataQuality": true,
-            "describedBy": "https://inventory.data.gov/dataset/federal-data-center-consolidation-initiative-fdcci-data-center-closings-2010-2014/resource/5ac29bc3-2a8f-4bdc-810c-31598058ba8f",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "issued": "2015-04-01",
-            "landingPage": "http://www.cio.gov/",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "023:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Cindy Smith",
                 "hasEmail": "mailto:cindya.smith@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://inventory.data.gov/dataset/federal-data-center-consolidation-initiative-fdcci-data-center-closings-2010-2014/resource/5ac29bc3-2a8f-4bdc-810c-31598058ba8f",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "Posted quarterly, using FDCCI Task Force data reported to OMB through the quarterly Integrated Data Collection (IDC) deadline. Federal Data Center Consolidation Initiative (FDCCI) Data Center Closures 2010-2015. Under the FDDCI, agencies have categorized their agency data center populations into two categories: core and non-core. The government is closing 40% of agency-identified, non-\u00adcore data centers, while optimizing agency-identified core-data centers, according to a series of total cost of ownership metrics (see OMB M-13-09 and OMB M-14-08). This dataset reflects information only for agency-identified, non-core closures. All questions or inquiries should be directed to the specific agencies. The FY2010 through FY2015 dataset provides a list of planned or closed data centers by agency and by city/state location since the FDCCI started. Please note ?OTHER? is listed for data centers in cloud, co-located or managed service data centers, where square footage is unavailable. See related information about the FDCCI, including the definition of a data center and other FAQs at http://cio.gov/fdcci.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "Federal_Data_Center_Consolidation_Initiative__FDCCI__Data_Center_Closings_2010-2015_053115",
                     "description": "Data as of 05/31/2015",
-                    "downloadURL": "https://inventory.data.gov/dataset/251f4905-c320-468a-975e-45e9835ba418/resource/5ac29bc3-2a8f-4bdc-810c-31598058ba8f/download/federaldatacenterconsolidationinitiativefdccidatacenterclosings20102015053115.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/251f4905-c320-468a-975e-45e9835ba418/resource/5ac29bc3-2a8f-4bdc-810c-31598058ba8f/download/federaldatacenterconsolidationinitiativefdccidatacenterclosings20102015053115.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Federal_Data_Center_Consolidation_Initiative__FDCCI__Data_Center_Closings_2010-2015_053115"
                 }
             ],
+            "identifier": "GSA - 32830",
+            "issued": "2015-04-01",
             "keyword": [
                 "consolidation",
                 "fddci",
                 "federal data center consolidation initiative"
             ],
-            "bureauCode": [
-                "023:10"
-            ],
-            "programCode": [
-                "023:019"
-            ],
+            "landingPage": "http://www.cio.gov/",
             "language": [
                 "us-EN"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2015-11-16",
+            "programCode": [
+                "023:019"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "references": [
                 "http://www.cio.gov/FDCCI"
             ],
             "theme": [
                 "Data Centers"
-            ]
+            ],
+            "title": "Fed. Data Center Consolidation Initiative (FDCCI) Data Center Closings 2010-2015"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Inventory Reporting Information System (IRIS) Safety",
-            "description": "IRIS tracks the status of safety deficiencies identified during Occupational Safety and Health Administration (OSHA) and Safety & Environmental Management (SEM) survey inspections.",
-            "modified": "2018-10-09",
             "accessLevel": "public",
-            "identifier": "GSA-33271",
-            "dataQuality": true,
-            "describedBy": "http://www.gsa.gov/pbs",
-            "issued": "2011-05-02",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bill Shah",
                 "hasEmail": "mailto:bill.shah@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.gsa.gov/pbs",
+            "description": "IRIS tracks the status of safety deficiencies identified during Occupational Safety and Health Administration (OSHA) and Safety & Environmental Management (SEM) survey inspections.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/24ccab47-cd58-4e1a-a7c3-d06ccd63b338/resource/0f648994-4341-40ed-9d19-e5746764c4a2/download/inventoryreportinginfosystemssafety.csv",
                     "format": "csv",
-                    "title": "Inventory_Reporting_Info_Systems_Safety.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/24ccab47-cd58-4e1a-a7c3-d06ccd63b338/resource/0f648994-4341-40ed-9d19-e5746764c4a2/download/inventoryreportinginfosystemssafety.csv"
+                    "mediaType": "text/csv",
+                    "title": "Inventory_Reporting_Info_Systems_Safety.csv"
                 }
             ],
+            "identifier": "GSA-33271",
+            "issued": "2011-05-02",
             "keyword": [
                 "Interactive",
                 "building",
@@ -763,49 +757,49 @@
                 "sem",
                 "survey"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-10-09",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "us-EN"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Data.gov Dataset Monthly Download Trends - Archival",
-            "description": "This dataset provides the trend of downloads in Data.gov up to 2013. These numbers represent the number of times a user has clicked on the XML or CSV (for example) links in the catalog.",
-            "modified": "2016-01-20",
-            "accessLevel": "public",
-            "identifier": "GSA-32421",
-            "dataQuality": true,
-            "describedBy": "http://www.data.gov/metric",
-            "describedByType": "text/csv",
-            "issued": "2013-04-11",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "Worldwide",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "spatial": "National",
+            "title": "Inventory Reporting Information System (IRIS) Safety"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "GSA-2015-09-14-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Joo Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.data.gov/metric",
+            "describedByType": "text/csv",
+            "description": "This dataset provides the trend of downloads in Data.gov up to 2013. These numbers represent the number of times a user has clicked on the XML or CSV (for example) links in the catalog.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/3a69e635-ff9c-4bd9-8fb3-04f8ccb7b351/resource/06684cd2-f911-49e9-8d44-d4fe256b4882/download/userssharedsdfdata.govdatasetmonthlydownloadtrends.csv",
                     "format": "text/csv",
-                    "title": "Data.gov_Dataset_Monthly_Download_Trends.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/3a69e635-ff9c-4bd9-8fb3-04f8ccb7b351/resource/06684cd2-f911-49e9-8d44-d4fe256b4882/download/userssharedsdfdata.govdatasetmonthlydownloadtrends.csv"
+                    "mediaType": "text/csv",
+                    "title": "Data.gov_Dataset_Monthly_Download_Trends.csv"
                 }
             ],
+            "identifier": "GSA-32421",
+            "isPartOf": "GSA-2015-09-14-01",
+            "issued": "2013-04-11",
             "keyword": [
                 "Data.gov",
                 "Dataset",
@@ -813,464 +807,464 @@
                 "Interactive",
                 "Monthly"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-20",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "spatial": "Worldwide",
             "theme": [
                 "Monthly Download Trends for Data.gov"
-            ]
+            ],
+            "title": "Data.gov Dataset Monthly Download Trends - Archival"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Data.gov Top 10 Visiting Countries - Archival",
-            "description": "This dataset provides top 10 visiting countries by month in Data.gov up to July 2013.",
-            "modified": "2016-01-20",
             "accessLevel": "public",
-            "identifier": "GSA-32491",
-            "dataQuality": true,
-            "describedBy": "http://www.data.gov/metric",
-            "describedByType": "text/csv",
-            "issued": "2013-05-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "GSA-2015-09-14-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Joo Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.data.gov/metric",
+            "describedByType": "text/csv",
+            "description": "This dataset provides top 10 visiting countries by month in Data.gov up to July 2013.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/b0d40da1-a505-476a-a49b-cfc50ea6d9da/resource/0a1a3fb8-a813-4470-b50c-51b7856203be/download/userssharedsdfdata.govtop10visitingcountries.csv",
                     "format": "text/csv",
-                    "title": "Data.gov_Top_10_Visiting_Countries.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/b0d40da1-a505-476a-a49b-cfc50ea6d9da/resource/0a1a3fb8-a813-4470-b50c-51b7856203be/download/userssharedsdfdata.govtop10visitingcountries.csv"
+                    "mediaType": "text/csv",
+                    "title": "Data.gov_Top_10_Visiting_Countries.csv"
                 }
             ],
+            "identifier": "GSA-32491",
+            "isPartOf": "GSA-2015-09-14-01",
+            "issued": "2013-05-13",
             "keyword": [
                 "Countries",
                 "Interactive"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-20",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "spatial": "United States",
             "theme": [
                 "Countries",
                 "Top 10"
-            ]
+            ],
+            "title": "Data.gov Top 10 Visiting Countries - Archival"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Data.gov Daily Visitor Statistics - Archival",
-            "description": "This dataset provides distribution of daily visitors to the Data.gov site up to 2013.",
-            "modified": "2016-01-20",
             "accessLevel": "public",
-            "identifier": "GSA-32441",
-            "dataQuality": true,
-            "describedBy": "http://www.data.gov/metric",
-            "describedByType": "text/csv",
-            "issued": "2013-04-11",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "Worldwide",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1D",
-            "isPartOf": "GSA-2015-09-14-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Joo Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.data.gov/metric",
+            "describedByType": "text/csv",
+            "description": "This dataset provides distribution of daily visitors to the Data.gov site up to 2013.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/2dc37fea-3afa-4f9d-93ef-5e11957a371b/resource/0f96083f-0089-4524-8574-8eec91e2a7f2/download/userssharedsdfdata.govdailyvisitorstatistics.csv",
                     "format": "text/csv",
-                    "title": "Data.gov_Daily_Visitor_Statistics.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/2dc37fea-3afa-4f9d-93ef-5e11957a371b/resource/0f96083f-0089-4524-8574-8eec91e2a7f2/download/userssharedsdfdata.govdailyvisitorstatistics.csv"
+                    "mediaType": "text/csv",
+                    "title": "Data.gov_Daily_Visitor_Statistics.csv"
                 }
             ],
+            "identifier": "GSA-32441",
+            "isPartOf": "GSA-2015-09-14-01",
+            "issued": "2013-04-11",
             "keyword": [
                 "Daily",
                 "Interactive",
                 "Statistics",
                 "Visitor"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-20",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "spatial": "Worldwide",
             "theme": [
                 "Visitors to Data.gov Site"
-            ]
+            ],
+            "title": "Data.gov Daily Visitor Statistics - Archival"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Data.gov Monthly Visitor Statistics - Archival",
-            "description": "This dataset provides the number of visitors to Data.gov per month up to 2013.",
-            "modified": "2016-01-20",
             "accessLevel": "public",
-            "identifier": "GSA-32431",
-            "dataQuality": true,
-            "describedBy": "http://www.data.gov/metric",
-            "describedByType": "text/csv",
-            "issued": "2013-04-11",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "Worldwide",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "GSA-2015-09-14-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Joo Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.data.gov/metric",
+            "describedByType": "text/csv",
+            "description": "This dataset provides the number of visitors to Data.gov per month up to 2013.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/a84616de-f4a8-4834-8acf-be5aa05e2713/resource/5fb970e5-11a5-4ef7-ae06-5df03688caec/download/userssharedsdfdata.govmonthlyvisitorstatistics.csv",
                     "format": "text/csv",
-                    "title": "Data.gov_Monthly_Visitor_Statistics.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/a84616de-f4a8-4834-8acf-be5aa05e2713/resource/5fb970e5-11a5-4ef7-ae06-5df03688caec/download/userssharedsdfdata.govmonthlyvisitorstatistics.csv"
+                    "mediaType": "text/csv",
+                    "title": "Data.gov_Monthly_Visitor_Statistics.csv"
                 }
             ],
+            "identifier": "GSA-32431",
+            "isPartOf": "GSA-2015-09-14-01",
+            "issued": "2013-04-11",
             "keyword": [
                 "Interactive",
                 "monthly",
                 "statistics",
                 "visitor"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-20",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "spatial": "Worldwide",
             "theme": [
                 "Statistics",
                 "Visitors Monthly"
-            ]
+            ],
+            "title": "Data.gov Monthly Visitor Statistics - Archival"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Data.gov Federal Agency Participation - Archival",
-            "description": "This dataset provides distribution of all datasets provided by all Departments/ Agencies/ Organizations in Data.gov up to 2013. See http://www.data.gov/metric for current information on federal agency participation.",
-            "modified": "2016-01-20",
             "accessLevel": "public",
-            "identifier": "GSA-32041",
-            "dataQuality": true,
-            "describedBy": "http://www.data.gov/metric",
-            "describedByType": "text/csv",
-            "issued": "2013-04-11",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "GSA-2015-09-14-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Joo Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.data.gov/metric",
+            "describedByType": "text/csv",
+            "description": "This dataset provides distribution of all datasets provided by all Departments/ Agencies/ Organizations in Data.gov up to 2013. See http://www.data.gov/metric for current information on federal agency participation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/f6f06df8-c102-4fe8-af31-c368be66166d/resource/d65072b5-08f0-4f90-bd57-65e731c59df2/download/userssharedsdfdata.govfederalagencyparticipation.csv",
                     "format": "text/csv",
-                    "title": "Data.gov_Federal_Agency_Participation.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/f6f06df8-c102-4fe8-af31-c368be66166d/resource/d65072b5-08f0-4f90-bd57-65e731c59df2/download/userssharedsdfdata.govfederalagencyparticipation.csv"
+                    "mediaType": "text/csv",
+                    "title": "Data.gov_Federal_Agency_Participation.csv"
                 }
             ],
+            "identifier": "GSA-32041",
+            "isPartOf": "GSA-2015-09-14-01",
+            "issued": "2013-04-11",
             "keyword": [
                 "Agency interactive",
                 "federal",
                 "participation"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-20",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "spatial": "United States",
             "theme": [
                 "Participation Federal"
-            ]
+            ],
+            "title": "Data.gov Federal Agency Participation - Archival"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Data.gov Monthly Page Views - Archival",
-            "description": "This dataset provides monthly page views in Data.gov up to 2013.",
-            "modified": "2016-01-20",
             "accessLevel": "public",
-            "identifier": "GSA-32451",
-            "dataQuality": true,
-            "describedBy": "http://www.data.gov/metric",
-            "describedByType": "text/csv",
-            "issued": "2013-04-11",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "Worldwide",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "GSA-2015-09-14-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Joo Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.data.gov/metric",
+            "describedByType": "text/csv",
+            "description": "This dataset provides monthly page views in Data.gov up to 2013.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/bbde0832-623e-46df-90eb-2c033843cd00/resource/3b2d23db-82ab-44a5-8152-1d65a88be376/download/userssharedsdfdata.govmonthlypageviews.csv",
                     "format": "text/csv",
-                    "title": "Data.gov_Monthly_Page_Views.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/bbde0832-623e-46df-90eb-2c033843cd00/resource/3b2d23db-82ab-44a5-8152-1d65a88be376/download/userssharedsdfdata.govmonthlypageviews.csv"
+                    "mediaType": "text/csv",
+                    "title": "Data.gov_Monthly_Page_Views.csv"
                 }
             ],
+            "identifier": "GSA-32451",
+            "isPartOf": "GSA-2015-09-14-01",
+            "issued": "2013-04-11",
             "keyword": [
                 "interactive",
                 "page",
                 "views"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-20",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "spatial": "Worldwide",
             "theme": [
                 "Page Views Monthly"
-            ]
+            ],
+            "title": "Data.gov Monthly Page Views - Archival"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Data.gov Datasets Uploaded by Agencies per Month - Archival",
-            "description": "This dataset provides count of datasets uploaded by agencies per month in Data.gov. This is from the prior dataset management system and not the current harvesting system for catalog.data.gov.",
-            "modified": "2016-01-20",
             "accessLevel": "public",
-            "identifier": "GSA-32481",
-            "dataQuality": true,
-            "describedBy": "http://www.data.gov/metric",
-            "describedByType": "text/csv",
-            "issued": "2013-05-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "GSA-2015-09-14-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Joo Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.data.gov/metric",
+            "describedByType": "text/csv",
+            "description": "This dataset provides count of datasets uploaded by agencies per month in Data.gov. This is from the prior dataset management system and not the current harvesting system for catalog.data.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/07db4fc0-3ab1-401a-bb77-7ce502d7dc1b/resource/8abf19fd-8d83-4eb0-a7cc-35d22c986673/download/userssharedsdfdata.govupldbyagenciespermonth.csv",
                     "format": "text/csv",
-                    "title": "Data.gov_Upld_By_Agencies_per_Month.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/07db4fc0-3ab1-401a-bb77-7ce502d7dc1b/resource/8abf19fd-8d83-4eb0-a7cc-35d22c986673/download/userssharedsdfdata.govupldbyagenciespermonth.csv"
+                    "mediaType": "text/csv",
+                    "title": "Data.gov_Upld_By_Agencies_per_Month.csv"
                 }
             ],
+            "identifier": "GSA-32481",
+            "isPartOf": "GSA-2015-09-14-01",
+            "issued": "2013-05-13",
             "keyword": [
                 "agencies",
                 "interactive data",
                 "monthly",
                 "uploaded"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0",
+            "modified": "2016-01-20",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "spatial": "United States",
             "theme": [
                 "Datasets uploaded"
-            ]
+            ],
+            "title": "Data.gov Datasets Uploaded by Agencies per Month - Archival"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "FAS Forecast Of Contracting Opportunities",
-            "description": "FAS Forecast of Contracting Opportunities",
-            "modified": "2016-01-21",
             "accessLevel": "public",
-            "identifier": "GSA-32021",
-            "dataQuality": true,
-            "describedBy": "http://inventory.data.gov/dataset/baa0ba2b-5eaa-4a71-b1b0-1c364d439f85/resource/ab0d35f6-7d88-4349-9e61-254ce4145a45",
-            "describedByType": "text/csv",
-            "issued": "2012-10-16",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Murugaboopathi Natarajan (IAG-C)",
                 "hasEmail": "mailto:Murugaboopathi.Natarajan@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://inventory.data.gov/dataset/baa0ba2b-5eaa-4a71-b1b0-1c364d439f85/resource/ab0d35f6-7d88-4349-9e61-254ce4145a45",
+            "describedByType": "text/csv",
+            "description": "FAS Forecast of Contracting Opportunities",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/baa0ba2b-5eaa-4a71-b1b0-1c364d439f85/resource/ab0d35f6-7d88-4349-9e61-254ce4145a45/download/userssharedsdffasforecastofcontractingopportunities.csv",
                     "format": "text/csv",
-                    "title": "FAS_Forecast_Of_Contracting_Opportunities.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/baa0ba2b-5eaa-4a71-b1b0-1c364d439f85/resource/ab0d35f6-7d88-4349-9e61-254ce4145a45/download/userssharedsdffasforecastofcontractingopportunities.csv"
+                    "mediaType": "text/csv",
+                    "title": "FAS_Forecast_Of_Contracting_Opportunities.csv"
                 }
             ],
+            "identifier": "GSA-32021",
+            "issued": "2012-10-16",
             "keyword": [
                 "FAS",
                 "Interactive",
                 "contracting",
                 "opportunities"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-21",
             "programCode": [
                 "023:014"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "spatial": "United States",
             "theme": [
                 "Contracting",
                 "FAS"
-            ]
+            ],
+            "title": "FAS Forecast Of Contracting Opportunities"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Data.gov Top 10 Visiting States - Archival",
-            "description": "This dataset provides top 10 states by month visiting Data.gov up to 2013.",
-            "modified": "2016-01-21",
             "accessLevel": "public",
-            "identifier": "GSA-32501",
-            "dataQuality": true,
-            "describedBy": "http://www.data.gov/metric",
-            "describedByType": "text/csv",
-            "issued": "2013-05-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "GSA-2015-09-14-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Joo Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.data.gov/metric",
+            "describedByType": "text/csv",
+            "description": "This dataset provides top 10 states by month visiting Data.gov up to 2013.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/2f3fa83b-80f3-4951-8ef7-96e213a53c16/resource/48dc3ad1-ebb0-4ee8-993a-defa131af5e2/download/userssharedsdfdata.govtop10visitingstates.csv",
                     "format": "text/csv",
-                    "title": "Data.gov_Top_10_Visiting_States.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/2f3fa83b-80f3-4951-8ef7-96e213a53c16/resource/48dc3ad1-ebb0-4ee8-993a-defa131af5e2/download/userssharedsdfdata.govtop10visitingstates.csv"
+                    "mediaType": "text/csv",
+                    "title": "Data.gov_Top_10_Visiting_States.csv"
                 }
             ],
+            "identifier": "GSA-32501",
+            "isPartOf": "GSA-2015-09-14-01",
+            "issued": "2013-05-13",
             "keyword": [
                 "Interactive",
                 "states"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-21",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "spatial": "United States",
             "theme": [
                 "States",
                 "Top 10"
-            ]
+            ],
+            "title": "Data.gov Top 10 Visiting States - Archival"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Data.gov Datasets Download By Data Category - Archival",
-            "description": "This dataset provides archival data on downloads for different data categories in Data.gov based on a previous dataset management system for Data.gov. Download represents the number of times a user has clicked on the XML or CSV (for example) links in the catalog to download datasets in these categories.",
-            "modified": "2016-01-20",
             "accessLevel": "public",
-            "identifier": "GSA-32031",
-            "dataQuality": true,
-            "describedBy": "http://www.data.gov/metric",
-            "describedByType": "text/csv",
-            "issued": "2013-04-11",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "Worldwide",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "GSA-2015-09-14-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Joo Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.data.gov/metric",
+            "describedByType": "text/csv",
+            "description": "This dataset provides archival data on downloads for different data categories in Data.gov based on a previous dataset management system for Data.gov. Download represents the number of times a user has clicked on the XML or CSV (for example) links in the catalog to download datasets in these categories.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/05c94390-bd32-4ae5-955e-6c812143a4fc/resource/5a64130b-d5d8-421b-9f2d-c8d6ff25b28b/download/userssharedsdfdata.govdatasetsdownloadbydatacategory.csv",
                     "format": "text/csv",
-                    "title": "Data.gov_Datasets_Download_By_Data_Category.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/05c94390-bd32-4ae5-955e-6c812143a4fc/resource/5a64130b-d5d8-421b-9f2d-c8d6ff25b28b/download/userssharedsdfdata.govdatasetsdownloadbydatacategory.csv"
+                    "mediaType": "text/csv",
+                    "title": "Data.gov_Datasets_Download_By_Data_Category.csv"
                 }
             ],
+            "identifier": "GSA-32031",
+            "isPartOf": "GSA-2015-09-14-01",
+            "issued": "2013-04-11",
             "keyword": [
                 "Category",
                 "Data.gov",
@@ -1278,50 +1272,50 @@
                 "datasets",
                 "download"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-20",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "spatial": "Worldwide",
             "theme": [
                 "Datasets download metrics"
-            ]
+            ],
+            "title": "Data.gov Datasets Download By Data Category - Archival"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions Apr-June 2020, 3rd Qtr - US Bank",
-            "description": "Purchases made with the purchase card.  Files will be batched quarterly.",
-            "modified": "2020-08-04",
             "accessLevel": "public",
-            "identifier": "GSA-2020-08-04-01",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card.  Files will be batched quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "US Bank PC Qtr 3 2020",
                     "description": "Purchase Card Transactions for 3rd Quarter",
-                    "downloadURL": "https://inventory.data.gov/dataset/25d36a55-e870-4b2d-9954-7042d2d7b7e9/resource/3a66ca12-e8af-491a-ac42-5d635dfb84ba/download/us-bank-pc-qtr3-2020.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/25d36a55-e870-4b2d-9954-7042d2d7b7e9/resource/3a66ca12-e8af-491a-ac42-5d635dfb84ba/download/us-bank-pc-qtr3-2020.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "US Bank PC Qtr 3 2020"
                 }
             ],
+            "identifier": "GSA-2020-08-04-01",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "april",
                 "june",
@@ -1329,51 +1323,51 @@
                 "purchase card",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-08-04",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions Apr-June 2020, 3rd Qtr - US Bank"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA Apr-June 2020, 3rd Qtr",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2020-08-05",
             "accessLevel": "public",
-            "identifier": "GSA-2020-08-05-01",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "2020 - 3rd Qtr (Apr-June)_CBCA PC",
                     "description": "3rd Quarter CBCA Purchase Card Transactions",
-                    "downloadURL": "https://inventory.data.gov/dataset/619a4a55-8b9d-427d-9e3b-6a4db1158fc6/resource/a394787c-589e-407f-8b62-1c46746f8d56/download/2020-3rd-qtr-apr-june-cbca-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/619a4a55-8b9d-427d-9e3b-6a4db1158fc6/resource/a394787c-589e-407f-8b62-1c46746f8d56/download/2020-3rd-qtr-apr-june-cbca-pc-transactions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "2020 - 3rd Qtr (Apr-June)_CBCA PC"
                 }
             ],
+            "identifier": "GSA-2020-08-05-01",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Contract Board",
@@ -1384,105 +1378,101 @@
                 "june",
                 "may"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-08-05",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA Apr-June 2020, 3rd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2020, 3rd Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2020-08-14",
             "accessLevel": "public",
-            "identifier": "GSA-2020-08-14-01",
-            "dataQuality": true,
-            "issued": "2015-11-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "Networx Business Volume FY20 3rd Qtr",
                     "description": "TotRevFY20_3rdQtr",
-                    "downloadURL": "https://inventory.data.gov/dataset/0844feb0-f5ab-4d34-9293-47c698b2a451/resource/86392610-3d0d-4a45-a011-a0e2b432c703/download/totrevfy203rdqtr.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/0844feb0-f5ab-4d34-9293-47c698b2a451/resource/86392610-3d0d-4a45-a011-a0e2b432c703/download/totrevfy203rdqtr.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Networx Business Volume FY20 3rd Qtr"
                 }
             ],
+            "identifier": "GSA-2020-08-14-01",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-11-13",
             "keyword": [
                 "Contract",
                 "Networx Telecommunications",
                 "Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-08-14",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Telecommunications Services"
-            ]
+            ],
+            "title": "Networx Business Volume FY2020, 3rd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "FY 2019 Federal Real Property Profile Data for Civilian Agencies",
-            "description": "An XLSX export of data from FRPP, a database of Federal Real Property \r\nfor Civilian Agencies.",
-            "modified": "2020-11-18",
             "accessLevel": "public",
-            "identifier": "GSA-2020-09-03-01",
-            "dataQuality": true,
-            "describedBy": "https://www.gsa.gov/cdnstatic/FY%202019%20FRPP%20DATA%20DICTIONARY%20Final%20V3.pdf",
-            "describedByType": "application/pdf",
-            "issued": "2019-09-24",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "US",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Government-wide Policy",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "General Services Administration"
-                }
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elizabeth Fahey",
                 "hasEmail": "mailto:elizabeth.fahey@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.gsa.gov/cdnstatic/FY%202019%20FRPP%20DATA%20DICTIONARY%20Final%20V3.pdf",
+            "describedByType": "application/pdf",
+            "description": "An XLSX export of data from FRPP, a database of Federal Real Property \r\nfor Civilian Agencies.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "FY 2019 Federal Real Property Profile Data for Civilian Agencies",
                     "description": "An XLSX export of data from FRPP, a database of Federal Real Property for Civilian Agencies.",
-                    "downloadURL": "https://inventory.data.gov/dataset/fe20be03-99bd-4dc6-ae08-fef9a4fb3544/resource/fa9449d5-09d7-49f4-8a1c-8e07a32c4b52/download/fy-2019-federal-real-property-profile-data-for-civilian-agencies.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/fe20be03-99bd-4dc6-ae08-fef9a4fb3544/resource/fa9449d5-09d7-49f4-8a1c-8e07a32c4b52/download/fy-2019-federal-real-property-profile-data-for-civilian-agencies.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2019 Federal Real Property Profile Data for Civilian Agencies"
                 }
             ],
+            "identifier": "GSA-2020-09-03-01",
+            "issued": "2019-09-24",
             "keyword": [
                 "FRPP",
                 "Federal Real Property Profile",
@@ -1498,494 +1488,497 @@
                 "structure",
                 "warehouse"
             ],
-            "bureauCode": [
-                "023:05"
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-18",
             "programCode": [
                 "023:015"
             ],
-            "language": [
-                "us-EN"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "City Pair Program (CSV)",
-            "description": "This csv file provides access to the City Pair Program FY15 Award data.",
-            "modified": "2015-05-19",
-            "accessLevel": "public",
-            "identifier": "GSA - 155327",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Government-wide Policy",
+                "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "General Services Administration"
+                }
+            },
+            "spatial": "US",
+            "title": "FY 2019 Federal Real Property Profile Data for Civilian Agencies"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Patrick Sok Son",
                 "hasEmail": "mailto:patrick.son@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "This csv file provides access to the City Pair Program FY15 Award data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://apps.fas.gsa.gov/citypairs/createcsv.cfm?runsched=yes&award_year=2015",
                     "format": "csv",
-                    "title": "City Pairs - FY15 Contract Awards",
-                    "downloadURL": "https://apps.fas.gsa.gov/citypairs/createcsv.cfm?runsched=yes&award_year=2015"
+                    "mediaType": "text/csv",
+                    "title": "City Pairs - FY15 Contract Awards"
                 }
             ],
+            "identifier": "GSA - 155327",
             "keyword": [
                 "City Pair Program"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2015-05-19",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Travel"
-            ]
+            ],
+            "title": "City Pair Program (CSV)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Data.gov Dataset Visitor Metrics",
-            "description": "The dataset provides metrics for the number of dataset views in catalog.data.gov broken down by month starting Jan 2014. There is a gap in the dataset for December 2016 due to a temporary halt in collection of metrics during infrastructure migration of the Data.gov site during that month.",
-            "modified": "2017-10-14",
             "accessLevel": "public",
-            "identifier": "GSA - 139375",
-            "dataQuality": true,
-            "describedBy": "https://inventory.data.gov/dataset/data-gov-dataset-view-metrics",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "GSA-2015-09-14-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://inventory.data.gov/dataset/data-gov-dataset-view-metrics",
+            "description": "The dataset provides metrics for the number of dataset views in catalog.data.gov broken down by month starting Jan 2014. There is a gap in the dataset for December 2016 due to a temporary halt in collection of metrics during infrastructure migration of the Data.gov site during that month.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "text/csv",
-                    "title": "datagov_datasets_view_metrics.csv",
                     "description": "Data.gov Datasets View Metrics",
-                    "downloadURL": "https://inventory.data.gov/dataset/e5ba009c-3e40-4f5a-b010-e294a8369ba4/resource/7385188a-84f1-4e1a-8e78-05e694b65bdf/download/datagovdatasetsviewmetrics.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/e5ba009c-3e40-4f5a-b010-e294a8369ba4/resource/7385188a-84f1-4e1a-8e78-05e694b65bdf/download/datagovdatasetsviewmetrics.csv",
+                    "format": "text/csv",
+                    "mediaType": "text/csv",
+                    "title": "datagov_datasets_view_metrics.csv"
                 }
             ],
+            "identifier": "GSA - 139375",
+            "isPartOf": "GSA-2015-09-14-01",
             "keyword": [
                 "Data",
                 "Data.gov",
                 "metrics"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "us-en"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2017-10-14",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "us-en"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Data metrics"
-            ]
+            ],
+            "title": "Data.gov Dataset Visitor Metrics"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2013, 4th Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
             "accessLevel": "public",
-            "identifier": "GSA-2015-02-26-2",
-            "dataQuality": false,
-            "describedBy": "https://www.asap.gsa.gov/datagov/networx/networx_revenue_data_dictionary.html",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": false,
+            "describedBy": "https://www.asap.gsa.gov/datagov/networx/networx_revenue_data_dictionary.html",
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "TotRevFY13_4thQtr Data",
                     "description": "TotRevFY13_3rdQtr Data",
-                    "downloadURL": "https://inventory.data.gov/dataset/5e375e42-9970-4dc2-8f7e-8d183758423e/resource/d3c8790c-f6ae-4667-b3d2-c57ed2d7de62/download/totrevfy134thqtr.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/5e375e42-9970-4dc2-8f7e-8d183758423e/resource/d3c8790c-f6ae-4667-b3d2-c57ed2d7de62/download/totrevfy134thqtr.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY13_4thQtr Data"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "TotRevFY13_4thQtr - Data element Descriptions",
                     "description": "Description of the Data elements presented in \"TotRevFY13_3thQtr Data\" resource.",
-                    "downloadURL": "https://inventory.data.gov/dataset/5e375e42-9970-4dc2-8f7e-8d183758423e/resource/19a72d90-75d2-4675-ac08-3609192e23e5/download/totrevfy134thqtrdataelementdescriptions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/5e375e42-9970-4dc2-8f7e-8d183758423e/resource/19a72d90-75d2-4675-ac08-3609192e23e5/download/totrevfy134thqtrdataelementdescriptions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY13_4thQtr - Data element Descriptions"
                 }
             ],
+            "identifier": "GSA-2015-02-26-2",
+            "isPartOf": "GSA-2015-08-27",
             "keyword": [
                 "Networx Telecommunications",
                 "telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2014, 2nd Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
-            "accessLevel": "public",
-            "identifier": "GSA-2015-02-26-4",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/networx/networx_revenue_data_dictionary.html",
-            "issued": "2015-03-03",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "National",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "spatial": "National",
+            "title": "Networx Business Volume FY2013, 4th Qtr"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/networx/networx_revenue_data_dictionary.html",
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "TotRevFY14_2ndQtr Data",
                     "description": "TotRevFY14_2ndQtr Data",
-                    "downloadURL": "https://inventory.data.gov/dataset/e30708c5-0801-42ef-8678-f30a6b3176a5/resource/57a062d1-559d-4399-b5ca-3f5c9584e49c/download/totrevfy142ndqtr.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/e30708c5-0801-42ef-8678-f30a6b3176a5/resource/57a062d1-559d-4399-b5ca-3f5c9584e49c/download/totrevfy142ndqtr.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY14_2ndQtr Data"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "TotRevFY14_2ndQtr - Data element Descriptions",
                     "description": "Description of the Data elements presented in \"TotRevFY14_2ndQtr Data\" resource.",
-                    "downloadURL": "https://inventory.data.gov/dataset/e30708c5-0801-42ef-8678-f30a6b3176a5/resource/664ed9f0-579b-43a5-96c7-0e39a7fc63ea/download/totrevfy142ndqtrdataelementdescriptions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/e30708c5-0801-42ef-8678-f30a6b3176a5/resource/664ed9f0-579b-43a5-96c7-0e39a7fc63ea/download/totrevfy142ndqtrdataelementdescriptions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY14_2ndQtr - Data element Descriptions"
                 }
             ],
+            "identifier": "GSA-2015-02-26-4",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-03-03",
             "keyword": [
                 "Networx Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2014, 3rd Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
-            "accessLevel": "public",
-            "identifier": "GSA-2015-02-26-5",
-            "dataQuality": false,
-            "issued": "2015-02-27",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "National",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "spatial": "National",
+            "title": "Networx Business Volume FY2014, 2nd Qtr"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": false,
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "TotRevFY14_3rdQtr Data",
                     "description": "TotRevFY14_3rdQtr Data",
-                    "downloadURL": "https://inventory.data.gov/dataset/6af87c9b-edc8-40cf-b692-6c35aa3d0e21/resource/4fc1bd3a-5019-4c45-9518-7543616d6049/download/totrevfy143rdqtr.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/6af87c9b-edc8-40cf-b692-6c35aa3d0e21/resource/4fc1bd3a-5019-4c45-9518-7543616d6049/download/totrevfy143rdqtr.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY14_3rdQtr Data"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "TotRevFY14_3rdQtr - Data element Descriptions",
                     "description": "Description of the Data elements presented in \"TotRevFY14_3rdQtr Data\" resource.",
-                    "downloadURL": "https://inventory.data.gov/dataset/6af87c9b-edc8-40cf-b692-6c35aa3d0e21/resource/dd2a75cd-9810-4335-9d57-3adc82c7ba0b/download/totrevfy143rdqtrdataelementdescriptions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/6af87c9b-edc8-40cf-b692-6c35aa3d0e21/resource/dd2a75cd-9810-4335-9d57-3adc82c7ba0b/download/totrevfy143rdqtrdataelementdescriptions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY14_3rdQtr - Data element Descriptions"
                 }
             ],
+            "identifier": "GSA-2015-02-26-5",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-02-27",
             "keyword": [
                 "networx business volume",
                 "revenue"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2015, 1st Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
-            "accessLevel": "public",
-            "identifier": "GSA-2015-03-02-2",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/networx/networx_revenue_data_dictionary.html",
-            "issued": "2015-03-03",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "spatial": "National",
+            "title": "Networx Business Volume FY2014, 3rd Qtr"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/networx/networx_revenue_data_dictionary.html",
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "TotRevFY15_1stQtr Data",
                     "description": "TotRevFY15_1stQtr Data",
-                    "downloadURL": "https://inventory.data.gov/dataset/38675b52-bfc1-41e1-ac88-303ce468cc7d/resource/a6017a41-2033-4e03-bb32-d74f32338391/download/totrevfy151stqtr.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/38675b52-bfc1-41e1-ac88-303ce468cc7d/resource/a6017a41-2033-4e03-bb32-d74f32338391/download/totrevfy151stqtr.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY15_1stQtr Data"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "TotRevFY15_1stQtr - Data element Descriptions",
                     "description": "Description of the Data elements presented in \"TotRevFY15_1stQtr Data\" resource.",
-                    "downloadURL": "https://inventory.data.gov/dataset/38675b52-bfc1-41e1-ac88-303ce468cc7d/resource/1c426769-8bd5-4440-9192-8b84834802cc/download/totrevfy151stqtrdataelementdescriptions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/38675b52-bfc1-41e1-ac88-303ce468cc7d/resource/1c426769-8bd5-4440-9192-8b84834802cc/download/totrevfy151stqtrdataelementdescriptions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY15_1stQtr - Data element Descriptions"
                 }
             ],
+            "identifier": "GSA-2015-03-02-2",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-03-03",
             "keyword": [
                 "Networx Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2015, 2nd Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
-            "accessLevel": "public",
-            "identifier": "GSA-2015-05-18-1",
-            "dataQuality": true,
-            "issued": "2015-05-18",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "title": "Networx Business Volume FY2015, 1st Qtr"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "TotRevFY15_2ndQtr Data",
                     "description": "TotRevFY15_2ndQtr Data",
-                    "downloadURL": "https://inventory.data.gov/dataset/54a13558-83ad-46c0-8c48-efe5f5bab48e/resource/3329e2ba-9915-4e1c-bdd3-89b81f7c28c8/download/totrevfy152ndqtr.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/54a13558-83ad-46c0-8c48-efe5f5bab48e/resource/3329e2ba-9915-4e1c-bdd3-89b81f7c28c8/download/totrevfy152ndqtr.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY15_2ndQtr Data"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "TotRevFY15_2ndQtr - Data element Descriptions",
                     "description": "Description of the Data elements presented in \"TotRevFY15_2ndQtr Data\" resource.",
-                    "downloadURL": "https://inventory.data.gov/dataset/54a13558-83ad-46c0-8c48-efe5f5bab48e/resource/c0dacdf8-0d61-4d62-8894-ab40bafd082a/download/totrevfy152ndqtrdataelementdescriptions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/54a13558-83ad-46c0-8c48-efe5f5bab48e/resource/c0dacdf8-0d61-4d62-8894-ab40bafd082a/download/totrevfy152ndqtrdataelementdescriptions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY15_2ndQtr - Data element Descriptions"
                 }
             ],
+            "identifier": "GSA-2015-05-18-1",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-05-18",
             "keyword": [
                 "Networx Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2014, 1st Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
-            "accessLevel": "public",
-            "identifier": "GSA-2015-02-26-3",
-            "dataQuality": false,
-            "describedBy": "https://www.asap.gsa.gov/datagov/networx/networx_revenue_data_dictionary.html",
-            "issued": "2015-02-27",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "National",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "title": "Networx Business Volume FY2015, 2nd Qtr"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": false,
+            "describedBy": "https://www.asap.gsa.gov/datagov/networx/networx_revenue_data_dictionary.html",
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "TotRevFY14_1stQtr Data",
                     "description": "TotRevFY14_1stQtr Data",
-                    "downloadURL": "https://inventory.data.gov/dataset/9f6683f7-4878-4cb8-93e2-98db46e1d283/resource/ee29e6de-f1b6-4ab0-ada4-250e6d8bee85/download/totrevfy141stqtr.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/9f6683f7-4878-4cb8-93e2-98db46e1d283/resource/ee29e6de-f1b6-4ab0-ada4-250e6d8bee85/download/totrevfy141stqtr.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY14_1stQtr Data"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "TotRevFY14_1stQtr - Data element Descriptions",
                     "description": "Description of the Data elements presented in \"TotRevFY14_1stQtr Data\" resource.",
-                    "downloadURL": "https://inventory.data.gov/dataset/9f6683f7-4878-4cb8-93e2-98db46e1d283/resource/ba3f9d79-8813-4787-9aea-fb03ecb85f9a/download/totrevfy141stqtrdataelementdescriptions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/9f6683f7-4878-4cb8-93e2-98db46e1d283/resource/ba3f9d79-8813-4787-9aea-fb03ecb85f9a/download/totrevfy141stqtrdataelementdescriptions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY14_1stQtr - Data element Descriptions"
                 }
             ],
+            "identifier": "GSA-2015-02-26-3",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-02-27",
             "keyword": [
                 "Networx Telecommunications",
                 "telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2014, 4th Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
-            "accessLevel": "public",
-            "identifier": "GSA-2015-02-26-6",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/networx/networx_revenue_data_dictionary.html",
-            "issued": "2015-02-27",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "National",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "spatial": "National",
+            "title": "Networx Business Volume FY2014, 1st Qtr"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/networx/networx_revenue_data_dictionary.html",
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "TotRevFY14_4thQtr Data",
                     "description": "TotRevFY14_4thQtr Data",
-                    "downloadURL": "https://inventory.data.gov/dataset/7555a0c0-0bb7-41d0-9430-4e5349c8b1da/resource/0945af83-6010-455e-b267-002106d30634/download/totrevfy144thqtr.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/7555a0c0-0bb7-41d0-9430-4e5349c8b1da/resource/0945af83-6010-455e-b267-002106d30634/download/totrevfy144thqtr.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY14_4thQtr Data"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "TotRevFY14_4thQtr - Data element Descriptions",
                     "description": "Description of the Data elements presented in \"TotRevFY14_4thQtr Data\" resource.",
-                    "downloadURL": "https://inventory.data.gov/dataset/7555a0c0-0bb7-41d0-9430-4e5349c8b1da/resource/d5aa2464-53a6-42db-b5ce-2c141a6d9541/download/totrevfy144thqtrdataelementdescriptions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/7555a0c0-0bb7-41d0-9430-4e5349c8b1da/resource/d5aa2464-53a6-42db-b5ce-2c141a6d9541/download/totrevfy144thqtrdataelementdescriptions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY14_4thQtr - Data element Descriptions"
                 }
             ],
+            "identifier": "GSA-2015-02-26-6",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-02-27",
             "keyword": [
                 "Networx Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Real Estate Across the United States (REXUS) Inventory (Building)",
-            "description": "Real Estate Across the United States (REXUS) is the primary tool used by PBS to track and manage the government's real property assets and to store inventory data, building data, customer data, and lease information. STAR manages aspects of real property space management, including identification of all building space and daily management of 22,000 assignments for all property to its client Federal agencies. This data set contains PBS building inventory that consists of both owned and leased buildings with active and excess status.",
-            "modified": "2022-08-01T12:54:47.495Z",
-            "accessLevel": "public",
-            "identifier": "GSA-25251",
-            "dataQuality": true,
-            "issued": "2011-07-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
-            "spatial": "US",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "spatial": "National",
+            "title": "Networx Business Volume FY2014, 4th Qtr"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Uba",
                 "hasEmail": "mailto:tom.uba@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Real Estate Across the United States (REXUS) is the primary tool used by PBS to track and manage the government's real property assets and to store inventory data, building data, customer data, and lease information. STAR manages aspects of real property space management, including identification of all building space and daily management of 22,000 assignments for all property to its client Federal agencies. This data set contains PBS building inventory that consists of both owned and leased buildings with active and excess status.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/04247624-1d6b-4e03-84eb-9eda1a6ea638/resource/12025a4f-1538-4ecf-a01e-77e1939f2d5d/download/data_gov_bldg_rexus.csv",
                     "mediaType": "text/csv",
-                    "title": "data_gov_bldg_rexus.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/04247624-1d6b-4e03-84eb-9eda1a6ea638/resource/12025a4f-1538-4ecf-a01e-77e1939f2d5d/download/data_gov_bldg_rexus.csv"
+                    "title": "data_gov_bldg_rexus.csv"
                 }
             ],
+            "identifier": "GSA-25251",
+            "issued": "2011-07-01",
             "keyword": [
                 "building",
                 "gsa",
@@ -1994,45 +1987,46 @@
                 "real estate",
                 "real property"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-08-01T12:54:47.495Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Real Estate Across the United States (REXUS) (Lease)",
-            "description": "Real Estate Across the United States (REXUS) is the primary tool used by PBS to track and manage the government's real property assets and to store inventory data, building data, customer data, and lease information. STAR manages aspects of real property space management, including identification of all building space and daily management of 22,000 assignments for all property to its client Federal agencies. This data set contains PBS building inventory that consists of both owned and leased buildings with active and excess status.",
-            "modified": "2022-08-01T13:10:15.814Z",
-            "accessLevel": "public",
-            "identifier": "GSA-25261",
-            "dataQuality": true,
-            "issued": "2011-07-15",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "rights": "true",
+            "spatial": "US",
+            "title": "Real Estate Across the United States (REXUS) Inventory (Building)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Uba",
                 "hasEmail": "mailto:tom.uba@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Real Estate Across the United States (REXUS) is the primary tool used by PBS to track and manage the government's real property assets and to store inventory data, building data, customer data, and lease information. STAR manages aspects of real property space management, including identification of all building space and daily management of 22,000 assignments for all property to its client Federal agencies. This data set contains PBS building inventory that consists of both owned and leased buildings with active and excess status.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/2cdc97b5-3029-4ec3-b3bf-baec7948bad1/resource/b16a0800-68dd-48c3-aa6d-8c975ed6f4ac/download/data_gov_lse_rexus.csv",
                     "mediaType": "text/csv",
-                    "title": "data_gov_lse_rexus.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/2cdc97b5-3029-4ec3-b3bf-baec7948bad1/resource/b16a0800-68dd-48c3-aa6d-8c975ed6f4ac/download/data_gov_lse_rexus.csv"
+                    "title": "data_gov_lse_rexus.csv"
                 }
             ],
+            "identifier": "GSA-25261",
+            "issued": "2011-07-15",
             "keyword": [
                 "building",
                 "gsa",
@@ -2041,138 +2035,135 @@
                 "real estate",
                 "real property"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2022-08-01T13:10:15.814Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2020, 4th Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2020-11-18",
-            "accessLevel": "public",
-            "identifier": "GSA-2020-11-18-01",
-            "dataQuality": true,
-            "issued": "2015-11-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "rights": "true",
+            "title": "Real Estate Across the United States (REXUS) (Lease)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "Networx Business Volume FY20 4th Qtr",
                     "description": "TotRevFY20_4thQtr",
-                    "downloadURL": "https://inventory.data.gov/dataset/ece893ff-c29b-4bad-bf8e-cde8d2658969/resource/7ebe6e5f-fd85-436f-8697-943766b9bb87/download/totrevfy204thqtr.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/ece893ff-c29b-4bad-bf8e-cde8d2658969/resource/7ebe6e5f-fd85-436f-8697-943766b9bb87/download/totrevfy204thqtr.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Networx Business Volume FY20 4th Qtr"
                 }
             ],
+            "identifier": "GSA-2020-11-18-01",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-11-13",
             "keyword": [
                 "Contract",
                 "Networx Telecommunications",
                 "Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-18",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Telecommunications Services"
-            ]
+            ],
+            "title": "Networx Business Volume FY2020, 4th Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Acquisition Service Instructional Letter 2009-01 Applying the IFF to Sch",
-            "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.  All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
-            "modified": "2017-05-08",
             "accessLevel": "public",
-            "identifier": "GSA-4593",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/fas-il/IL_01_data_dictionary.html",
-            "issued": "2011-02-22",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "GSA-2015-09-14-02",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David W Orcutt",
                 "hasEmail": "mailto:david.orcutt@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/fas-il/IL_01_data_dictionary.html",
+            "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.  All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/msword",
-                    "format": "doc",
-                    "title": "FAS INSTRUCTIONAL LETTER 2009-01",
                     "description": "Applying the Industrial Funding Fee (IFF) to Schedule Pricing.",
-                    "downloadURL": "https://inventory.data.gov/dataset/c6b18dfe-afe0-459a-94a0-6441fdf948d1/resource/caef4305-3eb6-41ce-b4f9-d16bfeffbf98/download/fas-instructional-letter-2009-01.docx"
+                    "downloadURL": "https://inventory.data.gov/dataset/c6b18dfe-afe0-459a-94a0-6441fdf948d1/resource/caef4305-3eb6-41ce-b4f9-d16bfeffbf98/download/fas-instructional-letter-2009-01.docx",
+                    "format": "doc",
+                    "mediaType": "application/msword",
+                    "title": "FAS INSTRUCTIONAL LETTER 2009-01"
                 }
             ],
+            "identifier": "GSA-4593",
+            "isPartOf": "GSA-2015-09-14-02",
+            "issued": "2011-02-22",
             "keyword": [
                 "Industrial Funding Fee"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2017-05-08",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "Federal Acquisition Service Instructional Letter 2009-01 Applying the IFF to Sch"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Acquisition Workforce Annual Report 2006",
-            "description": "This is the Federal Acquisition Institute's (FAI's) Annual demographic report on the Federal acquisition workforce, showing trends by occupational series, employment grade and educational level, as well as turnover and hiring data for fiscal year (FY) 2006.",
-            "modified": "2009-01-31",
             "accessLevel": "public",
-            "identifier": "GSA-4733",
-            "dataQuality": true,
-            "describedBy": "http://www.fai.gov/fapis.asp",
-            "issued": "2009-01-31",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "US domestic",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John P Andre",
                 "hasEmail": "mailto:john.andre@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.fai.gov/fapis.asp",
+            "description": "This is the Federal Acquisition Institute's (FAI's) Annual demographic report on the Federal acquisition workforce, showing trends by occupational series, employment grade and educational level, as well as turnover and hiring data for fiscal year (FY) 2006.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2180,139 +2171,141 @@
                     "title": "Acquisition Workforce Annual Report 2006"
                 }
             ],
+            "identifier": "GSA-4733",
+            "issued": "2009-01-31",
             "keyword": [
                 "Federal acquisition workforce report",
                 "Federal acquisition workforce statistics"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2009-01-31",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "US domestic",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "Acquisition Workforce Annual Report 2006"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "City Pair Program",
-            "description": "The City Pair Program offers discounted air passenger transportation for federal government travelers. The airfares offered under this program are discounted considerably off of comparable commercial fares, saving the federal government and taxpayers billions of dollars annually. In addition, these contracted annual fares enable government agencies to project travel costs and forecast their travel budgets more accurately.",
-            "modified": "2013-09-30",
             "accessLevel": "public",
-            "identifier": "GSA - 138584",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jerome Charles Bristow",
                 "hasEmail": "mailto:jerome.bristow@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The City Pair Program offers discounted air passenger transportation for federal government travelers. The airfares offered under this program are discounted considerably off of comparable commercial fares, saving the federal government and taxpayers billions of dollars annually. In addition, these contracted annual fares enable government agencies to project travel costs and forecast their travel budgets more accurately.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "http://gsa.gov/portal/category/27093",
                     "format": "text/html",
-                    "title": "City Pair Program",
-                    "downloadURL": "http://gsa.gov/portal/category/27093"
+                    "mediaType": "text/html",
+                    "title": "City Pair Program"
                 }
             ],
+            "identifier": "GSA - 138584",
             "keyword": [
                 "CPP",
                 "City Pair Program",
                 "Travel"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2013-09-30",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Travel and Transportation"
-            ]
+            ],
+            "title": "City Pair Program"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Concur - Reporting Authorization Model",
-            "description": "The data dictionary for the reporting authorization model  within Concur.",
-            "modified": "2016-02-23",
             "accessLevel": "non-public",
-            "identifier": "GSA - 139042",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-09-11-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Norma H Tolson",
                 "hasEmail": "mailto:norma.tolson@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The data dictionary for the reporting authorization model  within Concur.",
+            "identifier": "GSA - 139042",
+            "isPartOf": "GSA-2015-09-11-01",
             "keyword": [
                 "Credit Card",
                 "purchase card",
                 "travel card"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-02-23",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
             "theme": [
                 "Travel and Transportation"
-            ]
+            ],
+            "title": "Concur - Reporting Authorization Model"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GobiernoUSA.gov Blog RSS feed",
-            "description": "We help you find official U.S. government information and services in Spanish on the Internet.",
-            "modified": "2016-01-07",
             "accessLevel": "public",
-            "identifier": "GSA-2014-02-14-2",
-            "dataQuality": true,
-            "describedBy": "http://www.rssboard.org/rss-specification",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Russell G O'Neill",
                 "hasEmail": "mailto:russell.oneill@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.rssboard.org/rss-specification",
+            "description": "We help you find official U.S. government information and services in Spanish on the Internet.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "http://blog.gobiernousa.gov/rss",
                     "format": "text/html",
-                    "title": "GobiernoUSA.gov Blog RSS feed",
-                    "downloadURL": "http://blog.gobiernousa.gov/rss"
+                    "mediaType": "text/html",
+                    "title": "GobiernoUSA.gov Blog RSS feed"
                 }
             ],
+            "identifier": "GSA-2014-02-14-2",
             "keyword": [
                 "Blog",
                 "Consumer",
@@ -2322,40 +2315,39 @@
                 "government services",
                 "news"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:014"
-            ],
             "language": [
                 "en-us"
             ],
-            "theme": [
-                "Other"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "USA.gov Blog RSS feed",
-            "description": "We help you find official U.S. government information and services on the Internet.",
-            "modified": "2016-01-07",
-            "accessLevel": "public",
-            "identifier": "GSA-2014-02-14-6",
-            "dataQuality": true,
-            "describedBy": "http://www.rssboard.org/rss-specification",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
+            "modified": "2016-01-07",
+            "programCode": [
+                "023:014"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "rights": "N/A",
+            "spatial": "National",
+            "theme": [
+                "Other"
+            ],
+            "title": "GobiernoUSA.gov Blog RSS feed"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Russell G O'Neill",
                 "hasEmail": "mailto:russell.oneill@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.rssboard.org/rss-specification",
+            "description": "We help you find official U.S. government information and services on the Internet.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2364,6 +2356,7 @@
                     "title": "USA.gov Blog RSS feed"
                 }
             ],
+            "identifier": "GSA-2014-02-14-6",
             "keyword": [
                 "Blog",
                 "Consumer",
@@ -2372,41 +2365,42 @@
                 "government services",
                 "news"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-07",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Information Technology"
-            ]
+            ],
+            "title": "USA.gov Blog RSS feed"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "e-Buy Awards Parent",
-            "description": "This is the Parent folder for GSA e-Buy Fiscal Year information, e-Buy is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts.",
-            "modified": "2015-09-04",
             "accessLevel": "public",
-            "identifier": "GSA-2015-08-31",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/eBuy_Awards_Data_Dictionary.html",
-            "issued": "2015-08-31",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Usha Gopal",
                 "hasEmail": "mailto:usha.gopal@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/eBuy_Awards_Data_Dictionary.html",
+            "description": "This is the Parent folder for GSA e-Buy Fiscal Year information, e-Buy is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts.",
+            "identifier": "GSA-2015-08-31",
+            "issued": "2015-08-31",
             "keyword": [
                 "Award",
                 "Contracts",
@@ -2414,42 +2408,39 @@
                 "Schedules",
                 "e-Buy"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2015-09-04",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "spatial": "National",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "e-Buy Awards Parent"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Acquisition Workforce Annual Report 2008",
-            "description": "This is the Federal Acquisition Institute's (FAI's) Annual demographic report on the Federal acquisition workforce, showing trends by occupational series, employment grade and educational level, as well as turnover and hiring data for fiscal year (FY) 2008.",
-            "modified": "2024-11-05T16:01:29.980Z",
             "accessLevel": "public",
-            "identifier": "GSA-4732",
-            "dataQuality": true,
-            "describedBy": "http://www.fai.gov/fapis.asp",
-            "issued": "2009-01-31",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "US domestic",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John P Andre",
                 "hasEmail": "mailto:john.andre@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.fai.gov/fapis.asp",
+            "description": "This is the Federal Acquisition Institute's (FAI's) Annual demographic report on the Federal acquisition workforce, showing trends by occupational series, employment grade and educational level, as well as turnover and hiring data for fiscal year (FY) 2008.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2457,56 +2448,58 @@
                     "title": "Acquisition Workforce Annual Report 2008"
                 }
             ],
+            "identifier": "GSA-4732",
+            "issued": "2009-01-31",
             "keyword": [
                 "Federal acquisition workforce report",
                 "Federal acquisition workforce statistics"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-11-05T16:01:29.980Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "US domestic",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "Acquisition Workforce Annual Report 2008"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "e-Buy Awards for Fiscal Year 2008",
-            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
-            "modified": "2016-01-21",
             "accessLevel": "public",
-            "identifier": "GSA-4097",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/eBuy_Awards_Data_Dictionary.html",
-            "issued": "2010-10-21",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-08-31",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Usha Gopal",
                 "hasEmail": "mailto:usha.gopal@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/eBuy_Awards_Data_Dictionary.html",
+            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/eBuy_Awards_FY2008.xls",
                     "format": "excel",
-                    "title": "e-Buy Awards for Fiscal Year 2008",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/eBuy_Awards_FY2008.xls"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "e-Buy Awards for Fiscal Year 2008"
                 }
             ],
+            "identifier": "GSA-4097",
+            "isPartOf": "GSA-2015-08-31",
+            "issued": "2010-10-21",
             "keyword": [
                 "Award",
                 "Contracts",
@@ -2516,90 +2509,90 @@
                 "Schedules",
                 "e-Buy"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-21",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "e-Buy Awards for Fiscal Year 2008"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "FAS Instructional Letters 2008-02 Modification Receipt, Dates and Types",
-            "description": "This acquisition process improvement will enhance both the quality of contract modification data and our ability to process contract modifications electronically. The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts. All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
-            "modified": "2017-05-08",
             "accessLevel": "public",
-            "identifier": "GSA-5134",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/fas-il/IL_2007_2008.html",
-            "issued": "2011-07-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "GSA-2015-09-14-02",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David W Orcutt",
                 "hasEmail": "mailto:david.orcutt@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/fas-il/IL_2007_2008.html",
+            "description": "This acquisition process improvement will enhance both the quality of contract modification data and our ability to process contract modifications electronically. The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts. All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/msword",
-                    "format": "doc",
-                    "title": "FAS Instructional Letter 2008-02",
                     "description": "Multiple Award Schedules (MAS) Program: Modification Receipt Dates and Types.",
-                    "downloadURL": "https://inventory.data.gov/dataset/5e038d47-8166-4e1c-af9d-c94dbff7c99b/resource/f341e53b-7e8e-40e5-857f-c94cb103332e/download/fas-instructional-letter-2008-02.docx"
+                    "downloadURL": "https://inventory.data.gov/dataset/5e038d47-8166-4e1c-af9d-c94dbff7c99b/resource/f341e53b-7e8e-40e5-857f-c94cb103332e/download/fas-instructional-letter-2008-02.docx",
+                    "format": "doc",
+                    "mediaType": "application/msword",
+                    "title": "FAS Instructional Letter 2008-02"
                 }
             ],
+            "identifier": "GSA-5134",
+            "isPartOf": "GSA-2015-09-14-02",
+            "issued": "2011-07-26",
             "keyword": [
                 "Acquisition",
                 "Instructional Letters"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2017-05-08",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "FAS Instructional Letters 2008-02 Modification Receipt, Dates and Types"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "FedBizOpps Documentation",
-            "description": "In addition to the ability to interact directly with FedBizOpps using its on-line web interface, the service supports Web Services for Federal buyers to post information to the database using their agency\u2019s electronic procurement system",
-            "modified": "2018-01-09",
             "accessLevel": "public",
-            "identifier": "GSA - 138672",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bob Maslyn",
                 "hasEmail": "mailto:bob.maslyn@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "In addition to the ability to interact directly with FedBizOpps using its on-line web interface, the service supports Web Services for Federal buyers to post information to the database using their agency\u2019s electronic procurement system",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2608,56 +2601,56 @@
                     "title": "FedBizOpps Documentation"
                 }
             ],
+            "identifier": "GSA - 138672",
             "keyword": [
                 "FedBizOpps",
                 "Federal Buyers",
                 "procurement"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-01-09",
             "programCode": [
                 "023:012"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "API"
-            ]
+            ],
+            "title": "FedBizOpps Documentation"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Acquisition Service Balanced Scorecard 2009",
-            "description": "Federal Acquisition Service Performance Measures are tracked for each of the four portfolios within the organization (Assisted Acquisition Services; General Supplies and Services; Integrated Technology Services; and Travel, Motor Vehicle, and Card Services) and are reported Annual.  Each measure aligns to one of Kaplan and Norton's Balanced Scorecard Perspectives:  customer, stakeholder, internal processes and technology, human capital, and financial.  The results reported here are collected and maintained by the Office of Strategy Management.",
-            "modified": "2015-11-16",
             "accessLevel": "public",
-            "identifier": "GSA-2584",
-            "dataQuality": true,
-            "issued": "1905-07-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-09-14-02",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David W Orcutt",
                 "hasEmail": "mailto:david.orcutt@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Federal Acquisition Service Performance Measures are tracked for each of the four portfolios within the organization (Assisted Acquisition Services; General Supplies and Services; Integrated Technology Services; and Travel, Motor Vehicle, and Card Services) and are reported Annual.  Each measure aligns to one of Kaplan and Norton's Balanced Scorecard Perspectives:  customer, stakeholder, internal processes and technology, human capital, and financial.  The results reported here are collected and maintained by the Office of Strategy Management.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "http://www.gsa.gov/dg/FAS%20Balanced%20Scorecard_2009.xlsx",
                     "format": "xlsx",
-                    "title": "Federal Acquisition Service Balanced Scorecard 2009",
-                    "downloadURL": "http://www.gsa.gov/dg/FAS%20Balanced%20Scorecard_2009.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Federal Acquisition Service Balanced Scorecard 2009"
                 }
             ],
+            "identifier": "GSA-2584",
+            "isPartOf": "GSA-2015-09-14-02",
+            "issued": "1905-07-01",
             "keyword": [
                 "Balanced Scorecard Perspectives",
                 "Customer",
@@ -2667,252 +2660,252 @@
                 "internal processes and technology",
                 "stakeholder"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2015-11-16",
             "programCode": [
                 "023:014"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "Federal Acquisition Service Balanced Scorecard 2009"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "American Job Center Resource API",
-            "description": "American Job Center partners with O'Net to provide a variety of APIs useful for jobseekers.",
-            "modified": "2015-11-16",
             "accessLevel": "public",
-            "identifier": "GSA - 138668",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:30"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Darlene S Meskell",
                 "hasEmail": "mailto:darlene.meskell@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "American Job Center partners with O'Net to provide a variety of APIs useful for jobseekers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "http://jobcenter.usa.gov/apis",
                     "format": "text/html",
-                    "title": "American Job Center Resource API",
-                    "downloadURL": "http://jobcenter.usa.gov/apis"
+                    "mediaType": "text/html",
+                    "title": "American Job Center Resource API"
                 }
             ],
+            "identifier": "GSA - 138668",
             "keyword": [
                 "American Job Center",
                 "Job",
                 "Resource Center"
             ],
-            "bureauCode": [
-                "023:30"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2015-11-16",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "API"
-            ]
+            ],
+            "title": "American Job Center Resource API"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual Reports",
-            "description": "These reports provide GSA financial and performance information, enabling the assessment of agency performance (Agency Financial Reports, Peformance and Accountability Reports, Citizen Reports, Annual Performance Reports)",
-            "modified": "2014-11-11",
             "accessLevel": "public",
-            "identifier": "GSA - 32792",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:30"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vivi D Tran-Chu",
                 "hasEmail": "mailto:vivi.tran@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "These reports provide GSA financial and performance information, enabling the assessment of agency performance (Agency Financial Reports, Peformance and Accountability Reports, Citizen Reports, Annual Performance Reports)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "http://www.gsa.gov/portal/category/26851",
                     "format": "html",
-                    "title": "Annual Reports",
-                    "downloadURL": "http://www.gsa.gov/portal/category/26851"
+                    "mediaType": "text/html",
+                    "title": "Annual Reports"
                 }
             ],
+            "identifier": "GSA - 32792",
             "keyword": [
                 "Agency Financial Report AFR",
                 "Annual Performance Reports",
                 "Citizens Reports",
                 "Performance and Accountability Reports PAR"
             ],
-            "bureauCode": [
-                "023:30"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2014-11-11",
             "programCode": [
                 "023:014"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Other"
-            ]
+            ],
+            "title": "Annual Reports"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Concur - Reporting User Profile Folder",
-            "description": "The data dictionary for the reporting user profile folder within Concur.",
-            "modified": "2016-02-23",
             "accessLevel": "non-public",
-            "identifier": "GSA - 139047",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-09-11-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Norma H Tolson",
                 "hasEmail": "mailto:norma.tolson@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The data dictionary for the reporting user profile folder within Concur.",
+            "identifier": "GSA - 139047",
+            "isPartOf": "GSA-2015-09-11-01",
             "keyword": [
                 "Credit Card",
                 "Travel Card"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-02-23",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
             "theme": [
                 "Travel and Transportation"
-            ]
+            ],
+            "title": "Concur - Reporting User Profile Folder"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Acquisition Service Instructional Letter 2014",
-            "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts. All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
-            "modified": "2020-12-22",
             "accessLevel": "public",
-            "identifier": "GSA - 139297",
-            "dataQuality": true,
-            "issued": "2014-07-22",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-09-14-02",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David W Orcutt",
                 "hasEmail": "mailto:david.orcutt@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts. All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://inventory.data.gov/dataset/8c2f4e37-7420-4467-adcd-65a454b4cde0/resource/741ffa4c-ca09-47b7-9d52-68fff90286e5/download/federal-acquisition-service-instructional-letters-2014.xlsx",
+                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
                     "format": "xlsx",
-                    "title": "FAS IL 2014",
-                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts."
+                    "title": "FAS IL 2014"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2014-01",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/8c2f4e37-7420-4467-adcd-65a454b4cde0/resource/9751a2c1-1f28-447f-bbfc-d357391e361d/download/instruction-letter-il-2014-01.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/8c2f4e37-7420-4467-adcd-65a454b4cde0/resource/9751a2c1-1f28-447f-bbfc-d357391e361d/download/instruction-letter-il-2014-01.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2014-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://inventory.data.gov/dataset/8c2f4e37-7420-4467-adcd-65a454b4cde0/resource/a2c6d9f0-120f-4fcc-96e0-fde47551faa6/download/instruction-letter-il-2014-02.pdf",
+                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
                     "format": "pdf",
-                    "title": "FAS IL 2014-02",
-                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts."
+                    "title": "FAS IL 2014-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://inventory.data.gov/dataset/8c2f4e37-7420-4467-adcd-65a454b4cde0/resource/a3b93cfe-7ce4-4caf-b5eb-601d209ed9e5/download/instruction-letter-il-2014-03.pdf",
+                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
                     "format": "pdf",
-                    "title": "FAS IL 2014-03",
-                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts."
+                    "title": "FAS IL 2014-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://inventory.data.gov/dataset/8c2f4e37-7420-4467-adcd-65a454b4cde0/resource/1c773eb9-fd8a-4e9c-8d2d-d3454fc4f453/download/instruction-letter-il-2014-04.pdf",
+                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
                     "format": "pdf",
-                    "title": "FAS IL 2014-04",
-                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts."
+                    "title": "FAS IL 2014-04"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2014-05",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/8c2f4e37-7420-4467-adcd-65a454b4cde0/resource/eb6d8b95-0894-416b-aa9d-4c1afc27691b/download/instruction-letter-il-2014-05.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/8c2f4e37-7420-4467-adcd-65a454b4cde0/resource/eb6d8b95-0894-416b-aa9d-4c1afc27691b/download/instruction-letter-il-2014-05.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2014-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2014-06",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/8c2f4e37-7420-4467-adcd-65a454b4cde0/resource/446c038c-d6de-464e-bc4a-d0a489d535a1/download/instruction-letter-il-2014-06.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/8c2f4e37-7420-4467-adcd-65a454b4cde0/resource/446c038c-d6de-464e-bc4a-d0a489d535a1/download/instruction-letter-il-2014-06.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2014-06"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2014-07",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/8c2f4e37-7420-4467-adcd-65a454b4cde0/resource/2c61f14e-e0ca-431b-8aa2-80a4af3127e9/download/instruction-letter-il-2014-07.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/8c2f4e37-7420-4467-adcd-65a454b4cde0/resource/2c61f14e-e0ca-431b-8aa2-80a4af3127e9/download/instruction-letter-il-2014-07.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2014-07"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2014-08",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/8c2f4e37-7420-4467-adcd-65a454b4cde0/resource/d8a4de08-87bc-4b31-8b3d-f236fd1fd2d0/download/instruction-letter-il-2014-08.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/8c2f4e37-7420-4467-adcd-65a454b4cde0/resource/d8a4de08-87bc-4b31-8b3d-f236fd1fd2d0/download/instruction-letter-il-2014-08.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2014-08"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://inventory.data.gov/dataset/8c2f4e37-7420-4467-adcd-65a454b4cde0/resource/59464574-8e18-4a8e-9bc9-8987989b23db/download/instructional-letter-il-14-09.pdf",
+                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
                     "format": "pdf",
-                    "title": "FAS IL 2014-09",
-                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts."
+                    "title": "FAS IL 2014-09"
                 }
             ],
+            "identifier": "GSA - 139297",
+            "isPartOf": "GSA-2015-09-14-02",
+            "issued": "2014-07-22",
             "keyword": [
                 "FAS",
                 "GSA",
@@ -2920,87 +2913,87 @@
                 "Instructional Letters",
                 "Interactive"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-22",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "United States",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "Federal Acquisition Service Instructional Letter 2014"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Strategic Sourcing Initiative (FSSI) PM",
-            "description": "FSSI Print Management BPA vendor submitted usage reports",
-            "modified": "2016-02-23",
             "accessLevel": "non-public",
-            "identifier": "GSA - 139668",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael J Wano",
                 "hasEmail": "mailto:mike.wano@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "FSSI Print Management BPA vendor submitted usage reports",
+            "identifier": "GSA - 139668",
             "keyword": [
                 "FSSI",
                 "Print Management"
             ],
-            "bureauCode": [
-                "023:10"
+            "language": [
+                "en-us"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-02-23",
             "programCode": [
                 "023:012"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "Federal Strategic Sourcing Initiative (FSSI) PM"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Inventory Reporting Information System (IRIS)",
-            "description": "IRIS Work Item Module supports Real Property Asset Management (RPAM) and the Financial Operation Division. IRIS manages the estimated cost of building projects related to repairs and alterations, and new construction",
-            "modified": "2018-10-09",
             "accessLevel": "public",
-            "identifier": "GSA-4306",
-            "dataQuality": true,
-            "issued": "2010-11-15",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bill Shah",
                 "hasEmail": "mailto:bill.shah@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "IRIS Work Item Module supports Real Property Asset Management (RPAM) and the Financial Operation Division. IRIS manages the estimated cost of building projects related to repairs and alterations, and new construction",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/1222bd0e-66b1-4e89-b185-298767a75837/resource/f0dadca9-d688-48d7-af0e-62bb4913b8be/download/irisbuildingestimateactive.csv",
                     "format": "csv",
-                    "title": "Inventory Reporting Information System (IRIS)",
-                    "downloadURL": "https://inventory.data.gov/dataset/1222bd0e-66b1-4e89-b185-298767a75837/resource/f0dadca9-d688-48d7-af0e-62bb4913b8be/download/irisbuildingestimateactive.csv"
+                    "mediaType": "text/csv",
+                    "title": "Inventory Reporting Information System (IRIS)"
                 }
             ],
+            "identifier": "GSA-4306",
+            "issued": "2010-11-15",
             "keyword": [
                 "Alterations",
                 "Building",
@@ -3014,192 +3007,193 @@
                 "Survey",
                 "repairs"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-10-09",
             "programCode": [
                 "023:014"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Real Estate"
-            ]
+            ],
+            "title": "Inventory Reporting Information System (IRIS)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2011, 2nd Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
             "accessLevel": "public",
-            "identifier": "GSA-5195",
-            "dataQuality": true,
-            "describedBy": "https://emorris.fasbilling.gsa.gov",
-            "issued": "2011-09-20",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://emorris.fasbilling.gsa.gov",
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/networx/networx_revenue_fy11_q2.xls",
                     "format": "xls",
-                    "title": "NetworxBusinessVolume_FY2011_2ndQtr",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/networx/networx_revenue_fy11_q2.xls"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NetworxBusinessVolume_FY2011_2ndQtr"
                 }
             ],
+            "identifier": "GSA-5195",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2011-09-20",
             "keyword": [
                 "Networx",
                 "telecommunications."
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Real Estate"
-            ]
+            ],
+            "title": "Networx Business Volume FY2011, 2nd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Schedule Sales Query Raw Data",
-            "description": "Schedule Sales Query presents sales volume figures as reported to GSA by contractors. The reports are generated as quarterly reports for the current year and the past five fiscal years. The sales data reported here are updated as contractors' reports are received, but the data may not be up to date as adjustments can be received at any time. The information on this site mirrors the data used by GSA for contract administration and fee management. It is not the official source of sales data. This data should be used for informational purposes only.",
-            "modified": "2010-08-09",
             "accessLevel": "public",
-            "identifier": "GSA-2581",
-            "dataQuality": true,
-            "describedBy": "http://ssq.gsa.gov",
-            "issued": "2009-02-18",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Usha Gopal",
                 "hasEmail": "mailto:usha.gopal@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://ssq.gsa.gov",
+            "description": "Schedule Sales Query presents sales volume figures as reported to GSA by contractors. The reports are generated as quarterly reports for the current year and the past five fiscal years. The sales data reported here are updated as contractors' reports are received, but the data may not be up to date as adjustments can be received at any time. The information on this site mirrors the data used by GSA for contract administration and fee management. It is not the official source of sales data. This data should be used for informational purposes only.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://ssq.gsa.gov/ReportSelection.cfm",
                     "format": "html",
-                    "title": "Schedule Sales Query Raw Data",
-                    "downloadURL": "https://ssq.gsa.gov/ReportSelection.cfm"
+                    "mediaType": "text/html",
+                    "title": "Schedule Sales Query Raw Data"
                 }
             ],
+            "identifier": "GSA-2581",
+            "issued": "2009-02-18",
             "keyword": [
                 "GSA contract administration and fee management",
                 "Schedule Sales Query",
                 "sales data report",
                 "sales volume figures"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2010-08-09",
             "programCode": [
                 "023:014"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Other"
-            ]
+            ],
+            "title": "Schedule Sales Query Raw Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Parent",
-            "description": "These datasets represent the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contract.  This collection contains data from FY2008 to the present.",
-            "modified": "2021-03-09T13:48:49.623Z",
             "accessLevel": "public",
-            "identifier": "GSA-2015-08-27",
-            "dataQuality": true,
-            "describedBy": "http://www.gsa.gov/networx",
-            "describedByType": "text/html",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.gsa.gov/networx",
+            "describedByType": "text/html",
+            "description": "These datasets represent the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contract.  This collection contains data from FY2008 to the present.",
+            "identifier": "GSA-2015-08-27",
             "keyword": [
                 "Networx",
                 "Parent",
                 "Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-03-09T13:48:49.623Z",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "true",
             "theme": [
                 "Telecommunications"
-            ]
+            ],
+            "title": "Networx Business Parent"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Auctions",
-            "description": "The General Services Administration (GSA) has a history of pioneering electronic solutions for streamlining and enhancing the management of excess and surplus Federal assets. GSA continued the transformation of the Federal disposal process throughout the late 1990s with the introduction and subsequent refinement of the Federal Disposal System, a centralized electronic clearinghouse for reporting and transferring excess/surplus personal property within the Federal community and among eligible donees.\n\nThe GSA Auctions website (www.gsaauctions.gov) has been developed to complete GSA's transformation to an all-electronic asset management system. The site offers the general public the opportunity to bid electronically on a wide array of Federal assets. The auctions are completely web-enabled, allowing all registered participants to bid on a single item or multiple items (lots) within specified timeframes.\n\nGSA Auctions offers Federal personal property assets ranging from commonplace items (such as office equipment and furniture) to more select products like scientific equipment, heavy machinery, airplanes, vessels, and vehicles. GSA Auctions online capabilities allow GSA to offer assets located across the country to any interested buyer, regardless of location.\n\nParticipants may choose to browse items that are offered on this site or may choose to search for items and place bids. In order to place a bid(s), participants must register first. To register, please go to the GSA Auctions homepage and click on register.",
-            "modified": "2022-02-02T17:44:18.543Z",
             "accessLevel": "public",
-            "identifier": "GSA-4145",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/auctions/auctions-data-dictionary.html",
-            "describedByType": "text/html",
-            "issued": "2010-11-23",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mike Wycoff",
                 "hasEmail": "mailto:michael.wyckoff@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/auctions/auctions-data-dictionary.html",
+            "describedByType": "text/html",
+            "description": "The General Services Administration (GSA) has a history of pioneering electronic solutions for streamlining and enhancing the management of excess and surplus Federal assets. GSA continued the transformation of the Federal disposal process throughout the late 1990s with the introduction and subsequent refinement of the Federal Disposal System, a centralized electronic clearinghouse for reporting and transferring excess/surplus personal property within the Federal community and among eligible donees.\n\nThe GSA Auctions website (www.gsaauctions.gov) has been developed to complete GSA's transformation to an all-electronic asset management system. The site offers the general public the opportunity to bid electronically on a wide array of Federal assets. The auctions are completely web-enabled, allowing all registered participants to bid on a single item or multiple items (lots) within specified timeframes.\n\nGSA Auctions offers Federal personal property assets ranging from commonplace items (such as office equipment and furniture) to more select products like scientific equipment, heavy machinery, airplanes, vessels, and vehicles. GSA Auctions online capabilities allow GSA to offer assets located across the country to any interested buyer, regardless of location.\n\nParticipants may choose to browse items that are offered on this site or may choose to search for items and place bids. In order to place a bid(s), participants must register first. To register, please go to the GSA Auctions homepage and click on register.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://gsaauctions.gov/gsaauctions/gsaauctions/",
+                    "description": "GSA Auctions offers Federal personal property assets ranging from commonplace items (such as office equipment and furniture) to more select products like scientific equipment, heavy machinery, airplanes, vessels, and vehicles. GSA Auctions online capabilities allow GSA to offer assets located across the country to any interested buyer, regardless of location.",
                     "format": "html",
-                    "title": "GSA Auctions",
-                    "description": "GSA Auctions offers Federal personal property assets ranging from commonplace items (such as office equipment and furniture) to more select products like scientific equipment, heavy machinery, airplanes, vessels, and vehicles. GSA Auctions online capabilities allow GSA to offer assets located across the country to any interested buyer, regardless of location."
+                    "title": "GSA Auctions"
                 }
             ],
+            "identifier": "GSA-4145",
+            "issued": "2010-11-23",
             "keyword": [
                 "Agricultural Equipment and Supplies",
                 "Aircraft and Aircraft Parts",
@@ -3224,36 +3218,35 @@
                 "furniture",
                 "real estate"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-02-02T17:44:18.543Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-us"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "DigitalGov Search API (formerly USASearch)",
-            "description": "Provides DigitalGov Search customers their search results in JSON. Sign in with a .gov or .mil email is required.",
-            "modified": "2014-05-29",
-            "accessLevel": "restricted public",
-            "identifier": "GSA - 138681",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "rights": "true",
+            "title": "GSA Auctions"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ammie Nicole Farraj-Feijoo",
                 "hasEmail": "mailto:ammie.farrajfeijoo@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Provides DigitalGov Search customers their search results in JSON. Sign in with a .gov or .mil email is required.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3262,56 +3255,56 @@
                     "title": "DigitalGov Search API (formerly USASearch)"
                 }
             ],
+            "identifier": "GSA - 138681",
             "keyword": [
                 "API",
                 "USASearch"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-05-29",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
             "theme": [
                 "API"
-            ]
+            ],
+            "title": "DigitalGov Search API (formerly USASearch)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "e-Buy Awards for Fiscal Year 2006",
-            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
-            "modified": "2016-01-21",
             "accessLevel": "public",
-            "identifier": "GSA-4095",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/eBuy_Awards_Data_Dictionary.html",
-            "issued": "2010-10-21",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-08-31",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Usha Gopal",
                 "hasEmail": "mailto:usha.gopal@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/eBuy_Awards_Data_Dictionary.html",
+            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/eBuy_Awards_FY2006.xls",
                     "format": "excel",
-                    "title": "e-Buy Awards for Fiscal Year 2006",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/eBuy_Awards_FY2006.xls"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "e-Buy Awards for Fiscal Year 2006"
                 }
             ],
+            "identifier": "GSA-4095",
+            "isPartOf": "GSA-2015-08-31",
+            "issued": "2010-10-21",
             "keyword": [
                 "Award",
                 "Contracts",
@@ -3321,50 +3314,50 @@
                 "Schedules",
                 "e-Buy"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-21",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "e-Buy Awards for Fiscal Year 2006"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Fleet Report",
-            "description": "Annual report of Federal agencies' motor vehicle fleet data collected in the Federal Automotive Statistical Tool (FAST), a web-based reporting tool cosponsored by GSA and the Department of Energy. The Federal Fleet Report is a year-end snapshot of motor vehicle fleet inventory, cost, and use data from agency data submissions, and the resulting data tables are available in these datasets.",
-            "modified": "2022-02-17T19:48:14.134Z",
             "accessLevel": "public",
-            "identifier": "GSA-4543",
-            "dataQuality": true,
-            "issued": "2011-01-31",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "US domestic, foreign, worldwide",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vehicle.policy@gsa.gov",
                 "hasEmail": "mailto:vehicle.policy@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Annual report of Federal agencies' motor vehicle fleet data collected in the Federal Automotive Statistical Tool (FAST), a web-based reporting tool cosponsored by GSA and the Department of Energy. The Federal Fleet Report is a year-end snapshot of motor vehicle fleet inventory, cost, and use data from agency data submissions, and the resulting data tables are available in these datasets.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "http://www.gsa.gov/portal/content/102943",
                     "format": "html",
-                    "title": "Federal Fleet Report",
-                    "downloadURL": "http://www.gsa.gov/portal/content/102943"
+                    "mediaType": "text/html",
+                    "title": "Federal Fleet Report"
                 }
             ],
+            "identifier": "GSA-4543",
+            "issued": "2011-01-31",
             "keyword": [
                 "FAST report",
                 "federal fleet",
@@ -3376,162 +3369,162 @@
                 "motor vehicle fleet",
                 "motor vehicles"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-02-17T19:48:14.134Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "US domestic, foreign, worldwide",
             "theme": [
                 "Travel and Transportation"
-            ]
+            ],
+            "title": "Federal Fleet Report"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2012, 4th Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
             "accessLevel": "public",
-            "identifier": "GSA-25061",
-            "dataQuality": true,
-            "describedBy": "http://www.gsa.gov/networx",
-            "issued": "2012-12-15",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.gsa.gov/networx",
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/TotRevFY12_4thQtr.xlsx",
                     "format": "xlsx",
-                    "title": "NetworxBusinessVolume_FY2012_4thQtr",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/TotRevFY12_4thQtr.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "NetworxBusinessVolume_FY2012_4thQtr"
                 }
             ],
+            "identifier": "GSA-25061",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2012-12-15",
             "keyword": [
                 "Networx",
                 "telecommunications."
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Real Estate"
-            ]
+            ],
+            "title": "Networx Business Volume FY2012, 4th Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2008 FY2009",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2016-02-19",
             "accessLevel": "public",
-            "identifier": "GSA-4109",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/networx/networx_revenue_data_dictionary.html",
-            "issued": "2010-10-21",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/networx/networx_revenue_data_dictionary.html",
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/networx/NetworxRevenue.xls",
                     "format": "xls",
-                    "title": "NetworxBusinessVolume_FY2008_FY2009",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/networx/NetworxRevenue.xls"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NetworxBusinessVolume_FY2008_FY2009"
                 }
             ],
+            "identifier": "GSA-4109",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2010-10-21",
             "keyword": [
                 "Networx Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-02-19",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Real Estate"
-            ]
+            ],
+            "title": "Networx Business Volume FY2008 FY2009"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "System for Award Management (SAM) Public Extract - Entity Registration",
-            "description": "This dataset contains the information available under the Freedom of Information Act (FOIA) for those entities registered to do business with the Federal government in the System for Award Management (SAM). It is updated monthly. Prior to July 2012, this dataset was called the Central Contractor Registration (CCR) FOIA Extract.",
-            "modified": "2018-12-18",
             "accessLevel": "public",
-            "identifier": "GSA-1422",
-            "dataQuality": true,
-            "describedBy": "https://www.sam.gov/SAM/transcript/SAM_Functional_Data_Dictionary.pdf",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "issued": "2010-01-14",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "Global",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Meredith M Whitehead",
                 "hasEmail": "mailto:meredith.whitehead@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.sam.gov/SAM/transcript/SAM_Functional_Data_Dictionary.pdf",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "This dataset contains the information available under the Freedom of Information Act (FOIA) for those entities registered to do business with the Federal government in the System for Award Management (SAM). It is updated monthly. Prior to July 2012, this dataset was called the Central Contractor Registration (CCR) FOIA Extract.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "title": "ASCII - System for Award Management (SAM) Public Extract",
-                    "description": "System implementing the functionalities of the legacy IAE applications; CCR, FedReg, ORCA, and EPLS.",
                     "describedBy": "https://sam.gov/sam/transcript/SAM%20Master%20Extract%20Mapping%20v5.1%20Public%20File%20Layout.xlsx",
                     "describedByType": "application/vnd.ms-excel",
-                    "downloadURL": "https://www.sam.gov/SAM/extractfiledownload?role=WW&version=SAM&filename=SAM_PUBLIC_MONTHLY_EXTRACT.ZIP"
+                    "description": "System implementing the functionalities of the legacy IAE applications; CCR, FedReg, ORCA, and EPLS.",
+                    "downloadURL": "https://www.sam.gov/SAM/extractfiledownload?role=WW&version=SAM&filename=SAM_PUBLIC_MONTHLY_EXTRACT.ZIP",
+                    "mediaType": "application/zip",
+                    "title": "ASCII - System for Award Management (SAM) Public Extract"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "title": "UTF-8 System for Award Managment (SAM) Public Extract",
-                    "description": "System implementing the functionalities of the legacy IAE applications: CCR, FedReg, ORCA, and EPLS.",
                     "describedBy": "https://sam.gov/sam/transcript/SAM%20Master%20Extract%20Mapping%20v5.1%20Public%20File%20Layout.xlsx",
                     "describedByType": "application/vnd.ms-excel",
-                    "downloadURL": "https://www.sam.gov/SAM/extractfiledownload?role=SAM-PUBLIC-UTF8&version=SAM&filename=SAM_PUBLIC_UTF-8_MONTHLY_EXTRACT.ZIP"
+                    "description": "System implementing the functionalities of the legacy IAE applications: CCR, FedReg, ORCA, and EPLS.",
+                    "downloadURL": "https://www.sam.gov/SAM/extractfiledownload?role=SAM-PUBLIC-UTF8&version=SAM&filename=SAM_PUBLIC_UTF-8_MONTHLY_EXTRACT.ZIP",
+                    "mediaType": "application/zip",
+                    "title": "UTF-8 System for Award Managment (SAM) Public Extract"
                 }
             ],
+            "identifier": "GSA-1422",
+            "issued": "2010-01-14",
             "keyword": [
                 "CCR",
                 "Contractor",
@@ -3544,87 +3537,87 @@
                 "System for Award Management",
                 "Vendor"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-12-18",
             "programCode": [
                 "023:015"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "Global",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "System for Award Management (SAM) Public Extract - Entity Registration"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Advisory Committee Act (FACA) Database-Complete-Raw",
-            "description": "The Federal Advisory Committee Act (FACA) database is used by Federal agencies to continuously manage an average of 1,000 advisory committees government-wide. This database is also used by the Congress to perform oversight of related Executive Branch programs and by the public, the media, and others, to stay abreast of important developments resulting from advisory committee activities.  Although centrally supported by the General Services Administration's (GSA) Committee Management Secretariat, the database represents a true shared system wherein each participating agency and individual committee manager has responsibility for providing accurate and timely information that may be used to assure that the system's wide array of users has access to data required by FACA.",
-            "modified": "2016-05-10",
             "accessLevel": "public",
-            "identifier": "GSA-2015-08-26-01",
-            "dataQuality": false,
-            "describedBy": "http://www.fido.gov/facadatabase/help.asp",
-            "issued": "2015-08-26",
-            "landingPage": "http://www.facadatabase.gov/",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lorelei Kowalski",
                 "hasEmail": "mailto:lorelei.kowalski@gsa.gov"
             },
+            "dataQuality": false,
+            "describedBy": "http://www.fido.gov/facadatabase/help.asp",
+            "description": "The Federal Advisory Committee Act (FACA) database is used by Federal agencies to continuously manage an average of 1,000 advisory committees government-wide. This database is also used by the Congress to perform oversight of related Executive Branch programs and by the public, the media, and others, to stay abreast of important developments resulting from advisory committee activities.  Although centrally supported by the General Services Administration's (GSA) Committee Management Secretariat, the database represents a true shared system wherein each participating agency and individual committee manager has responsibility for providing accurate and timely information that may be used to assure that the system's wide array of users has access to data required by FACA.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://www.facadatabase.gov/",
+                    "describedBy": "http://www.fido.gov/facadatabase/help.asp",
                     "format": "text/html",
-                    "title": "Federal Advisory Committee Act (FACA) Database-Complete-Raw",
-                    "describedBy": "http://www.fido.gov/facadatabase/help.asp"
+                    "title": "Federal Advisory Committee Act (FACA) Database-Complete-Raw"
                 }
             ],
+            "identifier": "GSA-2015-08-26-01",
+            "issued": "2015-08-26",
             "keyword": [
                 "Executive Branch"
             ],
-            "bureauCode": [
-                "023:00"
+            "landingPage": "http://www.facadatabase.gov/",
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-05-10",
             "programCode": [
                 "023:015"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "spatial": "National",
             "theme": [
                 "Advisory Committee"
-            ]
+            ],
+            "title": "Federal Advisory Committee Act (FACA) Database-Complete-Raw"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA JSON",
-            "description": "The General Service Administration's data.json harvest source. This file contains the metadata for the GSA's public data listing shown on data.gov as defined by the Project Open Data",
-            "modified": "2024-11-05T16:23:42.111Z",
             "accessLevel": "public",
-            "identifier": "GSA - 139225",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Cindy Smith",
                 "hasEmail": "mailto:cindya.smith@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The General Service Administration's data.json harvest source. This file contains the metadata for the GSA's public data listing shown on data.gov as defined by the Project Open Data",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3632,6 +3625,7 @@
                     "title": "GSA JSON"
                 }
             ],
+            "identifier": "GSA - 139225",
             "keyword": [
                 "GSA",
                 "General Services Administration",
@@ -3640,110 +3634,109 @@
                 "Project Open Data",
                 "Public Data Listing"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-us"
             ],
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-05T16:23:42.111Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Other"
-            ]
+            ],
+            "title": "GSA JSON"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Interactive Financial Charts- Agency Financial Reports",
-            "description": "For a visual depiction of GSA's Balance Sheet and Statement of Net Cost, please use the interactive charts to view the financial results for fiscal years 2007-2013.",
-            "modified": "2013-12-31",
             "accessLevel": "public",
-            "identifier": "GSA - 3374",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vivi D Tran-Chu",
                 "hasEmail": "mailto:vivi.tran@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "For a visual depiction of GSA's Balance Sheet and Statement of Net Cost, please use the interactive charts to view the financial results for fiscal years 2007-2013.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "http://www.gsa.gov/portal/content/182763",
                     "format": "html",
-                    "title": "Interactive Financial Charts- Agency Financial Reports",
-                    "downloadURL": "http://www.gsa.gov/portal/content/182763"
+                    "mediaType": "text/html",
+                    "title": "Interactive Financial Charts- Agency Financial Reports"
                 }
             ],
+            "identifier": "GSA - 3374",
             "keyword": [
                 "AFR",
                 "Agency Financial Report AFR",
                 "Financial",
                 "Savings"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2013-12-31",
             "programCode": [
                 "023:016"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Other"
-            ]
+            ],
+            "title": "Interactive Financial Charts- Agency Financial Reports"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Inventory of Owned and Leased Properties (IOLP)",
-            "description": "The Inventory of Owned and Leased Properties (IOLP) allows users to search properties owned and leased by the General Services Administration (GSA) across the United States, Puerto Rico, Guam and American Samoa.\n\nThe Owned and Leased Data Sets include the following data except where noted below for Leases:\n\n- Location Code - GSA\u2019s alphanumeric identifier for the building\n- Real Property Asset Name - Allows users to find information about a specific building \n- Installation Name - Allows users to identify whether a property is part of an installation, such as a campus\n- Owned or Leased - Indicates the building is federally owned (F) or leased (L)\n- GSA Region - GSA assigned region for building location\n- Street Address/City/State/Zip Code - Building address\n- Longitude and Latitude - Map coordinates of the building (only through .csv export)\n- Rentable Square Feet - Total rentable square feet in building\n- Available Square Feet - Vacant space in building\n- Construction Date (Owned Only) - Year built\n- Congressional District - Congressional District building is located\n- Senator/Representative/URL - Senator/Representative of the Congressional District and their URL\n- Building Status (Owned Only) - Indicates building is active\n- Lease Number (Leased Only) - GSA\u2019s alphanumeric identifier for the lease\n- Lease Effective/Expiration Dates (Leased Only) - Date lease starts/expires\n- Real Property Asset Type - Identifies a property as land, building, or structure",
-            "modified": "2024-03-08T20:17:22.730Z",
             "accessLevel": "public",
-            "identifier": "GSA-4495",
-            "dataQuality": true,
-            "issued": "2002-01-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1W",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Valerie R Butler",
                 "hasEmail": "mailto:valerie.butler@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The Inventory of Owned and Leased Properties (IOLP) allows users to search properties owned and leased by the General Services Administration (GSA) across the United States, Puerto Rico, Guam and American Samoa.\n\nThe Owned and Leased Data Sets include the following data except where noted below for Leases:\n\n- Location Code - GSA\u2019s alphanumeric identifier for the building\n- Real Property Asset Name - Allows users to find information about a specific building \n- Installation Name - Allows users to identify whether a property is part of an installation, such as a campus\n- Owned or Leased - Indicates the building is federally owned (F) or leased (L)\n- GSA Region - GSA assigned region for building location\n- Street Address/City/State/Zip Code - Building address\n- Longitude and Latitude - Map coordinates of the building (only through .csv export)\n- Rentable Square Feet - Total rentable square feet in building\n- Available Square Feet - Vacant space in building\n- Construction Date (Owned Only) - Year built\n- Congressional District - Congressional District building is located\n- Senator/Representative/URL - Senator/Representative of the Congressional District and their URL\n- Building Status (Owned Only) - Indicates building is active\n- Lease Number (Leased Only) - GSA\u2019s alphanumeric identifier for the lease\n- Lease Effective/Expiration Dates (Leased Only) - Date lease starts/expires\n- Real Property Asset Type - Identifies a property as land, building, or structure",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/plain",
-                    "title": "IOLP19139_050324.txt",
                     "conformsTo": "http://www.isotc211.org/2005/gmd",
-                    "downloadURL": "https://inventory.data.gov/dataset/9a9e946e-124e-46f5-a934-e458a6c1c2b2/resource/699145f9-9bcd-4e8e-99a8-55b535fee6ae/download/iolp19139_050324.txt"
+                    "downloadURL": "https://inventory.data.gov/dataset/9a9e946e-124e-46f5-a934-e458a6c1c2b2/resource/699145f9-9bcd-4e8e-99a8-55b535fee6ae/download/iolp19139_050324.txt",
+                    "mediaType": "text/plain",
+                    "title": "IOLP19139_050324.txt"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/9a9e946e-124e-46f5-a934-e458a6c1c2b2/resource/f5d0cf4e-fdd9-45cf-9987-9f1122ff45e2/download/2025-1-31-iolp-leases.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "2025 - 1 - 31 - IOLP Leases.xlsx",
-                    "downloadURL": "https://inventory.data.gov/dataset/9a9e946e-124e-46f5-a934-e458a6c1c2b2/resource/f5d0cf4e-fdd9-45cf-9987-9f1122ff45e2/download/2025-1-31-iolp-leases.xlsx"
+                    "title": "2025 - 1 - 31 - IOLP Leases.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/9a9e946e-124e-46f5-a934-e458a6c1c2b2/resource/e9a02783-3127-4162-bdd9-c7c79140e52a/download/2025-1-31-iolp-buildings.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "2025 - 1 - 31 - IOLP Buildings.xlsx",
-                    "downloadURL": "https://inventory.data.gov/dataset/9a9e946e-124e-46f5-a934-e458a6c1c2b2/resource/e9a02783-3127-4162-bdd9-c7c79140e52a/download/2025-1-31-iolp-buildings.xlsx"
+                    "title": "2025 - 1 - 31 - IOLP Buildings.xlsx"
                 }
             ],
+            "identifier": "GSA-4495",
+            "issued": "2002-01-01",
             "keyword": [
                 "BUILDING_STATUS",
                 "City",
@@ -3757,39 +3750,39 @@
                 "Zipcode5",
                 "geospatial"
             ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
-            ],
             "language": [
                 "en-us"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "List of Government APIs",
-            "description": "A list of individual public APIs maintained by the US government.",
-            "modified": "2016-03-04",
-            "accessLevel": "public",
-            "identifier": "GSA - 139011",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
+            "modified": "2024-03-08T20:17:22.730Z",
+            "programCode": [
+                "015:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "rights": "true",
+            "spatial": "United States",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Inventory of Owned and Leased Properties (IOLP)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Richard G Brooks",
                 "hasEmail": "mailto:richard.g.brooks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "A list of individual public APIs maintained by the US government.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3798,57 +3791,57 @@
                     "title": "List of Government APIs"
                 }
             ],
+            "identifier": "GSA - 139011",
             "keyword": [
                 "API",
                 "developers",
                 "government",
                 "web service"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-03-04",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "API"
-            ]
+            ],
+            "title": "List of Government APIs"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Natural Gas Acquisition Program",
-            "description": "The \"NGAP\" system is a web based application which serves NGAP GSA users for tracking information details for various natural gas supply chain elements like Agency, LDC, and Facility with their respective Point of Contacts information. In addition to this, it also maintains the Cost & Usage Data and Invoices for the Facilities under different account managers.",
-            "modified": "2019-07-25",
             "accessLevel": "public",
-            "identifier": "GSA-4308",
-            "dataQuality": true,
-            "issued": "2010-11-16",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "023:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Shirl R Tillman",
                 "hasEmail": "mailto:shirl.tillman@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The \"NGAP\" system is a web based application which serves NGAP GSA users for tracking information details for various natural gas supply chain elements like Agency, LDC, and Facility with their respective Point of Contacts information. In addition to this, it also maintains the Cost & Usage Data and Invoices for the Facilities under different account managers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "Natural Gas Acquisition Program",
                     "description": "NGAP 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/3fbe4fc6-95fc-4ee4-bda7-06f985ae8276/resource/1866644f-22ca-4b4c-8e71-40983e91e2c8/download/data.govngap2019.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/3fbe4fc6-95fc-4ee4-bda7-06f985ae8276/resource/1866644f-22ca-4b4c-8e71-40983e91e2c8/download/data.govngap2019.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Natural Gas Acquisition Program"
                 }
             ],
+            "identifier": "GSA-4308",
+            "issued": "2010-11-16",
             "keyword": [
                 "Agency",
                 "Cost",
@@ -3858,140 +3851,140 @@
                 "Usage Data.",
                 "Utilities"
             ],
-            "bureauCode": [
-                "023:05"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-07-25",
             "programCode": [
                 "023:004"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "Natural Gas Acquisition Program"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2013, 1st Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
             "accessLevel": "public",
-            "identifier": "GSA-25071",
-            "dataQuality": true,
-            "describedBy": "http://www.gsa.gov/networx",
-            "issued": "2013-03-15",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.gsa.gov/networx",
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "http://www.asap.gsa.gov/datagov/TotRevFY13_1stQtr.xlsx",
                     "format": "xlsx",
-                    "title": "NetworxBusinessVolume_FY2013_1stQtr",
-                    "downloadURL": "http://www.asap.gsa.gov/datagov/TotRevFY13_1stQtr.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "NetworxBusinessVolume_FY2013_1stQtr"
                 }
             ],
+            "identifier": "GSA-25071",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2013-03-15",
             "keyword": [
                 "Networx",
                 "telecommunications."
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "United States",
             "theme": [
                 "Real Estate"
-            ]
+            ],
+            "title": "Networx Business Volume FY2013, 1st Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Concur - Reporting Travel Model",
-            "description": "The data dictionary for the reporting travel model  within Concur.",
-            "modified": "2016-01-20",
             "accessLevel": "non-public",
-            "identifier": "GSA - 139046",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-09-11-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Norma H Tolson",
                 "hasEmail": "mailto:norma.tolson@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The data dictionary for the reporting travel model  within Concur.",
+            "identifier": "GSA - 139046",
+            "isPartOf": "GSA-2015-09-11-01",
             "keyword": [
                 "Credit Card",
                 "travel card"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-01-20",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
             "theme": [
                 "Travel and Transportation"
-            ]
+            ],
+            "title": "Concur - Reporting Travel Model"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "e-Buy Awards for Fiscal Year 2005",
-            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
-            "modified": "2016-01-21",
             "accessLevel": "public",
-            "identifier": "GSA-4008",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/eBuy_Awards_Data_Dictionary.html",
-            "issued": "2010-09-27",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-08-31",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Usha Gopal",
                 "hasEmail": "mailto:usha.gopal@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/eBuy_Awards_Data_Dictionary.html",
+            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/eBuy_Awards_FY2005.xls",
                     "format": "excel",
-                    "title": "e-Buy Awards for Fiscal Year 2005",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/eBuy_Awards_FY2005.xls"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "e-Buy Awards for Fiscal Year 2005"
                 }
             ],
+            "identifier": "GSA-4008",
+            "isPartOf": "GSA-2015-08-31",
+            "issued": "2010-09-27",
             "keyword": [
                 "Award",
                 "Contracts",
@@ -4000,52 +3993,52 @@
                 "Schedules",
                 "e-Buy"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-21",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "e-Buy Awards for Fiscal Year 2005"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "e-Buy Awards for Fiscal Year 2009",
-            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
-            "modified": "2016-01-21",
             "accessLevel": "public",
-            "identifier": "GSA-4427",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/eBuy_Awards_Data_Dictionary.html",
-            "issued": "2011-02-04",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-08-31",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Usha Gopal",
                 "hasEmail": "mailto:usha.gopal@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/eBuy_Awards_Data_Dictionary.html",
+            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/eBuy_Awards_FY2009.xls",
                     "format": "excel",
-                    "title": "e-Buy Awards for Fiscal Year 2009",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/eBuy_Awards_FY2009.xls"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "e-Buy Awards for Fiscal Year 2009"
                 }
             ],
+            "identifier": "GSA-4427",
+            "isPartOf": "GSA-2015-08-31",
+            "issued": "2011-02-04",
             "keyword": [
                 "Award",
                 "Contracts",
@@ -4055,51 +4048,51 @@
                 "Schedules",
                 "e-Buy"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-21",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "N/A",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "e-Buy Awards for Fiscal Year 2009"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "E-Gov Travel (ETS) Measures",
-            "description": "The Number of Vouchers Processed measure represents the number of vouchers processed by the three ETS vendors Annual for the 24 largest Federal Civilian Agencies.  The % of Reservations Completed Online measure represents the percentage of reservations that are processed online versus manually by a travel agent.",
-            "modified": "2011-06-22",
             "accessLevel": "public",
-            "identifier": "GSA-4918",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/etravel/etravel_voucher_data_dictionary.html",
-            "issued": "2011-06-22",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jonathan Anderson",
                 "hasEmail": "mailto:jonathan.anderson@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/etravel/etravel_voucher_data_dictionary.html",
+            "description": "The Number of Vouchers Processed measure represents the number of vouchers processed by the three ETS vendors Annual for the 24 largest Federal Civilian Agencies.  The % of Reservations Completed Online measure represents the percentage of reservations that are processed online versus manually by a travel agent.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/etravel/etravel_data_2010.xls",
                     "format": "xls",
-                    "title": "E-Gov Travel (ETS) Measures",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/etravel/etravel_data_2010.xls"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "E-Gov Travel (ETS) Measures"
                 }
             ],
+            "identifier": "GSA-4918",
+            "issued": "2011-06-22",
             "keyword": [
                 "Balanced Scorecard Perspectives",
                 "Customer",
@@ -4108,98 +4101,98 @@
                 "stakeholder",
                 "travel"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2011-06-22",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "N/A",
             "theme": [
                 "Travel and Transportation"
-            ]
+            ],
+            "title": "E-Gov Travel (ETS) Measures"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Acquisition Service Instructional Letter 2013",
-            "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts. All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
-            "modified": "2020-12-22",
             "accessLevel": "public",
-            "identifier": "GSA - 139296",
-            "dataQuality": true,
-            "issued": "2014-07-22",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-09-14-02",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David W Orcutt",
                 "hasEmail": "mailto:david.orcutt@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts. All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "FAS IL Table of Contents 2013",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/81cd1b12-0cfc-4dbf-8e42-236194d9f608/resource/2d177970-f1a0-4d89-be33-0d8017ce411f/download/table-of-contents-federal-acquisition-service-instructional-letters-2013.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/81cd1b12-0cfc-4dbf-8e42-236194d9f608/resource/2d177970-f1a0-4d89-be33-0d8017ce411f/download/table-of-contents-federal-acquisition-service-instructional-letters-2013.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FAS IL Table of Contents 2013"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2013-01",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/81cd1b12-0cfc-4dbf-8e42-236194d9f608/resource/5c9db53e-cf36-48a5-aa07-37107e287d8e/download/instruction-letter-il-2013-01.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/81cd1b12-0cfc-4dbf-8e42-236194d9f608/resource/5c9db53e-cf36-48a5-aa07-37107e287d8e/download/instruction-letter-il-2013-01.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2013-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://inventory.data.gov/dataset/81cd1b12-0cfc-4dbf-8e42-236194d9f608/resource/13d1e6d1-fc3d-4962-ae3c-d63717a914a9/download/instruction-letter-il-2013-02.pdf",
+                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
                     "format": "pdf",
-                    "title": "FAS IL 2013-02",
-                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts."
+                    "title": "FAS IL 2013-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://inventory.data.gov/dataset/81cd1b12-0cfc-4dbf-8e42-236194d9f608/resource/5fef5fc6-c906-4173-9bfa-32ca1061a4c4/download/instruction-letter-il-2013-03.pdf",
+                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
                     "format": "pdf",
-                    "title": "FAS IL 2013-03",
-                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts."
+                    "title": "FAS IL 2013-03"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2013-04",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/81cd1b12-0cfc-4dbf-8e42-236194d9f608/resource/00eee92f-8ebe-41c3-98dc-b16a3e3c163a/download/instruction-letter-il-2013-04.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/81cd1b12-0cfc-4dbf-8e42-236194d9f608/resource/00eee92f-8ebe-41c3-98dc-b16a3e3c163a/download/instruction-letter-il-2013-04.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2013-04"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2013-05",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/81cd1b12-0cfc-4dbf-8e42-236194d9f608/resource/2afe451b-8b64-4bc6-8278-960b46b2b05e/download/instruction-letter-il-2013-05.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/81cd1b12-0cfc-4dbf-8e42-236194d9f608/resource/2afe451b-8b64-4bc6-8278-960b46b2b05e/download/instruction-letter-il-2013-05.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2013-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2013-06",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/81cd1b12-0cfc-4dbf-8e42-236194d9f608/resource/aa5e1cdd-c0d9-4789-8959-ba1fec4494d9/download/instructional-letter-il-2013-06.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/81cd1b12-0cfc-4dbf-8e42-236194d9f608/resource/aa5e1cdd-c0d9-4789-8959-ba1fec4494d9/download/instructional-letter-il-2013-06.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2013-06"
                 }
             ],
+            "identifier": "GSA - 139296",
+            "isPartOf": "GSA-2015-09-14-02",
+            "issued": "2014-07-22",
             "keyword": [
                 "FAS",
                 "GSA",
@@ -4207,51 +4200,51 @@
                 "Instructional Letters",
                 "Interactive"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-22",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "United States",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "Federal Acquisition Service Instructional Letter 2013"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Mail Expenditures",
-            "description": "Agencies annually report mail data using the Simplified Mail Accountability Reporting Tool (SMART), a web-based reporting tool cosponsored by GSA and the Department of Energy.  The Annual Mail Management Report publishes mail cost, professional certifications and the resulting data tables are available in these datasets.",
-            "modified": "2016-05-10",
             "accessLevel": "public",
-            "identifier": "GSA-6386",
-            "dataQuality": true,
-            "describedBy": "http://www.gsa.gov/mailpolicy",
-            "issued": "2011-01-01",
-            "license": "https://gsa.inl.gov/smart/",
-            "rights": "N/A",
-            "spatial": "28 Federal Agencies that spend a million dollars or more on mail",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lois Mandell",
                 "hasEmail": "mailto:lois.mandell@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.gsa.gov/mailpolicy",
+            "description": "Agencies annually report mail data using the Simplified Mail Accountability Reporting Tool (SMART), a web-based reporting tool cosponsored by GSA and the Department of Energy.  The Annual Mail Management Report publishes mail cost, professional certifications and the resulting data tables are available in these datasets.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "http://www.gsa.gov/portal/content/235245",
                     "format": "html",
-                    "title": "Federal Mail Expenditures",
-                    "downloadURL": "http://www.gsa.gov/portal/content/235245"
+                    "mediaType": "text/html",
+                    "title": "Federal Mail Expenditures"
                 }
             ],
+            "identifier": "GSA-6386",
+            "issued": "2011-01-01",
             "keyword": [
                 "Federal Mail",
                 "Federal Mail Expenditures",
@@ -4259,98 +4252,98 @@
                 "Federal Mail Pieces",
                 "Federal Mail Policy"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://gsa.inl.gov/smart/",
+            "modified": "2016-05-10",
             "programCode": [
                 "023:009"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "28 Federal Agencies that spend a million dollars or more on mail",
             "theme": [
                 "Other"
-            ]
+            ],
+            "title": "Federal Mail Expenditures"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA eLibrary Schedules and Contracts",
-            "description": "GSA eLibrary (formerly Schedules e-Library) is the online source for the latest contract award information for: GSA Schedules; Department of Veterans Affairs (VA) Schedules; and Technology Contracts, including Governmentwide Acquisition Contracts (GWACs), Network Services and Telecommunications Contracts, and Information Technology (IT) Schedule 70. This data contains all the current contracts under those contract vehicles and their respective schedule, special item number information.",
-            "modified": "2019-02-06",
             "accessLevel": "public",
-            "identifier": "GSA-4001",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/elibrary_schedule_contracts_data_dictionary.html",
-            "issued": "2010-09-17",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Usha Gopal",
                 "hasEmail": "mailto:usha.gopal@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/elibrary_schedule_contracts_data_dictionary.html",
+            "description": "GSA eLibrary (formerly Schedules e-Library) is the online source for the latest contract award information for: GSA Schedules; Department of Veterans Affairs (VA) Schedules; and Technology Contracts, including Governmentwide Acquisition Contracts (GWACs), Network Services and Telecommunications Contracts, and Information Technology (IT) Schedule 70. This data contains all the current contracts under those contract vehicles and their respective schedule, special item number information.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "eLibrary Schedule Contracts",
                     "description": "elibraryschedulecontracts20210505.xlsx",
-                    "downloadURL": "https://inventory.data.gov/dataset/4fd4a79f-7fd6-4699-a77a-411bc7e980b9/resource/f44444af-850a-4f21-ae05-48953ccee0f3/download/elibraryschedulecontracts20210505.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/4fd4a79f-7fd6-4699-a77a-411bc7e980b9/resource/f44444af-850a-4f21-ae05-48953ccee0f3/download/elibraryschedulecontracts20210505.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "eLibrary Schedule Contracts"
                 }
             ],
+            "identifier": "GSA-4001",
+            "issued": "2010-09-17",
             "keyword": [
                 "eLibrary GSA Schedule Contract"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-02-06",
             "programCode": [
                 "023:012"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "GSA eLibrary Schedules and Contracts"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "National Stock Number Extract",
-            "description": "National Stock Number extract includes the current listing of National Stock Numbers (NSNs) , NSN item name and descriptions, and current selling price of each product listed in GSA Advantage and managed by GSA.  Each NSN is listed with the vendors description of the item. Some descriptions exceed the standard length and are truncated.",
-            "modified": "2017-05-17",
             "accessLevel": "public",
-            "identifier": "GSA-2084",
-            "dataQuality": true,
-            "issued": "2010-03-22",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Frank Fornaris",
                 "hasEmail": "mailto:frank.fornaris@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "National Stock Number extract includes the current listing of National Stock Numbers (NSNs) , NSN item name and descriptions, and current selling price of each product listed in GSA Advantage and managed by GSA.  Each NSN is listed with the vendors description of the item. Some descriptions exceed the standard length and are truncated.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/67567804-073d-40ad-a710-2b0bed8b84e2/resource/3b7ed6b7-7dce-42f1-852d-6465e3e790e4/download/nsn-extract-2-21-23.xls.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "NSN extract 2-21-23.xls.xlsx",
-                    "downloadURL": "https://inventory.data.gov/dataset/67567804-073d-40ad-a710-2b0bed8b84e2/resource/3b7ed6b7-7dce-42f1-852d-6465e3e790e4/download/nsn-extract-2-21-23.xls.xlsx"
+                    "title": "NSN extract 2-21-23.xls.xlsx"
                 }
             ],
+            "identifier": "GSA-2084",
+            "issued": "2010-03-22",
             "keyword": [
                 "NSN",
                 "National Stock Number",
@@ -4358,187 +4351,186 @@
                 "Product",
                 "Vendor"
             ],
-            "bureauCode": [
-                "023:10"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2017-05-17",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Other"
-            ]
+            ],
+            "title": "National Stock Number Extract"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2013, 2nd Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
             "accessLevel": "public",
-            "identifier": "GSA-30771",
-            "dataQuality": true,
-            "describedBy": "http://www.gsa.gov/networx",
-            "issued": "2013-05-30",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.gsa.gov/networx",
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/TotRevFY13_2ndQtr.xlsx",
                     "format": "xlsx",
-                    "title": "NetworxBusinessVolume_FY2013_2ndQtr",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/TotRevFY13_2ndQtr.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "NetworxBusinessVolume_FY2013_2ndQtr"
                 }
             ],
+            "identifier": "GSA-30771",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2013-05-30",
             "keyword": [
                 "Networx",
                 "telecommunications."
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Real Estate"
-            ]
+            ],
+            "title": "Networx Business Volume FY2013, 2nd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions July-Sept 2015, 4th Qtr",
-            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA - 138791",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://inventory.data.gov/dataset/fb8096f8-b8a7-4391-beb9-b18907f6a8ed/resource/ba8c523e-cdd8-4245-aed9-ad49ed245da3/download/julysept-2015-gsa-pc-transactions.xlsx",
                     "format": "xlsx",
-                    "title": "July September 2015 PC Transactions",
-                    "downloadURL": "https://inventory.data.gov/dataset/fb8096f8-b8a7-4391-beb9-b18907f6a8ed/resource/ba8c523e-cdd8-4245-aed9-ad49ed245da3/download/julysept-2015-gsa-pc-transactions.xlsx"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "July September 2015 PC Transactions"
                 }
             ],
+            "identifier": "GSA - 138791",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "p-card",
                 "purchase card",
                 "purchase card transactions",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions July-Sept 2015, 4th Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "RWA Entry & Tracking Application (RETA)",
-            "description": "The Reimbursable Work Authorization (RWA) Entry & Tracking Application (RETA) is a web based system that serves the Public Buildings Service as a centralized repository for Reimbursable Work Authorization information.  It is a national PBS RWA database warehouse with electronic interface capabilities into the NEAR RWA Database System.",
-            "modified": "2023-11-27T19:54:14.144Z",
             "accessLevel": "public",
-            "identifier": "GSA-5008",
-            "dataQuality": true,
-            "describedBy": "http://www.gsa.gov/dg/RETA_Datadictionary.docx",
-            "issued": "2011-04-21",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "Contiguous United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rachel Bichsel",
                 "hasEmail": "mailto:rachel.bichsel@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.gsa.gov/dg/RETA_Datadictionary.docx",
+            "description": "The Reimbursable Work Authorization (RWA) Entry & Tracking Application (RETA) is a web based system that serves the Public Buildings Service as a centralized repository for Reimbursable Work Authorization information.  It is a national PBS RWA database warehouse with electronic interface capabilities into the NEAR RWA Database System.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://www.gsa.gov/rwa"
                 }
             ],
+            "identifier": "GSA-5008",
+            "issued": "2011-04-21",
             "keyword": [
                 "Building",
                 "Construction",
                 "Historic",
                 "Space"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-11-27T19:54:14.144Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "Contiguous United States",
             "theme": [
                 "Real Estate"
-            ]
+            ],
+            "title": "RWA Entry & Tracking Application (RETA)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "eMuseum API",
-            "description": "This API delivers search information and images from The Museum System (TMS) & eMuseum to GSA.gov.\r\n\r\nThis dataset replaces the dataset titled Fine Arts Database (FAD).",
-            "modified": "2018-10-03",
             "accessLevel": "public",
-            "identifier": "GSA-2015-05-18-3",
-            "dataQuality": true,
-            "issued": "2015-02-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "023:30"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mary Margaret M Carr",
                 "hasEmail": "mailto:mary.carr@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "This API delivers search information and images from The Museum System (TMS) & eMuseum to GSA.gov.\r\n\r\nThis dataset replaces the dataset titled Fine Arts Database (FAD).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4547,48 +4539,49 @@
                     "title": "eMuseum API"
                 }
             ],
+            "identifier": "GSA-2015-05-18-3",
+            "issued": "2015-02-01",
             "keyword": [
                 "API",
                 "Fine Arts",
                 "TMS",
                 "eMuseum"
             ],
-            "bureauCode": [
-                "023:30"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-10-03",
             "programCode": [
                 "023:017"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Real Estate"
-            ]
+            ],
+            "title": "eMuseum API"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Capital Projects Application (CPA)",
-            "description": "Capital Projects application (CPA) provides users with the ability to maintain project related financial data for Budget Activity (BA) 51, 55, 64, 01, 02, 03, 04.  CPA maintains extensive project related data for single year and multiple year funded projects for these budget activities.  CPA maintains transaction details of the amount appropriated and obligated over the course of the project at the project level.  The information contained in CPA is used daily by field personnel and serves as the system of record when responding to Office of management and Budget (OMB) and Congress.  CPA interfaces with Business Information System (BIS) and performs daily downloads of obligation data for BA51, BA55, BA64, BA01, BA02, BA03, BA04, segmented by budget activity, region, and project status and type.  Accessible through the PBS Portal CPA data elements include Region, Projects Number, Project Name/Location, Status, Project Manager, Balance Amounts, and Authorization/Schedules for single and multiple year funds projects.",
-            "modified": "2015-09-10",
             "accessLevel": "non-public",
-            "identifier": "GSA-4722",
-            "dataQuality": true,
-            "describedBy": "http://www.gsa.gov/dg/CPA_DataDictionary.docx",
-            "issued": "2011-03-24",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "023:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Justin M Pinkney",
                 "hasEmail": "mailto:justin.pinkney@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.gsa.gov/dg/CPA_DataDictionary.docx",
+            "description": "Capital Projects application (CPA) provides users with the ability to maintain project related financial data for Budget Activity (BA) 51, 55, 64, 01, 02, 03, 04.  CPA maintains extensive project related data for single year and multiple year funded projects for these budget activities.  CPA maintains transaction details of the amount appropriated and obligated over the course of the project at the project level.  The information contained in CPA is used daily by field personnel and serves as the system of record when responding to Office of management and Budget (OMB) and Congress.  CPA interfaces with Business Information System (BIS) and performs daily downloads of obligation data for BA51, BA55, BA64, BA01, BA02, BA03, BA04, segmented by budget activity, region, and project status and type.  Accessible through the PBS Portal CPA data elements include Region, Projects Number, Project Name/Location, Status, Project Manager, Balance Amounts, and Authorization/Schedules for single and multiple year funds projects.",
+            "identifier": "GSA-4722",
+            "issued": "2011-03-24",
             "keyword": [
                 "Activity",
                 "Alterations",
@@ -4599,50 +4592,50 @@
                 "Repairs",
                 "Reporting"
             ],
-            "bureauCode": [
-                "023:05"
+            "language": [
+                "en-us"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-09-10",
             "programCode": [
                 "023:014"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
+            "spatial": "United States",
             "theme": [
                 "Real Estate"
-            ]
+            ],
+            "title": "Capital Projects Application (CPA)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Assistance Listings at beta.SAM.gov (formerly CFDA)",
-            "description": "The federal government provides assistance to the American public in the form of projects, services, and activities.  It supports a broad range of programs such as education, health care, research, infrastructure, economic development and other programs through grants, loans, scholarships, insurance, and other types of financial assistance.\r\n\r\nAssistance Listings at beta.SAM.gov provides detailed, public descriptions of federal assistance listings available to State and Local governments (including the District of Columbia); federally recognized Indian tribal governments, Territories (and possessions) of the United States; domestic public, quasi- public, and private profit and nonprofit organizations and institutions; specialized groups, and individuals.",
-            "modified": "2010-07-16",
             "accessLevel": "public",
-            "identifier": "GSA-1423",
-            "dataQuality": true,
-            "describedBy": "http://www.cfda.gov",
-            "issued": "2010-01-14",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Stephenson",
                 "hasEmail": "mailto:michael.stephenson@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.cfda.gov",
+            "description": "The federal government provides assistance to the American public in the form of projects, services, and activities.  It supports a broad range of programs such as education, health care, research, infrastructure, economic development and other programs through grants, loans, scholarships, insurance, and other types of financial assistance.\r\n\r\nAssistance Listings at beta.SAM.gov provides detailed, public descriptions of federal assistance listings available to State and Local governments (including the District of Columbia); federally recognized Indian tribal governments, Territories (and possessions) of the United States; domestic public, quasi- public, and private profit and nonprofit organizations and institutions; specialized groups, and individuals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://s3.amazonaws.com/falextracts/Assistance%20Listings/datagov/AssistanceListings_DataGov_PUBLIC_CURRENT.csv",
+                    "description": "The Federal Government provides assistance to the American Public in the form of projects, services, and activities.",
                     "format": "bin",
-                    "title": "Assistance Listings in beta.SAM.gov (formerly CFDA)",
-                    "description": "The Federal Government provides assistance to the American Public in the form of projects, services, and activities."
+                    "title": "Assistance Listings in beta.SAM.gov (formerly CFDA)"
                 }
             ],
+            "identifier": "GSA-1423",
+            "issued": "2010-01-14",
             "keyword": [
                 "Assistance Listings",
                 "CFDA",
@@ -4663,361 +4656,361 @@
                 "Services",
                 "State Government"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2010-07-16",
             "programCode": [
                 "023:016"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Other"
-            ]
+            ],
+            "title": "Assistance Listings at beta.SAM.gov (formerly CFDA)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Concur - Reporting Voucher Model",
-            "description": "The data dictionary for the reporting voucher model within Concur.",
-            "modified": "2016-02-23",
             "accessLevel": "non-public",
-            "identifier": "GSA - 139048",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-09-11-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Norma H Tolson",
                 "hasEmail": "mailto:norma.tolson@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The data dictionary for the reporting voucher model within Concur.",
+            "identifier": "GSA - 139048",
+            "isPartOf": "GSA-2015-09-11-01",
             "keyword": [
                 "Credit Card",
                 "Travel Card"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-02-23",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
             "theme": [
                 "Travel and Transportation"
-            ]
+            ],
+            "title": "Concur - Reporting Voucher Model"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "FAS Instructional Letters 2007-01 Procedures for Financial Responsibility",
-            "description": "This IL sets forth procedures for financial responsibility. The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts. All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
-            "modified": "2017-05-08",
             "accessLevel": "public",
-            "identifier": "GSA-5180",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/fas-il/IL_2007_2008.html",
-            "issued": "2011-07-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "GSA-2015-09-14-02",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Robert D Bourne",
                 "hasEmail": "mailto:robert.bourne@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/fas-il/IL_2007_2008.html",
+            "description": "This IL sets forth procedures for financial responsibility. The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts. All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/msword",
-                    "format": "DOC",
-                    "title": "FAS INSTRUCTIONAL LETTER 2007-01",
                     "description": "The Multiple Award Schedule (MAS) Express Program: Expedited Procedures for Financial Responsibility Determination and Award.",
-                    "downloadURL": "https://inventory.data.gov/dataset/e6cca07d-5109-4a4f-aee4-6ee975d7f01a/resource/6c890d1c-4a9c-4dc1-a91c-6acc5f0ac3d4/download/fas-instructional-letter-2007-01.docx"
+                    "downloadURL": "https://inventory.data.gov/dataset/e6cca07d-5109-4a4f-aee4-6ee975d7f01a/resource/6c890d1c-4a9c-4dc1-a91c-6acc5f0ac3d4/download/fas-instructional-letter-2007-01.docx",
+                    "format": "DOC",
+                    "mediaType": "application/msword",
+                    "title": "FAS INSTRUCTIONAL LETTER 2007-01"
                 }
             ],
+            "identifier": "GSA-5180",
+            "isPartOf": "GSA-2015-09-14-02",
+            "issued": "2011-07-26",
             "keyword": [
                 "Acquisition",
                 "Instructional Letters"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2017-05-08",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "FAS Instructional Letters 2007-01 Procedures for Financial Responsibility"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "FAS Instructional Letters 2008-01 Transferring Contract Files",
-            "description": "The purpose of this Instructional Letter (IL) is to outline steps to take when transferring contract files between Acquisition Centers within the Federal Acquisition Service (FAS). The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts. All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
-            "modified": "2017-05-08",
             "accessLevel": "public",
-            "identifier": "GSA-5179",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/fas-il/IL_2007_2008.html",
-            "issued": "2011-07-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "GSA-2015-09-14-02",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Robert D Bourne",
                 "hasEmail": "mailto:robert.bourne@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/fas-il/IL_2007_2008.html",
+            "description": "The purpose of this Instructional Letter (IL) is to outline steps to take when transferring contract files between Acquisition Centers within the Federal Acquisition Service (FAS). The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts. All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/msword",
-                    "format": "doc",
-                    "title": "FAS Instructional Letter 2008-01",
                     "description": "The Multiple Award Schedule (MAS) Contract Transfer Guideline: How to Manage the Contract File Transfer Process.",
-                    "downloadURL": "https://inventory.data.gov/dataset/06f99d73-fd4a-4d86-af29-77f2a52c00cd/resource/0fdcd3ae-7fa9-4460-b486-ca8aba8ac217/download/fas-instructional-letter-2008-01.docx"
+                    "downloadURL": "https://inventory.data.gov/dataset/06f99d73-fd4a-4d86-af29-77f2a52c00cd/resource/0fdcd3ae-7fa9-4460-b486-ca8aba8ac217/download/fas-instructional-letter-2008-01.docx",
+                    "format": "doc",
+                    "mediaType": "application/msword",
+                    "title": "FAS Instructional Letter 2008-01"
                 }
             ],
+            "identifier": "GSA-5179",
+            "isPartOf": "GSA-2015-09-14-02",
+            "issued": "2011-07-26",
             "keyword": [
                 "Acquisition",
                 "Instructional Letters"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:007"
-            ],
             "language": [
                 "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2017-05-08",
+            "programCode": [
+                "023:007"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "FAS Instructional Letters 2008-01 Transferring Contract Files"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Acquisition Service Instructional Letter 2012",
-            "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.  All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
-            "modified": "2020-12-30",
             "accessLevel": "public",
-            "identifier": "GSA-6374",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/fas-il/IL_01_data_dictionary.html",
-            "issued": "2011-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-09-14-02",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David W Orcutt",
                 "hasEmail": "mailto:david.orcutt@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/fas-il/IL_01_data_dictionary.html",
+            "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.  All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "FAS IL Table of Contents 2012",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/733ac5c5-fe80-41f3-8d2b-e3c749793b96/download/table-of-contents-federal-acquisition-service-instructional-letters-2012.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/733ac5c5-fe80-41f3-8d2b-e3c749793b96/download/table-of-contents-federal-acquisition-service-instructional-letters-2012.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FAS IL Table of Contents 2012"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2012-01",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/24d008b0-9a84-48c6-a026-5bce98eed444/download/instruction-letter-il-2012-01.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/24d008b0-9a84-48c6-a026-5bce98eed444/download/instruction-letter-il-2012-01.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2012-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2012-02",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/d994b868-e03e-4f76-8c08-50348594b4ae/download/instruction-letter-il-2012-02.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/d994b868-e03e-4f76-8c08-50348594b4ae/download/instruction-letter-il-2012-02.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2012-02"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2012-03",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/5f750b55-dd41-40e4-bd78-64f9bbc95d1f/download/instruction-letter-il-2012-03.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/5f750b55-dd41-40e4-bd78-64f9bbc95d1f/download/instruction-letter-il-2012-03.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2012-03"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2012-03-Supplemental",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/2afa5ba0-33b6-4bae-b553-91446c408b23/download/instruction-letter-il-2012-03-supplement.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/2afa5ba0-33b6-4bae-b553-91446c408b23/download/instruction-letter-il-2012-03-supplement.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2012-03-Supplemental"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2012-04",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/84bfd581-a6bf-4631-b9cb-a842faff8a51/download/instruction-letter-il-2012-04.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/84bfd581-a6bf-4631-b9cb-a842faff8a51/download/instruction-letter-il-2012-04.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2012-04"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2012-05",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/0e2fb00a-7471-4050-adc9-12df8d15e673/download/instruction-letter-il-2012-05.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/0e2fb00a-7471-4050-adc9-12df8d15e673/download/instruction-letter-il-2012-05.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2012-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2012-06",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/00bf1ca0-a17f-40ee-ac87-4ab1e18db05f/download/instruction-letter-il-2012-06.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/00bf1ca0-a17f-40ee-ac87-4ab1e18db05f/download/instruction-letter-il-2012-06.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2012-06"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2012-07",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/dd3eb28b-dc6d-45c8-a76c-b45534f27a93/download/instruction-letter-il-2012-07.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/dd3eb28b-dc6d-45c8-a76c-b45534f27a93/download/instruction-letter-il-2012-07.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2012-07"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2012-07-Supplemental",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/9aa80046-b6f2-481c-a2bd-e3cbb00699bf/download/instruction-letter-il-2012-07-supplement.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/9aa80046-b6f2-481c-a2bd-e3cbb00699bf/download/instruction-letter-il-2012-07-supplement.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2012-07-Supplemental"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2012-08",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/7bdcc547-ae5b-4143-9dd2-a25e9e5dea9a/download/instruction-letter-il-2012-08.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/7bdcc547-ae5b-4143-9dd2-a25e9e5dea9a/download/instruction-letter-il-2012-08.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2012-08"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2012-09",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/a423f50c-1803-483a-ac39-4cfda640b968/download/instruction-letter-il-2012-09.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/a423f50c-1803-483a-ac39-4cfda640b968/download/instruction-letter-il-2012-09.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2012-09"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2012-09-Supplemental",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/06354a4e-ddae-479b-a001-ff5150ceccbb/download/fas-instruction-letter-il-2012-09-supplement.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/06354a4e-ddae-479b-a001-ff5150ceccbb/download/fas-instruction-letter-il-2012-09-supplement.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2012-09-Supplemental"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2012-10",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/068513c5-6917-426f-b5a7-f73551d118fd/download/instruction-letter-il-2012-10.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/068513c5-6917-426f-b5a7-f73551d118fd/download/instruction-letter-il-2012-10.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2012-10"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2012-10-Supplemental",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/b0219277-f535-4534-b646-996724ad443a/download/instruction-letter-il-2012-10-supplement.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/b0219277-f535-4534-b646-996724ad443a/download/instruction-letter-il-2012-10-supplement.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2012-10-Supplemental"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2012-11",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/746e3ec6-c226-4d32-9474-90cfca2e3280/download/instruction-letter-il-2012-11.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/4e5de992-579a-4709-9f46-77d399f4e9f8/resource/746e3ec6-c226-4d32-9474-90cfca2e3280/download/instruction-letter-il-2012-11.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2012-11"
                 }
             ],
+            "identifier": "GSA-6374",
+            "isPartOf": "GSA-2015-09-14-02",
+            "issued": "2011-10-01",
             "keyword": [
                 "FAS",
                 "Industrial Funding Fee",
                 "Instructional Letters",
                 "Interactive"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-30",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "United States",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "Federal Acquisition Service Instructional Letter 2012"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Procurement Data System",
-            "description": "The Federal Procurement Data System houses Federal contract information where a contract's value is expected to exceed the micro-purchase threshold.",
-            "modified": "2016-01-07",
             "accessLevel": "public",
-            "identifier": "GSA-2412",
-            "dataQuality": true,
-            "issued": "2003-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "U.S. Governmentwide",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mary Searcy",
                 "hasEmail": "mailto:mary.searcy@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The Federal Procurement Data System houses Federal contract information where a contract's value is expected to exceed the micro-purchase threshold.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/rss+xml",
+                    "downloadURL": "https://www.fpds.gov/fpdsng_cms/index.php?format=feed&type=atom",
                     "format": "application/rss+xml",
-                    "title": "Federal Procurement Data System",
-                    "downloadURL": "https://www.fpds.gov/fpdsng_cms/index.php?format=feed&type=atom"
+                    "mediaType": "application/rss+xml",
+                    "title": "Federal Procurement Data System"
                 }
             ],
+            "identifier": "GSA-2412",
+            "issued": "2003-10-01",
             "keyword": [
                 "Acquisition",
                 "Award",
@@ -5027,42 +5020,40 @@
                 "Procurement",
                 "reporting"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-07",
             "programCode": [
                 "023:012"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "U.S. Governmentwide",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "Federal Procurement Data System"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Fair Act Inventory Data",
-            "description": "The Federal Activities Inventory Reform (FAIR) Act Inventory contains GSA's information related to the determination of whether a position is commercial or inherently governmental in nature.  Total Full-time Equivalent (FTE) are listed by activity, city and state and a designation of commercial (C) or inherently governmental (I).",
-            "modified": "2015-11-16",
             "accessLevel": "public",
-            "identifier": "GSA-2079",
-            "dataQuality": true,
-            "describedBy": "http://www.whitehouse.gov/sites/default/files/omb/assets/procurement_fair/fair_spreadsheet.xls",
-            "issued": "2009-03-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Paul F Boyle",
                 "hasEmail": "mailto:paul.boyle@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.whitehouse.gov/sites/default/files/omb/assets/procurement_fair/fair_spreadsheet.xls",
+            "description": "The Federal Activities Inventory Reform (FAIR) Act Inventory contains GSA's information related to the determination of whether a position is commercial or inherently governmental in nature.  Total Full-time Equivalent (FTE) are listed by activity, city and state and a designation of commercial (C) or inherently governmental (I).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5070,6 +5061,8 @@
                     "title": "GSA Fair Act Inventory Data"
                 }
             ],
+            "identifier": "GSA-2079",
+            "issued": "2009-03-01",
             "keyword": [
                 "Activity",
                 "Commercial",
@@ -5078,141 +5071,141 @@
                 "Inherently Governmental",
                 "Inventory"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2015-11-16",
             "programCode": [
                 "023:014"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "People"
-            ]
+            ],
+            "title": "GSA Fair Act Inventory Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2012, 1st Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
             "accessLevel": "public",
-            "identifier": "GSA-6376",
-            "dataQuality": true,
-            "describedBy": "http://www.gsa.gov/networx",
-            "issued": "2012-01-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.gsa.gov/networx",
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/networx/TotRevFY12_1stQtr.xlsx",
                     "format": "xlsx",
-                    "title": "NetworxBusinessVolume_FY2012_1stQtr",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/networx/TotRevFY12_1stQtr.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "NetworxBusinessVolume_FY2012_1stQtr"
                 }
             ],
+            "identifier": "GSA-6376",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2012-01-01",
             "keyword": [
                 "Networx",
                 "telecommunications."
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "United States",
             "theme": [
                 "Real Estate"
-            ]
+            ],
+            "title": "Networx Business Volume FY2012, 1st Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - OIG Apr-June 2014, 3rd Qtr",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the Office of the Inspector General.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-05-10",
-            "dataQuality": true,
-            "issued": "2015-05-21",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-9",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daphne Muse",
                 "hasEmail": "mailto:gsaig.alias.daphne.muse@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the Office of the Inspector General.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xlsx",
-                    "title": "April June 2014 OIG PC Transactions",
                     "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the Office of the Inspector General.",
-                    "downloadURL": "https://inventory.data.gov/dataset/0a5b4508-03ab-431f-940a-bae972ef2382/resource/d5d026da-23c8-4f6f-8e78-6699045b984f/download/april-june-2014-oig-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/0a5b4508-03ab-431f-940a-bae972ef2382/resource/d5d026da-23c8-4f6f-8e78-6699045b984f/download/april-june-2014-oig-pc-transactions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "April June 2014 OIG PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-01-05-10",
+            "isPartOf": "GSA-2016-01-05-9",
+            "issued": "2015-05-21",
             "keyword": [
                 "Inspector General",
                 "Office of Inspector General",
                 "Purchase Card",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:020"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - OIG Apr-June 2014, 3rd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Sustainable Facilities Tool",
-            "description": "With the SFTool API, you can access a myriad of high performance building information. Pull the most up to date information about green products, services, and materials. Put sustainable strategies in the hands of your audience today. All of our API methods are HTTP GET and always return the latest data. Whether you\u2019re looking to add sustainable building information to your website or blog, or looking for data to build an application, the SFTool API is here for you.Making API calls is very straightforward. There is a single base URI for each data category. By default, it will return all of the data for that category. By using any of our optional parameters, you can filter the data as you see fit. Signup for free to get the SFTool API key at  https://api.data.gov/signup/.",
-            "modified": "2018-09-24",
             "accessLevel": "public",
-            "identifier": "GSA-138568",
-            "dataQuality": true,
-            "describedBy": "https://sftool.gov/Developers/",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael F Bloom",
                 "hasEmail": "mailto:michael.bloom@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://sftool.gov/Developers/",
+            "description": "With the SFTool API, you can access a myriad of high performance building information. Pull the most up to date information about green products, services, and materials. Put sustainable strategies in the hands of your audience today. All of our API methods are HTTP GET and always return the latest data. Whether you\u2019re looking to add sustainable building information to your website or blog, or looking for data to build an application, the SFTool API is here for you.Making API calls is very straightforward. There is a single base URI for each data category. By default, it will return all of the data for that category. By using any of our optional parameters, you can filter the data as you see fit. Signup for free to get the SFTool API key at  https://api.data.gov/signup/.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5221,171 +5214,171 @@
                     "title": "Sustainable Facilities Tool"
                 }
             ],
+            "identifier": "GSA-138568",
             "keyword": [
                 "API",
                 "SFTool",
                 "Sustainable Facilities Tool"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-09-24",
             "programCode": [
                 "023:009"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "API"
-            ]
+            ],
+            "title": "Sustainable Facilities Tool"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Acquisition Service Instructional Letter 2009",
-            "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.  All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
-            "modified": "2020-12-22",
             "accessLevel": "public",
-            "identifier": "GSA-6367",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/fas-il/IL_01_data_dictionary.html",
-            "issued": "2010-01-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-09-14-02",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David W Orcutt",
                 "hasEmail": "mailto:david.orcutt@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/fas-il/IL_01_data_dictionary.html",
+            "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.  All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "FAS IL 2009 Table of Contents",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/c15954a2-f177-4463-89d5-9b3cb0ae62fc/resource/f85a9b50-1929-49b0-8932-6e9e69497753/download/table-of-contents-federal-acquisition-service-instructional-letters-2009.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/c15954a2-f177-4463-89d5-9b3cb0ae62fc/resource/f85a9b50-1929-49b0-8932-6e9e69497753/download/table-of-contents-federal-acquisition-service-instructional-letters-2009.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FAS IL 2009 Table of Contents"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
-                    "format": "docx",
-                    "title": "FAS IL 2009-01",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/c15954a2-f177-4463-89d5-9b3cb0ae62fc/resource/2147cf36-32cc-48a0-bf3f-3993245b99b9/download/fas-instructional-letter-2009-01.docx"
+                    "downloadURL": "https://inventory.data.gov/dataset/c15954a2-f177-4463-89d5-9b3cb0ae62fc/resource/2147cf36-32cc-48a0-bf3f-3993245b99b9/download/fas-instructional-letter-2009-01.docx",
+                    "format": "docx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "FAS IL 2009-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2009-02",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/c15954a2-f177-4463-89d5-9b3cb0ae62fc/resource/c8722b57-1c8a-4a0b-a4f5-acd0d638b4af/download/fas-instructional-letter-2009-02.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/c15954a2-f177-4463-89d5-9b3cb0ae62fc/resource/c8722b57-1c8a-4a0b-a4f5-acd0d638b4af/download/fas-instructional-letter-2009-02.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2009-02"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2009-03",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/c15954a2-f177-4463-89d5-9b3cb0ae62fc/resource/04b327ee-ebc9-41b6-82fa-07e7294d87e4/download/fas-instructional-letter-2009-03.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/c15954a2-f177-4463-89d5-9b3cb0ae62fc/resource/04b327ee-ebc9-41b6-82fa-07e7294d87e4/download/fas-instructional-letter-2009-03.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2009-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://inventory.data.gov/dataset/c15954a2-f177-4463-89d5-9b3cb0ae62fc/resource/596525fe-eac8-48bb-8307-90ecbec2259b/download/fas-instructional-letter-il-2009-03-supplement-1.pdf",
+                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
                     "format": "pdf",
-                    "title": "FAS IL 2009-03 Supplemental",
-                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts."
+                    "title": "FAS IL 2009-03 Supplemental"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2009-04",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/c15954a2-f177-4463-89d5-9b3cb0ae62fc/resource/b3dfb0cd-daad-46dd-b91b-ff2f130b7a41/download/fas-instructional-letter-2009-04.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/c15954a2-f177-4463-89d5-9b3cb0ae62fc/resource/b3dfb0cd-daad-46dd-b91b-ff2f130b7a41/download/fas-instructional-letter-2009-04.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2009-04"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2009-05",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/c15954a2-f177-4463-89d5-9b3cb0ae62fc/resource/78e701df-bdba-4392-9805-80370dba7dc4/download/fas-instructional-letter-2009-05.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/c15954a2-f177-4463-89d5-9b3cb0ae62fc/resource/78e701df-bdba-4392-9805-80370dba7dc4/download/fas-instructional-letter-2009-05.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2009-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2009-06",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/c15954a2-f177-4463-89d5-9b3cb0ae62fc/resource/3ea4faca-90a5-4d5b-9bc3-f148974fbd35/download/fas-instructional-letter-2009-06.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/c15954a2-f177-4463-89d5-9b3cb0ae62fc/resource/3ea4faca-90a5-4d5b-9bc3-f148974fbd35/download/fas-instructional-letter-2009-06.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2009-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://inventory.data.gov/dataset/c15954a2-f177-4463-89d5-9b3cb0ae62fc/resource/9b146ca3-0032-471b-a6b9-6f3556da6e9a/download/fas-instructional-letter-2009-07.pdf",
+                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
                     "format": "pdf",
-                    "title": "FAS IL 2009-07",
-                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts."
+                    "title": "FAS IL 2009-07"
                 }
             ],
+            "identifier": "GSA-6367",
+            "isPartOf": "GSA-2015-09-14-02",
+            "issued": "2010-01-01",
             "keyword": [
                 "FAS",
                 "Industrial Funding Fee",
                 "Instructional Letters",
                 "Interactive"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-22",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "Federal Acquisition Service Instructional Letter 2009"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Aircraft Cost and Utilization Data",
-            "description": "Federal aviation data is submitted quarterly to the Federal Aviation Interactive Reporting System (FARIS) IT application.  This is a GSA system which is a secure, web-based application.  The report summarizes the Annual aviation cost and utilization information submitted by the thirteen agencies that own or operate aircraft as part of their mission.",
-            "modified": "2016-05-10",
             "accessLevel": "public",
-            "identifier": "GSA-2082",
-            "dataQuality": true,
-            "describedBy": "http://www.gsa.gov/Portal/gsa/ep/channelView.do?pageTypeId=17113&channelPage=%2Fep%2Fchannel%2FgsaOverview.jsp&channelId=-24585",
-            "issued": "2009-06-30",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "Federal agencies that own or lease aircraft.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Robert Galloway",
                 "hasEmail": "mailto:robert.galloway@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.gsa.gov/Portal/gsa/ep/channelView.do?pageTypeId=17113&channelPage=%2Fep%2Fchannel%2FgsaOverview.jsp&channelId=-24585",
+            "description": "Federal aviation data is submitted quarterly to the Federal Aviation Interactive Reporting System (FARIS) IT application.  This is a GSA system which is a secure, web-based application.  The report summarizes the Annual aviation cost and utilization information submitted by the thirteen agencies that own or operate aircraft as part of their mission.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "http://www.gsa.gov/portal/content/104076",
                     "format": "html",
-                    "title": "Federal Aircraft Cost and Utilization Data",
-                    "downloadURL": "http://www.gsa.gov/portal/content/104076"
+                    "mediaType": "text/html",
+                    "title": "Federal Aircraft Cost and Utilization Data"
                 }
             ],
+            "identifier": "GSA-2082",
+            "issued": "2009-06-30",
             "keyword": [
                 "Aircraft Agency",
                 "Aircraft Cost",
@@ -5393,50 +5386,50 @@
                 "Aircraft Utilization",
                 "FAIRS"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-05-10",
             "programCode": [
                 "023:013"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "Federal agencies that own or lease aircraft.",
             "theme": [
                 "Travel and Transportation"
-            ]
+            ],
+            "title": "Federal Aircraft Cost and Utilization Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Business Opportunities Data",
-            "description": "FedBizOpps is the single government point-of-entry for solicitations of any dollar amount and for required synopsis over $25,000, allowing commercial business suppliers and government buyers to post, search, monitor, and retrieve opportunities in federal government markets.  FBO now includes the functionality of the Federal Technical Data Solutions (FedTeDS) which allows agencies to securely disseminate sensitive acquisition-related technical data for solicitations to approved business partners. This dataset contains current active notices and is updated weekly.",
-            "modified": "2016-03-13",
             "accessLevel": "public",
-            "identifier": "GSA-4007",
-            "dataQuality": true,
-            "describedBy": "https://www.fbo.gov/?s=generalinfo&mode=list&tab=list&tabmode=list&static=interface",
-            "issued": "2010-08-10",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "U.S. Governmentwide",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Corro",
                 "hasEmail": "mailto:john.corro@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.fbo.gov/?s=generalinfo&mode=list&tab=list&tabmode=list&static=interface",
+            "description": "FedBizOpps is the single government point-of-entry for solicitations of any dollar amount and for required synopsis over $25,000, allowing commercial business suppliers and government buyers to post, search, monitor, and retrieve opportunities in federal government markets.  FBO now includes the functionality of the Federal Technical Data Solutions (FedTeDS) which allows agencies to securely disseminate sensitive acquisition-related technical data for solicitations to approved business partners. This dataset contains current active notices and is updated weekly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/xml",
+                    "downloadURL": "ftp://ftp.fbo.gov/datagov/FBOFullXML.xml",
                     "format": "application/xml",
-                    "title": "Federal Business Opportunities Data",
-                    "downloadURL": "ftp://ftp.fbo.gov/datagov/FBOFullXML.xml"
+                    "mediaType": "application/xml",
+                    "title": "Federal Business Opportunities Data"
                 }
             ],
+            "identifier": "GSA-4007",
+            "issued": "2010-08-10",
             "keyword": [
                 "Award",
                 "FBO",
@@ -5448,236 +5441,236 @@
                 "Solicitation",
                 "opportunities"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-03-13",
             "programCode": [
                 "023:012"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "U.S. Governmentwide",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "Federal Business Opportunities Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Strategic Sourcing Initiative (FSSI) DDS2",
-            "description": "FSSI Domestic Delivery Services 2 BPA vendor submitted usage reports",
-            "modified": "2016-02-23",
             "accessLevel": "non-public",
-            "identifier": "GSA - 139666",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Claudia J Brumbach",
                 "hasEmail": "mailto:claudia.brumbach@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "FSSI Domestic Delivery Services 2 BPA vendor submitted usage reports",
+            "identifier": "GSA - 139666",
             "keyword": [
                 "DDS2",
                 "FSSI"
             ],
-            "bureauCode": [
-                "023:10"
+            "language": [
+                "en-us"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-02-23",
             "programCode": [
                 "023:012"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "Federal Strategic Sourcing Initiative (FSSI) DDS2"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2011, 1st Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
             "accessLevel": "public",
-            "identifier": "GSA-5049",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/networx/networx_revenue_data_dictionary_fy10.html",
-            "issued": "2011-07-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/networx/networx_revenue_data_dictionary_fy10.html",
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/networx/networx_revenus_fy11_q1.xls",
                     "format": "xls",
-                    "title": "NetworxBusinessVolume_FY2011_1st Qtr",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/networx/networx_revenus_fy11_q1.xls"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NetworxBusinessVolume_FY2011_1st Qtr"
                 }
             ],
+            "identifier": "GSA-5049",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2011-07-13",
             "keyword": [
                 "Networx",
                 "telecommunications."
             ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:000"
-            ],
             "language": [
                 "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
+            "programCode": [
+                "023:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Real Estate"
-            ]
+            ],
+            "title": "Networx Business Volume FY2011, 1st Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2012, 2nd Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
             "accessLevel": "public",
-            "identifier": "GSA-7421",
-            "dataQuality": true,
-            "describedBy": "http://www.gsa.gov/networx",
-            "issued": "2012-07-17",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.gsa.gov/networx",
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/networx/TotRevFY12_2ndQtr.xlsx",
                     "format": "xlsx",
-                    "title": "NetworxBusinessVolume_FY2012_2ndQtr",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/networx/TotRevFY12_2ndQtr.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "NetworxBusinessVolume_FY2012_2ndQtr"
                 }
             ],
+            "identifier": "GSA-7421",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2012-07-17",
             "keyword": [
                 "Networx",
                 "telecommunications."
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Real Estate"
-            ]
+            ],
+            "title": "Networx Business Volume FY2012, 2nd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2011, 4th Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
             "accessLevel": "public",
-            "identifier": "GSA-6370",
-            "dataQuality": true,
-            "describedBy": "http://www.gsa.gov/networx",
-            "issued": "2012-01-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.gsa.gov/networx",
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/networx/TotRevFY11_4thQtr.xlsx",
                     "format": "xml",
-                    "title": "NetworxBusinessVolume_FY2011_4THQtr",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/networx/TotRevFY11_4thQtr.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "NetworxBusinessVolume_FY2011_4THQtr"
                 }
             ],
+            "identifier": "GSA-6370",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2012-01-01",
             "keyword": [
                 "Networx",
                 "telecommunications."
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "United States",
             "theme": [
                 "Real Estate"
-            ]
+            ],
+            "title": "Networx Business Volume FY2011, 4th Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Noticias y actualizaciones de GobiernoUSA.gov",
-            "description": "Mant&eacute;ngase al tanto de las noticias e informaciones importantes del Gobierno con el canal RSS de GobiernoUSA.gov: noticias y actualizaciones. Este canal se actualizar&aacute; cuando agreguemos noticias y contenido nuevo al sitio web GobiernoUSA.gov.",
-            "modified": "2015-11-23",
             "accessLevel": "public",
-            "identifier": "GSA-1275",
-            "dataQuality": true,
-            "describedBy": "http://www.rssboard.org/rss-specification",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Russell G O'Neill",
                 "hasEmail": "mailto:russell.oneill@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.rssboard.org/rss-specification",
+            "description": "Mant&eacute;ngase al tanto de las noticias e informaciones importantes del Gobierno con el canal RSS de GobiernoUSA.gov: noticias y actualizaciones. Este canal se actualizar&aacute; cuando agreguemos noticias y contenido nuevo al sitio web GobiernoUSA.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/xml",
+                    "downloadURL": "https://gobierno.usa.gov/rss/actualizaciones-articulos.xml",
                     "format": "xml",
-                    "title": "Noticias y actualizaciones de GobiernoUSA.gov",
-                    "downloadURL": "https://gobierno.usa.gov/rss/actualizaciones-articulos.xml"
+                    "mediaType": "application/xml",
+                    "title": "Noticias y actualizaciones de GobiernoUSA.gov"
                 }
             ],
+            "identifier": "GSA-1275",
             "keyword": [
                 "Blog",
                 "Consumer",
@@ -5687,52 +5680,52 @@
                 "news",
                 "smart living"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "sp-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2015-11-23",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "sp-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Other"
-            ]
+            ],
+            "title": "Noticias y actualizaciones de GobiernoUSA.gov"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "e-Buy Awards for Fiscal Year 2007",
-            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
-            "modified": "2016-01-21",
             "accessLevel": "public",
-            "identifier": "GSA-4096",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/eBuy_Awards_Data_Dictionary.html",
-            "issued": "2010-10-21",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-08-31",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Usha Gopal",
                 "hasEmail": "mailto:usha.gopal@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/eBuy_Awards_Data_Dictionary.html",
+            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/eBuy_Awards_FY2007.xls",
                     "format": "excel",
-                    "title": "e-Buy Awards for Fiscal Year 2007",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/eBuy_Awards_FY2007.xls"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "e-Buy Awards for Fiscal Year 2007"
                 }
             ],
+            "identifier": "GSA-4096",
+            "isPartOf": "GSA-2015-08-31",
+            "issued": "2010-10-21",
             "keyword": [
                 "Award",
                 "Contracts",
@@ -5742,289 +5735,290 @@
                 "Schedules",
                 "e-Buy"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-21",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "e-Buy Awards for Fiscal Year 2007"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Energy Usage Analysis System",
-            "description": "The EUAS application is a web based system which serves Energy Center of Expertise, under the Office of Facilitates Management and Service Programs.  EUAS is used for tracking energy details for various energy sources namely electricity, natural gas, oil, chilled water, steam and renewable energy.",
-            "modified": "2019-07-30",
             "accessLevel": "public",
-            "identifier": "GSA-4305",
-            "dataQuality": true,
-            "issued": "2010-11-15",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "023:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Shirl R Tillman",
                 "hasEmail": "mailto:shirl.tillman@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The EUAS application is a web based system which serves Energy Center of Expertise, under the Office of Facilitates Management and Service Programs.  EUAS is used for tracking energy details for various energy sources namely electricity, natural gas, oil, chilled water, steam and renewable energy.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "MAR.ACCTMULT",
                     "description": "EUAS - March 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/40a8dc65-3892-4b90-bc3d-aed025dcbeac/download/mar.acctmult.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/40a8dc65-3892-4b90-bc3d-aed025dcbeac/download/mar.acctmult.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MAR.ACCTMULT"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "MAR.AREA_FIELD_OFFICE",
                     "description": "EUAS - March 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/90f89199-c3a4-4e8b-ad81-59cfe30a24ff/download/mar.areafieldoffice.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/90f89199-c3a4-4e8b-ad81-59cfe30a24ff/download/mar.areafieldoffice.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MAR.AREA_FIELD_OFFICE"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "MAR.BUILDING_UNITS",
                     "description": "EUAS - March 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/2995cc8e-ddb5-4316-9cf5-9507c0284517/download/mar.buildingunits.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/2995cc8e-ddb5-4316-9cf5-9507c0284517/download/mar.buildingunits.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MAR.BUILDING_UNITS"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "MAR.CBECS_DATA_OFFICE_SPACE",
                     "description": "EUAS - March 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/8304cbcd-81b4-4fd7-aeea-bb31f2edf901/download/mar.cbecsdataofficespace.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/8304cbcd-81b4-4fd7-aeea-bb31f2edf901/download/mar.cbecsdataofficespace.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MAR.CBECS_DATA_OFFICE_SPACE"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "MAR.DIST_COST_CENTER",
                     "description": "EUAS - March 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/29f55faf-6e9e-456d-96eb-56d301f99f0a/download/mardistcostcenter.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/29f55faf-6e9e-456d-96eb-56d301f99f0a/download/mardistcostcenter.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MAR.DIST_COST_CENTER"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "MAR.DISTRICT",
                     "description": "EUAS - March 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/a27d2bf6-fd39-4207-a1f9-864365136a4a/download/mar.district.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/a27d2bf6-fd39-4207-a1f9-864365136a4a/download/mar.district.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MAR.DISTRICT"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "MAR.ENERGY_UTILIZATION",
                     "description": "EUAS - March 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/6db225db-9984-476d-b6eb-dd52d1205737/download/mar.energyutilization.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/6db225db-9984-476d-b6eb-dd52d1205737/download/mar.energyutilization.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MAR.ENERGY_UTILIZATION"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "MAR.FYR_BUILDING",
                     "description": "EUAS - March 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/6ee0689e-08ad-4317-90ae-2f8d68af5c49/download/mar.fyrbuilding.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/6ee0689e-08ad-4317-90ae-2f8d68af5c49/download/mar.fyrbuilding.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MAR.FYR_BUILDING"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "MAR.REGIONAL_PMT_TARGET",
                     "description": "EUAS - March 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/2dec83d7-1528-4441-a236-333dad55319d/download/mar.regionalpmttarget.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/2dec83d7-1528-4441-a236-333dad55319d/download/mar.regionalpmttarget.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MAR.REGIONAL_PMT_TARGET"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "MAR.UNIT_CONVERSIONS",
                     "description": "EUAS - March 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/79cc4b4a-0e4a-4eef-bc47-f766c17da0ab/download/mar.unitconversions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/79cc4b4a-0e4a-4eef-bc47-f766c17da0ab/download/mar.unitconversions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MAR.UNIT_CONVERSIONS"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "MAR.VENDOR",
                     "description": "EUAS - March 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/472ac414-8de7-405c-b81a-4c7f33778989/download/mar.vendor.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/472ac414-8de7-405c-b81a-4c7f33778989/download/mar.vendor.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MAR.VENDOR"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "MAR.WEATHER_DATA",
                     "description": "EUAS - March 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/02c874ff-0af6-40ba-9669-9bb83b46f9a9/download/mar.weatherdata.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/02c874ff-0af6-40ba-9669-9bb83b46f9a9/download/mar.weatherdata.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MAR.WEATHER_DATA"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "MAR.WEATHER_STATION",
                     "description": "EUAS - March 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/6b2eebc2-9399-4ffc-ba80-72154f330f1a/download/mar.weatherstation.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/6b2eebc2-9399-4ffc-ba80-72154f330f1a/download/mar.weatherstation.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MAR.WEATHER_STATION"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "MAR.FACILITY_BUILDINGS",
                     "description": "EUAS - March 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/b168c887-c8c7-4fa4-bb98-8603a38ca259/download/mar.facilitybuildings.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/b168c887-c8c7-4fa4-bb98-8603a38ca259/download/mar.facilitybuildings.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MAR.FACILITY_BUILDINGS"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "MAR.UNIT_SOURCE_CONVERSIONS",
                     "description": "EUAS - March 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/f22e1ca6-b246-4783-8472-ad2e3a65852c/download/mar.unitsourceconversions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/235b5536-64b0-4885-bc7a-5d3c6ac69761/resource/f22e1ca6-b246-4783-8472-ad2e3a65852c/download/mar.unitsourceconversions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MAR.UNIT_SOURCE_CONVERSIONS"
                 }
             ],
+            "identifier": "GSA-4305",
+            "issued": "2010-11-15",
             "keyword": [
                 "Analysis",
                 "Chilled Water",
                 "Energy Usage",
                 "Utilities",
                 "electricity",
-                "natural gas",
-                "oil",
-                "steam and renewable energy"
-            ],
-            "bureauCode": [
-                "023:05"
-            ],
-            "programCode": [
-                "023:014"
+                "natural gas",
+                "oil",
+                "steam and renewable energy"
             ],
             "language": [
                 "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-07-30",
+            "programCode": [
+                "023:014"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Energy & Environment"
-            ]
+            ],
+            "title": "Energy Usage Analysis System"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Procurement Data System - FPDS API",
-            "description": "The Federal Procurement Data System (FPDS) Next Generation has been re-engineered as a real-time federal enterprise information system. Web services based on SOAP and XML, implemented using Java technologies, are used in FPDS-NG to provide interoperability with various federal procurement systems",
-            "modified": "2018-10-09",
             "accessLevel": "public",
-            "identifier": "GSA - 138673",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mary Searcy",
                 "hasEmail": "mailto:mary.searcy@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The Federal Procurement Data System (FPDS) Next Generation has been re-engineered as a real-time federal enterprise information system. Web services based on SOAP and XML, implemented using Java technologies, are used in FPDS-NG to provide interoperability with various federal procurement systems",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/msword",
+                    "downloadURL": "https://www.fpds.gov/downloads/FPDS-Specifications-WebServices_Integration_Specifications_V1.5.doc",
                     "format": "API",
-                    "title": "Federal Procurement Data System - FPDS API",
-                    "downloadURL": "https://www.fpds.gov/downloads/FPDS-Specifications-WebServices_Integration_Specifications_V1.5.doc"
+                    "mediaType": "application/msword",
+                    "title": "Federal Procurement Data System - FPDS API"
                 }
             ],
+            "identifier": "GSA - 138673",
             "keyword": [
                 "API",
                 "FPDS"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-10-09",
             "programCode": [
                 "023:012"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "API"
-            ]
+            ],
+            "title": "Federal Procurement Data System - FPDS API"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Strategic Sourcing Initiative (FSSI) MRO",
-            "description": "FSSI Maintenance, Repair, and Operations BPA vendor submitted usage reports",
-            "modified": "2016-02-23",
             "accessLevel": "non-public",
-            "identifier": "GSA - 139667",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nathan Morgan Kreoger",
                 "hasEmail": "mailto:nathan.kreoger@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "FSSI Maintenance, Repair, and Operations BPA vendor submitted usage reports",
+            "identifier": "GSA - 139667",
             "keyword": [
                 "FSSI",
                 "MRO"
             ],
-            "bureauCode": [
-                "023:10"
+            "language": [
+                "en-us"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-02-23",
             "programCode": [
                 "023:012"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "Federal Strategic Sourcing Initiative (FSSI) MRO"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Strategic Sourcing Initiative(FSSI) Office Supplies 2",
-            "description": "FSSI Office Supplies 2 BPA vendor submitted usage reports",
-            "modified": "2016-02-23",
             "accessLevel": "non-public",
-            "identifier": "GSA - 139647",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joshua Daniel Royko",
                 "hasEmail": "mailto:joshua.royko@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "FSSI Office Supplies 2 BPA vendor submitted usage reports",
+            "identifier": "GSA - 139647",
             "keyword": [
                 "BPA",
                 "Data",
@@ -6038,39 +6032,38 @@
                 "Vendor",
                 "Wireless"
             ],
-            "bureauCode": [
-                "023:10"
+            "language": [
+                "en-us"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-02-23",
             "programCode": [
                 "023:012"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "Federal Strategic Sourcing Initiative(FSSI) Office Supplies 2"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "New Construction and Repair and Alteration (R&A) Projects",
-            "description": "This map shows new construction and major R&A projects in federal buildings under GSA\u2019s custody and control that are above the current prospectus threshold of $2.85 million. New construction and major R&A projects for two different fiscal years are displayed on the map. Projects for FY2014 were funded as part of the Consolidated Appropriations Act of 2014, and GSA will begin to execute these projects this year. Projects for FY2015 have been included in the President\u2019s Budget request, but require approval and funding from Congress before the projects can begin.",
-            "modified": "2014-04-28",
             "accessLevel": "public",
-            "identifier": "GSA-138569",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "023:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Andrew M Heller",
                 "hasEmail": "mailto:andrew.heller@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "This map shows new construction and major R&A projects in federal buildings under GSA\u2019s custody and control that are above the current prospectus threshold of $2.85 million. New construction and major R&A projects for two different fiscal years are displayed on the map. Projects for FY2014 were funded as part of the Consolidated Appropriations Act of 2014, and GSA will begin to execute these projects this year. Projects for FY2015 have been included in the President\u2019s Budget request, but require approval and funding from Congress before the projects can begin.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6079,6 +6072,7 @@
                     "title": "New Construction and Repair and Alteration (R&A) Projects"
                 }
             ],
+            "identifier": "GSA-138569",
             "keyword": [
                 "GSA",
                 "General Services Administration",
@@ -6086,99 +6080,100 @@
                 "PBS owned",
                 "buildings"
             ],
-            "bureauCode": [
-                "023:05"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2014-04-28",
             "programCode": [
                 "023:003"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Real Estate"
-            ]
+            ],
+            "title": "New Construction and Repair and Alteration (R&A) Projects"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "System for Award Management (SAM) API",
-            "description": "The SAM API is a RESTful method of retrieving public information about the businesses, organizations, or individuals (referred to as entities) within the SAM entity regsitration data set. Public registration information can currently be retrieved on an entity-by-entity basis.\u00a0In addition, the SAM Search API offers both a 'quick search' and 'advanced search' method.",
-            "modified": "2019-11-26",
             "accessLevel": "public",
-            "identifier": "GSA - 139633",
-            "dataQuality": true,
-            "describedBy": "http://gsa.github.io/sam_api/sam/fields3.html",
-            "issued": "2010-01-14",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
+            "bureauCode": [
+                "023:30"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Meredith Whitehead",
                 "hasEmail": "mailto:meredith.whitehead@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://gsa.github.io/sam_api/sam/fields3.html",
+            "description": "The SAM API is a RESTful method of retrieving public information about the businesses, organizations, or individuals (referred to as entities) within the SAM entity regsitration data set. Public registration information can currently be retrieved on an entity-by-entity basis.\u00a0In addition, the SAM Search API offers both a 'quick search' and 'advanced search' method.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://gsa.github.io/sam_api/sam/index.html",
-                    "format": "API",
-                    "title": "SAM - System for Award Management API",
-                    "description": "System implementing the functionalities of the legacy IAE applications: CCR, FedReg, ORCA, and EPLS.",
                     "describedBy": "http://gsa.github.io/sam_api/sam/fields3.html",
-                    "describedByType": "text/html"
+                    "describedByType": "text/html",
+                    "description": "System implementing the functionalities of the legacy IAE applications: CCR, FedReg, ORCA, and EPLS.",
+                    "format": "API",
+                    "title": "SAM - System for Award Management API"
                 }
             ],
+            "identifier": "GSA - 139633",
+            "issued": "2010-01-14",
             "keyword": [
                 "API",
                 "Acquisition",
                 "Award",
                 "Contracts"
             ],
-            "bureauCode": [
-                "023:30"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-11-26",
             "programCode": [
                 "023:012"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "API"
-            ]
+            ],
+            "title": "System for Award Management (SAM) API"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "CIO Governance Board Membership List",
-            "description": "Json file for CIO Governance Board Membership List",
-            "modified": "2015-09-01",
             "accessLevel": "public",
-            "identifier": "GSA-2015-09-01-01",
-            "dataQuality": true,
-            "issued": "2015-09-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jonah M Hatfield",
                 "hasEmail": "mailto:jonah.hatfield@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Json file for CIO Governance Board Membership List",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://www.gsa.gov/largedocs/governanceboards.json",
+                    "description": "CIO Governance Board Membership List",
                     "format": "json",
-                    "title": "Governance Board",
-                    "description": "CIO Governance Board Membership List"
+                    "title": "Governance Board"
                 }
             ],
+            "identifier": "GSA-2015-09-01-01",
+            "issued": "2015-09-01",
             "keyword": [
                 "Board",
                 "CIO",
@@ -6186,77 +6181,74 @@
                 "List",
                 "Membership"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2015-09-01",
             "programCode": [
                 "023:014"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Json File"
-            ]
+            ],
+            "title": "CIO Governance Board Membership List"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Strategic Sourcing Initiative(FSSI) Wireless",
-            "description": "FSSI Wireless BPA vendor submitted usage reports",
-            "modified": "2016-02-23",
             "accessLevel": "non-public",
-            "identifier": "GSA - 139665",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Andrew Peters",
                 "hasEmail": "mailto:david.peters@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "FSSI Wireless BPA vendor submitted usage reports",
+            "identifier": "GSA - 139665",
             "keyword": [
                 "FSSI",
                 "Wireless"
             ],
-            "bureauCode": [
-                "023:10"
+            "language": [
+                "en-us"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-02-23",
             "programCode": [
                 "023:012"
             ],
-            "language": [
-                "en-us"
-            ],
-            "theme": [
-                "Acquisition"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Go.USA.gov URL Shortner API",
-            "description": "The Go.USA.gov REST API allows you interact with Go.USA.gov by shortening URLs, previewing long urls, and getting the number of clicks to a Go.USA.gov URL..  An API key is required and available to any registered Go.USA.gov user.",
-            "modified": "2018-09-26",
-            "accessLevel": "public",
-            "identifier": "GSA-2014-02-14-1",
-            "dataQuality": true,
-            "describedBy": "https://go.usa.gov/api",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
+            "theme": [
+                "Acquisition"
+            ],
+            "title": "Federal Strategic Sourcing Initiative(FSSI) Wireless"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "023:30"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Russell G O'Neill",
                 "hasEmail": "mailto:russell.oneill@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://go.usa.gov/api",
+            "description": "The Go.USA.gov REST API allows you interact with Go.USA.gov by shortening URLs, previewing long urls, and getting the number of clicks to a Go.USA.gov URL..  An API key is required and available to any registered Go.USA.gov user.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6265,43 +6257,44 @@
                     "title": "Go.USA.gov URL Shortner API"
                 }
             ],
+            "identifier": "GSA-2014-02-14-1",
             "keyword": [
                 "API",
                 "Go.USA.gov URL shortener"
             ],
-            "bureauCode": [
-                "023:30"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-09-26",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "API"
-            ]
+            ],
+            "title": "Go.USA.gov URL Shortner API"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "List of Government Developer Hubs",
-            "description": "A list of public developer hubs maintained by the US government.",
-            "modified": "2016-03-04",
             "accessLevel": "public",
-            "identifier": "GSA - 139012",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Richard G Brooks",
                 "hasEmail": "mailto:richard.g.brooks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "A list of public developer hubs maintained by the US government.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6310,215 +6303,215 @@
                     "title": "List of Government Developer Hubs"
                 }
             ],
+            "identifier": "GSA - 139012",
             "keyword": [
                 "API",
                 "developers",
                 "government",
                 "web service"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-03-04",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "API"
-            ]
+            ],
+            "title": "List of Government Developer Hubs"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2010",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2016-02-19",
             "accessLevel": "public",
-            "identifier": "GSA-4498",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/networx/networx_revenue_data_dictionary_fy10.html",
-            "issued": "2011-02-24",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/networx/networx_revenue_data_dictionary_fy10.html",
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/networx/NetworxRevenue_FY10.xls",
                     "format": "xls",
-                    "title": "NetworxBusinessVolume_FY2010",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/networx/NetworxRevenue_FY10.xls"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NetworxBusinessVolume_FY2010"
                 }
             ],
+            "identifier": "GSA-4498",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2011-02-24",
             "keyword": [
                 "Networx",
                 "telecommunications."
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-02-19",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Real Estate"
-            ]
+            ],
+            "title": "Networx Business Volume FY2010"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2012, 3rd Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
             "accessLevel": "public",
-            "identifier": "GSA-9611",
-            "dataQuality": true,
-            "describedBy": "http://www.gsa.gov/networx",
-            "issued": "2012-09-14",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.gsa.gov/networx",
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/networx/TotRevFY12_3rdQtr.xlsx",
                     "format": "xlsx",
-                    "title": "NetworxBusinessVolume_FY2012_3rdQtr",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/networx/TotRevFY12_3rdQtr.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "NetworxBusinessVolume_FY2012_3rdQtr"
                 }
             ],
+            "identifier": "GSA-9611",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2012-09-14",
             "keyword": [
                 "Networx",
                 "telecommunications."
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Real Estate"
-            ]
+            ],
+            "title": "Networx Business Volume FY2012, 3rd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2011, 3rd Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
             "accessLevel": "public",
-            "identifier": "GSA-6249",
-            "dataQuality": true,
-            "describedBy": "http://www.gsa.gov/networx",
-            "issued": "2012-04-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.gsa.gov/networx",
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/networx/TotRevFY11_3rdQtr.xlsx",
                     "format": "xlsx",
-                    "title": "NetworxBusinessVolume_FY2011_3rdQtr",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/networx/TotRevFY11_3rdQtr.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "NetworxBusinessVolume_FY2011_3rdQtr"
                 }
             ],
+            "identifier": "GSA-6249",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2012-04-01",
             "keyword": [
                 "Networx",
                 "telecommunications."
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Real Estate"
-            ]
+            ],
+            "title": "Networx Business Volume FY2011, 3rd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "System for Award Management (SAM) Public Extract - Exclusions",
-            "description": "This dataset contains a daily snapshot of active exclusion records entered by the U.S. Federal government identifying those parties excluded from receiving Federal contracts, certain subcontracts, and certain types of Federal financial and non-financial assistance and benefits. The data was formerly contained in the Excluded Parties List System (EPLS). In July 2012, EPLS was incorporated into the System for Award Management (SAM). SAM is now the electronic, web-based system that keeps its user community aware of administrative and statutory exclusions across the entire government, and individuals barred from entering the United States. Users must read the exclusion record completely to understand how it impacts the excluded party.\u00a0\r\n\r\nNote - Here is the link for the SAM Functional Data Dictionary - https://www.sam.gov/SAM/transcript/SAM_Functional_Data_Dictionary.pdf",
-            "modified": "2018-12-18",
             "accessLevel": "public",
-            "identifier": "GSA-1626",
-            "dataQuality": true,
-            "describedBy": "https://www.sam.gov/sam/transcript/SAM_Exclusions_Extract_User_Guide.pdf",
-            "describedByType": "application/pdf",
-            "issued": "2006-09-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "U.S. Governmentwide",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Meredith M Whitehead",
                 "hasEmail": "mailto:meredith.whitehead@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.sam.gov/sam/transcript/SAM_Exclusions_Extract_User_Guide.pdf",
+            "describedByType": "application/pdf",
+            "description": "This dataset contains a daily snapshot of active exclusion records entered by the U.S. Federal government identifying those parties excluded from receiving Federal contracts, certain subcontracts, and certain types of Federal financial and non-financial assistance and benefits. The data was formerly contained in the Excluded Parties List System (EPLS). In July 2012, EPLS was incorporated into the System for Award Management (SAM). SAM is now the electronic, web-based system that keeps its user community aware of administrative and statutory exclusions across the entire government, and individuals barred from entering the United States. Users must read the exclusion record completely to understand how it impacts the excluded party.\u00a0\r\n\r\nNote - Here is the link for the SAM Functional Data Dictionary - https://www.sam.gov/SAM/transcript/SAM_Functional_Data_Dictionary.pdf",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://sam.gov/content/home",
+                    "description": "The System for Award Management (SAM.gov) is an official website of the U.S. Government. There is no cost to use SAM.gov. You can use this site to:\r\n\r\nRegister to do business with the U.S. Government, Update, renew, or check the status of your entity registration, Search for entity registration and exclusion records, Search for assistance listings (formerly CFDA.gov), wage determinations (formerly WDOL.gov), contract opportunities (formerly FBO.gov), and contract data reports (formerly part of FPDS.gov).\r\nView and submit BioPreferred and Service Contract Reports, Access publicly available award data via data extracts and system accounts.",
                     "format": "html",
-                    "title": "System for Award Management (SAM) Public Extract - Exclusions",
-                    "description": "The System for Award Management (SAM.gov) is an official website of the U.S. Government. There is no cost to use SAM.gov. You can use this site to:\r\n\r\nRegister to do business with the U.S. Government, Update, renew, or check the status of your entity registration, Search for entity registration and exclusion records, Search for assistance listings (formerly CFDA.gov), wage determinations (formerly WDOL.gov), contract opportunities (formerly FBO.gov), and contract data reports (formerly part of FPDS.gov).\r\nView and submit BioPreferred and Service Contract Reports, Access publicly available award data via data extracts and system accounts."
+                    "title": "System for Award Management (SAM) Public Extract - Exclusions"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://inventory.data.gov/dataset/7416a2e4-9aa7-4bcd-801c-20f25a545916/resource/78bb6c57-42e8-4055-931d-928ebcbde39f/download/samexclusionspublicextract-gsa-1626.csv",
+                    "description": "CSV file containing SAM Exclusions Public Extract",
                     "format": "csv",
-                    "title": "SAM_Exclusions_Public_Extract GSA-1626",
-                    "description": "CSV file containing SAM Exclusions Public Extract"
+                    "title": "SAM_Exclusions_Public_Extract GSA-1626"
                 }
             ],
+            "identifier": "GSA-1626",
+            "issued": "2006-09-26",
             "keyword": [
                 "Black List",
                 "EPLS",
@@ -6532,51 +6525,52 @@
                 "excluded parties list",
                 "list of exclusions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-12-18",
             "programCode": [
                 "023:015"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "U.S. Governmentwide",
             "theme": [
                 "Federal Acquisition Service Program"
-            ]
+            ],
+            "title": "System for Award Management (SAM) Public Extract - Exclusions"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "e-Buy Awards for Fiscal Year 2010",
-            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
-            "modified": "2016-01-21",
             "accessLevel": "public",
-            "identifier": "GSA-2015-05-18-2",
-            "dataQuality": true,
-            "issued": "2015-05-18",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-08-31",
+            "bureauCode": [
+                "023:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Usha Gopal",
                 "hasEmail": "mailto:usha.gopal@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "e-Buy Awards for Fiscal Year 2010",
                     "description": "Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
-                    "downloadURL": "https://inventory.data.gov/dataset/7a96f2a8-0422-4a4a-884b-3411e1cc7848/resource/6201b0df-4b36-454b-a1a1-02b81e309fe4/download/ebuyawardsfy2010.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/7a96f2a8-0422-4a4a-884b-3411e1cc7848/resource/6201b0df-4b36-454b-a1a1-02b81e309fe4/download/ebuyawardsfy2010.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "e-Buy Awards for Fiscal Year 2010"
                 }
             ],
+            "identifier": "GSA-2015-05-18-2",
+            "isPartOf": "GSA-2015-08-31",
+            "issued": "2015-05-18",
             "keyword": [
                 "Awards",
                 "Contracts",
@@ -6586,39 +6580,38 @@
                 "e-Buy",
                 "procurement"
             ],
-            "bureauCode": [
-                "023:10"
-            ],
-            "programCode": [
-                "023:007"
-            ],
             "language": [
                 "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-21",
+            "programCode": [
+                "023:007"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "e-Buy Awards for Fiscal Year 2010"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Second Generation Office Supplies (OS2) Savings and Small Business Dashboard",
-            "description": "The Second Generation Office Supplies (OS2) Savings and Small Business Dashboard is a graphical depiction of OS2 spend, savings and small business utilization, further highlighting FSSI OS2\u2019s accomplishments on behalf of small businesses, veterans, and the taxpayer. Its easy to use, and provides filters for users to focus on geographical, government agency, small or large business, and SDVOSB specifics.",
-            "modified": "2016-01-07",
             "accessLevel": "public",
-            "identifier": "GSA - 3420",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joshua Daniel Royko",
                 "hasEmail": "mailto:joshua.royko@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The Second Generation Office Supplies (OS2) Savings and Small Business Dashboard is a graphical depiction of OS2 spend, savings and small business utilization, further highlighting FSSI OS2\u2019s accomplishments on behalf of small businesses, veterans, and the taxpayer. Its easy to use, and provides filters for users to focus on geographical, government agency, small or large business, and SDVOSB specifics.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6627,49 +6620,46 @@
                     "title": "Savings and Small Business Dashboard"
                 }
             ],
+            "identifier": "GSA - 3420",
             "keyword": [
                 "FSSI",
                 "OS2",
                 "Office Supplies",
                 "Strategic Sourcing"
             ],
-            "bureauCode": [
-                "023:10"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-07",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "Second Generation Office Supplies (OS2) Savings and Small Business Dashboard"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Acquisition Service Instructional Letter 2010",
-            "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.  All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
-            "modified": "2020-12-22",
             "accessLevel": "public",
-            "identifier": "GSA-6368",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/fas-il/IL_01_data_dictionary.html",
-            "issued": "2011-01-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-09-14-02",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David W Orcutt",
                 "hasEmail": "mailto:david.orcutt@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/fas-il/IL_01_data_dictionary.html",
+            "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.  All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6680,381 +6670,384 @@
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://inventory.data.gov/dataset/8401eca3-0636-4671-b250-938b36232681/resource/18dbf229-ea0e-4177-9162-5742a29abb79/download/fas-instructional-letter-il-2010-01.pdf",
+                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
                     "format": "pdf",
-                    "title": "FAS IL 2010-01",
-                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts."
+                    "title": "FAS IL 2010-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2010-02",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/8401eca3-0636-4671-b250-938b36232681/resource/9ee81071-578f-4a44-a55f-184037382f09/download/fas-instructional-letter-il-2010-02.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/8401eca3-0636-4671-b250-938b36232681/resource/9ee81071-578f-4a44-a55f-184037382f09/download/fas-instructional-letter-il-2010-02.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2010-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://inventory.data.gov/dataset/8401eca3-0636-4671-b250-938b36232681/resource/9519df7f-796f-4034-8a3e-d0653f00ee39/download/fas-instructional-letter-2010-03.pdf",
+                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
                     "format": "pdf",
-                    "title": "FAS IL 2010-03",
-                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts."
+                    "title": "FAS IL 2010-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://inventory.data.gov/dataset/8401eca3-0636-4671-b250-938b36232681/resource/d845399c-3fe5-4cce-a052-484456f999c7/download/fas-instructional-letter-2010-04.pdf",
+                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
                     "format": "pdf",
-                    "title": "FAS IL 2010-04",
-                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts."
+                    "title": "FAS IL 2010-04"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://inventory.data.gov/dataset/8401eca3-0636-4671-b250-938b36232681/resource/7ef3b63b-3c8c-41d1-9c88-33fb7b049ff7/download/fas-instructional-letter-2010-05.pdf",
+                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
                     "format": "pdf",
-                    "title": "FAS IL 2010-05",
-                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts."
+                    "title": "FAS IL 2010-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://inventory.data.gov/dataset/8401eca3-0636-4671-b250-938b36232681/resource/96a7111a-77ce-4ca7-a4d8-056017a48aa3/download/fas-instructional-letter-2010-06.pdf",
+                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
                     "format": "pdf",
-                    "title": "FAS IL 2010-06",
-                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts."
+                    "title": "FAS IL 2010-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://inventory.data.gov/dataset/8401eca3-0636-4671-b250-938b36232681/resource/d6b366bb-1fc2-40b6-a8b0-7ad177f1d6cf/download/fas-instructional-letter-2010-07.pdf",
+                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
                     "format": "pdf",
-                    "title": "FAS IL 2010-07",
-                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts."
+                    "title": "FAS IL 2010-07"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2010-08",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/8401eca3-0636-4671-b250-938b36232681/resource/3704f43a-6ff7-4bac-bcaf-5081ea012783/download/fas-instructional-letter-il-2010-08.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/8401eca3-0636-4671-b250-938b36232681/resource/3704f43a-6ff7-4bac-bcaf-5081ea012783/download/fas-instructional-letter-il-2010-08.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2010-08"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2010-09 Supplemental",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/8401eca3-0636-4671-b250-938b36232681/resource/610fd1ec-468a-4d4c-a5ef-4d528c78fe0f/download/fas-instructional-letter-il-2010-09-supplement.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/8401eca3-0636-4671-b250-938b36232681/resource/610fd1ec-468a-4d4c-a5ef-4d528c78fe0f/download/fas-instructional-letter-il-2010-09-supplement.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2010-09 Supplemental"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://inventory.data.gov/dataset/8401eca3-0636-4671-b250-938b36232681/resource/1e1b9307-a8e4-47db-bf04-0340a5ee3c8e/download/instruction-letter-il-2010-07-supplement.pdf",
+                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
                     "format": "pdf",
-                    "title": "FAS IL 2010-07 Supplemental",
-                    "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts."
+                    "title": "FAS IL 2010-07 Supplemental"
                 }
             ],
+            "identifier": "GSA-6368",
+            "isPartOf": "GSA-2015-09-14-02",
+            "issued": "2011-01-01",
             "keyword": [
                 "FAS",
                 "Industrial Funding Fee",
                 "Instructional Letters",
                 "Interactive"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-22",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "United States",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "Federal Acquisition Service Instructional Letter 2010"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Acquisition Service Instructional Letter 2011",
-            "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.  All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
-            "modified": "2020-12-30",
             "accessLevel": "public",
-            "identifier": "GSA-6369",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/fas-il/IL_01_data_dictionary.html",
-            "issued": "2012-01-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-09-14-02",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David W Orcutt",
                 "hasEmail": "mailto:david.orcutt@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/fas-il/IL_01_data_dictionary.html",
+            "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.  All ILs are current only as of the date posted and are subject to amendment, update, and supersession without further notice being posted on this site. Changes and revisions to regulatory or statutory guidance subsequent to the effective date of this IL may affect its relevancy and accurateness. The IL is provided for informational purposes only.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-01-Supplemental",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/096719f8-c297-4e6d-8137-6a2d1ae18e3e/download/fas-il-2011-01-supplement.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/096719f8-c297-4e6d-8137-6a2d1ae18e3e/download/fas-il-2011-01-supplement.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-01-Supplemental"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-01",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/e4de071e-f4fe-44cd-90e5-ad43f99e3556/download/fas-il-2011-01.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/e4de071e-f4fe-44cd-90e5-ad43f99e3556/download/fas-il-2011-01.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-03",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/d07b44fd-7b33-4bac-8af7-6ce4950dc8f0/download/fas-il-2011-03.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/d07b44fd-7b33-4bac-8af7-6ce4950dc8f0/download/fas-il-2011-03.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-03"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-04",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/6fb955cd-4917-46af-b298-e8f4656f487b/download/fas-il-2011-04.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/6fb955cd-4917-46af-b298-e8f4656f487b/download/fas-il-2011-04.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-04"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-05",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/bf495425-9ec3-4842-aadd-f4ebd298b758/download/fas-il-2011-05.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/bf495425-9ec3-4842-aadd-f4ebd298b758/download/fas-il-2011-05.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-06",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/d51987e2-2736-4faf-8512-f40f03cbe92e/download/fas-il-2011-06.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/d51987e2-2736-4faf-8512-f40f03cbe92e/download/fas-il-2011-06.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-06"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-06-Supplemental",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/ae2a362f-e331-4636-889e-8700fde3e479/download/fas-il-2011-06-supplement.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/ae2a362f-e331-4636-889e-8700fde3e479/download/fas-il-2011-06-supplement.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-06-Supplemental"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-07",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/ed395edb-6038-45de-a8ff-efe13cdcf28b/download/fas-il-2011-07.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/ed395edb-6038-45de-a8ff-efe13cdcf28b/download/fas-il-2011-07.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-07"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-08",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/5594bef8-2aa8-45bb-85b3-97fae53eeb0b/download/fas-il-2011-08.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/5594bef8-2aa8-45bb-85b3-97fae53eeb0b/download/fas-il-2011-08.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-08"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-09",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/04bfaed9-bc5f-4374-a1eb-71d813fef4b8/download/fas-il-2011-09.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/04bfaed9-bc5f-4374-a1eb-71d813fef4b8/download/fas-il-2011-09.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-09"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-10",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/112d6789-17c2-4ad0-ab14-4a9b053981b4/download/fas-il-2011-10.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/112d6789-17c2-4ad0-ab14-4a9b053981b4/download/fas-il-2011-10.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-10"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 20011-11",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/066db519-bd26-4236-9c35-22a824b3c4cc/download/fas-il-2011-11.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/066db519-bd26-4236-9c35-22a824b3c4cc/download/fas-il-2011-11.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 20011-11"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-12",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/125b8c12-df70-4aa2-8925-2fcd268213d5/download/fas-il-2011-12.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/125b8c12-df70-4aa2-8925-2fcd268213d5/download/fas-il-2011-12.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-12"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-12-Supplemental",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/4890a3c2-e1fb-4376-8144-a8ae60bf0ac5/download/fas-il-2011-12-supplement.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/4890a3c2-e1fb-4376-8144-a8ae60bf0ac5/download/fas-il-2011-12-supplement.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-12-Supplemental"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-13",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/cefcc7aa-866a-491d-93d7-5820a3ea7a4c/download/fas-il-2011-13.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/cefcc7aa-866a-491d-93d7-5820a3ea7a4c/download/fas-il-2011-13.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-13"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-14",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/05415a1b-1878-4e5c-986f-17561328fe7e/download/fas-il-2011-13-supplement.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/05415a1b-1878-4e5c-986f-17561328fe7e/download/fas-il-2011-13-supplement.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-14"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-15",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/e9395971-07ac-4753-bb12-b12f7284d2a4/download/fas-il-2011-15.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/e9395971-07ac-4753-bb12-b12f7284d2a4/download/fas-il-2011-15.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-15-Supplemental",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/e25c790c-09f7-4b5e-b4f1-5d0f10887270/download/fas-il-2011-15-supplement.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/e25c790c-09f7-4b5e-b4f1-5d0f10887270/download/fas-il-2011-15-supplement.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-15-Supplemental"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-16-Revised",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/9b2b0136-2a83-414f-a81e-b18dddec5fcd/download/fas-il-2011-16-revised.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/9b2b0136-2a83-414f-a81e-b18dddec5fcd/download/fas-il-2011-16-revised.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-16-Revised"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-17",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/312f2ddc-c9ef-48c7-8128-eff1e6443b46/download/fas-il-2011-17.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/312f2ddc-c9ef-48c7-8128-eff1e6443b46/download/fas-il-2011-17.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-17"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-18",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/123d0cc7-c52d-4461-8a1f-8bd091d68f64/download/fas-il-2011-18.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/123d0cc7-c52d-4461-8a1f-8bd091d68f64/download/fas-il-2011-18.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-18"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-19",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/3f9fd9ba-5d07-462d-a6db-9944932354be/download/fas-il-2011-19.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/3f9fd9ba-5d07-462d-a6db-9944932354be/download/fas-il-2011-19.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-19"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-20",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/8f7b7cb7-a2d0-4026-85d3-7f5ab90cd2f3/download/fas-il-2011-20.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/8f7b7cb7-a2d0-4026-85d3-7f5ab90cd2f3/download/fas-il-2011-20.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-20"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-24",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/ccb366d0-c7fa-4536-a759-576a0b0fb1d5/download/fas-il-2011-24.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/ccb366d0-c7fa-4536-a759-576a0b0fb1d5/download/fas-il-2011-24.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-24"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "Table of Contents FAS IL 2011",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/14ed7d4d-ce95-4fbf-812c-906652a43cda/download/table-of-contents-fas-il-2011.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/14ed7d4d-ce95-4fbf-812c-906652a43cda/download/table-of-contents-fas-il-2011.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table of Contents FAS IL 2011"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "FAS IL 2011-13-Supplemental",
                     "description": "The GSA Federal Acquisition Service Instructional Letters (ILs) - guidance issued to internal FAS acquisition personnel that generally requires action as a result of a regulatory or programmatic change, e.g. inserting a new clause into solicitations and contracts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/91598bea-83b3-4ec2-8a8f-ff2df116cd0a/download/fas-il-2011-13-supplement.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/bdf29013-5d2e-4aeb-8604-24c2b1e29940/resource/91598bea-83b3-4ec2-8a8f-ff2df116cd0a/download/fas-il-2011-13-supplement.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FAS IL 2011-13-Supplemental"
                 }
             ],
+            "identifier": "GSA-6369",
+            "isPartOf": "GSA-2015-09-14-02",
+            "issued": "2012-01-01",
             "keyword": [
                 "FAS",
                 "Industrial Funding Fee",
                 "Instructional Letters",
                 "Interactive"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-30",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "Federal Acquisition Service Instructional Letter 2011"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "NAICS Matrix for Active GSA Schedules and GSA GWACs",
-            "description": "The Product Service Codes (PSC) and North American Industrial Classification Systems (NAICS) are the two methods that the Federal government classifies contracts.  They are used as a mechanism to identify scope of the products and services and business segment covered under the award.  This data can be used as a mechanism to understand the scope of GSA programs.  This can be used as means to identify best fit.  While a GSA contract can offer great opportunities for many businesses, the process of applying for that contract will take a significant amount of time and resources. Understanding best GSA contract for your products and services is a preliminary step to take prior to responding to a GSA solicitation.",
-            "modified": "2011-03-30",
             "accessLevel": "public",
-            "identifier": "GSA-4724",
-            "dataQuality": true,
-            "describedBy": "https://www.asap.gsa.gov/datagov/naics/NAICS_Schedule_GWAC_Matrix_Dictionary.html",
-            "issued": "2011-03-30",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "domestic and international",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daniel Twomey",
                 "hasEmail": "mailto:daniel.twomey@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.asap.gsa.gov/datagov/naics/NAICS_Schedule_GWAC_Matrix_Dictionary.html",
+            "description": "The Product Service Codes (PSC) and North American Industrial Classification Systems (NAICS) are the two methods that the Federal government classifies contracts.  They are used as a mechanism to identify scope of the products and services and business segment covered under the award.  This data can be used as a mechanism to understand the scope of GSA programs.  This can be used as means to identify best fit.  While a GSA contract can offer great opportunities for many businesses, the process of applying for that contract will take a significant amount of time and resources. Understanding best GSA contract for your products and services is a preliminary step to take prior to responding to a GSA solicitation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://www.asap.gsa.gov/datagov/naics/NAICS_Matrix_for_Active_GSA_Schedules_and_GSA_GWACs.xls",
                     "format": "xls",
-                    "title": "NAICS Matrix for Active GSA Schedules and GSA GWACs",
-                    "downloadURL": "https://www.asap.gsa.gov/datagov/naics/NAICS_Matrix_for_Active_GSA_Schedules_and_GSA_GWACs.xls"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NAICS Matrix for Active GSA Schedules and GSA GWACs"
                 }
             ],
+            "identifier": "GSA-4724",
+            "issued": "2011-03-30",
             "keyword": [
                 "BPA",
                 "Blanket Purchase Agreement",
@@ -7069,101 +7062,101 @@
                 "North American Industry Classification System",
                 "Schedules"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2011-03-30",
             "programCode": [
                 "023:000"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "domestic and international",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "NAICS Matrix for Active GSA Schedules and GSA GWACs"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Schedule Sales Query Report Generation System",
-            "description": "Schedule Sales Query presents sales volume figures as reported to GSA by contractors. The reports are generated as quarterly reports for the current year and the past five fiscal years. The sales data reported here are updated as contractors' reports are received, but the data may not be up to date as adjustments can be received at any time. The information on this site mirrors the data used by GSA for contract administration and fee management. It is not the official source of sales data. This data should be used for informational purposes only.",
-            "modified": "2016-01-07",
             "accessLevel": "public",
-            "identifier": "GSA-2641",
-            "dataQuality": true,
-            "describedBy": "http://www.gsa.gov/portal/content/104236",
-            "issued": "2009-02-19",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Usha Gopal",
                 "hasEmail": "mailto:usha.gopal@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.gsa.gov/portal/content/104236",
+            "description": "Schedule Sales Query presents sales volume figures as reported to GSA by contractors. The reports are generated as quarterly reports for the current year and the past five fiscal years. The sales data reported here are updated as contractors' reports are received, but the data may not be up to date as adjustments can be received at any time. The information on this site mirrors the data used by GSA for contract administration and fee management. It is not the official source of sales data. This data should be used for informational purposes only.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "http://ssq.gsa.gov",
                     "format": "text/html",
-                    "title": "Schedule Sales Query Report Generation System",
-                    "downloadURL": "http://ssq.gsa.gov"
+                    "mediaType": "text/html",
+                    "title": "Schedule Sales Query Report Generation System"
                 }
             ],
+            "identifier": "GSA-2641",
+            "issued": "2009-02-19",
             "keyword": [
                 "GSA contract administration and fee management",
                 "Schedule Sales Query",
                 "sales data report",
                 "sales volume figures"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-07",
             "programCode": [
                 "023:014"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "Other"
-            ]
+            ],
+            "title": "Schedule Sales Query Report Generation System"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Time to Hire",
-            "description": "This dataset represents time taken to hire a GSA employee from the internal request to hire through the entry on duty of the of the selected individual",
-            "modified": "2016-01-07",
             "accessLevel": "public",
-            "identifier": "GSA-1375",
-            "dataQuality": true,
-            "issued": "2010-01-15",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "023:30"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dawn R Smith",
                 "hasEmail": "mailto:dawn.smith@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "This dataset represents time taken to hire a GSA employee from the internal request to hire through the entry on duty of the of the selected individual",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://inventory.data.gov/dataset/58fa1cd3-c1bf-4492-964d-f994b26a6cae/resource/f6d8dd83-3080-470f-b453-03f8ead0228f/download/time-to-hire-data-file.xlsx",
                     "format": "xlsx",
-                    "title": "Time to Hire",
-                    "downloadURL": "https://inventory.data.gov/dataset/58fa1cd3-c1bf-4492-964d-f994b26a6cae/resource/f6d8dd83-3080-470f-b453-03f8ead0228f/download/time-to-hire-data-file.xlsx"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Time to Hire"
                 }
             ],
+            "identifier": "GSA-1375",
+            "issued": "2010-01-15",
             "keyword": [
                 "Application",
                 "Employment",
@@ -7173,133 +7166,134 @@
                 "USAJobs",
                 "Vacancy"
             ],
-            "bureauCode": [
-                "023:30"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-07",
             "programCode": [
                 "023:009"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
+            "spatial": "National",
             "theme": [
                 "People"
-            ]
+            ],
+            "title": "Time to Hire"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Bureau IT Leadership Directory",
-            "description": "Json file for Bureau IT Leadership Directory",
-            "modified": "2015-09-01",
             "accessLevel": "public",
-            "identifier": "GSA-2015-09-01-02",
-            "dataQuality": true,
-            "issued": "2015-09-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jonah M Hatfield",
                 "hasEmail": "mailto:jonah.hatfield@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Json file for Bureau IT Leadership Directory",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://www.gsa.gov/largedocs/bureaudirectory.json",
+                    "description": "Json file for Bureau IT Leadership",
                     "format": "json",
-                    "title": "Bureau IT Leadership",
-                    "description": "Json file for Bureau IT Leadership"
+                    "title": "Bureau IT Leadership"
                 }
             ],
+            "identifier": "GSA-2015-09-01-02",
+            "issued": "2015-09-01",
             "keyword": [
                 "Bureau",
                 "IT",
                 "Leadership"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2015-09-01",
             "programCode": [
                 "023:014"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Json file"
-            ]
+            ],
+            "title": "Bureau IT Leadership Directory"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2015, 3rd Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
             "accessLevel": "public",
-            "identifier": "GSA-2015-05-09-09",
-            "dataQuality": true,
-            "issued": "2015-05-18",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xlsx",
-                    "title": "Networx Business Volume FY15 3rd Quarter",
                     "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/44bff510-9e9d-4910-8e3f-da64a53f4680/resource/d881a4dd-9cc7-4c8e-86da-bde870f60444/download/networx-fy15-3rdqtr.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/44bff510-9e9d-4910-8e3f-da64a53f4680/resource/d881a4dd-9cc7-4c8e-86da-bde870f60444/download/networx-fy15-3rdqtr.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Networx Business Volume FY15 3rd Quarter"
                 }
             ],
+            "identifier": "GSA-2015-05-09-09",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-05-18",
             "keyword": [
                 "Networx Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Telecommunications Services"
-            ]
+            ],
+            "title": "Networx Business Volume FY2015, 3rd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Concur Travel Parent",
-            "description": "This is the Parent folder for Concur datasets reporting on; Closed-Paid Vouchers in Concur Government Edition (CGE), Authorization Model, Travel Model, User Profile, and Voucher Model.",
-            "modified": "2016-02-23",
             "accessLevel": "non-public",
-            "identifier": "GSA-2015-09-11-01",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Norma H Tolson",
                 "hasEmail": "mailto:norma.tolson@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "This is the Parent folder for Concur datasets reporting on; Closed-Paid Vouchers in Concur Government Edition (CGE), Authorization Model, Travel Model, User Profile, and Voucher Model.",
+            "identifier": "GSA-2015-09-11-01",
             "keyword": [
                 "Authorization",
                 "Closed",
@@ -7308,39 +7302,39 @@
                 "Travel",
                 "Voucher"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-02-23",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
             "theme": [
                 "Travel and Transportation"
-            ]
+            ],
+            "title": "Concur Travel Parent"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Data.gov Statistics Parent",
-            "description": "Various reports regarding the Data.gov sites, from Daily Visitors, to Top 10 Countries, and States.",
-            "modified": "2015-09-14",
             "accessLevel": "public",
-            "identifier": "GSA-2015-09-14-01",
-            "dataQuality": true,
-            "issued": "2013-04-11",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "Worldwide",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Joo Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Various reports regarding the Data.gov sites, from Daily Visitors, to Top 10 Countries, and States.",
+            "identifier": "GSA-2015-09-14-01",
+            "issued": "2013-04-11",
             "keyword": [
                 "Countries",
                 "States",
@@ -7348,345 +7342,345 @@
                 "Visitors",
                 "data.gov"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2015-09-14",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "spatial": "Worldwide",
             "theme": [
                 "Data.gov Site"
-            ]
+            ],
+            "title": "Data.gov Statistics Parent"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "FAS Parent",
-            "description": "This contains the Federal Acquisition Service collection of Instructional Letters and Scorecards.",
-            "modified": "2015-09-14",
             "accessLevel": "public",
-            "identifier": "GSA-2015-09-14-02",
-            "dataQuality": true,
-            "issued": "2015-09-14",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David W Orcutt",
                 "hasEmail": "mailto:david.orcutt@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "This contains the Federal Acquisition Service collection of Instructional Letters and Scorecards.",
+            "identifier": "GSA-2015-09-14-02",
+            "issued": "2015-09-14",
             "keyword": [
                 "Acquisition",
                 "Balanced Scorecard",
                 "FAS",
                 "Instructional Letters"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2015-09-14",
             "programCode": [
                 "023:007"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "spatial": "National",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "FAS Parent"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Subcontracting Directory for Small Businesses",
-            "description": "The GSA Subcontracting Directory list large Prime Contractors who, by law, are required to establish plans and goals for subcontracting with Small Business Firms.",
-            "modified": "2024-08-08T14:21:26.352Z",
             "accessLevel": "public",
-            "identifier": "GSA-2015-10-26-01",
-            "dataQuality": true,
-            "describedBy": "https://www.gsa.gov/small-business/register-your-business/subcontracting-and-other-partnerships",
-            "describedByType": "text/csv",
-            "issued": "2012-12-06",
-            "landingPage": "https://www.gsa.gov/small-business/register-your-business/subcontracting-and-other-partnerships",
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Carena Jackson",
                 "hasEmail": "mailto:carena.jackson@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.gsa.gov/small-business/register-your-business/subcontracting-and-other-partnerships",
+            "describedByType": "text/csv",
+            "description": "The GSA Subcontracting Directory list large Prime Contractors who, by law, are required to establish plans and goals for subcontracting with Small Business Firms.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/50bfccab-460c-4f18-9f17-28c4104e6d50/resource/d1c957f9-f38c-414f-a695-ad4ec7781f94/download/subk-directory-as-of-07112024-filtered-subk-directory-v3.csv",
                     "mediaType": "text/csv",
-                    "title": "Subk Directory as of 07112024 Filtered - subk directory v3.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/50bfccab-460c-4f18-9f17-28c4104e6d50/resource/d1c957f9-f38c-414f-a695-ad4ec7781f94/download/subk-directory-as-of-07112024-filtered-subk-directory-v3.csv"
+                    "title": "Subk Directory as of 07112024 Filtered - subk directory v3.csv"
                 }
             ],
+            "identifier": "GSA-2015-10-26-01",
+            "issued": "2012-12-06",
             "keyword": [
                 "NAICS",
                 "Prime Contractors",
                 "Subcontracting",
                 "Subcontracting Directory"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.gsa.gov/small-business/register-your-business/subcontracting-and-other-partnerships",
+            "language": [
+                "us-EN"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-08T14:21:26.352Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "true",
             "theme": [
                 "Directory"
-            ]
+            ],
+            "title": "Subcontracting Directory for Small Businesses"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Auctions API",
-            "description": "GSA Auctions offers Federal personal property assets ranging from common place items (such as office equipment and furniture) to more select products like scientific equipment, heavy machinery, airplanes, vessels and vehicles. GSA Auctions\u2019 online capabilities allow GSA to offer assets located across the country to any interested buyer, regardless of location.    Build your own tools using our API to access GSA Auctions listings.  The Auctions API is a GET API which has currently one operation. The operation will retrieve GSA Auctions data.  The output data will be in XML and JSON format. These files are downloadable.  The data in the API output file is live data.",
-            "modified": "2018-09-24",
             "accessLevel": "public",
-            "identifier": "GSA-2015-11-09-01",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "National",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "023:30"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Cindy A Smith",
                 "hasEmail": "mailto:cindya.smith@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "GSA Auctions offers Federal personal property assets ranging from common place items (such as office equipment and furniture) to more select products like scientific equipment, heavy machinery, airplanes, vessels and vehicles. GSA Auctions\u2019 online capabilities allow GSA to offer assets located across the country to any interested buyer, regardless of location.    Build your own tools using our API to access GSA Auctions listings.  The Auctions API is a GET API which has currently one operation. The operation will retrieve GSA Auctions data.  The output data will be in XML and JSON format. These files are downloadable.  The data in the API output file is live data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
-                    "format": "json",
-                    "title": "Auctions API",
                     "description": "GSA Auctions API is a public GET API. The Auction listings will be delivered to the user in two formats. One is JSON and the other one is XML. The auction listings delivered thru the API contains the auction listings from all the participating agencies.\r\n\r\nThe output data will be in XML and JSON format. These files are downloadable.  The data in the API output file is live data.",
-                    "downloadURL": "http://gsa.github.io/auctions_api/"
+                    "downloadURL": "http://gsa.github.io/auctions_api/",
+                    "format": "json",
+                    "mediaType": "application/json",
+                    "title": "Auctions API"
                 }
             ],
+            "identifier": "GSA-2015-11-09-01",
             "keyword": [
                 "API",
                 "Assets",
                 "Auctions",
                 "Federal Personal Property"
             ],
-            "bureauCode": [
-                "023:30"
+            "language": [
+                "us-en"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-09-24",
             "programCode": [
                 "023:009"
             ],
-            "language": [
-                "us-en"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "spatial": "National",
             "theme": [
                 "Auctions"
-            ]
+            ],
+            "title": "Auctions API"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Data.gov CKAN API",
-            "description": "The data.gov catalog is powered by CKAN, a powerful open source data platform that includes a robust API.  Please be aware that data.gov and the data.gov CKAN API only contain metadata about datasets.  This metadata includes URLs and descriptions of datasets, but it does not include the actual data within each dataset.",
-            "modified": "2018-09-24",
             "accessLevel": "public",
-            "identifier": "GSA-2015-11-09-02",
-            "dataQuality": true,
-            "landingPage": "https://www.data.gov/developers/harvesting",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Data.gov",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Technology Transformation Service",
-                    "subOrganizationOf": {
-                        "@type": "org:Organization",
-                        "name": "General Services Administration"
-                    }
-                }
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Kim",
                 "hasEmail": "mailto:datagov@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The data.gov catalog is powered by CKAN, a powerful open source data platform that includes a robust API.  Please be aware that data.gov and the data.gov CKAN API only contain metadata about datasets.  This metadata includes URLs and descriptions of datasets, but it does not include the actual data within each dataset.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://www.data.gov/developers/apis",
+                    "description": "This metadata includes URLs and descriptions of datasets, but it does not include the actual data within each dataset.",
                     "format": "JSON",
-                    "title": "Data.gov CKAN API",
-                    "description": "This metadata includes URLs and descriptions of datasets, but it does not include the actual data within each dataset."
+                    "title": "Data.gov CKAN API"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/gzip",
-                    "format": "JSON",
-                    "title": "Government-wide open data metadata bulk download",
                     "description": "This provides a bulk extract of all metadata stored in Data.gov for Federal datasets. The file is automatically generated monthly as an export from the CKAN API using the JSON Lines serialization format (jsonlines.org). This does not provide all metadata stored on Data.gov, only metadata for Federal datasets following the metadata guidelines described at http://www.digitalgov.gov/resources/how-to-get-your-open-data-on-data-gov/ \r\n\r\nThe compressed file is approximately 2.3GB.",
-                    "downloadURL": "https://filestore.data.gov/gsa/catalog/jsonl/dataset.jsonl.gz"
+                    "downloadURL": "https://filestore.data.gov/gsa/catalog/jsonl/dataset.jsonl.gz",
+                    "format": "JSON",
+                    "mediaType": "application/gzip",
+                    "title": "Government-wide open data metadata bulk download"
                 }
             ],
+            "identifier": "GSA-2015-11-09-02",
             "keyword": [
                 "API",
                 "CKAN",
                 "DATA",
                 "GOV"
             ],
-            "bureauCode": [
-                "023:00"
+            "landingPage": "https://www.data.gov/developers/harvesting",
+            "language": [
+                "us-en"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-09-24",
             "programCode": [
                 "023:014"
             ],
-            "language": [
-                "us-en"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Data.gov",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Technology Transformation Service",
+                    "subOrganizationOf": {
+                        "@type": "org:Organization",
+                        "name": "General Services Administration"
+                    }
+                }
+            },
             "theme": [
                 "API"
-            ]
+            ],
+            "title": "Data.gov CKAN API"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Enterprise Data Inventory (EDI)",
-            "description": "GSA Enterprise Data Inventory (EDI)",
-            "modified": "2022-08-01T13:35:22.951Z",
             "accessLevel": "public",
-            "identifier": "GSA-2015-11-13-01",
-            "dataQuality": true,
-            "describedByType": "application/json",
-            "issued": "2015-11-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Morgan L Redden",
                 "hasEmail": "mailto:morgan.redden@gsa.gov"
             },
+            "dataQuality": true,
+            "describedByType": "application/json",
+            "description": "GSA Enterprise Data Inventory (EDI)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/acf8e47e-24d2-4e4d-a786-847643f101fd/resource/0437517d-4fbd-43eb-8453-76ece7f562a8/download/1.27.25data.json",
                     "mediaType": "application/json",
-                    "title": "1.27.25data.json",
-                    "downloadURL": "https://inventory.data.gov/dataset/acf8e47e-24d2-4e4d-a786-847643f101fd/resource/0437517d-4fbd-43eb-8453-76ece7f562a8/download/1.27.25data.json"
+                    "title": "1.27.25data.json"
                 }
             ],
+            "identifier": "GSA-2015-11-13-01",
+            "issued": "2015-11-13",
             "keyword": [
                 "EDI",
                 "Enterprise Data Inventory",
                 "GSA EDI",
                 "JSON"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-08-01T13:35:22.951Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2015, 4th Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
-            "accessLevel": "public",
-            "identifier": "GSA-2015-11-16-01",
-            "dataQuality": true,
-            "issued": "2015-11-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "rights": "true",
+            "title": "GSA Enterprise Data Inventory (EDI)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xlsx",
-                    "title": "Networx Business Volume FY15 4th Quarter",
                     "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/18eab5fe-9bbf-4ca5-88d7-f71885052d0c/resource/5e3f57e5-ad4b-4ab0-8628-1508199cacb4/download/networx-business-volume-fy15-4th-quarter.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/18eab5fe-9bbf-4ca5-88d7-f71885052d0c/resource/5e3f57e5-ad4b-4ab0-8628-1508199cacb4/download/networx-business-volume-fy15-4th-quarter.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Networx Business Volume FY15 4th Quarter"
                 }
             ],
+            "identifier": "GSA-2015-11-16-01",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-11-13",
             "keyword": [
                 "Contract",
                 "Networx Telecommunications",
                 "Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Telecommunications Services"
-            ]
+            ],
+            "title": "Networx Business Volume FY2015, 4th Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA IT Reform Cost Savings/Avoidance",
-            "description": "GSA IT provides data related to Agency IT initiatives that save or avoid expenditures.  This data is provided as a requirement of OMB's Integrated Data Collection (IDC) and posted publicly as a requirement of the Federal Information Technology Acquisition Reform Act (FITARA) leglislation.",
-            "modified": "2024-08-19T15:39:58.340Z",
             "accessLevel": "public",
-            "identifier": "GSA-2015-11-25-01",
-            "issued": "2015-11-25",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alexandria Smith",
                 "hasEmail": "mailto:Alexandria.Smith@gsa.gov"
             },
+            "description": "GSA IT provides data related to Agency IT initiatives that save or avoid expenditures.  This data is provided as a requirement of OMB's Integrated Data Collection (IDC) and posted publicly as a requirement of the Federal Information Technology Acquisition Reform Act (FITARA) leglislation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
-                    "format": "JSON",
-                    "title": "GSA IT Reform Cost Savings/Avoidance",
-                    "description": "GSA's November 2024 Cost Savings/Avoidance submission to satisfy the requirements set forth in OMB's Integrated Data Collection.",
                     "conformsTo": "https://management.cio.gov/schemaexamples/costSavingsAvoidanceSchema.json",
-                    "downloadURL": "https://inventory.data.gov/dataset/57f52388-9b32-4069-925f-e0de9c5c6ea4/resource/87eb8833-7abb-432b-a272-e611c0aff04a/download/gsaitcostsavingsavoidance20151125.json"
+                    "description": "GSA's November 2024 Cost Savings/Avoidance submission to satisfy the requirements set forth in OMB's Integrated Data Collection.",
+                    "downloadURL": "https://inventory.data.gov/dataset/57f52388-9b32-4069-925f-e0de9c5c6ea4/resource/87eb8833-7abb-432b-a272-e611c0aff04a/download/gsaitcostsavingsavoidance20151125.json",
+                    "format": "JSON",
+                    "mediaType": "application/json",
+                    "title": "GSA IT Reform Cost Savings/Avoidance"
                 }
             ],
+            "identifier": "GSA-2015-11-25-01",
+            "issued": "2015-11-25",
             "keyword": [
                 "GSA IT",
                 "GSA IT reform cost savings",
@@ -7694,415 +7688,415 @@
                 "cost savings",
                 "savings"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0",
+            "modified": "2024-08-19T15:39:58.340Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "true",
             "theme": [
                 "IT Initiatives"
-            ]
+            ],
+            "title": "GSA IT Reform Cost Savings/Avoidance"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions Parent",
-            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
-            "modified": "2018-07-25",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-05-01",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
+            "identifier": "GSA-2016-01-05-01",
             "keyword": [
                 "p-card",
                 "purchase card",
                 "purchase card transactions",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-07-25",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions Parent"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions Apr-June 2014, 3rd Qtr",
-            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-05-6",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xlsx",
-                    "title": "April June 2014 PC Transactions",
                     "description": "Purchases made with the purchase card.",
-                    "downloadURL": "https://inventory.data.gov/dataset/a554234f-cf00-4a02-8fed-e333580660fd/resource/a01a43ad-5302-4558-ba24-2c9872f1d398/download/april-june-2014-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/a554234f-cf00-4a02-8fed-e333580660fd/resource/a01a43ad-5302-4558-ba24-2c9872f1d398/download/april-june-2014-pc-transactions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "April June 2014 PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-01-05-6",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "p-card",
                 "purchase card",
                 "purchase card transactions",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions Apr-June 2014, 3rd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - Office of  Inspector General Parent",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the Office of the Inspector General.",
-            "modified": "2016-01-05",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-05-9",
-            "dataQuality": true,
-            "issued": "2015-05-21",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daphne Muse",
                 "hasEmail": "mailto:gsaig.alias.daphne.muse@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the Office of the Inspector General.",
+            "identifier": "GSA-2016-01-05-9",
+            "issued": "2015-05-21",
             "keyword": [
                 "Purchase Card"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-05",
             "programCode": [
                 "023:020"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - Office of  Inspector General Parent"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions Apr-June 2015, 3rd Qtr",
-            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-05-2",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://inventory.data.gov/dataset/74a95741-336c-43ce-93e3-820c4074908c/resource/ccef13ed-62c3-4abc-af56-05133ea28e54/download/april-june-2015-pc-transactions.xlsx",
                     "format": "xlsx",
-                    "title": "April June 2015 PC Transactions",
-                    "downloadURL": "https://inventory.data.gov/dataset/74a95741-336c-43ce-93e3-820c4074908c/resource/ccef13ed-62c3-4abc-af56-05133ea28e54/download/april-june-2015-pc-transactions.xlsx"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "April June 2015 PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-01-05-2",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "p-card",
                 "purchase card",
                 "purchase card transactions",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions Apr-June 2015, 3rd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions Jan-Mar 2015, 2nd Qtr",
-            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-05-3",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://inventory.data.gov/dataset/71e0196c-533a-4efc-a878-1f447858b0c3/resource/4a8b8081-eef6-44a3-9840-58f459eb5388/download/january-march-2015-pc-transactions.xlsx",
                     "format": "xlsx",
-                    "title": "January March 2015 PC Transactions",
-                    "downloadURL": "https://inventory.data.gov/dataset/71e0196c-533a-4efc-a878-1f447858b0c3/resource/4a8b8081-eef6-44a3-9840-58f459eb5388/download/january-march-2015-pc-transactions.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "January March 2015 PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-01-05-3",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "p-card",
                 "purchase card",
                 "purchase card transactions",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions Jan-Mar 2015, 2nd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions Jan-Mar 2014, 2nd Qtr",
-            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-05-7",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xlsx",
-                    "title": "January March 2014 PC Transactions",
                     "description": "Purchases made with the purchase card.",
-                    "downloadURL": "https://inventory.data.gov/dataset/a2f142d9-8996-4b2f-8398-bb8c53d33cd8/resource/2f977100-51be-4438-9629-fa984ecb93cc/download/january-march-2014-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/a2f142d9-8996-4b2f-8398-bb8c53d33cd8/resource/2f977100-51be-4438-9629-fa984ecb93cc/download/january-march-2014-pc-transactions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "January March 2014 PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-01-05-7",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "p-card",
                 "purchase card",
                 "purchase card transactions",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions Jan-Mar 2014, 2nd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions Oct-Dec 2013, 1st Qtr",
-            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-05-8",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xlsx",
-                    "title": "October December 2013 PC Transactions",
                     "description": "Purchases made with the purchase card.",
-                    "downloadURL": "https://inventory.data.gov/dataset/414d204b-541f-441d-84c1-68d3f27ed3be/resource/5d54bcd6-f004-4dc3-bf53-3438aa3fb448/download/october-december-2013-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/414d204b-541f-441d-84c1-68d3f27ed3be/resource/5d54bcd6-f004-4dc3-bf53-3438aa3fb448/download/october-december-2013-pc-transactions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "October December 2013 PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-01-05-8",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "p-card",
                 "purchase card",
                 "purchase card transactions",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions Oct-Dec 2013, 1st Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - OIG Oct-Dec 2013, 1st Qtr",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the Office of the Inspector General.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-05-12",
-            "dataQuality": true,
-            "issued": "2015-05-21",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-9",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daphne Muse",
                 "hasEmail": "mailto:gsaig.alias.daphne.muse@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the Office of the Inspector General.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xlsx",
-                    "title": "October December 2013 OIG PC Transactions",
                     "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the Office of the Inspector General.",
-                    "downloadURL": "https://inventory.data.gov/dataset/5f832b05-cdf6-4c63-88f8-d05390a06029/resource/8e9fbfe8-d2b0-4a48-96cd-dc5302c279e0/download/october-december-2013-oig-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/5f832b05-cdf6-4c63-88f8-d05390a06029/resource/8e9fbfe8-d2b0-4a48-96cd-dc5302c279e0/download/october-december-2013-oig-pc-transactions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "October December 2013 OIG PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-01-05-12",
+            "isPartOf": "GSA-2016-01-05-9",
+            "issued": "2015-05-21",
             "keyword": [
                 "Inspector General",
                 "Office of Inspector General",
-                "Purchase Card",
-                "transactions"
-            ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:020"
+                "Purchase Card",
+                "transactions"
             ],
             "language": [
                 "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
+            "programCode": [
+                "023:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - OIG Oct-Dec 2013, 1st Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - Civilian Board of Contract Appeals (CBCA) Parent",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2017-02-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-06-1",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
+            "identifier": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Civilian Board",
@@ -8110,51 +8104,51 @@
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2017-02-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - Civilian Board of Contract Appeals (CBCA) Parent"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA July-Sept 2015, 4th Qtr",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-06-2",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xlsx",
-                    "title": "July September 2015 BOCA PC Transactions",
                     "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-                    "downloadURL": "https://inventory.data.gov/dataset/09ad9d3a-9758-44e1-8e94-19ff8ca13f42/resource/cafc450c-3ab9-41a9-9b5c-16494ed5db68/download/july-september2015-boca-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/09ad9d3a-9758-44e1-8e94-19ff8ca13f42/resource/cafc450c-3ab9-41a9-9b5c-16494ed5db68/download/july-september2015-boca-pc-transactions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "July September 2015 BOCA PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-01-06-2",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Contract Board",
@@ -8162,51 +8156,51 @@
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA July-Sept 2015, 4th Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA  Apr-June 2015, 3rd Qtr",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-06-3",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xlsx",
-                    "title": "April June 2015 BOCA PC Transactions",
                     "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-                    "downloadURL": "https://inventory.data.gov/dataset/284cd4e6-da37-446d-8ca3-79569780f4d5/resource/3d77fead-e5f8-49ad-9d82-0be928ec4abb/download/april-june-2015-boca-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/284cd4e6-da37-446d-8ca3-79569780f4d5/resource/3d77fead-e5f8-49ad-9d82-0be928ec4abb/download/april-june-2015-boca-pc-transactions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "April June 2015 BOCA PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-01-06-3",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Contract Board",
@@ -8214,51 +8208,51 @@
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA  Apr-June 2015, 3rd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA  Jan-Mar 2015, 2nd Qtr",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-06-4",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xlsx",
-                    "title": "January March 2015 BOCA PC Transactions",
                     "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-                    "downloadURL": "https://inventory.data.gov/dataset/163269b9-f474-4a28-a413-d1ac79fc578b/resource/abf3e5e9-fa7a-43e8-9ea6-52e644b7551e/download/january-march-2015-boca-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/163269b9-f474-4a28-a413-d1ac79fc578b/resource/abf3e5e9-fa7a-43e8-9ea6-52e644b7551e/download/january-march-2015-boca-pc-transactions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "January March 2015 BOCA PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-01-06-4",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Contract Board",
@@ -8266,51 +8260,51 @@
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA  Jan-Mar 2015, 2nd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA July-Sept 2014, 4th Qtr",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-06-6",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xlsx",
-                    "title": "July September 2014 BOCA PC Transactions",
                     "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-                    "downloadURL": "https://inventory.data.gov/dataset/c626be85-ca43-4608-b573-fd9bc0006bb2/resource/d0471cb0-ec64-443b-9a56-a2a0bddc5237/download/july-september-2014-boca-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/c626be85-ca43-4608-b573-fd9bc0006bb2/resource/d0471cb0-ec64-443b-9a56-a2a0bddc5237/download/july-september-2014-boca-pc-transactions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "July September 2014 BOCA PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-01-06-6",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Contract Board",
@@ -8318,100 +8312,100 @@
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA July-Sept 2014, 4th Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions Oct-Dec 2014, 1st Qtr",
-            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-05-4",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://inventory.data.gov/dataset/68562ea5-5cbf-49a3-b880-1b64f265139a/resource/4f8ca985-9bc3-41da-96f5-8fa8a2784665/download/october-december-2014-pc-transactions.xlsx",
                     "format": "xlsx",
-                    "title": "October December 2014 PC Transactions",
-                    "downloadURL": "https://inventory.data.gov/dataset/68562ea5-5cbf-49a3-b880-1b64f265139a/resource/4f8ca985-9bc3-41da-96f5-8fa8a2784665/download/october-december-2014-pc-transactions.xlsx"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "October December 2014 PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-01-05-4",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "p-card",
                 "purchase card",
                 "purchase card transactions",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions Oct-Dec 2014, 1st Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA  Oct-Dec 2014, 1st Qtr",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-06-5",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xlsx",
-                    "title": "October December 2014 BOCA PC Transactions",
                     "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-                    "downloadURL": "https://inventory.data.gov/dataset/b9b49662-4f9c-4048-811d-0b024ecb376d/resource/cbe7ccee-aa86-4f39-9f5c-0ca8b9442c68/download/october-december-2014-boca-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/b9b49662-4f9c-4048-811d-0b024ecb376d/resource/cbe7ccee-aa86-4f39-9f5c-0ca8b9442c68/download/october-december-2014-boca-pc-transactions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "October December 2014 BOCA PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-01-06-5",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Contract Board",
@@ -8419,51 +8413,51 @@
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA  Oct-Dec 2014, 1st Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA  Apr-June 2014, 3rd Qtr",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-06-7",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xlsx",
-                    "title": "April June 2014 BOCA PC Transactions",
                     "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-                    "downloadURL": "https://inventory.data.gov/dataset/a1dd6e03-6a27-4177-9f6c-aa59a8e4291f/resource/8a666bdd-a8e5-4f81-8a18-d2ac6ba03a60/download/april-june-2014-boca-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/a1dd6e03-6a27-4177-9f6c-aa59a8e4291f/resource/8a666bdd-a8e5-4f81-8a18-d2ac6ba03a60/download/april-june-2014-boca-pc-transactions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "April June 2014 BOCA PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-01-06-7",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Contract Board",
@@ -8471,51 +8465,51 @@
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA  Apr-June 2014, 3rd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA  Oct-Dec 2013, 1st Qtr",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-06-8",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xlsx",
-                    "title": "October December 2013 BOCA PC Transactions",
                     "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-                    "downloadURL": "https://inventory.data.gov/dataset/46d614e2-dcc6-4d9b-aa61-da4eea26d767/resource/810cb259-0efe-4efd-9490-a94965dc1ab1/download/october-december-2013-boca-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/46d614e2-dcc6-4d9b-aa61-da4eea26d767/resource/810cb259-0efe-4efd-9490-a94965dc1ab1/download/october-december-2013-boca-pc-transactions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "October December 2013 BOCA PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-01-06-8",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Contract Board",
@@ -8523,152 +8517,152 @@
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA  Oct-Dec 2013, 1st Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions July-Sept 2014, 4th Qtr",
-            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-05-5",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xlsx",
-                    "title": "July September 2014 PC Transactions",
                     "description": "Purchases made with purchase card.",
-                    "downloadURL": "https://inventory.data.gov/dataset/c8891019-aef4-4395-a5e4-70c77f2904bf/resource/51c7579d-739d-4f34-8c48-9e00b2eea0ee/download/july-september-2014-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/c8891019-aef4-4395-a5e4-70c77f2904bf/resource/51c7579d-739d-4f34-8c48-9e00b2eea0ee/download/july-september-2014-pc-transactions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "July September 2014 PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-01-05-5",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "p-card",
                 "purchase card",
                 "purchase card transactions",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions July-Sept 2014, 4th Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - OIG Jan-Mar 2014, 2nd Qtr",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the Office of the Inspector General.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-05-11",
-            "dataQuality": true,
-            "issued": "2015-05-21",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-9",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daphne Muse",
                 "hasEmail": "mailto:gsaig.alias.daphne.muse@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the Office of the Inspector General.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xlsx",
-                    "title": "January March 2014 OIG PC Transactions",
                     "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the Office of the Inspector General.",
-                    "downloadURL": "https://inventory.data.gov/dataset/c227f1bd-f127-4da3-92b1-665809646ee5/resource/70a9b97f-6f52-40db-bf95-545f5c809572/download/january-march-2014-oig-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/c227f1bd-f127-4da3-92b1-665809646ee5/resource/70a9b97f-6f52-40db-bf95-545f5c809572/download/january-march-2014-oig-pc-transactions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "January March 2014 OIG PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-01-05-11",
+            "isPartOf": "GSA-2016-01-05-9",
+            "issued": "2015-05-21",
             "keyword": [
                 "Inspector General",
                 "Office of Inspector General",
                 "Purchase Card",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:020"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - OIG Jan-Mar 2014, 2nd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "e-Buy Awards for Fiscal Year 2011",
-            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
-            "modified": "2016-01-21",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-21-1",
-            "dataQuality": true,
-            "issued": "2015-05-18",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-08-31",
+            "bureauCode": [
+                "023:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Usha Gopal",
                 "hasEmail": "mailto:usha.gopal@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "e-Buy Awards for Fiscal Year 2011",
                     "description": "Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
-                    "downloadURL": "https://inventory.data.gov/dataset/dccdec01-d8f8-4c01-aadb-8067d138250d/resource/2bf6b6c0-b196-4c4c-9af3-0e2ca58b897c/download/ebuyawardsfy2011.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/dccdec01-d8f8-4c01-aadb-8067d138250d/resource/2bf6b6c0-b196-4c4c-9af3-0e2ca58b897c/download/ebuyawardsfy2011.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "e-Buy Awards for Fiscal Year 2011"
                 }
             ],
+            "identifier": "GSA-2016-01-21-1",
+            "isPartOf": "GSA-2015-08-31",
+            "issued": "2015-05-18",
             "keyword": [
                 "Awards",
                 "Contracts",
@@ -8678,51 +8672,51 @@
                 "e-Buy",
                 "procurement"
             ],
-            "bureauCode": [
-                "023:10"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-21",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "e-Buy Awards for Fiscal Year 2011"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "e-Buy Awards for Fiscal Year 2012",
-            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
-            "modified": "2016-01-21",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-21-2",
-            "dataQuality": true,
-            "issued": "2015-05-18",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-08-31",
+            "bureauCode": [
+                "023:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Usha Gopal",
                 "hasEmail": "mailto:usha.gopal@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "e-Buy Awards for Fiscal Year 2012",
                     "description": "Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
-                    "downloadURL": "https://inventory.data.gov/dataset/5588754c-253a-4008-9ab1-dd517729a13b/resource/24faaff4-113d-40f8-a4ee-ebe369e4b160/download/ebuyawardsfy2012.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/5588754c-253a-4008-9ab1-dd517729a13b/resource/24faaff4-113d-40f8-a4ee-ebe369e4b160/download/ebuyawardsfy2012.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "e-Buy Awards for Fiscal Year 2012"
                 }
             ],
+            "identifier": "GSA-2016-01-21-2",
+            "isPartOf": "GSA-2015-08-31",
+            "issued": "2015-05-18",
             "keyword": [
                 "Awards",
                 "Contracts",
@@ -8732,51 +8726,51 @@
                 "e-Buy",
                 "procurement"
             ],
-            "bureauCode": [
-                "023:10"
-            ],
-            "programCode": [
-                "023:007"
-            ],
             "language": [
                 "en-us"
             ],
-            "theme": [
-                "Acquisition"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "e-Buy Awards for Fiscal Year 2013",
-            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
-            "modified": "2016-01-21",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-01-21-3",
-            "dataQuality": true,
-            "issued": "2015-05-18",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
+            "modified": "2016-01-21",
+            "programCode": [
+                "023:007"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "rights": "N/A",
+            "theme": [
+                "Acquisition"
+            ],
+            "title": "e-Buy Awards for Fiscal Year 2012"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-08-31",
+            "bureauCode": [
+                "023:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Usha Gopal",
                 "hasEmail": "mailto:usha.gopal@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "e-Buy Awards for Fiscal Year 2013",
                     "description": "Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year",
-                    "downloadURL": "https://inventory.data.gov/dataset/878a56fc-0181-43e7-8c1b-2d8a62de3bcb/resource/ed254f4a-1647-4fcb-a9db-93c2dae6f880/download/ebuyawardsfy2013.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/878a56fc-0181-43e7-8c1b-2d8a62de3bcb/resource/ed254f4a-1647-4fcb-a9db-93c2dae6f880/download/ebuyawardsfy2013.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "e-Buy Awards for Fiscal Year 2013"
                 }
             ],
+            "identifier": "GSA-2016-01-21-3",
+            "isPartOf": "GSA-2015-08-31",
+            "issued": "2015-05-18",
             "keyword": [
                 "Awards",
                 "Contracts",
@@ -8786,48 +8780,49 @@
                 "e-Buy",
                 "procurement"
             ],
-            "bureauCode": [
-                "023:10"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-21",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "e-Buy Awards for Fiscal Year 2013"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "2015 GSA Common Baseline Implementation Plan and CIO Assignment Plan",
-            "description": "This is GSA's 2015 Common Baseline Implementation Plan and its CIO Assignment Plan per the requirements set forth in FITARA legislation.",
-            "modified": "2017-05-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-22-01",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mick Harris",
                 "hasEmail": "mailto:michael.harris@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "This is GSA's 2015 Common Baseline Implementation Plan and its CIO Assignment Plan per the requirements set forth in FITARA legislation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "2015 GSA Common Baseline Implementation Plan and CIO Assignment Plan",
                     "description": "This is GSA's 2015 Common Baseline Implementation Plan and its CIO Assignment Plan per the requirements set forth in FITARA legislation. Updated April 2017. Last Major Change to version updated on March 4, 2019. Last Major change to version update on 8/5/2020. Last Major change to version update on 03/24/2022. Updated on 3/14/23 to add roles of SAOP and CPO to personnel list. Also updated new CTO name and contact info. Updated 5/11/2023 to add acting roles and delegation of authorities link. Updated most recently on 12/11/23 to update AI POC.  MB",
-                    "downloadURL": "https://inventory.data.gov/dataset/64c56cec-4b8f-44c7-ba69-090517f9f32e/resource/87e53999-aff1-4560-8bf0-42d9dc8e4a69/download/2015gsafitaraimplementationandcioassignmentplan.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/64c56cec-4b8f-44c7-ba69-090517f9f32e/resource/87e53999-aff1-4560-8bf0-42d9dc8e4a69/download/2015gsafitaraimplementationandcioassignmentplan.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "2015 GSA Common Baseline Implementation Plan and CIO Assignment Plan"
                 }
             ],
+            "identifier": "GSA-2016-01-22-01",
             "keyword": [
                 "Assignment Plan",
                 "CIO",
@@ -8836,65 +8831,64 @@
                 "GSA IT",
                 "Implementation Plan"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2017-05-15",
             "programCode": [
                 "023:000"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "IT Initiatives"
-            ]
+            ],
+            "title": "2015 GSA Common Baseline Implementation Plan and CIO Assignment Plan"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Hiring Assessments and Selection Outcome Dataset",
-            "description": "An Excel export of combined USA Staffing, Monster, Aviator (FAA) Hiring Assessment and Selection Outcome Data from the 24 CFO Act agencies.  We believe this data will empower Chief Human Capital Officers and Human Resources staff with the right data to focus on improved hiring outcomes while complying with open data requirements to increase transparency to the millions of applicants who apply for federal positions each year on USAJOBS.",
-            "modified": "2022-07-28T10:14:34.842Z",
             "accessLevel": "public",
-            "identifier": "GSA-2021-01-08-01",
-            "dataQuality": true,
-            "describedBy": "https://inventory.data.gov/dataset/4189591b-d78e-4ad3-9d75-582175ad0b3f/resource/e91deb82-0d38-48f9-8dd2-6109619758e6/download/data-dictionary-for-hiring-assessment-and-selection-outcome-dataset.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "issued": "2021-01-08",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "138"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Aaron Eisenbarth",
                 "hasEmail": "mailto:aaron.eisenbarth@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://inventory.data.gov/dataset/4189591b-d78e-4ad3-9d75-582175ad0b3f/resource/e91deb82-0d38-48f9-8dd2-6109619758e6/download/data-dictionary-for-hiring-assessment-and-selection-outcome-dataset.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "An Excel export of combined USA Staffing, Monster, Aviator (FAA) Hiring Assessment and Selection Outcome Data from the 24 CFO Act agencies.  We believe this data will empower Chief Human Capital Officers and Human Resources staff with the right data to focus on improved hiring outcomes while complying with open data requirements to increase transparency to the millions of applicants who apply for federal positions each year on USAJOBS.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/4189591b-d78e-4ad3-9d75-582175ad0b3f/resource/20929a06-1ea8-4666-89bc-387497ec0674/download/data-dictionary-for-federal-hiring-dataset-dec-31-2022.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "data-dictionary-for-federal-hiring-dataset-dec-31-2022.xlsx",
-                    "downloadURL": "https://inventory.data.gov/dataset/4189591b-d78e-4ad3-9d75-582175ad0b3f/resource/20929a06-1ea8-4666-89bc-387497ec0674/download/data-dictionary-for-federal-hiring-dataset-dec-31-2022.xlsx"
+                    "title": "data-dictionary-for-federal-hiring-dataset-dec-31-2022.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/4189591b-d78e-4ad3-9d75-582175ad0b3f/resource/ef9d8bb1-2b4f-4618-98d1-bf96deaa6503/download/hiring_selections_and_outcomes_public_data_set_as_of_dec_31_2023_fy2020_fy2021.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "hiring_selections_and_outcomes_public_data_set_as_of_Dec_31_2023_FY2020_FY2021.xlsx",
-                    "downloadURL": "https://inventory.data.gov/dataset/4189591b-d78e-4ad3-9d75-582175ad0b3f/resource/ef9d8bb1-2b4f-4618-98d1-bf96deaa6503/download/hiring_selections_and_outcomes_public_data_set_as_of_dec_31_2023_fy2020_fy2021.xlsx"
+                    "title": "hiring_selections_and_outcomes_public_data_set_as_of_Dec_31_2023_FY2020_FY2021.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/4189591b-d78e-4ad3-9d75-582175ad0b3f/resource/dc0a8624-0f45-4d39-97d7-2a6694810d19/download/hiring_selections_and_outcomes_public_data_set_as_of_dec_31_2023_fy2022_fy2023.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "hiring_selections_and_outcomes_public_data_set_as_of_Dec_31_2023_FY2022_FY2023.xlsx",
-                    "downloadURL": "https://inventory.data.gov/dataset/4189591b-d78e-4ad3-9d75-582175ad0b3f/resource/dc0a8624-0f45-4d39-97d7-2a6694810d19/download/hiring_selections_and_outcomes_public_data_set_as_of_dec_31_2023_fy2022_fy2023.xlsx"
+                    "title": "hiring_selections_and_outcomes_public_data_set_as_of_Dec_31_2023_FY2022_FY2023.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/4189591b-d78e-4ad3-9d75-582175ad0b3f/resource/6de5e82a-3e16-491c-baf9-204c3b2f4767/download/hiring_selections_and_outcomes_public_data_set_as_of_dec_31_2023_fy2024.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "hiring_selections_and_outcomes_public_data_set_as_of_Dec_31_2023_FY2024.xlsx",
-                    "downloadURL": "https://inventory.data.gov/dataset/4189591b-d78e-4ad3-9d75-582175ad0b3f/resource/6de5e82a-3e16-491c-baf9-204c3b2f4767/download/hiring_selections_and_outcomes_public_data_set_as_of_dec_31_2023_fy2024.xlsx"
+                    "title": "hiring_selections_and_outcomes_public_data_set_as_of_Dec_31_2023_FY2024.xlsx"
                 }
             ],
+            "identifier": "GSA-2021-01-08-01",
+            "issued": "2021-01-08",
             "keyword": [
                 "Monster",
                 "OMB",
@@ -8906,48 +8900,48 @@
                 "hiring",
                 "selection"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-07-28T10:14:34.842Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "138"
+            },
+            "rights": "true",
+            "title": "Federal Hiring Assessments and Selection Outcome Dataset"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "e-Buy Awards for Fiscal Year 2014",
-            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
-            "modified": "2016-01-21",
             "accessLevel": "public",
-            "identifier": "GSA-2016-01-21-4",
-            "dataQuality": true,
-            "issued": "2015-05-18",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-08-31",
+            "bureauCode": [
+                "023:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Usha Gopal",
                 "hasEmail": "mailto:usha.gopal@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "e-Buy Awards for Fiscal Year 2014",
                     "description": "Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
-                    "downloadURL": "https://inventory.data.gov/dataset/17945414-d229-45fb-a216-b0b05df931b8/resource/4f3e8d99-2fa8-4ea2-8bba-d1cca2cc0a48/download/ebuyawardsfy2014.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/17945414-d229-45fb-a216-b0b05df931b8/resource/4f3e8d99-2fa8-4ea2-8bba-d1cca2cc0a48/download/ebuyawardsfy2014.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "e-Buy Awards for Fiscal Year 2014"
                 }
             ],
+            "identifier": "GSA-2016-01-21-4",
+            "isPartOf": "GSA-2015-08-31",
+            "issued": "2015-05-18",
             "keyword": [
                 "Awards",
                 "Contracts",
@@ -8957,101 +8951,101 @@
                 "e-Buy",
                 "procurement"
             ],
-            "bureauCode": [
-                "023:10"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-01-21",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "e-Buy Awards for Fiscal Year 2014"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions Oct-Dec 2015, 1st Qtr",
-            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-02-01",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xls",
-                    "title": "Purchase Card Transactions Oct - Dec 2015",
                     "description": "Purchases made with the purchase card. Files will be batched quarterly.",
-                    "downloadURL": "https://inventory.data.gov/dataset/401dd7af-0042-4151-9145-1c86d945b201/resource/43be4fac-09fd-42a2-acea-8edd8752d0b2/download/1st-quarter-2016-octdec-2015-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/401dd7af-0042-4151-9145-1c86d945b201/resource/43be4fac-09fd-42a2-acea-8edd8752d0b2/download/1st-quarter-2016-octdec-2015-pc-transactions.xlsx",
+                    "format": "xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Purchase Card Transactions Oct - Dec 2015"
                 }
             ],
+            "identifier": "GSA-2016-02-01",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "p-card",
                 "purchase card",
                 "purchase card transactions",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions Oct-Dec 2015, 1st Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA Oct-Dec 2015, 1st Qtr",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-02-01-02",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "excel",
-                    "title": "October December 2015 BOCA PC Transactions",
                     "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-                    "downloadURL": "https://inventory.data.gov/dataset/b580478a-b61d-4553-bcf9-848cc4214aa8/resource/c2837a8d-6e83-4873-806b-f1ab58d64d13/download/october-december-2015-boca-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/b580478a-b61d-4553-bcf9-848cc4214aa8/resource/c2837a8d-6e83-4873-806b-f1ab58d64d13/download/october-december-2015-boca-pc-transactions.xlsx",
+                    "format": "excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "October December 2015 BOCA PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-02-01-02",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Contract Board",
@@ -9059,74 +9053,58 @@
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA Oct-Dec 2015, 1st Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2021, 1st Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contract, by Fiscal Year, Contract, Contract Vehicle, Agency and month for the Central and Direct billing accounts.",
-            "modified": "2022-02-14T13:34:41.515Z",
             "accessLevel": "public",
-            "identifier": "GSA-2021-02-17-01",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Acquisition Service",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Federal Acquisition Service"
-                }
-            },
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contract, by Fiscal Year, Contract, Contract Vehicle, Agency and month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/a4b28422-5ed4-4719-866a-111f1a9a61b1/resource/81f94fd5-f45f-4edf-83e8-fc58aea68294/download/totrevfy21_1stqtr.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "TotRevFY21_1stQtr.xlsx",
-                    "downloadURL": "https://inventory.data.gov/dataset/a4b28422-5ed4-4719-866a-111f1a9a61b1/resource/81f94fd5-f45f-4edf-83e8-fc58aea68294/download/totrevfy21_1stqtr.xlsx"
+                    "title": "TotRevFY21_1stQtr.xlsx"
                 }
             ],
+            "identifier": "GSA-2021-02-17-01",
+            "isPartOf": "GSA-2015-08-27",
             "keyword": [
                 "Networx"
             ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
-            ],
             "language": [
                 "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "COVID Support Services",
-            "description": "In January 2021, GSA\u2019s Federal Acquisition Service (FAS) was asked to support the Department of Health and Human Services\u2019 Center for Disease Control (CDC) to assist federal, state and local agencies to quickly procure COVID-19 related support services (CRSS) should they be needed as part of the nation\u2019s COVID-19 response.",
-            "modified": "2021-03-18T17:45:52.044Z",
-            "accessLevel": "public",
-            "identifier": "GSA-2021-03-18-01",
-            "issued": "2021-02-17",
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
+            "modified": "2022-02-14T13:34:41.515Z",
+            "programCode": [
+                "015:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Acquisition Service",
@@ -9135,12 +9113,22 @@
                     "name": "Federal Acquisition Service"
                 }
             },
+            "rights": "true",
+            "title": "Networx Business Volume FY2021, 1st Qtr"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jon Bearscove",
                 "hasEmail": "mailto:CRSSHelp@gsa.gov"
             },
+            "description": "In January 2021, GSA\u2019s Federal Acquisition Service (FAS) was asked to support the Department of Health and Human Services\u2019 Center for Disease Control (CDC) to assist federal, state and local agencies to quickly procure COVID-19 related support services (CRSS) should they be needed as part of the nation\u2019s COVID-19 response.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9149,6 +9137,8 @@
                     "title": "COVID Support Services"
                 }
             ],
+            "identifier": "GSA-2021-03-18-01",
+            "issued": "2021-02-17",
             "keyword": [
                 "contract",
                 "contractor",
@@ -9158,397 +9148,383 @@
                 "support services",
                 "tribal entities"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-03-18T17:45:52.044Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Acquisition Service",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Federal Acquisition Service"
+                }
+            },
+            "rights": "true",
+            "title": "COVID Support Services"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2016, 1st Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
             "accessLevel": "public",
-            "identifier": "GSA-2016-02-19",
-            "dataQuality": true,
-            "issued": "2015-11-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xlsx",
-                    "title": "Networx Business Volume FY16 1st Quarter",
                     "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-                    "downloadURL": "https://inventory.data.gov/dataset/c79e79c9-db24-415b-ae5a-ce183449e802/resource/ec4eeb54-fc86-4029-bd4a-f0ca339d1e31/download/networx-business-volume-fy16-1st-quarter.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/c79e79c9-db24-415b-ae5a-ce183449e802/resource/ec4eeb54-fc86-4029-bd4a-f0ca339d1e31/download/networx-business-volume-fy16-1st-quarter.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Networx Business Volume FY16 1st Quarter"
                 }
             ],
+            "identifier": "GSA-2016-02-19",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-11-13",
             "keyword": [
                 "Contract",
                 "Networx Telecommunications",
                 "Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Telecommunications Services"
-            ]
+            ],
+            "title": "Networx Business Volume FY2016, 1st Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Closed-Paid Vouchers in Concur Government Edition (CGE)",
-            "description": "Closed and Paid vouchers from the Concur Travel System.",
-            "modified": "2016-02-23",
             "accessLevel": "non-public",
-            "identifier": "GSA-2016-02-22-01",
-            "dataQuality": true,
-            "issued": "2015-08-27",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-09-11-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Marvin Wilber Somers",
                 "hasEmail": "mailto:marvin.somers@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Closed and Paid vouchers from the Concur Travel System.",
+            "identifier": "GSA-2016-02-22-01",
+            "isPartOf": "GSA-2015-09-11-01",
+            "issued": "2015-08-27",
             "keyword": [
                 "Purchase Card",
                 "Travel Program"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-02-23",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "Trade secrets & commercial/financial info obtained from a person and privileged or confidential.",
             "theme": [
                 "Travel",
                 "Transportation"
-            ]
+            ],
+            "title": "Closed-Paid Vouchers in Concur Government Edition (CGE)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Pulse HTTPS Survey",
-            "description": "Results of Pulse's Survey of HTTPS support in Government Agency Websites.",
-            "modified": "2016-12-01",
             "accessLevel": "public",
-            "identifier": "GSA-2016-03-03-01",
-            "dataQuality": true,
-            "issued": "2015-07-08",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Technology Transformation Service",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "General Services Administration"
-                }
-            },
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Eric Mill",
                 "hasEmail": "mailto:eric.mill@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Results of Pulse's Survey of HTTPS support in Government Agency Websites.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/csv",
-                    "format": "csv",
-                    "title": "Pulse HTTPS Survey",
                     "description": "Results of Pulse\u2019s survey of HTTPS support in government agency \r\nwebsites.",
-                    "downloadURL": "https://pulse.cio.gov/data/domains/https.csv"
+                    "downloadURL": "https://pulse.cio.gov/data/domains/https.csv",
+                    "format": "csv",
+                    "mediaType": "application/csv",
+                    "title": "Pulse HTTPS Survey"
                 }
             ],
+            "identifier": "GSA-2016-03-03-01",
+            "issued": "2015-07-08",
             "keyword": [
                 "18F",
                 "government",
                 "https",
                 "pulse"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-12-01",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Technology Transformation Service",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "General Services Administration"
+                }
+            },
             "theme": [
                 "HTTPS Survey"
-            ]
+            ],
+            "title": "Pulse HTTPS Survey"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Data.gov Daily Sessions",
-            "description": "Data.gov Daily Sessions 20120101-20151231",
-            "modified": "2016-08-01",
             "accessLevel": "public",
-            "identifier": "GSA - DATA.GOVMETRICS1",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
-            "isPartOf": "GSA-2015-09-14-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Joo Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "description": "Data.gov Daily Sessions 20120101-20151231",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "title": "Data.gov Daily Sessions",
                     "description": "Data.gov Daily Sessions 20120101-20151231",
-                    "downloadURL": "https://inventory.data.gov/dataset/e0de4198-eaaa-423a-9154-7af76ab8d822/resource/a78ae43e-0ceb-4f2d-83ac-99c61b249afa/download/analytics-www.data.gov-data.gov-daily-sessions-20120101-20151231-analytics-www.data.gov-data.g.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/e0de4198-eaaa-423a-9154-7af76ab8d822/resource/a78ae43e-0ceb-4f2d-83ac-99c61b249afa/download/analytics-www.data.gov-data.gov-daily-sessions-20120101-20151231-analytics-www.data.gov-data.g.csv",
+                    "mediaType": "text/csv",
+                    "title": "Data.gov Daily Sessions"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "title": "Data.gov Daily Sessions Day Index",
                     "description": "Data.gov Daily Sessions 20120101-20151231 Day Index",
-                    "downloadURL": "https://inventory.data.gov/dataset/e0de4198-eaaa-423a-9154-7af76ab8d822/resource/925f6204-5240-4dd1-8604-c279843c8974/download/analytics-www.data.gov-data.gov-daily-sessions-20120101-20151231b-sheet1.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/e0de4198-eaaa-423a-9154-7af76ab8d822/resource/925f6204-5240-4dd1-8604-c279843c8974/download/analytics-www.data.gov-data.gov-daily-sessions-20120101-20151231b-sheet1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Data.gov Daily Sessions Day Index"
                 }
             ],
+            "identifier": "GSA - DATA.GOVMETRICS1",
+            "isPartOf": "GSA-2015-09-14-01",
             "keyword": [
                 "Data.gov Analytics",
                 "metrics"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-08-01",
             "programCode": [
                 "023:019"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Data.gov Sessions by Month from Countries with Sessions Greater than 1000 per Month, Excluding United States",
-            "description": "Data.gov Sessions by Month from Countries with Sessions Greater than 1000 per Month, Excluding United States 20120101-20151231",
-            "modified": "2016-08-01",
-            "accessLevel": "public",
-            "identifier": "GSA - DATA.GOVMETRICS2",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
-            "isPartOf": "GSA-2015-09-14-01",
+            "title": "Data.gov Daily Sessions"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Joo Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "description": "Data.gov Sessions by Month from Countries with Sessions Greater than 1000 per Month, Excluding United States 20120101-20151231",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "csv",
-                    "title": "Data.gov Sessions by Month from Countries with Sessions Greater than 1000 per Month, Excluding United States",
                     "description": "Data.gov Sessions by Month from Countries with Sessions Greater than 1000 per Month, Excluding United States 20120101-20151231",
-                    "downloadURL": "https://inventory.data.gov/dataset/25013222-c373-4a08-9750-14794daffe66/resource/eb1faa07-1e63-454c-a968-8734a5faf9aa/download/analytics-www.data.gov-data.gov-sessions-by-month-from-countries-with-sessions-greater-than-1000.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/25013222-c373-4a08-9750-14794daffe66/resource/eb1faa07-1e63-454c-a968-8734a5faf9aa/download/analytics-www.data.gov-data.gov-sessions-by-month-from-countries-with-sessions-greater-than-1000.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "Data.gov Sessions by Month from Countries with Sessions Greater than 1000 per Month, Excluding United States"
                 }
             ],
+            "identifier": "GSA - DATA.GOVMETRICS2",
+            "isPartOf": "GSA-2015-09-14-01",
             "keyword": [
                 "data.gov",
                 "data.gov analytics",
                 "metrics"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-08-01",
             "programCode": [
                 "023:019"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Data.gov Sessions by U.S. States by Month",
-            "description": "Data.gov Sessions by U.S. States by Month 20120101-20151231",
-            "modified": "2016-08-01",
-            "accessLevel": "public",
-            "identifier": "GSA - DATA.GOVMETRICS3",
-            "describedByType": "text/csv",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
-            "isPartOf": "GSA-2015-09-14-01",
+            "title": "Data.gov Sessions by Month from Countries with Sessions Greater than 1000 per Month, Excluding United States"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Joo Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "describedByType": "text/csv",
+            "description": "Data.gov Sessions by U.S. States by Month 20120101-20151231",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "csv",
-                    "title": "Data.gov Sessions by U.S. States by Month",
                     "description": "Data.gov Sessions by U.S. States by Month 20120101-20151231",
-                    "downloadURL": "https://inventory.data.gov/dataset/77d6edf0-14a8-4e53-a211-403343328be2/resource/302fc081-484e-4de2-be55-f92b7d030691/download/analytics-www.data.gov-data.gov-sessions-by-u.s.-states-by-month-20120101-20151231-analytics-w.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/77d6edf0-14a8-4e53-a211-403343328be2/resource/302fc081-484e-4de2-be55-f92b7d030691/download/analytics-www.data.gov-data.gov-sessions-by-u.s.-states-by-month-20120101-20151231-analytics-w.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "Data.gov Sessions by U.S. States by Month"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "title": "Data.gov Sessions by U.S. States by Month Day Index",
                     "description": "Data.gov Sessions by U.S. States by Month 20120101-20151231 Day Index",
-                    "downloadURL": "https://inventory.data.gov/dataset/77d6edf0-14a8-4e53-a211-403343328be2/resource/3b1dce0e-2cda-4fed-a749-68954abafbc7/download/analytics-www.data.gov-data.gov-sessions-by-u.s.-states-by-month-20120101-20151231b-sheet1.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/77d6edf0-14a8-4e53-a211-403343328be2/resource/3b1dce0e-2cda-4fed-a749-68954abafbc7/download/analytics-www.data.gov-data.gov-sessions-by-u.s.-states-by-month-20120101-20151231b-sheet1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Data.gov Sessions by U.S. States by Month Day Index"
                 }
             ],
+            "identifier": "GSA - DATA.GOVMETRICS3",
+            "isPartOf": "GSA-2015-09-14-01",
             "keyword": [
                 "Data.gov Metrics",
                 "Data.gov Stats"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-08-01",
             "programCode": [
                 "023:019"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Data.gov Sessions by Month",
-            "description": "Data.gov Sessions by Month 20120101-20151231",
-            "modified": "2016-08-01",
-            "accessLevel": "public",
-            "identifier": "GSA - DATA.GOVMETRICS4",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
-            "isPartOf": "GSA-2015-09-14-01",
+            "title": "Data.gov Sessions by U.S. States by Month"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Joo Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "description": "Data.gov Sessions by Month 20120101-20151231",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "title": "Data.gov Sessions by Month",
                     "description": "Data.gov Sessions by Month 20120101-20151231",
-                    "downloadURL": "https://inventory.data.gov/dataset/93deddb9-ff7b-43ea-bce6-a747202bae6b/resource/f933a656-37c4-4c21-8ebc-b34a8e1ef891/download/analytics-www.data.gov-data.gov-sessions-by-month-20120101-20151231-analytics-www.data.gov-dat.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/93deddb9-ff7b-43ea-bce6-a747202bae6b/resource/f933a656-37c4-4c21-8ebc-b34a8e1ef891/download/analytics-www.data.gov-data.gov-sessions-by-month-20120101-20151231-analytics-www.data.gov-dat.csv",
+                    "mediaType": "text/csv",
+                    "title": "Data.gov Sessions by Month"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "title": "Data.gov Sessions by Month Day Index",
                     "description": "Data.gov Sessions by Month Day Index 20120101-20151231",
-                    "downloadURL": "https://inventory.data.gov/dataset/93deddb9-ff7b-43ea-bce6-a747202bae6b/resource/31218b56-e5a1-4f7d-9ad6-5ddca5f08083/download/analytics-www.data.gov-data.gov-sessions-by-month-20120101-20151231b-analytics-www.data.gov-da.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/93deddb9-ff7b-43ea-bce6-a747202bae6b/resource/31218b56-e5a1-4f7d-9ad6-5ddca5f08083/download/analytics-www.data.gov-data.gov-sessions-by-month-20120101-20151231b-analytics-www.data.gov-da.csv",
+                    "mediaType": "text/csv",
+                    "title": "Data.gov Sessions by Month Day Index"
                 }
             ],
+            "identifier": "GSA - DATA.GOVMETRICS4",
+            "isPartOf": "GSA-2015-09-14-01",
             "keyword": [
                 "Data.gov Metrics",
                 "Data.gov Stats"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-08-01",
             "programCode": [
                 "023:019"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Pulse Analytics Participation Survey",
-            "description": "Results of Pulse's survey of analytics participation on government agency websites.",
-            "modified": "2016-12-01",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-03-03-02",
-            "dataQuality": true,
-            "issued": "2015-07-08",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            ],
             "publisher": {
-                "@type": "org:Organization",
-                "name": "Technology Transformation Service",
-                "subOrganizationOf": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
-                }
             },
+            "title": "Data.gov Sessions by Month"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Eric Mill",
                 "hasEmail": "mailto:eric.mill@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Results of Pulse's survey of analytics participation on government agency websites.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "csv",
-                    "title": "Pulse Analytics Survey",
                     "description": "Results of Pulse's survey of analytics participation on government agency websites.",
-                    "downloadURL": "https://pulse.cio.gov/data/domains/analytics.csv"
+                    "downloadURL": "https://pulse.cio.gov/data/domains/analytics.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "Pulse Analytics Survey"
                 }
             ],
+            "identifier": "GSA-2016-03-03-02",
+            "issued": "2015-07-08",
             "keyword": [
                 "18F",
                 "analytics",
                 "pulse"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:019"
-            ],
             "language": [
                 "en-US"
             ],
-            "theme": [
-                "Pulse Analytics Survey"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Visits by Browser",
-            "description": "A breakdown by web browser of the past 90 days of visits to government websites.",
-            "modified": "2016-12-01",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-03-03-16",
-            "dataQuality": true,
-            "issued": "2015-07-08",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-12-01",
+            "programCode": [
+                "023:019"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Technology Transformation Service",
@@ -9557,53 +9533,51 @@
                     "name": "General Services Administration"
                 }
             },
+            "theme": [
+                "Pulse Analytics Survey"
+            ],
+            "title": "Pulse Analytics Participation Survey"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
-            "isPartOf": "GSA-2016-03-03-03",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Timothy Lowden",
                 "hasEmail": "mailto:timothy.lowden@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "A breakdown by web browser of the past 90 days of visits to government websites.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://analytics.usa.gov/data/live/browsers.json",
+                    "description": "A breakdown by web browser of the past 90 days of visits to government websites.",
                     "format": "application/json",
-                    "title": "Visits by Browser",
-                    "description": "A breakdown by web browser of the past 90 days of visits to government websites."
+                    "title": "Visits by Browser"
                 }
             ],
+            "identifier": "GSA-2016-03-03-16",
+            "isPartOf": "GSA-2016-03-03-03",
+            "issued": "2015-07-08",
             "keyword": [
                 "18F",
                 "analytics",
                 "browser",
                 "visitors"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:019"
-            ],
             "language": [
                 "en-US"
             ],
-            "theme": [
-                "Analytics"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "18F Internal Team API",
-            "description": "An API for information on what 18F is working on.",
-            "modified": "2016-12-01",
-            "accessLevel": "non-public",
-            "identifier": "GSA-2016-03-03-07",
-            "dataQuality": true,
-            "describedBy": "https://team-api.18f.gov/api/",
-            "describedByType": "text/html",
-            "issued": "2015-10-12",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-12-01",
+            "programCode": [
+                "023:019"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Technology Transformation Service",
@@ -9612,162 +9586,179 @@
                     "name": "General Services Administration"
                 }
             },
+            "theme": [
+                "Analytics"
+            ],
+            "title": "Visits by Browser"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Amanda Robinson",
                 "hasEmail": "mailto:amanda.robinson@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://team-api.18f.gov/api/",
+            "describedByType": "text/html",
+            "description": "An API for information on what 18F is working on.",
+            "identifier": "GSA-2016-03-03-07",
+            "issued": "2015-10-12",
             "keyword": [
                 "18F",
                 "documentation"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-12-01",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Technology Transformation Service",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "General Services Administration"
+                }
+            },
             "theme": [
                 "API"
-            ]
+            ],
+            "title": "18F Internal Team API"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions Jan-Mar 2016, 2nd Qtr",
-            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-04-15-01",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "Jan-Mar 2016 PC Transactions",
                     "description": "Purchases made with the purchase card. Files will be batched quarterly.",
-                    "downloadURL": "https://inventory.data.gov/dataset/ada3353e-b4da-4a3c-8f58-fd401cee999c/resource/7ff97ec6-f85d-409a-80f4-f84295c96623/download/jan-mar-2016-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/ada3353e-b4da-4a3c-8f58-fd401cee999c/resource/7ff97ec6-f85d-409a-80f4-f84295c96623/download/jan-mar-2016-pc-transactions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Jan-Mar 2016 PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-04-15-01",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "january",
                 "march",
                 "purchase card",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions Jan-Mar 2016, 2nd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Analytics.USA.gov",
-            "description": "High level website analytics from across the government domain.",
-            "modified": "2022-02-02T18:47:08.231Z",
             "accessLevel": "public",
-            "identifier": "GSA-2016-03-03-03",
-            "dataQuality": true,
-            "issued": "2015-07-08",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Technology Transformation Service",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Technology Transformation Service"
-                }
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Timothy Lowden",
                 "hasEmail": "mailto:timothy.lowden@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "High level website analytics from across the government domain.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://analytics.usa.gov/",
+                    "description": "Based on rough network segmentation data, we estimate that less than 5% of all traffic across all agencies comes from US federal government networks.",
                     "format": "html",
-                    "title": "analytics.usa.gov",
-                    "description": "Based on rough network segmentation data, we estimate that less than 5% of all traffic across all agencies comes from US federal government networks."
+                    "title": "analytics.usa.gov"
                 }
             ],
+            "identifier": "GSA-2016-03-03-03",
+            "issued": "2015-07-08",
             "keyword": [
                 "18F",
                 "analytics",
                 "visitors"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-02-02T18:47:08.231Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Current Active Users of Government Websites",
-            "description": "The total number of visitors to government websites in the last minute.",
-            "modified": "2016-12-01",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-03-03-11",
-            "dataQuality": true,
-            "issued": "2015-07-08",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Technology Transformation Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "General Services Administration"
+                    "name": "Technology Transformation Service"
                 }
             },
+            "rights": "true",
+            "title": "Analytics.USA.gov"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
-            "isPartOf": "GSA-2016-03-03-03",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Timothy Lowden",
                 "hasEmail": "mailto:timothy.lowden@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The total number of visitors to government websites in the last minute.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://analytics.usa.gov/data/live/realtime.json",
+                    "description": "The total number of visitors to government websites in the last minute.",
                     "format": "API",
-                    "title": "Current Active Users",
-                    "description": "The total number of visitors to government websites in the last minute."
+                    "title": "Current Active Users"
                 }
             ],
+            "identifier": "GSA-2016-03-03-11",
+            "isPartOf": "GSA-2016-03-03-03",
+            "issued": "2015-07-08",
             "keyword": [
                 "18F",
                 "analytics",
@@ -9775,29 +9766,14 @@
                 "visitors",
                 "websites"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:019"
-            ],
             "language": [
                 "en-US"
             ],
-            "theme": [
-                "Analytics"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Visits by Device Type",
-            "description": "A breakdown into Desktop/Mobile/Tablet of the past 90 days of visitors to government websites.",
-            "modified": "2016-12-01",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-03-03-13",
-            "dataQuality": true,
-            "issued": "2015-07-08",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-12-01",
+            "programCode": [
+                "023:019"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Technology Transformation Service",
@@ -9806,22 +9782,37 @@
                     "name": "General Services Administration"
                 }
             },
+            "theme": [
+                "Analytics"
+            ],
+            "title": "Current Active Users of Government Websites"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
-            "isPartOf": "GSA-2016-03-03-03",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Timothy Lowden",
                 "hasEmail": "mailto:timothy.lowden@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "A breakdown into Desktop/Mobile/Tablet of the past 90 days of visitors to government websites.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://analytics.usa.gov/data/live/devices.json",
+                    "description": "A breakdown into Desktop/Mobile/Tablet of the past 90 days of visitors to government websites",
                     "format": "application/json",
-                    "title": "Visits by Device Type",
-                    "description": "A breakdown into Desktop/Mobile/Tablet of the past 90 days of visitors to government websites"
+                    "title": "Visits by Device Type"
                 }
             ],
+            "identifier": "GSA-2016-03-03-13",
+            "isPartOf": "GSA-2016-03-03-03",
+            "issued": "2015-07-08",
             "keyword": [
                 "18F",
                 "analytics",
@@ -9831,29 +9822,14 @@
                 "visitors",
                 "websites"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:019"
-            ],
             "language": [
                 "en-US"
             ],
-            "theme": [
-                "Analytics"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Visits by Operating Systems",
-            "description": "A breakdown by operating system of the past 90 days of visits to government websites.",
-            "modified": "2016-12-01",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-03-03-14",
-            "dataQuality": true,
-            "issued": "2015-07-08",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-12-01",
+            "programCode": [
+                "023:019"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Technology Transformation Service",
@@ -9862,51 +9838,51 @@
                     "name": "General Services Administration"
                 }
             },
+            "theme": [
+                "Analytics"
+            ],
+            "title": "Visits by Device Type"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
-            "isPartOf": "GSA-2016-03-03-03",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Timothy Lowden",
                 "hasEmail": "mailto:timothy.lowden@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "A breakdown by operating system of the past 90 days of visits to government websites.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://analytics.usa.gov/data/live/os.json",
+                    "description": "A breakdown by operating system of the past 90 days of visits to government websites",
                     "format": "application/json",
-                    "title": "Visits by Operating Systems",
-                    "description": "A breakdown by operating system of the past 90 days of visits to government websites"
+                    "title": "Visits by Operating Systems"
                 }
             ],
+            "identifier": "GSA-2016-03-03-14",
+            "isPartOf": "GSA-2016-03-03-03",
+            "issued": "2015-07-08",
             "keyword": [
                 "18F",
                 "analytics",
                 "operating systems",
                 "visitors"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:019"
-            ],
             "language": [
                 "en-US"
             ],
-            "theme": [
-                "Analytics"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Visits by Windows Version",
-            "description": "A breakdown by Windows version of the past 90 days of visits to government websites.",
-            "modified": "2016-12-01",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-03-03-15",
-            "dataQuality": true,
-            "issued": "2015-07-08",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-12-01",
+            "programCode": [
+                "023:019"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Technology Transformation Service",
@@ -9915,22 +9891,37 @@
                     "name": "General Services Administration"
                 }
             },
+            "theme": [
+                "Analytics"
+            ],
+            "title": "Visits by Operating Systems"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
-            "isPartOf": "GSA-2016-03-03-03",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Timothy Lowden",
                 "hasEmail": "mailto:timothy.lowden@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "A breakdown by Windows version of the past 90 days of visits to government websites.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://analytics.usa.gov/data/live/windows.json",
+                    "description": "A breakdown by Windows version of the past 90 days of visits to government websites.",
                     "format": "application/json",
-                    "title": "Visits by Windows Version",
-                    "description": "A breakdown by Windows version of the past 90 days of visits to government websites."
+                    "title": "Visits by Windows Version"
                 }
             ],
+            "identifier": "GSA-2016-03-03-15",
+            "isPartOf": "GSA-2016-03-03-03",
+            "issued": "2015-07-08",
             "keyword": [
                 "18F",
                 "analytics",
@@ -9938,29 +9929,14 @@
                 "visitors",
                 "windows"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:019"
-            ],
             "language": [
                 "en-US"
             ],
-            "theme": [
-                "Analytics"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Visits by Internet Explorer Version",
-            "description": "A breakdown by Internet Explorer version of the past 90 days of visits to government websites.",
-            "modified": "2016-12-01",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-03-03-17",
-            "dataQuality": true,
-            "issued": "2015-07-08",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-12-01",
+            "programCode": [
+                "023:019"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Technology Transformation Service",
@@ -9969,22 +9945,37 @@
                     "name": "General Services Administration"
                 }
             },
+            "theme": [
+                "Analytics"
+            ],
+            "title": "Visits by Windows Version"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
-            "isPartOf": "GSA-2016-03-03-03",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Timothy Lowden",
                 "hasEmail": "mailto:timothy.lowden@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "A breakdown by Internet Explorer version of the past 90 days of visits to government websites.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://analytics.usa.gov/data/live/ie.json",
+                    "description": "A breakdown by Internet Explorer version of the past 90 days of visits to government websites.",
                     "format": "application/json",
-                    "title": "Visits by IE Version",
-                    "description": "A breakdown by Internet Explorer version of the past 90 days of visits to government websites."
+                    "title": "Visits by IE Version"
                 }
             ],
+            "identifier": "GSA-2016-03-03-17",
+            "isPartOf": "GSA-2016-03-03-03",
+            "issued": "2015-07-08",
             "keyword": [
                 "18F",
                 "analytics",
@@ -9992,29 +9983,14 @@
                 "version",
                 "visitors"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:019"
-            ],
             "language": [
                 "en-US"
             ],
-            "theme": [
-                "Analytics"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Top 20 Pages, Ranked by Current Visitors",
-            "description": "The top 20 pages visited in the last minute.",
-            "modified": "2016-12-01",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-03-03-18",
-            "dataQuality": true,
-            "issued": "2015-07-08",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-12-01",
+            "programCode": [
+                "023:019"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Technology Transformation Service",
@@ -10023,23 +9999,38 @@
                     "name": "General Services Administration"
                 }
             },
+            "theme": [
+                "Analytics"
+            ],
+            "title": "Visits by Internet Explorer Version"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
-            "isPartOf": "GSA-2016-03-03-03",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Timothy Lowden",
                 "hasEmail": "mailto:timothy.lowden@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The top 20 pages visited in the last minute.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
-                    "format": "json",
-                    "title": "Top 20 Pages, Ranked by Current Visitors",
                     "description": "The top 20 pages visited in the last minute",
-                    "downloadURL": "https://analytics.usa.gov/data/live/top-pages-realtime.json"
+                    "downloadURL": "https://analytics.usa.gov/data/live/top-pages-realtime.json",
+                    "format": "json",
+                    "mediaType": "application/json",
+                    "title": "Top 20 Pages, Ranked by Current Visitors"
                 }
             ],
+            "identifier": "GSA-2016-03-03-18",
+            "isPartOf": "GSA-2016-03-03-03",
+            "issued": "2015-07-08",
             "keyword": [
                 "18F",
                 "analytics",
@@ -10048,29 +10039,14 @@
                 "top",
                 "visitors"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:019"
-            ],
             "language": [
                 "en-US"
             ],
-            "theme": [
-                "Analytics"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Top 20 Domains Over Last 7 Days",
-            "description": "The top 20 domains visited in the last 7 days.",
-            "modified": "2016-12-01",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-03-03-19",
-            "dataQuality": true,
-            "issued": "2015-07-08",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-12-01",
+            "programCode": [
+                "023:019"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Technology Transformation Service",
@@ -10079,22 +10055,37 @@
                     "name": "General Services Administration"
                 }
             },
+            "theme": [
+                "Analytics"
+            ],
+            "title": "Top 20 Pages, Ranked by Current Visitors"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
-            "isPartOf": "GSA-2016-03-03-03",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Timothy Lowden",
                 "hasEmail": "mailto:timothy.lowden@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The top 20 domains visited in the last 7 days.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://analytics.usa.gov/data/live/top-domains-7-days.json",
+                    "description": "The top 20 domains visited in the last 7 days.",
                     "format": "application/json",
-                    "title": "Top 20 Domains Over Last 7 Days",
-                    "description": "The top 20 domains visited in the last 7 days."
+                    "title": "Top 20 Domains Over Last 7 Days"
                 }
             ],
+            "identifier": "GSA-2016-03-03-19",
+            "isPartOf": "GSA-2016-03-03-03",
+            "issued": "2015-07-08",
             "keyword": [
                 "18F",
                 "analytics",
@@ -10102,29 +10093,14 @@
                 "top",
                 "visitors"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:019"
-            ],
             "language": [
                 "en-US"
             ],
-            "theme": [
-                "Analytics"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Top 20 Domains Over Last 30 Days",
-            "description": "The top 20 government domains visited in the last 30 days.",
-            "modified": "2016-12-01",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-03-03-20",
-            "dataQuality": true,
-            "issued": "2015-07-08",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-12-01",
+            "programCode": [
+                "023:019"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Technology Transformation Service",
@@ -10133,22 +10109,37 @@
                     "name": "General Services Administration"
                 }
             },
+            "theme": [
+                "Analytics"
+            ],
+            "title": "Top 20 Domains Over Last 7 Days"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
-            "isPartOf": "GSA-2016-03-03-03",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Timothy Lowden",
                 "hasEmail": "mailto:timothy.lowden@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The top 20 government domains visited in the last 30 days.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://analytics.usa.gov/data/live/top-domains-30-days.json",
+                    "description": "The top 20 government domains visited in the last 30 days",
                     "format": "application/json",
-                    "title": "Top 20 Domains Over Last 30 Days",
-                    "description": "The top 20 government domains visited in the last 30 days"
+                    "title": "Top 20 Domains Over Last 30 Days"
                 }
             ],
+            "identifier": "GSA-2016-03-03-20",
+            "isPartOf": "GSA-2016-03-03-03",
+            "issued": "2015-07-08",
             "keyword": [
                 "18F",
                 "analytics",
@@ -10156,29 +10147,14 @@
                 "top",
                 "visitors"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:019"
-            ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "Analytics"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Discovery Market Research API",
-            "description": "The GSA Discovery Market Research API.",
-            "modified": "2018-09-24",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-03-03-04",
-            "dataQuality": true,
-            "issued": "2015-07-08",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-12-01",
+            "programCode": [
+                "023:019"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Technology Transformation Service",
@@ -10187,12 +10163,25 @@
                     "name": "General Services Administration"
                 }
             },
+            "theme": [
+                "Analytics"
+            ],
+            "title": "Top 20 Domains Over Last 30 Days"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Bailey",
                 "hasEmail": "mailto:kelly.bailey@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA Discovery Market Research API.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10201,6 +10190,8 @@
                     "title": "Discovery Market Research API"
                 }
             ],
+            "identifier": "GSA-2016-03-03-04",
+            "issued": "2015-07-08",
             "keyword": [
                 "18F",
                 "api",
@@ -10209,31 +10200,14 @@
                 "procurement",
                 "web service"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:019"
-            ],
             "language": [
                 "en-US"
             ],
-            "theme": [
-                "API"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "api.data.gov Admin API",
-            "description": "An administrative API to manage the api.data.gov service.",
-            "modified": "2016-12-01",
-            "accessLevel": "non-public",
-            "identifier": "GSA-2016-03-03-10",
-            "dataQuality": true,
-            "describedBy": "http://apiumbrella.io/docs/admin-api/",
-            "describedByType": "text/html",
-            "issued": "2015-11-04",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-09-24",
+            "programCode": [
+                "023:019"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Technology Transformation Service",
@@ -10242,41 +10216,43 @@
                     "name": "General Services Administration"
                 }
             },
+            "theme": [
+                "API"
+            ],
+            "title": "Discovery Market Research API"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Gray Brooks",
                 "hasEmail": "mailto:gray.brooks@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://apiumbrella.io/docs/admin-api/",
+            "describedByType": "text/html",
+            "description": "An administrative API to manage the api.data.gov service.",
+            "identifier": "GSA-2016-03-03-10",
+            "issued": "2015-11-04",
             "keyword": [
                 "18F",
                 "administration",
                 "api",
                 "shared service"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:019"
-            ],
             "language": [
                 "en-US"
             ],
-            "theme": [
-                "API"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Visitors Per Hour For The Last Day",
-            "description": "The visitors to government websites for each hour in the last 24 hours.",
-            "modified": "2016-12-01",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-03-03-12",
-            "dataQuality": true,
-            "issued": "2015-07-08",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-12-01",
+            "programCode": [
+                "023:019"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Technology Transformation Service",
@@ -10285,51 +10261,51 @@
                     "name": "General Services Administration"
                 }
             },
+            "theme": [
+                "API"
+            ],
+            "title": "api.data.gov Admin API"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1H",
-            "isPartOf": "GSA-2016-03-03-03",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Timothy Lowden",
                 "hasEmail": "mailto:timothy.lowden@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The visitors to government websites for each hour in the last 24 hours.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://analytics.usa.gov/data/live/today.json",
+                    "description": "The visitors to government websites for each hour in the last 24 hours.",
                     "format": "application/json",
-                    "title": "Visitors Per Hour",
-                    "description": "The visitors to government websites for each hour in the last 24 hours."
+                    "title": "Visitors Per Hour"
                 }
             ],
+            "identifier": "GSA-2016-03-03-12",
+            "isPartOf": "GSA-2016-03-03-03",
+            "issued": "2015-07-08",
             "keyword": [
                 "18F",
                 "analytics",
                 "visitors",
                 "websites"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:019"
-            ],
             "language": [
                 "en-US"
             ],
-            "theme": [
-                "Analytics"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Contract-Awarded Labor Category API",
-            "description": "An API for searching awarded ceiling rates for labor categories.",
-            "modified": "2018-09-24",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-03-03-05",
-            "dataQuality": true,
-            "issued": "2015-07-08",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-12-01",
+            "programCode": [
+                "023:019"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Technology Transformation Service",
@@ -10338,12 +10314,25 @@
                     "name": "General Services Administration"
                 }
             },
+            "theme": [
+                "Analytics"
+            ],
+            "title": "Visitors Per Hour For The Last Day"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Bailey",
                 "hasEmail": "mailto:kelly.bailey@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "An API for searching awarded ceiling rates for labor categories.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10352,6 +10341,8 @@
                     "title": "Contract-Awarded Labor Category API"
                 }
             ],
+            "identifier": "GSA-2016-03-03-05",
+            "issued": "2015-07-08",
             "keyword": [
                 "18F",
                 "api",
@@ -10359,92 +10350,95 @@
                 "labor",
                 "procurement"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-09-24",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Technology Transformation Service",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "General Services Administration"
+                }
+            },
             "theme": [
                 "API"
-            ]
+            ],
+            "title": "Contract-Awarded Labor Category API"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA FITARA Actions and Milestones",
-            "description": "This JSON file represents GSA's FITARA Actions and Milestones submission to OMB.  This file abides by the OMB JSON schema found here: https://management.cio.gov/schemaexamples/FITARA_milestones_schema.json",
-            "modified": "2018-02-28",
             "accessLevel": "public",
-            "identifier": "GSA-2016-04-27-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "conformsTo": "https://management.cio.gov/schemaexamples/FITARA_milestones_schema.json",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mick Harris",
                 "hasEmail": "mailto:michael.harris@gsa.gov"
             },
+            "description": "This JSON file represents GSA's FITARA Actions and Milestones submission to OMB.  This file abides by the OMB JSON schema found here: https://management.cio.gov/schemaexamples/FITARA_milestones_schema.json",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
-                    "format": "json",
-                    "title": "GSA FITARA Actions and Milestones 2023-11-09",
-                    "description": "GSA's Actions and Milestones JSON file to fulfill the FITARA requirements for the November 2023 quarterly submission to OMB on November 9, 2023.",
                     "conformsTo": "https://management.cio.gov/schemaexamples/FITARA_milestones_schema.json",
-                    "downloadURL": "https://inventory.data.gov/dataset/cedf61aa-c4c8-4c30-8357-9d57362afe9b/resource/69cf9b0f-fe64-4ec3-a082-664d34497d5e/download/fitaramilestones.json"
+                    "description": "GSA's Actions and Milestones JSON file to fulfill the FITARA requirements for the November 2023 quarterly submission to OMB on November 9, 2023.",
+                    "downloadURL": "https://inventory.data.gov/dataset/cedf61aa-c4c8-4c30-8357-9d57362afe9b/resource/69cf9b0f-fe64-4ec3-a082-664d34497d5e/download/fitaramilestones.json",
+                    "format": "json",
+                    "mediaType": "application/json",
+                    "title": "GSA FITARA Actions and Milestones 2023-11-09"
                 }
             ],
+            "identifier": "GSA-2016-04-27-01",
             "keyword": [
                 "FITARA",
                 "GSA",
                 "Milestones",
                 "fitaramilestones.json"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-02-28",
             "programCode": [
                 "023:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA Jan-Mar 2016, 2nd Qtr",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2018-11-15",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-04-28-01",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "title": "GSA FITARA Actions and Milestones"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://inventory.data.gov/dataset/53a65d0a-91b9-4b24-ad95-7cf135b0536b/resource/0bf6a2a6-581c-4737-96a5-ddcf57dc3363/download/jan-mar-2016-cbca-pc-transactions.xlsx",
                     "format": "excel",
-                    "title": "Jan-Mar BOCA PC Transactions",
-                    "downloadURL": "https://inventory.data.gov/dataset/53a65d0a-91b9-4b24-ad95-7cf135b0536b/resource/0bf6a2a6-581c-4737-96a5-ddcf57dc3363/download/jan-mar-2016-cbca-pc-transactions.xlsx"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Jan-Mar BOCA PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-04-28-01",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Board of Contract Appeals",
@@ -10452,57 +10446,53 @@
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA Jan-Mar 2016, 2nd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "COVID-19 Contract Obligation Tracking Dataset",
-            "description": "COVID-19 dashboard dataset provides all government-wide Emergency Acquisitions spending in support of the Novel Coronavirus Disease 2019 (COVID-19) pandemic.",
-            "modified": "2021-03-25T17:26:22.917Z",
             "accessLevel": "public",
-            "identifier": "GSA-2021-03-22-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Acquisition Service",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Federal Acquisition Service"
-                }
-            },
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Beang Tong",
                 "hasEmail": "mailto:beang.f.tong@gsa.gov"
             },
+            "description": "COVID-19 dashboard dataset provides all government-wide Emergency Acquisitions spending in support of the Novel Coronavirus Disease 2019 (COVID-19) pandemic.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://fpds.gov/wiki/index.php/V1.5_FPDS-NG_Data_Dictionary",
                     "format": "HTML",
-                    "title": "Covid-19 Contract Obligation Tracking Data Dictionary",
-                    "downloadURL": "https://fpds.gov/wiki/index.php/V1.5_FPDS-NG_Data_Dictionary"
+                    "mediaType": "text/html",
+                    "title": "Covid-19 Contract Obligation Tracking Data Dictionary"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://d2d.gsa.gov/report/covid-19-contract-obligation-tracking-dashboard",
                     "format": "html",
-                    "title": "Covid-19 Contract Obligation Tracking Dataset",
-                    "downloadURL": "https://d2d.gsa.gov/report/covid-19-contract-obligation-tracking-dashboard"
+                    "mediaType": "text/html",
+                    "title": "Covid-19 Contract Obligation Tracking Dataset"
                 }
             ],
+            "identifier": "GSA-2021-03-22-01",
             "keyword": [
                 "category",
                 "contract",
@@ -10518,38 +10508,38 @@
                 "socioeconomic",
                 "support services"
             ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
-            ],
             "language": [
                 "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Internal Partner Satisfaction Survey (IPSS)",
-            "description": "This survey collects feedback from GSA employees about the internal support services they receive from staff offices.",
-            "modified": "2021-03-22T20:15:58.771Z",
-            "accessLevel": "non-public",
-            "identifier": "GSA-2021-03-22-02",
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "The information is for internal GSA Employees only.",
+            "modified": "2021-03-25T17:26:22.917Z",
+            "programCode": [
+                "015:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Customer Experience",
+                "name": "Federal Acquisition Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Customer Experience"
+                    "name": "Federal Acquisition Service"
                 }
             },
+            "rights": "true",
+            "title": "COVID-19 Contract Obligation Tracking Dataset"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Camille Tucker",
                 "hasEmail": "mailto:camille.tucker@gsa.gov"
             },
+            "description": "This survey collects feedback from GSA employees about the internal support services they receive from staff offices.",
+            "identifier": "GSA-2021-03-22-02",
             "keyword": [
                 "GSA",
                 "IT support",
@@ -10560,52 +10550,53 @@
                 "support services",
                 "survey"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-03-22T20:15:58.771Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FedRAMP Authorization Letters",
-            "description": "A JSON export of cloud service providers authorized and in process of authorization by FedRAMP, as well as the agencies that use them.",
-            "modified": "2016-12-01",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-07-19-01",
-            "dataQuality": true,
-            "describedBy": "https://github.com/18F/fedramp-micropurchase/blob/master/schema.json",
-            "describedByType": "application/json",
-            "issued": "2016-07-19",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Technology Transformation Service",
+                "name": "Office of Customer Experience",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "General Services Administration"
+                    "name": "Office of Customer Experience"
                 }
             },
+            "rights": "The information is for internal GSA Employees only.",
+            "title": "Internal Partner Satisfaction Survey (IPSS)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Goodrich",
                 "hasEmail": "mailto:matthew.goodrich@gsa.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://github.com/18F/fedramp-micropurchase/blob/master/schema.json",
+            "describedByType": "application/json",
+            "description": "A JSON export of cloud service providers authorized and in process of authorization by FedRAMP, as well as the agencies that use them.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://github.com/18F/fedramp-data/blob/master/data/data.json",
-                    "format": "json",
-                    "title": "FedRAMP Authorization Letters",
                     "describedBy": "https://github.com/18F/fedramp-micropurchase/blob/master/schema.json",
-                    "describedByType": "application/json"
+                    "describedByType": "application/json",
+                    "format": "json",
+                    "title": "FedRAMP Authorization Letters"
                 }
             ],
+            "identifier": "GSA-2016-07-19-01",
+            "issued": "2016-07-19",
             "keyword": [
                 "18F",
                 "FISMA",
@@ -10613,54 +10604,53 @@
                 "cloud",
                 "cloud service providers"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-12-01",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Internal Partner Satisfaction Survey (IPSS) - 2020",
-            "description": "FY20 response data from the GSA Internal Partner Satisfaction Survey.  This survey collects feedback from GSA employees about the internal support services that they receive from staff offices.",
-            "modified": "2021-03-23T14:49:03.654Z",
-            "accessLevel": "non-public",
-            "identifier": "GSA-2021-03-22-03",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "The Internal Partner Satisfaction Survey (IPSS) is an annual study to evaluate the level of service being provided by GSA\u2019s staff offices to their internal customers (i.e., GSA employees).",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Customer Experience",
+                "name": "Technology Transformation Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "General Services Administration"
                 }
             },
-            "isPartOf": "GSA-2021-03-22-02",
+            "title": "FedRAMP Authorization Letters"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Camille Tucker",
                 "hasEmail": "mailto:camille.tucker@gsa.gov"
             },
+            "description": "FY20 response data from the GSA Internal Partner Satisfaction Survey.  This survey collects feedback from GSA employees about the internal support services that they receive from staff offices.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://d2d.gsa.gov/dataset/2020-internal-partner-satisfaction-survey-ipss",
                     "format": "html",
-                    "title": "2020 Internal Partner Satisfaction Survey (IPSS)",
-                    "downloadURL": "https://d2d.gsa.gov/dataset/2020-internal-partner-satisfaction-survey-ipss"
+                    "mediaType": "text/html",
+                    "title": "2020 Internal Partner Satisfaction Survey (IPSS)"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
                     "format": "html",
+                    "mediaType": "text/html",
                     "title": "Internal Partner Satisfaction Survey (IPSS) Data Dictionary"
                 }
             ],
+            "identifier": "GSA-2021-03-22-03",
+            "isPartOf": "GSA-2021-03-22-02",
             "keyword": [
                 "IT support",
                 "acquisition management",
@@ -10671,46 +10661,50 @@
                 "support services",
                 "survey"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-03-23T14:49:03.654Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions Apr-June 2016, 3rd Qtr",
-            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
-            "modified": "2018-11-15",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-08-03-01",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
             "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Customer Experience",
+                "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "General Services Administration"
+                }
+            },
+            "rights": "The Internal Partner Satisfaction Survey (IPSS) is an annual study to evaluate the level of service being provided by GSA\u2019s staff offices to their internal customers (i.e., GSA employees).",
+            "title": "Internal Partner Satisfaction Survey (IPSS) - 2020"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://inventory.data.gov/dataset/31b9e4bb-768f-4851-9e63-b8a9392143cb/resource/68c0a56e-12ff-4019-9752-2729bcad1c96/download/apr-jun-2016-pc-transactions.xlsx",
                     "format": "xls",
-                    "title": "Apr-Jun 2016 PC Transactions",
-                    "downloadURL": "https://inventory.data.gov/dataset/31b9e4bb-768f-4851-9e63-b8a9392143cb/resource/68c0a56e-12ff-4019-9752-2729bcad1c96/download/apr-jun-2016-pc-transactions.xlsx"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Apr-Jun 2016 PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-08-03-01",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "april",
                 "june",
@@ -10718,105 +10712,101 @@
                 "purchase card",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions Apr-June 2016, 3rd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2016, 3rd Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
             "accessLevel": "public",
-            "identifier": "GSA-2016-08-22-01",
-            "dataQuality": true,
-            "issued": "2015-11-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://inventory.data.gov/dataset/af7911e9-5d15-4a07-9b19-1a81204fb2d9/resource/f91650f5-0881-4b82-a6a4-8599ee919cf1/download/networxtotrevfy163rdqtr.xlsx",
                     "format": "xlsx",
-                    "title": "Networx Total Revenue FY16 3rdQtr",
-                    "downloadURL": "https://inventory.data.gov/dataset/af7911e9-5d15-4a07-9b19-1a81204fb2d9/resource/f91650f5-0881-4b82-a6a4-8599ee919cf1/download/networxtotrevfy163rdqtr.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Networx Total Revenue FY16 3rdQtr"
                 }
             ],
+            "identifier": "GSA-2016-08-22-01",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-11-13",
             "keyword": [
                 "Contract",
                 "Networx Telecommunications",
                 "Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Telecommunications Services"
-            ]
+            ],
+            "title": "Networx Business Volume FY2016, 3rd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Internal Partner Satisfaction Survey (IPSS) - 2019",
-            "description": "FY19 response data from the GSA Internal Partner Satisfaction Survey.  This survey collects feedback from GSA employees about the internal support services that they receive from staff offices.",
-            "modified": "2021-03-23T14:38:22.805Z",
             "accessLevel": "non-public",
-            "identifier": "GSA-2021-03-22-04",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "The Internal Partner Satisfaction Survey (IPSS) is an annual study to evaluate the level of service being provided by GSA\u2019s staff offices to their internal customers (i.e., GSA employees).",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Customer Experience",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "General Services Administration"
-                }
-            },
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Camille Tucker",
                 "hasEmail": "mailto:camille.tucker@gsa.gov"
             },
+            "description": "FY19 response data from the GSA Internal Partner Satisfaction Survey.  This survey collects feedback from GSA employees about the internal support services that they receive from staff offices.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://d2d.gsa.gov/dataset/2019-internal-partner-satisfaction-survey-ipss",
                     "format": "html",
-                    "title": "2019-Internal Partner Satisfaction Survey (IPSS)",
-                    "downloadURL": "https://d2d.gsa.gov/dataset/2019-internal-partner-satisfaction-survey-ipss"
+                    "mediaType": "text/html",
+                    "title": "2019-Internal Partner Satisfaction Survey (IPSS)"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://d2d.gsa.gov/document/internal-partner-satisfaction-survey-ipss-data-dictionary",
                     "format": "html",
-                    "title": "Internal Partner Satisfaction Survey (IPSS) Data Dictionary",
-                    "downloadURL": "https://d2d.gsa.gov/document/internal-partner-satisfaction-survey-ipss-data-dictionary"
+                    "mediaType": "text/html",
+                    "title": "Internal Partner Satisfaction Survey (IPSS) Data Dictionary"
                 }
             ],
+            "identifier": "GSA-2021-03-22-04",
             "keyword": [
                 "IT support",
                 "acquisition management",
@@ -10827,94 +10817,99 @@
                 "support services",
                 "survey"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-03-23T14:38:22.805Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "GSA Enterprise Roadmap",
-            "description": "As is described in OMB Memorandum 13-09, the Enterprise Roadmap is an annual summary of information technology (IT) initiatives that implement the agency\u2019s Information Resources Management (IRM) Strategic Plan. OMB will provide the agency Chief Information Officer with specific areas to comment on in the Roadmap with regard to IT mission and support functions that can be more effectively or efficiently provided through shared services or a transfer/termination of functions. OMB will conduct an analysis of Roadmap submissions during October and will engage directly with agencies on these areas of interest as part of the quarterly PortfolioStat review process.",
-            "modified": "2016-09-27",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-09-27-01",
-            "describedByType": "application/pdf",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Customer Experience",
+                "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "General Services Administration"
+                }
             },
+            "rights": "The Internal Partner Satisfaction Survey (IPSS) is an annual study to evaluate the level of service being provided by GSA\u2019s staff offices to their internal customers (i.e., GSA employees).",
+            "title": "Internal Partner Satisfaction Survey (IPSS) - 2019"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jonah Hatfield",
                 "hasEmail": "mailto:jonah.hatfield@gsa.gov"
             },
+            "describedByType": "application/pdf",
+            "description": "As is described in OMB Memorandum 13-09, the Enterprise Roadmap is an annual summary of information technology (IT) initiatives that implement the agency\u2019s Information Resources Management (IRM) Strategic Plan. OMB will provide the agency Chief Information Officer with specific areas to comment on in the Roadmap with regard to IT mission and support functions that can be more effectively or efficiently provided through shared services or a transfer/termination of functions. OMB will conduct an analysis of Roadmap submissions during October and will engage directly with agencies on these areas of interest as part of the quarterly PortfolioStat review process.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "GSA Enterprise Roadmap",
                     "description": "GSA's 2016 Enterprise Roadmap to fulfill OMB's requirements for the September 30, 2016 deadline.",
-                    "downloadURL": "https://inventory.data.gov/dataset/4773ad45-88b0-4a0f-bb0b-fb7173e2f7ba/resource/4d9c4af6-3902-44fd-a450-39e2c4713b48/download/gsa-enterprise-roadmap.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/4773ad45-88b0-4a0f-bb0b-fb7173e2f7ba/resource/4d9c4af6-3902-44fd-a450-39e2c4713b48/download/gsa-enterprise-roadmap.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "GSA Enterprise Roadmap"
                 }
             ],
+            "identifier": "GSA-2016-09-27-01",
             "keyword": [
                 "IT roadmap",
-                "Roadmap",
-                "enterprise roadmap"
-            ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "GSA DCOI Strategic Plan",
-            "description": "Under the Data Center Optimization Initiative (DCOI), covered agencies are required to post DCOI Strategic Plans and updates to their FITARA milestones publicly.",
-            "modified": "2018-02-28",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-09-27-02",
-            "conformsTo": "https://management.cio.gov/schemaexamples/DCOI_StrategicPlans_fy2016Schema.json",
-            "describedByType": "application/json",
+                "Roadmap",
+                "enterprise roadmap"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-09-27",
+            "programCode": [
+                "023:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "title": "GSA Enterprise Roadmap"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "023:00"
+            ],
+            "conformsTo": "https://management.cio.gov/schemaexamples/DCOI_StrategicPlans_fy2016Schema.json",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Teresa Curtis",
                 "hasEmail": "mailto:teresa.curtis@gsa.gov"
             },
+            "describedByType": "application/json",
+            "description": "Under the Data Center Optimization Initiative (DCOI), covered agencies are required to post DCOI Strategic Plans and updates to their FITARA milestones publicly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
-                    "format": "json",
-                    "title": "GSA DCOI Strategic Plan May 2022",
-                    "description": "Under the Data Center Optimization Initiative (DCOI), covered agencies are required to post DCOI Strategic Plans and updates to their FITARA milestones publicly. Updated 11/19/2018 at 8:52 pm Eastern. Updated 05/16/2019 to change tiered closures. Updated on 06/25/2019 to change planned value. Updated on 7/11/2019 to change achieved closures. Updated on 8/5/2019 to change closures for FYs16-20. Updated on 10/7/19 to reflect FY20 Achieved closure values. Updated on 11/15/19 to reflect only \"agency owned\" data centers for closures. Updated on 05/11/2020. Updated 5/17/22.",
                     "conformsTo": "https://management.cio.gov/schemaexamples/DCOI_StrategicPlans_fy2016Schema.json",
-                    "downloadURL": "https://inventory.data.gov/dataset/20d5c816-e31a-46be-81d2-abc59d0f4fdb/resource/b8d9e71b-963b-4398-8d37-04628e64871d/download/datacenteroptimizationstrategicplan.json"
+                    "description": "Under the Data Center Optimization Initiative (DCOI), covered agencies are required to post DCOI Strategic Plans and updates to their FITARA milestones publicly. Updated 11/19/2018 at 8:52 pm Eastern. Updated 05/16/2019 to change tiered closures. Updated on 06/25/2019 to change planned value. Updated on 7/11/2019 to change achieved closures. Updated on 8/5/2019 to change closures for FYs16-20. Updated on 10/7/19 to reflect FY20 Achieved closure values. Updated on 11/15/19 to reflect only \"agency owned\" data centers for closures. Updated on 05/11/2020. Updated 5/17/22.",
+                    "downloadURL": "https://inventory.data.gov/dataset/20d5c816-e31a-46be-81d2-abc59d0f4fdb/resource/b8d9e71b-963b-4398-8d37-04628e64871d/download/datacenteroptimizationstrategicplan.json",
+                    "format": "json",
+                    "mediaType": "application/json",
+                    "title": "GSA DCOI Strategic Plan May 2022"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "pdf",
-                    "title": "DCOI CIO Statement May 2022",
                     "description": "May 8, 2022- GSA has verified that our Strategic Plan is a valid JSON file, conforms to the schema on management.cio.gov/schema, and addresses all of the requirements for it specified in the DCOI. \r\n\r\nIt further confirms that this Strategic Plan has been posted publicly as requested in the template at [agency.gov]/digitalstrategy/datacenteroptimizationstrategicplan.json under the heading \u201cData Center Optimization Initiative Strategic Plans\u201d.",
-                    "downloadURL": "https://inventory.data.gov/dataset/20d5c816-e31a-46be-81d2-abc59d0f4fdb/resource/c61e4b8a-4a4a-46b3-9d95-36d227bc28c3/download/gsa-dcoi-cio-signature.pdf"
+                    "downloadURL": "https://inventory.data.gov/dataset/20d5c816-e31a-46be-81d2-abc59d0f4fdb/resource/c61e4b8a-4a4a-46b3-9d95-36d227bc28c3/download/gsa-dcoi-cio-signature.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "DCOI CIO Statement May 2022"
                 }
             ],
+            "identifier": "GSA-2016-09-27-02",
             "keyword": [
                 "DCOI",
                 "DCOI strategic plan",
@@ -10923,45 +10918,44 @@
                 "fdcci",
                 "strategic plan"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-02-28",
             "programCode": [
                 "023:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "e-Buy Awards for Fiscal Year 2015",
-            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
-            "modified": "2016-09-28",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-09-28-01",
-            "dataQuality": true,
-            "issued": "2015-09-28",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "title": "GSA DCOI Strategic Plan"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-08-31",
+            "bureauCode": [
+                "023:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Usha Gopal",
                 "hasEmail": "mailto:usha.gopal@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "eBuy_Awards_FY2015",
                     "description": "Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
-                    "downloadURL": "https://inventory.data.gov/dataset/81593d91-7c5a-45bd-b159-abe873249e6c/resource/f7344899-2fa2-4bed-92ee-3f1845e9a429/download/ebuyawardsfy2015.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/81593d91-7c5a-45bd-b159-abe873249e6c/resource/f7344899-2fa2-4bed-92ee-3f1845e9a429/download/ebuyawardsfy2015.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "eBuy_Awards_FY2015"
                 }
             ],
+            "identifier": "GSA-2016-09-28-01",
+            "isPartOf": "GSA-2015-08-31",
+            "issued": "2015-09-28",
             "keyword": [
                 "Awards",
                 "Contracts",
@@ -10971,104 +10965,104 @@
                 "e-Buy",
                 "procurement"
             ],
-            "bureauCode": [
-                "023:10"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-09-28",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "e-Buy Awards for Fiscal Year 2015"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA FAS FEDSIM Opportunities",
-            "description": "The Opportunities Dashboard is used to show external client's information about our acquisitions that are in the pre-award state.  Viewers can see high level details that would benefit those that are interested in proposing.",
-            "modified": "2021-03-29T14:49:52.059Z",
             "accessLevel": "non-public",
-            "identifier": "GSA-2021-03-23-01",
-            "describedBy": "https://d2d.gsa.gov/dataset/gsa-fedsim-project-lifecycle-tracker-extractextract",
-            "describedByType": "text/csv",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "Contains information for acquisitions that are in the pre-award state.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Acquisition Service",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Federal Acquisition Service"
-                }
-            },
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ryan Hall",
                 "hasEmail": "mailto:ryan.hall@gsa.gov"
             },
+            "describedBy": "https://d2d.gsa.gov/dataset/gsa-fedsim-project-lifecycle-tracker-extractextract",
+            "describedByType": "text/csv",
+            "description": "The Opportunities Dashboard is used to show external client's information about our acquisitions that are in the pre-award state.  Viewers can see high level details that would benefit those that are interested in proposing.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://d2d.gsa.gov/dataset/gsa-fedsim-project-lifecycle-tracker-extractextract",
                     "format": "html",
-                    "title": "GSA FEDSIM Project Lifecycle Tracker Data Dictionary",
-                    "downloadURL": "https://d2d.gsa.gov/dataset/gsa-fedsim-project-lifecycle-tracker-extractextract"
+                    "mediaType": "text/html",
+                    "title": "GSA FEDSIM Project Lifecycle Tracker Data Dictionary"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://d2d.gsa.gov/report/gsa-fas-fedsim-opportunities-dashboard",
                     "format": "html",
-                    "title": "GSA FAS FEDSIM Opportunities Dashboard",
-                    "downloadURL": "https://d2d.gsa.gov/report/gsa-fas-fedsim-opportunities-dashboard"
+                    "mediaType": "text/html",
+                    "title": "GSA FAS FEDSIM Opportunities Dashboard"
                 }
             ],
+            "identifier": "GSA-2021-03-23-01",
             "keyword": [
                 "FEDSIM",
                 "opportunities"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-03-29T14:49:52.059Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Acquisition Service",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Federal Acquisition Service"
+                }
+            },
+            "rights": "Contains information for acquisitions that are in the pre-award state.",
+            "title": "GSA FAS FEDSIM Opportunities"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions July-Sept 2016, 4th Qtr",
-            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-10-19-01",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://inventory.data.gov/dataset/ac13f165-5085-4cb7-899d-c1c752739d2b/resource/2038528a-592b-494a-b494-33c97cac6c5d/download/july-september-2016-pc-transactions.xlsx",
                     "format": "xls",
-                    "title": "July-September 2016 PC Transactions",
-                    "downloadURL": "https://inventory.data.gov/dataset/ac13f165-5085-4cb7-899d-c1c752739d2b/resource/2038528a-592b-494a-b494-33c97cac6c5d/download/july-september-2016-pc-transactions.xlsx"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "July-September 2016 PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-10-19-01",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "august",
                 "july",
@@ -11076,100 +11070,100 @@
                 "september",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions July-Sept 2016, 4th Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA Apr-June 2016, 3rd Qtr",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-10-19-02",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://inventory.data.gov/dataset/194d3c0b-d938-444d-a49a-ab1c837d2e76/resource/49691000-2c6c-477c-81f1-fbbea8f3ac71/download/april-june-2016-boca-pc-transactions.xlsx",
                     "format": "xlsw",
-                    "title": "April-June 2016 BOCA PC Transactions",
-                    "downloadURL": "https://inventory.data.gov/dataset/194d3c0b-d938-444d-a49a-ab1c837d2e76/resource/49691000-2c6c-477c-81f1-fbbea8f3ac71/download/april-june-2016-boca-pc-transactions.xlsx"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "April-June 2016 BOCA PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-10-19-02",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "GSA SmartPay",
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA Apr-June 2016, 3rd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA July-Sept 2016, 4th Qtr",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2016-10-19-03",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://inventory.data.gov/dataset/d1575481-b864-4e44-98d9-692d0e64a964/resource/d03c71d3-2e51-4b3c-9ced-79e88b9adc91/download/july-september-2016-boca-pc-transactions.xlsx",
                     "format": "xls",
-                    "title": "July-September 2016 BOCA PC Transactions",
-                    "downloadURL": "https://inventory.data.gov/dataset/d1575481-b864-4e44-98d9-692d0e64a964/resource/d03c71d3-2e51-4b3c-9ced-79e88b9adc91/download/july-september-2016-boca-pc-transactions.xlsx"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "July-September 2016 BOCA PC Transactions"
                 }
             ],
+            "identifier": "GSA-2016-10-19-03",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Contract Board",
@@ -11177,73 +11171,69 @@
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA July-Sept 2016, 4th Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "FY21 Enterprise Infrastructure Solutions (EIS) Quarterly Reports",
-            "description": "This dataset represents the EIS business volume of each government agency that has ordered telecommunication services from the EIS contract.  This contains data from FY2021.",
-            "modified": "2021-03-25T16:31:46.260Z",
             "accessLevel": "public",
-            "identifier": "GSA-2021-03-25-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Acquisition Service",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Federal Acquisition Service"
-                }
-            },
-            "isPartOf": "GSA-2020-06-26-01",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Loren Smith",
                 "hasEmail": "mailto:loren.smith@gsa.gov"
             },
+            "description": "This dataset represents the EIS business volume of each government agency that has ordered telecommunication services from the EIS contract.  This contains data from FY2021.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/1ce62e42-2604-4102-8119-3355e45903bc/resource/19b30ede-1083-44f4-97af-f022eb0b75b2/download/eistotrevfy21_q1.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "EISTotRevFY21_Q1",
-                    "downloadURL": "https://inventory.data.gov/dataset/1ce62e42-2604-4102-8119-3355e45903bc/resource/19b30ede-1083-44f4-97af-f022eb0b75b2/download/eistotrevfy21_q1.xlsx"
+                    "title": "EISTotRevFY21_Q1"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://inventory.data.gov/dataset/1ce62e42-2604-4102-8119-3355e45903bc/resource/2a9bd8cf-f847-46f5-941e-d9de57350f55/download/eistotrevfy21_q2.xlsx",
                     "format": "xlsx",
-                    "title": "EISTotRevFY21_Q2",
-                    "downloadURL": "https://inventory.data.gov/dataset/1ce62e42-2604-4102-8119-3355e45903bc/resource/2a9bd8cf-f847-46f5-941e-d9de57350f55/download/eistotrevfy21_q2.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EISTotRevFY21_Q2"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "EISTotRevFY21_Q3",
                     "description": "EISTotRevFY21_Q3",
-                    "downloadURL": "https://inventory.data.gov/dataset/1ce62e42-2604-4102-8119-3355e45903bc/resource/4e75cd88-db6a-4db6-991a-93c275af7d0f/download/eistotrevfy21_q3.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/1ce62e42-2604-4102-8119-3355e45903bc/resource/4e75cd88-db6a-4db6-991a-93c275af7d0f/download/eistotrevfy21_q3.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EISTotRevFY21_Q3"
                 },
                 {
-                    "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "EISTotRevFY21_Q4",
+                    "@type": "dcat:Distribution",
                     "description": "EISTotRevFY21_Q4",
-                    "downloadURL": "https://inventory.data.gov/dataset/1ce62e42-2604-4102-8119-3355e45903bc/resource/54ddaae3-9014-48fe-a999-4673f4429fa2/download/eistotrevfy21_q4.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/1ce62e42-2604-4102-8119-3355e45903bc/resource/54ddaae3-9014-48fe-a999-4673f4429fa2/download/eistotrevfy21_q4.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EISTotRevFY21_Q4"
                 }
             ],
+            "identifier": "GSA-2021-03-25-01",
+            "isPartOf": "GSA-2020-06-26-01",
             "keyword": [
                 "EIS",
                 "business-volume",
@@ -11251,137 +11241,138 @@
                 "gsa",
                 "telecommunications"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-03-25T16:31:46.260Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Acquisition Service",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Federal Acquisition Service"
+                }
+            },
+            "rights": "true",
+            "title": "FY21 Enterprise Infrastructure Solutions (EIS) Quarterly Reports"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA IT Policy Archive Zip",
-            "description": "A compressed zip file containing all of GSA's public IT policy documents, posted publicly at gsa.gov]/digitalstrategy/policyarchive.zip and identified in the agency public data listing as \u201cAgency IT Policy Archive\u201d.",
-            "modified": "2019-01-30",
             "accessLevel": "public",
-            "identifier": "GSA-2016-11-02-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Karen Overall",
                 "hasEmail": "mailto:karen.overall@gsa.gov"
             },
+            "description": "A compressed zip file containing all of GSA's public IT policy documents, posted publicly at gsa.gov]/digitalstrategy/policyarchive.zip and identified in the agency public data listing as \u201cAgency IT Policy Archive\u201d.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "GSA IT Policy Archive Zip",
                     "description": "Last update: 2024-11-12",
-                    "downloadURL": "https://inventory.data.gov/dataset/08a7a4da-f414-498c-858b-076fdc7da31a/resource/4a87172f-af14-4cf1-a024-e9fb04c0ac2d/download/gsa-it-policy-archive-zip.zip"
+                    "downloadURL": "https://inventory.data.gov/dataset/08a7a4da-f414-498c-858b-076fdc7da31a/resource/4a87172f-af14-4cf1-a024-e9fb04c0ac2d/download/gsa-it-policy-archive-zip.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "GSA IT Policy Archive Zip"
                 }
             ],
+            "identifier": "GSA-2016-11-02-01",
             "keyword": [
                 "Agency IT Policy Archive",
                 "IT policy archive",
                 "policy archive"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-01-30",
             "programCode": [
                 "023:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2016, 4th Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-06-12",
-            "accessLevel": "public",
-            "identifier": "GSA-2016-11-29-01",
-            "dataQuality": true,
-            "issued": "2015-11-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "title": "GSA IT Policy Archive Zip"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://inventory.data.gov/dataset/8b70220b-ebbd-4ebe-b8b4-2b982114574c/resource/b3b8c595-762d-4b13-9c99-d9726e346aec/download/networxtotrevfy164thqtr.xlsx",
                     "format": "xlsx",
-                    "title": "Networx TotRevFY16_4thQtr",
-                    "downloadURL": "https://inventory.data.gov/dataset/8b70220b-ebbd-4ebe-b8b4-2b982114574c/resource/b3b8c595-762d-4b13-9c99-d9726e346aec/download/networxtotrevfy164thqtr.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Networx TotRevFY16_4thQtr"
                 }
             ],
+            "identifier": "GSA-2016-11-29-01",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-11-13",
             "keyword": [
                 "Contract",
                 "Networx Telecommunications",
                 "Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-06-12",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Telecommunications Services"
-            ]
+            ],
+            "title": "Networx Business Volume FY2016, 4th Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "IT Standards Profile List",
-            "description": "A JSON export of the GSA IT Standards Profile.",
-            "modified": "2016-12-01",
             "accessLevel": "public",
-            "identifier": "GSA-2016-12-01-01",
-            "dataQuality": true,
-            "describedByType": "application/json",
-            "issued": "2016-09-07",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Chief Technology Officer",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "General Services Administration"
-                }
-            },
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chris Campbell",
                 "hasEmail": "mailto:christopher.campbell@gsa.gov"
             },
+            "dataQuality": true,
+            "describedByType": "application/json",
+            "description": "A JSON export of the GSA IT Standards Profile.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://raw.githubusercontent.com/GSA/data/gh-pages/enterprise-architecture/it-standards.csv",
+                    "description": "https://github.com/GSA/data/tree/gh-pages/enterprise-architecture",
                     "format": "json",
-                    "title": "GSA IT Standards Profile",
-                    "description": "https://github.com/GSA/data/tree/gh-pages/enterprise-architecture"
+                    "title": "GSA IT Standards Profile"
                 }
             ],
+            "identifier": "GSA-2016-12-01-01",
+            "issued": "2016-09-07",
             "keyword": [
                 "GSA",
                 "SaaS",
@@ -11389,47 +11380,50 @@
                 "compliance",
                 "software"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-12-01",
             "programCode": [
                 "023:008"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "e-Buy Awards for Fiscal Year 2016",
-            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
-            "modified": "2017-01-10",
-            "accessLevel": "public",
-            "identifier": "GSA-2017-01-09-01",
-            "dataQuality": true,
-            "issued": "2015-09-28",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
             "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Chief Technology Officer",
+                "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "General Services Administration"
+                }
             },
+            "title": "IT Standards Profile List"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "GSA-2015-08-31",
+            "bureauCode": [
+                "023:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Usha Gopal",
                 "hasEmail": "mailto:usha.gopal@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "GSA e-Buy, is an electronic Request for Quote (RFQ) / Request for Proposal (RFP) system designed to allow government buyers to request information, find sources, and prepare RFQs/RFPs, online, for millions of services and products offered through GSA's Multiple Award Schedule (MAS) and GSA Technology Contracts. Government buyers can use eBuy to obtain quotes or proposals for services, large quantity purchases, big ticket items, and purchases with complex requirements. Buyers may use e-Buy to evaluate and accept the quotation that represents the best value. Buyers may then make award to any contractor whose quotation was accepted. The e-Buy Award dataset are the award data collected by e-Buy for a given fiscal year.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://inventory.data.gov/dataset/2d2da689-5342-4024-b9e1-fb6bc9ec79eb/resource/64873a3a-432f-46f4-96e5-4fd0189f71ac/download/ebuyawardsfy2016.xlsx",
                     "format": "xlsx",
-                    "title": "eBuy_Awards_FY2016",
-                    "downloadURL": "https://inventory.data.gov/dataset/2d2da689-5342-4024-b9e1-fb6bc9ec79eb/resource/64873a3a-432f-46f4-96e5-4fd0189f71ac/download/ebuyawardsfy2016.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "eBuy_Awards_FY2016"
                 }
             ],
+            "identifier": "GSA-2017-01-09-01",
+            "isPartOf": "GSA-2015-08-31",
+            "issued": "2015-09-28",
             "keyword": [
                 "Awards",
                 "Contracts",
@@ -11439,74 +11433,59 @@
                 "e-Buy",
                 "procurement"
             ],
-            "bureauCode": [
-                "023:10"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2017-01-10",
             "programCode": [
                 "023:007"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Acquisition"
-            ]
+            ],
+            "title": "e-Buy Awards for Fiscal Year 2016"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA FAS CASE 10x10 Open Market Expirations FY20-21",
-            "description": "List of open market opportunities from FPDS FAS CASE is targeting for conversion to a FAS solution",
-            "modified": "2021-03-30T14:38:07.484Z",
             "accessLevel": "non-public",
-            "identifier": "GSA-2021-03-30-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "This data represent definitive open market contracts from FPDS expiring FY20-21 that FAS CASE is targeting in FY20 for possible conversion to a FAS contract vehicle.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Acquisition Service",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "General Services Administration"
-                }
-            },
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sven Carlson",
                 "hasEmail": "mailto:sven.carlson@gsa.gov"
             },
+            "description": "List of open market opportunities from FPDS FAS CASE is targeting for conversion to a FAS solution",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://d2d.gsa.gov/dataset/gsa-fas-case-10x10-open-market-expirations-fy20-21-0",
                     "format": "html",
-                    "title": "10x10 Integrated Opportunity Management",
-                    "downloadURL": "https://d2d.gsa.gov/dataset/gsa-fas-case-10x10-open-market-expirations-fy20-21-0"
+                    "mediaType": "text/html",
+                    "title": "10x10 Integrated Opportunity Management"
                 }
             ],
+            "identifier": "GSA-2021-03-30-01",
             "keyword": [
                 "10x10",
                 "CASE",
                 "open market"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-03-30T14:38:07.484Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "GSA FAS CASE 10x10 Open Market Expirations FY21-22",
-            "description": "List of open market opportunities from FPDS FAS CASE is targeting for conversion to a FAS solution",
-            "modified": "2021-03-30T14:45:49.143Z",
-            "accessLevel": "non-public",
-            "identifier": "GSA-2021-03-30-02",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "This data represent definitive open market contracts from FPDS expiring FY21-22 that FAS CASE is targeting in FY21 for possible conversion to a FAS contract vehicle.",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Acquisition Service",
@@ -11515,44 +11494,44 @@
                     "name": "General Services Administration"
                 }
             },
+            "rights": "This data represent definitive open market contracts from FPDS expiring FY20-21 that FAS CASE is targeting in FY20 for possible conversion to a FAS contract vehicle.",
+            "title": "GSA FAS CASE 10x10 Open Market Expirations FY20-21"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sven Carlson",
                 "hasEmail": "mailto:sven.carlson@gsa.gov"
             },
+            "description": "List of open market opportunities from FPDS FAS CASE is targeting for conversion to a FAS solution",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://d2d.gsa.gov/dataset/gsa-fas-case-10x10-open-market-expirations-fy21-22",
                     "format": "html",
-                    "title": "10x10 Integrated Opportunity Management",
-                    "downloadURL": "https://d2d.gsa.gov/dataset/gsa-fas-case-10x10-open-market-expirations-fy21-22"
+                    "mediaType": "text/html",
+                    "title": "10x10 Integrated Opportunity Management"
                 }
             ],
+            "identifier": "GSA-2021-03-30-02",
             "keyword": [
                 "10x10",
                 "CASE",
                 "open market"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-03-30T14:45:49.143Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Award Exploration Tool",
-            "description": "Interactive query tool designed to support in-depth data exploration and exports; users are able to search for specific award records, query expiring contracts, and export line item data with added Category Management enrichments such as Level 1/2 categories, SUM Tier, Addressable BIC / Tier 2 Contract, Contract Name (if applicable).",
-            "modified": "2021-03-30T15:14:53.668Z",
-            "accessLevel": "public",
-            "identifier": "GSA-2021-03-30-03",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Acquisition Service",
@@ -11561,20 +11540,31 @@
                     "name": "General Services Administration"
                 }
             },
+            "rights": "This data represent definitive open market contracts from FPDS expiring FY21-22 that FAS CASE is targeting in FY21 for possible conversion to a FAS contract vehicle.",
+            "title": "GSA FAS CASE 10x10 Open Market Expirations FY21-22"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kristen Wilson",
                 "hasEmail": "mailto:govtwidecmdashboards@gsa.gov"
             },
+            "description": "Interactive query tool designed to support in-depth data exploration and exports; users are able to search for specific award records, query expiring contracts, and export line item data with added Category Management enrichments such as Level 1/2 categories, SUM Tier, Addressable BIC / Tier 2 Contract, Contract Name (if applicable).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://d2d.gsa.gov/report/government-wide-category-management-contract-management-and-operational-reporting-tools",
                     "format": "html",
-                    "title": "Award Exploration Tool",
-                    "downloadURL": "https://d2d.gsa.gov/report/government-wide-category-management-contract-management-and-operational-reporting-tools"
+                    "mediaType": "text/html",
+                    "title": "Award Exploration Tool"
                 }
             ],
+            "identifier": "GSA-2021-03-30-03",
             "keyword": [
                 "award",
                 "category management",
@@ -11583,25 +11573,14 @@
                 "obligation",
                 "vendor"
             ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
-            ],
             "language": [
                 "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Contract Inventory Exploration Tool",
-            "description": "Simple reference for agency and category teams to search and export all tier rated contract information, including the enhanced fields used by the data team to determine the master and derivative contract information required to determine the appropriate tier level.",
-            "modified": "2021-03-30T15:24:06.013Z",
-            "accessLevel": "public",
-            "identifier": "GSA-2021-03-30-04",
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
+            "modified": "2021-03-30T15:14:53.668Z",
+            "programCode": [
+                "015:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Acquisition Service",
@@ -11610,20 +11589,31 @@
                     "name": "General Services Administration"
                 }
             },
+            "rights": "true",
+            "title": "Award Exploration Tool"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kristen Wilson",
                 "hasEmail": "mailto:govtwidecmdashboards@gsa.gov"
             },
+            "description": "Simple reference for agency and category teams to search and export all tier rated contract information, including the enhanced fields used by the data team to determine the master and derivative contract information required to determine the appropriate tier level.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://d2d.gsa.gov/report/government-wide-category-management-contract-management-and-operational-reporting-tools",
                     "format": "html",
-                    "title": "Contract Inventory Exploration Tool",
-                    "downloadURL": "https://d2d.gsa.gov/report/government-wide-category-management-contract-management-and-operational-reporting-tools"
+                    "mediaType": "text/html",
+                    "title": "Contract Inventory Exploration Tool"
                 }
             ],
+            "identifier": "GSA-2021-03-30-04",
             "keyword": [
                 "category management",
                 "contract",
@@ -11631,25 +11621,14 @@
                 "exploration",
                 "vendor"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-03-30T15:24:06.013Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "GSS Contractor Performance",
-            "description": "This dashboard provides insight into the shipping, tracking, delivery, transition to EDI/Contractor Portal etc. from Fax contractors etc.",
-            "modified": "2021-03-30T15:49:31.045Z",
-            "accessLevel": "non-public",
-            "identifier": "GSA-2021-03-30-05",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "This dataset contains contracting performance data.",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Acquisition Service",
@@ -11658,20 +11637,31 @@
                     "name": "General Services Administration"
                 }
             },
+            "rights": "true",
+            "title": "Contract Inventory Exploration Tool"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lloyd Aucoin",
                 "hasEmail": "mailto:lloyd.aucoin@gsa.gov"
             },
+            "description": "This dashboard provides insight into the shipping, tracking, delivery, transition to EDI/Contractor Portal etc. from Fax contractors etc.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://d2d.gsa.gov/report/gsa-fas-gss-contractor-performance-dashboard",
                     "format": "html",
-                    "title": "GSS Contractor Performance",
-                    "downloadURL": "https://d2d.gsa.gov/report/gsa-fas-gss-contractor-performance-dashboard"
+                    "mediaType": "text/html",
+                    "title": "GSS Contractor Performance"
                 }
             ],
+            "identifier": "GSA-2021-03-30-05",
             "keyword": [
                 "contracts",
                 "global supply",
@@ -11679,46 +11669,50 @@
                 "shipment data",
                 "transactions"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-03-30T15:49:31.045Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions Oct-Dec 2016, 1st Qtr",
-            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
-            "modified": "2018-11-15",
-            "accessLevel": "public",
-            "identifier": "GSA-2017-02-15-01",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
             "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Acquisition Service",
+                "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "General Services Administration"
+                }
             },
+            "rights": "This dataset contains contracting performance data.",
+            "title": "GSS Contractor Performance"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card. Files will be batched quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://inventory.data.gov/dataset/f81f1981-067b-47ad-84b3-19c0a9015e73/resource/fe9948b2-863d-4bed-8dd9-44d9c3c4e3a7/download/oct-dec-2016-gsa-pc-transactions.xlsx",
                     "format": "xls",
-                    "title": "Oct-Dec 2016 GSA PC Transactions",
-                    "downloadURL": "https://inventory.data.gov/dataset/f81f1981-067b-47ad-84b3-19c0a9015e73/resource/fe9948b2-863d-4bed-8dd9-44d9c3c4e3a7/download/oct-dec-2016-gsa-pc-transactions.xlsx"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oct-Dec 2016 GSA PC Transactions"
                 }
             ],
+            "identifier": "GSA-2017-02-15-01",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "december",
                 "november",
@@ -11726,50 +11720,50 @@
                 "purchase card",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions Oct-Dec 2016, 1st Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA Oct-Dec 2016, 1st Qtr",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2017-02-15-02",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://inventory.data.gov/dataset/cad93b17-6283-4b32-b8e7-92d37243baf5/resource/52a9a326-683a-4e86-ae02-235d9e8314b1/download/oct-dec-2016-cbca-pc-transactions.xlsx",
                     "format": "xls",
-                    "title": "Oct-Dec 2016 CBCA PC Transactions",
-                    "downloadURL": "https://inventory.data.gov/dataset/cad93b17-6283-4b32-b8e7-92d37243baf5/resource/52a9a326-683a-4e86-ae02-235d9e8314b1/download/oct-dec-2016-cbca-pc-transactions.xlsx"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oct-Dec 2016 CBCA PC Transactions"
                 }
             ],
+            "identifier": "GSA-2017-02-15-02",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Contract Board",
@@ -11777,146 +11771,146 @@
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA Oct-Dec 2016, 1st Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2017, 1st Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2017-02-15-03",
-            "dataQuality": true,
-            "issued": "2015-11-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://inventory.data.gov/dataset/79940556-3b58-45e6-b358-666aac8678ed/resource/0b0244cc-9c6f-46bf-8779-9468a178cc54/download/totrevfy171stqtr.xlsx",
                     "format": "xlsx",
-                    "title": "TotRevFY17_1stQtr",
-                    "downloadURL": "https://inventory.data.gov/dataset/79940556-3b58-45e6-b358-666aac8678ed/resource/0b0244cc-9c6f-46bf-8779-9468a178cc54/download/totrevfy171stqtr.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY17_1stQtr"
                 }
             ],
+            "identifier": "GSA-2017-02-15-03",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-11-13",
             "keyword": [
                 "Contract",
                 "Networx Telecommunications",
                 "Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Telecommunications Services"
-            ]
+            ],
+            "title": "Networx Business Volume FY2017, 1st Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2019, 3rd Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-08-19",
             "accessLevel": "public",
-            "identifier": "GSA-2019-08-19-01",
-            "dataQuality": true,
-            "issued": "2015-11-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "TotRevFY19_3rdQtr",
                     "description": "TotRevFY19_3rdQtr",
-                    "downloadURL": "https://inventory.data.gov/dataset/1a757d61-6861-42a0-bc72-8a1cf7379959/resource/2a13a13e-0278-4e1e-ad90-f817f96d7251/download/totrevfy193rdqtr.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/1a757d61-6861-42a0-bc72-8a1cf7379959/resource/2a13a13e-0278-4e1e-ad90-f817f96d7251/download/totrevfy193rdqtr.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY19_3rdQtr"
                 }
             ],
+            "identifier": "GSA-2019-08-19-01",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-11-13",
             "keyword": [
                 "Contract",
                 "Networx Telecommunications",
                 "Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-08-19",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Telecommunications Services"
-            ]
+            ],
+            "title": "Networx Business Volume FY2019, 3rd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions July-Sept 2018, 4th Qtr",
-            "description": "Purchases made with the purchase card.  Files will be batched quarterly.",
-            "modified": "2020-02-04",
             "accessLevel": "public",
-            "identifier": "GSA-2019-09-13-01",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Purchases made with the purchase card.  Files will be batched quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://inventory.data.gov/dataset/884d6e78-bc25-4664-8828-9e6fdc228f3f/resource/7424a889-8941-44c8-a819-0a97bb415fda/download/jul-sep-2018-gsa-pc-transactions.xlsx",
                     "format": "xlsx",
-                    "title": "Jul-Sep 2018 GSA PC Transactions",
-                    "downloadURL": "https://inventory.data.gov/dataset/884d6e78-bc25-4664-8828-9e6fdc228f3f/resource/7424a889-8941-44c8-a819-0a97bb415fda/download/jul-sep-2018-gsa-pc-transactions.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Jul-Sep 2018 GSA PC Transactions"
                 }
             ],
+            "identifier": "GSA-2019-09-13-01",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "august",
                 "july",
@@ -11924,50 +11918,50 @@
                 "september",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-02-04",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions July-Sept 2018, 4th Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GSA Purchase Card Transactions Jan-Mar 2017, 2nd Qtr",
-            "description": "2nd Quarter 2017 Purchase Card Transactions",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2017-04-13-01",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-05-01",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy V Hexmoor",
                 "hasEmail": "mailto:nancy.hexmoor@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "2nd Quarter 2017 Purchase Card Transactions",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "Jan - Mar 2017 GSA PC Transactions",
                     "description": "2nd Quarter 2017 Purchase Card Transactions",
-                    "downloadURL": "https://inventory.data.gov/dataset/b328789a-a070-446e-982a-a5b1a0984fa2/resource/c9858a44-dc63-49ef-903f-066651255330/download/jan-mar-2017-gsa-pc-transactions.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/b328789a-a070-446e-982a-a5b1a0984fa2/resource/c9858a44-dc63-49ef-903f-066651255330/download/jan-mar-2017-gsa-pc-transactions.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Jan - Mar 2017 GSA PC Transactions"
                 }
             ],
+            "identifier": "GSA-2017-04-13-01",
+            "isPartOf": "GSA-2016-01-05-01",
             "keyword": [
                 "february",
                 "january",
@@ -11975,50 +11969,50 @@
                 "purchase card",
                 "transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "GSA Purchase Card Transactions Jan-Mar 2017, 2nd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA Jan-Mar 2017, 2nd Qtr",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2017-05-04-01",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://inventory.data.gov/dataset/31ffade7-a9ee-448b-b1d6-84963835db22/resource/e84b68b1-cf6d-47d8-ae2d-6398d2a00ecf/download/january-march-2017-cbca-pc-transactions.xlsx",
                     "format": "xls",
-                    "title": "January - March 2017",
-                    "downloadURL": "https://inventory.data.gov/dataset/31ffade7-a9ee-448b-b1d6-84963835db22/resource/e84b68b1-cf6d-47d8-ae2d-6398d2a00ecf/download/january-march-2017-cbca-pc-transactions.xlsx"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "January - March 2017"
                 }
             ],
+            "identifier": "GSA-2017-05-04-01",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Contract Board",
@@ -12026,137 +12020,133 @@
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA Jan-Mar 2017, 2nd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2017, 2nd Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2018-11-15",
             "accessLevel": "public",
-            "identifier": "GSA-2017-05-22-01",
-            "dataQuality": true,
-            "issued": "2015-11-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://inventory.data.gov/dataset/169ff953-901f-48e4-b8e6-e27765473f06/resource/12c1d44d-2a95-45d4-8635-0c30e707514c/download/totrevfy172ndqtr.xlsx",
                     "format": "xlsx",
-                    "title": "TotRevFY17_2ndQtr",
-                    "downloadURL": "https://inventory.data.gov/dataset/169ff953-901f-48e4-b8e6-e27765473f06/resource/12c1d44d-2a95-45d4-8635-0c30e707514c/download/totrevfy172ndqtr.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY17_2ndQtr"
                 }
             ],
+            "identifier": "GSA-2017-05-22-01",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-11-13",
             "keyword": [
                 "Contract",
                 "Networx Telecommunications",
                 "Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-11-15",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Telecommunications Services"
-            ]
+            ],
+            "title": "Networx Business Volume FY2017, 2nd Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GEAR API Metadata",
-            "description": "The available API metadata from the GSA Enterprise Architecture Analytics and Reporting (GEAR) web application.",
-            "modified": "2017-06-08",
             "accessLevel": "public",
-            "identifier": "GSA-2017-06-08-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "GSA IT"
-            },
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chris Campbell",
                 "hasEmail": "mailto:christopher.campbell@gsa.gov"
             },
+            "description": "The available API metadata from the GSA Enterprise Architecture Analytics and Reporting (GEAR) web application.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
-                    "format": "JSON",
-                    "title": "GEAR Metadata placeholder",
                     "description": "This is just a placeholder for now. Data coming soon.",
-                    "downloadURL": "https://inventory.data.gov/dataset/7402f817-4297-4bb1-89d1-4b586bd89cd2/resource/71b180af-5f0d-4f04-9059-20e80e6816a1/download/gear-metadata.json"
+                    "downloadURL": "https://inventory.data.gov/dataset/7402f817-4297-4bb1-89d1-4b586bd89cd2/resource/71b180af-5f0d-4f04-9059-20e80e6816a1/download/gear-metadata.json",
+                    "format": "JSON",
+                    "mediaType": "application/json",
+                    "title": "GEAR Metadata placeholder"
                 }
             ],
+            "identifier": "GSA-2017-06-08-01",
             "keyword": [
                 "Enterprise Architecture",
                 "GEAR",
                 "GEAR API",
                 "GSA EA"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2017-06-08",
             "programCode": [
                 "023:000"
-            ]
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "GSA IT"
+            },
+            "title": "GEAR API Metadata"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "FY 2020 Federal Real Property Profile Data for Civilian Agencies",
-            "description": "A csv export of data from FRPP, a database of Federal real property for civilian agencies.",
-            "modified": "2021-11-05T13:54:47.294Z",
             "accessLevel": "public",
-            "identifier": "GSA-2021-04-27-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Government-wide Policy",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of Government-wide Policy"
-                }
-            },
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elizabeth Fahey",
                 "hasEmail": "mailto:elizabeth.fahey@gsa.gov"
             },
+            "description": "A csv export of data from FRPP, a database of Federal real property for civilian agencies.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/a1072b46-cf6b-443e-bfa2-dad7f1ab4195/resource/8dcd5905-35a9-4294-ac8e-c29732dd437e/download/frpp_public_dataset_fy2020_final_update_10012021.csv",
                     "mediaType": "text/csv",
-                    "title": "FRPP_Public_Dataset_FY2020_Final_Update_10012021.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/a1072b46-cf6b-443e-bfa2-dad7f1ab4195/resource/8dcd5905-35a9-4294-ac8e-c29732dd437e/download/frpp_public_dataset_fy2020_final_update_10012021.csv"
+                    "title": "FRPP_Public_Dataset_FY2020_Final_Update_10012021.csv"
                 }
             ],
+            "identifier": "GSA-2021-04-27-01",
             "keyword": [
                 "FRPP",
                 "Federal Real Property Profile",
@@ -12172,99 +12162,99 @@
                 "structure",
                 "warehouse"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-11-05T13:54:47.294Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2021, 2nd Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contract, by Fiscal Year, Contract, Contract Vehicle, Agency and month for the Central and Direct billing accounts.",
-            "modified": "2022-02-14T13:31:40.299Z",
-            "accessLevel": "public",
-            "identifier": "GSA-2021-05-07-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Federal Acquisition Service",
+                "name": "Office of Government-wide Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Federal Acquisition Service"
+                    "name": "Office of Government-wide Policy"
                 }
             },
-            "isPartOf": "GSA-2015-08-27",
+            "rights": "true",
+            "title": "FY 2020 Federal Real Property Profile Data for Civilian Agencies"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contract, by Fiscal Year, Contract, Contract Vehicle, Agency and month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/ceb336ce-eabd-476c-9bbe-8e023f980c72/resource/ec8a23ef-cc7f-4547-bb72-c8e43cb7e500/download/totrevfy21_2ndqtr.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "TotRevFY21_2ndQtr.xlsx",
-                    "downloadURL": "https://inventory.data.gov/dataset/ceb336ce-eabd-476c-9bbe-8e023f980c72/resource/ec8a23ef-cc7f-4547-bb72-c8e43cb7e500/download/totrevfy21_2ndqtr.xlsx"
+                    "title": "TotRevFY21_2ndQtr.xlsx"
                 }
             ],
+            "identifier": "GSA-2021-05-07-01",
+            "isPartOf": "GSA-2015-08-27",
             "keyword": [
                 "Networx",
                 "Networx Telecommunications",
                 "networx business volume"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-02-14T13:31:40.299Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FY2020 Federal Real Property Profile (FRPP) Summary Data by Installation Name",
-            "description": "A XLSX export of summarized data for specified assets contained within the FRPP, a database of Federal Real Property for executive agencies, are not included in the detailed level dataset..",
-            "modified": "2023-10-06T19:08:36.619Z",
-            "accessLevel": "public",
-            "identifier": "GSA-2021-05-13-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Government-wide Policy",
+                "name": "Federal Acquisition Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Government-wide Policy"
+                    "name": "Federal Acquisition Service"
                 }
             },
+            "rights": "true",
+            "title": "Networx Business Volume FY2021, 2nd Qtr"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elizabeth Fahey",
                 "hasEmail": "mailto:elizabeth.fahey@gsa.gov"
             },
+            "description": "A XLSX export of summarized data for specified assets contained within the FRPP, a database of Federal Real Property for executive agencies, are not included in the detailed level dataset..",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "FY 2020 FRPP Summarized Data by Installation Name 6.16.21",
-                    "description": "A XLSX export of summarized data for specified assets contained within the FRPP, a database of Federal Real Property for executive agencies, that cannot be made public at a detailed level.",
                     "describedBy": "https://www.gsa.gov/cdnstatic/FY_2020_FRPP_DATA_DICTIONARY_v2_final2.pdf",
-                    "downloadURL": "https://inventory.data.gov/dataset/ec3eec46-f136-43f7-a6e5-94e76be89104/resource/2c82571a-1af4-4797-a7cf-24a65eacfba9/download/fy-2020-frpp-summarized-data-by-installation-6.16.21.xlsx"
+                    "description": "A XLSX export of summarized data for specified assets contained within the FRPP, a database of Federal Real Property for executive agencies, that cannot be made public at a detailed level.",
+                    "downloadURL": "https://inventory.data.gov/dataset/ec3eec46-f136-43f7-a6e5-94e76be89104/resource/2c82571a-1af4-4797-a7cf-24a65eacfba9/download/fy-2020-frpp-summarized-data-by-installation-6.16.21.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2020 FRPP Summarized Data by Installation Name 6.16.21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "conformsTo": "http://www.isotc211.org/2005/gmd"
                 }
             ],
+            "identifier": "GSA-2021-05-13-01",
             "keyword": [
                 "FRPP",
                 "Federal Real Property Profile",
@@ -12275,25 +12265,14 @@
                 "real property",
                 "structure"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-10-06T19:08:36.619Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Tenant Satisfaction Survey (TSS) Reports",
-            "description": "This is a collection of TSS reports both at the individual and summary level.  The reports are for the following Fiscal Years; 2017, 2018, and 2019.  There is a data dictionary for the Individual Results and a data dictionary for the Summarized Results.",
-            "modified": "2021-05-26T12:11:56.111Z",
-            "accessLevel": "non-public",
-            "identifier": "GSA-2021-05-24-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "The POC for this collection of reports stated the information is 'Restricted'.",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Government-wide Policy",
@@ -12302,11 +12281,22 @@
                     "name": "Office of Government-wide Policy"
                 }
             },
+            "rights": "true",
+            "title": "FY2020 Federal Real Property Profile (FRPP) Summary Data by Installation Name"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Aaron Eisenbarth",
                 "hasEmail": "mailto:aaron.eisenbarth@gsa.gov"
             },
+            "description": "This is a collection of TSS reports both at the individual and summary level.  The reports are for the following Fiscal Years; 2017, 2018, and 2019.  There is a data dictionary for the Individual Results and a data dictionary for the Summarized Results.",
+            "identifier": "GSA-2021-05-24-01",
             "keyword": [
                 "Cleanliness",
                 "Happiness",
@@ -12319,25 +12309,14 @@
                 "satisfaction",
                 "tenant"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-05-26T12:11:56.111Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FY18 Tenant Satisfaction Survey (TSS) Summarized Results",
-            "description": "A CSV export of Tenant Satisfaction Survey (TSS) results summarized at the building and individual question level.",
-            "modified": "2021-05-25T17:00:57.825Z",
-            "accessLevel": "non-public",
-            "identifier": "GSA-2021-05-24-05",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "The POC for this report has stated this report is Restricted.",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Government-wide Policy",
@@ -12346,19 +12325,30 @@
                     "name": "Office of Government-wide Policy"
                 }
             },
+            "rights": "The POC for this collection of reports stated the information is 'Restricted'.",
+            "title": "Tenant Satisfaction Survey (TSS) Reports"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Aaron Eisenbarth",
                 "hasEmail": "mailto:aaron.eisenbarth@gsa.gov"
             },
+            "description": "A CSV export of Tenant Satisfaction Survey (TSS) results summarized at the building and individual question level.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/260d9579-065a-4ce0-a79e-e780b9bf27bb/resource/319ba928-a4ed-4dee-bebe-85d79d857fb4/download/fy18_tss_summarized_results.csv",
                     "mediaType": "text/csv",
-                    "title": "FY18_TSS_Summarized_Results.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/260d9579-065a-4ce0-a79e-e780b9bf27bb/resource/319ba928-a4ed-4dee-bebe-85d79d857fb4/download/fy18_tss_summarized_results.csv"
+                    "title": "FY18_TSS_Summarized_Results.csv"
                 }
             ],
+            "identifier": "GSA-2021-05-24-05",
             "keyword": [
                 "Cleanliness",
                 "Happiness",
@@ -12371,25 +12361,14 @@
                 "satisfaction",
                 "tenant"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-05-25T17:00:57.825Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FY17 Tenant Satisfaction Survey (TSS) Individual Responses with Comments",
-            "description": "A CSV export of Tenant Satisfaction Survey individual responses with comments, file does not contain PII",
-            "modified": "2021-05-25T16:58:44.930Z",
-            "accessLevel": "non-public",
-            "identifier": "GSA-2021-05-24-02",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "The POC for this TSS report has stated that it is Restricted.",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Government-wide Policy",
@@ -12398,19 +12377,30 @@
                     "name": "Office of Government-wide Policy"
                 }
             },
+            "rights": "The POC for this report has stated this report is Restricted.",
+            "title": "FY18 Tenant Satisfaction Survey (TSS) Summarized Results"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Aaron Eisenbarth",
                 "hasEmail": "mailto:aaron.eisenbarth@gsa.gov"
             },
+            "description": "A CSV export of Tenant Satisfaction Survey individual responses with comments, file does not contain PII",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/0bb971ac-faf6-4144-9e77-f67ee245f59e/resource/6695811f-23bb-4f01-8e2a-8d22bc5f21a2/download/fy17_tss_individual_results_with_comments.csv",
                     "mediaType": "text/csv",
-                    "title": "FY17_TSS_Individual_Results_with_Comments.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/0bb971ac-faf6-4144-9e77-f67ee245f59e/resource/6695811f-23bb-4f01-8e2a-8d22bc5f21a2/download/fy17_tss_individual_results_with_comments.csv"
+                    "title": "FY17_TSS_Individual_Results_with_Comments.csv"
                 }
             ],
+            "identifier": "GSA-2021-05-24-02",
             "keyword": [
                 "Cleanliness",
                 "Happiness",
@@ -12427,25 +12417,14 @@
                 "survey results",
                 "tenant"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-05-25T16:58:44.930Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FY19 Tenant Satisfaction Survey (TSS) Individual Responses with Comments",
-            "description": "A CSV export of Tenant Satisfaction Survey individual responses with comments, file does not contain PII.",
-            "modified": "2021-05-25T17:00:31.848Z",
-            "accessLevel": "non-public",
-            "identifier": "GSA-2021-05-24-06",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "The POC for this report has stated it is Restricted.",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Government-wide Policy",
@@ -12454,19 +12433,30 @@
                     "name": "Office of Government-wide Policy"
                 }
             },
+            "rights": "The POC for this TSS report has stated that it is Restricted.",
+            "title": "FY17 Tenant Satisfaction Survey (TSS) Individual Responses with Comments"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Aaron Eisenbarth",
                 "hasEmail": "mailto:aaron.eisenbarth@gsa.gov"
             },
+            "description": "A CSV export of Tenant Satisfaction Survey individual responses with comments, file does not contain PII.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/864dc07d-de7c-484f-b859-9839bf62c233/resource/9b194713-3b73-4f76-b9cb-226a5792ef3f/download/fy19_tss_individual_results_with_comments.csv",
                     "mediaType": "text/csv",
-                    "title": "FY19_TSS_Individual_Results_with_Comments.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/864dc07d-de7c-484f-b859-9839bf62c233/resource/9b194713-3b73-4f76-b9cb-226a5792ef3f/download/fy19_tss_individual_results_with_comments.csv"
+                    "title": "FY19_TSS_Individual_Results_with_Comments.csv"
                 }
             ],
+            "identifier": "GSA-2021-05-24-06",
             "keyword": [
                 "Cleanliness",
                 "Happiness",
@@ -12483,25 +12473,14 @@
                 "survey results",
                 "tenant"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-05-25T17:00:31.848Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FY17 Tenant Satisfaction Survey (TSS) Summarized Results",
-            "description": "A CSV export of Tenant Satisfaction Survey results summarized at the building and individual question level.",
-            "modified": "2021-05-25T17:02:44.996Z",
-            "accessLevel": "non-public",
-            "identifier": "GSA-2021-05-24-03",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "The POC stated that this TSS report is Restricted.",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Government-wide Policy",
@@ -12510,19 +12489,30 @@
                     "name": "Office of Government-wide Policy"
                 }
             },
+            "rights": "The POC for this report has stated it is Restricted.",
+            "title": "FY19 Tenant Satisfaction Survey (TSS) Individual Responses with Comments"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Aaron Eisenbarth",
                 "hasEmail": "mailto:aaron.eisenbarth@gsa.gov"
             },
+            "description": "A CSV export of Tenant Satisfaction Survey results summarized at the building and individual question level.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/30ce10f0-28ce-443b-a509-f4844e208609/resource/729fa561-e91d-4166-932f-2c57ed516521/download/fy17_tss_summarized_results.csv",
                     "mediaType": "text/csv",
-                    "title": "FY17_TSS_Summarized_Results.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/30ce10f0-28ce-443b-a509-f4844e208609/resource/729fa561-e91d-4166-932f-2c57ed516521/download/fy17_tss_summarized_results.csv"
+                    "title": "FY17_TSS_Summarized_Results.csv"
                 }
             ],
+            "identifier": "GSA-2021-05-24-03",
             "keyword": [
                 "Cleanliness",
                 "Condition",
@@ -12534,25 +12524,14 @@
                 "building",
                 "tenant"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-05-25T17:02:44.996Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FY18 Tenant Satisfaction Survey Individual Responses with Comments",
-            "description": "A CSV export of Tenant Satisfaction Survey (TSS) individual responses with comments, file does not contain PII.",
-            "modified": "2021-05-25T17:01:43.444Z",
-            "accessLevel": "non-public",
-            "identifier": "GSA-2021-05-24-04",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "The POC for this report has stated this is Restricted.",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Government-wide Policy",
@@ -12561,19 +12540,30 @@
                     "name": "Office of Government-wide Policy"
                 }
             },
+            "rights": "The POC stated that this TSS report is Restricted.",
+            "title": "FY17 Tenant Satisfaction Survey (TSS) Summarized Results"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Aaron Eisenbarth",
                 "hasEmail": "mailto:aaron.eisenbarth@gsa.gov"
             },
+            "description": "A CSV export of Tenant Satisfaction Survey (TSS) individual responses with comments, file does not contain PII.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/70e9e4ea-6244-4447-aa2c-3516a9267de7/resource/11ef082d-034a-432a-9a23-fdd35fe51790/download/fy18_tss_individual_results_with_comments.csv",
                     "mediaType": "text/csv",
-                    "title": "FY18_TSS_Individual_Results_with_Comments.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/70e9e4ea-6244-4447-aa2c-3516a9267de7/resource/11ef082d-034a-432a-9a23-fdd35fe51790/download/fy18_tss_individual_results_with_comments.csv"
+                    "title": "FY18_TSS_Individual_Results_with_Comments.csv"
                 }
             ],
+            "identifier": "GSA-2021-05-24-04",
             "keyword": [
                 "Cleanliness",
                 "Happiness",
@@ -12589,25 +12579,14 @@
                 "satisfaction",
                 "survey results"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-05-25T17:01:43.444Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FY19 Tenant Satisfaction Survey (TSS) Summarized Results",
-            "description": "A CSV export of Tenant Satisfaction Survey (TSS) results summarized at the building and individual question level.",
-            "modified": "2021-05-25T17:00:04.522Z",
-            "accessLevel": "non-public",
-            "identifier": "GSA-2021-05-24-07",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "The POC for this report has stated it is Restricted.",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Government-wide Policy",
@@ -12616,19 +12595,30 @@
                     "name": "Office of Government-wide Policy"
                 }
             },
+            "rights": "The POC for this report has stated this is Restricted.",
+            "title": "FY18 Tenant Satisfaction Survey Individual Responses with Comments"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Aaron Eisenbarth",
                 "hasEmail": "mailto:aaron.eisenbarth@gsa.gov"
             },
+            "description": "A CSV export of Tenant Satisfaction Survey (TSS) results summarized at the building and individual question level.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/0bdbca3d-c492-4503-a445-a7738f975c18/resource/3b0fd369-7089-4f54-a24d-82228d7c5c2d/download/fy19_tss_summarized_results.csv",
                     "mediaType": "text/csv",
-                    "title": "FY19_TSS_Summarized_Results.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/0bdbca3d-c492-4503-a445-a7738f975c18/resource/3b0fd369-7089-4f54-a24d-82228d7c5c2d/download/fy19_tss_summarized_results.csv"
+                    "title": "FY19_TSS_Summarized_Results.csv"
                 }
             ],
+            "identifier": "GSA-2021-05-24-07",
             "keyword": [
                 "Cleanliness",
                 "Happiness",
@@ -12640,25 +12630,14 @@
                 "satisfaction",
                 "survey"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-05-25T17:00:04.522Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "TSS Individual Results with Comments Data Dictionary",
-            "description": "A Data Dictionary for the TSS Individual Reports with Comments reports.",
-            "modified": "2021-05-25T16:59:40.968Z",
-            "accessLevel": "non-public",
-            "identifier": "GSA-2021-05-24-08",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "The POC has stated this is Restricted.",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Government-wide Policy",
@@ -12667,19 +12646,30 @@
                     "name": "Office of Government-wide Policy"
                 }
             },
+            "rights": "The POC for this report has stated it is Restricted.",
+            "title": "FY19 Tenant Satisfaction Survey (TSS) Summarized Results"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Aaron Eisenbarth",
                 "hasEmail": "mailto:aaron.eisenbarth@gsa.gov"
             },
+            "description": "A Data Dictionary for the TSS Individual Reports with Comments reports.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/a6b94e32-983d-4370-8935-ab1de8d3ca23/resource/173d7ab1-db2e-4bf4-b746-1183989e01ba/download/tss-individual-results-with-comments-data-dictionary.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "TSS Individual Results with Comments Data Dictionary.xlsx",
-                    "downloadURL": "https://inventory.data.gov/dataset/a6b94e32-983d-4370-8935-ab1de8d3ca23/resource/173d7ab1-db2e-4bf4-b746-1183989e01ba/download/tss-individual-results-with-comments-data-dictionary.xlsx"
+                    "title": "TSS Individual Results with Comments Data Dictionary.xlsx"
                 }
             ],
+            "identifier": "GSA-2021-05-24-08",
             "keyword": [
                 "Cleanliness",
                 "Happiness",
@@ -12696,25 +12686,14 @@
                 "survey results",
                 "tenant"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-05-25T16:59:40.968Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "TSS Summarized Results Data Dictionary",
-            "description": "A Data Dictionary for the TSS Summarized Reports at the Building and Individual level reports.",
-            "modified": "2021-05-25T16:59:13.064Z",
-            "accessLevel": "non-public",
-            "identifier": "GSA-2021-05-24-09",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "The POC has stated this dataset is Restricted.",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Government-wide Policy",
@@ -12723,19 +12702,30 @@
                     "name": "Office of Government-wide Policy"
                 }
             },
+            "rights": "The POC has stated this is Restricted.",
+            "title": "TSS Individual Results with Comments Data Dictionary"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Aaron Eisenbarth",
                 "hasEmail": "mailto:aaron.eisenbarth@gsa.gov"
             },
+            "description": "A Data Dictionary for the TSS Summarized Reports at the Building and Individual level reports.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/d8fd8e8f-8eab-4d17-a527-940f54fbaf31/resource/ebe8bfa9-6381-4f43-a0db-e93e7d5d6bd4/download/tss-summarized-results-data-dictionary.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "TSS Summarized Results Data Dictionary.xlsx",
-                    "downloadURL": "https://inventory.data.gov/dataset/d8fd8e8f-8eab-4d17-a527-940f54fbaf31/resource/ebe8bfa9-6381-4f43-a0db-e93e7d5d6bd4/download/tss-summarized-results-data-dictionary.xlsx"
+                    "title": "TSS Summarized Results Data Dictionary.xlsx"
                 }
             ],
+            "identifier": "GSA-2021-05-24-09",
             "keyword": [
                 "Cleanliness",
                 "Happiness",
@@ -12748,48 +12738,52 @@
                 "satisfaction",
                 "tenant"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-05-25T16:59:13.064Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Government-wide Policy",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of Government-wide Policy"
+                }
+            },
+            "rights": "The POC has stated this dataset is Restricted.",
+            "title": "TSS Summarized Results Data Dictionary"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA Oct-Dec 2019, 1st Qtr US Bank",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2019-11-13",
             "accessLevel": "public",
-            "identifier": "GSA-2019-11-13-05",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "2019-1st Qtr (Oct-Dec) CBCA PC transactions_US Bank",
                     "description": "1st Quarter CBCA PC transactions October-December \r\n2019 US Bank",
-                    "downloadURL": "https://inventory.data.gov/dataset/d30e84dd-45e5-4020-8b70-007dfa57d7df/resource/0ddff4d4-d41d-4e76-97ba-361816ec08f0/download/2019-1st-qtr-oct-dec-cbca-pc-transactionsus-bank.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/d30e84dd-45e5-4020-8b70-007dfa57d7df/resource/0ddff4d4-d41d-4e76-97ba-361816ec08f0/download/2019-1st-qtr-oct-dec-cbca-pc-transactionsus-bank.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "2019-1st Qtr (Oct-Dec) CBCA PC transactions_US Bank"
                 }
             ],
+            "identifier": "GSA-2019-11-13-05",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Contract Board",
@@ -12800,51 +12794,51 @@
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
-            ],
-            "programCode": [
-                "023:010"
-            ],
             "language": [
                 "en-us"
             ],
-            "theme": [
-                "Card Services Program"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA July-Sept 2019, 4th Qtr US Bank",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2020-02-13",
-            "accessLevel": "public",
-            "identifier": "GSA-2019-11-13-01",
-            "dataQuality": true,
-            "issued": "2014-10-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
+            "modified": "2019-11-13",
+            "programCode": [
+                "023:010"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "General Services Administration"
             },
+            "rights": "N/A",
+            "theme": [
+                "Card Services Program"
+            ],
+            "title": "Purchase Card Transactions - CBCA Oct-Dec 2019, 1st Qtr US Bank"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "2019-4th Qtr (July-Sept)_CBCA PC Transactions US Bank",
                     "description": "4th Quarter CBCA PC Transactions US Bank July-Sept 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/a3152c25-6be2-4acd-a676-7cca57d7b518/resource/79ca678d-c345-4653-b3e6-78b0e85d215d/download/2019-4th-qtr-july-septcbca-pc-transactions-us-bank.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/a3152c25-6be2-4acd-a676-7cca57d7b518/resource/79ca678d-c345-4653-b3e6-78b0e85d215d/download/2019-4th-qtr-july-septcbca-pc-transactions-us-bank.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "2019-4th Qtr (July-Sept)_CBCA PC Transactions US Bank"
                 }
             ],
+            "identifier": "GSA-2019-11-13-01",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "August",
                 "BOCA",
@@ -12855,51 +12849,51 @@
                 "September",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-02-13",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA July-Sept 2019, 4th Qtr US Bank"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA Apr-Jun 2019, 3rd Qtr US Bank",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2020-02-13",
             "accessLevel": "public",
-            "identifier": "GSA-2019-11-13-02",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "2019-3rd Qtr (Apr-Jun) CBCA PC transactions US Bank",
                     "description": "3rd Quarter CBCA PC transactions Apr-Jun 2019 US Bank",
-                    "downloadURL": "https://inventory.data.gov/dataset/c1cb14ea-5e8c-44f4-b403-5e9a3cdfc5b1/resource/0fdc3072-1793-4a00-82ce-a897a660daaf/download/2019-3rd-qtr-apr-jun-cbca-pc-transactionsus-bank.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/c1cb14ea-5e8c-44f4-b403-5e9a3cdfc5b1/resource/0fdc3072-1793-4a00-82ce-a897a660daaf/download/2019-3rd-qtr-apr-jun-cbca-pc-transactionsus-bank.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "2019-3rd Qtr (Apr-Jun) CBCA PC transactions US Bank"
                 }
             ],
+            "identifier": "GSA-2019-11-13-02",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "April",
                 "BOCA",
@@ -12910,51 +12904,51 @@
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-02-13",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA Apr-Jun 2019, 3rd Qtr US Bank"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA Jan-Mar 2019, 2nd Qtr US Bank",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2020-02-13",
             "accessLevel": "public",
-            "identifier": "GSA-2019-11-13-03",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "2019-2nd Qtr (Jan-Mar) CBCA PC transactions US Bank",
                     "description": "2nd Quarter CBCA PC transactions January-March 2019",
-                    "downloadURL": "https://inventory.data.gov/dataset/da897366-ddba-4da6-b8b7-039d440ed55a/resource/2cf101b4-f8a6-4636-b642-10b16196abd9/download/2019-2nd-qtr-jan-mar-cbca-pc-transactionsus-bank.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/da897366-ddba-4da6-b8b7-039d440ed55a/resource/2cf101b4-f8a6-4636-b642-10b16196abd9/download/2019-2nd-qtr-jan-mar-cbca-pc-transactionsus-bank.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "2019-2nd Qtr (Jan-Mar) CBCA PC transactions US Bank"
                 }
             ],
+            "identifier": "GSA-2019-11-13-03",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Contract Board",
@@ -12965,51 +12959,51 @@
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-02-13",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA Jan-Mar 2019, 2nd Qtr US Bank"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Purchase Card Transactions - CBCA Oct-Dec 2019, 1st Qtr Citibank",
-            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
-            "modified": "2019-11-13",
             "accessLevel": "public",
-            "identifier": "GSA-2019-11-13-04",
-            "dataQuality": true,
-            "issued": "2014-10-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "N/A",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2016-01-06-1",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James G Parks",
                 "hasEmail": "mailto:greg.parks@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The GSA SmartPay\u00ae purchase card program provides cards to federal employees to make official government purchases. These are transactions made by the GSA Board of Contract Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "2019-1st Qtr (Oct-Dec) CBCA PC transactions_Citibank",
                     "description": "1st Quarter CBCA PC transactions Citibank",
-                    "downloadURL": "https://inventory.data.gov/dataset/678e1717-0dda-495f-b995-7c1a6b015744/resource/a7b8c8dc-e10d-45ba-a193-1e13e1f9cc0f/download/2019-1st-qtr-oct-dec-cbca-pc-transactionsctibank.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/678e1717-0dda-495f-b995-7c1a6b015744/resource/a7b8c8dc-e10d-45ba-a193-1e13e1f9cc0f/download/2019-1st-qtr-oct-dec-cbca-pc-transactionsctibank.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "2019-1st Qtr (Oct-Dec) CBCA PC transactions_Citibank"
                 }
             ],
+            "identifier": "GSA-2019-11-13-04",
+            "isPartOf": "GSA-2016-01-06-1",
+            "issued": "2014-10-01",
             "keyword": [
                 "BOCA",
                 "Contract Board",
@@ -13020,124 +13014,109 @@
                 "Purchase Card",
                 "Transactions"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-us"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-11-13",
             "programCode": [
                 "023:010"
             ],
-            "language": [
-                "en-us"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
+            "rights": "N/A",
             "theme": [
                 "Card Services Program"
-            ]
+            ],
+            "title": "Purchase Card Transactions - CBCA Oct-Dec 2019, 1st Qtr Citibank"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Networx Business Volume FY2019, 4th Qtr",
-            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
-            "modified": "2019-11-13",
             "accessLevel": "public",
-            "identifier": "GSA-2019-11-13-06",
-            "dataQuality": true,
-            "issued": "2015-11-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "General Services Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "GSA-2015-08-27",
+            "bureauCode": [
+                "023:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni L Holloway",
                 "hasEmail": "mailto:toni.holloway@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The dataset represents the Networx Universal and Enterprise business volume of each government agency that has ordered telecommunications services from the Networx Contact, by Fiscal Year, Contract, Contract Vehicle, Agency and Month for the Central and Direct billing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "xlsx",
-                    "title": "TotRevFY19_4thQtr",
                     "description": "4th Quarter Total Revenue FY19",
-                    "downloadURL": "https://inventory.data.gov/dataset/7e3391d0-fe71-4fa6-b427-4151c8fd4be6/resource/71a794d4-c577-4259-a54c-ab58b2798f41/download/totrevfy194thqtr.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/7e3391d0-fe71-4fa6-b427-4151c8fd4be6/resource/71a794d4-c577-4259-a54c-ab58b2798f41/download/totrevfy194thqtr.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TotRevFY19_4thQtr"
                 }
             ],
+            "identifier": "GSA-2019-11-13-06",
+            "isPartOf": "GSA-2015-08-27",
+            "issued": "2015-11-13",
             "keyword": [
                 "Contract",
                 "Networx Telecommunications",
                 "Telecommunications"
             ],
-            "bureauCode": [
-                "023:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-11-13",
             "programCode": [
                 "023:019"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "General Services Administration"
+            },
             "theme": [
                 "Telecommunications Services"
-            ]
+            ],
+            "title": "Networx Business Volume FY2019, 4th Qtr"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Category Management (CM) Plan Workbench",
-            "description": "This workbook is a series of tools for Departments to use for their planning of the next FY for Category Management purposes; contract shifting from Tier 0 to Managed tiers, etc.",
-            "modified": "2021-07-16T16:59:04.037Z",
             "accessLevel": "public",
-            "identifier": "GSA-2021-07-16-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Acquisition Service",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "General Services Administration"
-                }
-            },
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Dixon",
                 "hasEmail": "mailto:david.dixon@gsa.gov"
             },
+            "description": "This workbook is a series of tools for Departments to use for their planning of the next FY for Category Management purposes; contract shifting from Tier 0 to Managed tiers, etc.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://d2d.gsa.gov/report/government-wide-category-management-contract-management-and-operational-reporting-tools",
                     "format": "html",
-                    "title": "Category Management (CM) Plan Workbench",
-                    "downloadURL": "https://d2d.gsa.gov/report/government-wide-category-management-contract-management-and-operational-reporting-tools"
+                    "mediaType": "text/html",
+                    "title": "Category Management (CM) Plan Workbench"
                 }
             ],
+            "identifier": "GSA-2021-07-16-01",
             "keyword": [
                 "FPDS",
                 "FY Plan",
                 "Spend Under Management",
                 "obligation"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-07-16T16:59:04.037Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common and Defense Centric Spend Tables",
-            "description": "Top-level view of annual Obligation totals for Categories and Subcategories.  Also includes Small Business utilization.  The only GWCM Dashboard that includes all 19 Lv1 categories (the other dashboards only include common-spend categories).",
-            "modified": "2021-07-16T17:21:58.837Z",
-            "accessLevel": "public",
-            "identifier": "GSA-2021-07-16-02",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Acquisition Service",
@@ -13146,43 +13125,43 @@
                     "name": "General Services Administration"
                 }
             },
+            "rights": "true",
+            "title": "Category Management (CM) Plan Workbench"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
```

