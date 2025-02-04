# Change History for va.json (Part 5)

### Changes from 31606f9 to dd2190f (Part 5/7)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+                    "downloadURL": "https://www.data.va.gov/api/views/k42f-3ku6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/k42f-3ku6",
+            "issued": "2024-08-07",
+            "keyword": [
+                "compensation",
+                "county",
+                "disability",
+                "fy19",
+                "fy 19",
+                "fy2019",
+                "fy 2019"
+            ],
+            "landingPage": "https://www.data.va.gov/d/k42f-3ku6",
+            "language": [
+                "English"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-08-08",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Disability Compensation"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "FY 2019 Disability Compensation Recipients by County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.oprm.va.gov/foia/",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VA OM Open Data",
+                "hasEmail": "mailto:VAOMOpenData@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) fee schedule.  It provides information regarding the fee associated with processing/providing feedback in support of FOIA requests.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.oprm.va.gov/foia/",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-17",
             "issued": "2017-07-26",
-            "temporal": "2010-04-29T04:00:00Z/2016-01-01T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
             "keyword": [
                 "certification",
                 "cost",
@@ -55439,69 +55451,40 @@
                 "postage",
                 "va"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VA OM Open Data",
-                "hasEmail": "mailto:VAOMOpenData@va.gov"
-            },
+            "landingPage": "https://www.oprm.va.gov/foia/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-06-07",
+            "programCode": [
+                "029:080"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-OIT-ITIS-17",
-            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) fee schedule.  It provides information regarding the fee associated with processing/providing feedback in support of FOIA requests.</p>",
-            "title": "Freedom of Information Act (FOIA) Fee Schedule",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.oprm.va.gov/foia/",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2010-04-29T04:00:00Z/2016-01-01T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Freedom of Information Act (FOIA) Fee Schedule"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/k67m-gyvp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2023-03-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-21",
-            "keyword": [
-                "dic benefits",
-                "veterans",
-                "veterans surviving spouses and children"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alysia Blake",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/k67m-gyvp",
+            "dataQuality": true,
             "description": "All DIC Recipients by the Period of Service of the Veterans, FY2022. DIC is a tax-free monetary benefit generally payable to a surviving spouse, child, or parent of deceased Servicemembers or Veterans.",
-            "title": "All Dependency and Indemnity (DIC) Compensation Recipients by Veteran\u2019s Period of Service, FY2022",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55509,84 +55492,89 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/k67m-gyvp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k67m-gyvp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k67m-gyvp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/k67m-gyvp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k67m-gyvp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k67m-gyvp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/k67m-gyvp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k67m-gyvp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k67m-gyvp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/k67m-gyvp",
+            "issued": "2023-03-21",
+            "keyword": [
+                "dic benefits",
+                "veterans",
+                "veterans surviving spouses and children"
+            ],
+            "landingPage": "https://www.data.va.gov/d/k67m-gyvp",
             "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
-            "dataQuality": true
+            "modified": "2023-03-21",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "All Dependency and Indemnity (DIC) Compensation Recipients by Veteran\u2019s Period of Service, FY2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/k7bt-c9uj",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary District of Columbia FY2023",
+            "identifier": "https://www.data.va.gov/api/views/k7bt-c9uj",
             "issued": "2024-06-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
             "keyword": [
                 "district of columbia",
                 "fy2023",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/k7bt-c9uj",
+            "modified": "2024-07-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/k7bt-c9uj",
-            "description": "NCVAS State Summary District of Columbia FY2023",
-            "title": "NCVAS State Summary District of Columbia FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary District of Columbia FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/k7f9-dtm7",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2024-08-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vhancod@va.gov",
                 "hasEmail": "mailto:VHA National Center for Organization Development (NCOD)"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/k7f9-dtm7",
             "description": "",
-            "title": "AES-FEVS Percents Tables",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55594,33 +55582,32 @@
                     "mediaType": "application/pdf"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/k7f9-dtm7",
+            "issued": "2024-08-01",
+            "landingPage": "https://www.data.va.gov/d/k7f9-dtm7",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "AES-FEVS Percents Tables"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/k7w9-hb5k",
-            "issued": "2023-06-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-25",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alysia D. Blake",
                 "hasEmail": "mailto:alysia.blake@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/k7w9-hb5k",
             "description": "FY 2021 VA Personal Income data used to populate the NCVAS State summary visualizations created in FY2023.",
-            "title": "FY 2021_NCVAS Personal Income Data For State Summary Visuals",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55628,62 +55615,53 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/k7w9-hb5k/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k7w9-hb5k/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k7w9-hb5k/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/k7w9-hb5k/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k7w9-hb5k/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k7w9-hb5k/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/k7w9-hb5k/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k7w9-hb5k/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k7w9-hb5k/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/k7w9-hb5k",
+            "issued": "2023-06-13",
+            "landingPage": "https://www.data.va.gov/d/k7w9-hb5k",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-25",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2021_NCVAS Personal Income Data For State Summary Visuals"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/k8a2-inaa",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-03-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-05",
-            "keyword": [
-                "utilization",
-                "va benefits",
-                "va programs",
-                "va services",
-                "veteran benefits",
-                "veterans",
-                "veterans benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/k8a2-inaa",
             "description": "Percentage of Service-Connected Disabled Who Did and Did Not Use Health Care, by Race/Ethnicity. Data underlying the fourth figure of Part 3 of the FY2021 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Percentage of Service-Connected Disabled Veterans Who Used VA Health Care, by Race/Ethnicity, FY 2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55691,99 +55669,134 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/k8a2-inaa/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k8a2-inaa/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k8a2-inaa/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/k8a2-inaa/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k8a2-inaa/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k8a2-inaa/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/k8a2-inaa/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k8a2-inaa/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k8a2-inaa/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/k8a2-inaa",
+            "issued": "2022-03-18",
+            "keyword": [
+                "utilization",
+                "va benefits",
+                "va programs",
+                "va services",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/k8a2-inaa",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-01-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Percentage of Service-Connected Disabled Veterans Who Used VA Health Care, by Race/Ethnicity, FY 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:40"
             ],
-            "landingPage": "https://www.data.va.gov/d/k8iy-vfmv",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-07",
-            "keyword": [
-                "delaware",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/k8iy-vfmv",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Delaware",
+            "identifier": "https://www.data.va.gov/api/views/k8iy-vfmv",
+            "issued": "2021-08-26",
+            "keyword": [
+                "delaware",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/k8iy-vfmv",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-07",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_Delaware"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/k94w-kssb",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Maine FY2023",
+            "identifier": "https://www.data.va.gov/api/views/k94w-kssb",
             "issued": "2024-06-07",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
             "keyword": [
                 "fy2024",
                 "maine",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/k94w-kssb",
+            "modified": "2024-07-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/k94w-kssb",
-            "description": "NCVAS State Summary Maine FY2023",
-            "title": "NCVAS State Summary Maine FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Maine FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/Expenditures.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Andrew Bickel",
+                "hasEmail": "mailto:andrew.bickel@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/VETDATA/docs/GDX/GDX_FY12_V1.xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "xls"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-011",
             "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -55797,69 +55810,37 @@
                 "insurance",
                 "medical care"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Andrew Bickel",
-                "hasEmail": "mailto:andrew.bickel@va.gov"
-            },
+            "landingPage": "https://www.va.gov/VETDATA/Expenditures.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-OEI-OEI-011",
-            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY2012",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/VETDATA/docs/GDX/GDX_FY12_V1.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "xls"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "Expenditures"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geographic Distribution of VA Expenditures FY2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/k9dc-9an8",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-09",
-            "keyword": [
-                "veteran population",
-                "veterans",
-                "vetpop",
-                "vetpop2023"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:VANCVAS@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/k9dc-9an8",
             "description": "VetPop2023 projection of living Veterans by gender and branch of service at the national level. \n\nNote: Rounding to the nearest 1,000 is always appropriate for VetPop estimates.",
-            "title": "VetPop2023 National Branch of Service Data, 4L",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55867,57 +55848,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/k9dc-9an8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k9dc-9an8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k9dc-9an8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/k9dc-9an8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k9dc-9an8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k9dc-9an8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/k9dc-9an8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k9dc-9an8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k9dc-9an8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/k9dc-9an8",
+            "issued": "2024-09-05",
+            "keyword": [
+                "veteran population",
+                "veterans",
+                "vetpop",
+                "vetpop2023"
+            ],
+            "landingPage": "https://www.data.va.gov/d/k9dc-9an8",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-09-09",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2023 National Branch of Service Data, 4L"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/k9f7-ngmg",
-            "bureauCode": [
-                "029:25"
-            ],
-            "issued": "2019-03-21",
             "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 116"
+            "accessLevel": "public",
+            "bureauCode": [
+                "029:25"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/k9f7-ngmg",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAMS to provide, through purchase and/or fabrication, prosthetic and related appliances, equipment and services to eligible veterans so that they may live and work as productive citizens. Veterans eligible for prosthetic services are service-connected veterans seeking care for a service-connected disability; veterans with compensable service-connected disabilities generally rated 10 percent or more; former prisoners of war, veterans discharged or released from active military service for a disability that was incurred or aggravated in the line of duty, and veterans who are in receipt of Section 1151 benefits; veterans who are in receipt of increased pension based on a need of regular aid and attendance or by reason of being permanently housebound; veterans who have annual income and net worth below the \"means test\" threshold; all other veterans who are not required to pay a copayment for their care, i.e., veterans of the Mexican border period and World War I, compensated zero (0) percent service-connected veterans who are receiving statutory awards, veterans exposed to a toxic substance, radiation or environmental hazard (limited to certain disabilities); and veterans who must pay a copayment for their care. Ineligible veterans are nonservice-connected veterans residing or sojourning in foreign lands.</p>",
-            "title": "USA SPENDING EDUCATION CH31 B116 VETERANS PROSTHETIC APPLIANCES NOV2018",
-            "isPartOf": "5760c6c5-d531-4dc3-9e99-4418034dbb16",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55925,58 +55909,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/k9f7-ngmg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k9f7-ngmg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k9f7-ngmg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/k9f7-ngmg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k9f7-ngmg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k9f7-ngmg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/k9f7-ngmg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k9f7-ngmg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k9f7-ngmg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/k9f7-ngmg",
+            "isPartOf": "5760c6c5-d531-4dc3-9e99-4418034dbb16",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 116"
+            ],
+            "landingPage": "https://www.data.va.gov/d/k9f7-ngmg",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "USA SPENDING EDUCATION CH31 B116 VETERANS PROSTHETIC APPLIANCES NOV2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/k9gy-dq9q",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "0152eb6c-27c6-4f0e-a854-16366260d0b8",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Vermont FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55984,51 +55968,44 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "0152eb6c-27c6-4f0e-a854-16366260d0b8",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/k9gy-dq9q",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data",
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "State Summary Vermont FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/k9i5-f2ec",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-11-30",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-30",
-            "keyword": [
-                "2021",
-                "compensation",
-                "compensation and pension",
-                "county",
-                "disability",
-                "disability compensation",
-                "fy2021",
-                "fy 2021",
-                "fy21",
-                "fy 21"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mike Schwaber",
                 "hasEmail": "mailto:\tvancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/k9i5-f2ec",
+            "dataQuality": true,
             "description": "This report provides county-level estimates of the number of Veterans who received VA Disability Compensation benefits during fiscal year 2021. It includes the Veterans\u2019 total service-connected disability (SCD) rating, age group, and gender. Blank values represent small cell counts that have been suppressed to protect the identity of Veterans. In the \"Total: Disability Compensation Recipients\" column, each blank cell represents less than 10 Veterans. Some categories may not sum to the total due to missing information (e.g., age, gender, etc.).\n\nSource: Department of Veterans Affairs, Office of Enterprise Integration, United States Veterans Eligibility Trends & Statistics (USVETS) 2021 and Veterans Benefits Administration VETSNET FY 2021 compensation data.\n\nPrepared by National Center for Veterans Analysis & Statistics, www.va.gov/vetdata.",
-            "title": "FY 2021 Disability Compensation Recipients by County",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56036,104 +56013,111 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/k9i5-f2ec/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k9i5-f2ec/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k9i5-f2ec/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/k9i5-f2ec/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k9i5-f2ec/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k9i5-f2ec/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/k9i5-f2ec/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k9i5-f2ec/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k9i5-f2ec/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
+            "identifier": "https://www.data.va.gov/api/views/k9i5-f2ec",
+            "issued": "2022-11-30",
+            "keyword": [
+                "2021",
+                "compensation",
+                "compensation and pension",
+                "county",
+                "disability",
+                "disability compensation",
+                "fy2021",
+                "fy 2021",
+                "fy21",
+                "fy 21"
+            ],
+            "landingPage": "https://www.data.va.gov/d/k9i5-f2ec",
             "language": [
                 "English"
-            ]
+            ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
+            "modified": "2022-11-30",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2021 Disability Compensation Recipients by County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/kbqi-8jyt",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Dusca Fichtel",
+                "hasEmail": "mailto:Dusca.Fichtel@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Face Amount of New Life Insurance Policies Issued- February 2013</p>",
+            "identifier": "VA-VBA-USASPENDING022014-040",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-02-01T05:00:00Z/2013-02-28T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 030",
                 "direct payment to veterans",
                 "insurance service",
                 "usa spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Dusca Fichtel",
-                "hasEmail": "mailto:Dusca.Fichtel@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/kbqi-8jyt",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING022014-040",
-            "description": "<p>USA Spending- Face Amount of New Life Insurance Policies Issued- February 2013</p>",
-            "title": "USA Spending file- Direct Payments for Veterans-Insurance -  CFDA 64.031",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2013-02-01T05:00:00Z/2013-02-28T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- Direct Payments for Veterans-Insurance -  CFDA 64.031"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/kcix-bb4m",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-09",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "5063f800-897b-4c94-bbec-1a2f27129efb",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Delaware FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56141,42 +56125,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "5063f800-897b-4c94-bbec-1a2f27129efb",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/kcix-bb4m",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary Delaware FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "fy2012 benefits",
-                "fy2012 vba",
-                "vba",
-                "vba benefits",
-                "vba benefits by state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-092",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Indiana-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56184,44 +56164,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-092",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy2012 benefits",
+                "fy2012 vba",
+                "vba",
+                "vba benefits",
+                "vba benefits by state"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR 2012"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Indiana-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/kei7-und6",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "7a2a3274-25c8-40e8-b589-c62a8bc3a21d",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary New Jersey FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56229,44 +56213,43 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "7a2a3274-25c8-40e8-b589-c62a8bc3a21d",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/kei7-und6",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data",
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "State Summary New Jersey FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/key6-qq4a",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "history",
-                "military"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Trisha Dang",
                 "hasEmail": "mailto:trisha.dang@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-ORCH-14",
+            "dataQuality": true,
             "description": "<p>The VIERS Military History service provides Veteran military history information that is consolidated across multiple data sources. This consolidated data is provided as part of the VRM initiative to improve the speed, accuracy and efficiency with which information is exchanged between Veterans and VA. This information is exposed to the VIERS Consumers via a SOAP based web service. It queries the VA/DoD Identity Repository (VADIR) and Corporate Database (CorpDB) repositories to retrieves electronic copies of military service information including periods of service, periods of captivity, and military pay. The VRM VIERS Military History Service also provides the capability to update the VA data repositories with unverified periods of service and unverified periods of captivity. Service provides a view of all military history to date(historical, current, retirement, Line of Duty/WII) for a partiular person such as branch, entry dates, separation dates, discharge characters. Provide definitive view of Veterans Military Service Information- Read access to veteran military service information (electronic DD-214/215)- Current member DoD affiliation status and information (Active duty, Guard/Reserve, Retired, Dependent)- DoD Eligibility and Entitlement (Insurance, Education)- DFAS Military Payments (severance, separation, retirement)- Supports submission by veterans of supplemental evidence of service (Vietnam Era)- Medals, awards</p>",
-            "title": "VIERS Military History Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56275,42 +56258,42 @@
                     "title": "VIERS Military History Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-ORCH-14",
+            "issued": "2017-11-17",
+            "keyword": [
+                "history",
+                "military"
+            ],
+            "landingPage": "https://www.data.va.gov/d/key6-qq4a",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "VIERS Military History Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/FUND/VA_Franchise_Fund_Annual_Reports.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
-            "keyword": [
-                "annual report",
-                "franchise fund",
-                "fy 2008"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OM Open Data",
                 "hasEmail": "mailto:VAOMOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-037",
+            "dataQuality": true,
             "description": "<p>Franchise Fund FY 2008 Annual Report</p>",
-            "title": "Franchise Fund FY 2008 Annual Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56319,45 +56302,46 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-037",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "franchise fund",
+                "fy 2008"
+            ],
+            "landingPage": "https://www.va.gov/FUND/VA_Franchise_Fund_Annual_Reports.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-07",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Franchise Fund FY 2008 Annual Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/pocketcard/index.asp",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "pocket card",
-                "statistics",
-                "stats at a glance"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS Mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-229",
+            "dataQuality": true,
             "description": "<p>NCVAS Pocket Cards are a compilation of facts related to the count of Veterans receiving Department of Veterans Affairs (VA) benefits and health care utilization.</p>",
-            "title": "VA Benefits & Health Care Utilization FY17 (Q1)",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56366,46 +56350,46 @@
                     "title": "Pocket Card \u2013 FY17 (Q1)"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-229",
+            "issued": "2017-07-26",
+            "keyword": [
+                "pocket card",
+                "statistics",
+                "stats at a glance"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/pocketcard/index.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Veteran Benefits",
                 "Veteran Utilization",
                 "Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Benefits & Health Care Utilization FY17 (Q1)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/kh46-typa",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 104"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/kh46-typa",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to assist wartime veterans in need whose non-service- connected disabilities are permanent and total preventing them from following a substantially gainful occupation. A Veteran who meets the wartime service requirements is potential eligible if he/she is: \u2022 permanently and totally disabled for reasons not necessarily due to service, \u2022 age 65 or older, or \u2022 is presumed to be totally and permanently disabled for pension purposes because: o he/she is a patient in a nursing home for long-term care due to a disability, or o being disabled, as determined by the Commissioner of Social Security (SS) for purposes of any benefits administered by the Commissioner, such as SS disability benefits or Supplemental Security Income. Income restrictions are prescribed in 38 U.S.C. 1521. Pension is not payable to those whose estates are so large that it is reasonable they use the estate for maintenance. A Veteran meets wartime service requirements if he/she served: \u2022 a total of 90 days or more during one or more periods of war; \u2022 90 or more consecutive days that began or ended during a period of war; or \u2022 for any length of time during a period of war if he/she was discharged or released for a service-connected disability. Veterans entering service after September 7, 1980, must also meet the minimum active duty requirement of 24 months of continuous service or the full period to which the Veteran was called to active duty. (38 U.S.C.5303(A)).</p>",
-            "title": "USA SPENDING C&P B104 PENSION FOR NON-SERVICE CONNECTED FOR VETERANS DEC2018",
-            "isPartOf": "279f1b11-a128-4135-825a-5530f04cb050",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56413,61 +56397,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/kh46-typa/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/kh46-typa/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/kh46-typa/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/kh46-typa/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/kh46-typa/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/kh46-typa/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/kh46-typa/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/kh46-typa/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/kh46-typa/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/kh46-typa",
+            "isPartOf": "279f1b11-a128-4135-825a-5530f04cb050",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 104"
+            ],
+            "landingPage": "https://www.data.va.gov/d/kh46-typa",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING C&P B104 PENSION FOR NON-SERVICE CONNECTED FOR VETERANS DEC2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/kieg-d5az",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2019-09-19",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-19",
-            "keyword": [
-                "ethnicity",
-                "healthcare"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Office of Health Equity",
                 "hasEmail": "mailto:healthequity@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/kieg-d5az",
             "description": "Summary level data from the National Veteran Health Equity Report - FY2013, filtered by race & ethnicity.",
-            "title": "VA-OHE-NVHER-FY13-Sociodemographic-Race/Ethnicity",
-            "programCode": [
-                "029:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56475,57 +56458,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/kieg-d5az/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/kieg-d5az/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/kieg-d5az/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/kieg-d5az/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/kieg-d5az/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/kieg-d5az/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/kieg-d5az/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/kieg-d5az/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/kieg-d5az/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/kieg-d5az",
+            "issued": "2019-09-19",
+            "keyword": [
+                "ethnicity",
+                "healthcare"
+            ],
+            "landingPage": "https://www.data.va.gov/d/kieg-d5az",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-07-19",
+            "programCode": [
+                "029:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VA-OHE-NVHER-FY13-Sociodemographic-Race/Ethnicity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/kiif-4bin",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-09",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "972bc755-14df-41d7-ba87-5ad20c9275db",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Guam FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56533,61 +56517,90 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "972bc755-14df-41d7-ba87-5ad20c9275db",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/kiif-4bin",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary Guam FY2016"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/kjd3-i5eq",
-            "issued": "2024-03-27",
             "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rebecca Matteo",
                 "hasEmail": "mailto:no-reply@ptsd-va.data.socrata.com"
             },
+            "description": "The PTSD Repository allows researchers to quickly identify relevant PTSD treatment clinical trials and download data in a variety of formats for the purpose of conducting systematic reviews and meta-analyses.",
             "identifier": "https://www.data.va.gov/api/views/kjd3-i5eq",
+            "issued": "2024-03-27",
+            "landingPage": "https://www.data.va.gov/d/kjd3-i5eq",
+            "modified": "2024-12-18",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "The PTSD Repository allows researchers to quickly identify relevant PTSD treatment clinical trials and download data in a variety of formats for the purpose of conducting systematic reviews and meta-analyses.",
             "title": "For Researchers: About the PTSD Repository"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/kkh2-eymp",
-            "issued": "2023-01-30",
             "@type": "dcat:Dataset",
-            "modified": "2023-04-11",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:VANCVAS@VA.GOV"
             },
+            "description": "Data story examining demographic and socioeconomic characteristics of the Veteran population residing in rural communities compared to those residing in urban communities for FY2021-2023.",
+            "identifier": "https://www.data.va.gov/api/views/kkh2-eymp",
+            "issued": "2023-01-30",
             "keyword": [
                 "rural",
                 "urban",
                 "veterans"
             ],
-            "identifier": "https://www.data.va.gov/api/views/kkh2-eymp",
+            "landingPage": "https://www.data.va.gov/d/kkh2-eymp",
+            "modified": "2023-04-11",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "Data story examining demographic and socioeconomic characteristics of the Veteran population residing in rural communities compared to those residing in urban communities for FY2021-2023.",
             "title": "Rural Veterans: FY2021-2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/kkp2-6v99",
             "bureauCode": [
                 "029:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lighthouse Support",
+                "hasEmail": "mailto:api@va.gov"
+            },
+            "description": "Look up VA forms and check for new versions. Our goal is to make it easier to keep up with the ever-changing landscape of VA forms. This API indexes data sourced from VA.gov, creating unique hashes for each version of a form and allowing quick lookup. The documentation is hosted by Lighthouse, a Veteran-centered API platform for securely accessing VA data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Look up VA forms and check for new versions. Our goal is to make it easier to keep up with the ever-changing landscape of VA forms. This API indexes data sourced from VA.gov, creating unique hashes for each version of a form and allowing quick lookup. The documentation is hosted by Lighthouse, a Veteran-centered API platform for securely accessing VA data.",
+                    "downloadURL": "https://developer.va.gov/explore/vaForms/docs/vaForms?version=current",
+                    "mediaType": "text/html",
+                    "title": "VA Forms API"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/kkp2-6v99",
             "issued": "2021-01-22",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-22",
             "keyword": [
                 "api",
                 "api documentation",
@@ -56595,42 +56608,34 @@
                 "lighthouse",
                 "open data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lighthouse Support",
-                "hasEmail": "mailto:api@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/kkp2-6v99",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-01-22",
+            "programCode": [
+                "029:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/kkp2-6v99",
-            "description": "Look up VA forms and check for new versions. Our goal is to make it easier to keep up with the ever-changing landscape of VA forms. This API indexes data sourced from VA.gov, creating unique hashes for each version of a form and allowing quick lookup. The documentation is hosted by Lighthouse, a Veteran-centered API platform for securely accessing VA data.",
-            "title": "VA Forms API",
-            "programCode": [
-                "029:000"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://developer.va.gov/explore/vaForms/docs/vaForms?version=current",
-                    "description": "Look up VA forms and check for new versions. Our goal is to make it easier to keep up with the ever-changing landscape of VA forms. This API indexes data sourced from VA.gov, creating unique hashes for each version of a form and allowing quick lookup. The documentation is hosted by Lighthouse, a Veteran-centered API platform for securely accessing VA data.",
-                    "@type": "dcat:Distribution",
             "title": "VA Forms API"
-                }
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Elwell",
+                "hasEmail": "mailto:thomas.elwell@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Fact sheet to guide Service Members on the benefits available to them.</p>",
+            "identifier": "VA-VBA-MEDIAPUB-002",
+            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
             "issued": "2017-07-26",
-            "temporal": "2008-10-30T04:00:00Z/2008-10-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
             "keyword": [
                 "benefits fact sheet",
                 "benefits to service members",
@@ -56638,114 +56643,93 @@
                 "va benefits",
                 "va fact sheet"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Elwell",
-                "hasEmail": "mailto:thomas.elwell@va.gov"
-            },
+            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-08",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-MEDIAPUB-002",
-            "description": "<p>Fact sheet to guide Service Members on the benefits available to them.</p>",
-            "title": "VBA Benefits Fact Sheet- VA Benefits for Service Members",
-            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2008-10-30T04:00:00Z/2008-10-30T04:00:00Z",
             "theme": [
                 "Veterans Benefits- Fact Sheets"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VBA Benefits Fact Sheet- VA Benefits for Service Members"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/km97-qdpp",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-21",
-            "keyword": [
-                "nebraska",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/km97-qdpp",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Nebraska",
+            "identifier": "https://www.data.va.gov/api/views/km97-qdpp",
+            "issued": "2021-08-26",
+            "keyword": [
+                "nebraska",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/km97-qdpp",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-21",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_Nebraska"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/kndj-bxzs",
-            "issued": "2023-06-24",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Hawaii FY2021",
+            "identifier": "https://www.data.va.gov/api/views/kndj-bxzs",
+            "issued": "2023-06-24",
             "keyword": [
                 "fy2021 data",
                 "hawaii",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/kndj-bxzs",
+            "landingPage": "https://www.data.va.gov/d/kndj-bxzs",
+            "modified": "2024-06-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Hawaii FY2021",
             "title": "NCVAS State Summary Hawaii FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/budget/products.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2015-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "budget",
-                "fy2015"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OM Open Data",
                 "hasEmail": "mailto:VAOMOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-100",
+            "dataQuality": true,
             "description": "<p>FY 2015 Budget Submission Volume IV: Construction, Long Range Capital Plan and Appendix</p>",
-            "title": "FY 2015 Budget Submission Volume IV",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56754,44 +56738,43 @@
                     "title": "FY 2015 Budget Submission"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-100",
+            "issued": "2017-07-26",
+            "keyword": [
+                "budget",
+                "fy2015"
+            ],
+            "landingPage": "https://www.va.gov/budget/products.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-10",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-10-01T04:00:00Z/2015-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2015 Budget Submission Volume IV"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/OGC/opinions/2014PrecedentOpinions.asp",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "ogc",
-                "opinion"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OGC Law Library",
                 "hasEmail": "mailto:OGCLawLibrary@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OGC-006",
             "description": "<p>Applicability of the Veterans Claims Assistance Act of 2000 to Decisions Concerning Benefits Administered by the National Cemetery Administration</p>",
-            "title": "OGC Precedent Opinion 2-2014",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56800,68 +56783,69 @@
                     "title": "VAOGCPREC 2-2014"
                 }
             ],
+            "identifier": "VA-OGC-006",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion"
+            ],
+            "landingPage": "https://www.va.gov/OGC/opinions/2014PrecedentOpinions.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:083"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OGC Precedent Opinion 2-2014"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ktyp-qycd",
-            "issued": "2023-07-13",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-13",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Montana FY2021",
+            "identifier": "https://www.data.va.gov/api/views/ktyp-qycd",
+            "issued": "2023-07-13",
             "keyword": [
                 "fy2021 data",
                 "montana",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/ktyp-qycd",
+            "landingPage": "https://www.data.va.gov/d/ktyp-qycd",
+            "modified": "2024-06-13",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Montana FY2021",
             "title": "NCVAS State Summary Montana FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/kv29-iep7",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "02f05020-f256-45a0-8067-c7840f083a26",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Oregon FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56869,39 +56853,42 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "02f05020-f256-45a0-8067-c7840f083a26",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/kv29-iep7",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data",
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "State Summary Oregon FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/kvkr-fsfv",
-            "issued": "2022-10-24",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-24",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/kvkr-fsfv",
             "description": "Honor Flights Program Statistics by Period of Service, 2017-2021",
-            "title": "Honor Flights Program Statistics, 2017-2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56909,57 +56896,53 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/kvkr-fsfv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/kvkr-fsfv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/kvkr-fsfv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/kvkr-fsfv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/kvkr-fsfv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/kvkr-fsfv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/kvkr-fsfv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/kvkr-fsfv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/kvkr-fsfv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/kvkr-fsfv",
+            "issued": "2022-10-24",
+            "landingPage": "https://www.data.va.gov/d/kvkr-fsfv",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-10-24",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Honor Flights Program Statistics, 2017-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/kwvt-2swh",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "gi bill benefit claims",
-                "recovery act"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rodney Emery",
                 "hasEmail": "mailto:Rodney.Emery@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OIT-OIT-055",
             "description": "<p>Long Term Solution supports the Secretary\u2019s FY 2010-2014Strategic Plan in creating new technology systems - through an automated IT platform as a means to efficiently and accurately process Post-911 GI Bill benefit claims</p>",
-            "title": "Recovery Act Program-Specific Plan",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56968,42 +56951,43 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OIT-OIT-055",
+            "issued": "2017-07-26",
+            "keyword": [
+                "gi bill benefit claims",
+                "recovery act"
+            ],
+            "landingPage": "https://www.data.va.gov/d/kwvt-2swh",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:080"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "Recovery Act Program-Specific Plan"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/budget/products.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2010-10-01T04:00:00Z/2011-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "budget",
-                "fy2011"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OM Open Data",
                 "hasEmail": "mailto:VAOMOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-028",
+            "dataQuality": true,
             "description": "<p>FY2011 VA Budget Submission.</p>",
-            "title": "FY2011 VA Budget Submission",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57012,86 +56996,86 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-028",
+            "issued": "2017-07-26",
+            "keyword": [
+                "budget",
+                "fy2011"
+            ],
+            "landingPage": "https://www.va.gov/budget/products.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-10",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2010-10-01T04:00:00Z/2011-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY2011 VA Budget Submission"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/vocrehab/jobs_for_veterans.asp",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2014-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
-            "keyword": [
-                "civilian career",
-                "vba benefits",
-                "vre benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INFO-015",
+            "dataQuality": true,
             "description": "<p>The tools which can help Veterans to get prepared for the transition to  civilian career.</p>",
-            "title": "Veteran Employment Resources/ Tools ( VRE)",
+            "identifier": "VA-VBA-INFO-015",
             "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "civilian career",
+                "vba benefits",
+                "vre benefits"
+            ],
+            "landingPage": "https://www.benefits.va.gov/vocrehab/jobs_for_veterans.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-08",
             "programCode": [
                 "029:003"
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-10-01T04:00:00Z/2014-12-30T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veteran Employment Resources/ Tools ( VRE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/kxsv-9qcb",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 109"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/kxsv-9qcb",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to compensate veterans for disabilities incurred or aggravated during military service according to the average impairment in earning capacity such disability would cause in civilian occupations. Persons who have suffered disabilities resulting from service in the Armed Forces of the United States. The disability must have been incurred or aggravated by service in the line of duty. Separation from service must have been under other than dishonorable conditions for the period in which the disability was incurred or aggravated.</p>",
-            "title": "USA SPENDING C&P B109 VETERANS COMPENSATION FOR SERVICE-CONNECTED DISABILITY OCT2018",
-            "isPartOf": "6013cae5-a8c2-47ff-9c90-9cbdba7bda63",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57099,62 +57083,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/kxsv-9qcb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/kxsv-9qcb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/kxsv-9qcb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/kxsv-9qcb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/kxsv-9qcb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/kxsv-9qcb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/kxsv-9qcb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/kxsv-9qcb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/kxsv-9qcb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/kxsv-9qcb",
+            "isPartOf": "6013cae5-a8c2-47ff-9c90-9cbdba7bda63",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 109"
+            ],
+            "landingPage": "https://www.data.va.gov/d/kxsv-9qcb",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING C&P B109 VETERANS COMPENSATION FOR SERVICE-CONNECTED DISABILITY OCT2018"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.va.gov/centerforminorityveterans/",
-            "bureauCode": [
-                "029:40"
-            ],
-            "rights": "Public- Locate under the overall Department of Veterans Affairs website at the bottom of the page under link &#039;minority veterans&#039;",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2005-09-01T04:00:00Z/2013-09-01T04:00:00Z",
-            "modified": "2020-05-15",
-            "keyword": [
-                "minority veterans"
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "029:40"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Earl Newsome",
                 "hasEmail": "mailto:earl.newsome@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OSVA-OOM-001",
+            "dataQuality": true,
             "description": "<p>Web link to the Advisory Committee on Minority Veterans (ACMV) Description and annual reports.  Located as a subordinate link under the Center for Minority Veterans.</p>",
-            "title": "Advisory Committee On Minority Veterans",
-            "programCode": [
-                "029:081"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57163,44 +57147,43 @@
                     "title": "Advisory Committee On Minority Veterans"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
+            "identifier": "VA-OSVA-OOM-001",
+            "issued": "2017-07-26",
+            "keyword": [
                 "minority veterans"
             ],
+            "landingPage": "https://www.va.gov/centerforminorityveterans/",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:081"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Public- Locate under the overall Department of Veterans Affairs website at the bottom of the page under link &#039;minority veterans&#039;",
+            "temporal": "2005-09-01T04:00:00Z/2013-09-01T04:00:00Z",
+            "theme": [
+                "minority veterans"
+            ],
+            "title": "Advisory Committee On Minority Veterans"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/kzrg-6bit",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "coin",
-                "finance"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vicki Soukup",
                 "hasEmail": "mailto:vicki.soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-176",
             "description": "<p>COIN 0017 report  for June 2016</p>",
-            "title": "COIN 0017 report  for June 2016",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57209,39 +57192,40 @@
                     "title": "COIN 0017 June 2016"
                 }
             ],
+            "identifier": "VA-OM-OM-176",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/kzrg-6bit",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Financial"
-            ]
+            ],
+            "title": "COIN 0017 report  for June 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/m29t-u7us",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 104"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/m29t-u7us",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to assist wartime veterans in need whose non-service- connected disabilities are permanent and total preventing them from following a substantially gainful occupation. A Veteran who meets the wartime service requirements is potential eligible if he/she is: \u2022 permanently and totally disabled for reasons not necessarily due to service, \u2022 age 65 or older, or \u2022 is presumed to be totally and permanently disabled for pension purposes because: o he/she is a patient in a nursing home for long-term care due to a disability, or o being disabled, as determined by the Commissioner of Social Security (SS) for purposes of any benefits administered by the Commissioner, such as SS disability benefits or Supplemental Security Income. Income restrictions are prescribed in 38 U.S.C. 1521. Pension is not payable to those whose estates are so large that it is reasonable they use the estate for maintenance. A Veteran meets wartime service requirements if he/she served: \u2022 a total of 90 days or more during one or more periods of war; \u2022 90 or more consecutive days that began or ended during a period of war; or \u2022 for any length of time during a period of war if he/she was discharged or released for a service-connected disability. Veterans entering service after September 7, 1980, must also meet the minimum active duty requirement of 24 months of continuous service or the full period to which the Veteran was called to active duty. (38 U.S.C.5303(A)).</p>",
-            "title": "USA SPENDING C&P B104 PENSION FOR NON-SERVICE CONNECTED FOR VETERANS FEB2019",
-            "isPartOf": "279f1b11-a128-4135-825a-5530f04cb050",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57249,80 +57233,80 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/m29t-u7us/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/m29t-u7us/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/m29t-u7us/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/m29t-u7us/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/m29t-u7us/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/m29t-u7us/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/m29t-u7us/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/m29t-u7us/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/m29t-u7us/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/m29t-u7us",
+            "isPartOf": "279f1b11-a128-4135-825a-5530f04cb050",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 104"
+            ],
+            "landingPage": "https://www.data.va.gov/d/m29t-u7us",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING C&P B104 PENSION FOR NON-SERVICE CONNECTED FOR VETERANS FEB2019"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/m3dj-txsh",
-            "issued": "2024-03-27",
             "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rebecca Matteo",
                 "hasEmail": "mailto:no-reply@ptsd-va.data.socrata.com"
             },
+            "description": "The resources on this page support learning about PTSD and effective treatments, providing treatment, and doing research using PTSD Repository data.",
             "identifier": "https://www.data.va.gov/api/views/m3dj-txsh",
+            "issued": "2024-03-27",
+            "landingPage": "https://www.data.va.gov/d/m3dj-txsh",
+            "modified": "2024-12-18",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "The resources on this page support learning about PTSD and effective treatments, providing treatment, and doing research using PTSD Repository data.",
             "title": "Other Resources"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/m3wv-yen3",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "66f4d3cd-aef4-47f9-8b31-7ea89a41487f",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Nevada FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57330,70 +57314,70 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "66f4d3cd-aef4-47f9-8b31-7ea89a41487f",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/m3wv-yen3",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary Nevada FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/m4e2-gdac",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-20",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
-            "keyword": [
-                "cdfa 64.124"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE D BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE FY2019",
+            "identifier": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
+            "issued": "2019-03-20",
+            "keyword": [
+                "cdfa 64.124"
+            ],
+            "landingPage": "https://www.data.va.gov/d/m4e2-gdac",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
             "programCode": [
                 "029:003"
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE FY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/m5x2-my32",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2020-01-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "women veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA Open Data",
                 "hasEmail": "mailto:OITOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/m5x2-my32",
             "description": "Data pulled from ACS that used to power certain visualizations for the \"Women Veterans Forum\" Story",
-            "title": "Women Veterans Forum - ACS Data for Story",
-            "programCode": [
-                "029:008"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57401,87 +57385,87 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/m5x2-my32/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/m5x2-my32/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/m5x2-my32/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/m5x2-my32/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/m5x2-my32/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/m5x2-my32/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/m5x2-my32/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/m5x2-my32/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/m5x2-my32/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/m5x2-my32",
+            "issued": "2020-01-22",
+            "keyword": [
+                "women veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/m5x2-my32",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:008"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Women Veterans Forum - ACS Data for Story"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/m65a-3me5",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Alaska FY2023",
+            "identifier": "https://www.data.va.gov/api/views/m65a-3me5",
             "issued": "2024-05-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-10",
             "keyword": [
                 "alaska",
                 "fy2024 data",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/m65a-3me5",
+            "modified": "2024-07-10",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/m65a-3me5",
-            "description": "NCVAS State Summary Alaska FY2023",
-            "title": "NCVAS State Summary Alaska FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Alaska FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/m6ip-6r4t",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 032"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/m6ip-6r4t",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to encourage membership in units of the Selected Reserve of the Ready Reserve and to provide educational assistance to members of the reserve components called or ordered to active service in response to a war or national emergency declared by the President or Congress. Generally, to qualify for benefits under MGIB-SR you must (1) Have a six-year obligation to serve in the Selected Reserve signed after June 30, 1985. If you are an officer, you must have agreed to serve six years in addition to your original obligation. For some types of training, it is necessary to have a six-year commitment that begins after September 30, 1990; (2) Complete your initial active duty for training (IADT); (3) Meet the requirement to receive a high school diploma or equivalency certificate before completing IADT. You may not use 12 hours toward a college degree to meet this requirement; and (4) Remain in good standing while serving in an active Selected Reserve unit. Generally, to qualify for benefits under REAP you must have served at least 90 consecutive days on active duty as a result of a call or order to active duty from a reserve component in response to a war or national emergency declared by the President or Congress. This is not a complete list of eligibility requirements. For more information on MGIB-SR and REAP visit <a href=\"http://www.gibill.va.gov\">http://www.gibill.va.gov</a>.</p>",
-            "title": "USA SPENDING EDUCATION CH1606 & CH1607 B032 MONTGOMERY GI BILL SELECTED RESERVE; RESERVE EDUCATIONAL ASSISTANCE PROGRAM MAR2019",
-            "isPartOf": "b2a0a5f0-3d2f-490f-8b42-3eb1db21b8e0",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57489,64 +57473,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/m6ip-6r4t/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/m6ip-6r4t/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/m6ip-6r4t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/m6ip-6r4t/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/m6ip-6r4t/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/m6ip-6r4t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/m6ip-6r4t/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/m6ip-6r4t/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/m6ip-6r4t/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/m6ip-6r4t",
+            "isPartOf": "b2a0a5f0-3d2f-490f-8b42-3eb1db21b8e0",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 032"
+            ],
+            "landingPage": "https://www.data.va.gov/d/m6ip-6r4t",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING EDUCATION CH1606 & CH1607 B032 MONTGOMERY GI BILL SELECTED RESERVE; RESERVE EDUCATIONAL ASSISTANCE PROGRAM MAR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/budget/report/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2007-01-01T05:00:00Z/2007-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "accountability",
-                "highlights",
-                "performance",
-                "report"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Zlowe",
                 "hasEmail": "mailto:David.Zlowe@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-012",
+            "dataQuality": true,
             "description": "<p>2007 VA Performance and Accountability Report Highlights.</p>",
-            "title": "2007 VA Performance and Accountability Report Highlights",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57555,74 +57537,70 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-012",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accountability",
+                "highlights",
+                "performance",
+                "report"
+            ],
+            "landingPage": "https://www.va.gov/budget/report/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2007-01-01T05:00:00Z/2007-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2007 VA Performance and Accountability Report Highlights"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/m9as-fj6h",
-            "issued": "2023-06-29",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-02",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Kansas FY2021",
+            "identifier": "https://www.data.va.gov/api/views/m9as-fj6h",
+            "issued": "2023-06-29",
             "keyword": [
                 "fy2021 data",
                 "kansas",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/m9as-fj6h",
+            "landingPage": "https://www.data.va.gov/d/m9as-fj6h",
+            "modified": "2024-06-02",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Kansas FY2021",
             "title": "NCVAS State Summary Kansas FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Number_of_VGLI_Enrolled_by_State.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-12-01T05:00:00Z/2011-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Members_Enrolled_in_VGLI_by_State.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "insurance",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2011-015",
+            "dataQuality": true,
             "description": "<p>Provides the number of Veterans insured under the Veterans' Group Life Insurance (VGLI) program by state.  This report provides a snapshot of the active VGLI membership as of December 31, 2011.  For members who reside outside the United States, membership is not identified by individual country.  The total number of members was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "Number of VGLI Policyholders Enrolled by State",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57630,66 +57608,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mbez-wgqg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mbez-wgqg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mbez-wgqg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/mbez-wgqg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mbez-wgqg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mbez-wgqg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mbez-wgqg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mbez-wgqg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mbez-wgqg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-015",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Number_of_VGLI_Enrolled_by_State.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Members_Enrolled_in_VGLI_by_State.doc"
+            ],
+            "temporal": "2012-12-01T05:00:00Z/2011-12-31T05:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Number of VGLI Policyholders Enrolled by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mbng-xsap",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-03T04:00:00Z/2014-10-03T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "facilities"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:tom.garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-064",
+            "dataQuality": true,
             "description": "<p>These report maps reflect a list of VA Facilities</p>",
-            "title": "Department of Veteran Affairs Facilities by State",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57698,46 +57683,45 @@
                     "title": "Department of Veterans Affairs Facilities by State"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-064",
+            "issued": "2017-07-26",
+            "keyword": [
+                "facilities"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mbng-xsap",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-03T04:00:00Z/2014-10-03T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veteran Affairs Facilities by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mcjn-bnqy",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-08-16",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-21",
-            "keyword": [
-                "religion",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS Mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "4b94ff43-3b72-4cd5-9894-ccfe8fc58716",
+            "dataQuality": true,
             "description": "<p>This dataset provide a count of Veteran by their religious affiliation and state of residence. The dataset set covers all 50 states, District of Columbia and other territories.</p>",
-            "title": "Veteran Religious Affiliation by State",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57745,46 +57729,41 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "4b94ff43-3b72-4cd5-9894-ccfe8fc58716",
+            "issued": "2017-08-16",
+            "keyword": [
+                "religion",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mcjn-bnqy",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-21",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Socioeconomics"
-            ]
+            ],
+            "title": "Veteran Religious Affiliation by State"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_enrollment_by_state.csv",
-            "bureauCode": [
-                "029:25"
-            ],
-            "issued": "2017-07-26",
-            "temporal": "2009-09-01T04:00:00Z/2011-09-30T04:00:00Z",
             "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotesNumber_of_Veterans_Enrolled_in_VGLI_by_State_2.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "insurance",
-                "state"
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "029:25"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2011-014",
+            "dataQuality": true,
             "description": "<p>Provides the number of Veterans insured under the Veterans' Group Life Insurance (VGLI) program by state.  This report provides a snapshot of the active VGLI membership as of September 30, 2011.  For members who reside outside the United States, membership is not identified by individual country.  The total number of members was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "Number of Veterans Insured by VGLI by State as of September 30, 2011",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57792,98 +57771,100 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mdiq-qdvv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mdiq-qdvv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mdiq-qdvv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/mdiq-qdvv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mdiq-qdvv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mdiq-qdvv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mdiq-qdvv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mdiq-qdvv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mdiq-qdvv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-014",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_enrollment_by_state.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotesNumber_of_Veterans_Enrolled_in_VGLI_by_State_2.doc"
+            ],
+            "temporal": "2009-09-01T04:00:00Z/2011-09-30T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Number of Veterans Insured by VGLI by State as of September 30, 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/mdjj-7nhd",
-            "issued": "2019-10-30",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-30",
-            "keyword": [
-                "about"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data Team",
                 "hasEmail": "mailto:OITopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/mdjj-7nhd",
             "description": "This page acts as a brief introduction to the data.va.gov data portal",
-            "title": "About Data.va.gov",
+            "identifier": "https://www.data.va.gov/api/views/mdjj-7nhd",
+            "issued": "2019-10-30",
+            "keyword": [
+                "about"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mdjj-7nhd",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2019-10-30",
             "programCode": [
                 "029:000"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "About Data.va.gov"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mdm3-fkn8",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2002-10-01T04:00:00Z/2003-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "annual report",
-                "audit report",
-                "franchise fund"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OM Open Data",
                 "hasEmail": "mailto:VAOMOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-114",
             "description": "<p>FY 2003 Franchise Fund Annual Report Auditor's Report</p>",
-            "title": "FY 2003 Franchise Fund Annual Report Auditor's Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57892,97 +57873,86 @@
                     "title": "FY 2003 Franchise Fund Annual Report Auditor's Report"
                 }
             ],
+            "identifier": "VA-OM-OM-114",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "audit report",
+                "franchise fund"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mdm3-fkn8",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-06-10",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2002-10-01T04:00:00Z/2003-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "FY 2003 Franchise Fund Annual Report Auditor's Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Elwell",
+                "hasEmail": "mailto:thomas.elwell@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Fact sheet to guide Veterans and Beneficiaries on the benefits available to Veterans at discharge.</p>",
+            "identifier": "VA-VBA-MEDIAPUB-004",
+            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
             "issued": "2017-07-26",
-            "temporal": "2008-10-01T04:00:00Z/2004-10-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
             "keyword": [
                 "benefits fact sheet",
                 "general benefit information",
                 "va benefits",
                 "va fact sheet"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Elwell",
-                "hasEmail": "mailto:thomas.elwell@va.gov"
-            },
+            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-08",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-MEDIAPUB-004",
-            "description": "<p>Fact sheet to guide Veterans and Beneficiaries on the benefits available to Veterans at discharge.</p>",
-            "title": "VA Benefits -Benefits delivery at Discharge",
-            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2008-10-01T04:00:00Z/2004-10-01T04:00:00Z",
             "theme": [
                 "General Benefit Information"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Benefits -Benefits delivery at Discharge"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/healthequity/NVHER.asp",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-19",
-            "keyword": [
-                "age",
-                "demographics",
-                "ethnicity",
-                "geography",
-                "health",
-                "health equity",
-                "mental health",
-                "ohe",
-                "patient",
-                "race",
-                "registry",
-                "sex",
-                "utilization",
-                "va",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Office of Health Equity",
                 "hasEmail": "mailto:healthequity@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/mg53-aau5",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/HEALTHEQUITY/docs/National_Veterans_Health_Equity_Report_FY2013_FINAL_508_Comp.pdf#page=165",
             "description": "<p>The National Veteran Health Equity Report details patterns and provides comparative rates of health conditions for vulnerable Veteran groups. Specifically, this report is designed to provide basic comparative information on the sociodemographics, utilization patterns and rates of diagnosed health conditions among the groups over which the VHA Office of Health Equity (OHE) has responsibility with respect to monitoring, evaluating and acting on identified disparities in access, use, care, quality and outcomes. The report allows the VA, Veterans, and stakeholders to monitor the care vulnerable Veterans receive and set goals for improving their care.</p>",
-            "title": "VA-OHE-NVHER",
-            "isPartOf": "VA-VHA-OHE-002",
-            "programCode": [
-                "029:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57990,47 +57960,83 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mg53-aau5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mg53-aau5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mg53-aau5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/mg53-aau5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mg53-aau5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mg53-aau5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mg53-aau5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mg53-aau5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mg53-aau5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/HEALTHEQUITY/docs/National_Veterans_Health_Equity_Report_FY2013_FINAL_508_Comp.pdf#page=165",
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/mg53-aau5",
+            "isPartOf": "VA-VHA-OHE-002",
+            "issued": "2017-07-26",
+            "keyword": [
+                "age",
+                "demographics",
+                "ethnicity",
+                "geography",
+                "health",
+                "health equity",
+                "mental health",
+                "ohe",
+                "patient",
+                "race",
+                "registry",
+                "sex",
+                "utilization",
+                "va",
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/healthequity/NVHER.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-07-19",
+            "programCode": [
+                "029:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
             "theme": [
                 "Veteran health equity"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA-OHE-NVHER"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Monica Reyes",
+                "hasEmail": "mailto:monica.reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Reserve Educational Assistance Program (Chapter 1606/1607) for March 2014</p>",
+            "identifier": "VA-VBA-USASPENDING032014-051",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-03-01T05:00:00Z/2014-03-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 028",
                 "chapter 1606 1607",
@@ -58038,66 +58044,39 @@
                 "reap",
                 "usa spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:monica.reyes@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING032014-051",
-            "description": "<p>USA Spending- Reserve Educational Assistance Program (Chapter 1606/1607) for March 2014</p>",
-            "title": "USA Spending file- Education- March 2014-Chapter 1606/1607- CFDA 64.032",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014-03-01T05:00:00Z/2014-03-31T04:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- Education- March 2014-Chapter 1606/1607- CFDA 64.032"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www1.va.gov/VETDATA/docs/Datagov/FY09_insurance_St_11-13-09_GDX.csv",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2009-01-01T05:00:00Z/2009-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www1.va.gov/VETDATA/docs/Datagov/FY09_insurance_St_11-13-09_GDX.csv"
-            ],
-            "keyword": [
-                "expenditure",
-                "insurance",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2009-003",
+            "dataQuality": true,
             "description": "<p>2009 Veteran life insurance expenditures by state.  Expenditures represented the actual disbursements from Insurance's Award and Inforce systems.</p>",
-            "title": "2009 Veterans' Insurance Expenditure by State",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58105,74 +58084,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mgkh-zumz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mgkh-zumz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mgkh-zumz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/mgkh-zumz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mgkh-zumz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mgkh-zumz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mgkh-zumz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mgkh-zumz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mgkh-zumz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2009-003",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "expenditure",
+                "insurance",
+                "veteran"
+            ],
+            "landingPage": "https://www1.va.gov/VETDATA/docs/Datagov/FY09_insurance_St_11-13-09_GDX.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www1.va.gov/VETDATA/docs/Datagov/FY09_insurance_St_11-13-09_GDX.csv"
+            ],
+            "temporal": "2009-01-01T05:00:00Z/2009-12-31T05:00:00Z",
             "theme": [
                 "Section 9. Federal Government Finances and Employment"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2009 Veterans' Insurance Expenditure by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mh3z-uri4",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-05-24",
-            "temporal": "2005-10-01T04:00:00Z/2009-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-09-30",
-            "keyword": [
-                "acute pancreatitis",
-                "ai",
-                "drug treatment",
-                "dyslipidemia",
-                "hydroxymethylglutaryl-coa reductase inhibitors (statins)",
-                "machine-learning",
-                "research",
-                "usg-artificial-intelligence",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Open Data",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "NO_ID_AP1htg_Dataset",
+            "dataQuality": true,
+            "describedBy": "https://www.data.va.gov/dataset/hypertriglyceridemia-pancreatitis-vha/resource/515281e1-5b09-4925-b478-2fa9f2e27ce7",
             "description": "<p>Person-level clinical data on patients admitted for acute pancreatitis Oct 2005-Sep 2009 in Veterans Health Administration hospitals.</p>",
-            "title": "NO_ID_AP1htg_Dataset",
-            "isPartOf": "1edcf5e7-7d20-4f1e-8970-91ed05e9bc0f",
-            "programCode": [
-                "029:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58180,67 +58156,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mh3z-uri4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mh3z-uri4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mh3z-uri4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/mh3z-uri4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mh3z-uri4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mh3z-uri4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mh3z-uri4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mh3z-uri4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mh3z-uri4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.data.va.gov/dataset/hypertriglyceridemia-pancreatitis-vha/resource/515281e1-5b09-4925-b478-2fa9f2e27ce7",
-            "dataQuality": true,
+            "identifier": "NO_ID_AP1htg_Dataset",
+            "isPartOf": "1edcf5e7-7d20-4f1e-8970-91ed05e9bc0f",
+            "issued": "2017-05-24",
+            "keyword": [
+                "acute pancreatitis",
+                "ai",
+                "drug treatment",
+                "dyslipidemia",
+                "hydroxymethylglutaryl-coa reductase inhibitors (statins)",
+                "machine-learning",
+                "research",
+                "usg-artificial-intelligence",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mh3z-uri4",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-09-30",
+            "programCode": [
+                "029:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2005-10-01T04:00:00Z/2009-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NO_ID_AP1htg_Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mh9y-sw4c",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-07-01T04:00:00Z/2015-07-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "debt referrals"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vikki Soukup",
                 "hasEmail": "mailto:Vikki.Soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-141",
+            "dataQuality": true,
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "COIN 146 July 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58248,43 +58232,43 @@
                     "mediaType": "text/plain"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-141",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referrals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mh9y-sw4c",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-07-01T04:00:00Z/2015-07-31T04:00:00Z",
             "theme": [
                 "financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "COIN 146 July 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mhib-dgqv",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "veteran employment federal",
-                "veteran employment in federal service"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS Mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-101-102a",
+            "dataQuality": true,
             "description": "<p>Employment of Veterans in the Federal Executive Branch Fiscal Year 2012.</p>",
-            "title": "Veterans Employment in the Federal Executive Branch: Fiscal Year 2012",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58292,60 +58276,88 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-101-102a",
+            "issued": "2017-07-26",
+            "keyword": [
+                "veteran employment federal",
+                "veteran employment in federal service"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mhib-dgqv",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Socioeconomics"
-            ]
+            ],
+            "title": "Veterans Employment in the Federal Executive Branch: Fiscal Year 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mhj2-hfpb",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-09",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
+            "dataQuality": true,
+            "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/mhj2-hfpb/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                }
+            ],
+            "identifier": "86e7357c-354d-495f-a587-73418f2f9acb",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mhj2-hfpb",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "86e7357c-354d-495f-a587-73418f2f9acb",
-            "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Arizona FY2016",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/mhj2-hfpb/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "title": "State Summary Arizona FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mick-4aih",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Primary Care Analytics Team",
+                "hasEmail": "mailto:PCAT@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://github.com/AdamVAPug/HighRiskMixIRT",
+            "description": "There are 2 datasets of high-risk patient populations; one from calendar year 2014 (N1 = 937,407),  for which we used International Classification of Disease Version 9 (ICD9) codes to identify comorbid conditions, and a second, more recent population selected from June 2017 to June 2018  (N2 = 979,607) for use with the newer International Classification of Disease Version 10 (ICD10) codes.\n\nDOI: 10.1109/JBHI.2019.2948734",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/mick-4aih/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/mick-4aih",
             "issued": "2020-07-21",
-            "@type": "dcat:Dataset",
-            "temporal": "2014-01/2018-06",
-            "modified": "2024-02-15",
             "keyword": [
                 "chronic conditions",
                 "high-risk",
@@ -58358,69 +58370,38 @@
                 "veterans health administration",
                 "vha"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Primary Care Analytics Team",
-                "hasEmail": "mailto:PCAT@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/mick-4aih",
+            "language": [
+                "English"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-02-15",
+            "programCode": [
+                "029:048"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/mick-4aih",
-            "description": "There are 2 datasets of high-risk patient populations; one from calendar year 2014 (N1 = 937,407),  for which we used International Classification of Disease Version 9 (ICD9) codes to identify comorbid conditions, and a second, more recent population selected from June 2017 to June 2018  (N2 = 979,607) for use with the newer International Classification of Disease Version 10 (ICD10) codes.\n\nDOI: 10.1109/JBHI.2019.2948734",
-            "title": "ICD9 and ICD10 Comorbid Diagnosis for High Risk Veteran Patients",
-            "programCode": [
-                "029:048"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/mick-4aih/application/zip",
-                    "mediaType": "application/zip"
-                }
-            ],
             "spatial": "From a national population of patients in the upper decile of risk for 1 year hospitalization as determined by the Veterans Health Administration (VHA) Care Assessment Needs score (CAN).",
-            "describedBy": "https://github.com/AdamVAPug/HighRiskMixIRT",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2014-01/2018-06",
             "theme": [
                 "Multimorbidity"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "ICD9 and ICD10 Comorbid Diagnosis for High Risk Veteran Patients"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mig9-wtsh",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "2014",
-                "compensation",
-                "pension",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-155",
             "description": "<p>This report provides county-level estimates of the number of Veterans who received VA Disability Compensation or Pension benefits during FY 2015. It includes the Veterans' total disability rating group, and gender. Bewtween 2014 and 2015, the number of Veterans receiving disability benefits has increased from 3.9 million to 4.5 million.</p>",
-            "title": "Compensation and Pension by County: 2015",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58429,43 +58410,46 @@
                     "title": "Compensation and Pension by County: 2015"
                 }
             ],
+            "identifier": "VA-OEI-OEI-155",
+            "issued": "2017-07-26",
+            "keyword": [
+                "2014",
+                "compensation",
+                "pension",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mig9-wtsh",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Compensation and Pension by County: 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/budget/products.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "budget submission",
-                "fy2013"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OM Open Data",
                 "hasEmail": "mailto:VAOMOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-026",
+            "dataQuality": true,
             "description": "<p>FY2013 VA Budget Submission.</p>",
-            "title": "FY2013 VA Budget Submission",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58474,140 +58458,126 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-026",
+            "issued": "2017-07-26",
+            "keyword": [
+                "budget submission",
+                "fy2013"
+            ],
+            "landingPage": "https://www.va.gov/budget/products.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-10",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY2013 VA Budget Submission"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Monica Reyes",
+                "hasEmail": "mailto:monica.reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Non Service Connected Disability- January 2014.</p>",
+            "identifier": "VA-VBA-USASPENDING012014-017",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-01-01T05:00:00Z/2014-01-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 104",
                 "compensation and pension",
                 "non service connected disability",
                 "usa spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:monica.reyes@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING012014-017",
-            "description": "<p>USA Spending- Non Service Connected Disability- January 2014.</p>",
-            "title": "USA Spending file- 01/2014 Compensation and Pension-  CFDA 64.104",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014-01-01T05:00:00Z/2014-01-31T05:00:00Z",
             "theme": [
                 "USA SPENDING"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- 01/2014 Compensation and Pension-  CFDA 64.104"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Elwell",
+                "hasEmail": "mailto:thomas.elwell@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Facts about the Fiduciary Program</p>",
+            "identifier": "VA-VBA-MEDIAPUB-051",
+            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
             "issued": "2017-07-26",
-            "temporal": "2012-11-01T04:00:00Z/2012-11-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
             "keyword": [
                 "benefits fact sheet",
                 "general benefit information",
                 "va benefits",
                 "va fact sheet"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Elwell",
-                "hasEmail": "mailto:thomas.elwell@va.gov"
-            },
+            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-08",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-MEDIAPUB-051",
-            "description": "<p>Facts about the Fiduciary Program</p>",
-            "title": "Facts about the Fiduciary Program",
-            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2012-11-01T04:00:00Z/2012-11-01T04:00:00Z",
             "theme": [
                 "General Benefit Information"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Facts about the Fiduciary Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mjp6-ik6p",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2019-11-12",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-19",
-            "keyword": [
-                "age",
-                "demographics",
-                "ethnicity",
-                "geography",
-                "health",
-                "health-equity",
-                "mental health",
-                "ohe",
-                "patient",
-                "race",
-                "registry",
-                "sex",
-                "utilization",
-                "va",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Office of Health Equity",
                 "hasEmail": "mailto:healthequity@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/mjp6-ik6p",
             "description": "A subset of the FY13 National Veteran Health Equity Report, filtered by sex.\n\nThe National Veteran Health Equity Report details patterns and provides comparative rates of health conditions for vulnerable Veteran groups. Specifically, this report is designed to provide basic comparative information on the sociodemographics, utilization patterns and rates of diagnosed health conditions among the groups over which the VHA Office of Health Equity (OHE) has responsibility with respect to monitoring, evaluating and acting on identified disparities in access, use, care, quality and outcomes. The report allows the VA, Veterans, and stakeholders to monitor the care vulnerable Veterans receive and set goals for improving their care.",
-            "title": "VA-OHE-NVHER-FY13-Diagnoses-Sex",
-            "programCode": [
-                "029:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58615,57 +58585,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mjp6-ik6p/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mjp6-ik6p/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mjp6-ik6p/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/mjp6-ik6p/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mjp6-ik6p/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mjp6-ik6p/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mjp6-ik6p/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mjp6-ik6p/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mjp6-ik6p/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode"
+            "identifier": "https://www.data.va.gov/api/views/mjp6-ik6p",
+            "issued": "2019-11-12",
+            "keyword": [
+                "age",
+                "demographics",
+                "ethnicity",
+                "geography",
+                "health",
+                "health-equity",
+                "mental health",
+                "ohe",
+                "patient",
+                "race",
+                "registry",
+                "sex",
+                "utilization",
+                "va",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mjp6-ik6p",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
+            "modified": "2021-07-19",
+            "programCode": [
+                "029:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VA-OHE-NVHER-FY13-Diagnoses-Sex"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mkgm-v7we",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 109"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/mkgm-v7we",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to compensate veterans for disabilities incurred or aggravated during military service according to the average impairment in earning capacity such disability would cause in civilian occupations. Persons who have suffered disabilities resulting from service in the Armed Forces of the United States. The disability must have been incurred or aggravated by service in the line of duty. Separation from service must have been under other than dishonorable conditions for the period in which the disability was incurred or aggravated.</p>",
-            "title": "USA SPENDING C&P B109 VETERANS COMPENSATION FOR SERVICE-CONNECTED DISABILITY APR2019",
-            "isPartOf": "6013cae5-a8c2-47ff-9c90-9cbdba7bda63",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58673,44 +58657,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mkgm-v7we/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mkgm-v7we/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mkgm-v7we/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/mkgm-v7we/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mkgm-v7we/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mkgm-v7we/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mkgm-v7we/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mkgm-v7we/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mkgm-v7we/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/mkgm-v7we",
+            "isPartOf": "6013cae5-a8c2-47ff-9c90-9cbdba7bda63",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 109"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mkgm-v7we",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING C&P B109 VETERANS COMPENSATION FOR SERVICE-CONNECTED DISABILITY APR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/mmqs-e8b2",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Primary Care Management Module (PCMM) was developed to assist VA facilities in implementing Primary Care.  PCMM supports both Primary Care and non-Primary Care teams.  The software allows the user to set up and define a team, assign positions to the team, assign staff to the positions, assign patients to the team, and assign patients to a Primary Care Provider (PCP) or Associate Provider (AP).  In a Primary Care setting, patients are assigned a PCP, Associate Provider (AP) and/or a Transition Patient Advocate (TPA) who is responsible for delivering essential health care, coordinating all health care services, and serving as the point of access for specialty care.  The PCP is supported by a team of professionals which may include nurses, pharmacists, social workers, etc.  Associate Providers are non-physician clinicians (such as Physicians Assistants, Nurse Practitioners or Residents) who may provide care under the supervision of a presiding PCP.  The PCMM software is considered to be an important component to measure patient demand and the PCPs capacity to meet that demand and to reduce wait times. PCMM was developed to assist facilities in implementing primary care for veterans.  It uses the site's data to identify patients and to assign them to a PCP.  PCMM provides tools to facilitate the startup process, automating such tasks as identifying patients to be assigned to primary care; assigning patients to teams, and assigning patients to practitioners via team positions.</p>",
+            "identifier": "VA-VHA-OIA-052",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2004-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "health",
                 "management",
@@ -58723,61 +58726,42 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/mmqs-e8b2",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-052",
-            "description": "<p>The Primary Care Management Module (PCMM) was developed to assist VA facilities in implementing Primary Care.  PCMM supports both Primary Care and non-Primary Care teams.  The software allows the user to set up and define a team, assign positions to the team, assign staff to the positions, assign patients to the team, and assign patients to a Primary Care Provider (PCP) or Associate Provider (AP).  In a Primary Care setting, patients are assigned a PCP, Associate Provider (AP) and/or a Transition Patient Advocate (TPA) who is responsible for delivering essential health care, coordinating all health care services, and serving as the point of access for specialty care.  The PCP is supported by a team of professionals which may include nurses, pharmacists, social workers, etc.  Associate Providers are non-physician clinicians (such as Physicians Assistants, Nurse Practitioners or Residents) who may provide care under the supervision of a presiding PCP.  The PCMM software is considered to be an important component to measure patient demand and the PCPs capacity to meet that demand and to reduce wait times. PCMM was developed to assist facilities in implementing primary care for veterans.  It uses the site's data to identify patients and to assign them to a PCP.  PCMM provides tools to facilitate the startup process, automating such tasks as identifying patients to be assigned to primary care; assigning patients to teams, and assigning patients to practitioners via team positions.</p>",
-            "title": "VHA Support Service Center Primary Care Management Module (PCMM)",
-            "programCode": [
-                "029:041"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2004-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VHA Support Service Center Primary Care Management Module (PCMM)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mmtp-itim",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 126"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/mmtp-itim",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide direct loans to certain veterans who are, or whose spouses are, Native Americans for the purchase or construction of homes on trust lands. Veterans who are, or whose spouses are, recognized by a Federally Recognized Tribal Government as a Native American and who: (a) Served on active duty on or after September 16, 1940, and were discharged or released under conditions other than dishonorable. If service was any time during World War II, the Korean Conflict, the Vietnam-era, or the Persian Gulf War, then the Native American Veteran must have served on active duty for 90 days or more; peacetime service only must have served a minimum of 181 days continuous active duty. If separated from enlisted service which began after September 7, 1980, or service as an officer which began after October 16, 1981, a veteran must also have served at least 24 months of continuous active duty or the full period for which called or ordered to active duty. Veterans of such recent service may qualify with less service time if they have a compensable service-connected disability or were discharged after at least 181 days, under the authority of 10 U.S.C 1171 or 1173. (b) Any veteran in the above classes with less service but discharged with a service-connected disability. (c) If acknowledged as a Native American by a Federally Recognized Tribal Government, unmarried surviving spouses of otherwise eligible veterans who died in service or whose deaths were attributable to service-connected disabilities and spouses of members of the Armed Forces serving on active duty, who are listed as missing in action, or as prisoners of war and who have been so listed 90 days or more. (d) Members of the Selected Reservists who ae, or whose spouses ae, recognized by a Federally Recognized Tribal Government as Native Americans and who are not otherwise eligible for home loan benefits and who have completed a total of 6 years in the Selected Reserves followed by an honorable discharge, placement on the retired list, or continued service.</p>",
-            "title": "USA SPENDING LGY B126 NATIVE AMERICAN VETERAN DIRECT LOAN PROGRAM MAR2019",
-            "isPartOf": "e30045ea-2153-40e3-91bc-23c0014ae69c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58785,66 +58769,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mmtp-itim/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mmtp-itim/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mmtp-itim/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/mmtp-itim/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mmtp-itim/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mmtp-itim/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mmtp-itim/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mmtp-itim/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mmtp-itim/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/mmtp-itim",
+            "isPartOf": "e30045ea-2153-40e3-91bc-23c0014ae69c",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 126"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mmtp-itim",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING LGY B126 NATIVE AMERICAN VETERAN DIRECT LOAN PROGRAM MAR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VBA/blob/master/FY12%204th%20qtr%20EDU%20recp%20by%20State.csv",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "education",
-                "education benefits",
-                "edu recipients",
-                "fy 2009 vba benefits recipients",
-                "vba performance"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Salminio Garner",
                 "hasEmail": "mailto:Garner.Salminio@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-EDU2014-001",
+            "dataQuality": true,
             "description": "<p>VBA Education Benefits Recipients by State for FY 2009.</p>",
-            "title": "VBA Education Benefits Recipients by State- FY 2009",
-            "isPartOf": "VA-VBA-MASTER-EDUCATION-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58852,44 +58832,48 @@
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-EDU2014-001",
+            "isPartOf": "VA-VBA-MASTER-EDUCATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "education",
+                "education benefits",
+                "edu recipients",
+                "fy 2009 vba benefits recipients",
+                "vba performance"
+            ],
+            "landingPage": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VBA/blob/master/FY12%204th%20qtr%20EDU%20recp%20by%20State.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
             "theme": [
                 "VBA Education Benefits"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VBA Education Benefits Recipients by State- FY 2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mnzh-8gpn",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "poverty",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-154",
+            "dataQuality": true,
             "description": "<p>This report uses 2014 American Community Survey data to compare the demographic and socioeconomic characteristics of Veterans in poverty to non-Veterans in poverty.</p>",
-            "title": "Profile of Veterans in Poverty: 2014",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58898,43 +58882,43 @@
                     "title": "Profile of Veterans in Poverty: 2014"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-154",
+            "issued": "2017-07-26",
+            "keyword": [
+                "poverty",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mnzh-8gpn",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Socioeconomics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Profile of Veterans in Poverty: 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/mphx-t4we",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2018-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "aggregation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Short",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "135720b6-b413-45f1-8a16-8d39b808d6bf",
+            "dataQuality": true,
             "description": "<p>Expose health and benefit data received from various sources based on business need.</p>",
-            "title": "Exposure of Data",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58943,36 +58927,37 @@
                     "title": "Exposure of Data"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "135720b6-b413-45f1-8a16-8d39b808d6bf",
+            "issued": "2018-02-23",
+            "keyword": [
+                "aggregation"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mphx-t4we",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "Exposure of Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mpkr-yv95",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-12-14",
-            "@type": "dcat:Dataset",
-            "modified": "2021-12-14",
-            "keyword": [
-                "survey"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA NCOD",
                 "hasEmail": "mailto:vhancod@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/mpkr-yv95",
             "description": "VA All Employee Survey (AES) and Federal Employee Viewpoint Survey (FEVS) shared item scores",
-            "title": "AES - FEVS",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58980,58 +58965,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mpkr-yv95/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mpkr-yv95/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mpkr-yv95/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/mpkr-yv95/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mpkr-yv95/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mpkr-yv95/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mpkr-yv95/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mpkr-yv95/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mpkr-yv95/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/mpkr-yv95",
+            "issued": "2021-12-14",
+            "keyword": [
+                "survey"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mpkr-yv95",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2021-12-14",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "AES - FEVS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mqau-h5t2",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 126"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/mqau-h5t2",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide direct loans to certain veterans who are, or whose spouses are, Native Americans for the purchase or construction of homes on trust lands. Veterans who are, or whose spouses are, recognized by a Federally Recognized Tribal Government as a Native American and who: (a) Served on active duty on or after September 16, 1940, and were discharged or released under conditions other than dishonorable. If service was any time during World War II, the Korean Conflict, the Vietnam-era, or the Persian Gulf War, then the Native American Veteran must have served on active duty for 90 days or more; peacetime service only must have served a minimum of 181 days continuous active duty. If separated from enlisted service which began after September 7, 1980, or service as an officer which began after October 16, 1981, a veteran must also have served at least 24 months of continuous active duty or the full period for which called or ordered to active duty. Veterans of such recent service may qualify with less service time if they have a compensable service-connected disability or were discharged after at least 181 days, under the authority of 10 U.S.C 1171 or 1173. (b) Any veteran in the above classes with less service but discharged with a service-connected disability. (c) If acknowledged as a Native American by a Federally Recognized Tribal Government, unmarried surviving spouses of otherwise eligible veterans who died in service or whose deaths were attributable to service-connected disabilities and spouses of members of the Armed Forces serving on active duty, who are listed as missing in action, or as prisoners of war and who have been so listed 90 days or more. (d) Members of the Selected Reservists who ae, or whose spouses ae, recognized by a Federally Recognized Tribal Government as Native Americans and who are not otherwise eligible for home loan benefits and who have completed a total of 6 years in the Selected Reserves followed by an honorable discharge, placement on the retired list, or continued service.</p>",
-            "title": "USA SPENDING LGY B126 NATIVE AMERICAN VETERAN DIRECT LOAN PROGRAM DEC2018",
-            "isPartOf": "e30045ea-2153-40e3-91bc-23c0014ae69c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59039,63 +59023,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mqau-h5t2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mqau-h5t2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mqau-h5t2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/mqau-h5t2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mqau-h5t2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mqau-h5t2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mqau-h5t2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mqau-h5t2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mqau-h5t2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/mqau-h5t2",
+            "isPartOf": "e30045ea-2153-40e3-91bc-23c0014ae69c",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 126"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mqau-h5t2",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING LGY B126 NATIVE AMERICAN VETERAN DIRECT LOAN PROGRAM DEC2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mqnc-hghc",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2023-09-12",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-12",
-            "keyword": [
-                "engagement",
-                "satisfaction",
-                "survey",
-                "veterans affairs"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA National Center for Organization Development (NCOD)",
                 "hasEmail": "mailto:vhancod@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/mqnc-hghc",
+            "dataQuality": true,
             "description": "VA All Employee Survey (AES) data from the 2022 & 2023 AES administrations. Scores are provided at the station level and up, and the occupation level within hospitals.",
-            "title": "All Employee Survey (AES) 2022 - 2023",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59103,55 +59086,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mqnc-hghc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mqnc-hghc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mqnc-hghc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/mqnc-hghc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mqnc-hghc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mqnc-hghc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mqnc-hghc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mqnc-hghc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mqnc-hghc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/mqnc-hghc",
+            "issued": "2023-09-12",
+            "keyword": [
+                "engagement",
+                "satisfaction",
+                "survey",
+                "veterans affairs"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mqnc-hghc",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2023-09-12",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "All Employee Survey (AES) 2022 - 2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/mqrh-hcwr",
-            "issued": "2024-10-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-21",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center of Veterans Analytics Services",
                 "hasEmail": "mailto:VACONCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/mqrh-hcwr",
             "description": "",
-            "title": "Veterans Class of Work in Government",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59159,42 +59146,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mqrh-hcwr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mqrh-hcwr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mqrh-hcwr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/mqrh-hcwr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mqrh-hcwr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mqrh-hcwr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mqrh-hcwr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mqrh-hcwr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mqrh-hcwr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/mqrh-hcwr",
+            "issued": "2024-10-01",
+            "landingPage": "https://www.data.va.gov/d/mqrh-hcwr",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-10-21",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Class of Work in Government"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-06-09T04:00:00Z/2014-06-09T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/access-audit.asp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/access-audit.asp",
+            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/health/docs/VISN12FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 12 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-086",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -59210,143 +59222,118 @@
                 "wait list",
                 "wait time"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-086",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 12",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN12FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 12 Fact Sheet"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2014-06-09T04:00:00Z/2014-06-09T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Audit"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 12"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Monica Reyes",
+                "hasEmail": "mailto:monica.reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Veterans Surviving Spouses and Children- February 2014</p>",
+            "identifier": "VA-VBA-USASPENDING032014-047",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-03-01T05:00:00Z/2014-03-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 105",
                 "compensation and pension",
                 "usa spending",
                 "veterans surviving spouses and children"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:monica.reyes@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING032014-047",
-            "description": "<p>USA Spending- Veterans Surviving Spouses and Children- February 2014</p>",
-            "title": "USA Spending file- 03/2014 Compensation and Pension-  CFDA 64.105",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014-03-01T05:00:00Z/2014-03-31T04:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- 03/2014 Compensation and Pension-  CFDA 64.105"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/msrw-uw4y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
-            "keyword": [
-                "cfda 64 105",
-                "cfda 64 110"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "8ad0aa0e-af41-448e-8ebf-287798035e69",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA's determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING C&P B105/B110 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE FY2019",
+            "identifier": "8ad0aa0e-af41-448e-8ebf-287798035e69",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 105",
+                "cfda 64 110"
+            ],
+            "landingPage": "https://www.data.va.gov/d/msrw-uw4y",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
             "programCode": [
                 "029:003"
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING C&P B105/B110 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE FY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/mt4n-bt3h",
-            "issued": "2024-04-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Florinda Balfour",
                 "hasEmail": "mailto:VACONCVAS@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/mt4n-bt3h",
             "description": "",
-            "title": "vetpop age groups graphs fy2024",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59354,57 +59341,54 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mt4n-bt3h/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mt4n-bt3h/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mt4n-bt3h/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/mt4n-bt3h/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mt4n-bt3h/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mt4n-bt3h/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mt4n-bt3h/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mt4n-bt3h/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mt4n-bt3h/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/mt4n-bt3h",
+            "issued": "2024-04-23",
+            "landingPage": "https://www.data.va.gov/d/mt4n-bt3h",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "vetpop age groups graphs fy2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mtmp-rt9d",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "503567e3-6b22-47b7-b35c-ef3a7662f5e8",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Texas FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59412,44 +59396,43 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "503567e3-6b22-47b7-b35c-ef3a7662f5e8",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mtmp-rt9d",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data",
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "State Summary Texas FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/mtxz-6qd9",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "healthcare",
-                "numi"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Clark Timmins",
                 "hasEmail": "mailto:clark.timmins@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VIA-6",
+            "dataQuality": true,
             "description": "<p>This is the . This service provides webservice methods that allow the user to track inpatient bed movements of patients. All access provided by this interface is read-only.</p>",
-            "title": "National Utilization Management Integration Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59458,42 +59441,41 @@
                     "title": "National Utilization Management Integration Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-VIA-6",
+            "issued": "2017-11-17",
+            "keyword": [
+                "healthcare",
+                "numi"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mtxz-6qd9",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "National Utilization Management Integration Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mu4i-a98q",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "issued": "2020-11-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-11",
-            "keyword": [
-                "ahrq report",
-                "appendix e",
-                "appendix f"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for PTSD",
                 "hasEmail": "mailto:ncptsd@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for PTSD"
-            },
-            "identifier": "https://www.data.va.gov/api/views/mu4i-a98q",
             "description": "The purpose of this project was to identify and abstract data from randomized controlled trials (RCTs) of posttraumatic stress disorder (PTSD) interventions to support the development of a publicly accessible data repository by the National Center for Posttraumatic Stress Disorder.\n\nThe 2019 Report and Evidence Tables (Appendix E & F) are included in the downloadable .zip file. For more information, visit AHRQ's page, and look under \"Previous Versions\" tab: https://effectivehealthcare.ahrq.gov/products/ptsd-pharm-treatment/research",
-            "title": "AHRQ Report and Data Files (2019): Pharmacologic and Nonpharmacologic Treatments for Posttraumatic Stress Disorder",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59501,44 +59483,42 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
+            "identifier": "https://www.data.va.gov/api/views/mu4i-a98q",
+            "issued": "2020-11-24",
+            "keyword": [
+                "ahrq report",
+                "appendix e",
+                "appendix f"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mu4i-a98q",
+            "modified": "2020-06-11",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for PTSD"
+            },
+            "rights": "All data is within the public domain and is currently available for download.",
             "theme": [
                 "Reference"
-            ]
+            ],
+            "title": "AHRQ Report and Data Files (2019): Pharmacologic and Nonpharmacologic Treatments for Posttraumatic Stress Disorder"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
-            "bureauCode": [
-                "029:25"
-            ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "@type": "dcat:Dataset",
-            "modified": "2022-03-05",
-            "keyword": [
-                "abr",
-                "abr2012",
-                "insurance",
-                "insurance benefits fy12",
-                "vba benefits"
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "029:25"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-074",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "SGLI Coverage Level - Active Duty and Reserve Duty",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59547,26 +59527,50 @@
                     "title": "SGLI Coverage Level - Active Duty and Reserve Duty"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-074",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "abr",
+                "abr2012",
+                "insurance",
+                "insurance benefits fy12",
+                "vba benefits"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-05",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR Reports"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SGLI Coverage Level - Active Duty and Reserve Duty"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.techstrategies.oit.va.gov/ETSP.asp",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Edward A. (Ted) Diaz",
+                "hasEmail": "mailto:Edward.Diaz2@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>One VA Enterprise Technology Strategic Plan (ETSP)</p>",
+            "identifier": "VA-OIT-ASD-003",
             "issued": "2017-07-26",
-            "temporal": "2014-02-01T05:00:00Z/2015-02-01T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "enterprise technical architecture",
                 "enterprise technology strategic plan",
@@ -59577,62 +59581,41 @@
                 "technology",
                 "technology vision"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Edward A. (Ted) Diaz",
-                "hasEmail": "mailto:Edward.Diaz2@va.gov"
-            },
+            "landingPage": "https://www.techstrategies.oit.va.gov/ETSP.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:078"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-OIT-ASD-003",
-            "description": "<p>One VA Enterprise Technology Strategic Plan (ETSP)</p>",
-            "title": "One VA Enterprise Technology Strategic Plan (ETSP)",
-            "programCode": [
-                "029:078"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2014-02-01T05:00:00Z/2015-02-01T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "One VA Enterprise Technology Strategic Plan (ETSP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/budget/report/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2002-01-01T05:00:00Z/2002-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "accountability",
-                "performance",
-                "report"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Zlowe",
                 "hasEmail": "mailto:David.Zlowe@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-017",
+            "dataQuality": true,
             "description": "<p>2002 VA Performance and Accountability Report.</p>",
-            "title": "2002 VA Performance and Accountability Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59641,29 +59624,58 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-017",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accountability",
+                "performance",
+                "report"
+            ],
+            "landingPage": "https://www.va.gov/budget/report/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2002-01-01T05:00:00Z/2002-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2002 VA Performance and Accountability Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "accrualPeriodicity": "R/P2M",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-09-01T04:00:00Z/2014-09-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/access-audit.asp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/access-audit.asp",
+            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/VAMC_Patient_Access_Data_20140918_pending.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "September 18, 2014"
+                }
             ],
+            "identifier": "VA-VHA-OIA-065",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -59677,71 +59689,43 @@
                 "wait list",
                 "wait time"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-065",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2014 Sept 18",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/VAMC_Patient_Access_Data_20140918_pending.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "September 18, 2014"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2014-09-01T04:00:00Z/2014-09-01T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2014 Sept 18"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mwmj-nbmi",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-09",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS Mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "22b972b2-6e44-4337-9139-9a7ec3ee38c4",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Alabama FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59749,19 +59733,41 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "22b972b2-6e44-4337-9139-9a7ec3ee38c4",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mwmj-nbmi",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary Alabama FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Monica Reyes",
+                "hasEmail": "mailto:monica.reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Education-Post 9/11 Veterans Educational Assistance ( Chapter33) for January 2014.</p>",
+            "identifier": "VA-VBA-USASPENDING012014-021",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-01-01T05:00:00Z/2014-01-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 028",
                 "ch33",
@@ -59769,65 +59775,37 @@
                 "education",
                 "usa spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:monica.reyes@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING012014-021",
-            "description": "<p>USA Spending- Education-Post 9/11 Veterans Educational Assistance ( Chapter33) for January 2014.</p>",
-            "title": "USA Spending file- 01/2014-Education- Chapter 33/ CFDA 64.028",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014-01-01T05:00:00Z/2014-01-31T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- 01/2014-Education- Chapter 33/ CFDA 64.028"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mx3r-2rtv",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-03-16",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-05",
-            "keyword": [
-                "utilization",
-                "va benefits",
-                "va programs",
-                "va services",
-                "veteran benefits",
-                "veterans",
-                "veterans benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/mx3r-2rtv",
             "description": "Percentage distributions of sexes across eras of initial service, FY2021. Data underlying the seventh figure of Part 1 of the FY 2021 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Percentage Distribution of Users by Era of Initial Service and Sex, FY 2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59835,99 +59813,104 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mx3r-2rtv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mx3r-2rtv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mx3r-2rtv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/mx3r-2rtv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mx3r-2rtv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mx3r-2rtv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mx3r-2rtv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mx3r-2rtv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mx3r-2rtv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/mx3r-2rtv",
+            "issued": "2022-03-16",
+            "keyword": [
+                "utilization",
+                "va benefits",
+                "va programs",
+                "va services",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mx3r-2rtv",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-01-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Percentage Distribution of Users by Era of Initial Service and Sex, FY 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Monica Reyes",
+                "hasEmail": "mailto:monica.reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Direct Home Loan- February- 2014.</p>",
+            "identifier": "VA-VBA-USASPENDING012014-044",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-02-01T05:00:00Z/2014-02-28T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 118",
                 "direct home loan",
                 "lgy",
                 "usa spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:monica.reyes@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING012014-044",
-            "description": "<p>USA Spending- Direct Home Loan- February- 2014.</p>",
-            "title": "USA Spending file- 02/2014-Direct Home Loan-  CFDA 64.118",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014-02-01T05:00:00Z/2014-02-28T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- 02/2014-Direct Home Loan-  CFDA 64.118"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/myb6-uzk7",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-10-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "healthcare",
-                "minority veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tamara Lee",
                 "hasEmail": "mailto:tamara.lee@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veteran Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/myb6-uzk7",
             "description": "Dataset listing the number of minority veterans enrolled in VA healthcare for the year 2014.",
-            "title": "Number of Minority Veterans Enrolled in VA Health Care, by VA Health Care Usage, 2014",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59935,57 +59918,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/myb6-uzk7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/myb6-uzk7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/myb6-uzk7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/myb6-uzk7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/myb6-uzk7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/myb6-uzk7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/myb6-uzk7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/myb6-uzk7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/myb6-uzk7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/myb6-uzk7",
+            "issued": "2019-10-24",
+            "keyword": [
+                "healthcare",
+                "minority veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/myb6-uzk7",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veteran Affairs"
+            },
+            "title": "Number of Minority Veterans Enrolled in VA Health Care, by VA Health Care Usage, 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/myk6-948d",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 028"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/myk6-948d",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to help servicepersons adjust to civilian life after separation from military service, assist in the recruitment and retention of highly qualified personnel in the active and reserve components in the Armed Forces by providing education benefits, and to provide educational opportunities to the dependents of certain service members and veterans. Individuals who entered active duty after September 10, 2001 may be eligible for the Post-9/11 GI Bill. Individuals can use the Post-9/11 GI Bill after serving 90 days on active duty (excluding entry level and skill training). Only periods of active duty under title 10 will be used to establish eligibility for the Post 9/11 GI Bill. A high school diploma or equivalency certificate is always required for eligibility. Individuals who are eligible for the Montgomery GI Bill \u2013 Active Duty (chapter 30), the Montgomery GI Bill \u2013 Selected Reserve (chapter 1606), or the Reserve Educational Assistance Program (REAP) will have to make an irrevocable election to relinquish eligibility under one of those benefit programs to establish eligibility under the Post-9/11 GI Bill. The dependent children of a person who died in the line of duty while serving as a member of the Armed Forces may be eligible to use benefits under the Fry Scholarship provision of the Post-9/11 GI Bill. The spouse and/or child(ren) of a veteran or service member may be eligible for the Post 9/11 GI Bill if the veteran or service member transfers entitlement to those dependents. Eligibility to transfer entitlement to dependents is determined by the Department of Defense. This is not a complete list of eligibility requirements. For more information on the latest changes to the Post-9/11 GI Bill go to the VA web-site.</p>",
-            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE MAY2019",
-            "isPartOf": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59993,43 +59977,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/myk6-948d/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/myk6-948d/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/myk6-948d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/myk6-948d/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/myk6-948d/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/myk6-948d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/myk6-948d/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/myk6-948d/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/myk6-948d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/myk6-948d",
+            "isPartOf": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 028"
+            ],
+            "landingPage": "https://www.data.va.gov/d/myk6-948d",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE MAY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/myti-3m5y",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHASailOperations",
+                "hasEmail": "mailto:VHASailOperations@va.gov"
+            },
+            "dataQuality": true,
+            "description": "Strategic Analytics for Improvement and Learning Value Model or SAIL, is a system for summarizing hospital system performance within Veterans Health Administration (VHA). SAIL assesses key Quality measures in areas such as death rate, complications, and patient satisfaction, as well as overall efficiency at individual VA Medical Centers (VAMCs).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/myti-3m5y/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/myti-3m5y",
+            "isPartOf": "VA-VHA-OIA-122",
             "issued": "2024-05-15",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-10-01/2024-03-31",
-            "modified": "2024-10-01",
             "keyword": [
                 "2024",
                 "analytics",
@@ -60050,53 +60063,52 @@
                 "sail",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHASailOperations",
-                "hasEmail": "mailto:VHASailOperations@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/myti-3m5y",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-10-01",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/myti-3m5y",
-            "description": "Strategic Analytics for Improvement and Learning Value Model or SAIL, is a system for summarizing hospital system performance within Veterans Health Administration (VHA). SAIL assesses key Quality measures in areas such as death rate, complications, and patient satisfaction, as well as overall efficiency at individual VA Medical Centers (VAMCs).",
-            "title": "SAIL FY2024 Hospital Performance - All Facilities",
-            "isPartOf": "VA-VHA-OIA-122",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/myti-3m5y/application/x-zip-compressed",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
             "spatial": "United States, Puerto Rico",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "temporal": "2023-10-01/2024-03-31",
             "theme": [
                 "Hospital Quality Measurement"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAIL FY2024 Hospital Performance - All Facilities"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P2M",
+            "bureauCode": [
+                "029:15"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/access-audit.asp",
+            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
+            "distribution": [
                 {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mz5y-gbsy",
-            "bureauCode": [
-                "029:15"
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/VAMC_Patient_Access_Data_20140828_completed.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "August 28, 2014"
+                }
             ],
+            "identifier": "VA-VHA-OIA-064",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2014-07-01T04:00:00Z/2014-07-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/access-audit.asp"
-            ],
             "keyword": [
                 "access",
                 "appointment",
@@ -60110,116 +60122,86 @@
                 "wait list",
                 "wait time"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/mz5y-gbsy",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-064",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Completed Appointments- Report 2014 August 28",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/VAMC_Patient_Access_Data_20140828_completed.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "August 28, 2014"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2014-07-01T04:00:00Z/2014-07-31T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Completed Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Completed Appointments- Report 2014 August 28"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://benefits.va.gov/BENEFITS/Benefits_Summary_Materials.asp",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2012-10-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
-            "keyword": [
-                "benefits summary",
-                "va benefits",
-                "va benefits summary"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-MEDIAPUB-061",
+            "dataQuality": true,
             "description": "<p>Summary of VA Benefits</p>",
-            "title": "Summary of VA Benefits",
+            "identifier": "VA-VBA-MEDIAPUB-061",
             "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits summary",
+                "va benefits",
+                "va benefits summary"
+            ],
+            "landingPage": "https://benefits.va.gov/BENEFITS/Benefits_Summary_Materials.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-08",
             "programCode": [
                 "029:003"
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2012-10-01T04:00:00Z/2012-10-01T04:00:00Z",
             "theme": [
                 "VA Benefits Summary"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Summary of VA Benefits"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mzhw-i2y6",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/vetdata/docs/Datagov/DataGov_GDX_FY08_Technical_Notes.doc"
-            ],
-            "keyword": [
-                "expenditure",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dorothy Glasgow",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-006",
-            "description": "<p>The Geographic Distribution of VA Expenditures (GDX)  is an annual report that shows estimated VA expenditures for major programmatic areas by geographic area (state, county, and congressional district). The major programmatic areas are: Compensation and Pension; Readjustment (Education) and Vocational Rehabilitation; Insurance; Construction; and, Medical and Administrative.</p>",
-            "title": "Veterans Affairs Geographic Distribution of Expenditures FY08 by State and County",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/vetdata/docs/Datagov/DataGov_GDX_FY08_Technical_Notes.doc",
             "describedByType": "application/msword",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>The Geographic Distribution of VA Expenditures (GDX)  is an annual report that shows estimated VA expenditures for major programmatic areas by geographic area (state, county, and congressional district). The major programmatic areas are: Compensation and Pension; Readjustment (Education) and Vocational Rehabilitation; Insurance; Construction; and, Medical and Administrative.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60227,66 +60209,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mzhw-i2y6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mzhw-i2y6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mzhw-i2y6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/mzhw-i2y6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mzhw-i2y6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mzhw-i2y6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mzhw-i2y6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mzhw-i2y6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mzhw-i2y6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/vetdata/docs/Datagov/DataGov_GDX_FY08_Technical_Notes.doc",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-006",
+            "issued": "2017-07-26",
+            "keyword": [
+                "expenditure",
+                "veteran"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mzhw-i2y6",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/vetdata/docs/Datagov/DataGov_GDX_FY08_Technical_Notes.doc"
+            ],
+            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
             "theme": [
                 "Section 9. Federal Government Finances and Employment"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Affairs Geographic Distribution of Expenditures FY08 by State and County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/mzpi-6byh",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 028"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/mzpi-6byh",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to help servicepersons adjust to civilian life after separation from military service, assist in the recruitment and retention of highly qualified personnel in the active and reserve components in the Armed Forces by providing education benefits, and to provide educational opportunities to the dependents of certain service members and veterans. Individuals who entered active duty after September 10, 2001 may be eligible for the Post-9/11 GI Bill. Individuals can use the Post-9/11 GI Bill after serving 90 days on active duty (excluding entry level and skill training). Only periods of active duty under title 10 will be used to establish eligibility for the Post 9/11 GI Bill. A high school diploma or equivalency certificate is always required for eligibility. Individuals who are eligible for the Montgomery GI Bill \u2013 Active Duty (chapter 30), the Montgomery GI Bill \u2013 Selected Reserve (chapter 1606), or the Reserve Educational Assistance Program (REAP) will have to make an irrevocable election to relinquish eligibility under one of those benefit programs to establish eligibility under the Post-9/11 GI Bill. The dependent children of a person who died in the line of duty while serving as a member of the Armed Forces may be eligible to use benefits under the Fry Scholarship provision of the Post-9/11 GI Bill. The spouse and/or child(ren) of a veteran or service member may be eligible for the Post 9/11 GI Bill if the veteran or service member transfers entitlement to those dependents. Eligibility to transfer entitlement to dependents is determined by the Department of Defense. This is not a complete list of eligibility requirements. For more information on the latest changes to the Post-9/11 GI Bill go to the VA web-site.</p>",
-            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE DEC2018",
-            "isPartOf": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60294,61 +60278,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mzpi-6byh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mzpi-6byh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mzpi-6byh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/mzpi-6byh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mzpi-6byh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mzpi-6byh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/mzpi-6byh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/mzpi-6byh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/mzpi-6byh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/mzpi-6byh",
+            "isPartOf": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 028"
+            ],
+            "landingPage": "https://www.data.va.gov/d/mzpi-6byh",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE DEC2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/n2nb-y7f7",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "utah",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-131",
             "description": "<p>This is a summary of the programs and services provided by VA in Utah in fiscal year 2014.</p>",
-            "title": "State Summary:  Utah",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60357,45 +60340,46 @@
                     "title": "State Summary:  Utah"
                 }
             ],
+            "identifier": "VA-OEI-OEI-131",
+            "issued": "2017-07-26",
+            "keyword": [
+                "utah",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/n2nb-y7f7",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "State Summary:  Utah"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/finance/overpaymentsReport.asp",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2013-01-01T05:00:00Z/2013-03-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "improper payments",
-                "overpayments"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Katherine Palmer",
                 "hasEmail": "mailto:Katherine.Palmer@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-082",
+            "dataQuality": true,
             "description": "<p>FY 2013 Second Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2013 Second Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60404,45 +60388,43 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-082",
+            "issued": "2017-07-26",
+            "keyword": [
+                "improper payments",
+                "overpayments"
+            ],
+            "landingPage": "https://www.va.gov/finance/overpaymentsReport.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2013-01-01T05:00:00Z/2013-03-31T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2013 Second Quarter High-Dollar Overpayments Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/PIVPROJECT/Reports/HSPD_12_Reporting_VA_MAR_2014.pdf",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "march 2014",
-                "report",
-                "va"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rodney Emery",
                 "hasEmail": "mailto:Rodney.Emery@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OIT-OIT-050",
             "description": "<p>March reporting for HSPD.</p>",
-            "title": "HSPD Reporting March 2014",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60451,46 +60433,42 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OIT-OIT-050",
+            "issued": "2017-07-26",
+            "keyword": [
+                "march 2014",
+                "report",
+                "va"
+            ],
+            "landingPage": "https://www.va.gov/PIVPROJECT/Reports/HSPD_12_Reporting_VA_MAR_2014.pdf",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:080"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "HSPD Reporting March 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/n5pf-iu2p",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-03-16",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-05",
-            "keyword": [
-                "utilization",
-                "va benefits",
-                "va programs",
-                "va services",
-                "veteran benefits",
-                "veterans",
-                "veterans benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/n5pf-iu2p",
             "description": "Rate of Veteran use of VA programs and services by sex within each era of conflict in which they first served. Data underlying eighth figure of Part 1 of the FY 2021 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Rates of Use by Sex within Era of Initial Service, FY 2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60498,56 +60476,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/n5pf-iu2p/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/n5pf-iu2p/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/n5pf-iu2p/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/n5pf-iu2p/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/n5pf-iu2p/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/n5pf-iu2p/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/n5pf-iu2p/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/n5pf-iu2p/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/n5pf-iu2p/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/n5pf-iu2p",
+            "issued": "2022-03-16",
+            "keyword": [
+                "utilization",
+                "va benefits",
+                "va programs",
+                "va services",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/n5pf-iu2p",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-01-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Rates of Use by Sex within Era of Initial Service, FY 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/n6bf-picb",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "virginia"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DG&amp;A Mailgroup",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-218",
             "description": "<p>This summary describes the programs and services VA provided in Virginia in fiscal year 2015.</p>",
-            "title": "State Summary: Virginia FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60556,23 +60540,54 @@
                     "title": "Virginia"
                 }
             ],
+            "identifier": "VA-OEI-OEI-218",
+            "issued": "2017-07-26",
+            "keyword": [
+                "virginia"
+            ],
+            "landingPage": "https://www.data.va.gov/d/n6bf-picb",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "State Summary: Virginia FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "accrualPeriodicity": "R/P2W",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/access-audit.asp",
+            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR30_092015_Completed_Wait_Times_Desired_Date_by_Division_CDW_PDFReady.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Completed Appointments 31 Aug 2015"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-419",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2015-08-31T04:00:00Z/2015-08-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -60586,113 +60601,81 @@
                 "wait list",
                 "wait time"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-419",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Aug 31",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR30_092015_Completed_Wait_Times_Desired_Date_by_Division_CDW_PDFReady.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Completed Appointments 31 Aug 2015"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2015-08-31T04:00:00Z/2015-08-31T04:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Aug 31"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/pocketcard/index.asp",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NCVAS Mailbox",
+                "hasEmail": "mailto:vancvas@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>NCVAS Pocket Cards are a compilation of facts related to the count of Veterans receiving Department of Veterans Affairs (VA) benefits and health care utilization.</p>",
+            "identifier": "VA-OEI-OEI-228",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "pocket card",
                 "statistics",
                 "stats at a glance"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NCVAS Mailbox",
-                "hasEmail": "mailto:vancvas@va.gov"
-            },
+            "landingPage": "https://www.va.gov/vetdata/pocketcard/index.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-OEI-OEI-228",
-            "description": "<p>NCVAS Pocket Cards are a compilation of facts related to the count of Veterans receiving Department of Veterans Affairs (VA) benefits and health care utilization.</p>",
-            "title": "VA Benefits & Health Care Utilization FY16 (Q4)",
-            "programCode": [
-                "029:086"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
             "theme": [
                 "Veteran Benefits",
                 "Veteran Utilization",
                 "Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Benefits & Health Care Utilization FY16 (Q4)"
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.va.gov/budget/report/",
-            "bureauCode": [
-                "029:00"
-            ],
-            "issued": "2017-07-26",
-            "temporal": "2010-01-01T05:00:00Z/2010-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "accountability",
-                "performance",
-                "report"
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "029:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Zlowe",
                 "hasEmail": "mailto:David.Zlowe@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-004",
+            "dataQuality": true,
             "description": "<p>2010 VA Performance and Accountability Report.</p>",
-            "title": "2010 VA Performance and Accountability Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60701,43 +60684,46 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-004",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accountability",
+                "performance",
+                "report"
+            ],
+            "landingPage": "https://www.va.gov/budget/report/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2010-01-01T05:00:00Z/2010-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2010 VA Performance and Accountability Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/n7av-4xmt",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2018-03-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-19",
-            "keyword": [
-                "equitable relief report"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sharon Weiner",
                 "hasEmail": "mailto:Sharon.Weiner@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "dataQuality": true,
             "description": "<p>Equitable Relief Reports as submitted to Congress</p>",
-            "title": "Equitable Relief Reports 2010",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60745,51 +60731,45 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "issued": "2018-03-19",
+            "keyword": [
+                "equitable relief report"
+            ],
+            "landingPage": "https://www.data.va.gov/d/n7av-4xmt",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-11-19",
+            "programCode": [
+                "029:083"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Equitable Relief Reports 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "fy2012 benefits",
-                "fy2012 vba",
-                "vba",
-                "vba benefits",
-                "vba benefits by state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-129",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Wisconsin-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60797,25 +60777,79 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-129",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy2012 benefits",
+                "fy2012 vba",
+                "vba",
+                "vba benefits",
+                "vba benefits by state"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR 2012"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Wisconsin-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/n849-uby9",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Mike Schwaber",
+                "hasEmail": "mailto:vancvas@va.gov"
+            },
+            "dataQuality": true,
+            "description": "This table provides state-level estimates of the percentage of Veterans who were VA pension recipients at the end of the fiscal years 2019, 2020, 2021, and 2023.  Percents are rounded to the nearest tenth.  Percents for fiscal year (FY) 2022 are not available by state.\n\nPrepared by the National Center for Veterans Analysis and Statistics.\n\nSources: Department of Veterans Affairs, Office of Enterprise Integration, Veteran Population Projection Model (VetPop) 2020, Veteran Object FY 2023 data, United States Veterans Eligibility Trends & Statistics (USVETS) 2019, 2020, and 2021 data; Veterans Benefits Administration, VETSNET FY 2019, FY 2020, FY 2021, and FY 2023 pension data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/api/views/n849-uby9/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://www.data.va.gov/api/views/n849-uby9/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://www.data.va.gov/api/views/n849-uby9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://www.data.va.gov/api/views/n849-uby9/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://www.data.va.gov/api/views/n849-uby9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://www.data.va.gov/api/views/n849-uby9/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://www.data.va.gov/api/views/n849-uby9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/n849-uby9",
             "issued": "2024-09-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-18",
             "keyword": [
                 "fy19",
                 "fy 19",
@@ -60840,85 +60874,35 @@
                 "state level",
                 "state-level"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Mike Schwaber",
-                "hasEmail": "mailto:vancvas@va.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/n849-uby9",
-            "description": "This table provides state-level estimates of the percentage of Veterans who were VA pension recipients at the end of the fiscal years 2019, 2020, 2021, and 2023.  Percents are rounded to the nearest tenth.  Percents for fiscal year (FY) 2022 are not available by state.\n\nPrepared by the National Center for Veterans Analysis and Statistics.\n\nSources: Department of Veterans Affairs, Office of Enterprise Integration, Veteran Population Projection Model (VetPop) 2020, Veteran Object FY 2023 data, United States Veterans Eligibility Trends & Statistics (USVETS) 2019, 2020, and 2021 data; Veterans Benefits Administration, VETSNET FY 2019, FY 2020, FY 2021, and FY 2023 pension data.",
-            "title": "VA Pension Recipients as a Percentage of Veteran Population by State for Fiscal Years: 2019, 2020, 2021, and 2023",
+            "landingPage": "https://www.data.va.gov/d/n849-uby9",
+            "language": [
+                "English"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-09-18",
             "programCode": [
                 "029:009"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/api/views/n849-uby9/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/n849-uby9/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://www.data.va.gov/api/views/n849-uby9/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/n849-uby9/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://www.data.va.gov/api/views/n849-uby9/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/n849-uby9/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://www.data.va.gov/api/views/n849-uby9/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
-            "language": [
-                "English"
-            ]
+            "title": "VA Pension Recipients as a Percentage of Veteran Population by State for Fiscal Years: 2019, 2020, 2021, and 2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/finance/overpaymentsReport.asp",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-04-01T04:00:00Z/2012-06-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "improper payments",
-                "overpayments"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Katherine Palmer",
                 "hasEmail": "mailto:Katherine.Palmer@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-087",
+            "dataQuality": true,
             "description": "<p>FY 2012 Third Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2012 Third Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60927,55 +60911,47 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-087",
+            "issued": "2017-07-26",
+            "keyword": [
+                "improper payments",
+                "overpayments"
+            ],
+            "landingPage": "https://www.va.gov/finance/overpaymentsReport.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2012-04-01T04:00:00Z/2012-06-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2012 Third Quarter High-Dollar Overpayments Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/naqj-txnn",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf"
-            ],
-            "keyword": [
-                "health",
-                "healthcare",
-                "hospital accreditation",
-                "patient safety",
-                "quality of care",
-                "satisfaction",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Open Data",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VHA-OIA-033",
-            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset represents the quality of care for defined populations: Gender, Geriatric, Disabled, Homeless, and patients with Mental Health Diagnosis.</p>",
-            "title": "Veterans Health Administration 2008 Hospital Report Card - Quality of Care - Populations",
-            "isPartOf": "VA-VHA-OIA-583",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:040"
-            ],
+            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset represents the quality of care for defined populations: Gender, Geriatric, Disabled, Homeless, and patients with Mental Health Diagnosis.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60983,67 +60959,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/naqj-txnn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/naqj-txnn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/naqj-txnn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/naqj-txnn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/naqj-txnn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/naqj-txnn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/naqj-txnn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/naqj-txnn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/naqj-txnn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-033",
+            "isPartOf": "VA-VHA-OIA-583",
+            "issued": "2017-07-26",
+            "keyword": [
+                "health",
+                "healthcare",
+                "hospital accreditation",
+                "patient safety",
+                "quality of care",
+                "satisfaction",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/naqj-txnn",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:040"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf"
+            ],
+            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
             "theme": [
                 "Section 3. Health and Nutrition"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Health Administration 2008 Hospital Report Card - Quality of Care - Populations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/nb65-6n4e",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "ogc",
-                "opinion",
-                "sah"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OGC Law Library",
                 "hasEmail": "mailto:OGCLawLibrary@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OGC-051",
             "description": "<p>Opinion on Reimbursing Veterans under the SAH Program</p>",
-            "title": "OGC Precedent Opinion 1-2008",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61052,46 +61034,44 @@
                     "title": "OGC Precedent Opinion 1-2008"
                 }
             ],
+            "identifier": "VA-OGC-051",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion",
+                "sah"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nb65-6n4e",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:083"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "OGC Precedent Opinion 1-2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "fy2012 benefits",
-                "fy2012 vba",
-                "vba",
-                "vba benefits",
-                "vba benefits by state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-079",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Arizona-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61099,44 +61079,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-079",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy2012 benefits",
+                "fy2012 vba",
+                "vba",
+                "vba benefits",
+                "vba benefits by state"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR 2012"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Arizona-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/nbeg-dzgp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-09",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "b5e5490c-6398-48d3-84de-53eceaed9a3f",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Alaska FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61144,78 +61128,76 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "b5e5490c-6398-48d3-84de-53eceaed9a3f",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nbeg-dzgp",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data",
                 "Demographics",
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "State Summary Alaska FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/nck8-4kvv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
-            "keyword": [
-                "cfda 64 032"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "b2a0a5f0-3d2f-490f-8b42-3eb1db21b8e0",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to encourage membership in units of the Selected Reserve of the Ready Reserve and to provide educational assistance to members of the reserve components called or ordered to active service in response to a war or national emergency declared by the President or Congress. Generally, to qualify for benefits under MGIB-SR you must (1) Have a six-year obligation to serve in the Selected Reserve signed after June 30, 1985. If you are an officer, you must have agreed to serve six years in addition to your original obligation. For some types of training, it is necessary to have a six-year commitment that begins after September 30, 1990; (2) Complete your initial active duty for training (IADT); (3) Meet the requirement to receive a high school diploma or equivalency certificate before completing IADT. You may not use 12 hours toward a college degree to meet this requirement; and (4) Remain in good standing while serving in an active Selected Reserve unit. Generally, to qualify for benefits under REAP you must have served at least 90 consecutive days on active duty as a result of a call or order to active duty from a reserve component in response to a war or national emergency declared by the President or Congress. This is not a complete list of eligibility requirements. For more information on MGIB-SR and REAP visit <a href=\"http://www.gibill.va.gov\">http://www.gibill.va.gov</a>.</p>",
-            "title": "USA SPENDING EDUCATION CH1606 & CH1607 B032 MONTGOMERY GI BILL SELECTED RESERVE; RESERVE EDUCATIONAL ASSISTANCE PROGRAM FY2019",
+            "identifier": "b2a0a5f0-3d2f-490f-8b42-3eb1db21b8e0",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 032"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nck8-4kvv",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
             "programCode": [
                 "029:003"
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING EDUCATION CH1606 & CH1607 B032 MONTGOMERY GI BILL SELECTED RESERVE; RESERVE EDUCATIONAL ASSISTANCE PROGRAM FY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ndt4-jm95",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-02-18",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-23",
-            "keyword": [
-                "health care",
-                "veteran",
-                "veteran benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Florinda Balfour",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/ndt4-jm95",
             "description": "Health Care: All Veterans who received either VA inpatient care, VA outpatient care, purchased (fee basis) care, VA long-term services and support, or VA pharmacy care were included. VA Health Care enrollees who did not seek care from VA during the current year were not included. Veterans who only sought care from a VHA Vet Center were not included. Veterans Health Administration (VHA) provides Health Care.",
-            "title": "Veterans who used VA Health Care",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61223,61 +61205,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ndt4-jm95/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ndt4-jm95/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ndt4-jm95/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ndt4-jm95/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ndt4-jm95/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ndt4-jm95/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ndt4-jm95/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ndt4-jm95/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ndt4-jm95/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "State",
-            "license": "https://www.usa.gov/government-works",
+            "identifier": "https://www.data.va.gov/api/views/ndt4-jm95",
+            "issued": "2021-02-18",
+            "keyword": [
+                "health care",
+                "veteran",
+                "veteran benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ndt4-jm95",
             "language": [
                 "English"
-            ]
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2021-03-23",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "spatial": "State",
+            "title": "Veterans who used VA Health Care"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ne4g-s4pf",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "9ff41542-88be-42b0-813d-81726e85e0ea",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Tennessee FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61285,43 +61269,43 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "9ff41542-88be-42b0-813d-81726e85e0ea",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ne4g-s4pf",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data",
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "State Summary Tennessee FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/nefm-insu",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-29",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "7513c09e-7cca-4d82-8a23-4e522caa668e",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Arkansas FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61329,43 +61313,43 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "7513c09e-7cca-4d82-8a23-4e522caa668e",
+            "issued": "2018-10-29",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nefm-insu",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data",
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "State Summary Arkansas FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/nepp-cgpc",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2018-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "storage"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Short",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "f65fef87-0fa6-4233-9ea9-426029c37544",
+            "dataQuality": true,
             "description": "<p>DAS stores structured and non-structured data from internal and external sources.</p>",
-            "title": "Storage",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61374,67 +61358,67 @@
                     "title": "Storage"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "f65fef87-0fa6-4233-9ea9-426029c37544",
+            "issued": "2018-02-23",
+            "keyword": [
+                "storage"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nepp-cgpc",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "Storage"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/nf27-qqfs",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-08",
-            "keyword": [
-                "texas",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:VANCVAS@VA.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/nf27-qqfs",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Texas",
+            "identifier": "https://www.data.va.gov/api/views/nf27-qqfs",
+            "issued": "2021-08-26",
+            "keyword": [
+                "texas",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nf27-qqfs",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-08-08",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_Texas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/nf49-jg6q",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-09",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "7c1305d2-e647-4d55-8994-33a8d423bd52",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Minnesota FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61442,20 +61426,39 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "7c1305d2-e647-4d55-8994-33a8d423bd52",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nf49-jg6q",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary Minnesota FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/nf89-pcxq",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Veterans Affairs Surgical Quality Improvement Program (VASQIP) database resides in the VA National Surgery Office (NSO) and is a quality assurance activity-derived database containing information on all patients who undergo surgery within the VA. The primary purpose of this database is to improve the quality of care for Veterans undergoing surgery by providing information to care provider teams for self-assessment and quality improvement purposes. Data for the VASQIP database are entered by nurse data managers using Veterans Health Information Systems and Technology Architecture (VistA) at the VA surgical facilities. These data captured in VistA are securely transmitted to the VASQIP database for compilation and analysis. Results of the data analysis are reported from the National Surgery Office (NSO) for quarterly and annual review of surgical quality and patient care issues; these data are confidential and privileged under the provisions of 38 U.S.C. 5705 and its implementing regulations. Note: In 2009, the Cardiac Specialty program (Continuous Improvement in Cardiac Surgery Program (CICSP)) was merged with the National Surgical Quality Improvement Program (NSQIP) for a comprehensive all-specialty surgical database, VASQIP.  It employs both Microsoft SQL Server and Statistical Analysis Software implementation.</p>",
+            "identifier": "VA-VHA-SS-002",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1987-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "38 usc",
                 "38 u s c",
@@ -61471,65 +61474,42 @@
                 "vasqip",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/nf89-pcxq",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-SS-002",
-            "description": "<p>The Veterans Affairs Surgical Quality Improvement Program (VASQIP) database resides in the VA National Surgery Office (NSO) and is a quality assurance activity-derived database containing information on all patients who undergo surgery within the VA. The primary purpose of this database is to improve the quality of care for Veterans undergoing surgery by providing information to care provider teams for self-assessment and quality improvement purposes. Data for the VASQIP database are entered by nurse data managers using Veterans Health Information Systems and Technology Architecture (VistA) at the VA surgical facilities. These data captured in VistA are securely transmitted to the VASQIP database for compilation and analysis. Results of the data analysis are reported from the National Surgery Office (NSO) for quarterly and annual review of surgical quality and patient care issues; these data are confidential and privileged under the provisions of 38 U.S.C. 5705 and its implementing regulations. Note: In 2009, the Cardiac Specialty program (Continuous Improvement in Cardiac Surgery Program (CICSP)) was merged with the National Surgical Quality Improvement Program (NSQIP) for a comprehensive all-specialty surgical database, VASQIP.  It employs both Microsoft SQL Server and Statistical Analysis Software implementation.</p>",
-            "title": "Veterans Affairs Surgical Quality Improvement Program (VASQIP)",
-            "programCode": [
-                "029:040"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "1987-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Affairs Surgical Quality Improvement Program (VASQIP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Datagov_FY10_EDU_recp_by_State.csv",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.vba.va.gov/REPORTS/abr/index.asp"
-            ],
-            "keyword": [
-                "education",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Salminio Garner",
                 "hasEmail": "mailto:salminio.garner1@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-EDU2010-001",
+            "dataQuality": true,
             "description": "<p>FY 10 Education Recipients by State. The data represents the number of individuals by VA education program who have used their VA education benefit during fiscal year 2010. State statistics may include individuals who used their education benefits in more than one state, therefore the total within this table may be different than the  total number of beneficiaries during the fiscal year.</p>",
-            "title": "FY 10 Education Recipients by State",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61537,83 +61517,107 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nf9u-grm7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nf9u-grm7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nf9u-grm7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/nf9u-grm7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nf9u-grm7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nf9u-grm7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nf9u-grm7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nf9u-grm7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nf9u-grm7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-EDU2010-001",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "education",
+                "veteran"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Datagov_FY10_EDU_recp_by_State.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.vba.va.gov/REPORTS/abr/index.asp"
+            ],
+            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
             "theme": [
                 "Section 4. Education"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 10 Education Recipients by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/nfw5-by69",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
-            "keyword": [
-                "cfda 64 127"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "faff9e4c-e7ad-440d-bd48-6843c4358f8a",
+            "dataQuality": true,
             "description": "<p>VBA COMPENSTATION BENEFITS PRGOGRAM to provide vocational training and rehabilitation to certain children born with spina bifida or other covered birth defects who are children of Vietnam veterans and some Korean veterans. \u201cA child born with spina bifida or other covered birth defects, except spina bifida occulta, who is the natural child of a Vietnam veteran and some Korean veterans, regardless of the age or marital status of the child, conceived after the date on which the veteran first served in the Republic of Vietnam during the Vietnam era and in particular areas near the DMZ in the Korean conflict. VA must also determine that it is feasible for the child to achieve a vocational goal.\u201d</p>",
-            "title": "USA SPENDING COMPENSATION CH18 B127 ALLOWANCE FOR CHILDREN OF VIETNAM VETERANS BORN WITH SPINA BIFIDA FY2019",
+            "identifier": "faff9e4c-e7ad-440d-bd48-6843c4358f8a",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 127"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nfw5-by69",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
             "programCode": [
                 "029:003"
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING COMPENSATION CH18 B127 ALLOWANCE FOR CHILDREN OF VIETNAM VETERANS BORN WITH SPINA BIFIDA FY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/HospitalReportCard.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
+            "describedByType": "application/pdf",
+            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset defines the scope of services provided at a facility.</p>",
+            "identifier": "VA-VHA-OIA-583",
             "issued": "2017-07-26",
-            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
-            "references": [
-                "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf"
-            ],
             "keyword": [
                 "health",
                 "healthcare",
@@ -61623,62 +61627,42 @@
                 "satisfaction",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.va.gov/health/HospitalReportCard.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-583",
-            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset defines the scope of services provided at a facility.</p>",
-            "title": "Veterans Health Administration 2008 Hospital Report Card",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "029:040"
+            "references": [
+                "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf"
             ],
-            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
             "theme": [
                 "Hospital Report Card"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Health Administration 2008 Hospital Report Card"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/budget/docs/summary/archive/FY-2015_VA-BudgetSubmission.zip",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2015-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "budget",
-                "fy2015"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OM Open Data",
                 "hasEmail": "mailto:VAOMOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-097",
+            "dataQuality": true,
             "description": "<p>FY 2015 Budget Submission Volume I: Summary</p>",
-            "title": "FY 2015 Budget Submission Volume I",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61687,45 +61671,45 @@
                     "title": "FY 2015 VA Budget Submission"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-097",
+            "issued": "2017-07-26",
+            "keyword": [
+                "budget",
+                "fy2015"
+            ],
+            "landingPage": "https://www.va.gov/budget/docs/summary/archive/FY-2015_VA-BudgetSubmission.zip",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-10",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-10-01T04:00:00Z/2015-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2015 Budget Submission Volume I"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/pocketcard/index.asp",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "pocket card",
-                "statistics",
-                "stats at a glance"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS Mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-227",
+            "dataQuality": true,
             "description": "<p>NCVAS Pocket Cards are a compilation of facts related to the count of Veterans receiving Department of Veterans Affairs (VA) benefits and health care utilization.</p>",
-            "title": "VA Benefits & Health Care Utilization FY16 (Q3)",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61734,47 +61718,45 @@
                     "title": "Pocket Card \u2013 FY16 (Q3)"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-227",
+            "issued": "2017-07-26",
+            "keyword": [
+                "pocket card",
+                "statistics",
+                "stats at a glance"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/pocketcard/index.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Veteran Benefits",
                 "Veteran Utilization",
                 "Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Benefits & Health Care Utilization FY16 (Q3)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/nhmj-k6j5",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2023-04-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-19",
-            "keyword": [
-                "death rate",
-                "life expectancy",
-                "life table"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/nhmj-k6j5",
             "description": "",
-            "title": "Table 8 - U. S. Veterans Life Table for Female 2010-2019",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61782,40 +61764,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nhmj-k6j5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nhmj-k6j5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nhmj-k6j5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/nhmj-k6j5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nhmj-k6j5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nhmj-k6j5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nhmj-k6j5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nhmj-k6j5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nhmj-k6j5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/nhmj-k6j5",
+            "issued": "2023-04-18",
+            "keyword": [
+                "death rate",
+                "life expectancy",
+                "life table"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nhmj-k6j5",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-04-19",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Table 8 - U. S. Veterans Life Table for Female 2010-2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/nhsm-uahe",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>As the number of Operation Enduring Freedom/Operation Iraqi Freedom (OEF/OIF) Traumatic Brain Injury (TBI) patients has grown, so has the need to track and monitor care to meet the lifelong needs of these veterans.  In March 2007, a Computerized Patient Record System (CPRS) OIF/OEF TBI Screening Reminder was released.  This is a first-line screening tool to identify potential TBI patients.  Additional information about veterans who have been identified as possible TBI patients by the initial Screening Reminder is collected through a Comprehensive TBI evaluation.  Reminder results, in the form of Health Factors, Comprehensive TBI evaluation data, and Comprehensive TBI Follow-up results of individual Veterans will be sent to a national database.  This data will be aggregated in order to provide relevant responses to key stakeholders, such as members of Congress, to monitor the quality of care and to implement system improvements. In addition, tracking applications will be used to collect data on TBI patient appointments.</p>",
+            "identifier": "VA-VHA-PCS-013",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2005-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "brain",
                 "enduring",
@@ -61831,61 +61834,42 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/nhsm-uahe",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-PCS-013",
-            "description": "<p>As the number of Operation Enduring Freedom/Operation Iraqi Freedom (OEF/OIF) Traumatic Brain Injury (TBI) patients has grown, so has the need to track and monitor care to meet the lifelong needs of these veterans.  In March 2007, a Computerized Patient Record System (CPRS) OIF/OEF TBI Screening Reminder was released.  This is a first-line screening tool to identify potential TBI patients.  Additional information about veterans who have been identified as possible TBI patients by the initial Screening Reminder is collected through a Comprehensive TBI evaluation.  Reminder results, in the form of Health Factors, Comprehensive TBI evaluation data, and Comprehensive TBI Follow-up results of individual Veterans will be sent to a national database.  This data will be aggregated in order to provide relevant responses to key stakeholders, such as members of Congress, to monitor the quality of care and to implement system improvements. In addition, tracking applications will be used to collect data on TBI patient appointments.</p>",
-            "title": "Traumatic Brain Injury Registry (TBI)",
-            "programCode": [
-                "029:040"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2005-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Traumatic Brain Injury Registry (TBI)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/niep-ta4w",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 127"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/niep-ta4w",
+            "dataQuality": true,
             "description": "<p>VBA COMPENSTATION BENEFITS PRGOGRAM to provide vocational training and rehabilitation to certain children born with spina bifida or other covered birth defects who are children of Vietnam veterans and some Korean veterans. \u201cA child born with spina bifida or other covered birth defects, except spina bifida occulta, who is the natural child of a Vietnam veteran and some Korean veterans, regardless of the age or marital status of the child, conceived after the date on which the veteran first served in the Republic of Vietnam during the Vietnam era and in particular areas near the DMZ in the Korean conflict. VA must also determine that it is feasible for the child to achieve a vocational goal.\u201d</p>",
-            "title": "USA SPENDING COMPENSATION CH18 B127 ALLOWANCE FOR CHILDREN OF VIETNAM VETERANS BORN WITH SPINA BIFIDA MAR2019",
-            "isPartOf": "faff9e4c-e7ad-440d-bd48-6843c4358f8a",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61893,61 +61877,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/niep-ta4w/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/niep-ta4w/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/niep-ta4w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/niep-ta4w/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/niep-ta4w/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/niep-ta4w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/niep-ta4w/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/niep-ta4w/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/niep-ta4w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/niep-ta4w",
+            "isPartOf": "faff9e4c-e7ad-440d-bd48-6843c4358f8a",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 127"
+            ],
+            "landingPage": "https://www.data.va.gov/d/niep-ta4w",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING COMPENSATION CH18 B127 ALLOWANCE FOR CHILDREN OF VIETNAM VETERANS BORN WITH SPINA BIFIDA MAR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/nigq-qjpp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-07-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-10",
-            "keyword": [
-                "veterans",
-                "women veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/nigq-qjpp",
             "description": "",
-            "title": "Education Attainment of Veterans by Gender",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61955,62 +61938,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nigq-qjpp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nigq-qjpp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nigq-qjpp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/nigq-qjpp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nigq-qjpp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nigq-qjpp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nigq-qjpp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nigq-qjpp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nigq-qjpp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/nigq-qjpp",
+            "issued": "2024-07-29",
+            "keyword": [
+                "veterans",
+                "women veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nigq-qjpp",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-12-10",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Education Attainment of Veterans by Gender"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/nj5s-yrjs",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2006-10-01T04:00:00Z/2007-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/vetdata/docs/Datagov/DataGov_GDX_FY07_Technical_Notes.doc"
-            ],
-            "keyword": [
-                "expenditure",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dorothy Glasgow",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-003",
-            "description": "<p>The Geographic Distribution of VA Expenditures (GDX)  is an annual report that shows estimated VA expenditures for major programmatic areas by geographic area (state, county, and congressional district). The major programmatic areas are: Compensation and Pension; Readjustment (Education) and Vocational Rehabilitation; Insurance; Construction; and, Medical and Administrative.</p>",
-            "title": "Veterans Affairs Geographic Distribution of Expenditures FY07 by Congressional District",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/vetdata/docs/Datagov/DataGov_GDX_FY07_Technical_Notes.doc",
             "describedByType": "application/msword",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>The Geographic Distribution of VA Expenditures (GDX)  is an annual report that shows estimated VA expenditures for major programmatic areas by geographic area (state, county, and congressional district). The major programmatic areas are: Compensation and Pension; Readjustment (Education) and Vocational Rehabilitation; Insurance; Construction; and, Medical and Administrative.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62018,67 +62000,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nj5s-yrjs/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nj5s-yrjs/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nj5s-yrjs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/nj5s-yrjs/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nj5s-yrjs/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nj5s-yrjs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nj5s-yrjs/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nj5s-yrjs/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nj5s-yrjs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/vetdata/docs/Datagov/DataGov_GDX_FY07_Technical_Notes.doc",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-003",
+            "issued": "2017-07-26",
+            "keyword": [
+                "expenditure",
+                "veteran"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nj5s-yrjs",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/vetdata/docs/Datagov/DataGov_GDX_FY07_Technical_Notes.doc"
+            ],
+            "temporal": "2006-10-01T04:00:00Z/2007-09-30T04:00:00Z",
             "theme": [
                 "Section 9. Federal Government Finances and Employment"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Affairs Geographic Distribution of Expenditures FY07 by Congressional District"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/njqs-5cnj",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 105",
-                "cfda 64 110"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/njqs-5cnj",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA's determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING C&P B110 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE OCT2018",
-            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62086,66 +62069,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/njqs-5cnj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/njqs-5cnj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/njqs-5cnj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/njqs-5cnj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/njqs-5cnj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/njqs-5cnj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/njqs-5cnj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/njqs-5cnj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/njqs-5cnj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/njqs-5cnj",
+            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 105",
+                "cfda 64 110"
+            ],
+            "landingPage": "https://www.data.va.gov/d/njqs-5cnj",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING C&P B110 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE OCT2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "abr",
-                "abr2012",
-                "compensation benefits fy12",
-                "dic benefits",
-                "vba benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-010",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Combined Degree of Service Connected Disabilities for Veterans Who Began Receiving Compensation by FY",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62153,44 +62133,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-010",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "abr",
+                "abr2012",
+                "compensation benefits fy12",
+                "dic benefits",
+                "vba benefits"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR Reports"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Combined Degree of Service Connected Disabilities for Veterans Who Began Receiving Compensation by FY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/nm78-5xkx",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "south carolina",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-127",
             "description": "<p>This is a summary of the programs and services provided by VA in South Carolina in fiscal year 2014.</p>",
-            "title": "State Summary:  South Carolina",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62199,44 +62182,45 @@
                     "title": "State Summary:  South Carolina"
                 }
             ],
+            "identifier": "VA-OEI-OEI-127",
+            "issued": "2017-07-26",
+            "keyword": [
+                "south carolina",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nm78-5xkx",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "State Summary:  South Carolina"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/nmjq-tbdw",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "086b2c88-de12-4548-a526-499903096a5f",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary North Carolina FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62244,39 +62228,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "086b2c88-de12-4548-a526-499903096a5f",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nmjq-tbdw",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary North Carolina FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.oprm.va.gov/privacy/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "pia",
-                "privacy impact assessment",
-                "va"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rita Grewal",
                 "hasEmail": "mailto:Rita.Grewal@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OIT-ITIS-22",
+            "dataQuality": true,
             "description": "<p>This repository contains Privacy Impact Assessments (PIA) that have been vetted/approved. Section 208 of the Electronic Government Act of 2002 (E-Gov Act) requires federal agencies to conduct a Privacy Impact Assessment (PIA) on information technology systems that either (1) collect, maintain, and/or disseminate Personally Identifiable Information (PII); or (2) make substantial changes to existing technology that manages PII.. A PIA is an analysis of how PII is collected, stored, protected, shared, and managed. Its purpose is to demonstrate that the information system owners and/or developers have incorporated privacy protections throughout the lifecycle of the system. Absent a legitimate security or sensitivity concern demonstrated by the agency, the E-Gov Act requires agencies to make PIAs publicly available.The Department of Veterans Affairs (VA) Office of Privacy, FOIA, and Records Management strive to be the leader among Federal Information Technology (IT) organizations in protecting the privacy of Veterans' personal data. Our goal is to respond to mandates to meet the needs of Veterans, while improving the protection of their personal information.To view a PIA for a particular system, go to the heading labeled 'System Operating with a Current/Valid FY2013 PIA' and select the name of the program/project of interest.</p>",
-            "title": "Privacy Impact Assessment (PIA) Repository",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62285,47 +62268,48 @@
                     "title": "html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OIT-ITIS-22",
+            "issued": "2017-07-26",
+            "keyword": [
+                "pia",
+                "privacy impact assessment",
+                "va"
+            ],
+            "landingPage": "https://www.oprm.va.gov/privacy/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:080"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Privacy Impact Assessment (PIA) Repository"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/pocketcard/index.asp",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "pocket card",
-                "statistics",
-                "stats at a glance"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS Mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-226",
+            "dataQuality": true,
             "description": "<p>NCVAS Pocket Cards are a compilation of facts related to the count of Veterans receiving Department of Veterans Affairs (VA) benefits and health care utilization.</p>",
-            "title": "VA Benefits & Health Care Utilization FY16 (Q2)",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62334,48 +62318,47 @@
                     "title": "Pocket Card \u2013 FY16 (Q2)"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-226",
+            "issued": "2017-07-26",
+            "keyword": [
+                "pocket card",
+                "statistics",
+                "stats at a glance"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/pocketcard/index.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Veteran Benefits",
                 "Veteran Utilization",
                 "Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Benefits & Health Care Utilization FY16 (Q2)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/npcj-egem",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "issued": "2023-10-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-11",
-            "keyword": [
-                "ncptsd",
-                "ptsd",
-                "study characteristics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for PTSD",
                 "hasEmail": "mailto:ncptsd@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for PTSD"
-            },
-            "identifier": "https://www.data.va.gov/api/views/npcj-egem",
+            "dataQuality": true,
             "description": "The Study Characteristics dataset includes basic information about study design. In addition to study class, the dataset includes clinical setting, whether the study looked at PTSD symptom clusters, whether there were any subgroup analyses, type of diagnostic measure used (e.g., diagnostic interview, self-report), and provider credentials. Use this dataset to better understand the variety of RCT designs employed, compare studies by study class or to identify gaps in the literature for potential new RCTs. Visualizations made from this dataset will be based on the 550 RCTs included in the PTSD-Repository. Values reported as \"NA\" or not reported \"NR\" by the study are null values (empty cells). Data is at the study level.",
-            "title": "Study Characteristics",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62383,116 +62366,115 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/npcj-egem/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/npcj-egem/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/npcj-egem/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/npcj-egem/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/npcj-egem/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/npcj-egem/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/npcj-egem/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/npcj-egem/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/npcj-egem/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/npcj-egem",
+            "issued": "2023-10-31",
+            "keyword": [
+                "ncptsd",
+                "ptsd",
+                "study characteristics"
+            ],
+            "landingPage": "https://www.data.va.gov/d/npcj-egem",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-06-11",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for PTSD"
+            },
+            "rights": "All data is within the public domain and is currently available for download.",
             "theme": [
                 "PTSD-Repository"
-            ]
+            ],
+            "title": "Study Characteristics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/pocketcard/index.asp",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NCVAS Mailbox",
+                "hasEmail": "mailto:vancvas@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>NCVAS Pocket Cards are a compilation of facts related to the count of Veterans receiving Department of Veterans Affairs (VA) benefits and health care utilization.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/vetdata/docs/pocketcards/fy2017q2.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pocket Card \u2013 FY17 (Q2)"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-230",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "pocket card",
                 "statistics",
                 "stats at a glance"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NCVAS Mailbox",
-                "hasEmail": "mailto:vancvas@va.gov"
-            },
+            "landingPage": "https://www.va.gov/vetdata/pocketcard/index.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-OEI-OEI-230",
-            "description": "<p>NCVAS Pocket Cards are a compilation of facts related to the count of Veterans receiving Department of Veterans Affairs (VA) benefits and health care utilization.</p>",
-            "title": "VA Benefits & Health Care Utilization FY17 (Q2)",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/vetdata/docs/pocketcards/fy2017q2.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pocket Card \u2013 FY17 (Q2)"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
             "theme": [
                 "Veteran Benefits",
                 "Veteran Utilization",
                 "Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Benefits & Health Care Utilization FY17 (Q2)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/nq4i-bn8i",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/vetdata/docs/Datagov/DataGov_GDX_FY08_Technical_Notes.doc"
-            ],
-            "keyword": [
-                "expenditure",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dorothy Glasgow",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-005",
-            "description": "<p>The Geographic Distribution of VA Expenditures (GDX)  is an annual report that shows estimated VA expenditures for major programmatic areas by geographic area (state, county, and congressional district). The major programmatic areas are: Compensation and Pension; Readjustment (Education) and Vocational Rehabilitation; Insurance; Construction; and, Medical and Administrative.</p>",
-            "title": "Veterans Affairs Geographic Distribution of Expenditures FY08 by Congressional District",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/vetdata/docs/Datagov/DataGov_GDX_FY08_Technical_Notes.doc",
             "describedByType": "application/msword",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>The Geographic Distribution of VA Expenditures (GDX)  is an annual report that shows estimated VA expenditures for major programmatic areas by geographic area (state, county, and congressional district). The major programmatic areas are: Compensation and Pension; Readjustment (Education) and Vocational Rehabilitation; Insurance; Construction; and, Medical and Administrative.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62500,66 +62482,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nq4i-bn8i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nq4i-bn8i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nq4i-bn8i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/nq4i-bn8i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nq4i-bn8i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nq4i-bn8i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nq4i-bn8i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nq4i-bn8i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nq4i-bn8i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/vetdata/docs/Datagov/DataGov_GDX_FY08_Technical_Notes.doc",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-005",
+            "issued": "2017-07-26",
+            "keyword": [
+                "expenditure",
+                "veteran"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nq4i-bn8i",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/vetdata/docs/Datagov/DataGov_GDX_FY08_Technical_Notes.doc"
+            ],
+            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
             "theme": [
                 "Section 9. Federal Government Finances and Employment"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Affairs Geographic Distribution of Expenditures FY08 by Congressional District"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/nq5n-cz76",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 109"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/nq5n-cz76",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to compensate veterans for disabilities incurred or aggravated during military service according to the average impairment in earning capacity such disability would cause in civilian occupations. Persons who have suffered disabilities resulting from service in the Armed Forces of the United States. The disability must have been incurred or aggravated by service in the line of duty. Separation from service must have been under other than dishonorable conditions for the period in which the disability was incurred or aggravated.</p>",
-            "title": "USA SPENDING C&P B109 VETERANS COMPENSATION FOR SERVICE-CONNECTED DISABILITY JAN2019",
-            "isPartOf": "6013cae5-a8c2-47ff-9c90-9cbdba7bda63",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62567,67 +62551,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nq5n-cz76/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nq5n-cz76/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nq5n-cz76/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/nq5n-cz76/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nq5n-cz76/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nq5n-cz76/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nq5n-cz76/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nq5n-cz76/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nq5n-cz76/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/nq5n-cz76",
+            "isPartOf": "6013cae5-a8c2-47ff-9c90-9cbdba7bda63",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 109"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nq5n-cz76",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING C&P B109 VETERANS COMPENSATION FOR SERVICE-CONNECTED DISABILITY JAN2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www1.va.gov/VETDATA/docs/Datagov/FY_07_Insurance_Expenditure_by_County_and_State.csv",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2007-01-01T05:00:00Z/2007-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www1.va.gov/VETDATA/docs/Datagov/FY_07_Insurance_Expenditure_by_County_and_State.csv"
-            ],
-            "keyword": [
-                "expenditure",
-                "insurance",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2007-002",
+            "dataQuality": true,
             "description": "<p>2007 Veteran life insurance expenditures by state and county.  Expenditures were derived from Insurance Actuarial reports that used the total Insurance program cash disbursed.  The total cash disbursed was prorated by in-force data by state, which was further prorated by county and congressional district.</p>",
-            "title": "2007 Veterans' Insurance Expenditure by State and County",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62635,64 +62614,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nqfw-uekq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nqfw-uekq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nqfw-uekq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/nqfw-uekq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nqfw-uekq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nqfw-uekq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nqfw-uekq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nqfw-uekq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nqfw-uekq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2007-002",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "expenditure",
+                "insurance",
+                "veteran"
+            ],
+            "landingPage": "https://www1.va.gov/VETDATA/docs/Datagov/FY_07_Insurance_Expenditure_by_County_and_State.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www1.va.gov/VETDATA/docs/Datagov/FY_07_Insurance_Expenditure_by_County_and_State.csv"
+            ],
+            "temporal": "2007-01-01T05:00:00Z/2007-12-31T05:00:00Z",
             "theme": [
                 "Section 9. Federal Government Finances and Employment"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2007 Veterans' Insurance Expenditure by State and County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/nrcc-ijez",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "accounts receivable"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vicki Soukup",
                 "hasEmail": "mailto:vicki.soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-160",
             "description": "<p>aged accounts receivable report; CARS Age Profile Report 9/30/2015</p>",
-            "title": "COIN 0017 - CARS Age Profile Report 9/30/2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62700,39 +62684,39 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-160",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accounts receivable"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nrcc-ijez",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Financial"
-            ]
+            ],
+            "title": "COIN 0017 - CARS Age Profile Report 9/30/2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/nsns-wxez",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "aca"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bret Meyer",
                 "hasEmail": "mailto:bret.meyer@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-ORCH-0",
+            "dataQuality": true,
             "description": "<p>CMS Enrollment definition - Enables a consumer to verify a veteran's ACA enrollment period</p>",
-            "title": "ACA Enrollment Status Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62741,43 +62725,41 @@
                     "title": "ACA Enrollment Status Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-ORCH-0",
+            "issued": "2017-11-17",
+            "keyword": [
+                "aca"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nsns-wxez",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "ACA Enrollment Status Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.osehra.org/blog/release-vista-evolution-program-plan-and-vista-4-product-roadmap",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2015-10-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "evolution",
-                "plan",
-                "program",
-                "vista"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tim Cox",
                 "hasEmail": "mailto:tim.cox@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OIT-ASD-005",
+            "dataQuality": true,
             "description": "<p>'The Department of Veterans Affairs (VA) and the Department of Defense (DoD) are working together to fundamentally and positively impact the health outcomes of Veterans, Service members, and their dependents. Achieving interoperability of health records between the two Departments is the chief goal motivating the Departments\u00ef\u00bf\u00bd electronic health record (EHR) efforts. Seamless integration of health data from VA, DoD, and other healthcare partners enables clinicians and patients to benefit from the availability of a complete longitudinal health record, achieving the goal of developing electronic records that will transition along with them from active-duty to retired status.The Departments are on complementary paths for modernizing their respective EHR systems, replacing or enhancing existing systems as required to support delivery of the best possible care in their particular environments. For its part, VA will enhance, or evolve, its Veterans Health Information Systems and Technology Architecture (VistA) EHR to achieve its interoperability, clinical, and technical objectives. This VistA Evolution Program Plan captures VA\u00ef\u00bf\u00bds structured approach to executing this mission.'</p>",
-            "title": "VistA Evolution Program Plan",
-            "programCode": [
-                "029:078"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62786,46 +62768,49 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OIT-ASD-005",
+            "issued": "2017-07-26",
+            "keyword": [
+                "evolution",
+                "plan",
+                "program",
+                "vista"
+            ],
+            "landingPage": "http://www.osehra.org/blog/release-vista-evolution-program-plan-and-vista-4-product-roadmap",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:078"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-10-01T04:00:00Z/2015-10-01T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VistA Evolution Program Plan"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/nt34-4qx9",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-20",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cdfa 64.124"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE D BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/nt34-4qx9",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE FEB2019",
-            "isPartOf": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62833,64 +62818,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nt34-4qx9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nt34-4qx9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nt34-4qx9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/nt34-4qx9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nt34-4qx9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nt34-4qx9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nt34-4qx9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nt34-4qx9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nt34-4qx9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/nt34-4qx9",
+            "isPartOf": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
+            "issued": "2019-03-20",
+            "keyword": [
+                "cdfa 64.124"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nt34-4qx9",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE FEB2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/pocketcard/index.asp",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2014-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "pocket card",
-                "statistics",
-                "stats at a glance"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Florinda Balfour",
                 "hasEmail": "mailto:florinda.balfour@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-054",
+            "dataQuality": true,
             "description": "<p>NCVAS Pocket Cards archives are a compilation of facts related to the count of Veterans receiving Department of Veterans Affairs (VA) benefits and health care utilization.</p>",
-            "title": "VA Benefits & Health Care Utilization",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62899,45 +62882,46 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-054",
+            "issued": "2017-07-26",
+            "keyword": [
+                "pocket card",
+                "statistics",
+                "stats at a glance"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/pocketcard/index.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-10-01T04:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Veterans Benefits",
                 "Veteran Utilization",
                 "Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Benefits & Health Care Utilization"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/nuf7-wjs4",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "debt referrals"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vicki Soukup",
                 "hasEmail": "mailto:vicki.soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-159",
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "COIN 146 September 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62945,23 +62929,52 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-159",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referrals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nuf7-wjs4",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 146 September 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/Expenditures.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Andrew Bickel",
+                "hasEmail": "mailto:andrew.bickel@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.va.gov/vetdata/docs/GDX/03geo97.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Geographic Distribution of VA Expenditures FY1997"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-023",
             "issued": "2017-07-26",
-            "temporal": "1996-10-01T04:00:00Z/1997-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -62975,69 +62988,37 @@
                 "insurance",
                 "medical care"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Andrew Bickel",
-                "hasEmail": "mailto:andrew.bickel@va.gov"
-            },
+            "landingPage": "https://www.va.gov/VETDATA/Expenditures.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-OEI-OEI-023",
-            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY1997",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.va.gov/vetdata/docs/GDX/03geo97.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Geographic Distribution of VA Expenditures FY1997"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "1996-10-01T04:00:00Z/1997-09-30T04:00:00Z",
             "theme": [
                 "Expenditures"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geographic Distribution of VA Expenditures FY1997"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/nuya-e38t",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2002-10-01T04:00:00Z/2003-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "annual report",
-                "cfo letter",
-                "franchise fund"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OM Open Data",
                 "hasEmail": "mailto:VAOMOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-109",
             "description": "<p>FY 2003 Franchise Fund Annual Report CFO Letter</p>",
-            "title": "FY 2003 Franchise Fund Annual Report CFO Letter",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63046,21 +63027,53 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OM-OM-109",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "cfo letter",
+                "franchise fund"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nuya-e38t",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-06-10",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2002-10-01T04:00:00Z/2003-09-30T04:00:00Z",
             "theme": [
                 "financial"
-            ]
+            ],
+            "title": "FY 2003 Franchise Fund Annual Report CFO Letter"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/nvef-6fb8",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.hsrd.research.va.gov/for_researchers/cyber_seminars/archives/video_archive.cfm?SessionID=1085",
+            "description": "<p>VA's TBI screening and evaluation program will be presented including historical development and progress, operational effectiveness, and research efforts to improve clinical care. Future enhancements to the program will be discussed as well as potential areas of further study. Intended audience: VHA Clinicians and Researchers, particularly those caring for Veterans with Traumatic Brain Injury. This dataset is no longer supported and is provided as-is. Any historical knowledge regarding meta data or it's creation is no longer available.  All known information is proved as part of this data set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/nvef-6fb8/text/plain",
+                    "mediaType": "text/plain"
+                }
+            ],
+            "identifier": "VA-VHA-PCS-019",
+            "isPartOf": "VA-VHA-PCS-020",
             "issued": "2017-07-26",
-            "temporal": "2013-10-01T04:00:00Z/2014-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-29",
             "keyword": [
                 "concussion",
                 "depression",
@@ -63071,103 +63084,68 @@
                 "veteran",
                 "vha"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/nvef-6fb8",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-06-29",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-PCS-019",
-            "description": "<p>VA's TBI screening and evaluation program will be presented including historical development and progress, operational effectiveness, and research efforts to improve clinical care. Future enhancements to the program will be discussed as well as potential areas of further study. Intended audience: VHA Clinicians and Researchers, particularly those caring for Veterans with Traumatic Brain Injury. This dataset is no longer supported and is provided as-is. Any historical knowledge regarding meta data or it's creation is no longer available.  All known information is proved as part of this data set.</p>",
-            "title": "Mild TBI Diagnosis and Management Strategies: VA's TBI Screening and Evaluation Program",
-            "isPartOf": "VA-VHA-PCS-020",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/nvef-6fb8/text/plain",
-                    "mediaType": "text/plain"
-                }
-            ],
-            "describedBy": "https://www.hsrd.research.va.gov/for_researchers/cyber_seminars/archives/video_archive.cfm?SessionID=1085",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2013-10-01T04:00:00Z/2014-09-30T04:00:00Z",
             "theme": [
                 "Mild TBI"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Mild TBI Diagnosis and Management Strategies: VA's TBI Screening and Evaluation Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/nvpe-e7iq",
-            "issued": "2019-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-04-23",
-            "keyword": [
-                "agriculture",
-                "veteran farmers"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA Open Data",
                 "hasEmail": "mailto:opendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/nvpe-e7iq",
             "description": "The Department of Veterans Affairs, Office of Enterprise Integration convened a collaborative event to encourage the development of innovative solutions to spark entrepreneurship and bring together the seemingly disparate worlds of software development, commercial farming, and Veterans.",
-            "title": "Apps for Ag Hackathon",
+            "identifier": "https://www.data.va.gov/api/views/nvpe-e7iq",
+            "issued": "2019-09-10",
+            "keyword": [
+                "agriculture",
+                "veteran farmers"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nvpe-e7iq",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-04-23",
             "programCode": [
                 "029:000"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Apps for Ag Hackathon"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/7_31_13_Enrollment_by_State.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2013-07-01T04:00:00Z/2013-07-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/7_31_13_Technical_Notes_Number_of_Veterans_Enrolled_in_VGLI_by_State.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "insurance",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:Dusca.Fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2013-002",
+            "dataQuality": true,
             "description": "<p>Provides the number of Veterans insured under the Veterans' Group Life Insurance (VGLI) program by state.  This report provides a snapshot of the active VGLI membership as of July 31, 2013.  For members who reside outside the United States, membership is not identified by individual country.  The total number of members was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "Number of Veterans Insured by VGLI by State as of July 31, 2013",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63175,65 +63153,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nvrx-cg2t/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nvrx-cg2t/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nvrx-cg2t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/nvrx-cg2t/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nvrx-cg2t/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nvrx-cg2t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nvrx-cg2t/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nvrx-cg2t/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nvrx-cg2t/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2013-002",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/7_31_13_Enrollment_by_State.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/7_31_13_Technical_Notes_Number_of_Veterans_Enrolled_in_VGLI_by_State.doc"
+            ],
+            "temporal": "2013-07-01T04:00:00Z/2013-07-31T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Number of Veterans Insured by VGLI by State as of July 31, 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/nwrz-6r6n",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2018-03-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-19",
-            "keyword": [
-                "equitable relief report"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sharon Weiner",
                 "hasEmail": "mailto:Sharon.Weiner@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "dataQuality": true,
             "description": "<p>Equitable Relief Reports as submitted to Congress</p>",
-            "title": "Equitable Relief Reports 2013",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63241,94 +63227,87 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "issued": "2018-03-19",
+            "keyword": [
+                "equitable relief report"
+            ],
+            "landingPage": "https://www.data.va.gov/d/nwrz-6r6n",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-11-19",
+            "programCode": [
+                "029:083"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Equitable Relief Reports 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Monica Reyes",
+                "hasEmail": "mailto:monica.reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Veterans Dependency and indemnity Compensation for Service-Connected Death-- December 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING122013-008",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 105",
                 "compensation and pension",
                 "dependency and indemnity compensation for service connected death",
                 "usa spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:monica.reyes@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING122013-008",
-            "description": "<p>USA Spending- Veterans Dependency and indemnity Compensation for Service-Connected Death-- December 2013.</p>",
-            "title": "USA Spending file- Veterans Dependency and indemnity Compensation for Service-Connected Death-  CFDA 64.110",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- Veterans Dependency and indemnity Compensation for Service-Connected Death-  CFDA 64.110"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/TSGLI_Claimants_and_Payments_by_Type_of_Loss.csv",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-05-01T04:00:00Z/2011-05-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_TSGLI_Claimants_and_Payments_by_Type_of_Loss.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "insurance",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2011-011",
+            "dataQuality": true,
             "description": "<p>The Servicemembers' Group Life Insurance Traumatic Injury Protection Program (TSGLI) Claimants and Payments by Type of Loss dataset provides the number of claimants approved, the dollar amount paid, and the average payment for each type of loss.</p>",
-            "title": "FY11_TSGLI Claimants and Payments by Type of Loss 05/2011",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63336,70 +63315,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nynv-4bdb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nynv-4bdb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nynv-4bdb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/nynv-4bdb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nynv-4bdb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nynv-4bdb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/nynv-4bdb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/nynv-4bdb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/nynv-4bdb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-011",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/TSGLI_Claimants_and_Payments_by_Type_of_Loss.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_TSGLI_Claimants_and_Payments_by_Type_of_Loss.doc"
+            ],
+            "temporal": "2011-05-01T04:00:00Z/2011-05-31T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY11_TSGLI Claimants and Payments by Type of Loss 05/2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://department-of-veterans-affairs.github.io/gi-bill-comparison-tool/",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2014-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
-            "keyword": [
-                "gi bill",
-                "gi bill benefits",
-                "vba benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INFO-013",
+            "dataQuality": true,
             "description": "<p>GI BILL Comparison Tool/ Calculate your benefits and research approved programs.</p>",
-            "title": "GI BILL Comparison Tool/ Calculate your benefits and research approved programs.",
-            "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63408,27 +63389,59 @@
                     "title": "html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INFO-013",
+            "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "gi bill",
+                "gi bill benefits",
+                "vba benefits"
+            ],
+            "landingPage": "http://department-of-veterans-affairs.github.io/gi-bill-comparison-tool/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-08",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-10-01T04:00:00Z/2014-12-30T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GI BILL Comparison Tool/ Calculate your benefits and research approved programs."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/p2pf-khui",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Sail Operations",
+                "hasEmail": "mailto:VHASailOperations@va.gov"
+            },
+            "dataQuality": true,
+            "description": "Strategic Analytics for Improvement and Learning Value Model or SAIL, is a system for summarizing hospital system performance within Veterans Health Administration (VHA). SAIL assesses key Quality measures in areas such as death rate, complications, and patient satisfaction, as well as overall efficiency at individual VA Medical Centers (VAMCs).  These .ZIP files are no longer supported and are in an 'as-is' state.  They were accurate at time of publication.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/p2pf-khui/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/p2pf-khui",
+            "isPartOf": "VA-VHA-OIA-122",
             "issued": "2020-08-18",
-            "@type": "dcat:Dataset",
-            "temporal": "2017-10-01/2018-09-30",
-            "modified": "2021-06-24",
             "keyword": [
                 "2018",
                 "analytics",
@@ -63449,69 +63462,39 @@
                 "veterans health administration",
                 "vha"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Sail Operations",
-                "hasEmail": "mailto:VHASailOperations@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/p2pf-khui",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-06-24",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/p2pf-khui",
-            "description": "Strategic Analytics for Improvement and Learning Value Model or SAIL, is a system for summarizing hospital system performance within Veterans Health Administration (VHA). SAIL assesses key Quality measures in areas such as death rate, complications, and patient satisfaction, as well as overall efficiency at individual VA Medical Centers (VAMCs).  These .ZIP files are no longer supported and are in an 'as-is' state.  They were accurate at time of publication.",
-            "title": "SAIL FY2018 Hospital Performance - All Facilities",
-            "isPartOf": "VA-VHA-OIA-122",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/p2pf-khui/application/zip",
-                    "mediaType": "application/zip"
-                }
-            ],
             "spatial": "United States, Puerto Rico",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "temporal": "2017-10-01/2018-09-30",
             "theme": [
                 "Hospital Quality Measurement"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAIL FY2018 Hospital Performance - All Facilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/p3jq-jrvt",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2013-08-03T04:00:00Z/2015-07-28T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cemetery",
-                "memorials list"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James Killens III",
                 "hasEmail": "mailto:james.killensiii@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-NCA-MP-012",
+            "dataQuality": true,
             "description": "<p>This documents lists all Memorials in VA's National Cemeteries</p>",
-            "title": "NCA Memorials By Cemetery",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63520,41 +63503,41 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-NCA-MP-012",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cemetery",
+                "memorials list"
+            ],
+            "landingPage": "https://www.data.va.gov/d/p3jq-jrvt",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2013-08-03T04:00:00Z/2015-07-28T04:00:00Z",
             "theme": [
                 "Memorials List"
-            ]
+            ],
+            "title": "NCA Memorials By Cemetery"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ptsd.va.gov/repository",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "issued": "2023-10-12",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-19",
-            "keyword": [
-                "ahrq",
-                "ahrq report"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for PTSD",
                 "hasEmail": "mailto:ncptsd@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for PTSD"
-            },
-            "identifier": "https://www.data.va.gov/api/views/p5ax-znsg",
             "description": "The U.S. Department of Veterans Affairs (VA) has established a long-term partnership to commission AHRQ to utilize its Evidence-based Practice Centers to develop update reviews to inform the VA\u2019s PTSD-Repository \u2013 a publicly accessible clinical trials database maintained by the National Center for PTSD (NCPTSD).\n\nThe 2023 Report, Executive Summary and Evidence Tables (Appendix E, F, G1, & G2) are included in the downloadable .zip file. For more information, visit AHRQ's page: https://effectivehealthcare.ahrq.gov/products/ptsd-pharm-non-pharm-treatment/research",
-            "title": "AHRQ Report and Data Files (2023): Pharmacologic and Nonpharmacologic Treatments for Posttraumatic Stress Disorder (Update of the PTSD-Repository Evidence Base)",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63562,48 +63545,45 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/p5ax-znsg",
+            "issued": "2023-10-12",
+            "keyword": [
+                "ahrq",
+                "ahrq report"
+            ],
+            "landingPage": "https://www.ptsd.va.gov/repository",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-03-19",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for PTSD"
+            },
+            "rights": "All data is within the public domain and is currently available for download.",
             "spatial": "International",
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "PTSD Randomized Controlled Trials"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AHRQ Report and Data Files (2023): Pharmacologic and Nonpharmacologic Treatments for Posttraumatic Stress Disorder (Update of the PTSD-Repository Evidence Base)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "fy2012 benefits",
-                "fy2012 vba",
-                "vba",
-                "vba benefits",
-                "vba benefits by state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-117",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Pennsylvania-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63611,45 +63591,49 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-117",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy2012 benefits",
+                "fy2012 vba",
+                "vba",
+                "vba benefits",
+                "vba benefits by state"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR 2012"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Pennsylvania-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/finance/overpaymentsReport.asp",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2011-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "improper payments",
-                "overpayments"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Katherine Palmer",
                 "hasEmail": "mailto:Katherine.Palmer@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-085",
+            "dataQuality": true,
             "description": "<p>FY 2012 First Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2012 First Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63658,86 +63642,86 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-085",
+            "issued": "2017-07-26",
+            "keyword": [
+                "improper payments",
+                "overpayments"
+            ],
+            "landingPage": "https://www.va.gov/finance/overpaymentsReport.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2011-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2012 First Quarter High-Dollar Overpayments Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Monica Reyes",
+                "hasEmail": "mailto:monica.reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Home Loan Guaranty- December 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING122013-013",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 114",
                 "home loan guaranty",
                 "lgy",
                 "usa spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:monica.reyes@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING122013-013",
-            "description": "<p>USA Spending- Home Loan Guaranty- December 2013.</p>",
-            "title": "USA Spending file- Home Loan  Guaranty-  CFDA 64.114",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- Home Loan  Guaranty-  CFDA 64.114"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/p7qi-k6z7",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-09",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "a93477d5-da85-449f-8c3b-85da1c1789e6",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary California FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63745,42 +63729,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "a93477d5-da85-449f-8c3b-85da1c1789e6",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/p7qi-k6z7",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary California FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "fy2012 benefits",
-                "fy2012 vba",
-                "vba",
-                "vba benefits",
-                "vba benefits by state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-106",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Nevada-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63788,98 +63768,96 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-106",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy2012 benefits",
+                "fy2012 vba",
+                "vba",
+                "vba benefits",
+                "vba benefits by state"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR 2012"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Nevada-FY12 Benefits Summary"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/p8ez-fpia",
-            "issued": "2023-07-04",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-11",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Minnesota FY2021",
+            "identifier": "https://www.data.va.gov/api/views/p8ez-fpia",
+            "issued": "2023-07-04",
             "keyword": [
                 "fy2021 data",
                 "minnesota",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/p8ez-fpia",
+            "landingPage": "https://www.data.va.gov/d/p8ez-fpia",
+            "modified": "2024-06-11",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Minnesota FY2021",
             "title": "NCVAS State Summary Minnesota FY2021"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/p8ge-7syx",
-            "issued": "2023-07-27",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-17",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Pennsylvania FY2021",
+            "identifier": "https://www.data.va.gov/api/views/p8ge-7syx",
+            "issued": "2023-07-27",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "pennsylvania"
             ],
-            "identifier": "https://www.data.va.gov/api/views/p8ge-7syx",
+            "landingPage": "https://www.data.va.gov/d/p8ge-7syx",
+            "modified": "2024-06-17",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Pennsylvania FY2021",
             "title": "NCVAS State Summary Pennsylvania FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Enrollment_by_State_as_of_Sept_2012.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-09-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotes_Number_of_Veterans_Enrolled_in_VGLI_by_State_2.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "insurance",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2012-014",
+            "dataQuality": true,
             "description": "<p>Provides the number of Veterans insured under the Veterans' Group Life Insurance (VGLI) program by state.  This report provides a snapshot of the active VGLI membership as of September 30, 2012.  For members who reside outside the United States, membership is not identified by individual country.  The total number of members was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "Number of Veterans Insured by VGLI by State as of September 30, 2012",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63887,71 +63865,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/p99d-rj6h/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/p99d-rj6h/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/p99d-rj6h/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/p99d-rj6h/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/p99d-rj6h/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/p99d-rj6h/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/p99d-rj6h/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/p99d-rj6h/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/p99d-rj6h/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-014",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Enrollment_by_State_as_of_Sept_2012.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotes_Number_of_Veterans_Enrolled_in_VGLI_by_State_2.doc"
+            ],
+            "temporal": "2012-09-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Number of Veterans Insured by VGLI by State as of September 30, 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/p9xy-tb8w",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-12-13",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-05",
-            "keyword": [
-                "utilization",
-                "va benefits",
-                "va programs",
-                "va services",
-                "veteran benefits",
-                "veterans",
-                "veterans benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/p9xy-tb8w",
             "description": "Reports number of participants in one or more VA programs. Data underlying the first table of Part 1 of the FY2021 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Number of Users of One or More VA Programs by Sex, FY2010-2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63959,57 +63937,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/p9xy-tb8w/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/p9xy-tb8w/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/p9xy-tb8w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/p9xy-tb8w/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/p9xy-tb8w/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/p9xy-tb8w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/p9xy-tb8w/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/p9xy-tb8w/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/p9xy-tb8w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/p9xy-tb8w",
+            "issued": "2022-12-13",
+            "keyword": [
+                "utilization",
+                "va benefits",
+                "va programs",
+                "va services",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/p9xy-tb8w",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-01-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Number of Users of One or More VA Programs by Sex, FY2010-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/OGC/opinions/2014PrecedentOpinions.asp",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "ogc",
-                "opinion"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OGC Law Library",
                 "hasEmail": "mailto:OGCLawLibrary@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OGC-007",
             "description": "<p>Effective Dates of Awards Based on Same-Sex Marriage</p>",
-            "title": "OGC Precedent Opinion 3-2014",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64018,49 +64001,44 @@
                     "title": "VAOGCPREC 3-2014"
                 }
             ],
+            "identifier": "VA-OGC-007",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion"
+            ],
+            "landingPage": "https://www.va.gov/OGC/opinions/2014PrecedentOpinions.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:083"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OGC Precedent Opinion 3-2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pbaa-5v5j",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-03-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-05",
-            "keyword": [
-                "utilization",
-                "va benefits",
-                "va programs",
-                "va services",
-                "veteran benefits",
-                "veterans",
-                "veterans benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/pbaa-5v5j",
             "description": "Data underlying the fourth figure of Part 1 of the FY2021 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Age Distribution of Users by Sex, FY2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64068,62 +64046,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pbaa-5v5j/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pbaa-5v5j/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pbaa-5v5j/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/pbaa-5v5j/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pbaa-5v5j/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pbaa-5v5j/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pbaa-5v5j/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pbaa-5v5j/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pbaa-5v5j/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/pbaa-5v5j",
+            "issued": "2022-03-15",
+            "keyword": [
+                "utilization",
+                "va benefits",
+                "va programs",
+                "va services",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pbaa-5v5j",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-01-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Age Distribution of Users by Sex, FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pbe2-j9db",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "references": [
-                "https://www.benefits.va.gov/reports/annual_performance_reports.asp"
-            ],
-            "keyword": [
-                "compensation",
-                "county",
-                "pension"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS Mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-042",
+            "dataQuality": true,
             "description": "<p>This report provides county-level estimates of the number of Veterans who received VA Disability Compensation or Pension benefits during FY 2012. It includes the Veterans' total disability rating, age group, and gender.</p>",
-            "title": "Compensation and pension by County: 2012",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64131,86 +64111,89 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-042",
+            "issued": "2017-07-26",
+            "keyword": [
+                "compensation",
+                "county",
+                "pension"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pbe2-j9db",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.benefits.va.gov/reports/annual_performance_reports.asp"
+            ],
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "Compensation and Pension Recipient by County"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Compensation and pension by County: 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Dusca Fichtel",
+                "hasEmail": "mailto:Dusca.Fichtel@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Face Amount of New Life Insurance Policies Issued- March 2013</p>",
+            "identifier": "VA-VBA-USASPENDING032014-055",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-03-01T05:00:00Z/2013-03-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 030",
                 "direct payment to veterans",
                 "insurance service",
                 "usa spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Dusca Fichtel",
-                "hasEmail": "mailto:Dusca.Fichtel@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING032014-055",
-            "description": "<p>USA Spending- Face Amount of New Life Insurance Policies Issued- March 2013</p>",
-            "title": "USA Spending file- March 2014-Direct Payments for Veterans-Insurance -  CFDA 64.031",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2013-03-01T05:00:00Z/2013-03-31T04:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- March 2014-Direct Payments for Veterans-Insurance -  CFDA 64.031"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pdxx-k6nz",
-            "bureauCode": [
-                "029:00"
-            ],
-            "issued": "2017-07-26",
             "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "minnesota",
-                "veterans"
+            "accessLevel": "public",
+            "bureauCode": [
+                "029:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-110",
             "description": "<p>This is a summary of the programs and services provided by VA in Minnesota in fiscal year 2014.</p>",
-            "title": "State Summary:  Minnesota",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64219,45 +64202,45 @@
                     "title": "State Summary:  Minnesota"
                 }
             ],
+            "identifier": "VA-OEI-OEI-110",
+            "issued": "2017-07-26",
+            "keyword": [
+                "minnesota",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pdxx-k6nz",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "State Summary:  Minnesota"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/pe25-dg2u",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "benefits",
-                "bgs"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kenneth Wimsatt",
                 "hasEmail": "mailto:kenneth.wimsatt@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-BGS-96",
+            "dataQuality": true,
             "description": "<p>Reads list values by a GroupTypeName, such as CMPTNY_DECN_TYPE, to get a list of competency decision types</p>",
-            "title": "SvnTypeEJBService",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64266,41 +64249,40 @@
                     "title": "SvnTypeEJBService"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-BGS-96",
+            "issued": "2017-11-17",
+            "keyword": [
+                "benefits",
+                "bgs"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pe25-dg2u",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "SvnTypeEJBService"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pe6h-8ani",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "accreditation",
-                "ogc",
-                "system of records"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OGC Law Library",
                 "hasEmail": "mailto:OGCLawLibrary@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OGC-043",
             "description": "<p>Accreditation Records\u2014VA</p>",
-            "title": "OGC Privacy Act System of Records Notice 01VA022",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64309,48 +64291,43 @@
                     "title": "OGC Privacy Act System of Records Notice 01VA022"
                 }
             ],
+            "identifier": "VA-OGC-043",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accreditation",
+                "ogc",
+                "system of records"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pe6h-8ani",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:083"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "OGC Privacy Act System of Records Notice 01VA022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_Amount_by_Program_by_State_October2012.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2012-10-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Face_Amount_by_Program_October2012.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "county",
-                "insurance",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2012-022",
+            "dataQuality": true,
             "description": "<p>Face value of insurance for each administered life insurance program listed by state. Data is current as of 10/31/12.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "Face Amount of Life Insurance Coverage by Program by State by 10-31-2012",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64358,66 +64335,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pea2-ddc6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pea2-ddc6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pea2-ddc6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/pea2-ddc6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pea2-ddc6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pea2-ddc6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pea2-ddc6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pea2-ddc6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pea2-ddc6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-022",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "county",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_Amount_by_Program_by_State_October2012.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Face_Amount_by_Program_October2012.doc"
+            ],
+            "temporal": "2012-10-01T04:00:00Z/2012-10-31T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Face Amount of Life Insurance Coverage by Program by State by 10-31-2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pfgr-c6ys",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "9e9cecf2-b92b-454a-87d2-10a292b575f8",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Puerto Rico FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64425,19 +64409,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "9e9cecf2-b92b-454a-87d2-10a292b575f8",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pfgr-c6ys",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary Puerto Rico FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/Expenditures.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Andrew Bickel",
+                "hasEmail": "mailto:andrew.bickel@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.va.gov/vetdata/docs/GDX/W-GDX-FY05-000-.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "xls"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-031",
             "issued": "2017-07-26",
-            "temporal": "2004-10-01T04:00:00Z/2005-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -64451,87 +64464,56 @@
                 "insurance",
                 "medical care"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Andrew Bickel",
-                "hasEmail": "mailto:andrew.bickel@va.gov"
-            },
+            "landingPage": "https://www.va.gov/VETDATA/Expenditures.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-OEI-OEI-031",
-            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY2005",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.va.gov/vetdata/docs/GDX/W-GDX-FY05-000-.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "xls"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2004-10-01T04:00:00Z/2005-09-30T04:00:00Z",
             "theme": [
                 "Expenditures"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geographic Distribution of VA Expenditures FY2005"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pgjk-rrqk",
-            "issued": "2024-09-02",
             "@type": "dcat:Dataset",
-            "modified": "2024-09-03",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rebecca Matteo",
                 "hasEmail": "mailto:no-reply@ptsd-va.data.socrata.com"
             },
+            "description": "Access reference guides for the PTSD Repository and manuals to support data analyses as well as the annual update reports created by the Agency for Healthcare and Research Quality.",
             "identifier": "https://www.data.va.gov/api/views/pgjk-rrqk",
+            "issued": "2024-09-02",
+            "landingPage": "https://www.data.va.gov/d/pgjk-rrqk",
+            "modified": "2024-09-03",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "Access reference guides for the PTSD Repository and manuals to support data analyses as well as the annual update reports created by the Agency for Healthcare and Research Quality.",
             "title": "Reference Guides"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pgjq-abwt",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2023-04-14",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-19",
-            "keyword": [
-                "death rate",
-                "life expectancy",
-                "life table"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/pgjq-abwt",
             "description": "",
-            "title": "Table 1 - U. S. Veterans Life Table for Male 1980-1989",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64539,57 +64521,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pgjq-abwt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pgjq-abwt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pgjq-abwt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/pgjq-abwt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pgjq-abwt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pgjq-abwt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pgjq-abwt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pgjq-abwt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pgjq-abwt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/pgjq-abwt",
+            "issued": "2023-04-14",
+            "keyword": [
+                "death rate",
+                "life expectancy",
+                "life table"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pgjq-abwt",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-04-19",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Table 1 - U. S. Veterans Life Table for Male 1980-1989"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pgnh-g8fq",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 109"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/pgnh-g8fq",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to compensate veterans for disabilities incurred or aggravated during military service according to the average impairment in earning capacity such disability would cause in civilian occupations. Persons who have suffered disabilities resulting from service in the Armed Forces of the United States. The disability must have been incurred or aggravated by service in the line of duty. Separation from service must have been under other than dishonorable conditions for the period in which the disability was incurred or aggravated.</p>",
-            "title": "USA SPENDING C&P B109 VETERANS COMPENSATION FOR SERVICE-CONNECTED DISABILITY NOV2018",
-            "isPartOf": "6013cae5-a8c2-47ff-9c90-9cbdba7bda63",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64597,91 +64581,83 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pgnh-g8fq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pgnh-g8fq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pgnh-g8fq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/pgnh-g8fq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pgnh-g8fq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pgnh-g8fq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pgnh-g8fq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pgnh-g8fq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pgnh-g8fq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/pgnh-g8fq",
+            "isPartOf": "6013cae5-a8c2-47ff-9c90-9cbdba7bda63",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 109"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pgnh-g8fq",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING C&P B109 VETERANS COMPENSATION FOR SERVICE-CONNECTED DISABILITY NOV2018"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/phtc-bs3w",
-            "issued": "2024-03-27",
             "@type": "dcat:Dataset",
-            "modified": "2024-09-04",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rebecca Matteo",
                 "hasEmail": "mailto:no-reply@ptsd-va.data.socrata.com"
             },
+            "description": "",
             "identifier": "https://www.data.va.gov/api/views/phtc-bs3w",
+            "issued": "2024-03-27",
+            "landingPage": "https://www.data.va.gov/d/phtc-bs3w",
+            "modified": "2024-09-04",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "",
             "title": "For Researchers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pj3n-knxa",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf"
-            ],
-            "keyword": [
-                "health",
-                "healthcare",
-                "hospital accreditation",
-                "patient safety",
-                "quality of care",
-                "satisfaction",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Open Data",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VHA-OIA-034",
-            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset defines the quality of care at a national level between rural vs urban populations.</p>",
-            "title": "Veterans Health Administration 2008 Hospital Report Card - Rural vs Urban",
-            "isPartOf": "VA-VHA-OIA-583",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:040"
-            ],
+            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset defines the quality of care at a national level between rural vs urban populations.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64689,95 +64665,104 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pj3n-knxa/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pj3n-knxa/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pj3n-knxa/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/pj3n-knxa/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pj3n-knxa/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pj3n-knxa/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pj3n-knxa/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pj3n-knxa/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pj3n-knxa/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-034",
+            "isPartOf": "VA-VHA-OIA-583",
+            "issued": "2017-07-26",
+            "keyword": [
+                "health",
+                "healthcare",
+                "hospital accreditation",
+                "patient safety",
+                "quality of care",
+                "satisfaction",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pj3n-knxa",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:040"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf"
+            ],
+            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
             "theme": [
                 "Section 3. Health and Nutrition"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Health Administration 2008 Hospital Report Card - Rural vs Urban"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:25"
             ],
-            "landingPage": "https://www.data.va.gov/d/pkau-dyhd",
-            "issued": "2021-02-07",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-07",
-            "keyword": [
-                "veterans benefits utilization covid claims programs backlog disability examinations"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell or Amy Adler",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/pkau-dyhd",
             "description": "Shows effect of COVID-19 and Medical Examination pause on VBA Claims Inventory",
-            "title": "VBA Weekly Benefits Claims Inventory",
+            "identifier": "https://www.data.va.gov/api/views/pkau-dyhd",
+            "issued": "2021-02-07",
+            "keyword": [
+                "veterans benefits utilization covid claims programs backlog disability examinations"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pkau-dyhd",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-02-07",
             "programCode": [
                 "029:003"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VBA Weekly Benefits Claims Inventory"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pkxd-6kb8",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-06-28",
-            "@type": "dcat:Dataset",
-            "modified": "2021-08-27",
-            "keyword": [
-                "ncvas",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/pkxd-6kb8",
+            "dataQuality": true,
             "description": "This dataset is comprised of 1 year estimate data from the American Community Survey published as of 2019.",
-            "title": "NCVAS State Summaries - Age Percentages (chart)",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64785,59 +64770,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pkxd-6kb8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pkxd-6kb8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pkxd-6kb8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/pkxd-6kb8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pkxd-6kb8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pkxd-6kb8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pkxd-6kb8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pkxd-6kb8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pkxd-6kb8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/pkxd-6kb8",
+            "issued": "2021-06-28",
+            "keyword": [
+                "ncvas",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pkxd-6kb8",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2021-08-27",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "NCVAS State Summaries - Age Percentages (chart)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pmg2-eh8a",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "060307ff-7ae5-4c40-ae20-9420414ea3a9",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Nebraska FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64845,37 +64829,37 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "060307ff-7ae5-4c40-ae20-9420414ea3a9",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pmg2-eh8a",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary Nebraska FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pmk4-42rk",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-06-01T04:00:00Z/2015-06-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-21",
-            "keyword": [
-                "debt referrals"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vikki Soukup",
                 "hasEmail": "mailto:Vikki.Soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-145",
+            "dataQuality": true,
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "June 2015 Coin 146",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64883,83 +64867,66 @@
                     "mediaType": "text/plain"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-145",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referrals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pmk4-42rk",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-21",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-06-01T04:00:00Z/2015-06-30T04:00:00Z",
             "theme": [
                 "financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "June 2015 Coin 146"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pncm-xu8k",
-            "issued": "2023-06-18",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Colorado FY2021",
+            "identifier": "https://www.data.va.gov/api/views/pncm-xu8k",
+            "issued": "2023-06-18",
             "keyword": [
                 "colorado",
                 "fy2021 data",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/pncm-xu8k",
+            "landingPage": "https://www.data.va.gov/d/pncm-xu8k",
+            "modified": "2024-05-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Colorado FY2021",
             "title": "NCVAS State Summary Colorado FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ppau-kqm3",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2020-10-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-05",
-            "keyword": [
-                "cemetery",
-                "disability compensation",
-                "disability pension",
-                "education benefits",
-                "gulf war",
-                "healthcare",
-                "health care",
-                "home loan guaranty",
-                "life insurance",
-                "memorial",
-                "memorials",
-                "pension",
-                "veteran population",
-                "veterans",
-                "veterans affairs",
-                "veterans data",
-                "vocational rehabilitation",
-                "vocational rehabilitation services"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mark Guagliardo",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/ppau-kqm3",
             "description": "This data set consists of one row per federal fiscal year (FY) from FY 2010 - FY 2019, and reports the number of users, non-users and percent users for each of eight VA programs for Veterans who were in service at any time between August 2, 1990, and September 10, 2001, the dates of the Pre-9/11 Gulf War era. Data for the Disability Compensation and Disability Pension programs are reported separately as well as together under the name Compensation or Pension.",
-            "title": "Gulf War - Pre 9/11 Veterans: Trends in Users by VA Program",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64967,57 +64934,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ppau-kqm3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ppau-kqm3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ppau-kqm3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ppau-kqm3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ppau-kqm3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ppau-kqm3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ppau-kqm3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ppau-kqm3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ppau-kqm3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/ppau-kqm3",
+            "issued": "2020-10-27",
+            "keyword": [
+                "cemetery",
+                "disability compensation",
+                "disability pension",
+                "education benefits",
+                "gulf war",
+                "healthcare",
+                "health care",
+                "home loan guaranty",
+                "life insurance",
+                "memorial",
+                "memorials",
+                "pension",
+                "veteran population",
+                "veterans",
+                "veterans affairs",
+                "veterans data",
+                "vocational rehabilitation",
+                "vocational rehabilitation services"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ppau-kqm3",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2020-11-05",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Gulf War - Pre 9/11 Veterans: Trends in Users by VA Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pr3y-rdsd",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "947172ce-2499-4e0b-85c3-c7bf092d11e9",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Utah FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65025,22 +65009,50 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "947172ce-2499-4e0b-85c3-c7bf092d11e9",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pr3y-rdsd",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary Utah FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pruk-7vxd",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/HospitalReportCard.asp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/HospitalReportCard.asp",
+            "description": "<p>Root Cause Analyses (RCAs) completed within 45 days and outcome measures reported.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset9_RCA.xml",
+                    "mediaType": "application/xml",
+                    "title": "Root Cause Analysis"
+                }
             ],
+            "identifier": "VA-VHA-OIA-047",
+            "isPartOf": "VA-VHA-OIA-584",
+            "issued": "2017-07-26",
             "keyword": [
                 "ambulatory",
                 "care",
@@ -65063,93 +65075,65 @@
                 "urban",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/pruk-7vxd",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-047",
-            "description": "<p>Root Cause Analyses (RCAs) completed within 45 days and outcome measures reported.</p>",
-            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Root Cause Analysis",
-            "isPartOf": "VA-VHA-OIA-584",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset9_RCA.xml",
-                    "mediaType": "application/xml",
-                    "title": "Root Cause Analysis"
-                }
+            "references": [
+                "https://www.va.gov/health/HospitalReportCard.asp"
             ],
-            "describedBy": "https://www.va.gov/health/HospitalReportCard.asp",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
             "theme": [
                 "Section 3. Health and Nutrition"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Root Cause Analysis"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ptdj-ss3q",
-            "issued": "2023-08-11",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Utah FY2021",
+            "identifier": "https://www.data.va.gov/api/views/ptdj-ss3q",
+            "issued": "2023-08-11",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "utah"
             ],
-            "identifier": "https://www.data.va.gov/api/views/ptdj-ss3q",
+            "landingPage": "https://www.data.va.gov/d/ptdj-ss3q",
+            "modified": "2024-06-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Utah FY2021",
             "title": "NCVAS State Summary Utah FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pu4d-ff97",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 127"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/pu4d-ff97",
+            "dataQuality": true,
             "description": "<p>VBA COMPENSTATION BENEFITS PRGOGRAM to provide vocational training and rehabilitation to certain children born with spina bifida or other covered birth defects who are children of Vietnam veterans and some Korean veterans. \u201cA child born with spina bifida or other covered birth defects, except spina bifida occulta, who is the natural child of a Vietnam veteran and some Korean veterans, regardless of the age or marital status of the child, conceived after the date on which the veteran first served in the Republic of Vietnam during the Vietnam era and in particular areas near the DMZ in the Korean conflict. VA must also determine that it is feasible for the child to achieve a vocational goal.\u201d</p>",
-            "title": "USA SPENDING COMPENSATION CH18 B127 ALLOWANCE FOR CHILDREN OF VIETNAM VETERANS BORN WITH SPINA BIFIDA OCT2018",
-            "isPartOf": "faff9e4c-e7ad-440d-bd48-6843c4358f8a",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65157,44 +65141,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pu4d-ff97/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pu4d-ff97/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pu4d-ff97/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/pu4d-ff97/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pu4d-ff97/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pu4d-ff97/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pu4d-ff97/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pu4d-ff97/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pu4d-ff97/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/pu4d-ff97",
+            "isPartOf": "faff9e4c-e7ad-440d-bd48-6843c4358f8a",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 127"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pu4d-ff97",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING COMPENSATION CH18 B127 ALLOWANCE FOR CHILDREN OF VIETNAM VETERANS BORN WITH SPINA BIFIDA OCT2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/pu94-4asd",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The VA Drug Pricing database contains the current prices for pharmaceuticals purchased by the federal government. These listed prices are based on the Federal Supply Schedule (FSS). This database is mandated by Public Law 102-585, the Veterans Health Care Act of 1992, which sets the maximum amount that a drug may be bought for by the Veterans Health Administration (VHA). The source of this information is contained in printed contracts or data files supplied by the drug manufacturers, representing the pricing agreements between VHA and the manufacturers. Price data is input by the National Acquisition Center (NAC) into the database administered by the Pharmacy Benefits Management Strategic Health Care Group. Information from this database is published on the World Wide Web at the following site: <a href=\"http://www.pbm.va.gov\">http://www.pbm.va.gov</a>. The users of this database include pharmaceutical manufacturers, drug wholesalers, Office of Inspector General (OIG) and those who purchase pharmaceuticals for the VHA and other government agencies.</p>",
+            "identifier": "VA-VHA-PBM-004",
+            "isPartOf": "VA-VHA-PBM-008",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1993-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "102-585",
                 "acquistion",
@@ -65210,97 +65214,72 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/pu94-4asd",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:047"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-PBM-004",
-            "description": "<p>The VA Drug Pricing database contains the current prices for pharmaceuticals purchased by the federal government. These listed prices are based on the Federal Supply Schedule (FSS). This database is mandated by Public Law 102-585, the Veterans Health Care Act of 1992, which sets the maximum amount that a drug may be bought for by the Veterans Health Administration (VHA). The source of this information is contained in printed contracts or data files supplied by the drug manufacturers, representing the pricing agreements between VHA and the manufacturers. Price data is input by the National Acquisition Center (NAC) into the database administered by the Pharmacy Benefits Management Strategic Health Care Group. Information from this database is published on the World Wide Web at the following site: <a href=\"http://www.pbm.va.gov\">http://www.pbm.va.gov</a>. The users of this database include pharmaceutical manufacturers, drug wholesalers, Office of Inspector General (OIG) and those who purchase pharmaceuticals for the VHA and other government agencies.</p>",
-            "title": "VA Drug Pricing Database",
-            "isPartOf": "VA-VHA-PBM-008",
-            "programCode": [
-                "029:047"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "1993-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Drug Pricing Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/pumt-4tkh",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-07",
-            "keyword": [
-                "florida",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/pumt-4tkh",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Florida",
+            "identifier": "https://www.data.va.gov/api/views/pumt-4tkh",
+            "issued": "2021-08-26",
+            "keyword": [
+                "florida",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pumt-4tkh",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-07",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_Florida"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Policies_in_Force_by_Program_by_State_August_2011.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-08-01T04:00:00Z/2011-08-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Policies_in_Force_by_Program3.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "insurance",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2011-007",
+            "dataQuality": true,
             "description": "<p>Number of life insurance policies for each administered life insurance program listed by state. Data is current as of 08/31/11.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "FY11_EOM_August_Number of Life Insurance Policies by Program by State",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65308,66 +65287,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/putc-e3gz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/putc-e3gz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/putc-e3gz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/putc-e3gz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/putc-e3gz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/putc-e3gz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/putc-e3gz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/putc-e3gz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/putc-e3gz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-007",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Policies_in_Force_by_Program_by_State_August_2011.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Policies_in_Force_by_Program3.doc"
+            ],
+            "temporal": "2011-08-01T04:00:00Z/2011-08-31T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY11_EOM_August_Number of Life Insurance Policies by Program by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pv33-xzzr",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "a1095712-5d50-426e-812f-41cdd561c5f9",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary South Dakota FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65375,45 +65359,43 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "a1095712-5d50-426e-812f-41cdd561c5f9",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pv33-xzzr",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data",
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "State Summary South Dakota FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pv6d-458a",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-02-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "compensation",
-                "county",
-                "direct payment to veterans",
-                "pension"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS Mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "10aec8d7-edea-461c-a87a-63265b70e8e1",
+            "dataQuality": true,
             "description": "<p>This file shows the number of Veterans in each state and county who received monthly Disability Compensation or Pension payments during fiscal year 2017.  It also includes breakdowns by disability rating groups, age groups, and gender.</p>",
-            "title": "FY2017 Compensation and Pension Recipients by County",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65421,41 +65403,43 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "10aec8d7-edea-461c-a87a-63265b70e8e1",
+            "issued": "2018-02-01",
+            "keyword": [
+                "compensation",
+                "county",
+                "direct payment to veterans",
+                "pension"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pv6d-458a",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "FY2017 Compensation and Pension Recipients by County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pvbe-vmni",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-01-01T05:00:00Z/2012-01-01T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "demographics",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:tom.garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-063",
+            "dataQuality": true,
             "description": "<p>The report uses 2012 Amercian Community Survey data to compare the demographic and socioeconomic characteristics of Veterans and non-Veterans.</p>",
-            "title": "Profile of Veterans: 2012",
-            "programCode": [
-                "029:006"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65464,74 +65448,73 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-063",
+            "issued": "2017-07-26",
+            "keyword": [
+                "demographics",
+                "veteran"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pvbe-vmni",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:006"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2012-01-01T05:00:00Z/2012-01-01T05:00:00Z",
             "theme": [
                 "Use of Benefits and Services"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Profile of Veterans: 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/pvqz-zcan",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Florida FY2023",
+            "identifier": "https://www.data.va.gov/api/views/pvqz-zcan",
             "issued": "2024-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
             "keyword": [
                 "fl",
                 "fy24 data",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/pvqz-zcan",
+            "modified": "2024-07-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/pvqz-zcan",
-            "description": "NCVAS State Summary Florida FY2023",
-            "title": "NCVAS State Summary Florida FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Florida FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pw5j-ygpw",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "ogc",
-                "opinion"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OGC Law Library",
                 "hasEmail": "mailto:OGCLawLibrary@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OGC-038",
             "description": "<p>Overpayment and Requirement to Offset from Compensation Paid Under 38 U.S.C., \u00a7 1151 Amounts Recovered Under the Federal Tort Claims Act</p>",
-            "title": "OGC Precedent Opinion 1-2010",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65540,46 +65523,43 @@
                     "title": "OGC Precedent Opinion 1-2010"
                 }
             ],
+            "identifier": "VA-OGC-038",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pw5j-ygpw",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:083"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "OGC Precedent Opinion 1-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "abr",
-                "abr2012",
-                "compensation benefits fy12",
-                "dic benefits",
-                "vba benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-034",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Veterans Receiving Service Connected Disability Benefits at the End of FY2012 by Period of Service",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65587,46 +65567,49 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-034",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "abr",
+                "abr2012",
+                "compensation benefits fy12",
+                "dic benefits",
+                "vba benefits"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR Reports"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Receiving Service Connected Disability Benefits at the End of FY2012 by Period of Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pwsq-k8vf",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2025-01-30",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-30",
-            "keyword": [
-                "engagement",
-                "satisfaction",
-                "survey",
-                "veterans affairs"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA National Center for Organization Development (NCOD)",
                 "hasEmail": "mailto:vhancod@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/pwsq-k8vf",
+            "dataQuality": true,
             "description": "2022 VA All Employee Survey (AES) deidentified individual-level public dataset",
-            "title": "AES 2022 PRDF",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65634,61 +65617,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pwsq-k8vf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pwsq-k8vf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pwsq-k8vf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/pwsq-k8vf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pwsq-k8vf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pwsq-k8vf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pwsq-k8vf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pwsq-k8vf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pwsq-k8vf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/pwsq-k8vf",
+            "issued": "2025-01-30",
+            "keyword": [
+                "engagement",
+                "satisfaction",
+                "survey",
+                "veterans affairs"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pwsq-k8vf",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2025-01-30",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "AES 2022 PRDF"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/pwwj-c6e5",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "bens",
-                "event",
-                "notification"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bret Meyer",
                 "hasEmail": "mailto:bret.meyer@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-ORCH-2",
+            "dataQuality": true,
             "description": "<p>BENS provides a notification of pre-defined business events to applications, portals, and automated business processes. Such events are defined in the Event Catalog, with examples including change in military service duty status, change of address, etc. Business events are defined and governed by the business, are used to drive business process, and exist independently of implementation considerations. The business event management service supports publication of business events by authorized publishers through the Event Notification governance process. The service supports subscription to business events by authorized subscribers, also supported by the governance process. The service supports automatic, reliable, and timely notification of published business events to subscribers. The service supports creation and modification of business event definitions. The service supports governance of changes to business event definitions, and authorization of publishers and subscribers. BENS is separate from data synchronization, though the interrelationships have been identified to ensure the elimination of redundancy and race conditions.</p>",
-            "title": "Business Event Notification Service (BENS)",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65697,40 +65679,42 @@
                     "title": "Business Event Notification Service (BENS)"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-ORCH-2",
+            "issued": "2017-11-17",
+            "keyword": [
+                "bens",
+                "event",
+                "notification"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pwwj-c6e5",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "Business Event Notification Service (BENS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pxuz-4zey",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "f4654ef5-892f-41d2-8a77-adfd3bbec9a1",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary North Dakota FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65738,43 +65722,37 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "f4654ef5-892f-41d2-8a77-adfd3bbec9a1",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pxuz-4zey",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary North Dakota FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Policies_in_Force_by_Program_by_State_July_2011.xls",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-07-01T04:00:00Z/2011-07-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Policies_in_Force_by_Program.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "insurance",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2011-001",
+            "dataQuality": true,
             "description": "<p>Number of life insurance policies for each administered life insurance program listed by state. Data is current as of 07/31/11.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "EOM July 2011 Number of Life Insurance Policies by Program by State",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65782,51 +65760,50 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-001",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Policies_in_Force_by_Program_by_State_July_2011.xls",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Policies_in_Force_by_Program.doc"
+            ],
+            "temporal": "2011-07-01T04:00:00Z/2011-07-31T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "EOM July 2011 Number of Life Insurance Policies by Program by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pxwu-u522",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2021-01-13",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-13",
-            "keyword": [
-                "benefits",
-                "exam",
-                "examinations",
-                "open data",
-                "va",
-                "vba",
-                "veterans",
-                "zip code"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:pai.vbaco@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/pxwu-u522",
             "description": "This is number 2 of 3 data sets that accompany Data Set for Maps Data Story on VA's Open Data Site. Specifically this identifies zip codes where VA facilities could perform benefits examinations during phase 2.\n\n\n\nSpecifically this provides zip codes where VA facilities that could perform benefits examinations during phase 2 .",
-            "title": "PAI Data Set For Maps Data Story 2 of 3",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65834,58 +65811,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pxwu-u522/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pxwu-u522/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pxwu-u522/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/pxwu-u522/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pxwu-u522/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pxwu-u522/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pxwu-u522/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pxwu-u522/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pxwu-u522/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/pxwu-u522",
+            "issued": "2021-01-13",
+            "keyword": [
+                "benefits",
+                "exam",
+                "examinations",
+                "open data",
+                "va",
+                "vba",
+                "veterans",
+                "zip code"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pxwu-u522",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-01-13",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "PAI Data Set For Maps Data Story 2 of 3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/budget/products.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "budget",
-                "fy2008"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OM Open Data",
                 "hasEmail": "mailto:VAOMOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-031",
+            "dataQuality": true,
             "description": "<p>FY2008 VA Budget Submission.</p>",
-            "title": "FY2008 VA Budget Submission",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65894,46 +65878,43 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-031",
+            "issued": "2017-07-26",
+            "keyword": [
+                "budget",
+                "fy2008"
+            ],
+            "landingPage": "https://www.va.gov/budget/products.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-10",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY2008 VA Budget Submission"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/pygk-j4gc",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2020-10-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
-            "keyword": [
-                "utilization",
-                "veteran benefits",
-                "veterans",
-                "veterans benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mark Guagliardo",
                 "hasEmail": "mailto:mark.guagliardo@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/pygk-j4gc",
             "description": "Participation Trend by Gender FY 2008-2019.  Reports number of participants in one or more VA programs. Data underlying the first table of Part 1 of the FY2018 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Veterans Utilization Profile FY18 - Table 1, Participation Trend by Gender FY 2008-2019",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65941,63 +65922,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pygk-j4gc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pygk-j4gc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pygk-j4gc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/pygk-j4gc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pygk-j4gc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pygk-j4gc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pygk-j4gc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pygk-j4gc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pygk-j4gc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/pygk-j4gc",
+            "issued": "2020-10-06",
+            "keyword": [
+                "utilization",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/pygk-j4gc",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Utilization Profile FY18 - Table 1, Participation Trend by Gender FY 2008-2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Coverage_by_State.csv",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-01-01T05:00:00Z/2011-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_VGLI_Coverage_Amount_by_State.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "insurance",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2011-016",
+            "dataQuality": true,
             "description": "<p>Provides the amount of Veterans' Group Life Insurance (VGLI) coverage by state.  This report provides a snapshot of the amount of VGLI coverage as of December 31, 2011.  For members who reside outside the United States, coverage is not identified by individual country.  The total amount of coverage was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "VGLI Coverage Amount by State as of December 31, 2011",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66005,74 +65984,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pzd7-ifzb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pzd7-ifzb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pzd7-ifzb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/pzd7-ifzb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pzd7-ifzb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pzd7-ifzb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/pzd7-ifzb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/pzd7-ifzb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/pzd7-ifzb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-016",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Coverage_by_State.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_VGLI_Coverage_Amount_by_State.doc"
+            ],
+            "temporal": "2011-01-01T05:00:00Z/2011-12-31T05:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VGLI Coverage Amount by State as of December 31, 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2013-10-01T04:00:00Z/2013-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "congress",
-                "data breeches",
-                "date of incident",
-                "location of event",
-                "number of credit protection letters",
-                "number of notification letters",
-                "quarterly notice",
-                "va"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rita Grewal",
                 "hasEmail": "mailto:Rita.Grewal@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OIT-ITIS-21",
+            "dataQuality": true,
             "description": "<p>This is a quarterly notice to congress containing statistics on data breeches for fiscal year 2014 for the first quarter (2014 October 1, 2013 through December 31, 2013).  The report contains information about date of the incidents, location of the events, number of notification letters, and number of credit protection letters sent.</p>",
-            "title": "Department of Veterans Affairs Quarterly Notice to Congress on Data Breaches First Quarter of Fiscal Year 2014 October 1, 2013 through December 31, 2013",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66081,46 +66059,52 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OIT-ITIS-21",
+            "issued": "2017-07-26",
+            "keyword": [
+                "congress",
+                "data breeches",
+                "date of incident",
+                "location of event",
+                "number of credit protection letters",
+                "number of notification letters",
+                "quarterly notice",
+                "va"
+            ],
+            "landingPage": "https://www.va.gov/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:080"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2013-10-01T04:00:00Z/2013-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Quarterly Notice to Congress on Data Breaches First Quarter of Fiscal Year 2014 October 1, 2013 through December 31, 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/q24f-g26e",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2014-10-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "accounts receivable"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vikki Soukup",
                 "hasEmail": "mailto:Vikki.Soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-101",
             "description": "<p>Aged accounts receivables report</p>",
-            "title": "COIN 0017 CARS AGE PROFILE REPORT Oct 2014",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66128,40 +66112,39 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-101",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accounts receivable"
+            ],
+            "landingPage": "https://www.data.va.gov/d/q24f-g26e",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-10-01T04:00:00Z/2014-10-31T04:00:00Z",
             "theme": [
                 "Financial"
-            ]
+            ],
+            "title": "COIN 0017 CARS AGE PROFILE REPORT Oct 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/q2cg-nej5",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "vermont",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-132",
             "description": "<p>This is a summary of the programs and services provided by VA in Vermont in fiscal year 2014.</p>",
-            "title": "State Summary:  Vermont",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66170,51 +66153,45 @@
                     "title": "State Summary:  Vermont"
                 }
             ],
+            "identifier": "VA-OEI-OEI-132",
+            "issued": "2017-07-26",
+            "keyword": [
+                "vermont",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/q2cg-nej5",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "State Summary:  Vermont"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_VGLI_Coverage_Amount_by_State.doc",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-09-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotes_VGLI_Coverage_Amount_by_State.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "county",
-                "insurance",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2012-021",
+            "dataQuality": true,
             "description": "<p>Provides the amount of Veterans' Group Life Insurance (VGLI) coverage by state.  This report provides a snapshot of the amount of VGLI coverage as of September 30, 2012.  For members who reside outside the United States, coverage is not identified by individual country.  The total amount of coverage was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "VGLI Coverage Amount by State as of September 30, 2012",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66222,65 +66199,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/q2vm-t64x/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/q2vm-t64x/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/q2vm-t64x/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/q2vm-t64x/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/q2vm-t64x/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/q2vm-t64x/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/q2vm-t64x/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/q2vm-t64x/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/q2vm-t64x/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-021",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "county",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_VGLI_Coverage_Amount_by_State.doc",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotes_VGLI_Coverage_Amount_by_State.doc"
+            ],
+            "temporal": "2012-09-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VGLI Coverage Amount by State as of September 30, 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/q33d-9hdm",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "missouri"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DG&amp;A Mailgroup",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-196",
             "description": "<p>This summary describes the programs and services VA provided in Missouri in fiscal year 2015.</p>",
-            "title": "State Summary: Missouri FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66289,22 +66273,42 @@
                     "title": "Missouri"
                 }
             ],
+            "identifier": "VA-OEI-OEI-196",
+            "issued": "2017-07-26",
+            "keyword": [
+                "missouri"
+            ],
+            "landingPage": "https://www.data.va.gov/d/q33d-9hdm",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "State Summary: Missouri FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/q3fu-7ckx",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Mark Guagliardo",
+                "hasEmail": "mailto:mark.guagliardo@va.gov"
+            },
+            "description": "The Department of Veterans honors Veterans of the Vietnam War with this data story published for Memorial Day 2021.",
+            "identifier": "https://www.data.va.gov/api/views/q3fu-7ckx",
             "issued": "2021-04-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-25",
             "keyword": [
                 "memorial day",
                 "veterans",
@@ -66313,51 +66317,31 @@
                 "vietnam veterans",
                 "vietnam war"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Mark Guagliardo",
-                "hasEmail": "mailto:mark.guagliardo@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/q3fu-7ckx",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2021-05-25",
+            "programCode": [
+                "029:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/q3fu-7ckx",
-            "description": "The Department of Veterans honors Veterans of the Vietnam War with this data story published for Memorial Day 2021.",
-            "title": "Vietnam Veterans - Memorial Day 2021",
-            "programCode": [
-                "029:000"
-            ],
-            "license": "https://www.usa.gov/government-works"
+            "title": "Vietnam Veterans - Memorial Day 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/q3gx-bw7i",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 032"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/q3gx-bw7i",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to encourage membership in units of the Selected Reserve of the Ready Reserve and to provide educational assistance to members of the reserve components called or ordered to active service in response to a war or national emergency declared by the President or Congress. Generally, to qualify for benefits under MGIB-SR you must (1) Have a six-year obligation to serve in the Selected Reserve signed after June 30, 1985. If you are an officer, you must have agreed to serve six years in addition to your original obligation. For some types of training, it is necessary to have a six-year commitment that begins after September 30, 1990; (2) Complete your initial active duty for training (IADT); (3) Meet the requirement to receive a high school diploma or equivalency certificate before completing IADT. You may not use 12 hours toward a college degree to meet this requirement; and (4) Remain in good standing while serving in an active Selected Reserve unit. Generally, to qualify for benefits under REAP you must have served at least 90 consecutive days on active duty as a result of a call or order to active duty from a reserve component in response to a war or national emergency declared by the President or Congress. This is not a complete list of eligibility requirements. For more information on MGIB-SR and REAP visit <a href=\"http://www.gibill.va.gov\">http://www.gibill.va.gov</a>.</p>",
-            "title": "USA SPENDING EDUCATION CH1606 & CH1607 B032 MONTGOMERY GI BILL SELECTED RESERVE; RESERVE EDUCATIONAL ASSISTANCE PROGRAM FEB2019",
-            "isPartOf": "b2a0a5f0-3d2f-490f-8b42-3eb1db21b8e0",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66365,66 +66349,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/q3gx-bw7i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/q3gx-bw7i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/q3gx-bw7i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/q3gx-bw7i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/q3gx-bw7i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/q3gx-bw7i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/q3gx-bw7i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/q3gx-bw7i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/q3gx-bw7i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/q3gx-bw7i",
+            "isPartOf": "b2a0a5f0-3d2f-490f-8b42-3eb1db21b8e0",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 032"
+            ],
+            "landingPage": "https://www.data.va.gov/d/q3gx-bw7i",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING EDUCATION CH1606 & CH1607 B032 MONTGOMERY GI BILL SELECTED RESERVE; RESERVE EDUCATIONAL ASSISTANCE PROGRAM FEB2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "fy2012 benefits",
-                "fy2012 vba",
-                "vba",
-                "vba benefits",
-                "vba benefits by state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-113",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Ohio-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66432,45 +66412,49 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-113",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy2012 benefits",
+                "fy2012 vba",
+                "vba",
+                "vba benefits",
+                "vba benefits by state"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR 2012"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ohio-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://facilities.health.mil",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Non-Public access level is warranted because of the development of space and equipment requirements for construction contract/financial data aggreated in the system.  Knowledge of this information could possibly compromise contract negoiations.",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2013-01-01T05:00:00Z/2014-07-31T04:00:00Z",
-            "modified": "2024-08-26",
-            "keyword": [
-                "construction project management"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Gary Fischer",
                 "hasEmail": "mailto:Gary.Fischer@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-CFM-SEPS-11",
+            "dataQuality": true,
             "description": "<p>This planning application provides each Administration the ability to plan space and equipment schedules to meet new construction project schedules and to manage procurement schedules for the project.</p>",
-            "title": "Space and Equipment Planning System (SEPS)",
-            "programCode": [
-                "029:092"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66479,44 +66463,44 @@
                     "title": "Space and Equipment Planning System (SEPS)"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-CFM-SEPS-11",
+            "issued": "2017-07-26",
+            "keyword": [
+                "construction project management"
+            ],
+            "landingPage": "https://facilities.health.mil",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1D",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:092"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Non-Public access level is warranted because of the development of space and equipment requirements for construction contract/financial data aggreated in the system.  Knowledge of this information could possibly compromise contract negoiations.",
+            "temporal": "2013-01-01T05:00:00Z/2014-07-31T04:00:00Z",
             "theme": [
                 "Construction Project Management"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Space and Equipment Planning System (SEPS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/q58t-7ren",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-29",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 101"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/q58t-7ren",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to assist States and federally recognized tribal governments in the establishment, expansion, and improvement of veterans' cemeteries. Monetary assistance is provided under this program to establish, expand, and improve State or Tribal government veterans\u2019 cemeteries. Cemeteries must be State or Tribal Government owned and operated solely for the interment of eligible veterans and their dependents and/or spouses. Construction cost means the amount found necessary to convert a tract of land to an operational cemetery. The cemetery must be used solely for the interment of veterans, their wives, husbands, surviving spouses, minor children, and unmarried adult children who were physically or mentally disabled and incapable of self-support: section 38 CFR Part 38.620.</p>",
-            "title": "USA SPENDING C&P BURIAL B101 VETERANS CEMETARY GRANTS PROGRAM DEC2018",
-            "isPartOf": "d17c822a-717c-40ff-8fbe-3dcaefddb706",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66524,60 +66508,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/q58t-7ren/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/q58t-7ren/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/q58t-7ren/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/q58t-7ren/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/q58t-7ren/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/q58t-7ren/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/q58t-7ren/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/q58t-7ren/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/q58t-7ren/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/q58t-7ren",
+            "isPartOf": "d17c822a-717c-40ff-8fbe-3dcaefddb706",
+            "issued": "2019-03-29",
+            "keyword": [
+                "cfda 64 101"
+            ],
+            "landingPage": "https://www.data.va.gov/d/q58t-7ren",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING C&P BURIAL B101 VETERANS CEMETARY GRANTS PROGRAM DEC2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/q5qd-ak57",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "new york"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DG&amp;A Mailgroup",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-203",
             "description": "<p>This summary describes the programs and services VA provided in New York in fiscal year 2015.</p>",
-            "title": "State Summary: New York FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66586,42 +66570,40 @@
                     "title": "New York"
                 }
             ],
+            "identifier": "VA-OEI-OEI-203",
+            "issued": "2017-07-26",
+            "keyword": [
+                "new york"
+            ],
+            "landingPage": "https://www.data.va.gov/d/q5qd-ak57",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "State Summary: New York FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/q7gt-p562",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-02-01T05:00:00Z/2015-02-28T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "cars",
-                "establishments"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vikki Soukup",
                 "hasEmail": "mailto:Vikki.Soukup@va.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-130",
-            "description": "<p>Activity in terms of establishments and dispositions for CARS on a monthly basis</p>",
-            "title": "COIN 0022 CARS MONTHLY CRS TOTALS REPORT FEB 2015",
-            "programCode": [
-                "029:084"
-            ],
+            },
+            "description": "<p>Activity in terms of establishments and dispositions for CARS on a monthly basis</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66629,41 +66611,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-130",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cars",
+                "establishments"
+            ],
+            "landingPage": "https://www.data.va.gov/d/q7gt-p562",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-02-01T05:00:00Z/2015-02-28T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 0022 CARS MONTHLY CRS TOTALS REPORT FEB 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/q7k7-uy5k",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "montana",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-113",
             "description": "<p>This is a summary of the programs and services provided by VA in Montana in fiscal year 2014.</p>",
-            "title": "State Summary:  Montana",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66672,44 +66655,46 @@
                     "title": "State Summary:  Montana"
                 }
             ],
+            "identifier": "VA-OEI-OEI-113",
+            "issued": "2017-07-26",
+            "keyword": [
+                "montana",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/q7k7-uy5k",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "State Summary:  Montana"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/q82p-ts3d",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-20",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cdfa 64.124"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE D BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/q82p-ts3d",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE JAN2019",
-            "isPartOf": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66717,62 +66702,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/q82p-ts3d/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/q82p-ts3d/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/q82p-ts3d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/q82p-ts3d/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/q82p-ts3d/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/q82p-ts3d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/q82p-ts3d/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/q82p-ts3d/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/q82p-ts3d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/q82p-ts3d",
+            "isPartOf": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
+            "issued": "2019-03-20",
+            "keyword": [
+                "cdfa 64.124"
+            ],
+            "landingPage": "https://www.data.va.gov/d/q82p-ts3d",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE JAN2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/q9em-2jc5",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "9ccff3da-7bc1-401c-b2b6-fb1677425661",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Rhode Island FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66780,20 +66764,39 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "9ccff3da-7bc1-401c-b2b6-fb1677425661",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/q9em-2jc5",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary Rhode Island FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/qafi-qw8x",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>My HealtheVet (MHV) is VA's award-winning online Personal Health Record (PHR), located at <a href=\"http://www.myhealth.va.gov\">www.myhealth.va.gov</a>. The mission of MHV is to transform the  delivery of health and health care for all Veterans, independent of where they receive care, by providing one-stop, online access to better manage their overall health, make informed health decisions, and record and store important health and military history information. MHV provides access to VA health care and information 24/7 through web-based tools that empower Veterans to become active partners in their health care.  MHV registrants can click a 'Blue Button' on the website to view, print or download their available personal health information and military service information. They can choose to share that information with other providers, caregivers, family members or job advocates safely, securely, and privately.  Web technology combines essential health record information enhanced by online health resources. This enables and encourages patient/clinician collaboration. The online environment maps closely to existing clinical business practices and extends management and delivery of care.  MHV allows VA patients to request and receive VA prescription refills and provides a blended history of VA and self-entered medications.  Registrants whose personal identities have been verified as VA patients can receive copies of select VA electronic health records, including VA Appointments, Chemistry/Hematology Lab Results, Allergies and Wellness Reminders.  Many VA patients are communicating with their participating health care teams through Secure Messaging.</p>",
+            "identifier": "VA-VHA-OIA-012",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2004-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "health",
                 "healthy",
@@ -66803,60 +66806,40 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/qafi-qw8x",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-012",
-            "description": "<p>My HealtheVet (MHV) is VA's award-winning online Personal Health Record (PHR), located at <a href=\"http://www.myhealth.va.gov\">www.myhealth.va.gov</a>. The mission of MHV is to transform the  delivery of health and health care for all Veterans, independent of where they receive care, by providing one-stop, online access to better manage their overall health, make informed health decisions, and record and store important health and military history information. MHV provides access to VA health care and information 24/7 through web-based tools that empower Veterans to become active partners in their health care.  MHV registrants can click a 'Blue Button' on the website to view, print or download their available personal health information and military service information. They can choose to share that information with other providers, caregivers, family members or job advocates safely, securely, and privately.  Web technology combines essential health record information enhanced by online health resources. This enables and encourages patient/clinician collaboration. The online environment maps closely to existing clinical business practices and extends management and delivery of care.  MHV allows VA patients to request and receive VA prescription refills and provides a blended history of VA and self-entered medications.  Registrants whose personal identities have been verified as VA patients can receive copies of select VA electronic health records, including VA Appointments, Chemistry/Hematology Lab Results, Allergies and Wellness Reminders.  Many VA patients are communicating with their participating health care teams through Secure Messaging.</p>",
-            "title": "My HealtheVet (MHV)",
-            "programCode": [
-                "029:040"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "2004-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "My HealtheVet (MHV)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qavh-u6s3",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-02-01T05:00:00Z/2015-02-28T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "accounts receivable"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vikki Soukup",
                 "hasEmail": "mailto:Vikki.Soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-127",
             "description": "<p>aged accounts receivable</p>",
-            "title": "COIN 0017 CARS AGE PROFILE REPORT FEB 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66864,26 +66847,55 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-127",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accounts receivable"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qavh-u6s3",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-02-01T05:00:00Z/2015-02-28T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 0017 CARS AGE PROFILE REPORT FEB 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "accrualPeriodicity": "R/P2M",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-05-15T04:00:00Z/2014-05-15T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/docs/VAAccessAuditFindingsReport.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/access-audit.asp",
+            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/health/docs/VAMCPatientAccessData06092014.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "June 9, 2014"
+                }
             ],
+            "identifier": "VA-VHA-OIA-056",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -66897,70 +66909,42 @@
                 "wait list",
                 "wait time"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-056",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.</p>",
-            "title": "Accelerating Access to Care Initiative - Report 2014 June 9",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VAMCPatientAccessData06092014.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "June 9, 2014"
-                }
+            "references": [
+                "https://www.va.gov/health/docs/VAAccessAuditFindingsReport.pdf"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2014-05-15T04:00:00Z/2014-05-15T04:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative - Report 2014 June 9"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qcqc-r7e4",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 120"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/qcqc-r7e4",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH32 B120 POST-VIETNAM ERA VETERANS' EDUCATIONAL ASSISTANCE DEC2018",
-            "isPartOf": "556ed405-3a6a-44b5-9911-7ce62cff5edf",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66968,40 +66952,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qcqc-r7e4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qcqc-r7e4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qcqc-r7e4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/qcqc-r7e4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qcqc-r7e4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qcqc-r7e4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qcqc-r7e4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qcqc-r7e4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qcqc-r7e4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/qcqc-r7e4",
+            "isPartOf": "556ed405-3a6a-44b5-9911-7ce62cff5edf",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 120"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qcqc-r7e4",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "USA SPENDING EDUCATION CH32 B120 POST-VIETNAM ERA VETERANS' EDUCATIONAL ASSISTANCE DEC2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Monica Reyes",
+                "hasEmail": "mailto:monica.reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Vocational Rehabilitation for Vietnam Veterans Children with Spina Bifida or other covered Birth Defects- February 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING122013-042",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-02-01T05:00:00Z/2014-02-28T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "birth defects",
                 "cfda 64 128",
@@ -67011,56 +67017,37 @@
                 "vocational rehabilatition for vietnam veterans children",
                 "vocational rehabilitation service"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:monica.reyes@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING122013-042",
-            "description": "<p>USA Spending- Vocational Rehabilitation for Vietnam Veterans Children with Spina Bifida or other covered Birth Defects- February 2013.</p>",
-            "title": "USA Spending file- Vocational Rehabilitation for Vietnam Veterans Children with Spina Bifida or other covered Birth Defects 02/2014-  CFDA 64.128",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014-02-01T05:00:00Z/2014-02-28T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- Vocational Rehabilitation for Vietnam Veterans Children with Spina Bifida or other covered Birth Defects 02/2014-  CFDA 64.128"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/qdi3-xeuk",
-            "issued": "2024-08-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-05",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VACONCVAS",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/qdi3-xeuk",
             "description": "VetPop2020 projections by Gender, Race, and Ethnicity from 2020 to 2050.",
-            "title": "VetPop2020_GenderRaceEthnicity",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67068,58 +67055,54 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qdi3-xeuk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qdi3-xeuk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qdi3-xeuk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/qdi3-xeuk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qdi3-xeuk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qdi3-xeuk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qdi3-xeuk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qdi3-xeuk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qdi3-xeuk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/qdi3-xeuk",
+            "issued": "2024-08-01",
+            "landingPage": "https://www.data.va.gov/d/qdi3-xeuk",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2020_GenderRaceEthnicity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qdm6-5qif",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2023-03-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-21",
-            "keyword": [
-                "pension",
-                "veterans",
-                "veterans surviving spouses and children"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alysia Blake",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/qdm6-5qif",
+            "dataQuality": true,
             "description": "All Survivors Pension Recipients by Age, FY2022. Surviving spouses and dependent children of deceased wartime Veterans are eligible for monthly pension benefits if they meet the net worth and income requirements.",
-            "title": "All Survivors Pension Recipients by Age, FY2022",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67127,40 +67110,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qdm6-5qif/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qdm6-5qif/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qdm6-5qif/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/qdm6-5qif/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qdm6-5qif/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qdm6-5qif/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qdm6-5qif/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qdm6-5qif/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qdm6-5qif/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/qdm6-5qif",
+            "issued": "2023-03-21",
+            "keyword": [
+                "pension",
+                "veterans",
+                "veterans surviving spouses and children"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qdm6-5qif",
             "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
-            "dataQuality": true
+            "modified": "2023-03-21",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "All Survivors Pension Recipients by Age, FY2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qdmv-d6vu",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.hsrd.research.va.gov/for_researchers/cyber_seminars/archives/video_archive.cfm?SessionID=1080",
+            "description": "<p>The Influence of Concussion on Persistent Post-Concussive Emotional, Somatic, &amp; Neurocognitive Symptoms: Implications for Assessment &amp; Treatment in Veterans based on whether the recency and number of lifetime concussions had a sustained impact on emotional, somatic, and cognitive functioning in a sample of U.S. Marines, accounting for deployment stress and symptoms of depression and PTSD.  This dataset is no longer supported and is provided as-is. Any historical knowledge regarding meta data or it's creation is no longer available.  All known information is proved as part of this data set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/qdmv-d6vu/text/plain",
+                    "mediaType": "text/plain"
+                }
+            ],
+            "identifier": "VA-VHA-PCS-018",
+            "isPartOf": "VA-VHA-PCS-020",
             "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-29",
             "keyword": [
                 "concussion",
                 "depression",
@@ -67171,130 +67184,101 @@
                 "veteran",
                 "vha"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/qdmv-d6vu",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-06-29",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-PCS-018",
-            "description": "<p>The Influence of Concussion on Persistent Post-Concussive Emotional, Somatic, &amp; Neurocognitive Symptoms: Implications for Assessment &amp; Treatment in Veterans based on whether the recency and number of lifetime concussions had a sustained impact on emotional, somatic, and cognitive functioning in a sample of U.S. Marines, accounting for deployment stress and symptoms of depression and PTSD.  This dataset is no longer supported and is provided as-is. Any historical knowledge regarding meta data or it's creation is no longer available.  All known information is proved as part of this data set.</p>",
-            "title": "Mild TBI Diagnosis and Management Strategies: Implications for Assessment & Treatment in Veterans",
-            "isPartOf": "VA-VHA-PCS-020",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/qdmv-d6vu/text/plain",
-                    "mediaType": "text/plain"
-                }
-            ],
-            "describedBy": "https://www.hsrd.research.va.gov/for_researchers/cyber_seminars/archives/video_archive.cfm?SessionID=1080",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "Mild TBI"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Mild TBI Diagnosis and Management Strategies: Implications for Assessment & Treatment in Veterans"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/qdn9-iqeh",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-12-09",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-13",
-            "keyword": [
-                "health",
-                "health provider",
-                "hospital",
-                "nutrition",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/qdn9-iqeh",
-            "description": "National Center for Health Statistics (NCHS) population health survey data have been linked to VA administrative data containing information on military service history and VA benefit program utilization. The linked data can provide information on the health status and access to health care for VA program beneficiaries. In addition, researchers can compare the health of Veterans within and outside the VA health care system and compare Veterans to non-Veterans in the civilian non-institutionalized U.S. population. \n\nDue to confidentiality requirements, the Restricted-use NCHS-VA Linked Data Files are accessible only through the NCHS Research Data Center (RDC) Network. All interested researchers must submit a research proposal to the RDC.  Please see the NCHS RDC website (https://www.cdc.gov/rdc/index.htm) for instructions on submitting a proposal.",
-            "title": "Restricted-Use NCHS-VA Linked Data Files",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "National Center for Health Statistics (NCHS) population health survey data have been linked to VA administrative data containing information on military service history and VA benefit program utilization. The linked data can provide information on the health status and access to health care for VA program beneficiaries. In addition, researchers can compare the health of Veterans within and outside the VA health care system and compare Veterans to non-Veterans in the civilian non-institutionalized U.S. population. \n\nDue to confidentiality requirements, the Restricted-use NCHS-VA Linked Data Files are accessible only through the NCHS Research Data Center (RDC) Network. All interested researchers must submit a research proposal to the RDC.  Please see the NCHS RDC website (https://www.cdc.gov/rdc/index.htm) for instructions on submitting a proposal.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/nchs/data-linkage/va-restricted.htm",
-                    "description": "Through its data linkage program, the National Center for Health Statistics (NCHS) has been able to expand the analytic utility of the data collected from the National Health Interview Survey (NHIS) and the National Health and Nutrition Examination Survey (NHANES) by augmenting the data with administrative data from the Department of Veterans Affairs (VA). \n\nNHIS and NHANES have been linked to VA administrative data containing information on details of active-duty service in the United States uniformed services (such as branch of service, and era of active-duty service) and VA benefit program utilization including VA health care, service-connected disability compensation, pension, VA guaranteed home loan program, life insurance, education, training, and veteran readiness (vocational rehabilitation), and employment benefit programs.",
                     "@type": "dcat:Distribution",
+                    "description": "Through its data linkage program, the National Center for Health Statistics (NCHS) has been able to expand the analytic utility of the data collected from the National Health Interview Survey (NHIS) and the National Health and Nutrition Examination Survey (NHANES) by augmenting the data with administrative data from the Department of Veterans Affairs (VA). \n\nNHIS and NHANES have been linked to VA administrative data containing information on details of active-duty service in the United States uniformed services (such as branch of service, and era of active-duty service) and VA benefit program utilization including VA health care, service-connected disability compensation, pension, VA guaranteed home loan program, life insurance, education, training, and veteran readiness (vocational rehabilitation), and employment benefit programs.",
+                    "downloadURL": "https://www.cdc.gov/nchs/data-linkage/va-restricted.htm",
+                    "mediaType": "text/html",
                     "title": "Restricted-Use NCHS-VA Data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.cdc.gov/nchs/data/datalinkage/NCHS-VA-Linked-Data-Methodology-and-Analytic-Considerations.pdf",
-                    "description": "Through its data linkage program, the National Center for Health Statistics (NCHS) has been able to expand the analytic utility of the data collected from the National Health Interview Survey (NHIS) and the National Health and Nutrition Examination Survey (NHANES) by augmenting the data with administrative data from the Department of Veterans Affairs (VA). \n\nNHIS and NHANES have been linked to VA administrative data containing information on details of active-duty service in the United States uniformed services (such as branch of service, and era of active-duty service) and VA benefit program utilization including VA health care, service-connected disability compensation, pension, VA guaranteed home loan program, life insurance, education, training, and veteran readiness (vocational rehabilitation), and employment benefit programs.",
                     "@type": "dcat:Distribution",
+                    "description": "Through its data linkage program, the National Center for Health Statistics (NCHS) has been able to expand the analytic utility of the data collected from the National Health Interview Survey (NHIS) and the National Health and Nutrition Examination Survey (NHANES) by augmenting the data with administrative data from the Department of Veterans Affairs (VA). \n\nNHIS and NHANES have been linked to VA administrative data containing information on details of active-duty service in the United States uniformed services (such as branch of service, and era of active-duty service) and VA benefit program utilization including VA health care, service-connected disability compensation, pension, VA guaranteed home loan program, life insurance, education, training, and veteran readiness (vocational rehabilitation), and employment benefit programs.",
+                    "downloadURL": "https://www.cdc.gov/nchs/data/datalinkage/NCHS-VA-Linked-Data-Methodology-and-Analytic-Considerations.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Restricted-Use NCHS-VA Data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/nchs/data-linkage/nhcs-va.htm",
-                    "description": "Through its data linkage program, the National Center for Health Statistics (NCHS) has been able to expand the analytic utility of the data collected from the National Hospital Care Survey (NHCS) by augmenting it with administrative data from the Department of Veterans Affairs (VA).\n\nNHCS data have been linked to VA administrative data containing information on details of active-duty service in the United States uniformed services (such as branch of service and era of active-duty service) and VA benefit program utilization including VA health care, service-connected disability compensation, pension, VA guaranteed home loan program, life insurance, education, training and veteran readiness (vocational rehabilitation), and employment benefit programs.\n\nVA administrative records are available for patient records in the NHCS for which NCHS was able to match with VA administrative records. VA provided NCHS with administrative data for all successfully matched patient records.",
                     "@type": "dcat:Distribution",
+                    "description": "Through its data linkage program, the National Center for Health Statistics (NCHS) has been able to expand the analytic utility of the data collected from the National Hospital Care Survey (NHCS) by augmenting it with administrative data from the Department of Veterans Affairs (VA).\n\nNHCS data have been linked to VA administrative data containing information on details of active-duty service in the United States uniformed services (such as branch of service and era of active-duty service) and VA benefit program utilization including VA health care, service-connected disability compensation, pension, VA guaranteed home loan program, life insurance, education, training and veteran readiness (vocational rehabilitation), and employment benefit programs.\n\nVA administrative records are available for patient records in the NHCS for which NCHS was able to match with VA administrative records. VA provided NCHS with administrative data for all successfully matched patient records.",
+                    "downloadURL": "https://www.cdc.gov/nchs/data-linkage/nhcs-va.htm",
+                    "mediaType": "text/html",
                     "title": "Restricted-Use Linked NHCS\u2013VA Administrative Data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.cdc.gov/nchs/data/datalinkage/NHCS-VA-Linkage-Methods-and-Analytic-Considerations.pdf",
-                    "description": "Through its data linkage program, the National Center for Health Statistics (NCHS) has been able to expand the analytic utility of the data collected from the National Hospital Care Survey (NHCS) by augmenting it with administrative data from the Department of Veterans Affairs (VA).\n\nNHCS data have been linked to VA administrative data containing information on details of active-duty service in the United States uniformed services (such as branch of service and era of active-duty service) and VA benefit program utilization including VA health care, service-connected disability compensation, pension, VA guaranteed home loan program, life insurance, education, training and veteran readiness (vocational rehabilitation), and employment benefit programs.\n\nVA administrative records are available for patient records in the NHCS for which NCHS was able to match with VA administrative records. VA provided NCHS with administrative data for all successfully matched patient records.",
                     "@type": "dcat:Distribution",
+                    "description": "Through its data linkage program, the National Center for Health Statistics (NCHS) has been able to expand the analytic utility of the data collected from the National Hospital Care Survey (NHCS) by augmenting it with administrative data from the Department of Veterans Affairs (VA).\n\nNHCS data have been linked to VA administrative data containing information on details of active-duty service in the United States uniformed services (such as branch of service and era of active-duty service) and VA benefit program utilization including VA health care, service-connected disability compensation, pension, VA guaranteed home loan program, life insurance, education, training and veteran readiness (vocational rehabilitation), and employment benefit programs.\n\nVA administrative records are available for patient records in the NHCS for which NCHS was able to match with VA administrative records. VA provided NCHS with administrative data for all successfully matched patient records.",
+                    "downloadURL": "https://www.cdc.gov/nchs/data/datalinkage/NHCS-VA-Linkage-Methods-and-Analytic-Considerations.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Restricted-Use Linked NHCS\u2013VA Administrative Data"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/qdn9-iqeh",
+            "issued": "2022-12-09",
+            "keyword": [
+                "health",
+                "health provider",
+                "hospital",
+                "nutrition",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qdn9-iqeh",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-12-13",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Restricted-Use NCHS-VA Linked Data Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qe8f-4cyi",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 118"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/qe8f-4cyi",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide veterans who are eligible for a Specially Adapted Housing grant with loan directly from the VA in certain circumstances. Permanently and totally disabled Veterans who served on active duty on or after September 16, 1940 and are eligible for a Specially Adapted Housing grant. VA may make loans up to $33,000 to eligible applicants if (a) the veteran is eligible for a VA Specially Adapted Housing grant, and (b) a loan is necessary to supplement the grant, and (c) home loans from a private lender are not available in the area where the property involved is located</p>",
-            "title": "USA SPENDING LGY B118 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS DEC2018",
-            "isPartOf": "7d0e269c-91a6-4b56-9c6a-68d0e7617aab",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67302,62 +67286,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qe8f-4cyi/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qe8f-4cyi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qe8f-4cyi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/qe8f-4cyi/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qe8f-4cyi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qe8f-4cyi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qe8f-4cyi/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qe8f-4cyi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qe8f-4cyi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/qe8f-4cyi",
+            "isPartOf": "7d0e269c-91a6-4b56-9c6a-68d0e7617aab",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 118"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qe8f-4cyi",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING LGY B118 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS DEC2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qede-ap5d",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-07",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "veterans farmer"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tamara Lee",
                 "hasEmail": "mailto:tamara.lee@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/qede-ap5d",
-            "description": "<p>These spreadsheets contain the percent of Veteran farmers and dairymen  by county for the state of California.</p>",
-            "title": "Veteran Farmer Age",
-            "isPartOf": "64971372-40a2-4207-937c-892283f391ba",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/data/VAOpenDataMigration2019/Data-Dictionary-Apps-for-Ag.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>These spreadsheets contain the percent of Veteran farmers and dairymen  by county for the state of California.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67365,46 +67350,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qede-ap5d/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qede-ap5d/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qede-ap5d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/qede-ap5d/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qede-ap5d/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qede-ap5d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qede-ap5d/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qede-ap5d/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qede-ap5d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/data/VAOpenDataMigration2019/Data-Dictionary-Apps-for-Ag.pdf",
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/qede-ap5d",
+            "isPartOf": "64971372-40a2-4207-937c-892283f391ba",
+            "issued": "2017-07-07",
+            "keyword": [
+                "veterans farmer"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qede-ap5d",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "Veteran Farmer Age"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "accrualPeriodicity": "R/P2W",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/access-audit.asp",
+            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/December_2014_Completed_Access_Data_using_Preferred_Date_020515.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Completed Access Data Using Preferred Date 2015-02-05"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-072",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2014-12-31T05:00:00Z/2014-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -67418,55 +67433,43 @@
                 "wait list",
                 "wait time"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-072",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Feb 5",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/December_2014_Completed_Access_Data_using_Preferred_Date_020515.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Completed Access Data Using Preferred Date 2015-02-05"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2014-12-31T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Feb 5"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/HospitalReportCard.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/HospitalReportCard.asp",
+            "description": "<p>Veterans Health Administration 2010 Facility Quality and Safety Report</p>",
+            "identifier": "VA-VHA-OIA-584",
             "issued": "2017-07-26",
-            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
-            "references": [
-                "https://www.va.gov/health/HospitalReportCard.asp"
-            ],
             "keyword": [
                 "ambulatory",
                 "care",
@@ -67489,56 +67492,42 @@
                 "urban",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.va.gov/health/HospitalReportCard.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-584",
-            "description": "<p>Veterans Health Administration 2010 Facility Quality and Safety Report</p>",
-            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report",
-            "programCode": [
-                "029:040"
+            "references": [
+                "https://www.va.gov/health/HospitalReportCard.asp"
             ],
-            "describedBy": "https://www.va.gov/health/HospitalReportCard.asp",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
             "theme": [
                 "2010 Facility Quality and Safety Report"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qhqa-74yq",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-08-02",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-24",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/qhqa-74yq",
+            "dataQuality": true,
             "description": "The Geographic Distribution of VA Expenditures (GDX) is an annual report that shows estimated VA expenditures for major programmatic areas by geographic area (state, county, and congressional district). The major programmatic areas are: Compensation and Pension; Readjustment (Education) and Vocational Rehabilitation; Insurance; Construction; and, Medical and Administrative.",
-            "title": "GDX FY21",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67546,41 +67535,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qhqa-74yq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qhqa-74yq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qhqa-74yq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/qhqa-74yq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qhqa-74yq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qhqa-74yq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qhqa-74yq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qhqa-74yq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qhqa-74yq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/qhqa-74yq",
+            "issued": "2022-08-02",
+            "landingPage": "https://www.data.va.gov/d/qhqa-74yq",
             "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2023-04-24",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "GDX FY21"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Dusca Fichtel",
+                "hasEmail": "mailto:Dusca.Fichtel@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Face Amount of New Life Insurance Policies Issued- December 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING122013-011",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 030",
                 "face amount",
@@ -67589,60 +67595,37 @@
                 "new life insurance policies",
                 "usa spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Dusca Fichtel",
-                "hasEmail": "mailto:Dusca.Fichtel@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING122013-011",
-            "description": "<p>USA Spending- Face Amount of New Life Insurance Policies Issued- December 2013.</p>",
-            "title": "USA Spending file- New Life Insurance Policies-Insurance -  CFDA 64.030",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- New Life Insurance Policies-Insurance -  CFDA 64.030"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qivt-xswz",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "coin",
-                "finance"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vicki Soukup",
                 "hasEmail": "mailto:vicki.soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "OM-OM-172",
             "description": "<p>COIN Report 0017 February 2016</p>",
-            "title": "COIN 0017 Feb 2016",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67650,22 +67633,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "OM-OM-172",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qivt-xswz",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Finance"
-            ]
+            ],
+            "title": "COIN 0017 Feb 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/qj2m-5y96",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Research and Development Information System (RDIS) is the Veterans Affairs Central Office budgetary and project data repository for managing the VA Research and Development Program. The RDIS contains data collected from Veterans Affairs Medical Centers (VAMCs) on all VA research projects. It stores information on VAMC investigators, project budget allocations and expenditures, initial project abstracts, progress reports and research space. VA Medical Centers collect and submit the data using an application called electronic Project Management and Information System (ePROMISE). That data is submitted to Veterans Affairs Central Office and becomes a component of RDIS. ePROMISE collects data from over 150 VA facilities (including 75 VAMCs). VA funded, non-VA funded and non-funded research proposals are reviewed and must be approved by the Research and Development (R&amp;D) Committee and relevant R&amp;D Subcommittees (Human Studies, Animal Use, and/or Biosafety) at each VAMC. Basic information on research projects approved by the VAMC Research and Development committee is transmitted to the RDIS, which tracks the life cycle of these projects.</p>",
+            "identifier": "VA-VHA-ORD-001",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1993-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "animal",
                 "budget",
@@ -67678,60 +67681,41 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/qj2m-5y96",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:048"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-ORD-001",
-            "description": "<p>The Research and Development Information System (RDIS) is the Veterans Affairs Central Office budgetary and project data repository for managing the VA Research and Development Program. The RDIS contains data collected from Veterans Affairs Medical Centers (VAMCs) on all VA research projects. It stores information on VAMC investigators, project budget allocations and expenditures, initial project abstracts, progress reports and research space. VA Medical Centers collect and submit the data using an application called electronic Project Management and Information System (ePROMISE). That data is submitted to Veterans Affairs Central Office and becomes a component of RDIS. ePROMISE collects data from over 150 VA facilities (including 75 VAMCs). VA funded, non-VA funded and non-funded research proposals are reviewed and must be approved by the Research and Development (R&amp;D) Committee and relevant R&amp;D Subcommittees (Human Studies, Animal Use, and/or Biosafety) at each VAMC. Basic information on research projects approved by the VAMC Research and Development committee is transmitted to the RDIS, which tracks the life cycle of these projects.</p>",
-            "title": "Research and Development Information System (RDIS)",
-            "programCode": [
-                "029:048"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "1993-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Research and Development Information System (RDIS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qma2-95cf",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "9737a278-271b-4b80-9d26-d2b604050503",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Kentucky FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67739,25 +67723,45 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "9737a278-271b-4b80-9d26-d2b604050503",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qma2-95cf",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data",
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "State Summary Kentucky FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qmjb-6xsx",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for PTSD",
+                "hasEmail": "mailto:ncptsd@va.gov"
+            },
+            "description": "Check this story often to see a chronological list of important edits, new data, recently published data stories and more.",
+            "identifier": "https://www.data.va.gov/api/views/qmjb-6xsx",
             "issued": "2021-11-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-04",
             "keyword": [
                 "edit",
                 "ncptsd",
@@ -67767,93 +67771,72 @@
                 "repository",
                 "update"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for PTSD",
-                "hasEmail": "mailto:ncptsd@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/qmjb-6xsx",
+            "modified": "2024-09-04",
+            "programCode": [
+                "029:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for PTSD"
             },
-            "identifier": "https://www.data.va.gov/api/views/qmjb-6xsx",
-            "description": "Check this story often to see a chronological list of important edits, new data, recently published data stories and more.",
-            "title": "What's new in the PTSD Repository data?",
-            "programCode": [
-                "029:000"
-            ],
-            "accrualPeriodicity": "R/P1Y"
+            "rights": "All data is within the public domain and is currently available for download.",
+            "title": "What's new in the PTSD Repository data?"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Monica Reyes",
+                "hasEmail": "mailto:monica.reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Vocational Rehabilitation for Disabled Veterans - Chapter 31- December 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING122013-009",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 116",
                 "usa spending",
                 "vocational rehabilitant for disabled veterans",
                 "vocational rehabilitation service"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:monica.reyes@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING122013-009",
-            "description": "<p>USA Spending- Vocational Rehabilitation for Disabled Veterans - Chapter 31- December 2013.</p>",
-            "title": "USA Spending file- Vocational Rehabilitation for Disabled Veterans-  CFDA 64.116",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- Vocational Rehabilitation for Disabled Veterans-  CFDA 64.116"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qmzk-bycf",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "service members",
-                "women"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
-                "fn": "NCVAS Mailbox",
-                "hasEmail": "mailto:vancvas@va.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
+                "fn": "NCVAS Mailbox",
+                "hasEmail": "mailto:vancvas@va.gov"
             },
-            "identifier": "VA-OEI-OEI-223",
             "description": "<p>Dataset shows Women Service Members by Total, Officer and Enlisted</p>",
-            "title": "Women Service Members by Total, Officer and Enlisted",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67861,44 +67844,41 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
+            "identifier": "VA-OEI-OEI-223",
+            "issued": "2017-07-26",
+            "keyword": [
+                "service members",
+                "women"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qmzk-bycf",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Demographics"
-            ]
+            ],
+            "title": "Women Service Members by Total, Officer and Enlisted"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qn4p-smud",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-05-24",
-            "temporal": "2005-10-01T04:00:00Z/2009-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "acute pancreatitis",
-                "drug treatment",
-                "dyslipidemia",
-                "hydroxymethylglutaryl-coa reductase inhibitors (statins)",
-                "research",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Open Data",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "1edcf5e7-7d20-4f1e-8970-91ed05e9bc0f",
+            "dataQuality": true,
+            "describedBy": "https://www.data.va.gov/dataset/hypertriglyceridemia-pancreatitis-vha/resource/515281e1-5b09-4925-b478-2fa9f2e27ce7",
             "description": "<p>Person-level clinical data on patients admitted for acute pancreatitis Oct 2005-Sep 2009 in Veterans Health Administration hospitals.</p>",
-            "title": "Hypertriglyceridemia-Pancreatitis-VHA",
-            "programCode": [
-                "029:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67906,46 +67886,50 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "describedBy": "https://www.data.va.gov/dataset/hypertriglyceridemia-pancreatitis-vha/resource/515281e1-5b09-4925-b478-2fa9f2e27ce7",
-            "dataQuality": true,
+            "identifier": "1edcf5e7-7d20-4f1e-8970-91ed05e9bc0f",
+            "issued": "2017-05-24",
+            "keyword": [
+                "acute pancreatitis",
+                "drug treatment",
+                "dyslipidemia",
+                "hydroxymethylglutaryl-coa reductase inhibitors (statins)",
+                "research",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qn4p-smud",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2005-10-01T04:00:00Z/2009-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Hypertriglyceridemia-Pancreatitis-VHA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qpj7-ahid",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 109"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/qpj7-ahid",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to compensate veterans for disabilities incurred or aggravated during military service according to the average impairment in earning capacity such disability would cause in civilian occupations. Persons who have suffered disabilities resulting from service in the Armed Forces of the United States. The disability must have been incurred or aggravated by service in the line of duty. Separation from service must have been under other than dishonorable conditions for the period in which the disability was incurred or aggravated.</p>",
-            "title": "USA SPENDING C&P B109 VETERANS COMPENSATION FOR SERVICE-CONNECTED DISABILITY DEC2018",
-            "isPartOf": "6013cae5-a8c2-47ff-9c90-9cbdba7bda63",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67953,60 +67937,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qpj7-ahid/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qpj7-ahid/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qpj7-ahid/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/qpj7-ahid/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qpj7-ahid/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qpj7-ahid/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qpj7-ahid/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qpj7-ahid/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qpj7-ahid/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/qpj7-ahid",
+            "isPartOf": "6013cae5-a8c2-47ff-9c90-9cbdba7bda63",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 109"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qpj7-ahid",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING C&P B109 VETERANS COMPENSATION FOR SERVICE-CONNECTED DISABILITY DEC2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qs7t-mcjy",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2018-03-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-19",
-            "keyword": [
-                "equitable relief report"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sharon Weiner",
                 "hasEmail": "mailto:Sharon.Weiner@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "dataQuality": true,
             "description": "<p>Equitable Relief Reports as submitted to Congress</p>",
-            "title": "Equitable Relief Reports 2006",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68014,46 +68000,44 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "issued": "2018-03-19",
+            "keyword": [
+                "equitable relief report"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qs7t-mcjy",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-11-19",
+            "programCode": [
+                "029:083"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Equitable Relief Reports 2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qsid-6be8",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "e63384f2-479d-47bc-afc5-6a98191160cc",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Georgia FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68061,44 +68045,42 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "e63384f2-479d-47bc-afc5-6a98191160cc",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qsid-6be8",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data",
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "State Summary Georgia FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qsrq-sfv8",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-10-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-21",
-            "keyword": [
-                "korean war",
-                "vietnam war",
-                "world war ii"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center of Veterans Analytics Services",
                 "hasEmail": "mailto:VACONCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/qsrq-sfv8",
             "description": "",
-            "title": "Multiple War Veterans",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68106,59 +68088,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qsrq-sfv8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qsrq-sfv8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qsrq-sfv8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/qsrq-sfv8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qsrq-sfv8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qsrq-sfv8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qsrq-sfv8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qsrq-sfv8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qsrq-sfv8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/qsrq-sfv8",
+            "issued": "2024-10-01",
+            "keyword": [
+                "korean war",
+                "vietnam war",
+                "world war ii"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qsrq-sfv8",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-10-21",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Multiple War Veterans"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qt92-j4n8",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "health",
-                "minority",
-                "socioeconomic",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-197",
             "description": "<p>This report uses data from the 2014 American Community Survey Public Use Microdata Sample to report data concerning the demographics, socioeconomic status, and health charactristics of Minority Veterans. It also compares major characteristics between Minority Veterans and Minority non-Veterans.</p>",
-            "title": "2014 Minority Veterans Report",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68167,44 +68148,46 @@
                     "title": "2014 Minority Veterans Report"
                 }
             ],
+            "identifier": "VA-OEI-OEI-197",
+            "issued": "2017-07-26",
+            "keyword": [
+                "health",
+                "minority",
+                "socioeconomic",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qt92-j4n8",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2014 Minority Veterans Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qtcw-pdce",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "coin",
-                "finance"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vicki Soukup",
                 "hasEmail": "mailto:vicki.soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "OM-OM-173",
             "description": "<p>COIN report 0022 Feb 2016</p>",
-            "title": "COIN 0022 Feb 2016",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68212,37 +68195,41 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "OM-OM-173",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qtcw-pdce",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 0022 Feb 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/qtej-kj9a",
-            "issued": "2024-07-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-29",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/qtej-kj9a",
             "description": "",
-            "title": "Income Distribution of Veterans by Gender",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68250,86 +68237,82 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qtej-kj9a/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qtej-kj9a/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qtej-kj9a/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/qtej-kj9a/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qtej-kj9a/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qtej-kj9a/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qtej-kj9a/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qtej-kj9a/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qtej-kj9a/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/qtej-kj9a",
+            "issued": "2024-07-29",
+            "landingPage": "https://www.data.va.gov/d/qtej-kj9a",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-07-29",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Income Distribution of Veterans by Gender"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/qtzp-vapu",
-            "issued": "2024-10-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "veterans day"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/qtzp-vapu",
             "description": "On this Veterans Day 2024, the Department of Veterans Affairs (VA) honors the loyalty and service of all Veterans. This data story highlights Veterans' legacy and commitment.",
-            "title": "Veterans Day 2024 - Loyalty and Service by All Who Served",
+            "identifier": "https://www.data.va.gov/api/views/qtzp-vapu",
+            "issued": "2024-10-01",
+            "keyword": [
+                "veterans day"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qtzp-vapu",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-11-04",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Day 2024 - Loyalty and Service by All Who Served"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/queu-kuys",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-07-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-10",
-            "keyword": [
-                "veterans",
-                "women veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/queu-kuys",
             "description": "",
-            "title": "Employment Status of Women Veterans by Age",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68337,57 +68320,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/queu-kuys/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/queu-kuys/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/queu-kuys/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/queu-kuys/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/queu-kuys/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/queu-kuys/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/queu-kuys/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/queu-kuys/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/queu-kuys/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/queu-kuys",
+            "issued": "2024-07-31",
+            "keyword": [
+                "veterans",
+                "women veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/queu-kuys",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-12-10",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Employment Status of Women Veterans by Age"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qura-phyh",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "business expanding establishments",
-                "cars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vicki Soukup",
                 "hasEmail": "mailto:vicki.soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-161",
             "description": "<p>CARS Monthly Totals, Part I - 9/30/2015; Activity in terms of establishments and dispositions for CARS on a monthly basis</p>",
-            "title": "COIN 0022 CARS Monthly Totals, Part I - 9/30/2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68395,46 +68378,40 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-161",
+            "issued": "2017-07-26",
+            "keyword": [
+                "business expanding establishments",
+                "cars"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qura-phyh",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "financial"
-            ]
+            ],
+            "title": "COIN 0022 CARS Monthly Totals, Part I - 9/30/2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/PolicyholdersbyStatebyProgramDecember2012.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-12-01T05:00:00Z/2012-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotes_Policyholders_by_Program_December_2012.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "county",
-                "insurance",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2012-017",
+            "dataQuality": true,
             "description": "<p>Number of life insurance policyholders for each administered life insurance program listed by state. Data is current as of 12/31/12.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "Provides number of life insurance policyholders for each program by state as of 12/31/12.",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68442,47 +68419,83 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/quz3-63ng/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/quz3-63ng/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/quz3-63ng/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/quz3-63ng/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/quz3-63ng/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/quz3-63ng/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/quz3-63ng/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/quz3-63ng/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/quz3-63ng/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-017",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "county",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/PolicyholdersbyStatebyProgramDecember2012.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotes_Policyholders_by_Program_December_2012.doc"
+            ],
+            "temporal": "2012-12-01T05:00:00Z/2012-12-31T05:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
-            ],
-            "language": [
-                "en-US"
-            ]
+            ],
+            "title": "Provides number of life insurance policyholders for each program by state as of 12/31/12."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/story/department-veterans-affairs-opioid-prescribing-data",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/opa/pressrel/pressrelease.cfm?id=3997",
+            "description": "<p>The posted information shows opioid-dispensing rates for each facility and how those rates have changed over time. It is important to note that because the needs and conditions of Veterans may be different at each facility, the rates of the use of opioids may also be different for that reason, and cannot be compared directly.  This information will be updated periodically.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/qvgv-ry3b/text/plain",
+                    "mediaType": "text/plain"
+                }
+            ],
+            "identifier": "f6c6f564-8c37-4e30-8e99-8e4a7d9d66f8",
             "issued": "2018-03-02",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
             "keyword": [
                 "chronic",
                 "dispencing",
@@ -68501,50 +68514,41 @@
                 "va pharmacy",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/story/department-veterans-affairs-opioid-prescribing-data",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "f6c6f564-8c37-4e30-8e99-8e4a7d9d66f8",
-            "description": "<p>The posted information shows opioid-dispensing rates for each facility and how those rates have changed over time. It is important to note that because the needs and conditions of Veterans may be different at each facility, the rates of the use of opioids may also be different for that reason, and cannot be compared directly.  This information will be updated periodically.</p>",
-            "title": "Department of Veterans Affairs Opioid Dispensing Data",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/qvgv-ry3b/text/plain",
-                    "mediaType": "text/plain"
-                }
-            ],
-            "describedBy": "https://www.va.gov/opa/pressrel/pressrelease.cfm?id=3997",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Opioid Dispensing Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qvh3-ya5b",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for PTSD",
+                "hasEmail": "mailto:ncptsd@va.gov"
+            },
+            "description": "This story outlines the organization scheme for the PTSD Repository dataset and coding rules--decisions made about variables and response items.",
+            "identifier": "https://www.data.va.gov/api/views/qvh3-ya5b",
             "issued": "2020-06-12",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-11",
             "keyword": [
                 "coding decision",
                 "coding rule",
@@ -68554,33 +68558,42 @@
                 "table",
                 "variable list"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for PTSD",
-                "hasEmail": "mailto:ncptsd@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/qvh3-ya5b",
+            "modified": "2020-06-11",
+            "programCode": [
+                "029:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for PTSD"
             },
-            "identifier": "https://www.data.va.gov/api/views/qvh3-ya5b",
-            "description": "This story outlines the organization scheme for the PTSD Repository dataset and coding rules--decisions made about variables and response items.",
-            "title": "How are the data organized?",
-            "programCode": [
-                "029:000"
-            ],
-            "accrualPeriodicity": "R/P1Y"
+            "rights": "All data is within the public domain and is currently available for download.",
+            "title": "How are the data organized?"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/Expenditures.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Andrew Bickel",
+                "hasEmail": "mailto:andrew.bickel@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/VETDATA/docs/GDX/GDX_FY10V14.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "xls"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-036",
             "issued": "2017-07-26",
-            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -68594,67 +68607,38 @@
                 "insurance",
                 "medical care"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Andrew Bickel",
-                "hasEmail": "mailto:andrew.bickel@va.gov"
-            },
+            "landingPage": "https://www.va.gov/VETDATA/Expenditures.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-OEI-OEI-036",
-            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY2010",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/VETDATA/docs/GDX/GDX_FY10V14.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "xls"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
             "theme": [
                 "Expenditures"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geographic Distribution of VA Expenditures FY2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qy2a-6u8m",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "e0824116-c6b5-458c-a014-fa4bbef5d61d",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Oregon FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68662,42 +68646,37 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "e0824116-c6b5-458c-a014-fa4bbef5d61d",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/qy2a-6u8m",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary Oregon FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_Amount_by_Program_by_State_August_2011.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-08-01T04:00:00Z/2011-08-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Face_Amount_by_Program3.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "insurance",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2011-006",
+            "dataQuality": true,
             "description": "<p>Face value of insurance for each administered life insurance program listed by state. Data is current as of 8-31-11.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "FY11_EOM_August_Face Amount of Life Insurance Coverage by Program by State",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68705,69 +68684,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qy5f-66cq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qy5f-66cq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qy5f-66cq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/qy5f-66cq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qy5f-66cq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qy5f-66cq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/qy5f-66cq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/qy5f-66cq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/qy5f-66cq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-006",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_Amount_by_Program_by_State_August_2011.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Face_Amount_by_Program3.doc"
+            ],
+            "temporal": "2011-08-01T04:00:00Z/2011-08-31T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY11_EOM_August_Face Amount of Life Insurance Coverage by Program by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/",
+            "accrualPeriodicity": "R/P2Y",
             "bureauCode": [
                 "029:00"
             ],
-            "rights": "Public",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2009-01-01T05:00:00Z/2009-12-31T05:00:00Z",
-            "modified": "2020-05-15",
-            "keyword": [
-                "veterans",
-                "women"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:tom.garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-021",
-            "description": "<p>This comprehensive report chronicles the history of women in the military and as Veterans, profiles the characteristics of women Veterans in 2009, illustrates how women Veterans in 2009 utilized some of the major benefits and services offered by the Department of Veterans Affairs (VA), and discusses the future of women Veterans in relation to VA. The goal of this report is to gain an understanding of who our women Veterans are, how their military service affects their post-military lives, and how they can be better served based on these insights.</p>",
-            "title": "America's Women Veterans: Military Service History and VA Benefit Utilization Statistics",
+            "dataQuality": true,
+            "describedBy": "https://www.census.gov/acs/www/Downloads/data_documentation/pums/DataDict/PUMSDataDict10.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>This comprehensive report chronicles the history of women in the military and as Veterans, profiles the characteristics of women Veterans in 2009, illustrates how women Veterans in 2009 utilized some of the major benefits and services offered by the Department of Veterans Affairs (VA), and discusses the future of women Veterans in relation to VA. The goal of this report is to gain an understanding of who our women Veterans are, how their military service affects their post-military lives, and how they can be better served based on these insights.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68776,70 +68760,69 @@
                     "title": "pdf"
                 }
             ],
-            "describedBy": "https://www.census.gov/acs/www/Downloads/data_documentation/pums/DataDict/PUMSDataDict10.pdf",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-021",
+            "issued": "2017-07-26",
+            "keyword": [
+                "veterans",
+                "women"
+            ],
+            "landingPage": "https://www.va.gov/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Public",
+            "temporal": "2009-01-01T05:00:00Z/2009-12-31T05:00:00Z",
             "theme": [
                 "Data on Women Veterans"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "America's Women Veterans: Military Service History and VA Benefit Utilization Statistics"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/qzqu-efd7",
-            "issued": "2023-06-20",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-23",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Georgia FY2021",
+            "identifier": "https://www.data.va.gov/api/views/qzqu-efd7",
+            "issued": "2023-06-20",
             "keyword": [
                 "fy2021 data",
                 "georgia",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/qzqu-efd7",
+            "landingPage": "https://www.data.va.gov/d/qzqu-efd7",
+            "modified": "2024-05-23",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Georgia FY2021",
             "title": "NCVAS State Summary Georgia FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/r24j-cdde",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-07-01T04:00:00Z/2015-07-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "cars",
-                "establishments"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vikki Soukup",
                 "hasEmail": "mailto:Vikki.Soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-139",
+            "dataQuality": true,
             "description": "<p>Activity in terms of establishments and dispositions for CARS on a monthly basis</p>",
-            "title": "COIN 0022 July 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68847,48 +68830,46 @@
                     "mediaType": "text/plain"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-139",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cars",
+                "establishments"
+            ],
+            "landingPage": "https://www.data.va.gov/d/r24j-cdde",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-07-01T04:00:00Z/2015-07-31T04:00:00Z",
             "theme": [
                 "financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "COIN 0022 July 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-01-01T05:00:00Z/2015-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "hcv",
-                "hepatitis c virus",
-                "hiv",
-                "human immunodeficiency virus",
-                "veterans",
-                "vha"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Open Data",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VHA-PCS-023",
+            "dataQuality": true,
+            "describedBy": "https://github.com/department-of-veterans-affairs/VHA-Facilities/blob/master/Report-HCV%20Registry%20Veterans%20in%20VHA%20Care%20in%202015%20by%20Nationa-VISN-Station.xlsx?raw=true",
             "description": "<p>This report describes the number of Hepatitis C Virus (HCV) registry Veterans in VHA care in 2015 based on serologic evidence of HCV infection status (HCV Positive) as well as the subset of those with VA laboratory evidence of HCV viremia (HCV Viremic). The difference between the HCV Positive and the HCV Viremic is the number of Veterans with a positive HCV antibody test who do not have VA laboratory documentation of a test for HCV viremia. For more information on data and methods see the HCV General Notes on this website and the Notes at the end of this report.</p>",
-            "title": "Hepatitis C Virus (HCV) Registry Veterans in VHA Care in 2015, for the Nation, by VISN and by Station",
-            "programCode": [
-                "029:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68896,45 +68877,48 @@
                     "mediaType": "text/plain"
                 }
             ],
-            "describedBy": "https://github.com/department-of-veterans-affairs/VHA-Facilities/blob/master/Report-HCV%20Registry%20Veterans%20in%20VHA%20Care%20in%202015%20by%20Nationa-VISN-Station.xlsx?raw=true",
-            "dataQuality": true,
+            "identifier": "VA-VHA-PCS-023",
+            "issued": "2017-07-26",
+            "keyword": [
+                "hcv",
+                "hepatitis c virus",
+                "hiv",
+                "human immunodeficiency virus",
+                "veterans",
+                "vha"
+            ],
+            "landingPage": "https://www.va.gov/health/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-01-01T05:00:00Z/2015-12-31T05:00:00Z",
             "theme": [
                 "HCV Infected Veterans in VHA Care"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Hepatitis C Virus (HCV) Registry Veterans in VHA Care in 2015, for the Nation, by VISN and by Station"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/r2by-xerj",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-29",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "62124c62-fca5-4367-b290-797b70cc37f3",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Delaware FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68942,115 +68926,114 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "62124c62-fca5-4367-b290-797b70cc37f3",
+            "issued": "2018-10-29",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/r2by-xerj",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data",
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "State Summary Delaware FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Monica Reyes",
+                "hasEmail": "mailto:monica.reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Veterans Dependency and indemnity Compensation for Service-Connected Death-- January 2014</p>",
+            "identifier": "VA-VBA-USASPENDING012014-020",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-01-01T05:00:00Z/2014-01-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 110",
                 "compensation and pension",
                 "dependency and indemnity compensation for service connected death",
                 "usa spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:monica.reyes@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING012014-020",
-            "description": "<p>USA Spending- Veterans Dependency and indemnity Compensation for Service-Connected Death-- January 2014</p>",
-            "title": "USA Spending file- 01/2014 Veterans Dependency and indemnity Compensation for Service-Connected Death-  CFDA 64.110",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014-01-01T05:00:00Z/2014-01-31T05:00:00Z",
             "theme": [
                 "USA SPENDING"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- 01/2014 Veterans Dependency and indemnity Compensation for Service-Connected Death-  CFDA 64.110"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/r2pd-zgpf",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-08",
-            "keyword": [
-                "massachusetts",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/r2pd-zgpf",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Massachusetts",
+            "identifier": "https://www.data.va.gov/api/views/r2pd-zgpf",
+            "issued": "2021-08-26",
+            "keyword": [
+                "massachusetts",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/r2pd-zgpf",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-08",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_Massachusetts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/r2wz-r6cm",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-12-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "debt referrals"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vikki Soukup",
                 "hasEmail": "mailto:Vikki.Soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-122",
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "COIN 0145 MONTHLY CRS TOTALS REPORT DEC 2014",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69058,77 +69041,74 @@
                     "mediaType": "text/plain"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-OM-OM-122",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referrals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/r2wz-r6cm",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-12-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 0145 MONTHLY CRS TOTALS REPORT DEC 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/r32e-j4vj",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-03-30",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
-            "keyword": [
-                "employee engagement",
-                "survey"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA National Center for Organization Development",
                 "hasEmail": "mailto:vhancod@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/r32e-j4vj",
             "description": "VA All Employee Survey data page",
-            "title": "VA All Employee Survey (AES)",
+            "identifier": "https://www.data.va.gov/api/views/r32e-j4vj",
+            "issued": "2021-03-30",
+            "keyword": [
+                "employee engagement",
+                "survey"
+            ],
+            "landingPage": "https://www.data.va.gov/d/r32e-j4vj",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2025-01-31",
             "programCode": [
                 "029:000"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VA All Employee Survey (AES)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "abr",
-                "abr2012",
-                "compensation benefits fy12",
-                "dic benefits",
-                "vba benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-013",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Frequency of Service Connected Disabilities by Body System for Veterans Receiving Comp at the End of FY2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69136,44 +69116,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-013",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "abr",
+                "abr2012",
+                "compensation benefits fy12",
+                "dic benefits",
+                "vba benefits"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR Reports"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Frequency of Service Connected Disabilities by Body System for Veterans Receiving Comp at the End of FY2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/r4bu-jxkz",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 117"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/r4bu-jxkz",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM BENEFITS to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA\u2019s determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING EDUCATION CH35 B117 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE DEC2018",
-            "isPartOf": "f9dff532-b60f-484c-aa3a-38716834d803",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69181,60 +69165,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/r4bu-jxkz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/r4bu-jxkz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/r4bu-jxkz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/r4bu-jxkz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/r4bu-jxkz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/r4bu-jxkz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/r4bu-jxkz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/r4bu-jxkz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/r4bu-jxkz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/r4bu-jxkz",
+            "isPartOf": "f9dff532-b60f-484c-aa3a-38716834d803",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 117"
+            ],
+            "landingPage": "https://www.data.va.gov/d/r4bu-jxkz",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING EDUCATION CH35 B117 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE DEC2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/r4eq-93j3",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "utah"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DG&amp;A Mailgroup",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-216",
             "description": "<p>This summary describes the programs and services VA provided in  Utah in fiscal year 2015.</p>",
-            "title": "State Summary: Utah FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69243,42 +69227,42 @@
                     "title": "Utah"
                 }
             ],
+            "identifier": "VA-OEI-OEI-216",
+            "issued": "2017-07-26",
+            "keyword": [
+                "utah"
+            ],
+            "landingPage": "https://www.data.va.gov/d/r4eq-93j3",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "State Summary: Utah FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/pocketcard/index.asp",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "dependents",
-                "statistics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS Mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-233",
+            "dataQuality": true,
             "description": "<p>This map is the first time that VA has identified Veteran Households with children at the county level.</p>",
-            "title": "Veteran Household with Children Map FY2015",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69287,77 +69271,77 @@
                     "title": "Veteran Household with Children Map FY2015"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-233",
+            "issued": "2017-07-26",
+            "keyword": [
+                "dependents",
+                "statistics",
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/pocketcard/index.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Veteran Benefits",
                 "Veteran Utilization",
                 "Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veteran Household with Children Map FY2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/r6jt-rht5",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Iowa FY2023",
+            "identifier": "https://www.data.va.gov/api/views/r6jt-rht5",
             "issued": "2024-06-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
             "keyword": [
                 "fy2024",
                 "iowa",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/r6jt-rht5",
+            "modified": "2024-07-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/r6jt-rht5",
-            "description": "NCVAS State Summary Iowa FY2023",
-            "title": "NCVAS State Summary Iowa FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Iowa FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/r6kz-mc37",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "issued": "2022-09-29",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-06",
-            "keyword": [
-                "harms",
-                "ptsd-repository"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for PTSD",
                 "hasEmail": "mailto:ncptsd@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for PTSD"
-            },
```

