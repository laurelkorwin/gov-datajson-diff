# Change History for dol.json

### Changes from 31606f9 to dd2190f (Part 1/2)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
diff --git a/dol.json b/dol.json
index 343d417..8a05529 100644
--- a/dol.json
+++ b/dol.json
@@ -1,68 +1,57 @@
 {
-    "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
-    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json",
     "@context": "https://project-open-data.cio.gov/v1.1/schema/catalog.jsonld",
     "@type": "dcat:Catalog",
+    "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
     "dataset": [
         {
             "@type": "dcat:Dataset",
-            "title": "DOL Enterprise Data Inventory",
-            "description": "The publicly-releaseable Enterprise Data Inventory",
-            "modified": "2015-02-27",
             "accessLevel": "public",
-            "identifier": "dol-OCIO-0001",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Department of Labor Office of the Solicitor"
-            },
+            "bureauCode": [
+                "012:25"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Phillip Sullivan",
                 "hasEmail": "mailto:sullivan.phillip.h@dol.gov"
             },
+            "description": "The publicly-releaseable Enterprise Data Inventory",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
-                    "format": "json",
-                    "title": "Enterprise Data Inventory",
                     "description": "DOL's publicly-viewable Enterprise Data Inventory",
-                    "downloadURL": "https://www.dol.gov/open/EDI/data-with-redactions.json"
+                    "downloadURL": "https://www.dol.gov/open/EDI/data-with-redactions.json",
+                    "format": "json",
+                    "mediaType": "application/json",
+                    "title": "Enterprise Data Inventory"
                 }
             ],
+            "identifier": "dol-OCIO-0001",
             "keyword": [
                 "data",
                 "datasets"
             ],
-            "bureauCode": [
-                "012:25"
-            ],
+            "modified": "2015-02-27",
             "programCode": [
                 "012:044"
-            ]
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Department of Labor Office of the Solicitor"
+            },
+            "title": "DOL Enterprise Data Inventory"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Form 5500 FOIA Datasets",
-            "description": "The Form 5500 Annual Report is the primary source of information about the operations, funding and investments of approximately 800,000 retirement and welfare benefit plans. Datasets contain the raw, unedited data from all of the Form 5500 and Form 5500-SF filings for each year, including the data reported in the various schedules.",
-            "modified": "2021-04-02T17:38:19.742Z",
             "accessLevel": "public",
-            "identifier": "EBSA-11-012:019-102",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Employee Benefits Security Administration",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Department of Labor"
-                }
-            },
+            "bureauCode": [
+                "012:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "The Form 5500 Annual Report is the primary source of information about the operations, funding and investments of approximately 800,000 retirement and welfare benefit plans. Datasets contain the raw, unedited data from all of the Form 5500 and Form 5500-SF filings for each year, including the data reported in the various schedules.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71,6 +60,7 @@
                     "title": "Form 5500 FOIA Data"
                 }
             ],
+            "identifier": "EBSA-11-012:019-102",
             "keyword": [
                 "5500",
                 "Benefit Plan",
@@ -79,25 +69,14 @@
                 "Participants",
                 "assets"
             ],
-            "bureauCode": [
-                "012:11"
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-04-02T17:38:19.742Z",
             "programCode": [
                 "012:019"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Abandoned Plan Search Database",
-            "description": "This database consists of submissions of abandoned ERISA plans by Qualified Termination Administrators",
-            "modified": "2021-04-02T17:41:36.011Z",
-            "accessLevel": "public",
-            "identifier": "EBSA-11-012:019-104",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employee Benefits Security Administration",
@@ -106,11 +85,21 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Form 5500 FOIA Datasets"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "012:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "This database consists of submissions of abandoned ERISA plans by Qualified Termination Administrators",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -118,6 +107,7 @@
                     "title": "Search Form"
                 }
             ],
+            "identifier": "EBSA-11-012:019-104",
             "keyword": [
                 "Abandoned Plans",
                 "Benefit Plans",
@@ -125,39 +115,39 @@
                 "ERISA",
                 "Missing Participants"
             ],
-            "bureauCode": [
-                "012:11"
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-04-02T17:41:36.011Z",
             "programCode": [
                 "012:019"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EBSA Form 5500 Annual Return/Report Filing Enforcement Data",
-            "description": "The dataset consists of closed cases that resulted in penalty assessments by EBSA since 2000. This data provides information on EBSA's enforcement programs to enforce ERISA's Form 5500 Annual Return/Report filing requirement focusing on deficient filers, late filers and non-filers.",
-            "modified": "2024-11-05T16:03:28.823Z",
-            "accessLevel": "public",
-            "identifier": "EBSA-11-012:019-100",
-            "issued": "2010-02-22",
-            "license": "https://www.usa.gov/government-copyright",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employee Benefits Security Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Employee Benefits Security Administration"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Abandoned Plan Search Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "The dataset consists of closed cases that resulted in penalty assessments by EBSA since 2000. This data provides information on EBSA's enforcement programs to enforce ERISA's Form 5500 Annual Return/Report filing requirement focusing on deficient filers, late filers and non-filers.",
+            "identifier": "EBSA-11-012:019-100",
+            "issued": "2010-02-22",
             "keyword": [
                 "502 c 2",
                 "Annual Return report",
@@ -172,38 +162,37 @@
                 "late filers",
                 "non-filers"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/government-copyright",
+            "modified": "2024-11-05T16:03:28.823Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "M-1 Filings Database",
-            "description": "Electronic filing system for the Form M-1 annual report for multiple employer welfare arrangements",
-            "modified": "2021-04-02T17:50:03.151Z",
-            "accessLevel": "public",
-            "identifier": "EBSA-11-012:019-116",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employee Benefits Security Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Employee Benefits Security Administration"
                 }
             },
+            "rights": "true",
+            "title": "EBSA Form 5500 Annual Return/Report Filing Enforcement Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "012:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "Electronic filing system for the Form M-1 annual report for multiple employer welfare arrangements",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -211,31 +200,21 @@
                     "title": "Search form"
                 }
             ],
+            "identifier": "EBSA-11-012:019-116",
             "keyword": [
                 "EBSA",
                 "ECE",
                 "MEWA",
                 "welfare"
             ],
-            "bureauCode": [
-                "012:11"
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-04-02T17:50:03.151Z",
             "programCode": [
                 "012:019"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Technical Assistance and Inquiry Database",
-            "description": "The Office of Outreach, Education and Assistance (OEA) of EBSA provides service to EBSA\u2019s customers by means of outreach, education & technical assistance. OEA is responsible for external communications with the public through a variety of vehicles including the media, public outreach, brochures, other educational materials, national educational campaigns, public service announcements, EBSA\u2019s web site, and participant and compliance assistance activities. The automated system that is used to track and manage the inquiries.",
-            "modified": "2021-04-01T15:18:48.076Z",
-            "accessLevel": "non-public",
-            "identifier": "EBSA-11-012:019-101",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Restricted dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employee Benefits Security Administration",
@@ -244,12 +223,23 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "M-1 Filings Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "012:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "The Office of Outreach, Education and Assistance (OEA) of EBSA provides service to EBSA\u2019s customers by means of outreach, education & technical assistance. OEA is responsible for external communications with the public through a variety of vehicles including the media, public outreach, brochures, other educational materials, national educational campaigns, public service announcements, EBSA\u2019s web site, and participant and compliance assistance activities. The automated system that is used to track and manage the inquiries.",
+            "identifier": "EBSA-11-012:019-101",
             "keyword": [
                 "Benefit Recovery",
                 "Benefits Advisor",
@@ -258,74 +248,69 @@
                 "Outreach Inquiry",
                 "inquiries"
             ],
-            "bureauCode": [
-                "012:11"
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-04-01T15:18:48.076Z",
             "programCode": [
                 "012:019"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Wage and Hour Division Compliance Action Data",
-            "description": "The dataset contains all concluded WHD compliance actions since FY 2005. The dataset includes whether any violations were found and the back wage amount, number of employees due back wages, and civil money penalties assessed. More information and details about the data provided can be found at http://www.dol.gov/whd/",
-            "modified": "2024-12-16T14:57:57.134Z",
-            "accessLevel": "public",
-            "identifier": "WHD-16-012:027-381",
-            "dataQuality": true,
-            "describedBy": "https://enfxfr.dol.gov/data_catalog/WHD/whd_data_dictionary_20220414.csv.zip",
-            "describedByType": "text/csv",
-            "issued": "2024-10-10",
-            "landingPage": "http://developer.dol.gov/dataset/dol-whd-compliance-dataset",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "WHD",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Wage and Hour Division",
+                "name": "Employee Benefits Security Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                        "name": "WHD"
-                    }
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "Restricted dataset",
+            "title": "Technical Assistance and Inquiry Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alex Cruz",
                 "hasEmail": "mailto:cruz.alexander@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://enfxfr.dol.gov/data_catalog/WHD/whd_data_dictionary_20220414.csv.zip",
+            "describedByType": "text/csv",
+            "description": "The dataset contains all concluded WHD compliance actions since FY 2005. The dataset includes whether any violations were found and the back wage amount, number of employees due back wages, and civil money penalties assessed. More information and details about the data provided can be found at http://www.dol.gov/whd/",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "csv",
-                    "title": "Wage and Hour Compliance Action Data",
-                    "description": "The dataset contains all concluded WHD compliance actions since FY 2005. The dataset includes whether any violations were found and the back wage amount, number of employees due back wages, and civil money penalties assessed.",
                     "describedBy": "https://enfxfr.dol.gov/data_catalog/WHD/whd_data_dictionary_20220414.csv.zip",
-                    "downloadURL": "http://ogesdw.dol.gov/"
+                    "description": "The dataset contains all concluded WHD compliance actions since FY 2005. The dataset includes whether any violations were found and the back wage amount, number of employees due back wages, and civil money penalties assessed.",
+                    "downloadURL": "http://ogesdw.dol.gov/",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "Wage and Hour Compliance Action Data"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/xml",
-                    "format": "xml",
-                    "title": "Wage and Hour Compliance Action Data",
-                    "description": "The dataset contains all concluded WHD compliance actions since FY 2005. The dataset includes whether any violations were found and the back wage amount, number of employees due back wages, and civil money penalties assessed.",
                     "describedBy": "https://enfxfr.dol.gov/data_catalog/WHD/whd_data_dictionary_20220414.xml.zip",
-                    "downloadURL": "http://ogesdw.dol.gov/"
+                    "description": "The dataset contains all concluded WHD compliance actions since FY 2005. The dataset includes whether any violations were found and the back wage amount, number of employees due back wages, and civil money penalties assessed.",
+                    "downloadURL": "http://ogesdw.dol.gov/",
+                    "format": "xml",
+                    "mediaType": "application/xml",
+                    "title": "Wage and Hour Compliance Action Data"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://enforcedata.dol.gov/",
-                    "title": "Wage and Hour Compliance Action Data",
-                    "description": "The dataset contains all concluded compliance actions since 2005. For all Acts under WHD jurisdiction, the dataset includes whether any violations were found and the back wage amount, number of employees due back wages, and civil money penalties assessed"
+                    "description": "The dataset contains all concluded compliance actions since 2005. For all Acts under WHD jurisdiction, the dataset includes whether any violations were found and the back wage amount, number of employees due back wages, and civil money penalties assessed",
+                    "title": "Wage and Hour Compliance Action Data"
                 }
             ],
+            "identifier": "WHD-16-012:027-381",
+            "issued": "2024-10-10",
             "keyword": [
                 "Enforcement",
                 "Labor",
@@ -333,86 +318,89 @@
                 "WHD",
                 "WHISARD"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://developer.dol.gov/dataset/dol-whd-compliance-dataset",
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-12-16T14:57:57.134Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Contractor Performance Assessment Reporting System (CPARS)",
-            "description": "Suite of web-enabled applications that are used to document contractor and grantee performance information.",
-            "modified": "2022-09-29T16:48:23.632Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OSPE-25-012:044-199",
-            "landingPage": "https://cpars.cpars.gov/cpars/app/home_input.action",
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
+                "name": "WHD",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
+                    "name": "Wage and Hour Division",
+                    "subOrganizationOf": {
+                        "@type": "org:Organization",
+                        "name": "WHD"
+                    }
                 }
             },
+            "rights": "true",
+            "title": "Wage and Hour Division Compliance Action Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Cassandra Mitchell",
                 "hasEmail": "mailto:mitchell.cassandra@dol.gov"
             },
+            "description": "Suite of web-enabled applications that are used to document contractor and grantee performance information.",
+            "identifier": "OASAM OSPE-25-012:044-199",
             "keyword": [
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
-            ],
+            "landingPage": "https://cpars.cpars.gov/cpars/app/home_input.action",
             "language": [
                 "en-US"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Pregnancy and Breastfeeding Rights map",
-            "description": "This map provides information on federal and state-level employment protections against pregnancy discrimination, provisions for pregnancy accommodation, and workplace breastfeeding rights.",
-            "modified": "2024-02-27T14:44:21.058Z",
-            "accessLevel": "public",
-            "identifier": "WB-12-012:038-362",
-            "issued": "2023-09-01",
-            "landingPage": "https://www.dol.gov/agencies/wb/pregnant-nursing-employment-protections",
-            "rights": "true",
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2022-09-29T16:48:23.632Z",
+            "programCode": [
+                "015:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Published",
+                "name": "Office of the Assistant Secretary for Administration and Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Published"
+                    "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "Internal dataset",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Contractor Performance Assessment Reporting System (CPARS)"
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
                 "fn": "Jeff Hayes",
                 "hasEmail": "mailto:hayes.jeffrey.a@dol.gov"
             },
+            "description": "This map provides information on federal and state-level employment protections against pregnancy discrimination, provisions for pregnancy accommodation, and workplace breastfeeding rights.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/wb/pregnant-nursing-employment-protections",
-                    "title": "Employment Protections for Workers Who Are Pregnant or Nursing",
-                    "description": "This map provides information on federal and state-level employment protections against pregnancy discrimination, provisions for pregnancy accommodation, and workplace breastfeeding rights."
+                    "description": "This map provides information on federal and state-level employment protections against pregnancy discrimination, provisions for pregnancy accommodation, and workplace breastfeeding rights.",
+                    "title": "Employment Protections for Workers Who Are Pregnant or Nursing"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -420,6 +408,8 @@
                     "title": "Employment Protections for Workers Who Are Pregnant or Nursing"
                 }
             ],
+            "identifier": "WB-12-012:038-362",
+            "issued": "2023-09-01",
             "keyword": [
                 "Employment protections",
                 "Federal",
@@ -432,75 +422,75 @@
                 "pay transparency",
                 "pregnancy"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/wb/pregnant-nursing-employment-protections",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-02-27T14:44:21.058Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Gov Delivery Account WB contact information",
-            "description": "Registry of WB contacts",
-            "modified": "2021-07-15T21:06:22.656Z",
-            "accessLevel": "non-public",
-            "identifier": "WB-12-012:038-364",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Women\u2019s Bureau",
+                "name": "Published",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Women\u2019s Bureau"
+                    "name": "Published"
                 }
             },
+            "rights": "true",
+            "title": "Pregnancy and Breastfeeding Rights map"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Andrea Jones",
                 "hasEmail": "mailto:Jones.Andrea.T@dol.gov"
             },
+            "description": "Registry of WB contacts",
+            "identifier": "WB-12-012:038-364",
             "keyword": [
                 "WB"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-07-15T21:06:22.656Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Workforce Recruitment Program database",
-            "description": "The Workforce Recruitment Program Database identifies college students with disabilities who have been pre-vetted for Schedule A hiring by employers",
-            "modified": "2022-09-29T21:00:50.616Z",
-            "accessLevel": "restricted public",
-            "identifier": "ODEP-12-012:039-300",
-            "landingPage": "https://www.wrp.gov/wrp",
-            "rights": "Restricted dataset",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Disability Employment Policy",
+                "name": "Women\u2019s Bureau",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Disability Employment Policy"
+                    "name": "Women\u2019s Bureau"
                 }
             },
+            "rights": "Internal dataset",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Gov Delivery Account WB contact information"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "WRP Mailbox",
                 "hasEmail": "mailto:wrp@dol.gov"
             },
+            "description": "The Workforce Recruitment Program Database identifies college students with disabilities who have been pre-vetted for Schedule A hiring by employers",
+            "identifier": "ODEP-12-012:039-300",
             "keyword": [
                 "Disability",
                 "Job Seekers",
@@ -514,37 +504,40 @@
                 "recruitment",
                 "students"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.wrp.gov/wrp",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-09-29T21:00:50.616Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Disability Employment Policy",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of Disability Employment Policy"
+                }
+            },
+            "rights": "Restricted dataset",
+            "title": "Workforce Recruitment Program database"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Research and Evaluation Inventory",
-            "description": "This inventory is the first phase in the development of a single repository of all completed and planned research and evaluation projects that have or will be conducted by DOL in the upcoming calendar year. This data set includes: a title and description of each project; the date the project began; the date the project was published with a link to completed research and evaluation project outcomes as these become available; and, information on Contract or Grant resources, if applicable. The database will be updated on a monthly basis to add more agency information and to links to completed projects.",
-            "modified": "2024-11-14T18:21:41.037Z",
             "accessLevel": "public",
-            "identifier": "DOL-OASP-8",
-            "issued": "2011-02-18",
-            "landingPage": "https://developer.dol.gov/others/research-and-evaluation-inventory/",
-            "license": "https://www.usa.gov/government-copyright",
-            "rights": "Internal dataset",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Department of Labor Office of the Assistant Secretary for Policy"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Terry Fryer",
                 "hasEmail": "mailto:Fryer.Terry@dol.gov"
             },
+            "description": "This inventory is the first phase in the development of a single repository of all completed and planned research and evaluation projects that have or will be conducted by DOL in the upcoming calendar year. This data set includes: a title and description of each project; the date the project began; the date the project was published with a link to completed research and evaluation project outcomes as these become available; and, information on Contract or Grant resources, if applicable. The database will be updated on a monthly basis to add more agency information and to links to completed projects.",
+            "identifier": "DOL-OASP-8",
+            "issued": "2011-02-18",
             "keyword": [
                 "DOL",
                 "Labor",
@@ -563,94 +556,92 @@
                 "veterans",
                 "workers"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://developer.dol.gov/others/research-and-evaluation-inventory/",
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/government-copyright",
+            "modified": "2024-11-14T18:21:41.037Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Department of Labor Office of the Assistant Secretary for Policy"
+            },
+            "rights": "Internal dataset",
+            "title": "Research and Evaluation Inventory"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "National Database of Childcare Prices",
-            "description": "This database provides county-level childcare prices for most states in the United States over 14 years. The childcare price data are combined with county-level data from the American Community Survey to provide demographic and economic characteristics of the counties. The database facilitates research on childcare prices by county and demographic and economic characteristics.",
-            "modified": "2024-12-20T19:16:56.275Z",
             "accessLevel": "public",
-            "identifier": "WB-12-012:038-366",
-            "describedBy": "https://www.dol.gov/sites/dolgov/files/WB/NDCP2022-Technical-Report-508.pdf",
-            "describedByType": "application/pdf",
-            "issued": "2024-11-15",
-            "landingPage": "https://www.dol.gov/agencies/wb/topics/featured-childcare",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Women\u2019s Bureau",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Women\u2019s Bureau"
-                }
-            },
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Georgia Poyatzis",
                 "hasEmail": "mailto:Poyatzis.Georgia.D@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/sites/dolgov/files/WB/NDCP2022-Technical-Report-508.pdf",
+            "describedByType": "application/pdf",
+            "description": "This database provides county-level childcare prices for most states in the United States over 14 years. The childcare price data are combined with county-level data from the American Community Survey to provide demographic and economic characteristics of the counties. The database facilitates research on childcare prices by county and demographic and economic characteristics.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/sites/dolgov/files/WB/NDCP2022.xlsx",
-                    "title": "National Database of Childcare Prices",
-                    "description": "This database provides county-level childcare prices for most states in the United States over 14 years. The childcare price data are combined with county-level data from the American Community Survey to provide demographic and economic characteristics of the counties. The database facilitates research on childcare prices by county and demographic and economic characteristics."
+                    "description": "This database provides county-level childcare prices for most states in the United States over 14 years. The childcare price data are combined with county-level data from the American Community Survey to provide demographic and economic characteristics of the counties. The database facilitates research on childcare prices by county and demographic and economic characteristics.",
+                    "title": "National Database of Childcare Prices"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://apiprod.dol.gov/v4/get/WB/ndcp/json",
-                    "title": "National Database of Childcare Prices (NDCP)",
-                    "description": "*UPDATED* The National Database of Childcare Prices (NDCP) is the most comprehensive federal source of childcare prices at the county level. The database offers childcare price data by childcare provider type, age of children, and county characteristics. Data are available from 2008 to 2022. The technical guide and more information can be found on our website: https://www.dol.gov/agencies/wb/topics/featured-childcare"
+                    "description": "*UPDATED* The National Database of Childcare Prices (NDCP) is the most comprehensive federal source of childcare prices at the county level. The database offers childcare price data by childcare provider type, age of children, and county characteristics. Data are available from 2008 to 2022. The technical guide and more information can be found on our website: https://www.dol.gov/agencies/wb/topics/featured-childcare",
+                    "title": "National Database of Childcare Prices (NDCP)"
                 }
             ],
+            "identifier": "WB-12-012:038-366",
+            "issued": "2024-11-15",
             "keyword": [
                 "WB",
                 "Women Employment",
                 "childcare prices",
                 "counties"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/wb/topics/featured-childcare",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-20T19:16:56.275Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Job Accommodation Network Datasets",
-            "description": "Data collected from interviews with employers, professionals, self-employed individuals, and individual workers who have been assisted by JAN",
-            "modified": "2023-03-31T15:23:19.723Z",
-            "accessLevel": "restricted public",
-            "identifier": "ODEP-12-012:039-301",
-            "rights": "Restricted dataset",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Disability Employment Policy",
+                "name": "Women\u2019s Bureau",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Disability Employment Policy"
+                    "name": "Women\u2019s Bureau"
                 }
             },
+            "rights": "true",
+            "title": "National Database of Childcare Prices"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Rosenblum",
                 "hasEmail": "mailto:Rosenblum.David.B@dol.gov"
             },
+            "description": "Data collected from interviews with employers, professionals, self-employed individuals, and individual workers who have been assisted by JAN",
+            "identifier": "ODEP-12-012:039-301",
             "keyword": [
                 "Accessibility",
                 "Disability",
@@ -662,24 +653,13 @@
                 "accommodation",
                 "employers"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-03-31T15:23:19.723Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "RETAIN Quarterly Performance Reports",
-            "description": "RETAIN QPR Appendix A elements, which will be delivered to ODEP by RETAIN grantees in the remainder of Phase 1 and continuing through Phase 2",
-            "modified": "2022-09-29T21:01:41.261Z",
-            "accessLevel": "restricted public",
-            "identifier": "ODEP-12-012:039-302",
-            "rights": "Restricted dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Disability Employment Policy",
@@ -688,12 +668,23 @@
                     "name": "Office of Disability Employment Policy"
                 }
             },
+            "rights": "Restricted dataset",
+            "title": "Job Accommodation Network Datasets"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Rosenblum",
                 "hasEmail": "mailto:Rosenblum.David.B@dol.gov"
             },
+            "description": "RETAIN QPR Appendix A elements, which will be delivered to ODEP by RETAIN grantees in the remainder of Phase 1 and continuing through Phase 2",
+            "identifier": "ODEP-12-012:039-302",
             "keyword": [
                 "Disability",
                 "ODEP",
@@ -703,84 +694,83 @@
                 "return-to-work",
                 "stay-at-work"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-09-29T21:01:41.261Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "GSA Data 2 Decisions Portal and Dashboard",
-            "description": "Tracking systems for timeliness and completion for business processes",
-            "modified": "2022-09-29T19:01:23.282Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OSPE-25-012:044-200",
-            "landingPage": "https://d2d.gsa.gov/",
-            "rights": "not available",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
+                "name": "Office of Disability Employment Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
+                    "name": "Office of Disability Employment Policy"
                 }
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
+            "rights": "Restricted dataset",
+            "title": "RETAIN Quarterly Performance Reports"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
                 "fn": "Ryan Chandler",
                 "hasEmail": "mailto:chandler.ryan.p@dol.gov"
             },
+            "description": "Tracking systems for timeliness and completion for business processes",
+            "identifier": "OASAM OSPE-25-012:044-200",
             "keyword": [
                 "OASAM",
                 "OSPE"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://d2d.gsa.gov/",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-09-29T19:01:23.282Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Industries with High Prevalence of H-2B Workers",
-            "description": "Three tables display data including violations, cases with violations, and back wages involving H-2B non-imigrant visas.  The tables are organized by Act and by industry",
-            "modified": "2024-12-16T14:59:58.802Z",
-            "accessLevel": "public",
-            "identifier": "WHD-16-012:027-375",
-            "issued": "2024-11-01",
-            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/industries-h2b-workers",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Wage and Hour Division",
+                "name": "Office of the Assistant Secretary for Administration and Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Wage and Hour Division"
+                    "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "not available",
+            "title": "GSA Data 2 Decisions Portal and Dashboard"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alex Cruz",
                 "hasEmail": "mailto:cruz.alexander@dol.gov"
             },
+            "description": "Three tables display data including violations, cases with violations, and back wages involving H-2B non-imigrant visas.  The tables are organized by Act and by industry",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/whd/data/charts/industries-h2b-workers",
-                    "title": "Industries with High Prevalence of H-2B Workers",
-                    "description": "Three tables display data including violations, cases with violations, and back wages involving H-2B non-imigrant visas.  The tables are organized by Act and by industry"
+                    "description": "Three tables display data including violations, cases with violations, and back wages involving H-2B non-imigrant visas.  The tables are organized by Act and by industry",
+                    "title": "Industries with High Prevalence of H-2B Workers"
                 }
             ],
+            "identifier": "WHD-16-012:027-375",
+            "issued": "2024-11-01",
             "keyword": [
                 "Janitorial",
                 "Landscaping",
@@ -790,26 +780,14 @@
                 "forestry",
                 "hotel"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/industries-h2b-workers",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T14:59:58.802Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Government Contracts",
-            "description": "Numbers of investigations, investigations with violations, employees and back wage owed are shown for acts involving government contracts (DBRA, SCA, CWHSSA) Includes three Act-specific breakouts for: Davis Bacon and Related Acts, Service Contract Act, Contract Work Hours Safety Standards Act",
-            "modified": "2024-12-16T15:21:24.363Z",
-            "accessLevel": "public",
-            "identifier": "WHD-16-012:027-377",
-            "issued": "2024-11-01",
-            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/government-contracts",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Wage and Hour Division",
@@ -818,46 +796,45 @@
                     "name": "Wage and Hour Division"
                 }
             },
+            "rights": "true",
+            "title": "Industries with High Prevalence of H-2B Workers"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alex Cruz",
                 "hasEmail": "mailto:cruz.alexander@dol.gov"
             },
+            "description": "Numbers of investigations, investigations with violations, employees and back wage owed are shown for acts involving government contracts (DBRA, SCA, CWHSSA) Includes three Act-specific breakouts for: Davis Bacon and Related Acts, Service Contract Act, Contract Work Hours Safety Standards Act",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/whd/data/charts/government-contracts",
-                    "title": "Government Contracts",
-                    "description": "Numbers of investigations, investigations with violations, employees and back wage owed are shown for acts involving government contracts (DBRA, SCA, CWHSSA) Includes three Act-specific breakouts for: Davis Bacon and Related Acts, Service Contract Act, Contract Work Hours Safety Standards Act"
+                    "description": "Numbers of investigations, investigations with violations, employees and back wage owed are shown for acts involving government contracts (DBRA, SCA, CWHSSA) Includes three Act-specific breakouts for: Davis Bacon and Related Acts, Service Contract Act, Contract Work Hours Safety Standards Act",
+                    "title": "Government Contracts"
                 }
             ],
+            "identifier": "WHD-16-012:027-377",
+            "issued": "2024-11-01",
             "keyword": [
                 "DBRA",
                 "SCA",
                 "WHD"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/government-contracts",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T15:21:24.363Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Registered Farm Labor Contractor Employee Listing",
-            "description": "List of eligible farm labor contractor employees certified under the Migrant and Seasonal Agricultural Worker Protection Act",
-            "modified": "2024-12-16T14:58:28.541Z",
-            "accessLevel": "public",
-            "identifier": "WHD-16-012:027-379",
-            "describedByType": "text/html",
-            "issued": "2024-12-11",
-            "landingPage": "https://www.dol.gov/agencies/whd/agriculture/mspa/farm-labor-contractors/employees",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Wage and Hour Division",
@@ -866,45 +843,46 @@
                     "name": "Wage and Hour Division"
                 }
             },
+            "rights": "true",
+            "title": "Government Contracts"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1W",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alex Cruz",
                 "hasEmail": "mailto:cruz.alexander@dol.gov"
             },
+            "describedByType": "text/html",
+            "description": "List of eligible farm labor contractor employees certified under the Migrant and Seasonal Agricultural Worker Protection Act",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/whd/agriculture/mspa/farm-labor-contractors/employees",
-                    "title": "Registered Farm Labor Contractor Employee Listing",
-                    "description": "List of eligible farm labor contractor employees certified under the Migrant and Seasonal Agricultural Worker Protection Act"
+                    "description": "List of eligible farm labor contractor employees certified under the Migrant and Seasonal Agricultural Worker Protection Act",
+                    "title": "Registered Farm Labor Contractor Employee Listing"
                 }
             ],
+            "identifier": "WHD-16-012:027-379",
+            "issued": "2024-12-11",
             "keyword": [
                 "FLCE",
                 "WHD",
                 "agriculture"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/whd/agriculture/mspa/farm-labor-contractors/employees",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T14:58:28.541Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Construction Surveys Survey Status by State",
-            "description": "Prevailing wage survey information is listed by state",
-            "modified": "2022-09-21T13:53:36.115Z",
-            "accessLevel": "public",
-            "identifier": "WHD-16-012:027-380",
-            "describedByType": "text/html",
-            "landingPage": "https://www.dol.gov/whd/programs/dbra/Survey/status.htm#searcher",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Wage and Hour Division",
@@ -913,58 +891,70 @@
                     "name": "Wage and Hour Division"
                 }
             },
+            "rights": "true",
+            "title": "Registered Farm Labor Contractor Employee Listing"
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
                 "fn": "Alex Cruz",
                 "hasEmail": "mailto:cruz.alexander@dol.gov"
             },
+            "describedByType": "text/html",
+            "description": "Prevailing wage survey information is listed by state",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/whd/government-contracts/construction/surveys/status#searcher",
-                    "title": "Construction Surveys - Survey Status by State",
-                    "description": "Prevailing wage survey information is listed by state"
+                    "description": "Prevailing wage survey information is listed by state",
+                    "title": "Construction Surveys - Survey Status by State"
                 }
             ],
+            "identifier": "WHD-16-012:027-380",
             "keyword": [
                 "Davis-Bacon",
                 "WD-10",
                 "WHD"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/whd/programs/dbra/Survey/status.htm#searcher",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-09-21T13:53:36.115Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Agency Records Management Records including, Holdings Reports, File Plans, Invoices, Capstone official listings, Electronic Information System listings, Disposal Notices",
-            "description": "The DOL Records Management Program consists of managerial activities required to ensure the proper management of agency records. This includes records created or received within the Department, the secure storage, maintenance, and accountability of these records, and the proper use and disposition of these records.",
-            "modified": "2024-12-09T18:22:11.521Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM BOC-25-012:044-205",
-            "landingPage": "https://usdol.sharepoint.com/sites/OASAM-DOLRECORDS/SitePages/Home.aspx",
-            "rights": "restricted",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
+                "name": "Wage and Hour Division",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
+                    "name": "Wage and Hour Division"
                 }
             },
+            "rights": "true",
+            "title": "Construction Surveys Survey Status by State"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Steven Pierce",
                 "hasEmail": "mailto:pierce.steven@dol.gov"
             },
+            "description": "The DOL Records Management Program consists of managerial activities required to ensure the proper management of agency records. This includes records created or received within the Department, the secure storage, maintenance, and accountability of these records, and the proper use and disposition of these records.",
+            "identifier": "OASAM BOC-25-012:044-205",
             "keyword": [
                 "Agency Records Officers",
                 "OASAM",
@@ -972,30 +962,14 @@
                 "records",
                 "records management"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://usdol.sharepoint.com/sites/OASAM-DOLRECORDS/SitePages/Home.aspx",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-09T18:22:11.521Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://usdol.sharepoint.com/sites/OASAM-DOLRECORDS"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Space Management System (SMS)",
-            "description": "Data repository for DOL's real property portfolio and GSA occupancy agreements",
-            "modified": "2024-12-06T13:23:04.029Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM BOC-25-012:044-207",
-            "describedBy": "https://sms.netdigitalsolutions.com/custom.aspx?cuiid=117",
-            "landingPage": "https://sms.netdigitalsolutions.com/custom.aspx?cuiid=117",
-            "rights": "private",
-            "spatial": "location characteristics, address",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -1004,89 +978,86 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "references": [
+                "https://usdol.sharepoint.com/sites/OASAM-DOLRECORDS"
+            ],
+            "rights": "restricted",
+            "title": "Agency Records Management Records including, Holdings Reports, File Plans, Invoices, Capstone official listings, Electronic Information System listings, Disposal Notices"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Heath Rehkop",
                 "hasEmail": "mailto:rehkop.christopher.h@dol.gov"
             },
+            "describedBy": "https://sms.netdigitalsolutions.com/custom.aspx?cuiid=117",
+            "description": "Data repository for DOL's real property portfolio and GSA occupancy agreements",
+            "identifier": "OASAM BOC-25-012:044-207",
             "keyword": [
                 "BOC",
                 "OASAM",
                 "Space management system",
                 "sms"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://sms.netdigitalsolutions.com/custom.aspx?cuiid=117",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-06T13:23:04.029Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Assistant Secretary for Administration and Management",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Assistant Secretary for Administration and Management"
+                }
+            },
             "references": [
                 "https://sms.netdigitalsolutions.com/custom.aspx?cuiid=117"
             ],
+            "rights": "private",
+            "spatial": "location characteristics, address",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "Space Management System (SMS)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Motor Vehicle Fleet data and infrastructure reporting",
-            "description": "GSA and DOE Federal Automotive Statistical Tool (FAST) for statutory reporting",
-            "modified": "2024-06-27T13:56:30.946Z",
             "accessLevel": "restricted public",
-            "identifier": "OASAM BOC-25-012:044-214",
-            "landingPage": "https://fastweb.inel.gov/",
-            "rights": "restricted",
-            "spatial": "location characteristics, address",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
-                }
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Heath Rehkop",
                 "hasEmail": "mailto:rehkop.christopher.h@dol.gov"
             },
+            "description": "GSA and DOE Federal Automotive Statistical Tool (FAST) for statutory reporting",
+            "identifier": "OASAM BOC-25-012:044-214",
             "keyword": [
                 "BOC",
                 "FAST report",
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
-            ],
+            "landingPage": "https://fastweb.inel.gov/",
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://fastweb.inel.gov/"
+            "modified": "2024-06-27T13:56:30.946Z",
+            "programCode": [
+                "015:001"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "energy use water use costs",
-            "description": "USEPA - Energy Star Portfolio Manager.  Repository for energy consumption data.  Also used for benchmarking building energy and water use prior to reporting to CTS.  JCCs also utilize Energy Watchdog, where individual JCC sites enter their water and energy consumption information.",
-            "modified": "2024-06-27T17:04:03.369Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM BOC-25-012:044-224",
-            "landingPage": "https://www.energystar.gov/buildings/facility-owners-and-managers/existing-buildings/use-portfolio-manager",
-            "rights": "restricted",
-            "spatial": "address",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -1095,39 +1066,42 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "references": [
+                "https://fastweb.inel.gov/"
+            ],
+            "rights": "restricted",
+            "spatial": "location characteristics, address",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Motor Vehicle Fleet data and infrastructure reporting"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kathryn Simpson",
                 "hasEmail": "mailto:simpson.kathryn.j@dol.gov"
             },
+            "description": "USEPA - Energy Star Portfolio Manager.  Repository for energy consumption data.  Also used for benchmarking building energy and water use prior to reporting to CTS.  JCCs also utilize Energy Watchdog, where individual JCC sites enter their water and energy consumption information.",
+            "identifier": "OASAM BOC-25-012:044-224",
             "keyword": [
                 "BOC",
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.energystar.gov/buildings/facility-owners-and-managers/existing-buildings/use-portfolio-manager",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-06-27T17:04:03.369Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://www.energystar.gov/buildings/facility-owners-and-managers/existing-buildings/use-portfolio-manager"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Complaints Tracking and Reporting System - Internal Enforcement Module",
-            "description": "DOL\u2019s internal EEO Complaint Tracking System; only DOL employees with EEO responsibility (Civil Rights Center staff and Workplace Equality Compliance Officers and their staff) have access to the system. Tracks the EEO complaints filed by employees of the department or individuals that have submitted applications for employment with the DOL.",
-            "modified": "2024-09-23T12:40:24.297Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM CRC-25-012:044-228",
-            "landingPage": "https://cmp.dol.gov/suite/sites/ctrs-tl7",
-            "rights": "not available",
-            "spatial": "location characteristics, address",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -1136,38 +1110,39 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "references": [
+                "https://www.energystar.gov/buildings/facility-owners-and-managers/existing-buildings/use-portfolio-manager"
+            ],
+            "rights": "restricted",
+            "spatial": "address",
+            "title": "energy use water use costs"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jehad Ali",
                 "hasEmail": "mailto:ali.jehad@dol.gov"
             },
+            "description": "DOL\u2019s internal EEO Complaint Tracking System; only DOL employees with EEO responsibility (Civil Rights Center staff and Workplace Equality Compliance Officers and their staff) have access to the system. Tracks the EEO complaints filed by employees of the department or individuals that have submitted applications for employment with the DOL.",
+            "identifier": "OASAM CRC-25-012:044-228",
             "keyword": [
                 "CRC",
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://cmp.dol.gov/suite/sites/ctrs-tl7",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T12:40:24.297Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "DOORS",
-            "description": "Web-based e-Recruitment system that provides both Department of Labor (DOL) employees and outside job seekers the opportunity to apply for DOL jobs via the Internet.",
-            "modified": "2024-09-23T13:44:30.180Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OHR-25-012:044-236",
-            "landingPage": "https://hr.monstergovt.com/dol/home/login.hms",
-            "rights": "private",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -1176,12 +1151,27 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "not available",
+            "spatial": "location characteristics, address",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Complaints Tracking and Reporting System - Internal Enforcement Module"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michelle Abellar",
                 "hasEmail": "mailto:Abellar.Michelle@dol.gov"
             },
+            "description": "Web-based e-Recruitment system that provides both Department of Labor (DOL) employees and outside job seekers the opportunity to apply for DOL jobs via the Internet.",
+            "identifier": "OASAM OHR-25-012:044-236",
             "keyword": [
                 "OASAM",
                 "OHR",
@@ -1189,26 +1179,14 @@
                 "certificate",
                 "vacancies"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://hr.monstergovt.com/dol/home/login.hms",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:44:30.180Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "HRConnect",
-            "description": "Core human resource system provided by Treasury's Shared Service Center (SSC)",
-            "modified": "2024-09-23T13:35:59.639Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OHR-25-012:044-237",
-            "landingPage": "https://datainsight.teaps.treasury.gov/PortalEntry",
-            "rights": "private",
-            "spatial": "location characteristics, addresses",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -1217,12 +1195,23 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "title": "DOORS"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LaRell Faulkner",
                 "hasEmail": "mailto:Faulkner.Larell@dol.gov"
             },
+            "description": "Core human resource system provided by Treasury's Shared Service Center (SSC)",
+            "identifier": "OASAM OHR-25-012:044-237",
             "keyword": [
                 "HR data",
                 "Human Capital Data",
@@ -1231,28 +1220,14 @@
                 "hr",
                 "human capital"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://datainsight.teaps.treasury.gov/PortalEntry",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:35:59.639Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MOU Tracker",
-            "description": "This is a system that tracks MOUs from the time sent to PMC for clearance to the time executed.",
-            "modified": "2024-09-23T13:49:39.961Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM PMC-25-012:044-290",
-            "landingPage": "https://usdol.sharepoint.com/sites/OASAM-OPP-PMC/MOU/SitePages/Home.aspx",
-            "rights": "restricted",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -1261,12 +1236,27 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "spatial": "location characteristics, addresses",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "HRConnect"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joseph Vilca",
                 "hasEmail": "mailto:vilca.joseph.h@dol.gov"
             },
+            "description": "This is a system that tracks MOUs from the time sent to PMC for clearance to the time executed.",
+            "identifier": "OASAM PMC-25-012:044-290",
             "keyword": [
                 "OASAM",
                 "PMC",
@@ -1274,73 +1264,61 @@
                 "iaa",
                 "mou"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://usdol.sharepoint.com/sites/OASAM-OPP-PMC/MOU/SitePages/Home.aspx",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:49:39.961Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Fiscal Year Data for WHD",
-            "description": "Main landing page for statistics tables",
-            "modified": "2024-12-16T15:00:43.880Z",
-            "accessLevel": "public",
-            "identifier": "WHD-16-012:027-367",
-            "issued": "2024-11-01",
-            "landingPage": "https://www.dol.gov/whd/data/datatables.htm",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Wage and Hour Division",
+                "name": "Office of the Assistant Secretary for Administration and Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Wage and Hour Division"
+                    "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "restricted",
+            "title": "MOU Tracker"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alex Cruz",
                 "hasEmail": "mailto:cruz.alexander@dol.gov"
             },
+            "description": "Main landing page for statistics tables",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/whd/data/charts",
-                    "title": "Fiscal Year Data for WHD",
-                    "description": "Main landing page for statistics tables"
+                    "description": "Main landing page for statistics tables",
+                    "title": "Fiscal Year Data for WHD"
                 }
             ],
+            "identifier": "WHD-16-012:027-367",
+            "issued": "2024-11-01",
             "keyword": [
                 "WHD",
                 "enforcement",
                 "wages"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/whd/data/datatables.htm",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T15:00:43.880Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Outreach",
-            "description": "Number of outreach events per year excluding mailing and media",
-            "modified": "2024-12-16T15:13:13.144Z",
-            "accessLevel": "public",
-            "identifier": "WHD-16-012:027-371",
-            "issued": "2024-11-01",
-            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/outreach",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Wage and Hour Division",
@@ -1349,43 +1327,43 @@
                     "name": "Wage and Hour Division"
                 }
             },
+            "rights": "true",
+            "title": "Fiscal Year Data for WHD"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alex Cruz",
                 "hasEmail": "mailto:cruz.alexander@dol.gov"
             },
+            "description": "Number of outreach events per year excluding mailing and media",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/whd/data/charts/outreach",
-                    "title": "Outreach",
-                    "description": "Number of outreach events per year excluding mailing and media"
+                    "description": "Number of outreach events per year excluding mailing and media",
+                    "title": "Outreach"
                 }
             ],
+            "identifier": "WHD-16-012:027-371",
+            "issued": "2024-11-01",
             "keyword": [
                 "WHD"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/outreach",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T15:13:13.144Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Child Labor",
-            "description": "Investigative case data involving child labor",
-            "modified": "2024-12-16T15:04:16.611Z",
-            "accessLevel": "public",
-            "identifier": "WHD-16-012:027-372",
-            "issued": "2024-11-01",
-            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/child-labor",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Wage and Hour Division",
@@ -1394,46 +1372,45 @@
                     "name": "Wage and Hour Division"
                 }
             },
+            "rights": "true",
+            "title": "Outreach"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alex Cruz",
                 "hasEmail": "mailto:cruz.alexander@dol.gov"
             },
+            "description": "Investigative case data involving child labor",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "title": "Child Labor",
                     "description": "Investigative case data involving child labor",
-                    "downloadURL": "https://www.dol.gov/agencies/whd/data/charts/child-labor"
+                    "downloadURL": "https://www.dol.gov/agencies/whd/data/charts/child-labor",
+                    "mediaType": "text/csv",
+                    "title": "Child Labor"
                 }
             ],
+            "identifier": "WHD-16-012:027-372",
+            "issued": "2024-11-01",
             "keyword": [
                 "WHD",
                 "child labor"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/child-labor",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T15:04:16.611Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FMLA",
-            "description": "Three tables display data on Family and Medical Leave Act (FMLA) enforcement, including number of cases, violation instances, and reasons for violations",
-            "modified": "2024-12-16T15:17:30.309Z",
-            "accessLevel": "public",
-            "identifier": "WHD-16-012:027-373",
-            "describedByType": "text/html",
-            "issued": "2024-11-01",
-            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/fmla",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Wage and Hour Division",
@@ -1442,59 +1419,72 @@
                     "name": "Wage and Hour Division"
                 }
             },
+            "rights": "true",
+            "title": "Child Labor"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alex Cruz",
                 "hasEmail": "mailto:cruz.alexander@dol.gov"
             },
+            "describedByType": "text/html",
+            "description": "Three tables display data on Family and Medical Leave Act (FMLA) enforcement, including number of cases, violation instances, and reasons for violations",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/whd/data/charts/fmla",
-                    "title": "FMLA",
-                    "description": "Three tables display data on Family and Medical Leave Act (FMLA) enforcement, including number of cases, violation instances, and reasons for violations"
+                    "description": "Three tables display data on Family and Medical Leave Act (FMLA) enforcement, including number of cases, violation instances, and reasons for violations",
+                    "title": "FMLA"
                 }
             ],
+            "identifier": "WHD-16-012:027-373",
+            "issued": "2024-11-01",
             "keyword": [
                 "WHD",
                 "benefit",
                 "family and medical leave act",
                 "fmla"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/fmla",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T15:17:30.309Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Activities Inventory Reform (FAIR) Act Inventory",
-            "description": "Suite of advanced collaboration, information sharing, data collection, publishing, business intelligence and authentication tools and services used to facilitate cross-government collaboration and knowledge management.",
-            "modified": "2024-12-09T18:25:20.163Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM BOC-25-012:044-206",
-            "landingPage": "https://portal.max.gov/portal/home",
-            "rights": "not available",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
+                "name": "Wage and Hour Division",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
+                    "name": "Wage and Hour Division"
                 }
             },
+            "rights": "true",
+            "title": "FMLA"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Candy March",
                 "hasEmail": "mailto:march.candy.a@dol.gov"
             },
+            "description": "Suite of advanced collaboration, information sharing, data collection, publishing, business intelligence and authentication tools and services used to facilitate cross-government collaboration and knowledge management.",
+            "identifier": "OASAM BOC-25-012:044-206",
             "keyword": [
                 "BOC",
                 "Department of Labor FAIR Act",
@@ -1503,29 +1493,14 @@
                 "OASAM",
                 "P.L. 105-270"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://portal.max.gov/portal/home",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-09T18:25:20.163Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://labornetcontentdev.opadev.dol.gov/workplaceresources/policies/FAIR-Act/"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Motor Vehicle Fleet data",
-            "description": "GSA Drive Thru",
-            "modified": "2024-06-27T13:59:47.411Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM BOC-25-012:044-217",
-            "landingPage": "https://drivethru.gsa.gov/fmdtsys/dthome",
-            "rights": "restricted",
-            "spatial": "location characteristics, address",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -1534,78 +1509,82 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "references": [
+                "https://labornetcontentdev.opadev.dol.gov/workplaceresources/policies/FAIR-Act/"
+            ],
+            "rights": "not available",
+            "title": "Federal Activities Inventory Reform (FAIR) Act Inventory"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Heath Rehkop",
                 "hasEmail": "mailto:rehkop.christopher.h@dol.gov"
             },
+            "description": "GSA Drive Thru",
+            "identifier": "OASAM BOC-25-012:044-217",
             "keyword": [
                 "BOC",
                 "GSA DriveThru",
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://drivethru.gsa.gov/fmdtsys/dthome",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-06-27T13:59:47.411Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Assistant Secretary for Administration and Management",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Assistant Secretary for Administration and Management"
+                }
+            },
             "references": [
                 "https://drivethru.gsa.gov/fmdtsys/dthome"
             ],
+            "rights": "restricted",
+            "spatial": "location characteristics, address",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "Motor Vehicle Fleet data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "MDM OS Compliance Tracker",
-            "description": "DOL mobile phone users are required to maintain the most current OS version to maintain DOL's cybersecurity posture.  This data source Endpoint protection but has also been used as a source for asset management and tracking.",
-            "modified": "2024-09-23T13:03:36.345Z",
             "accessLevel": "non-public",
-            "identifier": "OASAM OCIO-25-012:044-252",
-            "rights": "private",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
-                }
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Robert Walz",
                 "hasEmail": "mailto:walz.robert@dol.gov"
             },
+            "description": "DOL mobile phone users are required to maintain the most current OS version to maintain DOL's cybersecurity posture.  This data source Endpoint protection but has also been used as a source for asset management and tracking.",
+            "identifier": "OASAM OCIO-25-012:044-252",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:03:36.345Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Library Catalog (WMS)",
-            "description": "The library catalog is shared by WLL and MSHA Technical Information Center. WMS provides a searchable catalog of holdings for patrons and administration modules for library staff.",
-            "modified": "2024-09-23T13:06:27.074Z",
-            "accessLevel": "public",
-            "identifier": "OASAM OCIO-25-012:044-270",
-            "landingPage": "https://dollibrary.on.worldcat.org/discovery",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -1614,85 +1593,83 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "title": "MDM OS Compliance Tracker"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Julie Day",
                 "hasEmail": "mailto:day.julie.a@dol.gov"
             },
+            "description": "The library catalog is shared by WLL and MSHA Technical Information Center. WMS provides a searchable catalog of holdings for patrons and administration modules for library staff.",
+            "identifier": "OASAM OCIO-25-012:044-270",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://dollibrary.on.worldcat.org/discovery",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:06:27.074Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FLSA",
-            "description": "Fair Labor Standards Act (FLSA) back wage data is broken down between minimum wage and overtime violations",
-            "modified": "2024-12-16T15:18:46.467Z",
-            "accessLevel": "public",
-            "identifier": "WHD-16-012:027-369",
-            "describedByType": "text/html",
-            "issued": "2024-11-01",
-            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/fair-labor-standards-act",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Wage and Hour Division",
+                "name": "Office of the Assistant Secretary for Administration and Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Wage and Hour Division"
+                    "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "true",
+            "title": "Library Catalog (WMS)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alex Cruz",
                 "hasEmail": "mailto:cruz.alexander@dol.gov"
             },
+            "describedByType": "text/html",
+            "description": "Fair Labor Standards Act (FLSA) back wage data is broken down between minimum wage and overtime violations",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/whd/data/charts/fair-labor-standards-act",
-                    "title": "Fair Labor Standards Act",
-                    "description": "Fair Labor Standards Act (FLSA) back wage data is broken down between minimum wage and overtime violations"
+                    "description": "Fair Labor Standards Act (FLSA) back wage data is broken down between minimum wage and overtime violations",
+                    "title": "Fair Labor Standards Act"
                 }
             ],
+            "identifier": "WHD-16-012:027-369",
+            "issued": "2024-11-01",
             "keyword": [
                 "WHD",
                 "minimum wage",
                 "overtime"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/fair-labor-standards-act",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T15:18:46.467Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Registered Farm Labor Contractor Listing",
-            "description": "List of eligible farm labor contractors certified under the Migrant and Seasonal Agricultural Worker Protection Act",
-            "modified": "2024-12-16T14:59:06.187Z",
-            "accessLevel": "public",
-            "identifier": "WHD-16-012:027-378",
-            "describedByType": "text/html",
-            "issued": "2024-12-11",
-            "landingPage": "https://www.dol.gov/agencies/whd/agriculture/mspa/farm-labor-contractors",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Wage and Hour Division",
@@ -1701,46 +1678,46 @@
                     "name": "Wage and Hour Division"
                 }
             },
+            "rights": "true",
+            "title": "FLSA"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1W",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alex Cruz",
                 "hasEmail": "mailto:cruz.alexander@dol.gov"
             },
+            "describedByType": "text/html",
+            "description": "List of eligible farm labor contractors certified under the Migrant and Seasonal Agricultural Worker Protection Act",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/whd/agriculture/mspa/farm-labor-contractors",
-                    "title": "Registered Farm Labor Contractor Listing",
-                    "description": "List of eligible farm labor contractors certified under the Migrant and Seasonal Agricultural Worker Protection Act"
+                    "description": "List of eligible farm labor contractors certified under the Migrant and Seasonal Agricultural Worker Protection Act",
+                    "title": "Registered Farm Labor Contractor Listing"
                 }
             ],
+            "identifier": "WHD-16-012:027-378",
+            "issued": "2024-12-11",
             "keyword": [
                 "FLC",
                 "WHD",
                 "agriculture"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/whd/agriculture/mspa/farm-labor-contractors",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T14:59:06.187Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "14(c)-certificate-holders",
-            "description": "Data for employers who hold or have applied for certificates issued under section 14(c) of the Fair Labor Standards Act.",
-            "modified": "2024-12-16T15:05:01.722Z",
-            "accessLevel": "public",
-            "identifier": "WHD-16-012:027-382",
-            "describedByType": "text/html",
-            "issued": "2024-12-01",
-            "landingPage": "https://www.dol.gov/agencies/whd/workers-with-disabilities/section-14c/certificate-holders",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Wage and Hour Division",
@@ -1749,102 +1726,119 @@
                     "name": "Wage and Hour Division"
                 }
             },
+            "rights": "true",
+            "title": "Registered Farm Labor Contractor Listing"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alex Cruz",
                 "hasEmail": "mailto:cruz.alexander@dol.gov"
             },
+            "describedByType": "text/html",
+            "description": "Data for employers who hold or have applied for certificates issued under section 14(c) of the Fair Labor Standards Act.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/whd/workers-with-disabilities/section-14c/certificate-holders",
-                    "title": "14(c) Certificate Holders",
-                    "description": "List of employers, and related data, for employers holding 14(c) certificates.  The certificates allow the employer to pay wages below the federal minimum wage to workers disabled for the work"
+                    "description": "List of employers, and related data, for employers holding 14(c) certificates.  The certificates allow the employer to pay wages below the federal minimum wage to workers disabled for the work",
+                    "title": "14(c) Certificate Holders"
                 }
             ],
+            "identifier": "WHD-16-012:027-382",
+            "issued": "2024-12-01",
             "keyword": [
                 "14c",
                 "Subminimum",
                 "WHD",
                 "certificate"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/whd/workers-with-disabilities/section-14c/certificate-holders",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T15:05:01.722Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "GSA Rent on the Web",
-            "description": "ROW supports GSA's strategic goal of eliminating paper while supplying timely critical billing information to client agencies. ROW allows client agencies to view their monthly bills online using web browsers. Deployed software infrastructure is minimal for client agencies and GSA. Each agency can only see their agencies current bills or historical bills that are always available. ROW currently is the only electronic means in which external agencies can view their rent bills online.",
-            "modified": "2024-06-27T13:53:01.329Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM BOC-25-012:044-212",
-            "landingPage": "https://www.gsa.gov/tools-overview/buildings-real-estate-etools/rent-on-the-web",
-            "rights": "restricted",
-            "spatial": "location characteristics, address",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
+                "name": "Wage and Hour Division",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
+                    "name": "Wage and Hour Division"
                 }
             },
+            "rights": "true",
+            "title": "14(c)-certificate-holders"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Heath Rehkop",
                 "hasEmail": "mailto:rehkop.christopher.h@dol.gov"
             },
+            "description": "ROW supports GSA's strategic goal of eliminating paper while supplying timely critical billing information to client agencies. ROW allows client agencies to view their monthly bills online using web browsers. Deployed software infrastructure is minimal for client agencies and GSA. Each agency can only see their agencies current bills or historical bills that are always available. ROW currently is the only electronic means in which external agencies can view their rent bills online.",
+            "identifier": "OASAM BOC-25-012:044-212",
             "keyword": [
                 "BOC",
                 "OASAM",
                 "ROW",
                 "gsa"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.gsa.gov/tools-overview/buildings-real-estate-etools/rent-on-the-web",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-06-27T13:53:01.329Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Assistant Secretary for Administration and Management",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Assistant Secretary for Administration and Management"
+                }
+            },
             "references": [
                 "https://www.gsa.gov/tools-overview/buildings-real-estate-etools/rent-on-the-web"
             ],
+            "rights": "restricted",
+            "spatial": "location characteristics, address",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "GSA Rent on the Web"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Senior Community Service Employment Program Performance Data",
-            "description": "Senior Community Service Employment Program (SCSEP) dataset maintains data on the performance outcomes for the state and national grantees that provide part-time subsidized work experience and training through community service positions for older workers 55 and up before transitioning to unsubsidized employment.",
-            "modified": "2021-12-03T00:00:00Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:010-455",
-            "describedBy": "https://www.dol.gov/agencies/eta/seniors/performance",
-            "landingPage": "https://www.dol.gov/agencies/eta/seniors/performance",
-            "rights": "TRUE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Employment and Training Administration"
-            },
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toni Wilson",
                 "hasEmail": "mailto:wilson.toni@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/seniors/performance",
+            "description": "Senior Community Service Employment Program (SCSEP) dataset maintains data on the performance outcomes for the state and national grantees that provide part-time subsidized work experience and training through community service positions for older workers 55 and up before transitioning to unsubsidized employment.",
+            "identifier": "ETA-5-012:010-455",
             "keyword": [
                 "ETA",
                 "community service employment",
@@ -1852,153 +1846,135 @@
                 "scsep",
                 "senior"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.dol.gov/agencies/eta/seniors/performance",
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-12-03T00:00:00Z",
             "programCode": [
                 "012:010"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Employment and Training Administration"
+            },
+            "rights": "TRUE",
+            "title": "Senior Community Service Employment Program Performance Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "DOL Fleet Management  Information System (FMIS)",
-            "description": "Automotive Utilization Tool System (AUTOS)",
-            "modified": "2024-06-27T13:58:30.164Z",
             "accessLevel": "restricted public",
-            "identifier": "OASAM BOC-25-012:044-215",
-            "landingPage": "https://autosv5.netdigitalsolutions.com",
-            "rights": "restricted",
-            "spatial": "location characteristics, address",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
-                }
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Heath Rehkop",
                 "hasEmail": "mailto:rehkop.christopher.h@dol.gov"
             },
+            "description": "Automotive Utilization Tool System (AUTOS)",
+            "identifier": "OASAM BOC-25-012:044-215",
             "keyword": [
                 "AUTOS",
                 "BOC",
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://autosv5.netdigitalsolutions.com",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-06-27T13:58:30.164Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Assistant Secretary for Administration and Management",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Assistant Secretary for Administration and Management"
+                }
+            },
             "references": [
                 "https://autosv5.netdigitalsolutions.com"
             ],
+            "rights": "restricted",
+            "spatial": "location characteristics, address",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "DOL Fleet Management  Information System (FMIS)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Surplusing of federal property and acquisitions of surplused property",
-            "description": "PPMS.gov, Personal Property Management System",
-            "modified": "2024-06-27T13:49:58.629Z",
             "accessLevel": "restricted public",
-            "identifier": "OASAM BOC-25-012:044-687",
-            "landingPage": "https://PPMS.gov",
-            "rights": "restricted",
-            "spatial": "location characteristics, address",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
-                }
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Darcell Hardaway",
                 "hasEmail": "mailto:hardaway.darcell.l@dol.gov"
             },
+            "description": "PPMS.gov, Personal Property Management System",
+            "identifier": "OASAM BOC-25-012:044-687",
             "keyword": [
                 "BOC",
                 "OASAM",
                 "PPMS.gov"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://PPMS.gov",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-06-27T13:49:58.629Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Assistant Secretary for Administration and Management",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Assistant Secretary for Administration and Management"
+                }
+            },
             "references": [
                 "https://gsaxcess.gov/"
             ],
+            "rights": "restricted",
+            "spatial": "location characteristics, address",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "Surplusing of federal property and acquisitions of surplused property"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "E-Forms",
-            "description": "This is a common database used by multiple applications and itself does not have an application interface. It is used together with identification to house the latest federal employee information including their names, SSN, location, address, pay grade and level, and other personnel and payroll information.",
-            "modified": "2022-09-29T17:22:55.260Z",
             "accessLevel": "non-public",
-            "identifier": "OASAM OCIO-25-012:044-265",
-            "rights": "not available",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
-                }
-            },
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Watt-Thomas, Norma Vazquez",
                 "hasEmail": "mailto:thomas.watts.linda@dol.gov"
             },
+            "description": "This is a common database used by multiple applications and itself does not have an application interface. It is used together with identification to house the latest federal employee information including their names, SSN, location, address, pay grade and level, and other personnel and payroll information.",
+            "identifier": "OASAM OCIO-25-012:044-265",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-09-29T17:22:55.260Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "PMC Tracker",
-            "description": "This is an Excel file that captures actual dates for PMC business processes relevant to GPRMA and key PMC lines of business.",
-            "modified": "2024-09-23T13:51:46.418Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM PMC-25-012:044-291",
-            "landingPage": "https://usdol.sharepoint.com/:x:/s/T-OASAM-PMC-PerformanceTeam/EYHIsB1pcyxOmSOgaqid2j4BHe6raXe1Y4if3pOzikFXMQ?e=gw0feL",
-            "rights": "private",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -2007,89 +1983,102 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "not available",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "E-Forms"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lisa Landres",
                 "hasEmail": "mailto:landres.lisa@dol.gov"
             },
+            "description": "This is an Excel file that captures actual dates for PMC business processes relevant to GPRMA and key PMC lines of business.",
+            "identifier": "OASAM PMC-25-012:044-291",
             "keyword": [
                 "OASAM",
                 "PMC"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://usdol.sharepoint.com/:x:/s/T-OASAM-PMC-PerformanceTeam/EYHIsB1pcyxOmSOgaqid2j4BHe6raXe1Y4if3pOzikFXMQ?e=gw0feL",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:51:46.418Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "OCFT Common Indicators (Education, Livelihoods, Capacity)",
-            "description": "OCFT tracks three common indicators that grantees report progress on (as applicable). The three indicators are related to education service provision, livelihood service provision, and country capacity built. These have been tracked routinely since the indicators were developed.",
-            "modified": "2021-07-14T14:50:31.586Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-133",
-            "landingPage": "https://www.dol.gov/agencies/ilab/projects",
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Bureau of International Labor Affairs",
+                "name": "Office of the Assistant Secretary for Administration and Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Bureau of International Labor Affairs"
+                    "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "title": "PMC Tracker"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Doris Senko",
                 "hasEmail": "mailto:senko.doris@dol.gov"
             },
+            "description": "OCFT tracks three common indicators that grantees report progress on (as applicable). The three indicators are related to education service provision, livelihood service provision, and country capacity built. These have been tracked routinely since the indicators were developed.",
+            "identifier": "ILAB-12-012:037-133",
             "keyword": [
                 "ILAB"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/ilab/projects",
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-07-14T14:50:31.586Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://www.dol.gov/agencies/ilab/projects"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Master Listing of Aggregated Grant Data",
-            "description": "Listing of cooperative agreements, funding amount, period of performance, and grantee from grant inception through present",
-            "modified": "2021-01-25T21:56:48.505Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-136",
-            "landingPage": "https://www.dol.gov/agencies/ilab/projects",
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of International Labor Affairs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Bureau of International Labor Affairs"
                 }
             },
+            "references": [
+                "https://www.dol.gov/agencies/ilab/projects"
+            ],
+            "rights": "true",
+            "title": "OCFT Common Indicators (Education, Livelihoods, Capacity)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Doris Senko",
                 "hasEmail": "mailto:senko.doris@dol.gov"
             },
+            "description": "Listing of cooperative agreements, funding amount, period of performance, and grantee from grant inception through present",
+            "identifier": "ILAB-12-012:037-136",
             "keyword": [
                 "Child Labor",
                 "Child labor",
@@ -2099,29 +2088,15 @@
                 "forced labor",
                 "supply chain"
             ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
-            ],
+            "landingPage": "https://www.dol.gov/agencies/ilab/projects",
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://www.dol.gov/agencies/ilab/projects"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "List of Goods Produced by Child Labor or Forced Labor",
-            "description": "Available on website, has all the reports published since 2009. \nAlso provides bibliography and list in Excel format\nhttps://www.dol.gov/agencies/ilab/reports/child-labor/list-of-goods",
-            "modified": "2021-01-27T21:20:59.912Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-141",
-            "landingPage": "https://www.dol.gov/agencies/ilab/reports/child-labor/list-of-goods",
             "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
+            "modified": "2021-01-25T21:56:48.505Z",
+            "programCode": [
+                "015:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of International Labor Affairs",
@@ -2130,73 +2105,77 @@
                     "name": "Department of Labor"
                 }
             },
+            "references": [
+                "https://www.dol.gov/agencies/ilab/projects"
+            ],
+            "rights": "true",
+            "title": "Master Listing of Aggregated Grant Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jon Underdahl-Peirce",
                 "hasEmail": "mailto:peirce.jon.r@dol.gov"
             },
+            "description": "Available on website, has all the reports published since 2009. \nAlso provides bibliography and list in Excel format\nhttps://www.dol.gov/agencies/ilab/reports/child-labor/list-of-goods",
+            "identifier": "ILAB-12-012:037-141",
             "keyword": [
                 "ILAB",
                 "child labor",
                 "forced labor"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/ilab/reports/child-labor/list-of-goods",
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-01-27T21:20:59.912Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "List of Products Produced by Forced or Indentured Child Labor",
-            "description": "Available on website.  Also provides bibliography and list in Excel format.\nhttps://www.dol.gov/agencies/ilab/reports/child-labor/list-of-products",
-            "modified": "2021-01-27T21:26:05.218Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-142",
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of International Labor Affairs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Bureau of International Labor Affairs"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "List of Goods Produced by Child Labor or Forced Labor"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jon Underdahl-Peirce",
                 "hasEmail": "mailto:peirce.jon.r@dol.gov"
             },
+            "description": "Available on website.  Also provides bibliography and list in Excel format.\nhttps://www.dol.gov/agencies/ilab/reports/child-labor/list-of-products",
+            "identifier": "ILAB-12-012:037-142",
             "keyword": [
                 "ILAB",
                 "child labor",
                 "forced child labor",
                 "forced labor"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-01-27T21:26:05.218Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public Submissions for Child Labor and Forced Labor Reporting",
-            "description": "Available on website, list of public submissions.\nhttps://www.dol.gov/agencies/ilab/public-submissions-child-labor-forced-labor-reporting",
-            "modified": "2021-07-15T21:06:55.548Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-143",
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of International Labor Affairs",
@@ -2205,156 +2184,155 @@
                     "name": "Bureau of International Labor Affairs"
                 }
             },
+            "rights": "true",
+            "title": "List of Products Produced by Forced or Indentured Child Labor"
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
                 "fn": "Jon Underdahl-Peirce",
                 "hasEmail": "mailto:peirce.jon.r@dol.gov"
             },
+            "description": "Available on website, list of public submissions.\nhttps://www.dol.gov/agencies/ilab/public-submissions-child-labor-forced-labor-reporting",
+            "identifier": "ILAB-12-012:037-143",
             "keyword": [
                 "ILAB",
                 "child labor",
                 "forced child labor",
                 "forced labor"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-07-15T21:06:55.548Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of International Labor Affairs",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Bureau of International Labor Affairs"
+                }
+            },
+            "rights": "true",
+            "title": "Public Submissions for Child Labor and Forced Labor Reporting"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Job Banks data",
-            "description": "Job Banks data is a list of URLs for state electronic job bank.\n\nCareerOneStop.org web service available upon request",
-            "modified": "2022-12-19T00:00:00Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:018-452",
-            "landingPage": "https://www.careeronestop.org/JobSearch/FindJobs/state-job-banks.aspx",
-            "rights": "TRUE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Employment and Training Administration"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Steve Rietzke",
                 "hasEmail": "mailto:rietzke.steven@dol.gov"
             },
+            "description": "Job Banks data is a list of URLs for state electronic job bank.\n\nCareerOneStop.org web service available upon request",
+            "identifier": "ETA-5-012:018-452",
             "keyword": [
                 "job banks"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.careeronestop.org/JobSearch/FindJobs/state-job-banks.aspx",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-12-19T00:00:00Z",
             "programCode": [
                 "012:018"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Employment and Training Administration"
+            },
+            "rights": "TRUE",
+            "title": "Job Banks data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Longshore Audited Financial Statements",
-            "description": "Financial Statements and Independent Auditor's Report",
-            "modified": "2021-02-02T21:56:40.203Z",
             "accessLevel": "public",
-            "identifier": "OCFO-12-012:044-296",
-            "landingPage": "https://www.oig.dol.gov/cgi-bin/oa_rpts-v4.cgi?s=&y=2017&a=all",
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Published",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Department of Energy"
-                }
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jennifer Maurer",
                 "hasEmail": "mailto:maurer.jennifer@dol.gov"
             },
+            "description": "Financial Statements and Independent Auditor's Report",
+            "identifier": "OCFO-12-012:044-296",
             "keyword": [
                 "ocfo"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.oig.dol.gov/cgi-bin/oa_rpts-v4.cgi?s=&y=2017&a=all",
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-02-02T21:56:40.203Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Agriculture",
-            "description": "Five tables display enforcement data broken down by Act or group of Acts.  Data points include number of investigations, employees receiving back wages, and back wages",
-            "modified": "2024-12-16T15:12:20.272Z",
-            "accessLevel": "public",
-            "identifier": "WHD-16-012:027-374",
-            "describedByType": "text/html",
-            "issued": "2024-11-01",
-            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/agriculture",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Wage and Hour Division",
+                "name": "Published",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Wage and Hour Division"
+                    "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "title": "Longshore Audited Financial Statements"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alex Cruz",
                 "hasEmail": "mailto:cruz.alexander@dol.gov"
             },
+            "describedByType": "text/html",
+            "description": "Five tables display enforcement data broken down by Act or group of Acts.  Data points include number of investigations, employees receiving back wages, and back wages",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/whd/data/charts/agriculture",
-                    "title": "Agriculture",
-                    "description": "Five tables display enforcement data broken down by Act or group of Acts.  Data points include number of investigations, employees receiving back wages, and back wages"
+                    "description": "Five tables display enforcement data broken down by Act or group of Acts.  Data points include number of investigations, employees receiving back wages, and back wages",
+                    "title": "Agriculture"
                 }
             ],
+            "identifier": "WHD-16-012:027-374",
+            "issued": "2024-11-01",
             "keyword": [
                 "H-2A",
                 "MSPA",
                 "WHD",
                 "agriculture"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/agriculture",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T15:12:20.272Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "H-1B",
-            "description": "Investigative case data involving H-1B non-immigrant visas",
-            "modified": "2024-12-16T15:07:40.012Z",
-            "accessLevel": "public",
-            "identifier": "WHD-16-012:027-376",
-            "issued": "2024-11-01",
-            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/h-1b",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Wage and Hour Division",
@@ -2363,86 +2341,83 @@
                     "name": "Wage and Hour Division"
                 }
             },
+            "rights": "true",
+            "title": "Agriculture"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alex Cruz",
                 "hasEmail": "mailto:cruz.alexander@dol.gov"
             },
+            "description": "Investigative case data involving H-1B non-immigrant visas",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/whd/data/charts/h-1b",
-                    "title": "H-1B",
-                    "description": "Investigative case data involving H-1B non-immigrant visas"
+                    "description": "Investigative case data involving H-1B non-immigrant visas",
+                    "title": "H-1B"
                 }
             ],
+            "identifier": "WHD-16-012:027-376",
+            "issued": "2024-11-01",
             "keyword": [
                 "H-1B",
                 "WHD"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/h-1b",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T15:07:40.012Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Records Transfer Requests to the Federal Records Centers and Reference Requests",
-            "description": "Archives and Records Centers Information System (ARCIS)\nOnline portal through which DOL conduct business with the Federal Records Centers.",
-            "modified": "2024-09-23T13:09:01.783Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM BOC-25-012:044-202",
-            "landingPage": "https://arcis.archives.gov/arcis/start.swe?SWECmd=Start&SWEHo=arcis.archives.gov",
-            "rights": "restricted",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
+                "name": "Wage and Hour Division",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
+                    "name": "Wage and Hour Division"
                 }
             },
+            "rights": "true",
+            "title": "H-1B"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Steven Pierce",
                 "hasEmail": "mailto:pierce.steven@dol.gov"
             },
+            "description": "Archives and Records Centers Information System (ARCIS)\nOnline portal through which DOL conduct business with the Federal Records Centers.",
+            "identifier": "OASAM BOC-25-012:044-202",
             "keyword": [
                 "ARCIS",
                 "Archives and Records Centers Information System",
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://arcis.archives.gov/arcis/start.swe?SWECmd=Start&SWEHo=arcis.archives.gov",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:09:01.783Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://arcis.archives.gov/arcis/start.swe?SWECmd=Start&SWEHo=arcis.archives.gov"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "energy use water use facility audit findings costs Measurement and Verification",
-            "description": "DOE/FEMP - EISA 432 Compliance Tracking System (CTS).  For reporting statutory compliance with EISA Section 432 energy and water conservation requirements.",
-            "modified": "2024-09-23T16:00:00.009Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM BOC-25-012:044-223",
-            "landingPage": "https://www.eisa-432-cts.eere.energy.gov/EISACTS/Login.aspx?ReturnUrl=%2fEISACTS",
-            "rights": "restricted",
-            "spatial": "location characteristics, address",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -2451,55 +2426,70 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "references": [
+                "https://arcis.archives.gov/arcis/start.swe?SWECmd=Start&SWEHo=arcis.archives.gov"
+            ],
+            "rights": "restricted",
+            "title": "Records Transfer Requests to the Federal Records Centers and Reference Requests"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kathryn Simpson, (Sustainability Analyst)",
                 "hasEmail": "mailto:simpson.kathryn.j@dol.gov"
             },
+            "description": "DOE/FEMP - EISA 432 Compliance Tracking System (CTS).  For reporting statutory compliance with EISA Section 432 energy and water conservation requirements.",
+            "identifier": "OASAM BOC-25-012:044-223",
             "keyword": [
                 "BOC",
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.eisa-432-cts.eere.energy.gov/EISACTS/Login.aspx?ReturnUrl=%2fEISACTS",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T16:00:00.009Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Assistant Secretary for Administration and Management",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Assistant Secretary for Administration and Management"
+                }
+            },
             "references": [
                 "https://www.eisa-432-cts.eere.energy.gov/EISACTS/Login.aspx?ReturnUrl=%2fEISACTS"
             ],
+            "rights": "restricted",
+            "spatial": "location characteristics, address",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "energy use water use facility audit findings costs Measurement and Verification"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Payroll",
-            "description": "OPM-certified Payroll Shared Service Center (SSC)",
-            "modified": "2024-09-23T13:37:20.415Z",
             "accessLevel": "non-public",
-            "identifier": "OASAM OHR-25-012:044-240",
-            "rights": "private",
-            "spatial": "location characteristics, addresses",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
-                }
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LaRell Faulkner",
                 "hasEmail": "mailto:Faulkner.Larell@dol.gov"
             },
+            "description": "OPM-certified Payroll Shared Service Center (SSC)",
+            "identifier": "OASAM OHR-25-012:044-240",
             "keyword": [
                 "HR data",
                 "Human Capital Data",
@@ -2509,29 +2499,13 @@
                 "hr",
                 "tna"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:37:20.415Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "WebTA",
-            "description": "Time and Attendance System",
-            "modified": "2024-09-23T13:38:36.949Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OHR-25-012:044-243",
-            "landingPage": "https://doltime.dol.gov/webta",
-            "rights": "private",
-            "spatial": "location characteristics",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -2540,37 +2514,41 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "spatial": "location characteristics, addresses",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Payroll"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LaRell Faulkner",
                 "hasEmail": "mailto:Faulkner.Larell@dol.gov"
             },
+            "description": "Time and Attendance System",
+            "identifier": "OASAM OHR-25-012:044-243",
             "keyword": [
                 "OASAM",
                 "OHR",
                 "WebTA",
                 "time and attendance"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://doltime.dol.gov/webta",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:38:36.949Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "LER internal tracking",
-            "description": "LER Case Inventory System",
-            "modified": "2022-09-29T19:09:08.189Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OHR-25-012:044-244",
-            "landingPage": "https://dol-lerms.entellitrak.com/etk-dol-lerms-prod/login.request.do",
-            "rights": "not available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -2579,12 +2557,24 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "spatial": "location characteristics",
+            "title": "WebTA"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Shawn Hooper",
                 "hasEmail": "mailto:Hooper.Shawn@dol.gov"
             },
+            "description": "LER Case Inventory System",
+            "identifier": "OASAM OHR-25-012:044-244",
             "keyword": [
                 "LERMS",
                 "OASAM",
@@ -2592,194 +2582,179 @@
                 "labor employee relations",
                 "labor management"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://dol-lerms.entellitrak.com/etk-dol-lerms-prod/login.request.do",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-09-29T19:09:08.189Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://dol-lerms.entellitrak.com/etk-dol-lerms-prod/login.request.do"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Performance Evaluations of OCFT-funded Projects",
-            "description": "Performance Evaluations - qualitative evaluations of cooperative agreement projects, usually at the midpoint and end of project performance.",
-            "modified": "2021-01-25T19:49:12.416Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-134",
-            "landingPage": "https://www.dol.gov/agencies/ilab/performance-monitoring-accountability",
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Bureau of International Labor Affairs",
+                "name": "Office of the Assistant Secretary for Administration and Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "references": [
+                "https://dol-lerms.entellitrak.com/etk-dol-lerms-prod/login.request.do"
+            ],
+            "rights": "not available",
+            "title": "LER internal tracking"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Maureen Jaffe",
                 "hasEmail": "mailto:jaffe.maureen@dol.gov"
             },
+            "description": "Performance Evaluations - qualitative evaluations of cooperative agreement projects, usually at the midpoint and end of project performance.",
+            "identifier": "ILAB-12-012:037-134",
             "keyword": [
                 "ILAB",
                 "evaluation"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/ilab/performance-monitoring-accountability",
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-01-25T19:49:12.416Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Permanent Records Transfers to the National Archives and Records Retention Schedules",
-            "description": "Electronic Records Archive (ERA)\nOnline portal through which DOL conduct business new system that allows Federal agencies to perform critical records management transactions  with the National Archives and Records Administration",
-            "modified": "2024-09-23T13:09:56.102Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM BOC-25-012:044-203",
-            "landingPage": "https://www.archives.gov/records-mgmt/era",
-            "rights": "restricted",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
+                "name": "Bureau of International Labor Affairs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Performance Evaluations of OCFT-funded Projects"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Steven Pierce",
                 "hasEmail": "mailto:pierce.steven@dol.gov"
             },
+            "description": "Electronic Records Archive (ERA)\nOnline portal through which DOL conduct business new system that allows Federal agencies to perform critical records management transactions  with the National Archives and Records Administration",
+            "identifier": "OASAM BOC-25-012:044-203",
             "keyword": [
                 "ERA",
                 "Electronic Records Archive",
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.archives.gov/records-mgmt/era",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:09:56.102Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://www.archives.gov/records-mgmt/era"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Engineering Support Contractor Information System (ESCIS)",
-            "description": "Data repository for ETA Job Corps Center Facility Information, DOL's real property portfolio, and GSA occupancy agreements",
-            "modified": "2024-12-06T13:21:37.846Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM BOC-25-012:044-208",
-            "rights": "private",
-            "spatial": "location characteristics, address",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Employment and Training Administration",
+                "name": "Office of the Assistant Secretary for Administration and Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Employment and Training Administration"
+                    "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "references": [
+                "https://www.archives.gov/records-mgmt/era"
+            ],
+            "rights": "restricted",
+            "title": "Permanent Records Transfers to the National Archives and Records Retention Schedules"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Derrek Sanks",
                 "hasEmail": "mailto:sanks.derrek.d@dol.gov"
             },
+            "description": "Data repository for ETA Job Corps Center Facility Information, DOL's real property portfolio, and GSA occupancy agreements",
+            "identifier": "OASAM BOC-25-012:044-208",
             "keyword": [
                 "BOC",
                 "ESCIS",
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-06T13:21:37.846Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Employment and Training Administration",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Employment and Training Administration"
+                }
+            },
             "references": [
                 "https://eta-arl-papps1/eschome/"
             ],
+            "rights": "private",
+            "spatial": "location characteristics, address",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "Engineering Support Contractor Information System (ESCIS)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "MAX.gov",
-            "description": "MAX.gov government-wide suite of advanced collaboration, information sharing, data collection, publishing, business intelligence and authentication tools and services used to facilitate cross-government collaboration and knowledge management.",
-            "modified": "2024-12-06T13:19:25.640Z",
             "accessLevel": "restricted public",
-            "identifier": "OASAM BOC-25-012:044-209",
-            "landingPage": "https://login.max.gov",
-            "rights": "restricted",
-            "spatial": "location characteristics",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
-                }
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daniel Cornish",
                 "hasEmail": "mailto:cornish.daniel.f@dol.gov"
             },
+            "description": "MAX.gov government-wide suite of advanced collaboration, information sharing, data collection, publishing, business intelligence and authentication tools and services used to facilitate cross-government collaboration and knowledge management.",
+            "identifier": "OASAM BOC-25-012:044-209",
             "keyword": [
                 "BOC",
                 "MAX",
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://login.max.gov",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-06T13:19:25.640Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://max.gov"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "LearningLink",
-            "description": "DOL's e-Training solution which provides employees access to a one-stop portal of training programs and services. LearningLink supports business and management processes by providing agencies, staff, and customers with single-site access for the management, delivery, and development of learning and knowledge.",
-            "modified": "2024-09-23T13:22:44.919Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OHR-25-012:044-239",
-            "landingPage": "https://labornet.dol.gov/learninglink/",
-            "rights": "not available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -2788,12 +2763,27 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "references": [
+                "https://max.gov"
+            ],
+            "rights": "restricted",
+            "spatial": "location characteristics",
+            "title": "MAX.gov"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jwalant Ariyal",
                 "hasEmail": "mailto:Arjyal.Jwalant@dol.gov"
             },
+            "description": "DOL's e-Training solution which provides employees access to a one-stop portal of training programs and services. LearningLink supports business and management processes by providing agencies, staff, and customers with single-site access for the management, delivery, and development of learning and knowledge.",
+            "identifier": "OASAM OHR-25-012:044-239",
             "keyword": [
                 "OASAM",
                 "OCIO",
@@ -2801,27 +2791,14 @@
                 "courses",
                 "training"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://labornet.dol.gov/learninglink/",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:22:44.919Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ServiceNow",
-            "description": "Automation of Enterprise Services customer/employee experiences. Called a Universal Service Management Tool (USMT), ServiceNow is an ITIL-compliant workflow system and database for managing user incidents and problems, IT hardware and software changes, hardware and software assets, and change management processes for the DOL IT infrastructure.  ServiceNow also supports several Agency application Help Desks.",
-            "modified": "2024-12-09T18:23:31.150Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OCIO-25-012:044-246",
-            "describedBy": "https://service.dol.gov/ocio_esd_sp?id=kb_view",
-            "landingPage": "https://service.dol.gov/",
-            "rights": "private",
-            "spatial": "location characteristics, addresses",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -2830,12 +2807,24 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "not available",
+            "title": "LearningLink"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sudha N Ayyangar",
                 "hasEmail": "mailto:ayyangar.sudha.n@dol.gov"
             },
+            "describedBy": "https://service.dol.gov/ocio_esd_sp?id=kb_view",
+            "description": "Automation of Enterprise Services customer/employee experiences. Called a Universal Service Management Tool (USMT), ServiceNow is an ITIL-compliant workflow system and database for managing user incidents and problems, IT hardware and software changes, hardware and software assets, and change management processes for the DOL IT infrastructure.  ServiceNow also supports several Agency application Help Desks.",
+            "identifier": "OASAM OCIO-25-012:044-246",
             "keyword": [
                 "Desktop inventory",
                 "ESD",
@@ -2852,28 +2841,14 @@
                 "troubleshoot",
                 "troubleshooting"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://service.dol.gov/",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-09T18:23:31.150Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Folio",
-            "description": "Folio is a shared service application that enables government agencies to manage their IT projects, programs, portfolios and submit the IT Budget to OMB. The General Service Administration (GSA) manages the Folio application in collaboration with the 18 member agencies. OMB requires agencies to track and report on realized cost savings / avoidance as part of the IT investment submission. \n(previously titled: Electronic Capital Planning Investment Control (eCPIC))",
-            "modified": "2024-09-23T13:17:53.669Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM OCIO-25-012:044-253",
-            "landingPage": "https://dol.folio.ecpic.gov/home",
-            "rights": "restricted",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -2882,163 +2857,159 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "spatial": "location characteristics, addresses",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "ServiceNow"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Traci Smith",
                 "hasEmail": "mailto:smith.traci@dol.gov"
             },
+            "description": "Folio is a shared service application that enables government agencies to manage their IT projects, programs, portfolios and submit the IT Budget to OMB. The General Service Administration (GSA) manages the Folio application in collaboration with the 18 member agencies. OMB requires agencies to track and report on realized cost savings / avoidance as part of the IT investment submission. \n(previously titled: Electronic Capital Planning Investment Control (eCPIC))",
+            "identifier": "OASAM OCIO-25-012:044-253",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://dol.folio.ecpic.gov/home",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:17:53.669Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "E-Travel System",
-            "description": "DOL Travel System for case management system for travel request",
-            "modified": "2021-02-02T22:05:35.032Z",
-            "accessLevel": "non-public",
-            "identifier": "OCFO-DOL wide -012:044-299",
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Chief Financial Officer",
+                "name": "Office of the Assistant Secretary for Administration and Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Energy"
+                    "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "restricted",
+            "title": "Folio"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sheila Alexander",
                 "hasEmail": "mailto:alexander.shelia@dol.gov"
             },
+            "description": "DOL Travel System for case management system for travel request",
+            "identifier": "OCFO-DOL wide -012:044-299",
             "keyword": [
                 "ocfo"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-02-02T22:05:35.032Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Real Property Profile (FRPP) (GSA-DOL)",
-            "description": "Government-wide real property inventory / data collection system.  Information on DOL Owned and Direct leased properties",
-            "modified": "2024-09-23T13:56:56.025Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM BOC-25-012:044-210",
-            "landingPage": "https://www.realpropertyprofile.gov/FRPPMS",
-            "rights": "restricted",
-            "spatial": "location characteristics, address",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
+                "name": "Office of Chief Financial Officer",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
+                    "name": "Department of Energy"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "E-Travel System"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daniel Cornish",
                 "hasEmail": "mailto:cornish.daniel.f@dol.gov"
             },
+            "description": "Government-wide real property inventory / data collection system.  Information on DOL Owned and Direct leased properties",
+            "identifier": "OASAM BOC-25-012:044-210",
             "keyword": [
                 "BOC",
                 "FRPP",
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.realpropertyprofile.gov/FRPPMS",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:56:56.025Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Assistant Secretary for Administration and Management",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Assistant Secretary for Administration and Management"
+                }
+            },
             "references": [
                 "https://www.realpropertyprofile.gov/FRPPMS"
             ],
+            "rights": "restricted",
+            "spatial": "location characteristics, address",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "Federal Real Property Profile (FRPP) (GSA-DOL)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "eRETA",
-            "description": "The external RWA Entry and Tracking Application (eRETA) is the customer portal for RWA information integrated with GSA's financial management system, providing users real-time access to RWA project and financial information. Federal customers are required to send all RWA and RWA Work Request information to GSA via eRETA.",
-            "modified": "2024-12-06T13:30:41.232Z",
             "accessLevel": "restricted public",
-            "identifier": "OASAM BOC-25-012:044-211",
-            "landingPage": "https://extportal.pbs.gsa.gov",
-            "rights": "restricted",
-            "spatial": "location characteristics, address",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
-                }
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Heath Rehkop",
                 "hasEmail": "mailto:rehkop.christopher.h@dol.gov"
             },
+            "description": "The external RWA Entry and Tracking Application (eRETA) is the customer portal for RWA information integrated with GSA's financial management system, providing users real-time access to RWA project and financial information. Federal customers are required to send all RWA and RWA Work Request information to GSA via eRETA.",
+            "identifier": "OASAM BOC-25-012:044-211",
             "keyword": [
                 "BOC",
                 "OASAM",
                 "RWA",
                 "eRETA"
             ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
-            ],
+            "landingPage": "https://extportal.pbs.gsa.gov",
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://extportal.pbs.gsa.gov"
+            "modified": "2024-12-06T13:30:41.232Z",
+            "programCode": [
+                "015:001"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Complaint Tracking and Reporting System - External Enforcement Module",
-            "description": "A computerized system used by Civil Rights Center management and employees to record and track Equal Opportunity (EO) complaints alleging discrimination in programs and activities that receive DOL Federal financial assistance or alleging discrimination by public entities that operate programs related to labor and the work force.",
-            "modified": "2024-09-23T12:38:16.446Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM CRC-25-012:044-226",
-            "landingPage": "https://cmp.dol.gov/suite/sites/ctrs-tl6",
-            "rights": "private",
-            "spatial": "location characteristics, address",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -3047,39 +3018,42 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "references": [
+                "https://extportal.pbs.gsa.gov"
+            ],
+            "rights": "restricted",
+            "spatial": "location characteristics, address",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "eRETA"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Carlton Brown",
                 "hasEmail": "mailto:brown.carlton@dol.gov"
             },
+            "description": "A computerized system used by Civil Rights Center management and employees to record and track Equal Opportunity (EO) complaints alleging discrimination in programs and activities that receive DOL Federal financial assistance or alleging discrimination by public entities that operate programs related to labor and the work force.",
+            "identifier": "OASAM CRC-25-012:044-226",
             "keyword": [
                 "CRC",
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://cmp.dol.gov/suite/sites/ctrs-tl6",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T12:38:16.446Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Reasonable Accommodation Tracking and Reporting System",
-            "description": "The Reasonable Accommodation Tracking System (RATS) is an electronic system for processing reasonable accommodation requests.  RATS allows the Reasonable Accommodation Resource Center to organize data to determine trends, fulfill the DLMS recordkeeping requirements, maintain a centralized repository of information, track when future action is needed (such as purchasing software upgrades), and allows for quick reference on the status and resolution of a request.",
-            "modified": "2024-12-06T13:54:00.142Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM CRC-25-012:044-227",
-            "landingPage": "https://usdol.sharepoint.com/sites/OASAM-CRC-RARC/SitePages/Home.aspx",
-            "rights": "private",
-            "spatial": "location characteristics, addresses",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -3088,37 +3062,39 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "spatial": "location characteristics, address",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Complaint Tracking and Reporting System - External Enforcement Module"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Samuel Rhames",
                 "hasEmail": "mailto:rhames.samuel@dol.gov"
             },
+            "description": "The Reasonable Accommodation Tracking System (RATS) is an electronic system for processing reasonable accommodation requests.  RATS allows the Reasonable Accommodation Resource Center to organize data to determine trends, fulfill the DLMS recordkeeping requirements, maintain a centralized repository of information, track when future action is needed (such as purchasing software upgrades), and allows for quick reference on the status and resolution of a request.",
+            "identifier": "OASAM CRC-25-012:044-227",
             "keyword": [
                 "OASAM",
                 "WECO"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://usdol.sharepoint.com/sites/OASAM-CRC-RARC/SitePages/Home.aspx",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-06T13:54:00.142Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "DOL Emergency Response Group Member Information Form Inventory",
-            "description": "This is an Excel file that inventories signed DL-6068 Emergency Response Group Member Information Forms and captures who has been formally designated as a DOL Emergency Response Group member.",
-            "modified": "2024-09-23T12:49:31.750Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM EMC-25-012:044-232",
-            "rights": "not available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -3127,34 +3103,38 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "spatial": "location characteristics, addresses",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Reasonable Accommodation Tracking and Reporting System"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Smith",
                 "hasEmail": "mailto:smith.michael.b@dol.gov"
             },
+            "description": "This is an Excel file that inventories signed DL-6068 Emergency Response Group Member Information Forms and captures who has been formally designated as a DOL Emergency Response Group member.",
+            "identifier": "OASAM EMC-25-012:044-232",
             "keyword": [
                 "EMC",
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T12:49:31.750Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "DOL Continiuty Shared Drive Rules of Behavior Form Inventory",
-            "description": "This is an Excel file that inventories signed DL-6075 / DL-6075a Continuity Shared Drive (CSD) Rules of Behavior Forms and captures who is authorized to grant access to Agency and Regional information on the CSD.",
-            "modified": "2024-04-11T17:02:20.750Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM EMC-25-012:044-233",
-            "rights": "not available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -3163,36 +3143,34 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "not available",
+            "title": "DOL Emergency Response Group Member Information Form Inventory"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Smith",
                 "hasEmail": "mailto:smith.michael.b@dol.gov"
             },
+            "description": "This is an Excel file that inventories signed DL-6075 / DL-6075a Continuity Shared Drive (CSD) Rules of Behavior Forms and captures who is authorized to grant access to Agency and Regional information on the CSD.",
+            "identifier": "OASAM EMC-25-012:044-233",
             "keyword": [
                 "EMC",
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-04-11T17:02:20.750Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Labor Employee Relations Management Systems 2.0 (LERMS 2.0)",
-            "description": "LERMS provides all the Office of Employee Labor Management Relations (DELMR) the ability to standardize processes and centralize its data to significantly improve the collection, management and reporting capabilities of the organization.  LERMS gives OELMR the ability to collect pertinent data related to cases and subsequently produce reports for DOL management to fulfill their annual reporting requirements.",
-            "modified": "2024-09-23T13:47:29.141Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OCIO-25-012:044-244",
-            "landingPage": "https://dol-lerms.entellitrak.com/etk-dol-lerms-prod/login.request.do",
-            "rights": "private",
-            "spatial": "location characteristics, addresses",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -3201,12 +3179,23 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "not available",
+            "title": "DOL Continiuty Shared Drive Rules of Behavior Form Inventory"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sheila DeMartiNo",
                 "hasEmail": "mailto:demartiNo.sheila@dol.gov"
             },
+            "description": "LERMS provides all the Office of Employee Labor Management Relations (DELMR) the ability to standardize processes and centralize its data to significantly improve the collection, management and reporting capabilities of the organization.  LERMS gives OELMR the ability to collect pertinent data related to cases and subsequently produce reports for DOL management to fulfill their annual reporting requirements.",
+            "identifier": "OASAM OCIO-25-012:044-244",
             "keyword": [
                 "LERMS",
                 "OASAM",
@@ -3214,28 +3203,14 @@
                 "labor employee relations",
                 "management system"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://dol-lerms.entellitrak.com/etk-dol-lerms-prod/login.request.do",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:47:29.141Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "OIG Recommendations Tracker",
-            "description": "This spreadsheet tracks the quarterly status of a subset of open OIG recommendations.",
-            "modified": "2024-09-23T13:50:54.126Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM PMC-25-012:044-289",
-            "landingPage": "https://usdol.sharepoint.com/:f:/s/T-OASAM-PMC-PerformanceTeam/EoKH0R4Mz0pMmfRgH2bNXJsBQPnqzYNl-Id1b8hgrEHV4g?e=Zf16ax",
-            "rights": "restricted",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -3244,86 +3219,104 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "spatial": "location characteristics, addresses",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Labor Employee Relations Management Systems 2.0 (LERMS 2.0)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rebecca MacMillan",
                 "hasEmail": "mailto:macmillan.rebecca.l@dol.gov"
             },
+            "description": "This spreadsheet tracks the quarterly status of a subset of open OIG recommendations.",
+            "identifier": "OASAM PMC-25-012:044-289",
             "keyword": [
                 "OASAM",
                 "OIG",
                 "PMC"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://usdol.sharepoint.com/:f:/s/T-OASAM-PMC-PerformanceTeam/EoKH0R4Mz0pMmfRgH2bNXJsBQPnqzYNl-Id1b8hgrEHV4g?e=Zf16ax",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:50:54.126Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Findings on the Worst Forms of Child Labor",
-            "description": "Available on website, has all the reports published since 2001",
-            "modified": "2021-01-27T21:17:37.417Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-140",
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Bureau of International Labor Affairs",
+                "name": "Office of the Assistant Secretary for Administration and Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "restricted",
+            "title": "OIG Recommendations Tracker"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Claudia Giudi",
                 "hasEmail": "mailto:guidi.claudia.l@dol.gov"
             },
+            "description": "Available on website, has all the reports published since 2001",
+            "identifier": "ILAB-12-012:037-140",
             "keyword": [
                 "ILAB",
                 "child labor",
                 "forced labor"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-01-27T21:17:37.417Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of International Labor Affairs",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Department of Labor"
+                }
+            },
+            "rights": "true",
+            "title": "Findings on the Worst Forms of Child Labor"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Labor Exchange Agricultural Reporting System (LEARS) Data",
-            "description": "State Workforce Agencies (SWA) use the Labor Exchange Agricultural Reporting System (LEARS) to submit data quarterly to ETA on the services they provide to Migrant and Seasonal Farmworkers (MSFW). This data is reported as aggregate data  counts and as narrative data through ETA Form 5148 into LEARS. LEARS captures this data that is not reported in WIPS as participant level data.\n\nETA -5148 includes:\nPart 1: Services to Migrant and Seasonal Farmworkers\nPart 2: Narrative Response\nPart 3: Minimum Service Level Indicators\nPart 4: State Monitor Advocate Annual Summary",
-            "modified": "2024-12-26T19:21:36.902Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:006-461",
-            "describedBy": "https://www.dol.gov/agencies/eta/agriculture/monitor-advocate-system/performance",
-            "describedByType": "text/html",
-            "landingPage": "https://www.dol.gov/agencies/eta/agriculture/monitor-advocate-system/performance",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Employment and Training Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Steve Rietzke",
                 "hasEmail": "mailto:rietzke.steven@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/agriculture/monitor-advocate-system/performance",
+            "describedByType": "text/html",
+            "description": "State Workforce Agencies (SWA) use the Labor Exchange Agricultural Reporting System (LEARS) to submit data quarterly to ETA on the services they provide to Migrant and Seasonal Farmworkers (MSFW). This data is reported as aggregate data  counts and as narrative data through ETA Form 5148 into LEARS. LEARS captures this data that is not reported in WIPS as participant level data.\n\nETA -5148 includes:\nPart 1: Services to Migrant and Seasonal Farmworkers\nPart 2: Narrative Response\nPart 3: Minimum Service Level Indicators\nPart 4: State Monitor Advocate Annual Summary",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3331,6 +3324,7 @@
                     "title": "LEARS Data"
                 }
             ],
+            "identifier": "ETA-5-012:006-461",
             "keyword": [
                 "Agriculture",
                 "ETA",
@@ -3345,151 +3339,151 @@
                 "msfw",
                 "nfjp"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/eta/agriculture/monitor-advocate-system/performance",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-26T19:21:36.902Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Employment and Training Administration"
+            },
+            "rights": "true",
+            "title": "Labor Exchange Agricultural Reporting System (LEARS) Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electronic Labor Organization Reporting System eLORS",
-            "description": "e.LORS was created under the requirements of the Labor-Management Reporting and Disclosure Act to provide for electronic filing, storage, and disclosure of data filed with the Department by labor unions, employers, and others.  It also contains a module for investigative case management.",
-            "modified": "2024-03-22T21:17:04.973Z",
             "accessLevel": "restricted public",
-            "identifier": "OLMS-23-012:026-308",
-            "landingPage": "https://www.dol.gov/agencies/olms/public-disclosure-room",
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Labor-Management Standards",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of Labor-Management Standards"
-                }
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jolyn Underwood",
                 "hasEmail": "mailto:underwood.donna@dol.gov"
             },
+            "description": "e.LORS was created under the requirements of the Labor-Management Reporting and Disclosure Act to provide for electronic filing, storage, and disclosure of data filed with the Department by labor unions, employers, and others.  It also contains a module for investigative case management.",
+            "identifier": "OLMS-23-012:026-308",
             "keyword": [
                 "Labor-Management Reporting and Disclosure Act",
                 "OLMS",
                 "eLORS",
                 "unions"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/olms/public-disclosure-room",
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-03-22T21:17:04.973Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Labor-Management Standards",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of Labor-Management Standards"
+                }
+            },
+            "rights": "Internal dataset",
+            "title": "Electronic Labor Organization Reporting System eLORS"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Tax Performance System (TPS) Computed Measures",
-            "description": "The Tax Performance System's (TPS) Computed Measures are gathered from data that are electronically reported by each state to the US Department of Labor. They provide information on the timeliness and \"completeness\" of state activity. Up to four years of Computed Measures can be displayed, with contributory and reimbursing employer data provided separately. To provide context, national aggregates are also displayed for each year requested.",
-            "modified": "2023-01-03T00:00:00Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:013-497",
-            "describedBy": "https://wdr.doleta.gov/directives/corr_doc.cfm?DOCN=2929",
-            "landingPage": "https://oui.doleta.gov/unemploy/tps.asp",
-            "rights": "TRUE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Employment and Training Administration"
-            },
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://wdr.doleta.gov/directives/corr_doc.cfm?DOCN=2929",
+            "description": "The Tax Performance System's (TPS) Computed Measures are gathered from data that are electronically reported by each state to the US Department of Labor. They provide information on the timeliness and \"completeness\" of state activity. Up to four years of Computed Measures can be displayed, with contributory and reimbursing employer data provided separately. To provide context, national aggregates are also displayed for each year requested.",
+            "identifier": "ETA-5-012:013-497",
             "keyword": [
                 "ETA",
                 "computed measures",
                 "tax performance"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://oui.doleta.gov/unemploy/tps.asp",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-01-03T00:00:00Z",
             "programCode": [
                 "012:013"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Employment and Training Administration"
+            },
+            "rights": "TRUE",
+            "title": "Tax Performance System (TPS) Computed Measures"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual Financial Report",
-            "description": "DOL Annual Financial Report",
-            "modified": "2021-02-01T21:17:40.004Z",
             "accessLevel": "public",
-            "identifier": "OCFO-12-012:044-293",
-            "landingPage": "https://www.dol.gov/agencies/ocfo/resources",
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Chief Financial Officer",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Department of Energy"
-                }
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jennifer Maurer",
                 "hasEmail": "mailto:maurer.jennifer@dol.gov"
             },
+            "description": "DOL Annual Financial Report",
+            "identifier": "OCFO-12-012:044-293",
             "keyword": [
                 "AFR",
                 "Annual Financial Report",
                 "DOL",
                 "ocfo"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/ocfo/resources",
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-02-01T21:17:40.004Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Chief Financial Officer",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Department of Energy"
+                }
+            },
+            "rights": "true",
+            "title": "Annual Financial Report"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Unemployment Insurance Weekly Claims & Extended Benefits Trigger Data (ETA-539)",
-            "description": "Historical series of the State Unemployment Insurance (UI) Weekly Claims & Extended Benefits Trigger Data Reports (ETA-539) which contain data used in the production of the UI Weekly Claims news release. The data also includes information of the Extended Benefit program trigger status and includes the information provided by states to the US Department of Labor indicating the weekly extended benefits trigger status.",
-            "modified": "2024-03-29T15:33:56.608Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:013-464",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_539",
-            "rights": "TRUE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Employment and Training Administration"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
+            "description": "Historical series of the State Unemployment Insurance (UI) Weekly Claims & Extended Benefits Trigger Data Reports (ETA-539) which contain data used in the production of the UI Weekly Claims news release. The data also includes information of the Extended Benefit program trigger status and includes the information provided by states to the US Department of Labor indicating the weekly extended benefits trigger status.",
+            "identifier": "ETA-5-012:013-464",
             "keyword": [
                 "ETA",
                 "economic indicators",
@@ -3498,63 +3492,47 @@
                 "trigger notice",
                 "weeks claimed"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_539",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T15:33:56.608Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Employment and Training Administration"
+            },
+            "rights": "TRUE",
+            "title": "Unemployment Insurance Weekly Claims & Extended Benefits Trigger Data (ETA-539)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "FECA Quarterly Authoritative File",
-            "description": "Quarterly report detailing the FECA balance due from all Federal agencies",
-            "modified": "2021-02-02T21:38:26.682Z",
             "accessLevel": "public",
-            "identifier": "OCFO-12-012:044-294",
-            "landingPage": "https://www.dol.gov/agencies/ocfo/publications",
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Published",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Department of Energy"
-                }
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jennifer Maurer",
                 "hasEmail": "mailto:maurer.jennifer@dol.gov"
             },
+            "description": "Quarterly report detailing the FECA balance due from all Federal agencies",
+            "identifier": "OCFO-12-012:044-294",
             "keyword": [
                 "ocfo"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/ocfo/publications",
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-02-02T21:38:26.682Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "DCCA Audited Financial Statements",
-            "description": "Financial Statements and Independent Auditor's Report",
-            "modified": "2021-02-02T21:59:10.139Z",
-            "accessLevel": "public",
-            "identifier": "OCFO-12-012:044-297",
-            "landingPage": "https://www.oig.dol.gov/cgi-bin/oa_rpts-v4.cgi?s=&y=2017&a=all",
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Published",
@@ -3563,367 +3541,368 @@
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "title": "FECA Quarterly Authoritative File"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jennifer Maurer",
                 "hasEmail": "mailto:maurer.jennifer@dol.gov"
             },
+            "description": "Financial Statements and Independent Auditor's Report",
+            "identifier": "OCFO-12-012:044-297",
             "keyword": [
                 "ocfo"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.oig.dol.gov/cgi-bin/oa_rpts-v4.cgi?s=&y=2017&a=all",
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-02-02T21:59:10.139Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "OSHA Information System",
-            "description": "The OSHA Information System is the primary repository of OSHA\u2019s data.  Started in 2012, the application is divided into multiple modules. A database object in OIS may be used exclusively within a single module or shared across modules, which include program data on enforcement, consultation, and -- will soon include -- compliance-assistance data.",
-            "modified": "2024-12-16T17:52:09.413Z",
-            "accessLevel": "restricted public",
-            "identifier": "OSHA-18-012:029-396",
-            "landingPage": "https://www.osha.gov/pls/imis/establishment.search?",
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Occupational Safety and Health Administration",
+                "name": "Published",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Occupational Safety and Health Administration"
+                    "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "title": "DCCA Audited Financial Statements"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas 'Nate' Benz",
                 "hasEmail": "mailto:benz.thomas.n@dol.gov"
             },
+            "description": "The OSHA Information System is the primary repository of OSHA\u2019s data.  Started in 2012, the application is divided into multiple modules. A database object in OIS may be used exclusively within a single module or shared across modules, which include program data on enforcement, consultation, and -- will soon include -- compliance-assistance data.",
+            "identifier": "OSHA-18-012:029-396",
             "keyword": [
                 "OSHA"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.osha.gov/pls/imis/establishment.search?",
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-12-16T17:52:09.413Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Occupational Safety and Health Administration",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Occupational Safety and Health Administration"
+                }
+            },
+            "rights": "Internal dataset",
+            "title": "OSHA Information System"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Characteristics of the Insured Unemployed (ETA-203)",
-            "description": "Historical series of Characteristics of the Insured Unemployed Reports (ETA-203) including monthly data by state breaking out insured unemployment by claimant characteristics including age, gender, race, occupation and industry. The report collects characteric information on individuals filing a continued claim for Unemployment Insurance reflecting unemployment during the week which includes the 12th of the month. The data in this dataset is intended to align with the unemployment data collected through the monthly Consumer Population Survey.",
-            "modified": "2024-03-29T16:24:42.259Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:013-477",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_203",
-            "rights": "TRUE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Employment and Training Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
+            "description": "Historical series of Characteristics of the Insured Unemployed Reports (ETA-203) including monthly data by state breaking out insured unemployment by claimant characteristics including age, gender, race, occupation and industry. The report collects characteric information on individuals filing a continued claim for Unemployment Insurance reflecting unemployment during the week which includes the 12th of the month. The data in this dataset is intended to align with the unemployment data collected through the monthly Consumer Population Survey.",
+            "identifier": "ETA-5-012:013-477",
             "keyword": [
                 "ETA",
                 "characteristics",
                 "demographics",
                 "labor market information"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_203",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:24:42.259Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Employment and Training Administration"
+            },
+            "rights": "TRUE",
+            "title": "Characteristics of the Insured Unemployed (ETA-203)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "UTF Quarterly Authoritative File",
-            "description": "Quarterly report detailing the UTF balance due from all Federal agencies",
-            "modified": "2021-02-02T21:41:02.055Z",
             "accessLevel": "public",
-            "identifier": "OCFO-12-012:044-295",
-            "landingPage": "https://www.dol.gov/agencies/ocfo/publications",
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Chief Financial Officer",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Department of Energy"
-                }
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Diana Manzanarez",
                 "hasEmail": "mailto:manzanarez.diana.c@dol.gov"
             },
+            "description": "Quarterly report detailing the UTF balance due from all Federal agencies",
+            "identifier": "OCFO-12-012:044-295",
             "keyword": [
                 "ocfo"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/ocfo/publications",
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-02-02T21:41:02.055Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "New Core Financial Management System",
-            "description": "DOL Financial System, capturing all financial transactions for DOL",
-            "modified": "2023-03-16T19:16:24.310Z",
-            "accessLevel": "non-public",
-            "identifier": "OCFO-DOL wide -012:044-298",
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Chief Financial Officer",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Chief Financial Officer"
+                    "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "title": "UTF Quarterly Authoritative File"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sharnell Montgomery",
                 "hasEmail": "mailto:Montgomery.Sharnel@dol.gov"
             },
+            "description": "DOL Financial System, capturing all financial transactions for DOL",
+            "identifier": "OCFO-DOL wide -012:044-298",
             "keyword": [
                 "ocfo"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-03-16T19:16:24.310Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Chief Financial Officer",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of Chief Financial Officer"
+                }
+            },
+            "rights": "Internal dataset",
+            "title": "New Core Financial Management System"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Youth Opportunity Grant Initiative Evaluation (Public)",
-            "description": "These data files and documentation are derived from the evaluation of the Youth Opportunity Grant Initiative, which provided comprehensive services to at-risk youths in 36 urban, rural, and Native American reservation communities. The evaluation included an area survey of local youths to measure labor-market outcomes in YO grant sites and the use of American Community Survey (ACS) for comparison analysis to estimate the impact of YO programs.",
-            "modified": "2023-03-14T00:00:00Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:003-517",
-            "describedBy": "https://www.dol.gov/agencies/eta/policy/youth-opportunity-data-set",
-            "landingPage": "https://www.dol.gov/agencies/eta/policy/youth-opportunity-data-set",
-            "rights": "TRUE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Employment and Training Administration"
-            },
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Wayne Gordon",
                 "hasEmail": "mailto:gordon.wayne@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/policy/youth-opportunity-data-set",
+            "description": "These data files and documentation are derived from the evaluation of the Youth Opportunity Grant Initiative, which provided comprehensive services to at-risk youths in 36 urban, rural, and Native American reservation communities. The evaluation included an area survey of local youths to measure labor-market outcomes in YO grant sites and the use of American Community Survey (ACS) for comparison analysis to estimate the impact of YO programs.",
+            "identifier": "ETA-5-012:003-517",
             "keyword": [
                 "ETA",
                 "youth opportunity"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.dol.gov/agencies/eta/policy/youth-opportunity-data-set",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-03-14T00:00:00Z",
             "programCode": [
                 "012:003"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Employment and Training Administration"
+            },
+            "rights": "TRUE",
+            "title": "Youth Opportunity Grant Initiative Evaluation (Public)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Transit Grants",
-            "description": "Tracks the progress and completion of certifications under under the Transit Grant (DSP) program",
-            "modified": "2021-02-04T19:14:29.131Z",
             "accessLevel": "non-public",
-            "identifier": "OLMS-23-012:026-309",
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Labor-Management Standards",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Department of Labor"
-                }
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Karen Torre",
                 "hasEmail": "mailto:torre.karen@dol.gov"
             },
+            "description": "Tracks the progress and completion of certifications under under the Transit Grant (DSP) program",
+            "identifier": "OLMS-23-012:026-309",
             "keyword": [
                 "OLMS",
                 "Transit Grants"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-02-04T19:14:29.131Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "SailPoint IQ Provisioning/De-Provisioning and Active Directory (AD)",
-            "description": "Tracking to ensure Agencies send Network Account Deletion requests to OCIO within required timeframes.",
-            "modified": "2024-09-23T12:53:00.578Z",
-            "accessLevel": "public",
-            "identifier": "OASAM OCIO-25-012:044-247",
-            "license": "https://opendatacommons.org/licenses/by/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
+                "name": "Office of Labor-Management Standards",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Transit Grants"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ellie Behzad",
                 "hasEmail": "mailto:behzad.ellie@dol.gov"
             },
+            "description": "Tracking to ensure Agencies send Network Account Deletion requests to OCIO within required timeframes.",
+            "identifier": "OASAM OCIO-25-012:044-247",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2024-09-23T12:53:00.578Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Assistant Secretary for Administration and Management",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Assistant Secretary for Administration and Management"
+                }
+            },
+            "rights": "true",
+            "title": "SailPoint IQ Provisioning/De-Provisioning and Active Directory (AD)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Youth - Indian and Native American Program (INAP) data",
-            "description": "The Workforce Innovation Opportunity Act (WIOA) Section 166, Indian and Native American Youth Program collects aggregate summary level data from tribal grantees on a semi-annual and annual basis. This dataset includes information specific to the WIOA Section 166 Supplemental Youth Services Program (SYSP) for performance accountability purposes.  The aggregate program report (ETA 9085) includes data on summary level characteristics, types of services received, and performance outcomes attained as a result of participating in the program. Data is available in aggregate and modified public use files on ETA\u2019s website (doleta.gov/performance).",
-            "modified": "2024-12-26T19:11:02.794Z",
             "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:005-440",
-            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
-            "rights": "Not Available",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Employment and Training Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nathaniel Coley",
                 "hasEmail": "mailto:coley.nathaniel.d@dol.gov"
             },
+            "description": "The Workforce Innovation Opportunity Act (WIOA) Section 166, Indian and Native American Youth Program collects aggregate summary level data from tribal grantees on a semi-annual and annual basis. This dataset includes information specific to the WIOA Section 166 Supplemental Youth Services Program (SYSP) for performance accountability purposes.  The aggregate program report (ETA 9085) includes data on summary level characteristics, types of services received, and performance outcomes attained as a result of participating in the program. Data is available in aggregate and modified public use files on ETA\u2019s website (doleta.gov/performance).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/eta/dinap/performance",
-                    "title": "DINAP WIOA Performance Results",
-                    "description": "Access the dashboard for ETA-9173 national and grantee level data for the WIOA Section 166 INA\u2019s Comprehensive Services Program and Supplemental Youth Services Program. The Workforce Innovation and Opportunity Act (WIOA) requires Indian and Native American (INA) Programs to submit programmatic performance data to the Department of Labor on a quarterly basis through the ETA-9173 (OMB Control Number 1205-0521) reporting template."
+                    "description": "Access the dashboard for ETA-9173 national and grantee level data for the WIOA Section 166 INA\u2019s Comprehensive Services Program and Supplemental Youth Services Program. The Workforce Innovation and Opportunity Act (WIOA) requires Indian and Native American (INA) Programs to submit programmatic performance data to the Department of Labor on a quarterly basis through the ETA-9173 (OMB Control Number 1205-0521) reporting template.",
+                    "title": "DINAP WIOA Performance Results"
                 }
             ],
+            "identifier": "ETA-5-012:005-440",
             "keyword": [
                 "ETA",
                 "inap",
                 "indian native american program",
                 "native american"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-26T19:11:02.794Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Employment and Training Administration"
+            },
+            "rights": "Not Available",
+            "title": "Youth - Indian and Native American Program (INAP) data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "BigFix",
-            "description": "Endpoint management and security.",
-            "modified": "2024-09-23T12:59:10.873Z",
             "accessLevel": "non-public",
-            "identifier": "OASAM OCIO-25-012:044-249",
-            "landingPage": "https://usdol.sharepoint.com/:f:/s/OASAM-OCIO-Security/ESS/EgMGrFMP0X1OpHFFAvuklQQBSKGuiarduj4O2nDnfHxhHQ?e=EV1Yuh",
-            "rights": "private",
-            "spatial": "location characteristics",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
-                }
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vinh Nguyen",
                 "hasEmail": "mailto:nguyen.vinh@dol.gov"
             },
+            "description": "Endpoint management and security.",
+            "identifier": "OASAM OCIO-25-012:044-249",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://usdol.sharepoint.com/:f:/s/OASAM-OCIO-Security/ESS/EgMGrFMP0X1OpHFFAvuklQQBSKGuiarduj4O2nDnfHxhHQ?e=EV1Yuh",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T12:59:10.873Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Business Operations Support System (BOSS)",
-            "description": "OCIO\u2019s internal business operations tracking system",
-            "modified": "2024-12-06T16:25:07.723Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OCIO-25-012:044-274",
-            "rights": "private",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -3932,35 +3911,35 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "spatial": "location characteristics",
+            "title": "BigFix"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Leo Miller",
                 "hasEmail": "mailto:miller.leo@dol.gov"
             },
+            "description": "OCIO\u2019s internal business operations tracking system",
+            "identifier": "OASAM OCIO-25-012:044-274",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
-            ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Cybersecurity Assessment and Management (CSAM)",
-            "description": "A Plan of Action and Milestones (POA&M) is a DHS requirement, and is a corrective action plan for tracking and planning the resolution of information security weaknesses assigned to Agencies for remediation.",
-            "modified": "2024-09-23T13:01:10.255Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OCIO-25-012:044-250",
-            "license": "https://opendatacommons.org/licenses/pddl/1.0/",
-            "rights": "private",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-06T16:25:07.723Z",
+            "programCode": [
+                "015:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -3969,51 +3948,62 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "title": "Business Operations Support System (BOSS)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Muhammad Butt",
                 "hasEmail": "mailto:butt.muhammad@dol.gov"
             },
+            "description": "A Plan of Action and Milestones (POA&M) is a DHS requirement, and is a corrective action plan for tracking and planning the resolution of information security weaknesses assigned to Agencies for remediation.",
+            "identifier": "OASAM OCIO-25-012:044-250",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://opendatacommons.org/licenses/pddl/1.0/",
+            "modified": "2024-09-23T13:01:10.255Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "VETS-701 - Homeless Veteran Reintegration Program (HVRP) Technical Performance Report (TPR)",
-            "description": "\"Quarterly Technical Performance Report (TPR) from HVRP grantees. This includes demographic and employment characteristics of HVRP participants aggregated at the grantee-level.\nThe TPR is an Excel-based data collection and reporting tool for grant recipients to enter participant and project information. The workbook allows VETS\u2019 Grant Officer\u2019s Technical Representatives (GOTR) to monitor performance and enables the aggregation and analysis of \ngrant recipient data to assess the effectiveness of grant programs and submit reports to Congress. Grant recipients must submit the TPR and its accompanying TPN for a specific grant award for all twelve quarters in the grant Period of Performance (PoP).\nThe TPR Excel workbook is comprised of six worksheets:\n1. Planned Goals \u2013 Recipient input required\n2. Tech Perf Report \u2013 Report / minimal recipient input required\n3. New Enrollment Entry \u2013 Recipient input optional\n4. Participant Info \u2013 Recipient input required \n5. Demographics Summary \u2013 Report / no input required\n6. Goals v. Actual \u2013 Report / no input required\"",
-            "modified": "2024-12-17T12:55:57.574Z",
-            "accessLevel": "restricted public",
-            "identifier": "VETS-29-012:042-356",
-            "describedBy": "https://www.dol.gov/sites/dolgov/files/VETS/files/HVRP-Quarterly-Performance-Report-Desk-Guide-Revised-2024-with-Formulas.pdf",
-            "describedByType": "application/pdf",
-            "rights": "This data includes personally identifiable information and sensitive information (homeless status)",
-            "spatial": "Street Address",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Veterans\u2019 Employment and Training Service",
+                "name": "Office of the Assistant Secretary for Administration and Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Veterans\u2019 Employment and Training Service"
+                    "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "title": "Cybersecurity Assessment and Management (CSAM)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOL-VETS-HVRP",
                 "hasEmail": "mailto:HVRP@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/sites/dolgov/files/VETS/files/HVRP-Quarterly-Performance-Report-Desk-Guide-Revised-2024-with-Formulas.pdf",
+            "describedByType": "application/pdf",
+            "description": "\"Quarterly Technical Performance Report (TPR) from HVRP grantees. This includes demographic and employment characteristics of HVRP participants aggregated at the grantee-level.\nThe TPR is an Excel-based data collection and reporting tool for grant recipients to enter participant and project information. The workbook allows VETS\u2019 Grant Officer\u2019s Technical Representatives (GOTR) to monitor performance and enables the aggregation and analysis of \ngrant recipient data to assess the effectiveness of grant programs and submit reports to Congress. Grant recipients must submit the TPR and its accompanying TPN for a specific grant award for all twelve quarters in the grant Period of Performance (PoP).\nThe TPR Excel workbook is comprised of six worksheets:\n1. Planned Goals \u2013 Recipient input required\n2. Tech Perf Report \u2013 Report / minimal recipient input required\n3. New Enrollment Entry \u2013 Recipient input optional\n4. Participant Info \u2013 Recipient input required \n5. Demographics Summary \u2013 Report / no input required\n6. Goals v. Actual \u2013 Report / no input required\"",
+            "identifier": "VETS-29-012:042-356",
             "keyword": [
                 "701",
                 "HVRP",
@@ -4031,64 +4021,53 @@
                 "incarcerated veterans",
                 "veterans"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T12:55:57.574Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "DOL Applications Inventory and Cloud Application Inventory",
-            "description": "OCIO keeps a running list of applications that are and will be hosted to the cloud.",
-            "modified": "2024-09-23T13:05:05.981Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM OCIO-25-012:044-254",
-            "rights": "restricted",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
+                "name": "Veterans\u2019 Employment and Training Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
+                    "name": "Veterans\u2019 Employment and Training Service"
                 }
             },
+            "rights": "This data includes personally identifiable information and sensitive information (homeless status)",
+            "spatial": "Street Address",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "VETS-701 - Homeless Veteran Reintegration Program (HVRP) Technical Performance Report (TPR)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Edward Meyman",
                 "hasEmail": "mailto:meyman.edward@dol.gov"
             },
+            "description": "OCIO keeps a running list of applications that are and will be hosted to the cloud.",
+            "identifier": "OASAM OCIO-25-012:044-254",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:05:05.981Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Benefits.gov",
-            "description": "The official benefits website of the U.S. government.  Benefits.gov provides an innovative, technology-based solution to connect U.S. citizens to federal, and some state benefits.\n\nBenefits.gov is a cross-governmental collaboration between multiple Federal agencies. Our Partner agencies share in the governance and strategic guidance of the Program, approve the features and enhancements to the site, provide the benefit program content, and contribute funding. The U.S. Department of Labor serves as the Managing Partner for Benefits.gov.",
-            "modified": "2024-12-06T13:56:38.460Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM OCIO-25-012:044-273",
-            "landingPage": "http://www.benefits.gov",
-            "rights": "restricted",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -4097,56 +4076,65 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "restricted",
+            "title": "DOL Applications Inventory and Cloud Application Inventory"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1W",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Myung Moon",
                 "hasEmail": "mailto:moon.myung@dol.gov"
             },
+            "description": "The official benefits website of the U.S. government.  Benefits.gov provides an innovative, technology-based solution to connect U.S. citizens to federal, and some state benefits.\n\nBenefits.gov is a cross-governmental collaboration between multiple Federal agencies. Our Partner agencies share in the governance and strategic guidance of the Program, approve the features and enhancements to the site, provide the benefit program content, and contribute funding. The U.S. Department of Labor serves as the Managing Partner for Benefits.gov.",
+            "identifier": "OASAM OCIO-25-012:044-273",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://www.benefits.gov",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-06T13:56:38.460Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://jira.dol.gov/projects/OCIO_BGOV/summary"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Veteran Data Exchange Initiative (VDEI) 2.0",
-            "description": "The Veteran Data Exchange Initiative (VDEI) allows DOL/VETS to retrieve data extracted from the Department of Defense (DOD)/ DEFENSE MANPOWER DATA CENTER  per a MOU with DoD.  This dataset contains the following characteristics of all service members transitioning from Active duty to civilian life: responses to the DD Forms 2648, 2648-1, transition assistance program (TAP) courses taken, and eForm data sets.  This dataset also includes transitioning service members' personal data and course session data.",
-            "modified": "2024-12-17T14:02:30.934Z",
-            "accessLevel": "non-public",
-            "identifier": "VETS-29-012:041-358",
-            "describedBy": "https://www.federalregister.gov/documents/2015/07/06/2015-16460/privacy-act-of-1974-publication-of-an-individual-systems-of-records",
-            "describedByType": "text/html",
-            "landingPage": "https://vdei.dol.gov",
-            "rights": "This data includes personally identifiable information",
-            "systemOfRecords": "https://www.federalregister.gov/documents/2015/07/06/2015-16460/privacy-act-of-1974-publication-of-an-individual-systems-of-records",
-            "spatial": "mailing address",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Veterans\u2019 Employment and Training Service",
+                "name": "Office of the Assistant Secretary for Administration and Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Veterans\u2019 Employment and Training Service"
+                    "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "references": [
+                "https://jira.dol.gov/projects/OCIO_BGOV/summary"
+            ],
+            "rights": "restricted",
+            "title": "Benefits.gov"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Serge King",
                 "hasEmail": "mailto:king.serge.a@dol.gov"
             },
+            "describedBy": "https://www.federalregister.gov/documents/2015/07/06/2015-16460/privacy-act-of-1974-publication-of-an-individual-systems-of-records",
+            "describedByType": "text/html",
+            "description": "The Veteran Data Exchange Initiative (VDEI) allows DOL/VETS to retrieve data extracted from the Department of Defense (DOD)/ DEFENSE MANPOWER DATA CENTER  per a MOU with DoD.  This dataset contains the following characteristics of all service members transitioning from Active duty to civilian life: responses to the DD Forms 2648, 2648-1, transition assistance program (TAP) courses taken, and eForm data sets.  This dataset also includes transitioning service members' personal data and course session data.",
+            "identifier": "VETS-29-012:041-358",
             "keyword": [
                 "DD2648",
                 "Department of Defense",
@@ -4161,30 +4149,14 @@
                 "transition assistance program",
                 "transitioning service member"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://vdei.dol.gov",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:02:30.934Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://www.federalregister.gov/documents/2015/07/06/2015-16460/privacy-act-of-1974-publication-of-an-individual-systems-of-records"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "HIRE Veterans Medallion Award Applications",
-            "description": "\"The Honoring Investments in Recruiting and Employing American Military Veterans Act of 2017 (HIRE Vets Act or the Act), requires the Secretary of Labor to establish a program, by rule, that recognizes employer efforts to recruit, employ, and retain veterans. Employer-applicants meeting criteria established in the rule will receive a \u201cHIRE Vets Medallion Award.\u201d As described in the Act, there are different awards for large employers (500-plus employees), medium employers (51-499 employees), and small employers (50 or fewer employees). Additionally, there are two award tiers: platinum and gold. For each award, the employer must satisfy a set of criteria.\nThis dataset contains information from the application form completed by employers who applied to the HIRE Veterans Medallion Program.  Information collected includes: company identifier, personal identifier, hiring/retention statistics and program information in application process from businesses who wish to be recognized for outstanding veteran hiring/retention. Under the Act, VETS will:  1. Solicit applications no later than January 31;  and  2.  Stop accepting applications on April 30.\"",
-            "modified": "2024-12-17T12:58:23.884Z",
-            "accessLevel": "restricted public",
-            "identifier": "VETS-29-012:043-359",
-            "describedBy": "https://www.hirevets.gov/resources#program",
-            "describedByType": "text/html",
-            "rights": "These data include employer identification information",
-            "spatial": "Street Address of Applicant",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Veterans\u2019 Employment and Training Service",
@@ -4193,12 +4165,30 @@
                     "name": "Veterans\u2019 Employment and Training Service"
                 }
             },
+            "references": [
+                "https://www.federalregister.gov/documents/2015/07/06/2015-16460/privacy-act-of-1974-publication-of-an-individual-systems-of-records"
+            ],
+            "rights": "This data includes personally identifiable information",
+            "spatial": "mailing address",
+            "systemOfRecords": "https://www.federalregister.gov/documents/2015/07/06/2015-16460/privacy-act-of-1974-publication-of-an-individual-systems-of-records",
+            "title": "Veteran Data Exchange Initiative (VDEI) 2.0"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOL-VETS-HVMP",
                 "hasEmail": "mailto:HIREVets@dol.gov"
             },
+            "describedBy": "https://www.hirevets.gov/resources#program",
+            "describedByType": "text/html",
+            "description": "\"The Honoring Investments in Recruiting and Employing American Military Veterans Act of 2017 (HIRE Vets Act or the Act), requires the Secretary of Labor to establish a program, by rule, that recognizes employer efforts to recruit, employ, and retain veterans. Employer-applicants meeting criteria established in the rule will receive a \u201cHIRE Vets Medallion Award.\u201d As described in the Act, there are different awards for large employers (500-plus employees), medium employers (51-499 employees), and small employers (50 or fewer employees). Additionally, there are two award tiers: platinum and gold. For each award, the employer must satisfy a set of criteria.\nThis dataset contains information from the application form completed by employers who applied to the HIRE Veterans Medallion Program.  Information collected includes: company identifier, personal identifier, hiring/retention statistics and program information in application process from businesses who wish to be recognized for outstanding veteran hiring/retention. Under the Act, VETS will:  1. Solicit applications no later than January 31;  and  2.  Stop accepting applications on April 30.\"",
+            "identifier": "VETS-29-012:043-359",
             "keyword": [
                 "HIRE Vets",
                 "HVMP",
@@ -4206,29 +4196,13 @@
                 "VETS Office of Strategic Outreach",
                 "veterans"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T12:58:23.884Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://www.hirevets.gov/resources#program"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "VETS USERRA and Veterans Preference Investigations",
-            "description": "\"This dataset contains information on claims of potential violations of the Uniformed Services Employment Reemployment Rights Act (USERRA) and Veterans  Preference (VP). The VETS\u2019 Case Management System (VCMS) allows USERRA claimants to submit claims to VETS involving potential USERRA and Veterans Preference violations.  Claimants may also monitor the status of their claim, request withdrawal and referral actions, and upload evidence and other documents directly to their assigned investigator through the VCMS.  VETS\u2019 investigators use the VCMS as the case file of record to conduct investigations based on the claims submitted by claimants.  The VCMS maintains secure copies of all investigative files, and case elements, and produces data regarding investigations for formal reporting requirements. This system contains 100 relational tables.\n\nDOL-VETS produce annual and quarterly Reports to Congress on USERRA. The source data for those reports are run using SQL, and we keep the data pulls in a secure SharePoint site for audit purposes.  Those \"\"official\"\" data pulls are done quarterly on the 1st of the month after the end of the quarter.\"\n\nThe VCMS was put into production on April 1, 2020 and fully replaced all paper and other electronic USERRA case management systems and processes for newly filed claims. The VCMS is entirely electronic, and incorporates all aspects of the investigative and referral processes, making case investigations more efficient and fungible. The VCMS will continue to be updated and improved to create greater efficiency and effectiveness during the upcoming five years (starting in FY 2020).",
-            "modified": "2024-12-17T12:59:56.474Z",
-            "accessLevel": "non-public",
-            "identifier": "VETS-29-012:043-360",
-            "describedBy": "https://www.dol.gov/sites/dolgov/files/VETS/files/VETS-USERRA-VEOA-VP-Investigations-Manual-2022-01-Redacted-UPDATE.pdf",
-            "rights": "This data includes personally identifiable information",
-            "spatial": "Street Address",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Veterans\u2019 Employment and Training Service",
@@ -4237,12 +4211,28 @@
                     "name": "Veterans\u2019 Employment and Training Service"
                 }
             },
+            "references": [
+                "https://www.hirevets.gov/resources#program"
+            ],
+            "rights": "These data include employer identification information",
+            "spatial": "Street Address of Applicant",
+            "title": "HIRE Veterans Medallion Award Applications"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOL-VETS-Compliance",
                 "hasEmail": "mailto:vetscompliance@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/sites/dolgov/files/VETS/files/VETS-USERRA-VEOA-VP-Investigations-Manual-2022-01-Redacted-UPDATE.pdf",
+            "description": "\"This dataset contains information on claims of potential violations of the Uniformed Services Employment Reemployment Rights Act (USERRA) and Veterans  Preference (VP). The VETS\u2019 Case Management System (VCMS) allows USERRA claimants to submit claims to VETS involving potential USERRA and Veterans Preference violations.  Claimants may also monitor the status of their claim, request withdrawal and referral actions, and upload evidence and other documents directly to their assigned investigator through the VCMS.  VETS\u2019 investigators use the VCMS as the case file of record to conduct investigations based on the claims submitted by claimants.  The VCMS maintains secure copies of all investigative files, and case elements, and produces data regarding investigations for formal reporting requirements. This system contains 100 relational tables.\n\nDOL-VETS produce annual and quarterly Reports to Congress on USERRA. The source data for those reports are run using SQL, and we keep the data pulls in a secure SharePoint site for audit purposes.  Those \"\"official\"\" data pulls are done quarterly on the 1st of the month after the end of the quarter.\"\n\nThe VCMS was put into production on April 1, 2020 and fully replaced all paper and other electronic USERRA case management systems and processes for newly filed claims. The VCMS is entirely electronic, and incorporates all aspects of the investigative and referral processes, making case investigations more efficient and fungible. The VCMS will continue to be updated and improved to create greater efficiency and effectiveness during the upcoming five years (starting in FY 2020).",
+            "identifier": "VETS-29-012:043-360",
             "keyword": [
                 "Case File",
                 "USERRA",
@@ -4250,47 +4240,47 @@
                 "VCMS",
                 "Veterans Preference",
                 "compliance",
-                "investigation",
-                "vets"
-            ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
-            ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://www.ecfr.gov/current/title-20/chapter-IX/part-1002?toc=1"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "4212 \u2013 Federal Contractor Reporting of Veteran Employment",
-            "description": "This dataset contains required veteran employment data by federal contractors/subcontractors, who are required to report annually the number of employees in their workforces who are veterans covered under VEVRAA.\n\nThe U.S. Department of Labor's Veterans' Employment and Training Service (VETS) and Office of Federal Contractor Compliance Programs (OFCCP) have supported affirmative actions to employ and advance in employment of covered veterans since 2008. As legislatively mandated under 38 U.S. Code Section 4212, codified at 41 CFR 61-300, contractors and subcontractors who enter into, or modify a contract or subcontract with the federal government, and whose contract meets the criteria set forth in the above legislation / regulations, are required to report annually on their affirmative action efforts in employing veterans. Data reported through form VETS-4212 is used by OFCCP in compliance evaluations.",
-            "modified": "2024-12-17T13:02:33.595Z",
-            "accessLevel": "restricted public",
-            "identifier": "VETS-29-012:043-361",
-            "describedBy": "https://www.dol.gov/sites/dolgov/files/VETS/files/VETS-4212-rev-2023.pdf",
-            "describedByType": "application/pdf",
-            "rights": "This data includes personally identifiable information",
-            "spatial": "Street Address of Federal Contractor's Parent Company and Hiring Location",
+                "investigation",
+                "vets"
+            ],
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-17T12:59:56.474Z",
+            "programCode": [
+                "015:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the Chief Information Officer",
+                "name": "Veterans\u2019 Employment and Training Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Veterans\u2019 Employment and Training Service"
                 }
             },
+            "references": [
+                "https://www.ecfr.gov/current/title-20/chapter-IX/part-1002?toc=1"
+            ],
+            "rights": "This data includes personally identifiable information",
+            "spatial": "Street Address",
+            "title": "VETS USERRA and Veterans Preference Investigations"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1W",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOL-VETS-Compliance",
                 "hasEmail": "mailto:vetscompliance@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/sites/dolgov/files/VETS/files/VETS-4212-rev-2023.pdf",
+            "describedByType": "application/pdf",
+            "description": "This dataset contains required veteran employment data by federal contractors/subcontractors, who are required to report annually the number of employees in their workforces who are veterans covered under VEVRAA.\n\nThe U.S. Department of Labor's Veterans' Employment and Training Service (VETS) and Office of Federal Contractor Compliance Programs (OFCCP) have supported affirmative actions to employ and advance in employment of covered veterans since 2008. As legislatively mandated under 38 U.S. Code Section 4212, codified at 41 CFR 61-300, contractors and subcontractors who enter into, or modify a contract or subcontract with the federal government, and whose contract meets the criteria set forth in the above legislation / regulations, are required to report annually on their affirmative action efforts in employing veterans. Data reported through form VETS-4212 is used by OFCCP in compliance evaluations.",
+            "identifier": "VETS-29-012:043-361",
             "keyword": [
                 "4212",
                 "Compliance",
@@ -4304,39 +4294,43 @@
                 "subcontractors",
                 "veterans"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T13:02:33.595Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Chief Information Officer",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Department of Labor"
+                }
+            },
             "references": [
                 "https://www.dol.gov/sites/dolgov/files/VETS/files/VETS-4212-rev-2023.pdf"
-            ]
+            ],
+            "rights": "This data includes personally identifiable information",
+            "spatial": "Street Address of Federal Contractor's Parent Company and Hiring Location",
+            "title": "4212 \u2013 Federal Contractor Reporting of Veteran Employment"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "List of Comprehensive and Affiliate American Job Centers",
-            "description": "List of Comprehensive and Affilitate American Job Centers includes the name of center, program type (affiliate or comprehensive), address, and contact information for American Job Centers in the United States and territories. Also included are the names and contact information of Veterans Representatives, Business Service Representatives, and Youth Service Representatives if the data is available, and if the center has such representatives.\n\n\nDownloadable file; CareerOneStop web service available upon request.",
-            "modified": "2022-11-28T00:00:00Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:018-451",
-            "describedBy": "https://www.careeronestop.org/Developers/Data/comprehensive-and-affiliate-american-job-centers.aspx",
-            "landingPage": "https://www.careeronestop.org/Developers/Data/comprehensive-and-affiliate-american-job-centers.aspx",
-            "rights": "TRUE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Employment and Training Administration"
-            },
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Steve Rietzke",
                 "hasEmail": "mailto:rietzke.steven@dol.gov"
             },
+            "describedBy": "https://www.careeronestop.org/Developers/Data/comprehensive-and-affiliate-american-job-centers.aspx",
+            "description": "List of Comprehensive and Affilitate American Job Centers includes the name of center, program type (affiliate or comprehensive), address, and contact information for American Job Centers in the United States and territories. Also included are the names and contact information of Veterans Representatives, Business Service Representatives, and Youth Service Representatives if the data is available, and if the center has such representatives.\n\n\nDownloadable file; CareerOneStop web service available upon request.",
+            "identifier": "ETA-5-012:018-451",
             "keyword": [
                 "ETA",
                 "ajc",
@@ -4344,40 +4338,37 @@
                 "job search tips",
                 "one stop career centers"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.careeronestop.org/Developers/Data/comprehensive-and-affiliate-american-job-centers.aspx",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-11-28T00:00:00Z",
             "programCode": [
                 "012:018"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Employment and Training Administration"
+            },
+            "rights": "TRUE",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "List of Comprehensive and Affiliate American Job Centers"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Black lung Distribution of Part C Black Lung Claims and Disbursements by State by Fiscal Year",
-            "description": "This dataset represents the information collected during the claims management process. It contains information about the number of claims received, actions taken, decisions and compensation by state.",
-            "modified": "2024-12-17T14:52:03.095Z",
             "accessLevel": "public",
-            "identifier": "OWCP-15-012:025-310",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
-                }
-            },
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This dataset represents the information collected during the claims management process. It contains information about the number of claims received, actions taken, decisions and compensation by state.",
+            "identifier": "OWCP-15-012:025-310",
             "keyword": [
                 "Blacklung",
                 "Insurance",
@@ -4391,24 +4382,13 @@
                 "provider",
                 "survivor"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:52:03.095Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Claims with Attorney or Lay Representation at District Director Level For Claims with PDO",
-            "description": "This dataset represents the information collected during the claims management process. It contains information about the number of PDO claims at the District Director level by attorneys or lay representation.",
-            "modified": "2024-12-17T15:01:56.550Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:025-312",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -4417,11 +4397,22 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "title": "Black lung Distribution of Part C Black Lung Claims and Disbursements by State by Fiscal Year"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This dataset represents the information collected during the claims management process. It contains information about the number of PDO claims at the District Director level by attorneys or lay representation.",
+            "identifier": "OWCP-15-012:025-312",
             "keyword": [
                 "Blacklung",
                 "PDO",
@@ -4435,75 +4426,75 @@
                 "payee",
                 "provider"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:01:56.550Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Whistleblower",
-            "description": "OSHA administers 23 whistleblower statutes.  The agency has an online complaint that gathers information about adverse actions, potential reasons for adverse actions, dates of adverse actions, and establishment identifying information including location, and contact information.  All is included in a database and supplemented by complaint information that is collected by other means, and data that is collected during investigations.  The additional data gathered from the public includes greater depth on allegations, type of complaint, and in some cases -- appeals.  The Privacy Act controls much of what is released to the public, and the agency also follows a system of records notice, which leads to the aggregation of data on docketed cases and complaint determinations by statute, which are released to the public.",
-            "modified": "2024-12-16T18:13:18.685Z",
-            "accessLevel": "restricted public",
-            "identifier": "OSHA-18-012:029-397",
-            "landingPage": "https://www.whistleblowers.gov/factsheets_page/statistics/FY2023",
-            "rights": "Restricted public access",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Occupational Safety and Health Administration",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Occupational Safety and Health Administration"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "title": "Claims with Attorney or Lay Representation at District Director Level For Claims with PDO"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas 'Nate' Benz",
                 "hasEmail": "mailto:benz.thomas.n@dol.gov"
             },
+            "description": "OSHA administers 23 whistleblower statutes.  The agency has an online complaint that gathers information about adverse actions, potential reasons for adverse actions, dates of adverse actions, and establishment identifying information including location, and contact information.  All is included in a database and supplemented by complaint information that is collected by other means, and data that is collected during investigations.  The additional data gathered from the public includes greater depth on allegations, type of complaint, and in some cases -- appeals.  The Privacy Act controls much of what is released to the public, and the agency also follows a system of records notice, which leads to the aggregation of data on docketed cases and complaint determinations by statute, which are released to the public.",
+            "identifier": "OSHA-18-012:029-397",
             "keyword": [
                 "OSHA",
                 "Whistleblower",
                 "whistleblower protection"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.whistleblowers.gov/factsheets_page/statistics/FY2023",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T18:13:18.685Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Part C Black Lung Claim Adjudications at the District Director Level During Fiscal Year",
-            "description": "This dataset represents the information collected during the claims management process. It contains information about the number of claims decisions and approvals at the District Director level.",
-            "modified": "2024-12-17T14:59:41.994Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:025-311",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
+                "name": "Occupational Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
+                    "name": "Occupational Safety and Health Administration"
                 }
             },
+            "rights": "Restricted public access",
+            "title": "Whistleblower"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This dataset represents the information collected during the claims management process. It contains information about the number of claims decisions and approvals at the District Director level.",
+            "identifier": "OWCP-15-012:025-311",
             "keyword": [
                 "Blacklung",
                 "and survivor insurance",
@@ -4515,24 +4506,13 @@
                 "payee",
                 "provider"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:59:41.994Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Total Number Black Lung Beneficiaries FY 2004 to Present",
-            "description": "This dataset represents the information collected during the claims management process. It contains information about the number of Part B and C Beneficiaries by Fiscal Year 2004 - Present FY.",
-            "modified": "2024-12-17T14:58:39.255Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:025-314",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -4541,11 +4521,22 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "title": "Part C Black Lung Claim Adjudications at the District Director Level During Fiscal Year"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This dataset represents the information collected during the claims management process. It contains information about the number of Part B and C Beneficiaries by Fiscal Year 2004 - Present FY.",
+            "identifier": "OWCP-15-012:025-314",
             "keyword": [
                 "Blacklung",
                 "benefits",
@@ -4558,24 +4549,13 @@
                 "provider",
                 "survivor"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:58:39.255Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Black Lung Program Benefit Payment Totals by Year",
-            "description": "This dataset represents the information collected during the claims management process. It contains information about the number of Part B and C Benefit Compensation by Fiscal Year.",
-            "modified": "2024-12-17T14:58:59.063Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:025-313",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -4584,11 +4564,22 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "title": "Total Number Black Lung Beneficiaries FY 2004 to Present"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This dataset represents the information collected during the claims management process. It contains information about the number of Part B and C Benefit Compensation by Fiscal Year.",
+            "identifier": "OWCP-15-012:025-313",
             "keyword": [
                 "Blacklung",
                 "benefits",
@@ -4601,73 +4592,73 @@
                 "provider",
                 "survivor"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:58:59.063Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Voluntary Protection Programs",
-            "description": "OSHA\u2019s Voluntary Protection Programs (VPP) is a program that recognizes employers and workers in industry and federal agencies who have implemented effective safety and health management systems and who maintain injury and illness rates below the national average for their industries.  OSHA collects data on entities that apply to the program and those that are active in the program.  Most data is establishment-specific, but data is also collected on best practices, delayed applications, reasons for withdrawal and cancellation, and outcomes of evaluations.",
-            "modified": "2024-12-16T18:04:51.366Z",
-            "accessLevel": "non-public",
-            "identifier": "OSHA-18-012:029-398",
-            "rights": "Restricted",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Occupational Safety and Health Administration",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Occupational Safety and Health Administration"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "title": "Black Lung Program Benefit Payment Totals by Year"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas 'Nate' Benz",
                 "hasEmail": "mailto:benz.thomas.n@dol.gov"
             },
+            "description": "OSHA\u2019s Voluntary Protection Programs (VPP) is a program that recognizes employers and workers in industry and federal agencies who have implemented effective safety and health management systems and who maintain injury and illness rates below the national average for their industries.  OSHA collects data on entities that apply to the program and those that are active in the program.  Most data is establishment-specific, but data is also collected on best practices, delayed applications, reasons for withdrawal and cancellation, and outcomes of evaluations.",
+            "identifier": "OSHA-18-012:029-398",
             "keyword": [
                 "OSHA",
                 "Voluntary Protection Programs"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T18:04:51.366Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Claims filed under Part C of the Black Lung Benefits Act 2001 Present FY",
-            "description": "This dataset represents the information collected during the claims management process. It contains information about the number of Part C Claims filed under the Black Lung Benefits Act from FY 2001 - Present FY.",
-            "modified": "2024-12-17T15:02:21.315Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:025-315",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
+                "name": "Occupational Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
+                    "name": "Occupational Safety and Health Administration"
                 }
             },
+            "rights": "Restricted",
+            "title": "Voluntary Protection Programs"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This dataset represents the information collected during the claims management process. It contains information about the number of Part C Claims filed under the Black Lung Benefits Act from FY 2001 - Present FY.",
+            "identifier": "OWCP-15-012:025-315",
             "keyword": [
                 "Blacklung",
                 "benefits",
@@ -4679,24 +4670,13 @@
                 "payee",
                 "provider"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:02:21.315Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Longshore DBA Case Summary Report",
-            "description": "The OWCP Defense Base Act Case Summary Reports (DBA Case Summaries) are compiled from data maintained by the Department of Labor, Office of Workers' Compensation Programs (OWCP), Division of Longshore and Harbor Workers' Compensation (DLHWC) in the administration of the Longshore and Harbor Workers' Compensation Act and its extensions. These reports do not constitute the complete or official casualty statistics of civilian contractor injuries and deaths. They are offered as general information to the public who may be interested in the scope of civilian government contracting overseas.",
-            "modified": "2024-12-17T14:52:24.891Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:025-319",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -4705,37 +4685,34 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "title": "Claims filed under Part C of the Black Lung Benefits Act 2001 Present FY"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "The OWCP Defense Base Act Case Summary Reports (DBA Case Summaries) are compiled from data maintained by the Department of Labor, Office of Workers' Compensation Programs (OWCP), Division of Longshore and Harbor Workers' Compensation (DLHWC) in the administration of the Longshore and Harbor Workers' Compensation Act and its extensions. These reports do not constitute the complete or official casualty statistics of civilian contractor injuries and deaths. They are offered as general information to the public who may be interested in the scope of civilian government contracting overseas.",
+            "identifier": "OWCP-15-012:025-319",
             "keyword": [
                 "compensation",
                 "longshore"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:52:24.891Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Black Lung Benefit Rates Under Part B 1969-Present",
-            "description": "This dataset represents the information collected during the claims management process. It contains information about the  Part B Benefit rates by Calendar Year.",
-            "modified": "2024-12-18T21:02:17.165Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:025-541",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -4744,12 +4721,26 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Longshore DBA Case Summary Report"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This dataset represents the information collected during the claims management process. It contains information about the  Part B Benefit rates by Calendar Year.",
+            "identifier": "OWCP-15-012:025-541",
             "keyword": [
                 "Blacklung",
                 "claim",
@@ -4757,66 +4748,54 @@
                 "miner",
                 "rate"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-18T21:02:17.165Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State Plan Activity",
-            "description": "The State Plan Application (SPA) tracks State Plan responses to federal program changes, usually new standards and directives, which the State Plans are required to adopt to meet statutory requirements of the State Plan being at least as effective as the federal program to maintain its status.  In accordance with the Occupational Safety and Health Act of 1970, OSHA conducts an evaluation of the 28 State Plans each fiscal year.  Case file reviews from the on-site visits also produce collected data.",
-            "modified": "2024-12-16T18:10:03.728Z",
-            "accessLevel": "public",
-            "identifier": "OSHA-18-012:029-402",
-            "landingPage": "https://www.osha.gov/stateplans/famereport",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Occupational Safety and Health Administration",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Occupational Safety and Health Administration"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Black Lung Benefit Rates Under Part B 1969-Present"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas 'Nate' Benz",
                 "hasEmail": "mailto:benz.thomas.n@dol.gov"
             },
+            "description": "The State Plan Application (SPA) tracks State Plan responses to federal program changes, usually new standards and directives, which the State Plans are required to adopt to meet statutory requirements of the State Plan being at least as effective as the federal program to maintain its status.  In accordance with the Occupational Safety and Health Act of 1970, OSHA conducts an evaluation of the 28 State Plans each fiscal year.  Case file reviews from the on-site visits also produce collected data.",
+            "identifier": "OSHA-18-012:029-402",
             "keyword": [
                 "OSHA",
                 "State Plans",
                 "state plan activity"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.osha.gov/stateplans/famereport",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T18:10:03.728Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "OSHA Form 300A",
-            "description": "Through CFR 1904.41, OSHA has the primary responsibility for the collection, compilation, and distribution of establishment-specific OSHA Form 300A injury and illness data.\u00a0 These data are collected through an Injury Tracking Application (ITA).  The agency currently has CY 2016-2020 data.",
-            "modified": "2024-12-16T18:00:47.270Z",
-            "accessLevel": "public",
-            "identifier": "OSHA-18-012:029-399",
-            "landingPage": "https://www.osha.gov/Establishment-Specific-Injury-and-Illness-Data",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Occupational Safety and Health Administration",
@@ -4825,12 +4804,23 @@
                     "name": "Occupational Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "title": "State Plan Activity"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas 'Nate' Benz",
                 "hasEmail": "mailto:benz.thomas.n@dol.gov"
             },
+            "description": "Through CFR 1904.41, OSHA has the primary responsibility for the collection, compilation, and distribution of establishment-specific OSHA Form 300A injury and illness data.\u00a0 These data are collected through an Injury Tracking Application (ITA).  The agency currently has CY 2016-2020 data.",
+            "identifier": "OSHA-18-012:029-399",
             "keyword": [
                 "300A",
                 "Injury Tracking Applicaton",
@@ -4840,44 +4830,43 @@
                 "injuries",
                 "summary data"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.osha.gov/Establishment-Specific-Injury-and-Illness-Data",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T18:00:47.270Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Historical Mine Safety and Health At A Glance: Calendar Year",
-            "description": "MSHA's high level summary report pertaining to mining employment, safety and health, and enforcement - historical.",
-            "modified": "2024-12-11T21:24:59.585Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-145",
-            "dataQuality": true,
-            "describedBy": "https://www.msha.gov/msha-glance",
-            "describedByType": "text/html",
-            "issued": "2021-02-01",
-            "landingPage": "https://www.msha.gov/msha-glance",
-            "rights": "true",
-            "systemOfRecords": "https://www.msha.gov/mine-data-retrieval-system",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Mine Safety and Health Administration",
+                "name": "Occupational Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Mine Safety and Health Administration"
+                    "name": "Occupational Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "title": "OSHA Form 300A"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.msha.gov/msha-glance",
+            "describedByType": "text/html",
+            "description": "MSHA's high level summary report pertaining to mining employment, safety and health, and enforcement - historical.",
+            "identifier": "MSHA-19-012:030-145",
+            "issued": "2021-02-01",
             "keyword": [
                 "Coal Mine Safety and Health",
                 "MNM Safety and Health",
@@ -4892,75 +4881,59 @@
                 "mining injury rates",
                 "mining violations"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/msha-glance",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:24:59.585Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Contractor Complaint Investigations",
-            "description": "The dataset consists of closed complaint investigations, conducted by the OFCCP, for the last five fiscal years. This data provides information on the OFCCP's efforts to enforce the EEO-mandated laws and regulations within the Federal Contractor Community (those companies which have been provided government contracts).",
-            "modified": "2024-11-21T15:13:14.122Z",
-            "accessLevel": "public",
-            "identifier": "OFCCP-22-012:028-306",
-            "dataQuality": true,
-            "describedBy": "https://enforcedata.dol.gov/views/data_summary.php",
-            "describedByType": "text/csv",
-            "issued": "2024-11-19",
-            "landingPage": "https://enforcedata.dol.gov/views/data_summary.php",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Federal Contract Compliance Programs",
+                "name": "Mine Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Federal Contract Compliance Programs"
+                    "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "systemOfRecords": "https://www.msha.gov/mine-data-retrieval-system",
+            "title": "Historical Mine Safety and Health At A Glance: Calendar Year"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Webb",
                 "hasEmail": "mailto:webb.michael.l@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://enforcedata.dol.gov/views/data_summary.php",
+            "describedByType": "text/csv",
+            "description": "The dataset consists of closed complaint investigations, conducted by the OFCCP, for the last five fiscal years. This data provides information on the OFCCP's efforts to enforce the EEO-mandated laws and regulations within the Federal Contractor Community (those companies which have been provided government contracts).",
+            "identifier": "OFCCP-22-012:028-306",
+            "issued": "2024-11-19",
             "keyword": [
                 "Investigation",
                 "OFCCP",
                 "complaint",
                 "enforcement",
-                "evaluation"
-            ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
-            ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Contractor Compliance Evaluations",
-            "description": "The dataset consists of closed compliance evaluations, conducted by the OFCCP, for the last five fiscal years. This data provides information on the OFCCP's efforts to enforce the EEO-mandated laws and regulations within the Federal Contractor Community (those companies which have been provided government contracts).",
-            "modified": "2024-11-21T15:12:17.952Z",
-            "accessLevel": "public",
-            "identifier": "OFCCP-22-012:028-307",
-            "describedBy": "https://enforcedata.dol.gov/views/data_summary.php",
-            "describedByType": "text/csv",
-            "issued": "2024-11-19",
+                "evaluation"
+            ],
             "landingPage": "https://enforcedata.dol.gov/views/data_summary.php",
-            "rights": "true",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-21T15:13:14.122Z",
+            "programCode": [
+                "015:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Federal Contract Compliance Programs",
@@ -4969,12 +4942,29 @@
                     "name": "Office of Federal Contract Compliance Programs"
                 }
             },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Federal Contractor Complaint Investigations"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Webb",
                 "hasEmail": "mailto:webb.michael.l@dol.gov"
             },
+            "describedBy": "https://enforcedata.dol.gov/views/data_summary.php",
+            "describedByType": "text/csv",
+            "description": "The dataset consists of closed compliance evaluations, conducted by the OFCCP, for the last five fiscal years. This data provides information on the OFCCP's efforts to enforce the EEO-mandated laws and regulations within the Federal Contractor Community (those companies which have been provided government contracts).",
+            "identifier": "OFCCP-22-012:028-307",
+            "issued": "2024-11-19",
             "keyword": [
                 "Investigation",
                 "OFCCP",
@@ -4982,63 +4972,53 @@
                 "enforcement",
                 "evaluation"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://enforcedata.dol.gov/views/data_summary.php",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-11-21T15:12:17.952Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Published",
-            "description": "In FY 2010, the DLHWC adopted as its performance goal under the Government Performance Results Act (GPRA) improving program effectiveness by facilitating prompt delivery of benefits to injured workers and their families. See the Longshore Program Performance Page for more information about the program's GPRA goals and results. To further this goal, we are sharing data on the timeliness of First Reports of Injury filed under the Defense Base Act. The data, aggregated by insurance carrier, shows the percent of reports received in the DLHWC District Offices within 30, 60, and 90 days of the date of the injury or death, or the date of the employer's knowledge of the injury and the onset of disability, whichever is later.",
-            "modified": "2024-12-17T15:07:45.701Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:025-320",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
+                "name": "Office of Federal Contract Compliance Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
+                    "name": "Office of Federal Contract Compliance Programs"
                 }
             },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Federal Contractor Compliance Evaluations"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "In FY 2010, the DLHWC adopted as its performance goal under the Government Performance Results Act (GPRA) improving program effectiveness by facilitating prompt delivery of benefits to injured workers and their families. See the Longshore Program Performance Page for more information about the program's GPRA goals and results. To further this goal, we are sharing data on the timeliness of First Reports of Injury filed under the Defense Base Act. The data, aggregated by insurance carrier, shows the percent of reports received in the DLHWC District Offices within 30, 60, and 90 days of the date of the injury or death, or the date of the employer's knowledge of the injury and the onset of disability, whichever is later.",
+            "identifier": "OWCP-15-012:025-320",
             "keyword": [
                 "injury",
                 "longshore"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:07:45.701Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Longshore Program Performance",
-            "description": "In Fiscal Year 2010, the Longshore Division adopted a new set of performance measures aimed at improving program effectiveness by facilitating the prompt delivery of benefits to injured workers and their families. Two new performance measures target the timeliness of the Employer's First Report of Injury and the First Payment of Compensation, thereby improving initial claims processing and benefit delivery outcomes. The \"First Report of Injury\" measure tracks the time from the date of the injury or death, or the date of the employer's knowledge of the injury and the onset of disability, whichever is later, to the date the Longshore District Office receives the Employer's First Report of Injury (Form LS-202). The \"First Payment\" measure tracks the time it takes the employer or insurance carrier to issue the First Payment of Compensation after the worker becomes disabled for work or after the worker's death.  Performance targets aim to increase the percentage of cases in which employers submit their First Reports of Injury and employers and carriers issue the First Payments of Compensation within 30 days. Performance results are shown in the tables below. The DBA performance measures were introduced in 2010, and the non-DBA measures in 2011.",
-            "modified": "2024-12-17T15:08:41.847Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:025-321",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -5047,36 +5027,33 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "title": "Published"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "In Fiscal Year 2010, the Longshore Division adopted a new set of performance measures aimed at improving program effectiveness by facilitating the prompt delivery of benefits to injured workers and their families. Two new performance measures target the timeliness of the Employer's First Report of Injury and the First Payment of Compensation, thereby improving initial claims processing and benefit delivery outcomes. The \"First Report of Injury\" measure tracks the time from the date of the injury or death, or the date of the employer's knowledge of the injury and the onset of disability, whichever is later, to the date the Longshore District Office receives the Employer's First Report of Injury (Form LS-202). The \"First Payment\" measure tracks the time it takes the employer or insurance carrier to issue the First Payment of Compensation after the worker becomes disabled for work or after the worker's death.  Performance targets aim to increase the percentage of cases in which employers submit their First Reports of Injury and employers and carriers issue the First Payments of Compensation within 30 days. Performance results are shown in the tables below. The DBA performance measures were introduced in 2010, and the non-DBA measures in 2011.",
+            "identifier": "OWCP-15-012:025-321",
             "keyword": [
                 "longshore"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:08:41.847Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Black Lung Benefit Rates Under Part C 1973-Present",
-            "description": "This dataset represents the information collected during the claims management process. It contains information about the  Part C Benefit rates by CalendarYear.",
-            "modified": "2024-12-18T21:01:12.836Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:025-542",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -5085,12 +5062,26 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Longshore Program Performance"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This dataset represents the information collected during the claims management process. It contains information about the  Part C Benefit rates by CalendarYear.",
+            "identifier": "OWCP-15-012:025-542",
             "keyword": [
                 "Blacklung",
                 "claim",
@@ -5098,27 +5089,13 @@
                 "miner",
                 "rate"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-18T21:01:12.836Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Black Lung Part C Automatic Survivor Entitlements Approved By District Offices",
-            "description": "This dataset represents the information collected during the claims management process. It contains information about the number of Part C Automatic Survivor Entitlements approved by District Offices FY 2001 - Present FY.",
-            "modified": "2024-12-17T15:00:13.050Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:025-317",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -5127,11 +5104,25 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Black Lung Benefit Rates Under Part C 1973-Present"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This dataset represents the information collected during the claims management process. It contains information about the number of Part C Automatic Survivor Entitlements approved by District Offices FY 2001 - Present FY.",
+            "identifier": "OWCP-15-012:025-317",
             "keyword": [
                 "Blacklung",
                 "benefits",
@@ -5144,24 +5135,13 @@
                 "provider",
                 "survivor"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:00:13.050Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Black Lung Case Management Data",
-            "description": "This is the entire dataset collected during the claims process for Black Lung Claims and includes significant PII",
-            "modified": "2024-12-17T14:55:56.016Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-318",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -5170,120 +5150,117 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "title": "Black Lung Part C Automatic Survivor Entitlements Approved By District Offices"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This is the entire dataset collected during the claims process for Black Lung Claims and includes significant PII",
+            "identifier": "OWCP-15-012:025-318",
             "keyword": [
                 "Blacklung"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:55:56.016Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Mining Fatalities - by State",
-            "description": "1983 and forward:\nFatalities by State and Calendar Year - All\nFatalities by State and Calendar Year - Coal\nFatalities by State and Calendar Year - MNM",
-            "modified": "2024-12-11T21:21:48.632Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-150",
-            "dataQuality": true,
-            "describedBy": "https://www.msha.gov/mine-data-retrieval-system",
-            "describedByType": "text/html",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "1983-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Mine Safety and Health Administration",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Mine Safety and Health Administration"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "title": "Black Lung Case Management Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.msha.gov/mine-data-retrieval-system",
+            "describedByType": "text/html",
+            "description": "1983 and forward:\nFatalities by State and Calendar Year - All\nFatalities by State and Calendar Year - Coal\nFatalities by State and Calendar Year - MNM",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.msha.gov/mine-data-retrieval-system"
                 }
             ],
+            "identifier": "MSHA-19-012:030-150",
             "keyword": [
                 "MSHA",
                 "mining fatalities"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:21:48.632Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Longshore Case Management (LCMS) data",
-            "description": "This dataset represents the information collected during the claims management process.",
-            "modified": "2024-12-17T14:56:15.615Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-322",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
+                "name": "Mine Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
+                    "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "1983-01-01/2024-09-30",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Mining Fatalities - by State"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
-            "keyword": [
-                "longshore"
-            ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
+            "description": "This dataset represents the information collected during the claims management process.",
+            "identifier": "OWCP-15-012:025-322",
+            "keyword": [
+                "longshore"
             ],
             "language": [
                 "en-US"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Longshore Disbursement System (LDS) data",
-            "description": "This dataset represents the information collected during the Special Fund benefit payment process.",
-            "modified": "2024-12-17T14:56:34.838Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-323",
-            "rights": "The dataset contains PII",
+            "modified": "2024-12-17T14:56:15.615Z",
+            "programCode": [
+                "015:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -5292,36 +5269,36 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Longshore Case Management (LCMS) data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This dataset represents the information collected during the Special Fund benefit payment process.",
+            "identifier": "OWCP-15-012:025-323",
             "keyword": [
                 "longshore"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:56:34.838Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Lognshore Party Data",
-            "description": "This dataset consists of several tables that store all individuals and organizations information. The main subsets are Individual and Organization. The Organization subset stores all the attributes regarding an Organization, including Organization Type and nature of business. \nThe Person subset contains information regarding individual, including last, first, and middles names, DOB, marital information, gender, job title, nationality,  guardian, DOD, and social security. This entity will capture key attributes regarding claimants, dependents, and attorney.\nThe other subsets contain address, phone, alias information for all parties and the relationship between the organization and a person.",
-            "modified": "2024-12-17T15:06:42.464Z",
-            "accessLevel": "restricted public",
-            "identifier": "OWCP-15-012:025-324",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -5330,12 +5307,26 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Longshore Disbursement System (LDS) data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This dataset consists of several tables that store all individuals and organizations information. The main subsets are Individual and Organization. The Organization subset stores all the attributes regarding an Organization, including Organization Type and nature of business. \nThe Person subset contains information regarding individual, including last, first, and middles names, DOB, marital information, gender, job title, nationality,  guardian, DOD, and social security. This entity will capture key attributes regarding claimants, dependents, and attorney.\nThe other subsets contain address, phone, alias information for all parties and the relationship between the organization and a person.",
+            "identifier": "OWCP-15-012:025-324",
             "keyword": [
                 "attorney",
                 "claimant",
@@ -5344,27 +5335,13 @@
                 "longshore",
                 "organization"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:06:42.464Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Published",
-            "description": "The 'MY PAL\" stands for My Personal Action List. This dataset contains all tasks for the user for a case, including the case number for that specific task, the status of the case, the injured worker\u2019s name, the specific task that needs to be completed within the case, the due date of the task, he number of days until the task is due, the overdue information, the name of the user the task has been referred to, and reassigned to and from information when applicable.",
-            "modified": "2024-12-17T15:06:05.633Z",
-            "accessLevel": "restricted public",
-            "identifier": "OWCP-15-012:025-325",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -5373,12 +5350,26 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Lognshore Party Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "The 'MY PAL\" stands for My Personal Action List. This dataset contains all tasks for the user for a case, including the case number for that specific task, the status of the case, the injured worker\u2019s name, the specific task that needs to be completed within the case, the due date of the task, he number of days until the task is due, the overdue information, the name of the user the task has been referred to, and reassigned to and from information when applicable.",
+            "identifier": "OWCP-15-012:025-325",
             "keyword": [
                 "case",
                 "claim",
@@ -5386,115 +5377,115 @@
                 "longshore",
                 "status"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:06:05.633Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Rulemaking",
-            "description": "Directorate of Standards and Guidance (DSG) collects information directly from the public at stakeholder meetings, site visits, and informal hearings.  Occasionally, DSG may solicit individual experts or groups of experts for information that is difficult to derive from available data sources or academic studies. The Office of Regulatory Analysis within DSG has conducted surveys in the past.",
-            "modified": "2024-12-16T18:13:43.185Z",
-            "accessLevel": "public",
-            "identifier": "OSHA-18-012:029-401",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Occupational Safety and Health Administration",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Occupational Safety and Health Administration"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "title": "Published"
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
                 "fn": "Thomas 'Nate' Benz",
                 "hasEmail": "mailto:benz.thomas.n@dol.gov"
             },
+            "description": "Directorate of Standards and Guidance (DSG) collects information directly from the public at stakeholder meetings, site visits, and informal hearings.  Occasionally, DSG may solicit individual experts or groups of experts for information that is difficult to derive from available data sources or academic studies. The Office of Regulatory Analysis within DSG has conducted surveys in the past.",
+            "identifier": "OSHA-18-012:029-401",
             "keyword": [
                 "OSHA",
                 "regulations",
                 "rulemaking"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T18:13:43.185Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Longshore Correspondence Data",
-            "description": "This dataset contains Correspondence information for a case, which includes Correspondence Type (Congressional Inquiry, Income Verification), Correspondence options, status and dates.",
-            "modified": "2024-12-17T14:57:01.933Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-327",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
+                "name": "Occupational Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
+                    "name": "Occupational Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "title": "Rulemaking"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This dataset contains Correspondence information for a case, which includes Correspondence Type (Congressional Inquiry, Income Verification), Correspondence options, status and dates.",
+            "identifier": "OWCP-15-012:025-327",
             "keyword": [
                 "case",
                 "correspondence",
                 "longshore"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:57:01.933Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "OSHA Medical Evaluation Tracking Application",
-            "description": "The OSHA Medical Evaluation Tracking Application (OMETA) supports the DTSEM Office of Occupational Medicine and Nursing (OOMN) as a repository for OSHA Compliance Officer medical information used to determine fitness for duty and exposure tracking.\u00a0 This application supports annual medical evaluations of covered employees, assessments of medical histories, physical examinations, and pre-placement examinations.",
-            "modified": "2024-12-16T18:01:45.583Z",
-            "accessLevel": "non-public",
-            "identifier": "OSHA-18-012:029-403",
-            "rights": "Restricted, except for health sampling data",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Occupational Safety and Health Administration",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Occupational Safety and Health Administration"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Longshore Correspondence Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas 'Nate' Benz",
                 "hasEmail": "mailto:benz.thomas.n@dol.gov"
             },
+            "description": "The OSHA Medical Evaluation Tracking Application (OMETA) supports the DTSEM Office of Occupational Medicine and Nursing (OOMN) as a repository for OSHA Compliance Officer medical information used to determine fitness for duty and exposure tracking.\u00a0 This application supports annual medical evaluations of covered employees, assessments of medical histories, physical examinations, and pre-placement examinations.",
+            "identifier": "OSHA-18-012:029-403",
             "keyword": [
                 "OSHA",
                 "exposure",
@@ -5505,24 +5496,13 @@
                 "physical examination",
                 "pre-placement examination"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T18:01:45.583Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Technical Equipment Support Application",
-            "description": "Technical Equipment Support Application (TESA) supports the Cincinnati Technical Center (CTC). The TESA system is used to record, store, track and make available to OSHA personnel, technical information pertaining to OSHA\u2019s equipment servicing, which most often includes calibration measurements.",
-            "modified": "2024-12-16T18:04:21.399Z",
-            "accessLevel": "non-public",
-            "identifier": "OSHA-18-012:029-405",
-            "rights": "Restricted, except for health sampling data",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Occupational Safety and Health Administration",
@@ -5531,12 +5511,23 @@
                     "name": "Occupational Safety and Health Administration"
                 }
             },
+            "rights": "Restricted, except for health sampling data",
+            "title": "OSHA Medical Evaluation Tracking Application"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas 'Nate' Benz",
                 "hasEmail": "mailto:benz.thomas.n@dol.gov"
             },
+            "description": "Technical Equipment Support Application (TESA) supports the Cincinnati Technical Center (CTC). The TESA system is used to record, store, track and make available to OSHA personnel, technical information pertaining to OSHA\u2019s equipment servicing, which most often includes calibration measurements.",
+            "identifier": "OSHA-18-012:029-405",
             "keyword": [
                 "Calibration",
                 "OSHA",
@@ -5545,26 +5536,13 @@
                 "technical equipment support application",
                 "technical information"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T18:04:21.399Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Severe Injury Report (SIR) Data",
-            "description": "Through CFR 1904.39, OSHA also has the primary responsibility of cleaning, compiling and publishing Severe Injury Report (SIR) data.\u00a0 These data include employer reported incidents involving in-patient hospitalizations, amputations, and the loss of an eye.\u00a0 OSHA cleans the reports of PII, codes the reports using the Occupational Injury and Illness Classification System, and publishes the data.",
-            "modified": "2024-12-16T18:05:47.975Z",
-            "accessLevel": "public",
-            "identifier": "OSHA-18-012:029-400",
-            "landingPage": "https://www.osha.gov/severeinjury",
-            "rights": "true",
-            "spatial": "latitude/longitude",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Occupational Safety and Health Administration",
@@ -5573,12 +5551,23 @@
                     "name": "Occupational Safety and Health Administration"
                 }
             },
+            "rights": "Restricted, except for health sampling data",
+            "title": "Technical Equipment Support Application"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas 'Nate' Benz",
                 "hasEmail": "mailto:benz.thomas.n@dol.gov"
             },
+            "description": "Through CFR 1904.39, OSHA also has the primary responsibility of cleaning, compiling and publishing Severe Injury Report (SIR) data.\u00a0 These data include employer reported incidents involving in-patient hospitalizations, amputations, and the loss of an eye.\u00a0 OSHA cleans the reports of PII, codes the reports using the Occupational Injury and Illness Classification System, and publishes the data.",
+            "identifier": "OSHA-18-012:029-400",
             "keyword": [
                 "OSHA",
                 "SIR",
@@ -5590,82 +5579,83 @@
                 "severe injury report",
                 "source code"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.osha.gov/severeinjury",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T18:05:47.975Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Longshore Case Detail Data",
-            "description": "The information in this dataset includes: case ID, case type, case create date, Longshore Act related to the case, case status, criminal background of the claimant flag when applicable, disability flag, litigation flag, relations to other parties (dataset) related to the case, specific section of the Act that is applicable to the case, information about various documents that are bronzed to the case,  injury information for a case, the event information for the actions performed by the user, user role information.",
-            "modified": "2024-12-17T15:04:57.000Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-328",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
+                "name": "Occupational Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
+                    "name": "Occupational Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "spatial": "latitude/longitude",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Severe Injury Report (SIR) Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "The information in this dataset includes: case ID, case type, case create date, Longshore Act related to the case, case status, criminal background of the claimant flag when applicable, disability flag, litigation flag, relations to other parties (dataset) related to the case, specific section of the Act that is applicable to the case, information about various documents that are bronzed to the case,  injury information for a case, the event information for the actions performed by the user, user role information.",
+            "identifier": "OWCP-15-012:025-328",
             "keyword": [
                 "case",
                 "claim",
                 "longshore"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:04:57.000Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Laboratory Information System Application",
-            "description": "The Laboratory Information System Application (LISA) is the main database for the collection of sampling and analytical results produced during the laboratory analysis of chemical samples.\u00a0 This database directly supports laboratory processes in which sampling and analytical results are generated, processed, and distributed to OSHA field personnel.",
-            "modified": "2024-12-16T18:06:29.378Z",
-            "accessLevel": "non-public",
-            "identifier": "OSHA-18-012:029-404",
-            "landingPage": "https://www.osha.gov/opengov/healthsamples.html",
-            "rights": "Restricted, except for health sampling data",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Occupational Safety and Health Administration",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Occupational Safety and Health Administration"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Longshore Case Detail Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas 'Nate' Benz",
                 "hasEmail": "mailto:benz.thomas.n@dol.gov"
             },
+            "description": "The Laboratory Information System Application (LISA) is the main database for the collection of sampling and analytical results produced during the laboratory analysis of chemical samples.\u00a0 This database directly supports laboratory processes in which sampling and analytical results are generated, processed, and distributed to OSHA field personnel.",
+            "identifier": "OSHA-18-012:029-404",
             "keyword": [
                 "OSHA",
                 "analytical results",
@@ -5675,63 +5665,50 @@
                 "laboratory processes",
                 "sampling results"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.osha.gov/opengov/healthsamples.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T18:06:29.378Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Longshore Pre-Penalty Data",
-            "description": "This dataset contains pre penalty information for a the case such as, Penalty Amount assessed ( Approved), penalty type, penalty status, penalty amounts corresponding to the number of offences, and other penalty related information.",
-            "modified": "2024-12-17T14:58:20.692Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-326",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
+                "name": "Occupational Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
+                    "name": "Occupational Safety and Health Administration"
                 }
             },
+            "rights": "Restricted, except for health sampling data",
+            "title": "Laboratory Information System Application"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This dataset contains pre penalty information for a the case such as, Penalty Amount assessed ( Approved), penalty type, penalty status, penalty amounts corresponding to the number of offences, and other penalty related information.",
+            "identifier": "OWCP-15-012:025-326",
             "keyword": [
                 "longshore",
                 "penalty"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:58:20.692Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Longshore Adjudication Data",
-            "description": "This dataset contains records of any intervention requests or issues, which includes, Intervention Requests for a case (actions and dates), Intervention issues  for a case (actions and dates), information about commutation request for a case, additional cases CE took action on as part of Commutation request and settlement request for a case, settlement request tracking for a case, case order and attorney fees, case settlements details and amount, conference calls details.",
-            "modified": "2024-12-17T15:03:50.404Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-329",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -5740,64 +5717,76 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Longshore Pre-Penalty Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This dataset contains records of any intervention requests or issues, which includes, Intervention Requests for a case (actions and dates), Intervention issues  for a case (actions and dates), information about commutation request for a case, additional cases CE took action on as part of Commutation request and settlement request for a case, settlement request tracking for a case, case order and attorney fees, case settlements details and amount, conference calls details.",
+            "identifier": "OWCP-15-012:025-329",
             "keyword": [
                 "case",
                 "claim",
                 "intervention",
                 "longshore"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:03:50.404Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Fatality Reports",
-            "description": "Fatalities by Coal or Metal/Non-Metal\nFatalites by Calendar Year\nFatalites by Calendar State\nFatalities by Mine Location\nFatalities by Accident Type\nFatalities by Mined Material",
-            "modified": "2024-12-11T21:38:34.998Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-151",
-            "dataQuality": true,
-            "describedBy": "https://www.msha.gov/data-reports/fatality-reports/search",
-            "describedByType": "text/html",
-            "landingPage": "https://www.msha.gov/data-reports/fatality-reports/search",
-            "rights": "true",
-            "spatial": "U.S. States",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Mine Safety and Health Administration",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Mine Safety and Health Administration"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Longshore Adjudication Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.msha.gov/data-reports/fatality-reports/search",
+            "describedByType": "text/html",
+            "description": "Fatalities by Coal or Metal/Non-Metal\nFatalites by Calendar Year\nFatalites by Calendar State\nFatalities by Mine Location\nFatalities by Accident Type\nFatalities by Mined Material",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.msha.gov/data-reports/fatality-reports/search"
                 }
             ],
+            "identifier": "MSHA-19-012:030-151",
             "keyword": [
                 "MSHA",
                 "fatals",
@@ -5807,31 +5796,14 @@
                 "mining fatalities by state",
                 "mining fatals"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/data-reports/fatality-reports/search",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:38:34.998Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Daily Fatality Summary",
-            "description": "Fatalities charged to the Mining Industry - Daily Report\nData by Accident Classification and Surface/Underground",
-            "modified": "2024-12-11T21:37:39.738Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-152",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/stats/charts/combined.php",
-            "describedByType": "text/html",
-            "landingPage": "https://arlweb.msha.gov/stats/charts/combined.php",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -5840,56 +5812,75 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "spatial": "U.S. States",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "MSHA Fatality Reports"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/stats/charts/combined.php",
+            "describedByType": "text/html",
+            "description": "Fatalities charged to the Mining Industry - Daily Report\nData by Accident Classification and Surface/Underground",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://arlweb.msha.gov/stats/charts/combined.php"
                 }
             ],
+            "identifier": "MSHA-19-012:030-152",
             "keyword": [
                 "Daily Fatality Report",
                 "MSHA",
                 "mining fatalities",
                 "mining fatals"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://arlweb.msha.gov/stats/charts/combined.php",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:37:39.738Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Longshore Payments Data",
-            "description": "The Payments dataset consists of calculations and distribution information of the necessary financial amounts to associated parties. It also contains benefits information, such as benefits due date, payment types, wages of the claimant, compensation rate, total benefit amount, injured body parts, special funds payments if applicable.",
-            "modified": "2024-12-17T15:01:25.619Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-330",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
+                "name": "Mine Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
+                    "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "title": "MSHA Daily Fatality Summary"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "The Payments dataset consists of calculations and distribution information of the necessary financial amounts to associated parties. It also contains benefits information, such as benefits due date, payment types, wages of the claimant, compensation rate, total benefit amount, injured body parts, special funds payments if applicable.",
+            "identifier": "OWCP-15-012:025-330",
             "keyword": [
                 "body parts",
                 "case",
@@ -5898,27 +5889,13 @@
                 "longshore",
                 "wages"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:01:25.619Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Published",
-            "description": "The Fiscal dataset is a derivative of outcomes from the Payments actions. This dataset contains Disbursement (list of all payment files that have been both generated and certified) information, Accounts Receivable (list of all account receivables entered), Change Log (list of all adds, edits, and deletes of items from the \u2018Disbursement\u2019 and \u2018Accounts Receivable\u2019), payment files, Interest Rates and respective effective dates, the Min/Max/Cola values for each FY.",
-            "modified": "2024-12-17T15:04:36.461Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-331",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -5927,12 +5904,26 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Longshore Payments Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "The Fiscal dataset is a derivative of outcomes from the Payments actions. This dataset contains Disbursement (list of all payment files that have been both generated and certified) information, Accounts Receivable (list of all account receivables entered), Change Log (list of all adds, edits, and deletes of items from the \u2018Disbursement\u2019 and \u2018Accounts Receivable\u2019), payment files, Interest Rates and respective effective dates, the Min/Max/Cola values for each FY.",
+            "identifier": "OWCP-15-012:025-331",
             "keyword": [
                 "change log",
                 "disbursement",
@@ -5940,24 +5931,13 @@
                 "payment",
                 "rates"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:04:36.461Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Longshore 14(g) Penalty Resolution Data",
-            "description": "The 14(g) Penalty Resolution report contains data for penalty decisions resolved within number of days for Notices of Payment not filed timely.\n* Percentage of penalty decisions resolved within 90 days for Notices of Payment not filed timely; target: 85% (OPS Plan Goal)",
-            "modified": "2024-12-17T15:00:39.421Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-335",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -5966,12 +5946,23 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "title": "Published"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "The 14(g) Penalty Resolution report contains data for penalty decisions resolved within number of days for Notices of Payment not filed timely.\n* Percentage of penalty decisions resolved within 90 days for Notices of Payment not filed timely; target: 85% (OPS Plan Goal)",
+            "identifier": "OWCP-15-012:025-335",
             "keyword": [
                 "longshore",
                 "notice",
@@ -5979,46 +5970,45 @@
                 "penalty",
                 "resolution"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:00:39.421Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Non-Chargeable Mining Deaths",
-            "description": "Year by year breakdown (based on determination date), for all non-chargeable deaths, lists date of incident, mine name, operator, determination, with a link to accident report.",
-            "modified": "2024-12-11T21:12:40.101Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-160",
-            "dataQuality": true,
-            "landingPage": "https://www.msha.gov/coal-and-metalnonmetal-non-chargeable-mining-deaths",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Mine Safety and Health Administration",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Mine Safety and Health Administration"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "title": "Longshore 14(g) Penalty Resolution Data"
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
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "description": "Year by year breakdown (based on determination date), for all non-chargeable deaths, lists date of incident, mine name, operator, determination, with a link to accident report.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.msha.gov/coal-and-metalnonmetal-non-chargeable-mining-deaths"
                 }
             ],
+            "identifier": "MSHA-19-012:030-160",
             "keyword": [
                 "MNM mining",
                 "MSHA",
@@ -6027,29 +6017,14 @@
                 "mining",
                 "non-chargeable deaths"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/coal-and-metalnonmetal-non-chargeable-mining-deaths",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:12:40.101Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Mine Injury and Worktime Quarterly Reports",
-            "description": "Part 50 Report:\nNumber of Fatal Injuries\nOperator and contractor injury data by type of coal mined/mineral industry, work location, State (operator only), and accident classification\nOperator and contractor average number of employees and employees hours by work location, coal mined/mineral industry, work location, and State (operator only).",
-            "modified": "2024-12-11T21:11:55.715Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-162",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/ACCINJ/accinj.htm",
-            "describedByType": "application/pdf",
-            "landingPage": "https://arlweb.msha.gov/ACCINJ/accinj.htm",
-            "rights": "true",
-            "temporal": "1993-01-01/2024-06-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -6058,12 +6033,25 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "title": "Non-Chargeable Mining Deaths"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/ACCINJ/accinj.htm",
+            "describedByType": "application/pdf",
+            "description": "Part 50 Report:\nNumber of Fatal Injuries\nOperator and contractor injury data by type of coal mined/mineral industry, work location, State (operator only), and accident classification\nOperator and contractor average number of employees and employees hours by work location, coal mined/mineral industry, work location, and State (operator only).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6071,6 +6059,7 @@
                     "title": "MIWQ landing page"
                 }
             ],
+            "identifier": "MSHA-19-012:030-162",
             "keyword": [
                 "MIWQ",
                 "MSHA",
@@ -6084,41 +6073,43 @@
                 "mining injury rates",
                 "mining operators"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://arlweb.msha.gov/ACCINJ/accinj.htm",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:11:55.715Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://www.ecfr.gov/cgi-bin/text-idx?SID=95170f94d7c0fa8bcc1bdc4ad18eaed8&node=pt30.1.50&rgn=div5"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Medical Access Order (MAO) Application",
-            "description": "The Medical Access Order (MAO) Application supports OSHA field inspections during which employee medical records must be requested and reviewed.  This application facilitates field requests for medical records and tracks essential notifications and report generation needed to formally request medical records from employers.",
-            "modified": "2024-12-16T18:12:49.713Z",
-            "accessLevel": "non-public",
-            "identifier": "OSHA-18-012:029-406",
-            "rights": "Restricted, except for health sampling data",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Occupational Safety and Health Administration",
+                "name": "Mine Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Occupational Safety and Health Administration"
+                    "name": "Mine Safety and Health Administration"
                 }
             },
+            "references": [
+                "https://www.ecfr.gov/cgi-bin/text-idx?SID=95170f94d7c0fa8bcc1bdc4ad18eaed8&node=pt30.1.50&rgn=div5"
+            ],
+            "rights": "true",
+            "temporal": "1993-01-01/2024-06-30",
+            "title": "Mine Injury and Worktime Quarterly Reports"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas 'Nate' Benz",
                 "hasEmail": "mailto:benz.thomas.n@dol.gov"
             },
+            "description": "The Medical Access Order (MAO) Application supports OSHA field inspections during which employee medical records must be requested and reviewed.  This application facilitates field requests for medical records and tracks essential notifications and report generation needed to formally request medical records from employers.",
+            "identifier": "OSHA-18-012:029-406",
             "keyword": [
                 "OSHA",
                 "employee medical records",
@@ -6128,65 +6119,51 @@
                 "medical records",
                 "report generation"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T18:12:49.713Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Longshore Documents Data",
-            "description": "This dataset tracks the various incoming documents. All the incoming documents are landed in the document intake subset. As part of the workflow the documents are attached to various queues. These documents may or may not bronze to the case. This dataset also contains the link to the document.",
-            "modified": "2024-12-17T15:00:59.443Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-332",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
+                "name": "Occupational Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
+                    "name": "Occupational Safety and Health Administration"
                 }
             },
+            "rights": "Restricted, except for health sampling data",
+            "title": "Medical Access Order (MAO) Application"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This dataset tracks the various incoming documents. All the incoming documents are landed in the document intake subset. As part of the workflow the documents are attached to various queues. These documents may or may not bronze to the case. This dataset also contains the link to the document.",
+            "identifier": "OWCP-15-012:025-332",
             "keyword": [
                 "case",
                 "claim",
                 "document",
                 "longshore"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:00:59.443Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Published",
-            "description": "The \"First Report of Injury Filed\" contains data of Report of Injury filed within number days for Defense and Non-Defense Base Act cases as listed below (OPS Plan Goal Language):  Percentage of Employers\u2019 First Report of Injury filed within 20 days for Defense Base Act cases; target: 88%",
-            "modified": "2024-12-17T15:03:27.812Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-333",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -6195,83 +6172,81 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Longshore Documents Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "The \"First Report of Injury Filed\" contains data of Report of Injury filed within number days for Defense and Non-Defense Base Act cases as listed below (OPS Plan Goal Language):  Percentage of Employers\u2019 First Report of Injury filed within 20 days for Defense Base Act cases; target: 88%",
+            "identifier": "OWCP-15-012:025-333",
             "keyword": [
                 "Defense Base Act",
                 "Non-defense base act",
                 "injury",
                 "longshore"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:03:27.812Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Coal Production",
-            "description": "Coal Production - Closed Years Only\nData Starting: 2012\nBy Calendar Year, Mine Type",
-            "modified": "2024-12-11T21:22:54.393Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-158",
-            "dataQuality": true,
-            "describedBy": "https://www.msha.gov/mine-data-retrieval-system",
-            "describedByType": "text/html",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Mine Safety and Health Administration",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Mine Safety and Health Administration"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "title": "Published"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.msha.gov/mine-data-retrieval-system",
+            "describedByType": "text/html",
+            "description": "Coal Production - Closed Years Only\nData Starting: 2012\nBy Calendar Year, Mine Type",
+            "identifier": "MSHA-19-012:030-158",
             "keyword": [
                 "MSHA",
                 "coal",
                 "coal production",
                 "coal tonnage"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:22:54.393Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Coal Employment & Fatality Statistics",
-            "description": "Historical Data: 1900 - present.\nNumber of Miners & Mining Fatalities - Coal",
-            "modified": "2024-12-11T21:35:44.435Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-159",
-            "dataQuality": true,
-            "describedBy": "http://arlweb.msha.gov/stats/centurystats/coalstats.asp",
-            "describedByType": "text/html",
-            "landingPage": "http://arlweb.msha.gov/stats/centurystats/coalstats.asp",
-            "rights": "true",
-            "temporal": "1900-01-01/2023-12-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -6280,18 +6255,32 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "title": "Coal Production"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://arlweb.msha.gov/stats/centurystats/coalstats.asp",
+            "describedByType": "text/html",
+            "description": "Historical Data: 1900 - present.\nNumber of Miners & Mining Fatalities - Coal",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://arlweb.msha.gov/stats/centurystats/mnmstats.asp"
                 }
             ],
+            "identifier": "MSHA-19-012:030-159",
             "keyword": [
                 "MSHA",
                 "coal employment",
@@ -6300,78 +6289,80 @@
                 "mining fatalities",
                 "mining historical fatalities"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://arlweb.msha.gov/stats/centurystats/coalstats.asp",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:35:44.435Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "http://arlweb.msha.gov/stats/centurystats/mnmstats.asp"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State Plan Grant Tracking",
-            "description": "For State Plan grant applicants, a personnel funding breakout with a corresponding organizational chart and object class/supportive cost analysis with detailed financial information for all object class categories are required. For consultation program agreements, a complete and current equipment inventory, a staffing and organizational chart, budget information, with supporting details of anticipated costs are required.",
-            "modified": "2024-12-16T18:14:50.345Z",
-            "accessLevel": "non-public",
-            "identifier": "OSHA-18-012:029-408",
-            "rights": "Restricted",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Occupational Safety and Health Administration",
+                "name": "Mine Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Occupational Safety and Health Administration"
+                    "name": "Mine Safety and Health Administration"
                 }
             },
+            "references": [
+                "http://arlweb.msha.gov/stats/centurystats/mnmstats.asp"
+            ],
+            "rights": "true",
+            "temporal": "1900-01-01/2023-12-31",
+            "title": "MSHA Coal Employment & Fatality Statistics"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas 'Nate' Benz",
                 "hasEmail": "mailto:benz.thomas.n@dol.gov"
             },
+            "description": "For State Plan grant applicants, a personnel funding breakout with a corresponding organizational chart and object class/supportive cost analysis with detailed financial information for all object class categories are required. For consultation program agreements, a complete and current equipment inventory, a staffing and organizational chart, budget information, with supporting details of anticipated costs are required.",
+            "identifier": "OSHA-18-012:029-408",
             "keyword": [
                 "OSHA",
                 "State Plans",
                 "state plan grant tracking"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T18:14:50.345Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Published",
-            "description": "Conference Memo dataset is used to analyze Conference memorandum not issued timely. This dataset contains the following information: all Conference records that been held and those that require to Issue Conference Memo (i.e not all types of conferences, but only intervention request; Attorney fees and Special fund app conferences must not appear in this report as those do not require memo to be issued), Date conference was held, Case Type, Case Status, Payment Status, Extent of Injury, Injury Type, Office of the User who issued 1st conference memorandum (either Interim or Final), User who issued 1st conference memorandum (either Interim or Final), RCE of the Case when 1st conference memorandum was issued (either Interim or Final).\nConference memorandum issued within 10 days of conference held; target: 92% (OPS Goal Language)",
-            "modified": "2024-12-17T15:08:24.038Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-338",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
+                "name": "Occupational Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
+                    "name": "Occupational Safety and Health Administration"
                 }
             },
+            "rights": "Restricted",
+            "title": "State Plan Grant Tracking"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "Conference Memo dataset is used to analyze Conference memorandum not issued timely. This dataset contains the following information: all Conference records that been held and those that require to Issue Conference Memo (i.e not all types of conferences, but only intervention request; Attorney fees and Special fund app conferences must not appear in this report as those do not require memo to be issued), Date conference was held, Case Type, Case Status, Payment Status, Extent of Injury, Injury Type, Office of the User who issued 1st conference memorandum (either Interim or Final), User who issued 1st conference memorandum (either Interim or Final), RCE of the Case when 1st conference memorandum was issued (either Interim or Final).\nConference memorandum issued within 10 days of conference held; target: 92% (OPS Goal Language)",
+            "identifier": "OWCP-15-012:025-338",
             "keyword": [
                 "Memorandum",
                 "case",
@@ -6379,47 +6370,46 @@
                 "conference",
                 "longshore"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:08:24.038Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Hours Worked Report",
-            "description": "Hours Worked (Office Workers Excluded) - Closed Years Only\nData Starting: 2012\nBy Calendar Year, Coal or Metal/Non-Metal ; and Mine Type\nContractor Data is Included",
-            "modified": "2024-12-11T21:19:08.477Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-156",
-            "dataQuality": true,
-            "describedBy": "https://microstrategy.msha.gov/MicroStrategy/asp/mdrshelp/helpdocumentation.pdf",
-            "describedByType": "application/pdf",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Mine Safety and Health Administration",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Mine Safety and Health Administration"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "title": "Published"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://microstrategy.msha.gov/MicroStrategy/asp/mdrshelp/helpdocumentation.pdf",
+            "describedByType": "application/pdf",
+            "description": "Hours Worked (Office Workers Excluded) - Closed Years Only\nData Starting: 2012\nBy Calendar Year, Coal or Metal/Non-Metal ; and Mine Type\nContractor Data is Included",
             "distribution": [
                 {
                     "@type": "dcat:Distribution"
                 }
             ],
+            "identifier": "MSHA-19-012:030-156",
             "keyword": [
                 "MNM mining hours worked",
                 "MSHA",
@@ -6428,28 +6418,14 @@
                 "mining hours",
                 "operator hours"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:19:08.477Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Number of Employees",
-            "description": "Mining Employment (Office Workers Excluded) - Closed Years Only\nData Starting: 2012\nBy Calendar Year, Coal or Metal/Non-Metal ; and Mine Type\nContractor Data is included",
-            "modified": "2024-12-11T21:22:27.954Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-157",
-            "dataQuality": true,
-            "describedBy": "https://www.msha.gov/mine-data-retrieval-system",
-            "describedByType": "text/html",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -6458,41 +6434,40 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "title": "Hours Worked Report"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.msha.gov/mine-data-retrieval-system",
+            "describedByType": "text/html",
+            "description": "Mining Employment (Office Workers Excluded) - Closed Years Only\nData Starting: 2012\nBy Calendar Year, Coal or Metal/Non-Metal ; and Mine Type\nContractor Data is included",
+            "identifier": "MSHA-19-012:030-157",
             "keyword": [
                 "MNM employment",
                 "MSHA",
                 "coal employment",
                 "mining employment"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:22:27.954Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Metal NonMetal Employment & Fatality Statistics",
-            "description": "Historical Data: 1900 - present. \nNumber of Miners & Mining Fatalities - MNM",
-            "modified": "2024-12-11T21:27:10.249Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-580",
-            "dataQuality": true,
-            "describedBy": "http://arlweb.msha.gov/stats/centurystats/mnmstats.asp",
-            "describedByType": "text/html",
-            "landingPage": "http://arlweb.msha.gov/stats/centurystats/mnmstats.asp",
-            "rights": "true",
-            "temporal": "1900-01-01/2023-12-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -6501,18 +6476,32 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "title": "Number of Employees"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://arlweb.msha.gov/stats/centurystats/mnmstats.asp",
+            "describedByType": "text/html",
+            "description": "Historical Data: 1900 - present. \nNumber of Miners & Mining Fatalities - MNM",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://arlweb.msha.gov/stats/centurystats/mnmstats.asp"
                 }
             ],
+            "identifier": "MSHA-19-012:030-580",
             "keyword": [
                 "MNM employment",
                 "MNM fatalities",
@@ -6521,32 +6510,14 @@
                 "metal non-metal fatalities",
                 "mining historical data"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://arlweb.msha.gov/stats/centurystats/mnmstats.asp",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:27:10.249Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "http://arlweb.msha.gov/stats/centurystats/coalstats.asp"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Accident Injuries Data Set",
-            "description": "All accidents, injuries and illnesses reported by mine operators and contractors. Obtained from the Mine Accident, Injury and Illness Report form (MSHA Form 7000-1). Document number is the unique key for this data. It provides information about the accident/injury/illness such as type, mine location, lost days and the degree of injury.",
-            "modified": "2024-12-11T21:35:17.164Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-163",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Accidents_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "2000-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -6555,18 +6526,35 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "references": [
+                "http://arlweb.msha.gov/stats/centurystats/coalstats.asp"
+            ],
+            "rights": "true",
+            "temporal": "1900-01-01/2023-12-31",
+            "title": "MSHA Metal NonMetal Employment & Fatality Statistics"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Accidents_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "All accidents, injuries and illnesses reported by mine operators and contractors. Obtained from the Mine Accident, Injury and Illness Report form (MSHA Form 7000-1). Document number is the unique key for this data. It provides information about the accident/injury/illness such as type, mine location, lost days and the degree of injury.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.msha.gov/mine-data-retrieval-system",
-                    "title": "Mine Data Retrieval System - Explore MSHA Datasets",
-                    "description": "Flat files under Explore MSHA Datasets section."
+                    "description": "Flat files under Explore MSHA Datasets section.",
+                    "title": "Mine Data Retrieval System - Explore MSHA Datasets"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -6574,6 +6562,7 @@
                     "title": "Mine Data Retrieval System - Explore MSHA Datasets"
                 }
             ],
+            "identifier": "MSHA-19-012:030-163",
             "keyword": [
                 "MSHA",
                 "mining",
@@ -6582,32 +6571,14 @@
                 "mining fatals",
                 "mining injuries"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:35:17.164Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Conferences",
-            "description": "Information about completed conferences. Contains the conference number, the responsible party requesting the conference, the event number leading to the citation and the final status of the conference for all completed conferences.",
-            "modified": "2024-12-11T21:42:13.078Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-166",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Conferences_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "2000-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -6616,12 +6587,29 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "2000-01-01/2024-09-30",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "MSHA Accident Injuries Data Set"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Conferences_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "Information about completed conferences. Contains the conference number, the responsible party requesting the conference, the event number leading to the citation and the final status of the conference for all completed conferences.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6629,44 +6617,47 @@
                     "title": "Mine Data Retrieval System - Explore MSHA Datasets"
                 }
             ],
+            "identifier": "MSHA-19-012:030-166",
             "keyword": [
                 "CLR",
                 "MSHA",
                 "MSHA CLR",
                 "MSHA Conferences"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:42:13.078Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Published",
-            "description": "The \"First Payment of Compensation Issued\" report contains data that is ready to be analyzed for First Payment of Compensation issued within number of days for Defense and Non-Defense Base Act cases. Such as (Report OPS Goal Language):\n* Percentage of First Payment of Compensation issued within 28 days for Defense Base Act cases; target: 70%\n* Percentage of First Payment of Compensation issued within 28 days for non-Defense Base Act cases; target: 88%",
-            "modified": "2024-12-17T15:05:46.195Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-334",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
+                "name": "Mine Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
+                    "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "2000-01-01/2024-09-30",
+            "title": "MSHA Conferences"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "The \"First Payment of Compensation Issued\" report contains data that is ready to be analyzed for First Payment of Compensation issued within number of days for Defense and Non-Defense Base Act cases. Such as (Report OPS Goal Language):\n* Percentage of First Payment of Compensation issued within 28 days for Defense Base Act cases; target: 70%\n* Percentage of First Payment of Compensation issued within 28 days for non-Defense Base Act cases; target: 88%",
+            "identifier": "OWCP-15-012:025-334",
             "keyword": [
                 "Defense Base Act",
                 "Non-defense base act",
@@ -6675,24 +6666,13 @@
                 "longshore",
                 "payment"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:05:46.195Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Longshore 30(e) Penalty Resolution Data",
-            "description": "The \"30(e) Penalty Resolution\" report contains data that is ready to be analyzed for penalty decisions resolved within number of days for First Reports of Injury not filed timely. \n* Percentage of penalty decisions resolved within 90 days for First Reports of Injury not filed timely; target: 85% (OPS Plan Language)",
-            "modified": "2024-12-17T15:02:48.466Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-336",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -6701,86 +6681,97 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "title": "Published"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "The \"30(e) Penalty Resolution\" report contains data that is ready to be analyzed for penalty decisions resolved within number of days for First Reports of Injury not filed timely. \n* Percentage of penalty decisions resolved within 90 days for First Reports of Injury not filed timely; target: 85% (OPS Plan Language)",
+            "identifier": "OWCP-15-012:025-336",
             "keyword": [
                 "First report",
                 "Penalty Resolution",
                 "longshore"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:02:48.466Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Harwood Training Grant Tracking",
-            "description": "Budget information collected to describe activity under OSHA\u2019s Harwood training grants.",
-            "modified": "2024-12-16T18:03:33.544Z",
-            "accessLevel": "non-public",
-            "identifier": "OSHA-18-012:029-409",
-            "rights": "Restricted",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Occupational Safety and Health Administration",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Occupational Safety and Health Administration"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "title": "Longshore 30(e) Penalty Resolution Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas 'Nate' Benz",
                 "hasEmail": "mailto:benz.thomas.n@dol.gov"
             },
+            "description": "Budget information collected to describe activity under OSHA\u2019s Harwood training grants.",
+            "identifier": "OSHA-18-012:029-409",
             "keyword": [
                 "Harwood Grants",
                 "Harwood Training Grant Tracking",
                 "OSHA"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T18:03:33.544Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Published",
-            "description": "Intervention Initial Action Complete dataset is used to analyze records for action on request for Intervention not completed timely. This dataset contains the following information: all Intervention requests processed or not - either PAL tasks or manually added/edited intervention records (excluding records from deleted cases), Date Intervention record (LS-7) Received, Case Type, Payment Status, Case Status, Extent of Injury, Injury Type, User who took the response action, RCE of the Case when response action was taken. \nComplete action on request for Intervention within 15 days; target: 85% (OPS Plan Goal Language)",
-            "modified": "2024-12-17T15:07:10.504Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-337",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
+                "name": "Occupational Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
+                    "name": "Occupational Safety and Health Administration"
                 }
             },
+            "rights": "Restricted",
+            "title": "Harwood Training Grant Tracking"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "Intervention Initial Action Complete dataset is used to analyze records for action on request for Intervention not completed timely. This dataset contains the following information: all Intervention requests processed or not - either PAL tasks or manually added/edited intervention records (excluding records from deleted cases), Date Intervention record (LS-7) Received, Case Type, Payment Status, Case Status, Extent of Injury, Injury Type, User who took the response action, RCE of the Case when response action was taken. \nComplete action on request for Intervention within 15 days; target: 85% (OPS Plan Goal Language)",
+            "identifier": "OWCP-15-012:025-337",
             "keyword": [
                 "case",
                 "injury",
@@ -6788,51 +6779,49 @@
                 "longshore",
                 "payment"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:07:10.504Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Coal Dust Samples",
-            "description": "All operator and inspector dust samples taken for gravimetric samples. It includes information such as cassette numbers, date the sample was taken, initial and final weights, sample type, occupation codes related to the person taking the sample and mine information. Cassette number is the primary key for gravimetric samples. It also contains operator Continuous Personal Dust Monitor (CPDM) samples for operators as of 2/1/2016. The unique key is the CPDM file name. This dataset can be linked to the Mines dataset for further mine information.",
-            "modified": "2024-12-11T21:36:34.399Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-165",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Coal_Dust_Sample_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "2000-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Mine Safety and Health Administration",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Mine Safety and Health Administration"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "title": "Published"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Coal_Dust_Sample_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "All operator and inspector dust samples taken for gravimetric samples. It includes information such as cassette numbers, date the sample was taken, initial and final weights, sample type, occupation codes related to the person taking the sample and mine information. Cassette number is the primary key for gravimetric samples. It also contains operator Continuous Personal Dust Monitor (CPDM) samples for operators as of 2/1/2016. The unique key is the CPDM file name. This dataset can be linked to the Mines dataset for further mine information.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.msha.gov/mine-data-retrieval-system",
-                    "title": "Mine Data Retrieval System - Explore MSHA Datasets",
-                    "description": "Flat Files under Explore MSHA Datasets."
+                    "description": "Flat Files under Explore MSHA Datasets.",
+                    "title": "Mine Data Retrieval System - Explore MSHA Datasets"
                 }
             ],
+            "identifier": "MSHA-19-012:030-165",
             "keyword": [
                 "MSHA",
                 "air samples",
@@ -6843,29 +6832,14 @@
                 "mining health",
                 "mining samples"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:36:34.399Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Civil Penalty Dockets and Decisions",
-            "description": "Lists civil penalty dockets both in the litigation process and those that received an ALJ/Commission Settlement Approval or Decision. Includes the original proposed penalty amount as well as the decision amount, if the decision is recorded. Violations at a mine for a specific violator are bundled together into billing statements referred to as Assessment Cases (assess case no). Each Assessment Case may be associated to one or more docket numbers. Excluded from this dataset are discrimination dockets and agent/miner dockets.",
-            "modified": "2024-12-11T21:31:46.821Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-167",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Civil_Penalty_Dockets_And_Decisions_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "2000-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -6874,20 +6848,35 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "2000-01-01/2024-09-30",
+            "title": "MSHA Coal Dust Samples"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Civil_Penalty_Dockets_And_Decisions_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "Lists civil penalty dockets both in the litigation process and those that received an ALJ/Commission Settlement Approval or Decision. Includes the original proposed penalty amount as well as the decision amount, if the decision is recorded. Violations at a mine for a specific violator are bundled together into billing statements referred to as Assessment Cases (assess case no). Each Assessment Case may be associated to one or more docket numbers. Excluded from this dataset are discrimination dockets and agent/miner dockets.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.msha.gov/mine-data-retrieval-system",
-                    "title": "Mine Data Retrieval System - Explore MSHA Datasets",
-                    "description": "MSHA Flat Files"
+                    "description": "MSHA Flat Files",
+                    "title": "Mine Data Retrieval System - Explore MSHA Datasets"
                 }
             ],
+            "identifier": "MSHA-19-012:030-167",
             "keyword": [
                 "MSHA",
                 "MSHA assessments",
@@ -6897,29 +6886,14 @@
                 "mining dockets",
                 "mining violations"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:31:46.821Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Area Samples",
-            "description": "Samples taken at Metal/Non-Metal mines and the locations where the samples were taken. It includes such information as the sample date, contaminant code, location code, concentration and the action taken upon analysis of the sample. Sample No. is the unique key for this file.",
-            "modified": "2024-12-11T21:39:49.957Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-164",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Area_Samples_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "2000-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -6928,20 +6902,35 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "2000-01-01/2024-09-30",
+            "title": "MSHA Civil Penalty Dockets and Decisions"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Area_Samples_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "Samples taken at Metal/Non-Metal mines and the locations where the samples were taken. It includes such information as the sample date, contaminant code, location code, concentration and the action taken upon analysis of the sample. Sample No. is the unique key for this file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.msha.gov/mine-data-retrieval-system",
-                    "title": "Mine Data Retrieval System - Explore MSHA Datasets",
-                    "description": "Flat files under Explore MSHA Datasets section."
+                    "description": "Flat files under Explore MSHA Datasets section.",
+                    "title": "Mine Data Retrieval System - Explore MSHA Datasets"
                 }
             ],
+            "identifier": "MSHA-19-012:030-164",
             "keyword": [
                 "MNM samples",
                 "MSHA",
@@ -6951,29 +6940,14 @@
                 "mining",
                 "mining samples"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:39:49.957Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Contractor Employment and Production - Quarterly",
-            "description": "Contains employment and coal production reported by contractors for each quarter in a calendar year, by subunit and mine ID. The subunit code identifies the location or operation of the mine relating to the: (01) Underground; (02) Surface at underground; (03) Strip, quarry, open pit; (04) Auger; (05) Culm bank/refuse pile; (06) Dredge; (12) Other mining; (17) Independent shops or yards; (30) Mill operation/preparation plant; (99) Office workers at mine site.",
-            "modified": "2024-12-11T21:16:12.704Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-168",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/ContractorProdQuarterly_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "1983-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -6982,12 +6956,26 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "2000-01-01/2024-09-30",
+            "title": "MSHA Area Samples"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/ContractorProdQuarterly_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "Contains employment and coal production reported by contractors for each quarter in a calendar year, by subunit and mine ID. The subunit code identifies the location or operation of the mine relating to the: (01) Underground; (02) Surface at underground; (03) Strip, quarry, open pit; (04) Auger; (05) Culm bank/refuse pile; (06) Dredge; (12) Other mining; (17) Independent shops or yards; (30) Mill operation/preparation plant; (99) Office workers at mine site.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6995,6 +6983,7 @@
                     "title": "Mine Data Retrieval System - Explore MSHA Datasets"
                 }
             ],
+            "identifier": "MSHA-19-012:030-168",
             "keyword": [
                 "MSHA",
                 "Part 50",
@@ -7003,29 +6992,14 @@
                 "mining contractor employment",
                 "mining contractor production"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:16:12.704Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Controller and Operator History",
-            "description": "Shows the history of controllers at mining operations and the associations to the operators at those mines. Included are the starting and ending dates for a controller at each mine and the operator history at that mine.",
-            "modified": "2024-12-11T21:34:11.316Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-170",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Controller_Operator_History_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "1983-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -7034,12 +7008,26 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "1983-01-01/2024-09-30",
+            "title": "Contractor Employment and Production - Quarterly"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Controller_Operator_History_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "Shows the history of controllers at mining operations and the associations to the operators at those mines. Included are the starting and ending dates for a controller at each mine and the operator history at that mine.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7047,34 +7035,20 @@
                     "title": "Mine Data Retrieval System - Explore MSHA Datasets"
                 }
             ],
+            "identifier": "MSHA-19-012:030-170",
             "keyword": [
                 "MSHA",
                 "mine controller",
                 "mine operator"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:34:11.316Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Contractor Employment and Production - Yearly",
-            "description": "Contains the annual summation of employee hours and coal production reported by contractors where the average quarterly employment is greater than zero with grouping by calendar year, subunit code and mine ID . The subunit code identifies the location or operation of the mine relating to the: (01) Underground; (02) Surface at underground; (03) Strip, quarry, open pit; (04) Auger; (05) Culm bank/refuse pile; (06) Dredge; (12) Other mining; (17) Independent shops or yards; (30) Mill operation/preparation plant; (99) Office workers at mine site.",
-            "modified": "2024-12-11T21:15:37.898Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-169",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/ContractorProdAnnual_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "1983-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -7083,12 +7057,26 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "1983-01-01/2024-09-30",
+            "title": "MSHA Controller and Operator History"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/ContractorProdAnnual_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "Contains the annual summation of employee hours and coal production reported by contractors where the average quarterly employment is greater than zero with grouping by calendar year, subunit code and mine ID . The subunit code identifies the location or operation of the mine relating to the: (01) Underground; (02) Surface at underground; (03) Strip, quarry, open pit; (04) Auger; (05) Culm bank/refuse pile; (06) Dredge; (12) Other mining; (17) Independent shops or yards; (30) Mill operation/preparation plant; (99) Office workers at mine site.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7096,6 +7084,7 @@
                     "title": "Mine Data Retrieval System - Explore MSHA Datasets"
                 }
             ],
+            "identifier": "MSHA-19-012:030-169",
             "keyword": [
                 "MSHA",
                 "Part 50",
@@ -7104,58 +7093,49 @@
                 "mining contractor employment",
                 "mining contractor production"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:15:37.898Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Enforcement Management System (EMS) Database",
-            "description": "Database contains EBSA\u2019s civil cases, criminal cases, and Voluntary Fiduciary Correction (VFCP) data.",
-            "modified": "2021-04-01T16:40:56.633Z",
-            "accessLevel": "non-public",
-            "identifier": "EBSA-11-012:019-114",
-            "rights": "Restricted dataset",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Employee Benefits Security Administration",
+                "name": "Mine Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "1983-01-01/2024-09-30",
+            "title": "Contractor Employment and Production - Yearly"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "Database contains EBSA\u2019s civil cases, criminal cases, and Voluntary Fiduciary Correction (VFCP) data.",
+            "identifier": "EBSA-11-012:019-114",
             "keyword": [
                 "EBSA"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-04-01T16:40:56.633Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "DFVCS Database",
-            "description": "Database contains DVFC program participant data.",
-            "modified": "2021-04-01T15:56:25.411Z",
-            "accessLevel": "non-public",
-            "identifier": "EBSA-11-012:019-110",
-            "rights": "Restricted dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employee Benefits Security Administration",
@@ -7164,36 +7144,36 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "Restricted dataset",
+            "title": "Enforcement Management System (EMS) Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "Database contains DVFC program participant data.",
+            "identifier": "EBSA-11-012:019-110",
             "keyword": [
                 "Delinquent Filer",
                 "EBSA",
                 "pension",
                 "welfare"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-04-01T15:56:25.411Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EBSA Account Management Application (EAMA) Database",
-            "description": "Database contains EBSA personnel account management information i.e., account establishment, revocations, access modifications, etc.",
-            "modified": "2021-04-01T16:12:15.153Z",
-            "accessLevel": "non-public",
-            "identifier": "EBSA-11-012:019-112",
-            "rights": "Restricted dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employee Benefits Security Administration",
@@ -7202,32 +7182,32 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "Restricted dataset",
+            "title": "DFVCS Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "Database contains EBSA personnel account management information i.e., account establishment, revocations, access modifications, etc.",
+            "identifier": "EBSA-11-012:019-112",
             "keyword": [
                 "EBSA"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-04-01T16:12:15.153Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ERISA Data System (EDS) Database",
-            "description": "Database contains ERISA regulated entities, plan filing facsimiles, OE targeting and plan filing images.",
-            "modified": "2021-04-01T16:16:58.970Z",
-            "accessLevel": "non-public",
-            "identifier": "EBSA-11-012:019-113",
-            "rights": "Restricted dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employee Benefits Security Administration",
@@ -7236,35 +7216,35 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "Restricted dataset",
+            "title": "EBSA Account Management Application (EAMA) Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "Database contains ERISA regulated entities, plan filing facsimiles, OE targeting and plan filing images.",
+            "identifier": "EBSA-11-012:019-113",
             "keyword": [
                 "EBSA",
                 "Form 5500",
                 "Form M-1",
                 "Top Hat"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-04-01T16:16:58.970Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ERISA Public Data System (EPDS) Database",
-            "description": "Database contains publicly disclosable ERISA regulated entities, plan filing facsimiles, and plan filing images.",
-            "modified": "2021-04-01T16:33:55.343Z",
-            "accessLevel": "non-public",
-            "identifier": "EBSA-11-012:019-544",
-            "rights": "Restricted dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employee Benefits Security Administration",
@@ -7273,34 +7253,34 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "Restricted dataset",
+            "title": "ERISA Data System (EDS) Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "Database contains publicly disclosable ERISA regulated entities, plan filing facsimiles, and plan filing images.",
+            "identifier": "EBSA-11-012:019-544",
             "keyword": [
                 "EBSA",
                 "Form 5500",
                 "Form M-1"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-04-01T16:33:55.343Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Office of the Chief Accountant Case Tracking System (OCA CTS) Database",
-            "description": "This enforcement database contains cases of non-filers, stop-filers and deficient filers of Forms 5500.",
-            "modified": "2021-04-01T16:43:31.257Z",
-            "accessLevel": "non-public",
-            "identifier": "EBSA-11-012:019-117",
-            "rights": "Restricted dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employee Benefits Security Administration",
@@ -7309,11 +7289,22 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "Restricted dataset",
+            "title": "ERISA Public Data System (EPDS) Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "This enforcement database contains cases of non-filers, stop-filers and deficient filers of Forms 5500.",
+            "identifier": "EBSA-11-012:019-117",
             "keyword": [
                 "5500",
                 "EBSA",
@@ -7322,24 +7313,13 @@
                 "pension",
                 "welfare"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-04-01T16:43:31.257Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "OE Litigation Reference Library Database",
-            "description": "This database contains OE litigation documents.",
-            "modified": "2021-04-01T18:00:46.029Z",
-            "accessLevel": "non-public",
-            "identifier": "EBSA-11-012:019-119",
-            "rights": "Restricted dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employee Benefits Security Administration",
@@ -7348,54 +7328,62 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "Restricted dataset",
+            "title": "Office of the Chief Accountant Case Tracking System (OCA CTS) Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "This database contains OE litigation documents.",
+            "identifier": "EBSA-11-012:019-119",
             "keyword": [
                 "Benefit Plans",
                 "EBSA",
                 "enforcement",
                 "litigation"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-04-01T18:00:46.029Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Inspections Dataset",
-            "description": "Lists every mine inspection conducted by MSHA. Includes the name of the mine inspected, MSHA's internal inspection number (event number), the type of inspection and the start and end dates of the inspection. Event Number is the unique key for this dataset. It also includes the Mine ID associated with the inspections which can be used to relate it to the Mines Data Set.",
-            "modified": "2024-12-11T21:41:49.686Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-173",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Inspections_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "2000-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Mine Safety and Health Administration",
+                "name": "Employee Benefits Security Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Mine Safety and Health Administration"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "Restricted dataset",
+            "title": "OE Litigation Reference Library Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Inspections_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "Lists every mine inspection conducted by MSHA. Includes the name of the mine inspected, MSHA's internal inspection number (event number), the type of inspection and the start and end dates of the inspection. Event Number is the unique key for this dataset. It also includes the Mine ID associated with the inspections which can be used to relate it to the Mines Data Set.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7403,6 +7391,7 @@
                     "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-173",
             "keyword": [
                 "MSHA",
                 "MSHA enforcement",
@@ -7412,29 +7401,14 @@
                 "mining",
                 "mining inspections"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:41:49.686Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Operator Employment and Production Dataset - Yearly",
-            "description": "Contains the annual summation of employee hours and coal production reported by mine operators where the average quarterly employment is greater than zero with grouping by calendar year, subunit code and mine ID. The subunit code identifies the location or operation of the mine relating to the: (01) Underground; (02) Surface at underground; (03) Strip, quarry, open pit; (04) Auger; (05) Culm bank/refuse pile; (06) Dredge; (12) Other mining; (17) Independent shops or yards; (30) Mill operation/preparation plant; (99) Office workers at mine site.",
-            "modified": "2024-12-11T21:26:04.618Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-171",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/MineSProdYearly_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "1983-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -7443,12 +7417,26 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "2000-01-01/2024-09-30",
+            "title": "MSHA Inspections Dataset"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/MineSProdYearly_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "Contains the annual summation of employee hours and coal production reported by mine operators where the average quarterly employment is greater than zero with grouping by calendar year, subunit code and mine ID. The subunit code identifies the location or operation of the mine relating to the: (01) Underground; (02) Surface at underground; (03) Strip, quarry, open pit; (04) Auger; (05) Culm bank/refuse pile; (06) Dredge; (12) Other mining; (17) Independent shops or yards; (30) Mill operation/preparation plant; (99) Office workers at mine site.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7456,6 +7444,7 @@
                     "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-171",
             "keyword": [
                 "MSHA",
                 "Part 50",
@@ -7466,32 +7455,14 @@
                 "operator hours",
                 "operator production"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:26:04.618Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Operator Employment and Production Data Set - Quarterly",
-            "description": "Contains employment and coal production reported by mine operators for each quarter in a calendar year, by subunit and mine ID. The subunit code identifies the location or operation of the mine relating to the: (01) Underground; (02) Surface at underground; (03) Strip, quarry, open pit; (04) Auger; (05) Culm bank/refuse pile; (06) Dredge; (12) Other mining; (17) Independent shops or yards; (30) Mill operation/preparation plant; (99) Office workers at mine site.",
-            "modified": "2024-12-11T21:24:13.916Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-172",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/MineSProdQuarterly_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "2000-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -7500,12 +7471,29 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "1983-01-01/2024-09-30",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "MSHA Operator Employment and Production Dataset - Yearly"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/MineSProdQuarterly_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "Contains employment and coal production reported by mine operators for each quarter in a calendar year, by subunit and mine ID. The subunit code identifies the location or operation of the mine relating to the: (01) Underground; (02) Surface at underground; (03) Strip, quarry, open pit; (04) Auger; (05) Culm bank/refuse pile; (06) Dredge; (12) Other mining; (17) Independent shops or yards; (30) Mill operation/preparation plant; (99) Office workers at mine site.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7513,6 +7501,7 @@
                     "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-172",
             "keyword": [
                 "MSHA",
                 "Part 50",
@@ -7525,31 +7514,14 @@
                 "operator hours",
                 "operator production"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:24:13.916Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Mine Addresses of Record",
-            "description": "Contains mine addresses for all mines in the database except for Abandoned mines prior to 1998 from MSHA's legacy system. The address is the one entered by the mine operator at the time a Legal ID form is completed for a requested mine identification number. It is updated by MSHA district offices as required. The mine id is the unique key for this data.",
-            "modified": "2024-12-11T21:36:08.878Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-174",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/AddressofRecord_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -7558,12 +7530,29 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "2000-01-01/2024-09-30",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "MSHA Operator Employment and Production Data Set - Quarterly"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/AddressofRecord_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "Contains mine addresses for all mines in the database except for Abandoned mines prior to 1998 from MSHA's legacy system. The address is the one entered by the mine operator at the time a Legal ID form is completed for a requested mine identification number. It is updated by MSHA district offices as required. The mine id is the unique key for this data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7571,6 +7560,7 @@
                     "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-174",
             "keyword": [
                 "AOR",
                 "MSHA",
@@ -7578,32 +7568,14 @@
                 "mine addresses",
                 "mining"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:36:08.878Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Personal Health Samples",
-            "description": "Information about samples taken at Metal/Non-Metal mines as it relates to miners. Information included is the sample number and date, contaminant codes, concentration amounts and action taken upon analysis of the sample. Sample No. is the unique key for this file.",
-            "modified": "2024-12-11T21:37:22.013Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-177",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Personal_Health_Samples_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "2000-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -7612,12 +7584,28 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "MSHA Mine Addresses of Record"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Personal_Health_Samples_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "Information about samples taken at Metal/Non-Metal mines as it relates to miners. Information included is the sample number and date, contaminant codes, concentration amounts and action taken upon analysis of the sample. Sample No. is the unique key for this file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7625,6 +7613,7 @@
                     "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-177",
             "keyword": [
                 "MNM mining",
                 "MSHA",
@@ -7636,28 +7625,14 @@
                 "mining",
                 "mining health"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:37:22.013Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Quartz Samples",
-            "description": "Lists all operator and inspector dust samples taken. It includes information such as cassette numbers, date the sample was taken, quartz percentage, sample type, occupation codes related to the person or area sampled and mine information. Cassette number is the primary key for this dataset and it can be linked to the Mines dataset using Mine ID for further mine information.",
-            "modified": "2024-12-11T21:38:08.129Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-178",
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Quartz_Samples_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "2000-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -7666,12 +7641,25 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "2000-01-01/2024-09-30",
+            "title": "MSHA Personal Health Samples"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Quartz_Samples_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "Lists all operator and inspector dust samples taken. It includes information such as cassette numbers, date the sample was taken, quartz percentage, sample type, occupation codes related to the person or area sampled and mine information. Cassette number is the primary key for this dataset and it can be linked to the Mines dataset using Mine ID for further mine information.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7679,6 +7667,7 @@
                     "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-178",
             "keyword": [
                 "Cassette",
                 "MSHA",
@@ -7689,29 +7678,14 @@
                 "quartz",
                 "silica"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:38:08.129Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Violations Dataset",
-            "description": "Violations issued as a result of MSHA inspections conducted. Each inspection results in a unique Event Number that can be associated with many violations and is a direct link to the Inspections Data Set. The violator name at the time of the violation, the actual date the violation occurred and the date the violation was issued are in this file. Contains details about the specific citation/order/safeguard issued, such as Section of the Act, relevant dates and the conditions or practices which caused and constituted a violation or an imminent danger. The data is captured from (MSHA form 7000-3).",
-            "modified": "2024-12-11T21:40:45.022Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-179",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/violations_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "2000-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -7720,12 +7694,26 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "2000-01-01/2024-09-30",
+            "title": "MSHA Quartz Samples"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/violations_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "Violations issued as a result of MSHA inspections conducted. Each inspection results in a unique Event Number that can be associated with many violations and is a direct link to the Inspections Data Set. The violator name at the time of the violation, the actual date the violation occurred and the date the violation was issued are in this file. Contains details about the specific citation/order/safeguard issued, such as Section of the Act, relevant dates and the conditions or practices which caused and constituted a violation or an imminent danger. The data is captured from (MSHA form 7000-3).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7733,6 +7721,7 @@
                     "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-179",
             "keyword": [
                 "30 CFR",
                 "7000-3",
@@ -7753,29 +7742,14 @@
                 "violations",
                 "violator"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:40:45.022Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Mines Dataset",
-            "description": "Lists all Coal and Metal/Non-Metal mines under MSHA's jurisdiction. Including current status of each mine (Active, Abandoned, Nonproducing, etc.), the current owner and operating company, commodity codes and physical attributes of the mine. Mine ID is the unique key for this data.",
-            "modified": "2024-12-11T21:40:16.222Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-175",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Mines_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "1978-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -7784,12 +7758,26 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "2000-01-01/2024-09-30",
+            "title": "MSHA Violations Dataset"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Mines_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "Lists all Coal and Metal/Non-Metal mines under MSHA's jurisdiction. Including current status of each mine (Active, Abandoned, Nonproducing, etc.), the current owner and operating company, commodity codes and physical attributes of the mine. Mine ID is the unique key for this data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7802,6 +7790,7 @@
                     "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-175",
             "keyword": [
                 "103I Codes",
                 "Coordinates",
@@ -7825,32 +7814,14 @@
                 "mines",
                 "state"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:40:16.222Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Noise Samples",
-            "description": "Includes information about noise samples taken and the types of protection being used, the machines active and environment at the time. Form No. and Survey No. together create a unique key for the file.",
-            "modified": "2024-12-11T21:42:40.577Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-176",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Noise_Samples_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "2000-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -7859,12 +7830,29 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "1978-01-01/2024-09-30",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "MSHA Mines Dataset"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Noise_Samples_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "Includes information about noise samples taken and the types of protection being used, the machines active and environment at the time. Form No. and Survey No. together create a unique key for the file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7872,6 +7860,7 @@
                     "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-176",
             "keyword": [
                 "Calibration",
                 "MSHA",
@@ -7888,29 +7877,14 @@
                 "noise samples",
                 "php"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:42:40.577Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Contested Violations",
-            "description": "Assessed violations  contested by the violator and the contest request has been accepted by the Federal Mine Safety and Health Review Commission (FMSHRC). These dockets are tracked through the hearing process and ultimately receive a decision. Decisions can affect the penalty amount and/or citation attributes.",
-            "modified": "2024-12-11T21:38:58.919Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-180",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Contested_Violations_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "2000-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -7919,12 +7893,26 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "2000-01-01/2024-09-30",
+            "title": "MSHA Noise Samples"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Contested_Violations_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "Assessed violations  contested by the violator and the contest request has been accepted by the Federal Mine Safety and Health Review Commission (FMSHRC). These dockets are tracked through the hearing process and ultimately receive a decision. Decisions can affect the penalty amount and/or citation attributes.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7932,6 +7920,7 @@
                     "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-180",
             "keyword": [
                 "CMP",
                 "FMSHRC",
@@ -7941,72 +7930,74 @@
                 "federal review commission",
                 "mining"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:38:58.919Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Office Of Regulations And Interpretations Reference Library System (ORI RLS) Database",
-            "description": "This database contains advisory opinions, interpretive bulletins, Congressional inquiries and correspondence.",
-            "modified": "2021-04-02T15:45:59.603Z",
-            "accessLevel": "non-public",
-            "identifier": "EBSA-11-012:019-126",
-            "rights": "Restricted dataset",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Employee Benefits Security Administration",
+                "name": "Mine Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "2000-01-01/2024-09-30",
+            "title": "MSHA Contested Violations"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "This database contains advisory opinions, interpretive bulletins, Congressional inquiries and correspondence.",
+            "identifier": "EBSA-11-012:019-126",
             "keyword": [
                 "EBSA"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-04-02T15:45:59.603Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Published",
-            "description": "8( i) Settlements Processed dataset records to help with analysis of Settlement Application under Section 8( i) processed within number of days of receipt. This dataset contains the following data: all 8( i) Settlement Records (either processed or not processed LS-8 OR manually added Settlement record, excluded those records from deleted cases), Settlement received date, Case Type, Case Status, Payment Status, Extent of Injury, Injury Type, Office to which User who processed LS-8 (manually or via PAL task), User who processed LS-8 (manually or via PAL task), RCE of the Case at the time when LS-8 was processed (manually or via PAL task).",
-            "modified": "2024-12-17T15:07:27.960Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-343",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
+                "name": "Employee Benefits Security Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "Restricted dataset",
+            "title": "Office Of Regulations And Interpretations Reference Library System (ORI RLS) Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "8( i) Settlements Processed dataset records to help with analysis of Settlement Application under Section 8( i) processed within number of days of receipt. This dataset contains the following data: all 8( i) Settlement Records (either processed or not processed LS-8 OR manually added Settlement record, excluded those records from deleted cases), Settlement received date, Case Type, Case Status, Payment Status, Extent of Injury, Injury Type, Office to which User who processed LS-8 (manually or via PAL task), User who processed LS-8 (manually or via PAL task), RCE of the Case at the time when LS-8 was processed (manually or via PAL task).",
+            "identifier": "OWCP-15-012:025-343",
             "keyword": [
                 "case",
                 "injury",
@@ -8015,24 +8006,13 @@
                 "section",
                 "settlement"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:07:27.960Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "DFEC iFECS Case Management Data",
-            "description": "This dataset represents the information collected during the integrated Federal Employees Compensation (iFECS) case management process. It contains information about the number of claims received, actions taken, decisions and compensation.",
-            "modified": "2024-12-17T14:59:18.192Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-345",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -8041,12 +8021,23 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "title": "Published"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This dataset represents the information collected during the integrated Federal Employees Compensation (iFECS) case management process. It contains information about the number of claims received, actions taken, decisions and compensation.",
+            "identifier": "OWCP-15-012:025-345",
             "keyword": [
                 "DFEC",
                 "case",
@@ -8054,45 +8045,42 @@
                 "compansation",
                 "federal"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:59:18.192Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA - Assessed Violations",
-            "description": "Violations that have been assessed penalties as a result of MSHA inspections. Some of the values available are assessment case number, Mine Act Section Code, proposed penalty amounts, assessment and interest amounts, various penalty points and assessed case status information.",
-            "modified": "2024-12-11T21:41:22.834Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-181",
-            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Assessed_Violations_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "2000-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Mine Safety and Health Administration",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Mine Safety and Health Administration"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "DFEC iFECS Case Management Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "describedBy": "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Assessed_Violations_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "Violations that have been assessed penalties as a result of MSHA inspections. Some of the values available are assessment case number, Mine Act Section Code, proposed penalty amounts, assessment and interest amounts, various penalty points and assessed case status information.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8100,6 +8088,7 @@
                     "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-181",
             "keyword": [
                 "MSHA",
                 "MSHA violations",
@@ -8108,74 +8097,76 @@
                 "mining",
                 "penalties"
             ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
-            ],
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
             "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Office Of Regulations And Interpretations Case Tracking System (ORI CTS) Database",
-            "description": "This database contains case tracking records for production of advisory opinions, interpretive bulletins and responses to Congressional inquiries",
-            "modified": "2021-04-02T15:47:50.418Z",
-            "accessLevel": "non-public",
-            "identifier": "EBSA-11-012:019-125",
-            "rights": "Restricted dataset",
+                "en-US"
+            ],
+            "modified": "2024-12-11T21:41:22.834Z",
+            "programCode": [
+                "015:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Employee Benefits Security Administration",
+                "name": "Mine Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Employee Benefits Security Administration"
+                    "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "2000-01-01/2024-09-30",
+            "title": "MSHA - Assessed Violations"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "This database contains case tracking records for production of advisory opinions, interpretive bulletins and responses to Congressional inquiries",
+            "identifier": "EBSA-11-012:019-125",
             "keyword": [
                 "Advisory Opinions",
                 "EBSA",
                 "Employee benefits",
                 "Tracking"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-04-02T15:47:50.418Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "OPPEM Debt Management System (DMS) Database",
-            "description": "This database contains data related to agency procurement, spending and debt management (monies owed).",
-            "modified": "2021-04-02T16:28:15.862Z",
-            "accessLevel": "non-public",
-            "identifier": "EBSA-11-012:019-129",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employee Benefits Security Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Employee Benefits Security Administration"
                 }
             },
+            "rights": "Restricted dataset",
+            "title": "Office Of Regulations And Interpretations Case Tracking System (ORI CTS) Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "This database contains data related to agency procurement, spending and debt management (monies owed).",
+            "identifier": "EBSA-11-012:019-129",
             "keyword": [
                 "Debt Status",
                 "Demand Letter",
@@ -8186,80 +8177,77 @@
                 "collections",
                 "debt management"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-04-02T16:28:15.862Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EEOICP Program Statistics",
-            "description": "This dataset represents weekly statistics of applications submitted, compensations paid and medical bills paid.",
-            "modified": "2024-12-17T14:53:59.430Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:025-351",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
+                "name": "Employee Benefits Security Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "OPPEM Debt Management System (DMS) Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This dataset represents weekly statistics of applications submitted, compensations paid and medical bills paid.",
+            "identifier": "OWCP-15-012:025-351",
             "keyword": [
                 "compensation",
                 "energy",
                 "medical",
                 "statistics"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:53:59.430Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA Part 50 Self-Extracting Files",
-            "description": "Actual information (raw data) from the accident and injury MSHA Form 7000-2 filed with MSHA by mining operators and contractors as required under 30 CFR Part 50.",
-            "modified": "2024-12-11T21:30:56.367Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-183",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/STATS/PART50/p50y2k/p50y2k.HTM",
-            "describedByType": "application/pdf",
-            "landingPage": "https://arlweb.msha.gov/STATS/PART50/p50y2k/p50y2k.HTM",
-            "rights": "true",
-            "temporal": "1983-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Mine Safety and Health Administration",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Mine Safety and Health Administration"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "title": "EEOICP Program Statistics"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/STATS/PART50/p50y2k/p50y2k.HTM",
+            "describedByType": "application/pdf",
+            "description": "Actual information (raw data) from the accident and injury MSHA Form 7000-2 filed with MSHA by mining operators and contractors as required under 30 CFR Part 50.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8271,6 +8259,7 @@
                     "title": "Accident, Illness and Injury and Employment Self-Extracting Files (Part 50 Data)"
                 }
             ],
+            "identifier": "MSHA-19-012:030-183",
             "keyword": [
                 "7000-2",
                 "MSHA",
@@ -8280,56 +8269,57 @@
                 "mining",
                 "mining employment"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://arlweb.msha.gov/STATS/PART50/p50y2k/p50y2k.HTM",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:30:56.367Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Mine Safety and Health Administration",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Mine Safety and Health Administration"
+                }
+            },
             "references": [
                 "https://www.msha.gov/sites/default/files/Support_Resources/Forms/rptonpart50.pdf"
             ],
+            "rights": "true",
+            "temporal": "1983-01-01/2024-09-30",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "MSHA Part 50 Self-Extracting Files"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "MSHA - S&S Rate Calculator",
-            "description": "This tool shows the rate of S&S citations and orders per 100 inspection hours during a certain time period.\nThis tool is available after the initial Mine selection.",
-            "modified": "2024-12-11T21:34:39.868Z",
             "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-188",
-            "dataQuality": true,
-            "describedBy": "https://www.msha.gov/mine-data-retrieval-system",
-            "describedByType": "text/html",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Mine Safety and Health Administration",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Mine Safety and Health Administration"
-                }
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.msha.gov/mine-data-retrieval-system",
+            "describedByType": "text/html",
+            "description": "This tool shows the rate of S&S citations and orders per 100 inspection hours during a certain time period.\nThis tool is available after the initial Mine selection.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.msha.gov/mine-data-retrieval-system",
-                    "title": "MSHA Mine Data Retrieval System",
-                    "description": "After selecting a Mine, S&S Calculator will display as an option."
+                    "description": "After selecting a Mine, S&S Calculator will display as an option.",
+                    "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-188",
             "keyword": [
                 "MSHA",
                 "Significant and Substantial",
@@ -8337,60 +8327,50 @@
                 "mining",
                 "violations"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:34:39.868Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Concordance Database",
-            "description": "This database contains collections of documents from plans acquired via subpoena during investigation and litigation.",
-            "modified": "2021-04-02T17:35:19.813Z",
-            "accessLevel": "non-public",
-            "identifier": "EBSA-11-012:019-132",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Employee Benefits Security Administration",
+                "name": "Mine Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "title": "MSHA - S&S Rate Calculator"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "This database contains collections of documents from plans acquired via subpoena during investigation and litigation.",
+            "identifier": "EBSA-11-012:019-132",
             "keyword": [
                 "EBSA",
                 "Employee benefits",
                 "investigations"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-04-02T17:35:19.813Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Apprenticeship and Training Plan Notices (ATP) Database",
-            "description": "Database consists of notices filed by welfare plans that provide apprenticeship and/or training  benefits (ATP).",
-            "modified": "2021-04-02T17:48:28.088Z",
-            "accessLevel": "public",
-            "identifier": "EBSA-11-012:019-106",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employee Benefits Security Administration",
@@ -8399,33 +8379,33 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "Concordance Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "Database consists of notices filed by welfare plans that provide apprenticeship and/or training  benefits (ATP).",
+            "identifier": "EBSA-11-012:019-106",
             "keyword": [
                 "EBSA",
                 "apprenticeship"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-04-02T17:48:28.088Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Office of Exemption Determinations Case Tracking System (OED CTS) Database",
-            "description": "This database contains cases of submissions for requests for exemptions to Title I of ERISA (individual and class), along with applicable determinations, general correspondence, inquiries, and requests for clarification.",
-            "modified": "2021-04-02T15:37:51.447Z",
-            "accessLevel": "non-public",
-            "identifier": "EBSA-11-012:019-123",
-            "rights": "Restricted dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employee Benefits Security Administration",
@@ -8434,49 +8414,60 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Apprenticeship and Training Plan Notices (ATP) Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "This database contains cases of submissions for requests for exemptions to Title I of ERISA (individual and class), along with applicable determinations, general correspondence, inquiries, and requests for clarification.",
+            "identifier": "EBSA-11-012:019-123",
             "keyword": [
                 "Benefit Plans",
                 "EBSA",
                 "Exemptions",
                 "regulatory"
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
-            "title": "Published",
-            "description": "Conference Held dataset is used to analyze Conference records not held timely. The dataset contain the following information: all Conference records - either scheduled/rescheduled and pending OR held OR cancelled (excluding those records from deleted cases), Date conference scheduled/re-scheduled, Case Type, Payment Status, Case Status, Extent of Injury, Injury Type, Office of the User who closed Conference record, RCE of the Case when Conference record was closed.\nConference held within 45 days of request or reschedule; target: 90% (OPS Plan Goal Language).",
-            "modified": "2024-12-17T15:05:26.787Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-340",
-            "rights": "The dataset contains PII",
+            ],
+            "modified": "2021-04-02T15:37:51.447Z",
+            "programCode": [
+                "015:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
+                "name": "Employee Benefits Security Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "Restricted dataset",
+            "title": "Office of Exemption Determinations Case Tracking System (OED CTS) Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "Conference Held dataset is used to analyze Conference records not held timely. The dataset contain the following information: all Conference records - either scheduled/rescheduled and pending OR held OR cancelled (excluding those records from deleted cases), Date conference scheduled/re-scheduled, Case Type, Payment Status, Case Status, Extent of Injury, Injury Type, Office of the User who closed Conference record, RCE of the Case when Conference record was closed.\nConference held within 45 days of request or reschedule; target: 90% (OPS Plan Goal Language).",
+            "identifier": "OWCP-15-012:025-340",
             "keyword": [
                 "case",
                 "conference",
@@ -8484,24 +8475,13 @@
                 "longshore",
                 "status"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:05:26.787Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FECA Actuarial Report",
-            "description": "Report projecting potential future expenses for the FECA program and allocation by Federal agencies",
-            "modified": "2024-12-17T14:54:22.793Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:021-545",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -8510,35 +8490,35 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "title": "Published"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "Report projecting potential future expenses for the FECA program and allocation by Federal agencies",
+            "identifier": "OWCP-15-012:021-545",
             "keyword": [
                 "FECA",
                 "actuarial",
                 "expenses",
                 "future"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:54:22.793Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Energy Actuarial Report",
-            "description": "Report projecting potential future expenses for the Energy program",
-            "modified": "2024-12-17T14:53:13.932Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:023-546",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -8547,34 +8527,34 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "title": "FECA Actuarial Report"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "Report projecting potential future expenses for the Energy program",
+            "identifier": "OWCP-15-012:023-546",
             "keyword": [
                 "Energy",
                 "expenses",
                 "future"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:53:13.932Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ECS Case Management Data",
-            "description": "This dataset represents the information collected during the Energy Compensation System (ECS) case management process. It contains information about the number of claims received, actions taken, decisions and compensation.",
-            "modified": "2024-12-17T14:58:04.220Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-349",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -8583,57 +8563,66 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "title": "Energy Actuarial Report"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "This dataset represents the information collected during the Energy Compensation System (ECS) case management process. It contains information about the number of claims received, actions taken, decisions and compensation.",
+            "identifier": "OWCP-15-012:025-349",
             "keyword": [
                 "case",
                 "claims",
                 "decisions",
                 "energy"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:58:04.220Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA - Top 20 Most Frequently Cited Standards",
-            "description": "Lists top 20 most frequently CFR standards by mine type and primary canvass grouping.",
-            "modified": "2024-12-11T21:26:43.120Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-184",
-            "dataQuality": true,
-            "describedBy": "https://www.msha.gov/mine-data-retrieval-system",
-            "describedByType": "text/html",
-            "rights": "true",
-            "temporal": "1983-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Mine Safety and Health Administration",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Mine Safety and Health Administration"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "ECS Case Management Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.msha.gov/mine-data-retrieval-system",
+            "describedByType": "text/html",
+            "description": "Lists top 20 most frequently CFR standards by mine type and primary canvass grouping.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8641,6 +8630,7 @@
                     "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-184",
             "keyword": [
                 "CFR",
                 "MSHA",
@@ -8648,28 +8638,13 @@
                 "enforcement",
                 "mining"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:26:43.120Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA - Citations and Orders by Case Number",
-            "description": "Assessed violations by Assessment Case Number.\nYou need a valid Case Number in order to use this report.",
-            "modified": "2024-12-11T21:29:47.902Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-186",
-            "dataQuality": true,
-            "describedBy": "https://microstrategy.msha.gov/MicroStrategy/asp/mdrshelp/helpdocumentation.pdf",
-            "describedByType": "application/pdf",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -8678,12 +8653,26 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "1983-01-01/2024-09-30",
+            "title": "MSHA - Top 20 Most Frequently Cited Standards"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://microstrategy.msha.gov/MicroStrategy/asp/mdrshelp/helpdocumentation.pdf",
+            "describedByType": "application/pdf",
+            "description": "Assessed violations by Assessment Case Number.\nYou need a valid Case Number in order to use this report.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8691,35 +8680,21 @@
                     "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-186",
             "keyword": [
                 "MSHA",
                 "MSHA Case Number",
                 "assessed violations",
                 "mining"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:29:47.902Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA - High Dollar Citations and Orders Report",
-            "description": "This report provides data for citations, order and safeguards assessed at $10,000 or more.",
-            "modified": "2024-12-11T21:28:58.753Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-187",
-            "dataQuality": true,
-            "describedBy": "https://microstrategy.msha.gov/MicroStrategy/asp/mdrshelp/helpdocumentation.pdf",
-            "describedByType": "application/pdf",
-            "landingPage": "https://www.msha.gov/data-and-reports/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "2000-01-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -8728,12 +8703,25 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "title": "MSHA - Citations and Orders by Case Number"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://microstrategy.msha.gov/MicroStrategy/asp/mdrshelp/helpdocumentation.pdf",
+            "describedByType": "application/pdf",
+            "description": "This report provides data for citations, order and safeguards assessed at $10,000 or more.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8741,6 +8729,7 @@
                     "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-187",
             "keyword": [
                 "MSHA",
                 "assessments",
@@ -8749,117 +8738,101 @@
                 "mining",
                 "penalties"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/data-and-reports/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:28:58.753Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "SharePoint Case Portal Databases",
-            "description": "This database contains collections of documents from plans acquired via subpoena during investigation and litigation.",
-            "modified": "2021-04-02T17:33:51.726Z",
-            "accessLevel": "non-public",
-            "identifier": "EBSA-11-012:019-131",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Employee Benefits Security Administration",
+                "name": "Mine Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Mine Safety and Health Administration"
                 }
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Elaine Zimmerman",
-                "hasEmail": "mailto:zimmerman.elaine@dol.gov"
+            "rights": "true",
+            "temporal": "2000-01-01/2024-09-30",
+            "title": "MSHA - High Dollar Citations and Orders Report"
         },
-            "keyword": [
-                "EBSA",
-                "Employee benefits",
-                "investigations"
-            ],
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "bureauCode": [
                 "015:11"
             ],
-            "programCode": [
-                "015:001"
-            ],
-            "language": [
-                "en-US"
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Elaine Zimmerman",
+                "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA - Monthly Monitoring Tool for POV",
-            "description": "The tool provides a comparison of a mine's enforcement and injury data against the four POV screening criteria.\nThis tool is available after the initial Mine selection.",
-            "modified": "2024-12-11T21:32:22.888Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-189",
-            "dataQuality": true,
-            "describedBy": "https://www.msha.gov/mine-data-retrieval-system",
-            "describedByType": "text/html",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
+            "description": "This database contains collections of documents from plans acquired via subpoena during investigation and litigation.",
+            "identifier": "EBSA-11-012:019-131",
+            "keyword": [
+                "EBSA",
+                "Employee benefits",
+                "investigations"
+            ],
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-04-02T17:33:51.726Z",
+            "programCode": [
+                "015:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Mine Safety and Health Administration",
+                "name": "Employee Benefits Security Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Mine Safety and Health Administration"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "SharePoint Case Portal Databases"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.msha.gov/mine-data-retrieval-system",
+            "describedByType": "text/html",
+            "description": "The tool provides a comparison of a mine's enforcement and injury data against the four POV screening criteria.\nThis tool is available after the initial Mine selection.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.msha.gov/mine-data-retrieval-system",
-                    "title": "MSHA Mine Data Retrieval System",
-                    "description": "After selecting a mine, POV Calculator will be displayed as an option."
+                    "description": "After selecting a mine, POV Calculator will be displayed as an option.",
+                    "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-189",
             "keyword": [
                 "MSHA",
                 "POV",
                 "Pattern of Violations",
                 "mining"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:32:22.888Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://www.msha.gov/compliance-enforcement/pattern-violations-pov"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA - VPID Calculator",
-            "description": "Inspection days are derived by totaling the MSHA on-site inspection hours entered by Authorized Representatives of the Secretary (AR) for certain inspection activities and task codes and dividing by five. A remainder amount greater than zero increases the count by one. All of the inspectors' time (not including Travel time to and from the mines) at the mine site is included when calculating inspection days.\nCalculator is available after the initial Mine selection.",
-            "modified": "2024-12-11T21:39:23.369Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-190",
-            "describedBy": "https://www.msha.gov/mine-data-retrieval-system",
-            "describedByType": "text/html",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "2007-04-23/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -8868,20 +8841,36 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "references": [
+                "https://www.msha.gov/compliance-enforcement/pattern-violations-pov"
+            ],
+            "rights": "true",
+            "title": "MSHA - Monthly Monitoring Tool for POV"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "describedBy": "https://www.msha.gov/mine-data-retrieval-system",
+            "describedByType": "text/html",
+            "description": "Inspection days are derived by totaling the MSHA on-site inspection hours entered by Authorized Representatives of the Secretary (AR) for certain inspection activities and task codes and dividing by five. A remainder amount greater than zero increases the count by one. All of the inspectors' time (not including Travel time to and from the mines) at the mine site is included when calculating inspection days.\nCalculator is available after the initial Mine selection.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.msha.gov/mine-data-retrieval-system",
-                    "title": "MSHA Mine Data Retrieval System",
-                    "description": "After a user selects a Mine, VPID Calculator option will be displayed."
+                    "description": "After a user selects a Mine, VPID Calculator option will be displayed.",
+                    "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-190",
             "keyword": [
                 "MSHA",
                 "RPID",
@@ -8889,59 +8878,50 @@
                 "VPID Calculator",
                 "mining"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:39:23.369Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Top Hat Database",
-            "description": "Database consists of filing data for Top Hat plan notices for management and HCE's, who defer income until termination of employment, and are therefore exempt from ERISA.",
-            "modified": "2021-04-02T17:45:30.064Z",
-            "accessLevel": "public",
-            "identifier": "EBSA-11-012:019-105",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Employee Benefits Security Administration",
+                "name": "Mine Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "2007-04-23/2024-09-30",
+            "title": "MSHA - VPID Calculator"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "Database consists of filing data for Top Hat plan notices for management and HCE's, who defer income until termination of employment, and are therefore exempt from ERISA.",
+            "identifier": "EBSA-11-012:019-105",
             "keyword": [
                 "EBSA",
                 "Top Hat"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-04-02T17:45:30.064Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Auxiliary Health Insurance Data",
-            "description": "Imputed employer-sponsored health insurance coverage data which when linked to the March Annual Social and Economic Supplement to the Current Population Survey (March CPS), generates estimates of the number of individuals with different types of insurance coverage.",
-            "modified": "2021-04-02T18:03:27.457Z",
-            "accessLevel": "public",
-            "identifier": "EBSA-11-012:019-549",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employee Benefits Security Administration",
@@ -8950,11 +8930,22 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Top Hat Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "Imputed employer-sponsored health insurance coverage data which when linked to the March Annual Social and Economic Supplement to the Current Population Survey (March CPS), generates estimates of the number of individuals with different types of insurance coverage.",
+            "identifier": "EBSA-11-012:019-549",
             "keyword": [
                 "EBSA",
                 "Employer-Sponsored",
@@ -8962,24 +8953,13 @@
                 "health insurance",
                 "individuals"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-04-02T18:03:27.457Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Fee Disclosure Failure Notice Internal Database",
-            "description": "Database contains notification of a service provider's failure to disclose fee information required by the Department's 408(b)(2) regulation.",
-            "modified": "2021-04-02T18:08:07.590Z",
-            "accessLevel": "non-public",
-            "identifier": "EBSA-11-012:019-109",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employee Benefits Security Administration",
@@ -8988,46 +8968,57 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Auxiliary Health Insurance Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "Database contains notification of a service provider's failure to disclose fee information required by the Department's 408(b)(2) regulation.",
+            "identifier": "EBSA-11-012:019-109",
             "keyword": [
                 "EBSA"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-04-02T18:08:07.590Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Published",
-            "description": "Conference Memo Final dataset contains all Conference records that been held where at least 1 Interim Memo was Issued. It also includes the Interim Conference Issues start and end dates, case type, case status, payments status, Extent of Injury, Injury Type, Office of the User who issued conference memorandum type Final.\n*Measure the number of days between the date the conference is held and the memorandum type Final is issued (OPS Goal Language)",
-            "modified": "2024-12-17T15:04:19.035Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-339",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
+                "name": "Employee Benefits Security Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "Fee Disclosure Failure Notice Internal Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "Conference Memo Final dataset contains all Conference records that been held where at least 1 Interim Memo was Issued. It also includes the Interim Conference Issues start and end dates, case type, case status, payments status, Extent of Injury, Injury Type, Office of the User who issued conference memorandum type Final.\n*Measure the number of days between the date the conference is held and the memorandum type Final is issued (OPS Goal Language)",
+            "identifier": "OWCP-15-012:025-339",
             "keyword": [
                 "Memo",
                 "conference",
@@ -9035,24 +9026,13 @@
                 "longshore",
                 "payment"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:04:19.035Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Longshore non conference action data",
-            "description": "Non-Conference Action dataset contains all Intervention records received a recommendation within number of days with no conference, Resolutions Confirmation, Written Recommendation and DD Order (no records from deleted cases). It also contains the following data: Start Date and End Date, Case Type, Case Status, Extent of Injury, Injury Type, Office of the User who closed Intervention, RCE of the Case when Intervention record was closed.\nRecommendation for Intervention issue is made within 90 days of LS-7 if no conference; target: 85% (OPS Plan Goal Language).",
-            "modified": "2024-12-17T15:06:23.350Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-341",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -9061,12 +9041,23 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "title": "Published"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "Non-Conference Action dataset contains all Intervention records received a recommendation within number of days with no conference, Resolutions Confirmation, Written Recommendation and DD Order (no records from deleted cases). It also contains the following data: Start Date and End Date, Case Type, Case Status, Extent of Injury, Injury Type, Office of the User who closed Intervention, RCE of the Case when Intervention record was closed.\nRecommendation for Intervention issue is made within 90 days of LS-7 if no conference; target: 85% (OPS Plan Goal Language).",
+            "identifier": "OWCP-15-012:025-341",
             "keyword": [
                 "case",
                 "injury",
@@ -9074,24 +9065,13 @@
                 "longshore",
                 "resolution"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:06:23.350Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Published",
-            "description": "Intervention Issue Resolved or Closed dataset contains data to assist with analysis of the Intervention records not resolved timely. This dataset contains the following data: All Intervention records where resolution is Resolved prior to Intervention, Resolution Closed - Inactivity, Resolution Closed - Prolonged Duration, Resolutions Closed - Escalated to ALJ, Resolved With Conference, Resolved without Conference (excluding records from deleted cases), Received date, Case Type, Case Status, Payment Status, Extent of Injury, Injury Type, Office of the User who closed Intervention, User who closed Intervention, RCE of the Case at the time when the Intervention record was closed.\nIntervention issue resolved or closed within 90 days; target 85% (OPS Plan Goal Language).",
-            "modified": "2024-12-17T15:08:03.874Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-342",
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -9100,12 +9080,23 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "title": "Longshore non conference action data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "Intervention Issue Resolved or Closed dataset contains data to assist with analysis of the Intervention records not resolved timely. This dataset contains the following data: All Intervention records where resolution is Resolved prior to Intervention, Resolution Closed - Inactivity, Resolution Closed - Prolonged Duration, Resolutions Closed - Escalated to ALJ, Resolved With Conference, Resolved without Conference (excluding records from deleted cases), Received date, Case Type, Case Status, Payment Status, Extent of Injury, Injury Type, Office of the User who closed Intervention, User who closed Intervention, RCE of the Case at the time when the Intervention record was closed.\nIntervention issue resolved or closed within 90 days; target 85% (OPS Plan Goal Language).",
+            "identifier": "OWCP-15-012:025-342",
             "keyword": [
                 "case",
                 "injury",
@@ -9113,24 +9104,13 @@
                 "longshore",
                 "payment"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T15:08:03.874Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Longshore Financial Statements Audited",
-            "description": "Financial Statements and Independent Auditor's Report",
-            "modified": "2024-12-17T14:53:34.703Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:025-344",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -9139,35 +9119,35 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "title": "Published"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "Financial Statements and Independent Auditor's Report",
+            "identifier": "OWCP-15-012:025-344",
             "keyword": [
                 "audit",
                 "financial",
                 "longshore",
                 "statement"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:53:34.703Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FECA Quarterly Authoritative File Data",
-            "description": "Quarterly report detailing the FECA balance due from all Federal agencies.",
-            "modified": "2024-12-17T14:55:10.260Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:025-346",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -9176,35 +9156,35 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "title": "Longshore Financial Statements Audited"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "Quarterly report detailing the FECA balance due from all Federal agencies.",
+            "identifier": "OWCP-15-012:025-346",
             "keyword": [
                 "FECA",
                 "agency",
                 "balance",
                 "quarterly"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:55:10.260Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "DCCA Audited Financial Statements Data",
-            "description": "Financial Statements and Independent Auditor's Report",
-            "modified": "2024-12-17T14:52:51.484Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:025-347",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -9213,35 +9193,35 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "title": "FECA Quarterly Authoritative File Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "Financial Statements and Independent Auditor's Report",
+            "identifier": "OWCP-15-012:025-347",
             "keyword": [
                 "DCAA",
                 "FECA",
                 "financial",
                 "statement"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:52:51.484Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Black Lung Actuarial Report",
-            "description": "Report projecting potential future expenses for the Black Lung Disability Trust Fund",
-            "modified": "2024-12-17T14:54:41.622Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:024-547",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Workers\u2019 Compensation Programs",
@@ -9250,11 +9230,22 @@
                     "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "title": "DCCA Audited Financial Statements Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "Report projecting potential future expenses for the Black Lung Disability Trust Fund",
+            "identifier": "OWCP-15-012:024-547",
             "keyword": [
                 "Blacklung",
                 "disability",
@@ -9262,71 +9253,71 @@
                 "future",
                 "trust fund"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:54:41.622Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Qualified Termination Administrator Management System (QTAMS) Database",
-            "description": "This database contains ERISA abandoned plan terminations.",
-            "modified": "2021-04-02T16:38:44.993Z",
-            "accessLevel": "non-public",
-            "identifier": "EBSA-11-012:019-130",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Employee Benefits Security Administration",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "title": "Black Lung Actuarial Report"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elaine Zimmerman",
                 "hasEmail": "mailto:zimmerman.elaine@dol.gov"
             },
+            "description": "This database contains ERISA abandoned plan terminations.",
+            "identifier": "EBSA-11-012:019-130",
             "keyword": [
                 "EBSA"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-04-02T16:38:44.993Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Coal Excise Tax Report",
-            "description": "Report projecting potential future coal excise tax receipts for the Black Lung Disability Trust Fund",
-            "modified": "2024-12-17T14:55:38.524Z",
-            "accessLevel": "public",
-            "identifier": "OWCP-15-012:024-548",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
+                "name": "Employee Benefits Security Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "Qualified Termination Administrator Management System (QTAMS) Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "description": "Report projecting potential future coal excise tax receipts for the Black Lung Disability Trust Fund",
+            "identifier": "OWCP-15-012:024-548",
             "keyword": [
                 "Blacklung",
                 "coal",
@@ -9334,43 +9325,40 @@
                 "tax",
                 "trust fund"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:55:38.524Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA 107(a) Orders Issued",
-            "description": "Listing of 107(a) Orders issued by MSHA since July 1, 2010. This listing does not include any vacated orders.\nFrom Mine Act: SEC. 107. (a) If, upon any inspection or investigation of a coal or other mine which is subject to this Act, an authorized representative of the Secretary finds that an imminent danger exists, such representative shall determine the extent of the area of such mine throughout which the danger exists, and issue an order requiring the operator of such mine to cause all persons, except those referred to in section 104(c), to be withdrawn from, and to be prohibited from entering, such area until an authorized representative of the Secretary determines that such imminent danger and the conditions or practices which caused such imminent danger no longer exist. The issuance of an order under this subsection shall not preclude the issuance of a citation under section 104 or the. proposing of a penalty under section 110.",
-            "modified": "2024-12-11T21:33:34.785Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-182",
-            "dataQuality": true,
-            "describedBy": "https://arlweb.msha.gov/opengovernmentdata/DataSets/107(a)_Orders_Issued_Definition_File.txt",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
-            "temporal": "2010-07-01/2024-09-30",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Mine Safety and Health Administration",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Mine Safety and Health Administration"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "true",
+            "title": "Coal Excise Tax Report"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://arlweb.msha.gov/opengovernmentdata/DataSets/107(a)_Orders_Issued_Definition_File.txt",
+            "describedByType": "text/plain",
+            "description": "Listing of 107(a) Orders issued by MSHA since July 1, 2010. This listing does not include any vacated orders.\nFrom Mine Act: SEC. 107. (a) If, upon any inspection or investigation of a coal or other mine which is subject to this Act, an authorized representative of the Secretary finds that an imminent danger exists, such representative shall determine the extent of the area of such mine throughout which the danger exists, and issue an order requiring the operator of such mine to cause all persons, except those referred to in section 104(c), to be withdrawn from, and to be prohibited from entering, such area until an authorized representative of the Secretary determines that such imminent danger and the conditions or practices which caused such imminent danger no longer exist. The issuance of an order under this subsection shall not preclude the issuance of a citation under section 104 or the. proposing of a penalty under section 110.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9378,6 +9366,7 @@
                     "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-182",
             "keyword": [
                 "107 a Orders",
                 "Citations and Orders",
@@ -9387,28 +9376,14 @@
                 "mining",
                 "violations"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:33:34.785Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "MSHA - Mine Data Retrieval System (MDRS)",
-            "description": "Generates reports on mine's ownership, inspections, accidents, violations, VPID, POV, and Health Samples history.\n20 various flat files, uploaded every Friday, are under section Explore MSHA Datasets.",
-            "modified": "2024-12-11T21:32:44.752Z",
-            "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-185",
-            "dataQuality": true,
-            "describedBy": "https://microstrategy.msha.gov/MicroStrategy/asp/mdrshelp/helpdocumentation.pdf",
-            "describedByType": "text/plain",
-            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mine Safety and Health Administration",
@@ -9417,12 +9392,26 @@
                     "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "temporal": "2010-07-01/2024-09-30",
+            "title": "MSHA 107(a) Orders Issued"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://microstrategy.msha.gov/MicroStrategy/asp/mdrshelp/helpdocumentation.pdf",
+            "describedByType": "text/plain",
+            "description": "Generates reports on mine's ownership, inspections, accidents, violations, VPID, POV, and Health Samples history.\n20 various flat files, uploaded every Friday, are under section Explore MSHA Datasets.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9430,6 +9419,7 @@
                     "title": "MSHA Mine Data Retrieval System"
                 }
             ],
+            "identifier": "MSHA-19-012:030-185",
             "keyword": [
                 "MDRS",
                 "MSHA",
@@ -9437,75 +9427,63 @@
                 "mining data",
                 "mining open data"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/mine-data-retrieval-system",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:32:44.752Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Number of Requests Per Month per Key",
-            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
-            "modified": "2023-03-09T16:19:01.290Z",
-            "accessLevel": "public",
-            "identifier": "API_M-12-012:000-552",
-            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "API Management",
+                "name": "Mine Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "API Management"
+                    "name": "Mine Safety and Health Administration"
                 }
             },
+            "rights": "true",
+            "title": "MSHA - Mine Data Retrieval System (MDRS)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Keith Grabhorn",
                 "hasEmail": "mailto:Grabhorn.Keith@dol.gov"
             },
+            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://api.dol.gov/V1/ApiMetrics/PerKey/NumberOfRequestsPerMonthByKeys?KEY=352e8ef9-7b38-4428-875b-eefd39df6289&$filter=TOKEN%20eq%20guid%27352e8ef9-7b38-4428-875b-eefd39df6289%27",
-                    "format": "API",
-                    "title": "DOL API",
+                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata",
                     "description": "For these queries, a specially-configured $filter method is REQUIRED.",
-                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata"
+                    "format": "API",
+                    "title": "DOL API"
                 }
             ],
+            "identifier": "API_M-12-012:000-552",
             "keyword": [
                 "API MANAGEMENT",
                 "developer",
                 "metrics"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-03-09T16:19:01.290Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Top Datasets Per Month per Key",
-            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
-            "modified": "2023-03-09T16:22:58.941Z",
-            "accessLevel": "public",
-            "identifier": "API_M-12-012:000-557",
-            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "API Management",
@@ -9514,143 +9492,143 @@
                     "name": "API Management"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "Number of Requests Per Month per Key"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Keith Grabhorn",
                 "hasEmail": "mailto:Grabhorn.Keith@dol.gov"
             },
+            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://api.dol.gov/V1/ApiMetrics/PerKey/TopDatasetsPerMonthPerKeys?KEY=352e8ef9-7b38-4428-875b-eefd39df6289&$filter=TOKEN%20eq%20guid%27352e8ef9-7b38-4428-875b-eefd39df6289%27",
-                    "format": "API",
-                    "title": "DOL API",
+                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata",
                     "description": "For these queries, a specially-configured $filter method is REQUIRED.",
-                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata"
+                    "format": "API",
+                    "title": "DOL API"
                 }
             ],
+            "identifier": "API_M-12-012:000-557",
             "keyword": [
                 "API MANAGEMENT",
                 "developer",
                 "metrics"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-03-09T16:22:58.941Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "VETS-100A",
-            "description": "This dataset contains required veteran employment data by federal contractors/subcontractors. There are two tables V100DataDotGov and V100ADataDotGov. Both collections contain the past two years plus current filing cycle. V100AdataDotGov are reports entered for contracts that were established after December 1, 2003 and greater than $100,000.00. For additional information on data being reported review information at http://www.dol.gov/vets/vets-100.html#add.",
-            "modified": "2021-04-08T18:42:36.247Z",
-            "accessLevel": "non-public",
-            "identifier": "VETS-12-012:040-569",
-            "landingPage": "http://developer.dol.gov/others/vets100/",
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "Restricted dataset",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Veterans\u2019 Employment and Training Service",
+                "name": "API Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "API Management"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "Top Datasets Per Month per Key"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "012:25"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephanie Chan",
                 "hasEmail": "mailto:Chan.Stephanie.S@dol.gov"
             },
+            "description": "This dataset contains required veteran employment data by federal contractors/subcontractors. There are two tables V100DataDotGov and V100ADataDotGov. Both collections contain the past two years plus current filing cycle. V100AdataDotGov are reports entered for contracts that were established after December 1, 2003 and greater than $100,000.00. For additional information on data being reported review information at http://www.dol.gov/vets/vets-100.html#add.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://api.dol.gov/V1/VETS100/V100ADataDotGov?KEY=352e8ef9-7b38-4428-875b-eefd39df6289",
-                    "format": "API",
-                    "title": "DOL API",
+                    "describedBy": "http://api.dol.gov/V1/VETS100/$metadata",
                     "description": "API serving JSON and XML",
-                    "describedBy": "http://api.dol.gov/V1/VETS100/$metadata"
+                    "format": "API",
+                    "title": "DOL API"
                 }
             ],
+            "identifier": "VETS-12-012:040-569",
             "keyword": [
                 "VETS",
                 "Veterans"
             ],
-            "bureauCode": [
-                "012:25"
+            "landingPage": "http://developer.dol.gov/others/vets100/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-04-08T18:42:36.247Z",
             "programCode": [
                 "012:043"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Number of Requests Per Key",
-            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
-            "modified": "2023-03-09T16:20:00.365Z",
-            "accessLevel": "public",
-            "identifier": "API_M-12-012:000-551",
-            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "API Management",
+                "name": "Veterans\u2019 Employment and Training Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "API Management"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "Restricted dataset",
+            "title": "VETS-100A"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Keith Grabhorn",
                 "hasEmail": "mailto:Grabhorn.Keith@dol.gov"
             },
+            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://api.dol.gov/V1/ApiMetrics/PerKey/NumberOfRequestsPerKeys?KEY=352e8ef9-7b38-4428-875b-eefd39df6289&$filter=TOKEN%20eq%20guid%27352e8ef9-7b38-4428-875b-eefd39df6289%27",
-                    "format": "API",
-                    "title": "DOL API",
+                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata",
                     "description": "For these queries, a specially-configured $filter method is REQUIRED.",
-                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata"
+                    "format": "API",
+                    "title": "DOL API"
                 }
             ],
+            "identifier": "API_M-12-012:000-551",
             "keyword": [
                 "API MANAGEMENT",
                 "developer",
                 "metrics"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-03-09T16:20:00.365Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Number of Requests Per Year by Week per Key",
-            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
-            "modified": "2023-03-09T16:20:30.741Z",
-            "accessLevel": "public",
-            "identifier": "API_M-12-012:000-553",
-            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "API Management",
@@ -9659,47 +9637,47 @@
                     "name": "API Management"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "Number of Requests Per Key"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Keith Grabhorn",
                 "hasEmail": "mailto:Grabhorn.Keith@dol.gov"
             },
+            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://api.dol.gov/V1/ApiMetrics/PerKey/NumberOfRequestsPerYearByWeeks?KEY=352e8ef9-7b38-4428-875b-eefd39df6289&$filter=TOKEN%20eq%20guid%27352e8ef9-7b38-4428-875b-eefd39df6289%27",
-                    "format": "API",
-                    "title": "DOL API",
+                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata",
                     "description": "For these queries, a specially-configured $filter method is REQUIRED.",
-                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata"
+                    "format": "API",
+                    "title": "DOL API"
                 }
             ],
+            "identifier": "API_M-12-012:000-553",
             "keyword": [
                 "API MANAGEMENT",
                 "developer",
                 "metrics"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-03-09T16:20:30.741Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Top Datasets Per Week per Key",
-            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
-            "modified": "2023-03-09T19:16:48.254Z",
-            "accessLevel": "public",
-            "identifier": "API_M-12-012:000-558",
-            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "API Management",
@@ -9708,47 +9686,47 @@
                     "name": "API Management"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "Number of Requests Per Year by Week per Key"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Keith Grabhorn",
                 "hasEmail": "mailto:Grabhorn.Keith@dol.gov"
             },
+            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://api.dol.gov/V1/ApiMetrics/PerKey/TopDatasetsPerWeekPerKeys?KEY=352e8ef9-7b38-4428-875b-eefd39df6289&$filter=TOKEN%20eq%20guid%27352e8ef9-7b38-4428-875b-eefd39df6289%27",
-                    "format": "API",
-                    "title": "DOL API",
+                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata",
                     "description": "For these queries, a specially-configured $filter method is REQUIRED.",
-                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata"
+                    "format": "API",
+                    "title": "DOL API"
                 }
             ],
+            "identifier": "API_M-12-012:000-558",
             "keyword": [
                 "API MANAGEMENT",
                 "developer",
                 "metrics"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-03-09T19:16:48.254Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Top Data Tables Per Week per Key",
-            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
-            "modified": "2023-03-09T19:16:04.712Z",
-            "accessLevel": "public",
-            "identifier": "API_M-12-012:000-563",
-            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "API Management",
@@ -9757,47 +9735,47 @@
                     "name": "API Management"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "Top Datasets Per Week per Key"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Keith Grabhorn",
                 "hasEmail": "mailto:Grabhorn.Keith@dol.gov"
             },
+            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://api.dol.gov/V1/ApiMetrics/PerKey/TopDataTablesPerKeyWeeks?KEY=352e8ef9-7b38-4428-875b-eefd39df6289&$filter=TOKEN%20eq%20guid%27352e8ef9-7b38-4428-875b-eefd39df6289%27",
-                    "format": "API",
-                    "title": "DOL API",
+                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata",
                     "description": "For these queries, a specially-configured $filter method is REQUIRED.",
-                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata"
+                    "format": "API",
+                    "title": "DOL API"
                 }
             ],
+            "identifier": "API_M-12-012:000-563",
             "keyword": [
                 "API MANAGEMENT",
                 "developer",
                 "metrics"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-03-09T19:16:04.712Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Number of Requests Per Day per Key",
-            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
-            "modified": "2023-03-09T16:33:14.674Z",
-            "accessLevel": "public",
-            "identifier": "API_M-12-012:000-550",
-            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "API Management",
@@ -9806,47 +9784,47 @@
                     "name": "API Management"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "Top Data Tables Per Week per Key"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Keith Grabhorn",
                 "hasEmail": "mailto:Grabhorn.Keith@dol.gov"
             },
+            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://api.dol.gov/V1/ApiMetrics/PerKey/NumberOfRequestsPerDayByKeys?KEY=352e8ef9-7b38-4428-875b-eefd39df6289&$filter=TOKEN%20eq%20guid%27352e8ef9-7b38-4428-875b-eefd39df6289%27",
-                    "format": "API",
-                    "title": "DOL API",
+                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata",
                     "description": "For these queries, a specially-configured $filter method is REQUIRED.",
-                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata"
+                    "format": "API",
+                    "title": "DOL API"
                 }
             ],
+            "identifier": "API_M-12-012:000-550",
             "keyword": [
                 "API MANAGEMENT",
                 "developer",
                 "metrics"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-03-09T16:33:14.674Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Top Datasets Per Year per Key",
-            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
-            "modified": "2023-03-09T16:22:09.748Z",
-            "accessLevel": "public",
-            "identifier": "API_M-12-012:000-559",
-            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "API Management",
@@ -9855,47 +9833,47 @@
                     "name": "API Management"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "Number of Requests Per Day per Key"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Keith Grabhorn",
                 "hasEmail": "mailto:Grabhorn.Keith@dol.gov"
             },
+            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://api.dol.gov/V1/ApiMetrics/PerKey/TopDatasetsPerYearPerKeys?KEY=352e8ef9-7b38-4428-875b-eefd39df6289&$filter=TOKEN%20eq%20guid%27352e8ef9-7b38-4428-875b-eefd39df6289%27",
-                    "format": "API",
-                    "title": "DOL API",
+                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata",
                     "description": "For these queries, a specially-configured $filter method is REQUIRED.",
-                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata"
+                    "format": "API",
+                    "title": "DOL API"
                 }
             ],
+            "identifier": "API_M-12-012:000-559",
             "keyword": [
                 "API MANAGEMENT",
                 "developer",
                 "metrics"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-03-09T16:22:09.748Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Top Datasets Per Key",
-            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
-            "modified": "2023-03-09T16:26:47.226Z",
-            "accessLevel": "public",
-            "identifier": "API_M-12-012:000-556",
-            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "API Management",
@@ -9904,47 +9882,47 @@
                     "name": "API Management"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "Top Datasets Per Year per Key"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Keith Grabhorn",
                 "hasEmail": "mailto:Grabhorn.Keith@dol.gov"
             },
+            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://api.dol.gov/V1/ApiMetrics/PerKey/TopDatasetsPerKeys?KEY=352e8ef9-7b38-4428-875b-eefd39df6289&$filter=TOKEN%20eq%20guid%27352e8ef9-7b38-4428-875b-eefd39df6289%27",
-                    "format": "API",
-                    "title": "DOL API",
+                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata",
                     "description": "For these queries, a specially-configured $filter method is REQUIRED.",
-                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata"
+                    "format": "API",
+                    "title": "DOL API"
                 }
             ],
+            "identifier": "API_M-12-012:000-556",
             "keyword": [
                 "API MANAGEMENT",
                 "developer",
                 "metrics"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-03-09T16:26:47.226Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Top Data Tables Per Month per Key",
-            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
-            "modified": "2023-03-09T16:31:03.819Z",
-            "accessLevel": "public",
-            "identifier": "API_M-12-012:000-562",
-            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "API Management",
@@ -9953,47 +9931,47 @@
                     "name": "API Management"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "Top Datasets Per Key"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Keith Grabhorn",
                 "hasEmail": "mailto:Grabhorn.Keith@dol.gov"
             },
+            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://api.dol.gov/V1/ApiMetrics/PerKey/TopDataTablesPerKeyMonths?KEY=352e8ef9-7b38-4428-875b-eefd39df6289&$filter=TOKEN%20eq%20guid%27352e8ef9-7b38-4428-875b-eefd39df6289%27",
-                    "format": "API",
-                    "title": "DOL API",
+                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata",
                     "description": "For these queries, a specially-configured $filter method is REQUIRED.",
-                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata"
+                    "format": "API",
+                    "title": "DOL API"
                 }
             ],
+            "identifier": "API_M-12-012:000-562",
             "keyword": [
                 "API MANAGEMENT",
                 "developer",
                 "metrics"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-03-09T16:31:03.819Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Top Data Tables Per Year per Key",
-            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
-            "modified": "2023-03-09T16:32:08.537Z",
-            "accessLevel": "public",
-            "identifier": "API_M-12-012:000-564",
-            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "API Management",
@@ -10002,47 +9980,47 @@
                     "name": "API Management"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "Top Data Tables Per Month per Key"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Keith Grabhorn",
                 "hasEmail": "mailto:Grabhorn.Keith@dol.gov"
             },
+            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://api.dol.gov/V1/ApiMetrics/PerKey/TopDataTablesPerKeyYears?KEY=352e8ef9-7b38-4428-875b-eefd39df6289&$filter=TOKEN%20eq%20guid%27352e8ef9-7b38-4428-875b-eefd39df6289%27",
-                    "format": "API",
-                    "title": "DOL API",
+                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata",
                     "description": "For these queries, a specially-configured $filter method is REQUIRED.",
-                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata"
+                    "format": "API",
+                    "title": "DOL API"
                 }
             ],
+            "identifier": "API_M-12-012:000-564",
             "keyword": [
                 "API MANAGEMENT",
                 "developer",
                 "metrics"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-03-09T16:32:08.537Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Top Datasets Per Day per Key",
-            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
-            "modified": "2023-03-09T16:27:36.555Z",
-            "accessLevel": "public",
-            "identifier": "API_M-12-012:000-555",
-            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "API Management",
@@ -10051,47 +10029,47 @@
                     "name": "API Management"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "Top Data Tables Per Year per Key"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Keith Grabhorn",
                 "hasEmail": "mailto:Grabhorn.Keith@dol.gov"
             },
+            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://api.dol.gov/V1/ApiMetrics/PerKey/TopDatasetsPerDayPerKeys?KEY=352e8ef9-7b38-4428-875b-eefd39df6289&$filter=TOKEN%20eq%20guid%27352e8ef9-7b38-4428-875b-eefd39df6289%27",
-                    "format": "API",
-                    "title": "DOL API",
+                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata",
                     "description": "For these queries, a specially-configured $filter method is REQUIRED.",
-                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata"
+                    "format": "API",
+                    "title": "DOL API"
                 }
             ],
+            "identifier": "API_M-12-012:000-555",
             "keyword": [
                 "API MANAGEMENT",
                 "developer",
                 "metrics"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-03-09T16:27:36.555Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Top Data Tables Per Day per Key",
-            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
-            "modified": "2023-03-09T16:30:22.709Z",
-            "accessLevel": "public",
-            "identifier": "API_M-12-012:000-560",
-            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "API Management",
@@ -10100,47 +10078,47 @@
                     "name": "API Management"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "Top Datasets Per Day per Key"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Keith Grabhorn",
                 "hasEmail": "mailto:Grabhorn.Keith@dol.gov"
             },
+            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://api.dol.gov/V1/ApiMetrics/PerKey/TopDataTablesPerKeyDays?KEY=352e8ef9-7b38-4428-875b-eefd39df6289&$filter=TOKEN%20eq%20guid%27352e8ef9-7b38-4428-875b-eefd39df6289%27",
-                    "format": "API",
-                    "title": "DOL API",
+                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata",
                     "description": "For these queries, a specially-configured $filter method is REQUIRED.",
-                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata"
+                    "format": "API",
+                    "title": "DOL API"
                 }
             ],
+            "identifier": "API_M-12-012:000-560",
             "keyword": [
                 "API MANAGEMENT",
                 "developer",
                 "metrics"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-03-09T16:30:22.709Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Top Data Tables Per Key",
-            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
-            "modified": "2023-03-09T16:29:14.681Z",
-            "accessLevel": "public",
-            "identifier": "API_M-12-012:000-561",
-            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "API Management",
@@ -10149,47 +10127,47 @@
                     "name": "API Management"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "Top Data Tables Per Day per Key"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Keith Grabhorn",
                 "hasEmail": "mailto:Grabhorn.Keith@dol.gov"
             },
+            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://api.dol.gov/V1/ApiMetrics/PerKey/TopDataTablesPerKeys?KEY=352e8ef9-7b38-4428-875b-eefd39df6289&$filter=TOKEN%20eq%20guid%27352e8ef9-7b38-4428-875b-eefd39df6289%27",
-                    "format": "API",
-                    "title": "DOL API",
+                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata",
                     "description": "For these queries, a specially-configured $filter method is REQUIRED.",
-                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata"
+                    "format": "API",
+                    "title": "DOL API"
                 }
             ],
+            "identifier": "API_M-12-012:000-561",
             "keyword": [
                 "API MANAGEMENT",
                 "developer",
                 "metrics"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://developer.dol.gov/others/api-metrics-per-key/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-03-09T16:29:14.681Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Number of Requests Per Year per Key",
-            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
-            "modified": "2023-03-09T16:32:46.446Z",
-            "accessLevel": "public",
-            "identifier": "API_M-12-012:000-554",
-            "landingPage": "http://developer.dol.gov/others/api-metrics-key",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "API Management",
@@ -10198,130 +10176,130 @@
                     "name": "API Management"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "Top Data Tables Per Key"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Keith Grabhorn",
                 "hasEmail": "mailto:Grabhorn.Keith@dol.gov"
             },
+            "description": "Developers using the DOL-wide API have access to a variety of queries providing usage metrics for their app's key.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://api.dol.gov/V1/ApiMetrics/PerKey/NumberOfRequestsPerYearByKeys?KEY=352e8ef9-7b38-4428-875b-eefd39df6289&$filter=TOKEN%20eq%20guid%27352e8ef9-7b38-4428-875b-eefd39df6289%27",
-                    "format": "API",
-                    "title": "DOL API",
+                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata",
                     "description": "For these queries, a specially-configured $filter method is REQUIRED.",
-                    "describedBy": "http://api.dol.gov/V1/ApiMetrics/PerKey/$metadata"
+                    "format": "API",
+                    "title": "DOL API"
                 }
             ],
+            "identifier": "API_M-12-012:000-554",
             "keyword": [
                 "API MANAGEMENT",
                 "developer",
                 "metrics"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://developer.dol.gov/others/api-metrics-key",
+            "language": [
+                "en-US"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-03-09T16:32:46.446Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "VETS-100",
-            "description": "This dataset contains required veteran employment data by federal contractors/subcontractors. There are two tables V100DataDotGov and V100ADataDotGov. Both collections contain the past two years plus current filing cycle. V100DataDotGov are reports entered for contracts that were established prior to December 1, 2003 and greater than $25,000.00. For additional information on data being reported review information at http://www.dol.gov/vets/vets-100.html#add.",
-            "modified": "2021-04-12T17:25:27.066Z",
-            "accessLevel": "non-public",
-            "identifier": "VETS-12-012:040-568",
-            "landingPage": "http://developer.dol.gov/others/vets100/",
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "Restricted dataset",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Veterans\u2019 Employment and Training Service",
+                "name": "API Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Veterans\u2019 Employment and Training Service"
+                    "name": "API Management"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "Number of Requests Per Year per Key"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "012:25"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephanie Chan",
                 "hasEmail": "mailto:Chan.Stephanie.S@dol.gov"
             },
+            "description": "This dataset contains required veteran employment data by federal contractors/subcontractors. There are two tables V100DataDotGov and V100ADataDotGov. Both collections contain the past two years plus current filing cycle. V100DataDotGov are reports entered for contracts that were established prior to December 1, 2003 and greater than $25,000.00. For additional information on data being reported review information at http://www.dol.gov/vets/vets-100.html#add.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://api.dol.gov/V1/VETS100/V100DataDotGov?KEY=352e8ef9-7b38-4428-875b-eefd39df6289",
-                    "format": "API",
-                    "title": "DOL API",
+                    "describedBy": "http://api.dol.gov/V1/VETS100/$metadata",
                     "description": "API serving JSON and XML",
-                    "describedBy": "http://api.dol.gov/V1/VETS100/$metadata"
+                    "format": "API",
+                    "title": "DOL API"
                 }
             ],
+            "identifier": "VETS-12-012:040-568",
             "keyword": [
                 "VETS",
                 "Veterans"
             ],
-            "bureauCode": [
-                "012:25"
+            "landingPage": "http://developer.dol.gov/others/vets100/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-04-12T17:25:27.066Z",
             "programCode": [
                 "012:043"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "DOL Enterprise Physical Access Control System (DOL EPACS)",
-            "description": "DOL ePACS is the physical access control system that is used to manage authorized physical access to the DOL Frances Perkins Building and some regional DOL locations. This system uses the GSA USAccess PIV badge issued for DOL, as the primary token for authenticating holders at the entrances of the DOL FPB and regional integrated locations.  Access is granted based on the employment status.",
-            "modified": "2024-09-23T13:52:47.045Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM SC-25-012:044-292",
-            "rights": "Internal dataset",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
+                "name": "Veterans\u2019 Employment and Training Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
+                    "name": "Veterans\u2019 Employment and Training Service"
                 }
             },
+            "rights": "Restricted dataset",
+            "title": "VETS-100"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Robert Behm, Tim Deane",
                 "hasEmail": "mailto:behm.robert@dol.gov"
             },
+            "description": "DOL ePACS is the physical access control system that is used to manage authorized physical access to the DOL Frances Perkins Building and some regional DOL locations. This system uses the GSA USAccess PIV badge issued for DOL, as the primary token for authenticating holders at the entrances of the DOL FPB and regional integrated locations.  Access is granted based on the employment status.",
+            "identifier": "OASAM SC-25-012:044-292",
             "keyword": [
                 "OASAM",
                 "SC"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:52:47.045Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Fleet cards vehicle tags account codes",
-            "description": "Citibank Fleet Card",
-            "modified": "2024-06-27T14:01:04.878Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM BOC-25-012:044-219",
-            "landingPage": "https://home.cards.citidirect.com/CommercialCard/ux/index.html#/",
-            "rights": "Internal dataset",
-            "spatial": "location characteristics",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -10330,39 +10308,36 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "Internal dataset",
+            "title": "DOL Enterprise Physical Access Control System (DOL EPACS)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Heath Rehkop",
                 "hasEmail": "mailto:rehkop.christopher.h@dol.gov"
             },
+            "description": "Citibank Fleet Card",
+            "identifier": "OASAM BOC-25-012:044-219",
             "keyword": [
                 "BOC",
                 "CITI",
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://home.cards.citidirect.com/CommercialCard/ux/index.html#/",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-06-27T14:01:04.878Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://home.cards.citidirect.com/CommercialCard/ux/index.html#/"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Formulation Execution Performance and Planning",
-            "description": "DEBS collects data in the context of automating the end-to-end budget formulation and execution lifecycle, and key departmental performance processes.",
-            "modified": "2024-09-23T12:47:08.157Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM DBC-25-012:044-229",
-            "landingPage": "https://debs.dol.gov",
-            "rights": "restricted",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -10371,12 +10346,27 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "references": [
+                "https://home.cards.citidirect.com/CommercialCard/ux/index.html#/"
+            ],
+            "rights": "Internal dataset",
+            "spatial": "location characteristics",
+            "title": "Fleet cards vehicle tags account codes"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Christopher Banks",
                 "hasEmail": "mailto:banks.christopher@dol.gov"
             },
+            "description": "DEBS collects data in the context of automating the end-to-end budget formulation and execution lifecycle, and key departmental performance processes.",
+            "identifier": "OASAM DBC-25-012:044-229",
             "keyword": [
                 "DBC",
                 "OASAM",
@@ -10387,25 +10377,14 @@
                 "justification",
                 "performance"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://debs.dol.gov",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T12:47:08.157Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Sustainability Plan OMB Sustainability Scorecard",
-            "description": "MAX.GOV Provided by Office of Management and Budget (OMB) as the portal for submitting Sustainability Plan, Appendices, OMB Energy/Sustainability Scorecards, and other OMB and CEQ required reports. Also a portal for other activities (unrelated to Sustainability and Energy).",
-            "modified": "2024-06-27T17:08:08.980Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM BOC-25-012:044-225",
-            "landingPage": "https://www.energystar.gov/buildings/facility-owners-and-managers/existing-buildings/use-portfolio-manager",
-            "rights": "private",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -10414,39 +10393,35 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "restricted",
+            "title": "Formulation Execution Performance and Planning"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kathryn Simpson",
                 "hasEmail": "mailto:simpson.kathryn.j@dol.gov"
             },
+            "description": "MAX.GOV Provided by Office of Management and Budget (OMB) as the portal for submitting Sustainability Plan, Appendices, OMB Energy/Sustainability Scorecards, and other OMB and CEQ required reports. Also a portal for other activities (unrelated to Sustainability and Energy).",
+            "identifier": "OASAM BOC-25-012:044-225",
             "keyword": [
                 "BOC",
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.energystar.gov/buildings/facility-owners-and-managers/existing-buildings/use-portfolio-manager",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-06-27T17:08:08.980Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://www.energystar.gov/buildings/facility-owners-and-managers/existing-buildings/use-portfolio-manager"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "vehicle fuel tank configuration fueling information and alternative fuel use",
-            "description": "DOE/EERE Fleet Sustainability Dashboard (FleetDash)",
-            "modified": "2024-06-27T14:02:31.958Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM BOC-25-012:044-220",
-            "landingPage": "https://federalfleets.energy.gov/FleetDASH/",
-            "rights": "restricted",
-            "spatial": "location characteristics, address",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -10455,65 +10430,80 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "references": [
+                "https://www.energystar.gov/buildings/facility-owners-and-managers/existing-buildings/use-portfolio-manager"
+            ],
+            "rights": "private",
+            "title": "Sustainability Plan OMB Sustainability Scorecard"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Heath Rehkop",
                 "hasEmail": "mailto:rehkop.christopher.h@dol.gov"
             },
+            "description": "DOE/EERE Fleet Sustainability Dashboard (FleetDash)",
+            "identifier": "OASAM BOC-25-012:044-220",
             "keyword": [
                 "BOC",
                 "Fed Fleet",
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://federalfleets.energy.gov/FleetDASH/",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-06-27T14:02:31.958Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Assistant Secretary for Administration and Management",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Assistant Secretary for Administration and Management"
+                }
+            },
             "references": [
                 "https://federalfleets.energy.gov/FleetDASH/"
             ],
+            "rights": "restricted",
+            "spatial": "location characteristics, address",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "vehicle fuel tank configuration fueling information and alternative fuel use"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "low wage high violation industries",
-            "description": "Case data for investigations in industries marked by a generally low wage workforce, low complaint rates, and high violation rates",
-            "modified": "2024-12-16T15:08:06.620Z",
             "accessLevel": "public",
-            "identifier": "WHD-16-012:027-370",
-            "issued": "2024-11-01",
-            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/low-wage-high-violation-industries",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Wage and Hour Division",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Wage and Hour Division"
-                }
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alex Cruz",
                 "hasEmail": "mailto:cruz.alexander@dol.gov"
             },
+            "description": "Case data for investigations in industries marked by a generally low wage workforce, low complaint rates, and high violation rates",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/whd/data/charts/low-wage-high-violation-industries",
-                    "title": "Low Wage, High Violation Industries",
-                    "description": "Case data for investigations in industries marked by a generally low wage workforce, low complaint rates, and high violation rates"
+                    "description": "Case data for investigations in industries marked by a generally low wage workforce, low complaint rates, and high violation rates",
+                    "title": "Low Wage, High Violation Industries"
                 }
             ],
+            "identifier": "WHD-16-012:027-370",
+            "issued": "2024-11-01",
             "keyword": [
                 "Garment",
                 "Salons",
@@ -10525,26 +10515,14 @@
                 "hotel",
                 "retail"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/low-wage-high-violation-industries",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T15:08:06.620Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "WHD enforcement statistics all acts",
-            "description": "Six data points are listed per year, including concluded cases, registered complaints, and enforcement hours",
-            "modified": "2024-12-16T15:03:54.935Z",
-            "accessLevel": "public",
-            "identifier": "WHD-16-012:027-368",
-            "issued": "2024-11-01",
-            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/all-acts",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Wage and Hour Division",
@@ -10553,175 +10531,187 @@
                     "name": "Wage and Hour Division"
                 }
             },
+            "rights": "true",
+            "title": "low wage high violation industries"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alex Cruz",
                 "hasEmail": "mailto:cruz.alexander@dol.gov"
             },
+            "description": "Six data points are listed per year, including concluded cases, registered complaints, and enforcement hours",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/whd/data/charts/all-acts",
-                    "title": "WHD Enforcement Statistics: All Acts",
-                    "description": "Six data points are listed per year, including concluded cases, registered complaints, and enforcement hours"
+                    "description": "Six data points are listed per year, including concluded cases, registered complaints, and enforcement hours",
+                    "title": "WHD Enforcement Statistics: All Acts"
                 }
             ],
+            "identifier": "WHD-16-012:027-368",
+            "issued": "2024-11-01",
             "keyword": [
                 "WHD"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/whd/data/charts/all-acts",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T15:03:54.935Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Sweat and Toil API",
-            "description": "These datasets contain information on child labor and forced labor worldwide from ILAB\u2019s three flagship reports: Findings on the Worst Forms of Child Labor; List of Goods Produced by Child Labor or Forced Labor; and List of Products Produced by Forced or Indentured Child Labor. There are 14 tables containing data from the 2015-2019 reporting cycles and 11 tables from the 2014 reporting cycle. ILAB plans to update the structure of the API. This information is also available in ILAB\u2019s app, Sweat & Toil: Child Labor, Forced Labor, and Human Trafficking Around the World. For more information, see ILAB\u2019s International Child Labor and Forced Labor Reports page. https://www.dol.gov/agencies/ilab/resources/reports/child-labor/findings https://developer.dol.gov/others/sweat-and-toil/",
-            "modified": "2022-03-24T17:42:55.836Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-139",
-            "landingPage": "https://developer.dol.gov/others/sweat-and-toil/",
-            "license": "https://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Bureau of International Labor Affairs",
+                "name": "Wage and Hour Division",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Bureau of International Labor Affairs"
+                    "name": "Wage and Hour Division"
                 }
             },
+            "rights": "true",
+            "title": "WHD enforcement statistics all acts"
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
                 "fn": "Claudia Giudi",
                 "hasEmail": "mailto:guidi.claudia.l@dol.gov"
             },
+            "description": "These datasets contain information on child labor and forced labor worldwide from ILAB\u2019s three flagship reports: Findings on the Worst Forms of Child Labor; List of Goods Produced by Child Labor or Forced Labor; and List of Products Produced by Forced or Indentured Child Labor. There are 14 tables containing data from the 2015-2019 reporting cycles and 11 tables from the 2014 reporting cycle. ILAB plans to update the structure of the API. This information is also available in ILAB\u2019s app, Sweat & Toil: Child Labor, Forced Labor, and Human Trafficking Around the World. For more information, see ILAB\u2019s International Child Labor and Forced Labor Reports page. https://www.dol.gov/agencies/ilab/resources/reports/child-labor/findings https://developer.dol.gov/others/sweat-and-toil/",
+            "identifier": "ILAB-12-012:037-139",
             "keyword": [
                 "ILAB",
                 "child labor"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://developer.dol.gov/others/sweat-and-toil/",
+            "language": [
+                "en-US"
             ],
+            "license": "https://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2022-03-24T17:42:55.836Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual NonFederal Recipient Data and Exchange Sale Transactions",
-            "description": "GSA Personal Property Reporting Tool (PPRT)",
-            "modified": "2024-12-09T18:26:20.008Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM BOC-25-012:044-222",
-            "landingPage": "https://www.property.reporting.gov/PPRT/PPRTLogin",
-            "rights": "restricted",
-            "spatial": "Address, location characteristics",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
+                "name": "Bureau of International Labor Affairs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
+                    "name": "Bureau of International Labor Affairs"
                 }
             },
+            "rights": "true",
+            "title": "Sweat and Toil API"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Brianna Butler",
                 "hasEmail": "mailto:butler.brianna.k@dol.gov"
             },
+            "description": "GSA Personal Property Reporting Tool (PPRT)",
+            "identifier": "OASAM BOC-25-012:044-222",
             "keyword": [
                 "BOC",
                 "OASAM",
                 "PPRT"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.property.reporting.gov/PPRT/PPRTLogin",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-09T18:26:20.008Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Assistant Secretary for Administration and Management",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Assistant Secretary for Administration and Management"
+                }
+            },
             "references": [
                 "https://www.property.reporting.gov/PPRT/PPRTLogin"
             ],
+            "rights": "restricted",
+            "spatial": "Address, location characteristics",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "Annual NonFederal Recipient Data and Exchange Sale Transactions"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "National Farmworker Jobs Program Quarterly Performance Report (QPR) Data",
-            "description": "The NFJP QPR collects aggregate data on a quarterly, annual, and program-to-date basis on number of participants, characteristics of participants, and interim and long-term performance outcomes.",
-            "modified": "2022-12-12T00:00:00Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:002-544",
-            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
-            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
-            "rights": "TRUE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Employment and Training Administration"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Steve Rietzke",
                 "hasEmail": "mailto:rietzke.steven@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
+            "description": "The NFJP QPR collects aggregate data on a quarterly, annual, and program-to-date basis on number of participants, characteristics of participants, and interim and long-term performance outcomes.",
+            "identifier": "ETA-5-012:002-544",
             "keyword": [
                 "ETA",
                 "employment and training",
                 "farmworker",
                 "narrative"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-12-12T00:00:00Z",
             "programCode": [
                 "012:002"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Employment and Training Administration"
+            },
+            "rights": "TRUE",
+            "title": "National Farmworker Jobs Program Quarterly Performance Report (QPR) Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Mine Safety and Health At A Glance Calendar year",
-            "description": "Reports the following metrics:  All injury rate; citations and orders issued, dollar amount assessed (millions); fatal injury rate; fatalities; number of miners; number of mines; production (millions of tons); S&S citations and orders (%); Total mining area inspection (hours per mine)",
-            "modified": "2024-12-11T21:23:26.580Z",
             "accessLevel": "public",
-            "identifier": "MSHA-19-012:030-144",
-            "landingPage": "https://www.msha.gov/msha-glance",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Mine Safety and Health Administration",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Mine Safety and Health Administration"
-                }
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Victor Yu",
                 "hasEmail": "mailto:yu.victor@dol.gov"
             },
+            "description": "Reports the following metrics:  All injury rate; citations and orders issued, dollar amount assessed (millions); fatal injury rate; fatalities; number of miners; number of mines; production (millions of tons); S&S citations and orders (%); Total mining area inspection (hours per mine)",
+            "identifier": "MSHA-19-012:030-144",
             "keyword": [
                 "MSHA",
                 "MSHA At the Glance",
@@ -10738,206 +10728,195 @@
                 "mining trends",
                 "mining yearly comparisons"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.msha.gov/msha-glance",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-11T21:23:26.580Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://www.msha.gov/msha-glance"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Master Listing of Grant Information for OTLA projects",
-            "description": "Administrative/Grant management, cooperative agreements",
-            "modified": "2021-09-02T14:02:27.647Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-548",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Bureau of International Labor Affairs",
+                "name": "Mine Safety and Health Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Mine Safety and Health Administration"
                 }
             },
+            "references": [
+                "https://www.msha.gov/msha-glance"
+            ],
+            "rights": "true",
+            "title": "Mine Safety and Health At A Glance Calendar year"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bruce Yoon",
                 "hasEmail": "mailto:Yoon.Bruce@dol.gov"
             },
+            "description": "Administrative/Grant management, cooperative agreements",
+            "identifier": "ILAB-12-012:037-548",
             "keyword": [
                 "ILAB"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-09-02T14:02:27.647Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "White House Gender Policy Council Strategy",
-            "description": "White House Gender Policy Council Strategy",
-            "modified": "2022-01-05T17:22:21.162Z",
-            "accessLevel": "non-public",
-            "identifier": "WB-12-012:038-579",
-            "rights": "not published yet",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Women's Bureau",
+                "name": "Bureau of International Labor Affairs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Women's Bureau"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Master Listing of Grant Information for OTLA projects"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tiffany Boiman",
                 "hasEmail": "mailto:boiman.tiffany.h@dol.gov"
             },
+            "description": "White House Gender Policy Council Strategy",
+            "identifier": "WB-12-012:038-579",
             "keyword": [
                 "WB"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-01-05T17:22:21.162Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Performance & Impact Evaluations of OTLA projects",
-            "description": "project evaluation reports, synthesized qualitative and quantitative data analysis",
-            "modified": "2021-09-02T13:59:39.531Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-547",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Bureau of International Labor Affairs",
+                "name": "Women's Bureau",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Women's Bureau"
                 }
             },
+            "rights": "not published yet",
+            "title": "White House Gender Policy Council Strategy"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lili Bacon",
                 "hasEmail": "mailto:bacon.lili@dol.gov"
             },
+            "description": "project evaluation reports, synthesized qualitative and quantitative data analysis",
+            "identifier": "ILAB-12-012:037-547",
             "keyword": [
                 "ILAB"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2021-09-02T13:59:39.531Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "OIS  OWCP",
-            "description": "OWCP Imaging System (OIS) is used by DCMWC, and DLHWC programs to capture, store and display digitized images of case documents (correspondence, medical reports, etc.) so that the imaged case records can be retrieved online by appropriate personnel who need to view and/or work with them.  Contains high volume of PII and PHI information that is not in machine-readable form and therefore cannot be easily redacted.",
-            "modified": "2024-12-17T14:51:39.655Z",
-            "accessLevel": "non-public",
-            "identifier": "OWCP-15-012:025-352",
-            "dataQuality": true,
-            "rights": "The dataset contains PII",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Workers\u2019 Compensation Programs",
+                "name": "Bureau of International Labor Affairs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Workers\u2019 Compensation Programs"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Performance & Impact Evaluations of OTLA projects"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rizwan Ahmad",
                 "hasEmail": "mailto:ahmad.rizwan@dol.gov"
             },
+            "dataQuality": true,
+            "description": "OWCP Imaging System (OIS) is used by DCMWC, and DLHWC programs to capture, store and display digitized images of case documents (correspondence, medical reports, etc.) so that the imaged case records can be retrieved online by appropriate personnel who need to view and/or work with them.  Contains high volume of PII and PHI information that is not in machine-readable form and therefore cannot be easily redacted.",
+            "identifier": "OWCP-15-012:025-352",
             "keyword": [
                 "correspondance",
                 "document",
                 "employee medical records",
                 "image"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:51:39.655Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Parking System",
-            "description": "The DOL Parking System is a client-based application that was developed for tracking parking assignments and violations.  This system generates reports based on its own data and it is used as a tool to monitor the parking spaces and occupants.",
-            "modified": "2024-12-09T18:20:14.298Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM EMC-25-012:044-283",
-            "landingPage": "https://monument-ent.com/parking/",
-            "rights": "private",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
+                "name": "Office of Workers\u2019 Compensation Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
+                    "name": "Office of Workers\u2019 Compensation Programs"
                 }
             },
+            "rights": "The dataset contains PII",
+            "title": "OIS  OWCP"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Epps",
                 "hasEmail": "mailto:epps.michael.t@dol.gov"
             },
+            "description": "The DOL Parking System is a client-based application that was developed for tracking parking assignments and violations.  This system generates reports based on its own data and it is used as a tool to monitor the parking spaces and occupants.",
+            "identifier": "OASAM EMC-25-012:044-283",
             "keyword": [
                 "BOC",
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://monument-ent.com/parking/",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-09T18:20:14.298Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "SolarWinds",
-            "description": "Help DOL track and handle outages.",
-            "modified": "2024-09-23T12:57:29.190Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM OCIO-25-012:044-248",
-            "rights": "restricted",
-            "spatial": "location characteristics",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -10946,35 +10925,34 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "title": "Parking System"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Darren Holmnes",
                 "hasEmail": "mailto:holmes.darren.c@dol.gov"
             },
+            "description": "Help DOL track and handle outages.",
+            "identifier": "OASAM OCIO-25-012:044-248",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T12:57:29.190Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Alarm System",
-            "description": "This application automates the process between the building alarm and Notification systems such email, VoIP Phone and GFE laptops. It triggers Notifications to all occupants of the Frances Perkins Building (FPB) by sending Notifications by email, VoIP Phone and GFE laptops screen pop to improve the accuracy and timeliness of the communication amongst FPB occupants in an emergency.",
-            "modified": "2024-09-23T12:54:28.643Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OCIO-25-012:044-255",
-            "rights": "private",
-            "spatial": "location characteristics",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -10983,34 +10961,35 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "restricted",
+            "spatial": "location characteristics",
+            "title": "SolarWinds"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Eric Bryson",
                 "hasEmail": "mailto:bryson.eric.b@dol.gov"
             },
+            "description": "This application automates the process between the building alarm and Notification systems such email, VoIP Phone and GFE laptops. It triggers Notifications to all occupants of the Frances Perkins Building (FPB) by sending Notifications by email, VoIP Phone and GFE laptops screen pop to improve the accuracy and timeliness of the communication amongst FPB occupants in an emergency.",
+            "identifier": "OASAM OCIO-25-012:044-255",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T12:54:28.643Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Audit Web Service (AuditWS)",
-            "description": "no description",
-            "modified": "2022-09-29T16:38:59.485Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OCIO-25-012:044-256",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -11019,113 +10998,110 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "spatial": "location characteristics",
+            "title": "Alarm System"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Richard Green",
                 "hasEmail": "mailto:Green.richard@dol.gov"
             },
+            "description": "no description",
+            "identifier": "OASAM OCIO-25-012:044-256",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-09-29T16:38:59.485Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Clearinghouse for Labor Evaluation and Research (CLEAR)",
-            "description": "none",
-            "modified": "2022-07-19T14:39:17.555Z",
-            "accessLevel": "public",
-            "identifier": "OASAM OCIO-25-012:044-258",
-            "landingPage": "https://clear.dol.gov/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Audit Web Service (AuditWS)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Megan Lizik",
                 "hasEmail": "mailto:lizik.megan@dol.gov"
             },
+            "description": "none",
+            "identifier": "OASAM OCIO-25-012:044-258",
             "keyword": [
                 "evaluation",
                 "research"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://clear.dol.gov/",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-07-19T14:39:17.555Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Entity - Identification",
-            "description": "none",
-            "modified": "2022-09-29T17:29:15.247Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OCIO-25-012:044-259",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Clearinghouse for Labor Evaluation and Research (CLEAR)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Akosua Frimpong-Arhin",
                 "hasEmail": "mailto:Frimpong-Arhin.Akosua@dol.gov"
             },
+            "description": "none",
+            "identifier": "OASAM OCIO-25-012:044-259",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-09-29T17:29:15.247Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Department of Labor Acquisition Management System (DOLAMS)",
-            "description": "The Department's contract writing system that provides the Department's means to acquire goods and services.",
-            "modified": "2024-09-23T13:48:35.193Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM OCIO-25-012:044-681",
-            "rights": "restricted",
-            "spatial": "location characteristics, address",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -11134,12 +11110,26 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Entity - Identification"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Heather Parker",
                 "hasEmail": "mailto:parker.healter@dol.gov"
             },
+            "description": "The Department's contract writing system that provides the Department's means to acquire goods and services.",
+            "identifier": "OASAM OCIO-25-012:044-681",
             "keyword": [
                 "Contracting",
                 "OASAM",
@@ -11147,27 +11137,13 @@
                 "acquisition",
                 "contract"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:48:35.193Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Event Management System",
-            "description": "Event Management System",
-            "modified": "2024-06-27T18:09:16.378Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OCIO-25-012:044-266",
-            "rights": "private",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -11176,34 +11152,38 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "restricted",
+            "spatial": "location characteristics, address",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Department of Labor Acquisition Management System (DOLAMS)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Black",
                 "hasEmail": "mailto:black.michael@dol.gov"
             },
+            "description": "Event Management System",
+            "identifier": "OASAM OCIO-25-012:044-266",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-06-27T18:09:16.378Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Pitney Bowes Mail Metering System (PBMMS)",
-            "description": "none",
-            "modified": "2022-09-29T19:25:39.234Z",
-            "accessLevel": "public",
-            "identifier": "OASAM OCIO-25-012:044-268",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -11212,37 +11192,34 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "title": "Event Management System"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tim McCafferty",
                 "hasEmail": "mailto:mccafferty.tim.p@dol.gov"
             },
+            "description": "none",
+            "identifier": "OASAM OCIO-25-012:044-268",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-09-29T19:25:39.234Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Universal System Management Tool (USMT)",
-            "description": "USMT is an ITIL-compliant workflow system and database for managing incidents, problems, changes, assets, and configurations.  It uses the BMC/Remedy COTS product to support several IT Help Desks, and change management processes for segments of DOL IT infrastructure.",
-            "modified": "2022-09-29T19:32:05.781Z",
-            "accessLevel": "public",
-            "identifier": "OASAM OCIO-25-012:044-269",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -11251,37 +11228,37 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Pitney Bowes Mail Metering System (PBMMS)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Floyd (Eddie) Whetzel",
                 "hasEmail": "mailto:Whetzel.Floyd.E@dol.gov"
             },
+            "description": "USMT is an ITIL-compliant workflow system and database for managing incidents, problems, changes, assets, and configurations.  It uses the BMC/Remedy COTS product to support several IT Help Desks, and change management processes for segments of DOL IT infrastructure.",
+            "identifier": "OASAM OCIO-25-012:044-269",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
-            ],
             "language": [
                 "en-US"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Test System",
-            "description": "none",
-            "modified": "2022-09-29T19:31:06.206Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OCIO-25-012:044-288",
-            "rights": "true",
+            "modified": "2022-09-29T19:32:05.781Z",
+            "programCode": [
+                "015:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -11290,53 +11267,66 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Universal System Management Tool (USMT)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alan Boutureira",
                 "hasEmail": "mailto:boutureira.alan@dol.gov"
             },
+            "description": "none",
+            "identifier": "OASAM OCIO-25-012:044-288",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-09-29T19:31:06.206Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Closing the Child Labor and Forced Labor Evidence Gap Impact Evaluations - American University - India",
-            "description": "Randomized controlled trial impact evaluations examining the effects on child labor of a Room to Read-implemented intervention in Rajasthan, India",
-            "modified": "2022-08-05T21:30:31.517Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-604",
-            "dataQuality": true,
-            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "describedByType": "text/html",
-            "issued": "2021-12-31",
-            "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Bureau of International Labor Affairs",
+                "name": "Office of the Assistant Secretary for Administration and Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Bureau of International Labor Affairs"
+                    "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "true",
+            "title": "Test System"
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
                 "fn": "Evan Burke",
                 "hasEmail": "mailto:burke.evan.t@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "describedByType": "text/html",
+            "description": "Randomized controlled trial impact evaluations examining the effects on child labor of a Room to Read-implemented intervention in Rajasthan, India",
+            "identifier": "ILAB-12-012:037-604",
+            "issued": "2021-12-31",
             "keyword": [
                 "ILAB",
                 "Impact evaluation",
@@ -11349,29 +11339,14 @@
                 "Room-to-Read",
                 "randomized control trials"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-08-05T21:30:31.517Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Closing the Child Labor and Forced Labor Evidence Gap - Impact Evaluations - IMPAQ - Malawi",
-            "description": "Randomized controlled trial impact evaluations examining interventions on combating child labor in Malawi.",
-            "modified": "2022-08-05T21:49:48.792Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-600",
-            "dataQuality": true,
-            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "describedByType": "application/pdf",
-            "issued": "2021-12-31",
-            "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of International Labor Affairs",
@@ -11380,18 +11355,33 @@
                     "name": "Bureau of International Labor Affairs"
                 }
             },
+            "rights": "true",
+            "title": "Closing the Child Labor and Forced Labor Evidence Gap Impact Evaluations - American University - India"
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
                 "fn": "Evan Burke",
                 "hasEmail": "mailto:burke.evan.t@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "describedByType": "application/pdf",
+            "description": "Randomized controlled trial impact evaluations examining interventions on combating child labor in Malawi.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations"
                 }
             ],
+            "identifier": "ILAB-12-012:037-600",
+            "issued": "2021-12-31",
             "keyword": [
                 "ILAB",
                 "Impact evaluation",
@@ -11399,29 +11389,14 @@
                 "Malawi",
                 "randomized control trials"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-08-05T21:49:48.792Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Closing the Child Labor and Forced Labor Evidence Gap - Impact Evaluations - IMPAQ - Costa Rica",
-            "description": "Randomized controlled trial impact evaluations examining interventions on combating child labor in Costa Rica.",
-            "modified": "2022-08-05T21:53:21.271Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-601",
-            "dataQuality": true,
-            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "describedByType": "application/pdf",
-            "issued": "0201-12-31",
-            "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of International Labor Affairs",
@@ -11430,18 +11405,33 @@
                     "name": "Bureau of International Labor Affairs"
                 }
             },
+            "rights": "true",
+            "title": "Closing the Child Labor and Forced Labor Evidence Gap - Impact Evaluations - IMPAQ - Malawi"
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
                 "fn": "Evan Burke",
                 "hasEmail": "mailto:burke.evan.t@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "describedByType": "application/pdf",
+            "description": "Randomized controlled trial impact evaluations examining interventions on combating child labor in Costa Rica.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations"
                 }
             ],
+            "identifier": "ILAB-12-012:037-601",
+            "issued": "0201-12-31",
             "keyword": [
                 "Costa Rica",
                 "ILAB",
@@ -11449,29 +11439,14 @@
                 "International Child Labor",
                 "randomized control trials"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-08-05T21:53:21.271Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Closing the Child Labor and Forced Labor Evidence Gap - Impact Evaluations - IMPAQ - Rwanda",
-            "description": "Randomized controlled trial impact evaluations examining interventions on combating child labor in Rwanda.",
-            "modified": "2022-08-05T21:54:28.337Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-602",
-            "dataQuality": true,
-            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "describedByType": "application/pdf",
-            "issued": "2021-12-31",
-            "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of International Labor Affairs",
@@ -11480,18 +11455,33 @@
                     "name": "Bureau of International Labor Affairs"
                 }
             },
+            "rights": "true",
+            "title": "Closing the Child Labor and Forced Labor Evidence Gap - Impact Evaluations - IMPAQ - Costa Rica"
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
                 "fn": "Evan Burke",
                 "hasEmail": "mailto:burke.evan.t@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "describedByType": "application/pdf",
+            "description": "Randomized controlled trial impact evaluations examining interventions on combating child labor in Rwanda.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations"
                 }
             ],
+            "identifier": "ILAB-12-012:037-602",
+            "issued": "2021-12-31",
             "keyword": [
                 "ILAB",
                 "Impact evaluation",
@@ -11499,29 +11489,14 @@
                 "Rwanda",
                 "randomized control trials"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-08-05T21:54:28.337Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Closing the Child Labor and Forced Labor Evidence Gap - Impact Evaluations - IMPAQ - Ecuador",
-            "description": "Randomized controlled trial impact evaluations examining interventions on combating child labor in Ecuador.",
-            "modified": "2022-08-05T21:56:58.526Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-603",
-            "dataQuality": true,
-            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "describedByType": "application/pdf",
-            "issued": "0021-12-31",
-            "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of International Labor Affairs",
@@ -11530,18 +11505,33 @@
                     "name": "Bureau of International Labor Affairs"
                 }
             },
+            "rights": "true",
+            "title": "Closing the Child Labor and Forced Labor Evidence Gap - Impact Evaluations - IMPAQ - Rwanda"
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
                 "fn": "Evan Burke",
                 "hasEmail": "mailto:etburke86@gmail.com"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "describedByType": "application/pdf",
+            "description": "Randomized controlled trial impact evaluations examining interventions on combating child labor in Ecuador.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations"
                 }
             ],
+            "identifier": "ILAB-12-012:037-603",
+            "issued": "0021-12-31",
             "keyword": [
                 "Ecuador",
                 "ILAB",
@@ -11549,29 +11539,14 @@
                 "International Child Labor",
                 "randomized control trials"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-08-05T21:56:58.526Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Closing the Child Labor and Forced Labor Evidence Gap - Impact Evaluations - IPA - Peru",
-            "description": "Randomized control trial impact evaluations examining the effects of an information campaign on child labor in Peru.",
-            "modified": "2022-08-05T21:57:44.356Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-605",
-            "dataQuality": true,
-            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "describedByType": "application/pdf",
-            "issued": "2021-12-31",
-            "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of International Labor Affairs",
@@ -11580,53 +11555,50 @@
                     "name": "Bureau of International Labor Affairs"
                 }
             },
+            "rights": "true",
+            "title": "Closing the Child Labor and Forced Labor Evidence Gap - Impact Evaluations - IMPAQ - Ecuador"
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
                 "fn": "Evan Burke",
                 "hasEmail": "mailto:burke.evan.t@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "describedByType": "application/pdf",
+            "description": "Randomized control trial impact evaluations examining the effects of an information campaign on child labor in Peru.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations"
                 }
             ],
-            "keyword": [
-                "ILAB",
-                "Impact evaluation",
-                "International Child Labor",
-                "Peru",
-                "information campaign",
-                "public awareness",
-                "randomized control trials"
-            ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
-            ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Closing the Child Labor and Forced Labor Evidence Gap - Impact Evaluations - Notre Dame - Nepal & China",
-            "description": "Randomized controlled trial impact evaluations examining the effects of mass media campaigns on norms and behaviors related to vulnerability to forced labor and the worst forms of child labor in Nepal and China.",
-            "modified": "2022-08-05T22:01:00.857Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-606",
-            "dataQuality": true,
-            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "describedByType": "application/pdf",
+            "identifier": "ILAB-12-012:037-605",
             "issued": "2021-12-31",
+            "keyword": [
+                "ILAB",
+                "Impact evaluation",
+                "International Child Labor",
+                "Peru",
+                "information campaign",
+                "public awareness",
+                "randomized control trials"
+            ],
             "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "rights": "true",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-08-05T21:57:44.356Z",
+            "programCode": [
+                "015:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of International Labor Affairs",
@@ -11635,18 +11607,36 @@
                     "name": "Bureau of International Labor Affairs"
                 }
             },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Closing the Child Labor and Forced Labor Evidence Gap - Impact Evaluations - IPA - Peru"
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
                 "fn": "Evan Burke",
                 "hasEmail": "mailto:burke.evan.t@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "describedByType": "application/pdf",
+            "description": "Randomized controlled trial impact evaluations examining the effects of mass media campaigns on norms and behaviors related to vulnerability to forced labor and the worst forms of child labor in Nepal and China.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations"
                 }
             ],
+            "identifier": "ILAB-12-012:037-606",
+            "issued": "2021-12-31",
             "keyword": [
                 "China",
                 "ILAB",
@@ -11657,29 +11647,14 @@
                 "public awareness",
                 "randomized control trials"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-08-05T22:01:00.857Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Closing the Child Labor and Forced Labor Evidence Gap - IE -Berkeley-General Public-Nepal",
-            "description": "Randomized controlled trial impact evaluations examining the effects of mass media campaigns on norms and behaviors related to vulnerability to forced labor and the worst forms of child labor in Nepal and China.",
-            "modified": "2022-08-05T22:00:03.377Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-607",
-            "dataQuality": true,
-            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "describedByType": "application/pdf",
-            "issued": "2021-12-31",
-            "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of International Labor Affairs",
@@ -11688,18 +11663,33 @@
                     "name": "Bureau of International Labor Affairs"
                 }
             },
+            "rights": "true",
+            "title": "Closing the Child Labor and Forced Labor Evidence Gap - Impact Evaluations - Notre Dame - Nepal & China"
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
                 "fn": "Evan Burke",
                 "hasEmail": "mailto:burke.evan.t@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "describedByType": "application/pdf",
+            "description": "Randomized controlled trial impact evaluations examining the effects of mass media campaigns on norms and behaviors related to vulnerability to forced labor and the worst forms of child labor in Nepal and China.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations"
                 }
             ],
+            "identifier": "ILAB-12-012:037-607",
+            "issued": "2021-12-31",
             "keyword": [
                 "ILAB",
                 "Impact evaluation",
@@ -11709,29 +11699,14 @@
                 "public awareness",
                 "randomized control trials"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-08-05T22:00:03.377Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Closing the Child Labor and Forced Labor Evidence Gap - IE -Berkeley-Law Enforcement-Nepal",
-            "description": "Randomized controlled trial impact evaluations examining the effects of mass media campaigns on norms and behaviors related to vulnerability to forced labor and the worst forms of child labor in Nepal and China.",
-            "modified": "2022-08-05T21:59:26.718Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-608",
-            "dataQuality": true,
-            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "describedByType": "application/pdf",
-            "issued": "2021-12-31",
-            "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of International Labor Affairs",
@@ -11740,18 +11715,33 @@
                     "name": "Bureau of International Labor Affairs"
                 }
             },
+            "rights": "true",
+            "title": "Closing the Child Labor and Forced Labor Evidence Gap - IE -Berkeley-General Public-Nepal"
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
                 "fn": "Evan Burke",
                 "hasEmail": "mailto:burke.evan.t@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "describedByType": "application/pdf",
+            "description": "Randomized controlled trial impact evaluations examining the effects of mass media campaigns on norms and behaviors related to vulnerability to forced labor and the worst forms of child labor in Nepal and China.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations"
                 }
             ],
+            "identifier": "ILAB-12-012:037-608",
+            "issued": "2021-12-31",
             "keyword": [
                 "ILAB",
                 "Impact evaluation",
@@ -11761,28 +11751,14 @@
                 "public awareness",
                 "randomized control trials"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-08-05T21:59:26.718Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Closing the Child Labor and Forced Labor Evidence Gap - Impact Evaluations - IPA - Philippines",
-            "description": "Randomized controlled trial (RCT) impact evaluations examining the effects of the Government of the Philippines KASAMA program on child labor.",
-            "modified": "2022-08-05T22:03:24.577Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-609",
-            "dataQuality": true,
-            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "describedByType": "application/pdf",
-            "issued": "2021-12-31",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of International Labor Affairs",
@@ -11791,18 +11767,33 @@
                     "name": "Bureau of International Labor Affairs"
                 }
             },
+            "rights": "true",
+            "title": "Closing the Child Labor and Forced Labor Evidence Gap - IE -Berkeley-Law Enforcement-Nepal"
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
                 "fn": "Evan Burke",
                 "hasEmail": "mailto:burke.evan.t@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "describedByType": "application/pdf",
+            "description": "Randomized controlled trial (RCT) impact evaluations examining the effects of the Government of the Philippines KASAMA program on child labor.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations"
                 }
             ],
+            "identifier": "ILAB-12-012:037-609",
+            "issued": "2021-12-31",
             "keyword": [
                 "ILAB",
                 "Impact evaluation",
@@ -11811,29 +11802,13 @@
                 "philippines",
                 "randomized control trials"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-08-05T22:03:24.577Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Closing the Child Labor and Forced Labor Evidence Gap - IE - Berkeley - Migrant Domestic Worker - Hong Kong",
-            "description": "Randomized controlled trial impact evaluations examining  migrant domestic work in Hong Kong.",
-            "modified": "2022-08-05T22:04:54.170Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-610",
-            "dataQuality": true,
-            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "describedByType": "application/pdf",
-            "issued": "2021-12-31",
-            "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of International Labor Affairs",
@@ -11842,18 +11817,33 @@
                     "name": "Bureau of International Labor Affairs"
                 }
             },
+            "rights": "true",
+            "title": "Closing the Child Labor and Forced Labor Evidence Gap - Impact Evaluations - IPA - Philippines"
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
                 "fn": "Evan Burke",
                 "hasEmail": "mailto:burke.evan.t@dol.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "describedByType": "application/pdf",
+            "description": "Randomized controlled trial impact evaluations examining  migrant domestic work in Hong Kong.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations"
                 }
             ],
+            "identifier": "ILAB-12-012:037-610",
+            "issued": "2021-12-31",
             "keyword": [
                 "China",
                 "ILAB",
@@ -11863,137 +11853,124 @@
                 "public awareness",
                 "randomized control trials"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/ilab/our-work/impact-evaluations",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-08-05T22:04:54.170Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Global Economic Briefing",
-            "description": "Highlight released data on G20 economies, GDP growth, Labor force participation, unemployment rate, and trade",
-            "modified": "2022-08-05T21:37:16.134Z",
-            "accessLevel": "public",
-            "identifier": "ILAB-12-012:037-598",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of International Labor Affairs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Bureau of International Labor Affairs"
                 }
             },
+            "rights": "true",
+            "title": "Closing the Child Labor and Forced Labor Evidence Gap - IE - Berkeley - Migrant Domestic Worker - Hong Kong"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Evan Burke",
                 "hasEmail": "mailto:burke.evan.t@dol.gov"
             },
+            "description": "Highlight released data on G20 economies, GDP growth, Labor force participation, unemployment rate, and trade",
+            "identifier": "ILAB-12-012:037-598",
             "keyword": [
                 "ILAB"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-08-05T21:37:16.134Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "cpsbasic_finaldata",
-            "description": "Survey data files: Current Population Survey Basic Monthly data aggregated from January 2005 till August 2014 from the Early Effects of the 2010 Affordable Care Act on Labor Market Outcomes project",
-            "modified": "2022-10-03T14:07:53.709Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-612",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2015-01-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Assistant Secretary for Policy",
+                "name": "Bureau of International Labor Affairs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Assistant Secretary for Policy"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Global Economic Briefing"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Survey data files: Current Population Survey Basic Monthly data aggregated from January 2005 till August 2014 from the Early Effects of the 2010 Affordable Care Act on Labor Market Outcomes project",
+            "identifier": "OASP-12-012:044-612",
+            "issued": "2015-01-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T14:07:53.709Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "PUBLIC_USE_DATA_FILE_workers_rights_access_assertion_knowledge_study",
-            "description": "Survey data from the project to develop a measure of WRAAK and to pilot test methods for collecting data on WRAAK from miners",
-            "modified": "2022-10-03T14:16:11.715Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-613",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2013-11-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Office of Assistant Secretary for Policy"
                 }
             },
+            "rights": "true",
+            "title": "cpsbasic_finaldata"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Survey data from the project to develop a measure of WRAAK and to pilot test methods for collecting data on WRAAK from miners",
+            "identifier": "OASP-12-012:044-613",
+            "issued": "2013-11-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T14:16:11.715Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "PUBLIC_DATA_USE_FILE_employee",
-            "description": "Survey data files: Employee and Worksite Surveys",
-            "modified": "2022-10-03T14:19:37.485Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-614",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2012-09-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12002,36 +11979,36 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "PUBLIC_USE_DATA_FILE_workers_rights_access_assertion_knowledge_study"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Survey data files: Employee and Worksite Surveys",
+            "identifier": "OASP-12-012:044-614",
+            "issued": "2012-09-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T14:19:37.485Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "PUBLIC_DATA_USE_FILE_worksite",
-            "description": "Survey data files: Employee and Worksite Surveys",
-            "modified": "2022-10-03T14:21:50.893Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-615",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2012-09-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12040,36 +12017,36 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "PUBLIC_DATA_USE_FILE_employee"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Survey data files: Employee and Worksite Surveys",
+            "identifier": "OASP-12-012:044-615",
+            "issued": "2012-09-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T14:21:50.893Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FMLAMICH",
-            "description": "Survey data files from the 1995 employee and worksite FMLA survey.",
-            "modified": "2022-10-03T15:11:30.240Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-616",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2013-11-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12078,36 +12055,36 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "PUBLIC_DATA_USE_FILE_worksite"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Survey data files from the 1995 employee and worksite FMLA survey.",
+            "identifier": "OASP-12-012:044-616",
+            "issued": "2013-11-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T15:11:30.240Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Michform",
-            "description": "Survey data files from the 1995 employee and worksite FMLA survey.",
-            "modified": "2022-10-03T15:13:14.829Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-617",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2013-11-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12116,36 +12093,36 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "FMLAMICH"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Survey data files from the 1995 employee and worksite FMLA survey.",
+            "identifier": "OASP-12-012:044-617",
+            "issued": "2013-11-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T15:13:14.829Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Roster",
-            "description": "Survey data files from the 1995 employee and worksite FMLA survey.",
-            "modified": "2022-10-03T15:14:36.295Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-618",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2013-11-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12154,36 +12131,36 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Michform"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Survey data files from the 1995 employee and worksite FMLA survey.",
+            "identifier": "OASP-12-012:044-618",
+            "issued": "2013-11-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T15:14:36.295Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Westpub",
-            "description": "Survey data files from the 1995 employee and worksite FMLA survey.",
-            "modified": "2022-10-03T15:16:09.881Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-619",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2013-11-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12192,36 +12169,36 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Roster"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Survey data files from the 1995 employee and worksite FMLA survey.",
+            "identifier": "OASP-12-012:044-619",
+            "issued": "2013-11-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T15:16:09.881Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FMLA_EMP",
-            "description": "Survey data files from the 2000 employee and worksite FMLA surveys.",
-            "modified": "2022-10-03T15:17:43.608Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-620",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2013-11-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12230,36 +12207,36 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Westpub"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Survey data files from the 2000 employee and worksite FMLA surveys.",
+            "identifier": "OASP-12-012:044-620",
+            "issued": "2013-11-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T15:17:43.608Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FMLA_EST",
-            "description": "Survey data files from the 2000 employee and worksite FMLA surveys.",
-            "modified": "2022-10-03T15:19:07.542Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-621",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2013-11-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12268,36 +12245,36 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "FMLA_EMP"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Survey data files from the 2000 employee and worksite FMLA surveys.",
+            "identifier": "OASP-12-012:044-621",
+            "issued": "2013-11-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T15:19:07.542Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FMLA_2018_Worksite_PUF",
-            "description": "Survey data files from the 2018 employee and worksite FMLA surveys",
-            "modified": "2022-10-03T15:21:08.873Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-622",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2018-01-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12306,36 +12283,36 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "FMLA_EST"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Survey data files from the 2018 employee and worksite FMLA surveys",
+            "identifier": "OASP-12-012:044-622",
+            "issued": "2018-01-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T15:21:08.873Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FMLA_2018_Employee_PUF",
-            "description": "Survey data files from the 2018 employee and worksite FMLA surveys",
-            "modified": "2022-10-03T15:22:15.433Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-623",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2018-01-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12344,36 +12321,36 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "FMLA_2018_Worksite_PUF"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Survey data files from the 2018 employee and worksite FMLA surveys",
+            "identifier": "OASP-12-012:044-623",
+            "issued": "2018-01-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T15:22:15.433Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "cp_meta_publicdataset",
-            "description": "Data used for the Meta-Analysis of 46 Career Pathways Impact and data from four large nationally representative longitudinal surveys, as well as licensed data on occupational transitions from online career profiles, to examine workers\u2019 career paths and wages for the Career Trajectories and Occupational Transitions Study.",
-            "modified": "2022-10-03T15:23:49.866Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-624",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2022-01-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12382,36 +12359,36 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "FMLA_2018_Employee_PUF"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Data used for the Meta-Analysis of 46 Career Pathways Impact and data from four large nationally representative longitudinal surveys, as well as licensed data on occupational transitions from online career profiles, to examine workers\u2019 career paths and wages for the Career Trajectories and Occupational Transitions Study.",
+            "identifier": "OASP-12-012:044-624",
+            "issued": "2022-01-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T15:23:49.866Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Emsi dataset",
-            "description": "Data used for the Meta-Analysis of 46 Career Pathways Impact and data from four large nationally representative longitudinal surveys, as well as licensed data on occupational transitions from online career profiles, to examine workers\u2019 career paths and wages for the Career Trajectories and Occupational Transitions Study.",
-            "modified": "2022-10-03T15:25:10.414Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-625",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2022-01-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12420,35 +12397,36 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "cp_meta_publicdataset"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Data used for the Meta-Analysis of 46 Career Pathways Impact and data from four large nationally representative longitudinal surveys, as well as licensed data on occupational transitions from online career profiles, to examine workers\u2019 career paths and wages for the Career Trajectories and Occupational Transitions Study.",
+            "identifier": "OASP-12-012:044-625",
+            "issued": "2022-01-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T15:25:10.414Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Dashboard transitions dataset",
-            "description": "Data used for the Meta-Analysis of 46 Career Pathways Impact and data from four large nationally representative longitudinal surveys, as well as licensed data on occupational transitions from online career profiles, to examine workers\u2019 career paths and wages for the Career Trajectories and Occupational Transitions Study.",
-            "modified": "2022-10-03T15:26:17.906Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-626",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12457,36 +12435,35 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Emsi dataset"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Data used for the Meta-Analysis of 46 Career Pathways Impact and data from four large nationally representative longitudinal surveys, as well as licensed data on occupational transitions from online career profiles, to examine workers\u2019 career paths and wages for the Career Trajectories and Occupational Transitions Study.",
+            "identifier": "OASP-12-012:044-626",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T15:26:17.906Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "CPS-SIPP dataset",
-            "description": "Data used for the Meta-Analysis of 46 Career Pathways Impact and data from four large nationally representative longitudinal surveys, as well as licensed data on occupational transitions from online career profiles, to examine workers\u2019 career paths and wages for the Career Trajectories and Occupational Transitions Study.",
-            "modified": "2022-10-03T15:27:52.487Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-627",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2022-01-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12495,36 +12472,36 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Dashboard transitions dataset"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Data used for the Meta-Analysis of 46 Career Pathways Impact and data from four large nationally representative longitudinal surveys, as well as licensed data on occupational transitions from online career profiles, to examine workers\u2019 career paths and wages for the Career Trajectories and Occupational Transitions Study.",
+            "identifier": "OASP-12-012:044-627",
+            "issued": "2022-01-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T15:27:52.487Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Dashboard trajectories dataset",
-            "description": "Data used for the Meta-Analysis of 46 Career Pathways Impact and data from four large nationally representative longitudinal surveys, as well as licensed data on occupational transitions from online career profiles, to examine workers\u2019 career paths and wages for the Career Trajectories and Occupational Transitions Study.",
-            "modified": "2022-10-03T15:29:18.439Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-628",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2022-01-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12533,112 +12510,112 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "CPS-SIPP dataset"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Data used for the Meta-Analysis of 46 Career Pathways Impact and data from four large nationally representative longitudinal surveys, as well as licensed data on occupational transitions from online career profiles, to examine workers\u2019 career paths and wages for the Career Trajectories and Occupational Transitions Study.",
+            "identifier": "OASP-12-012:044-628",
+            "issued": "2022-01-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T15:29:18.439Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Dashboard cluster dataset",
-            "description": "Data used for the Meta-Analysis of 46 Career Pathways Impact and data from four large nationally representative longitudinal surveys, as well as licensed data on occupational transitions from online career profiles, to examine workers\u2019 career paths and wages for the Career Trajectories and Occupational Transitions Study.",
-            "modified": "2022-10-03T15:31:08.438Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-629",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2022-01-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Assistant Secretary for Policy"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Dashboard trajectories dataset"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Data used for the Meta-Analysis of 46 Career Pathways Impact and data from four large nationally representative longitudinal surveys, as well as licensed data on occupational transitions from online career profiles, to examine workers\u2019 career paths and wages for the Career Trajectories and Occupational Transitions Study.",
+            "identifier": "OASP-12-012:044-629",
+            "issued": "2022-01-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T15:31:08.438Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Trajectories (10 years) dataset",
-            "description": "Data used for the Meta-Analysis of 46 Career Pathways Impact and data from four large nationally representative longitudinal surveys, as well as licensed data on occupational transitions from online career profiles, to examine workers\u2019 career paths and wages for the Career Trajectories and Occupational Transitions Study.",
-            "modified": "2022-10-03T15:32:18.589Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-630",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2022-01-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Office of Assistant Secretary for Policy"
                 }
             },
+            "rights": "true",
+            "title": "Dashboard cluster dataset"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Data used for the Meta-Analysis of 46 Career Pathways Impact and data from four large nationally representative longitudinal surveys, as well as licensed data on occupational transitions from online career profiles, to examine workers\u2019 career paths and wages for the Career Trajectories and Occupational Transitions Study.",
+            "identifier": "OASP-12-012:044-630",
+            "issued": "2022-01-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T15:32:18.589Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Trajectories (5 years) dataset",
-            "description": "Data used for the Meta-Analysis of 46 Career Pathways Impact and data from four large nationally representative longitudinal surveys, as well as licensed data on occupational transitions from online career profiles, to examine workers\u2019 career paths and wages for the Career Trajectories and Occupational Transitions Study.",
-            "modified": "2022-10-03T15:33:59.317Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-631",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2022-01-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12647,36 +12624,36 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Trajectories (10 years) dataset"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Data used for the Meta-Analysis of 46 Career Pathways Impact and data from four large nationally representative longitudinal surveys, as well as licensed data on occupational transitions from online career profiles, to examine workers\u2019 career paths and wages for the Career Trajectories and Occupational Transitions Study.",
+            "identifier": "OASP-12-012:044-631",
+            "issued": "2022-01-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T15:33:59.317Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Trajectories (3 years) dataset",
-            "description": "Data used for the Meta-Analysis of 46 Career Pathways Impact and data from four large nationally representative longitudinal surveys, as well as licensed data on occupational transitions from online career profiles, to examine workers\u2019 career paths and wages for the Career Trajectories and Occupational Transitions Study.",
-            "modified": "2022-10-03T18:54:13.757Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-632",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2022-01-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12685,74 +12662,74 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Trajectories (5 years) dataset"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Data used for the Meta-Analysis of 46 Career Pathways Impact and data from four large nationally representative longitudinal surveys, as well as licensed data on occupational transitions from online career profiles, to examine workers\u2019 career paths and wages for the Career Trajectories and Occupational Transitions Study.",
+            "identifier": "OASP-12-012:044-632",
+            "issued": "2022-01-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T18:54:13.757Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "cobrasubsidysurvey",
-            "description": "Survey data files: COBRA Subsidy Survey",
-            "modified": "2022-10-03T18:58:53.591Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-633",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2015-04-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Assistant Secretary for Policy"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Trajectories (3 years) dataset"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Survey data files: COBRA Subsidy Survey",
+            "identifier": "OASP-12-012:044-633",
+            "issued": "2015-04-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T18:58:53.591Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "pud",
-            "description": "Administrative data: 1986\u201387 Washington Alternative Work Search experiment (merged with nine years of follow-up administrative wage records)",
-            "modified": "2022-10-03T18:57:59.876Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-634",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2015-01-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12761,74 +12738,74 @@
                     "name": "Office of Assistant Secretary for Policy"
                 }
             },
+            "rights": "true",
+            "title": "cobrasubsidysurvey"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Administrative data: 1986\u201387 Washington Alternative Work Search experiment (merged with nine years of follow-up administrative wage records)",
+            "identifier": "OASP-12-012:044-634",
+            "issued": "2015-01-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T18:57:59.876Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "nlrb_elections_19622009",
-            "description": "Administrative data: OSHA enforcement data and NLRB election records",
-            "modified": "2022-10-03T19:01:18.826Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-635",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2015-01-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Office of Assistant Secretary for Policy"
                 }
             },
+            "rights": "true",
+            "title": "pud"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Administrative data: OSHA enforcement data and NLRB election records",
+            "identifier": "OASP-12-012:044-635",
+            "issued": "2015-01-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T19:01:18.826Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "PUBLIC_DATA_USE_FILE_using_administrative_data_address_federal_contractor_Violations_equal_employmen",
-            "description": "Administrative data file: Office of Federal Contract Compliance Programs (OFCCP) Information System (OFIS) records for reviews closed during FY2003 through FY 2012.",
-            "modified": "2022-10-03T19:06:17.211Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-636",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2013-07-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -12837,179 +12814,182 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "nlrb_elections_19622009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Administrative data file: Office of Federal Contract Compliance Programs (OFCCP) Information System (OFIS) records for reviews closed during FY2003 through FY 2012.",
+            "identifier": "OASP-12-012:044-636",
+            "issued": "2013-07-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T19:06:17.211Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "DATA_1_YEAR_addressing_return_to_work_issues",
-            "description": "Administrative data: Outcomes for FECA Cases after 1 year (January 2005 - December 2010) and 3 years (January 2005 - December 2008).",
-            "modified": "2022-10-03T19:08:49.954Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-637",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2013-04-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Assistant Secretary for Policy"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "PUBLIC_DATA_USE_FILE_using_administrative_data_address_federal_contractor_Violations_equal_employmen"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Administrative data: Outcomes for FECA Cases after 1 year (January 2005 - December 2010) and 3 years (January 2005 - December 2008).",
+            "identifier": "OASP-12-012:044-637",
+            "issued": "2013-04-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T19:08:49.954Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "DATA_3_YEAR_addressing_return_to_work_issues",
-            "description": "Administrative data: Outcomes for FECA Cases after 1 year (January 2005 - December 2010) and 3 years (January 2005 - December 2008).",
-            "modified": "2022-10-03T19:10:04.472Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-638",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2013-04-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Office of Assistant Secretary for Policy"
                 }
             },
+            "rights": "true",
+            "title": "DATA_1_YEAR_addressing_return_to_work_issues"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Administrative data: Outcomes for FECA Cases after 1 year (January 2005 - December 2010) and 3 years (January 2005 - December 2008).",
+            "identifier": "OASP-12-012:044-638",
+            "issued": "2013-04-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T19:10:04.472Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "adra2_es_pudf",
-            "description": "Data collected and used for the Administrative Data Research and Analysis (ADRA2) study focused on customers enrolled in four programs that are part of the national workforce investment system: the Employment Service (ES) and three Workforce Investment Act (WIA) programs\u2014the Adult Program, the National Farmworker Jobs Program (NFJP), and the Indian and Native American Program (INAP). The study produced four public use data files, each of which contains individual-level information on customers who left one of the four workforce investment programs in calendar year 2011.",
-            "modified": "2022-10-03T19:18:35.524Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-639",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Assistant Secretary for Policy"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "DATA_3_YEAR_addressing_return_to_work_issues"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "Data collected and used for the Administrative Data Research and Analysis (ADRA2) study focused on customers enrolled in four programs that are part of the national workforce investment system: the Employment Service (ES) and three Workforce Investment Act (WIA) programs\u2014the Adult Program, the National Farmworker Jobs Program (NFJP), and the Indian and Native American Program (INAP). The study produced four public use data files, each of which contains individual-level information on customers who left one of the four workforce investment programs in calendar year 2011.",
+            "identifier": "OASP-12-012:044-639",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-03T19:18:35.524Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "adra2_wiaadult_pudf",
-            "description": "Data collected and used for the Administrative Data Research and Analysis (ADRA2) study focused on customers enrolled in four programs that are part of the national workforce investment system: the Employment Service (ES) and three Workforce Investment Act (WIA) programs\u2014the Adult Program, the National Farmworker Jobs Program (NFJP), and the Indian and Native American Program (INAP). The study produced four public use data files, each of which contains individual-level information on customers who left one of the four workforce investment programs in calendar year 2011.",
-            "modified": "2022-10-04T18:18:49.733Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-640",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Office of Assistant Secretary for Policy"
                 }
             },
+            "rights": "true",
+            "title": "adra2_es_pudf"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "Data collected and used for the Administrative Data Research and Analysis (ADRA2) study focused on customers enrolled in four programs that are part of the national workforce investment system: the Employment Service (ES) and three Workforce Investment Act (WIA) programs\u2014the Adult Program, the National Farmworker Jobs Program (NFJP), and the Indian and Native American Program (INAP). The study produced four public use data files, each of which contains individual-level information on customers who left one of the four workforce investment programs in calendar year 2011.",
+            "identifier": "OASP-12-012:044-640",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T18:18:49.733Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "adra2_nfjp_pudf",
-            "description": "Data collected and used for the Administrative Data Research and Analysis (ADRA2) study focused on customers enrolled in four programs that are part of the national workforce investment system: the Employment Service (ES) and three Workforce Investment Act (WIA) programs\u2014the Adult Program, the National Farmworker Jobs Program (NFJP), and the Indian and Native American Program (INAP). The study produced four public use data files, each of which contains individual-level information on customers who left one of the four workforce investment programs in calendar year 2011.",
-            "modified": "2022-10-04T18:19:47.203Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-641",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13018,33 +12998,33 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "adra2_wiaadult_pudf"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "Data collected and used for the Administrative Data Research and Analysis (ADRA2) study focused on customers enrolled in four programs that are part of the national workforce investment system: the Employment Service (ES) and three Workforce Investment Act (WIA) programs\u2014the Adult Program, the National Farmworker Jobs Program (NFJP), and the Indian and Native American Program (INAP). The study produced four public use data files, each of which contains individual-level information on customers who left one of the four workforce investment programs in calendar year 2011.",
+            "identifier": "OASP-12-012:044-641",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T18:19:47.203Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "adra2_inap_pudf",
-            "description": "Data collected and used for the Administrative Data Research and Analysis (ADRA2) study focused on customers enrolled in four programs that are part of the national workforce investment system: the Employment Service (ES) and three Workforce Investment Act (WIA) programs\u2014the Adult Program, the National Farmworker Jobs Program (NFJP), and the Indian and Native American Program (INAP). The study produced four public use data files, each of which contains individual-level information on customers who left one of the four workforce investment programs in calendar year 2011.",
-            "modified": "2022-10-04T18:21:44.085Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-642",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13053,36 +13033,33 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "adra2_nfjp_pudf"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "Data collected and used for the Administrative Data Research and Analysis (ADRA2) study focused on customers enrolled in four programs that are part of the national workforce investment system: the Employment Service (ES) and three Workforce Investment Act (WIA) programs\u2014the Adult Program, the National Farmworker Jobs Program (NFJP), and the Indian and Native American Program (INAP). The study produced four public use data files, each of which contains individual-level information on customers who left one of the four workforce investment programs in calendar year 2011.",
+            "identifier": "OASP-12-012:044-642",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T18:21:44.085Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Full Day K and Employment Data",
-            "description": "These data files contain data from assessing the Impact of Full-day Kindergarten on Maternal Employment and Achievement.",
-            "modified": "2022-10-04T18:26:42.008Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-643",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2016-01-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13091,36 +13068,36 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "adra2_inap_pudf"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "These data files contain data from assessing the Impact of Full-day Kindergarten on Maternal Employment and Achievement.",
+            "identifier": "OASP-12-012:044-643",
+            "issued": "2016-01-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T18:26:42.008Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Full Day K and Achievement Data",
-            "description": "These data files contain data from assessing the Impact of Full-day Kindergarten on Maternal Employment and Achievement.",
-            "modified": "2022-10-04T18:28:01.333Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-644",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2016-01-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13129,112 +13106,112 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Full Day K and Employment Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "These data files contain data from assessing the Impact of Full-day Kindergarten on Maternal Employment and Achievement.",
+            "identifier": "OASP-12-012:044-644",
+            "issued": "2016-01-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T18:28:01.333Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "adra_wiasrd_exits2007_with_acs",
-            "description": "Results from the study are summarized in Maxwell et al. (2012) and were based on data collected from five public sources: WIA Standardized Records Data (WIASRD) public-use files, American Community Survey (ACS) summary data, 2000 U.S. Census data, A Census-to-LWIA geographic crosswalk, and A set of annual LWIA geographic definition files",
-            "modified": "2022-10-04T18:34:53.225Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-645",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2012-12-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Assistant Secretary for Policy"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Full Day K and Achievement Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Results from the study are summarized in Maxwell et al. (2012) and were based on data collected from five public sources: WIA Standardized Records Data (WIASRD) public-use files, American Community Survey (ACS) summary data, 2000 U.S. Census data, A Census-to-LWIA geographic crosswalk, and A set of annual LWIA geographic definition files",
+            "identifier": "OASP-12-012:044-645",
+            "issued": "2012-12-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T18:34:53.225Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "adra_wiasrd_exits2009_with_acs",
-            "description": "Results from the study are summarized in Maxwell et al. (2012) and were based on data collected from five public sources: WIA Standardized Records Data (WIASRD) public-use files, American Community Survey (ACS) summary data, 2000 U.S. Census data, A Census-to-LWIA geographic crosswalk, and A set of annual LWIA geographic definition files",
-            "modified": "2022-10-04T18:37:05.270Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-646",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2012-12-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Office of Assistant Secretary for Policy"
                 }
             },
+            "rights": "true",
+            "title": "adra_wiasrd_exits2007_with_acs"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Results from the study are summarized in Maxwell et al. (2012) and were based on data collected from five public sources: WIA Standardized Records Data (WIASRD) public-use files, American Community Survey (ACS) summary data, 2000 U.S. Census data, A Census-to-LWIA geographic crosswalk, and A set of annual LWIA geographic definition files",
+            "identifier": "OASP-12-012:044-646",
+            "issued": "2012-12-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T18:37:05.270Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "YPD_PublicUse_R12",
-            "description": "Survey data files: Participant Tracking System (PTS) and Participant 18-month Follow-up Survey",
-            "modified": "2022-10-04T18:39:48.911Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-648",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2019-06-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13243,36 +13220,36 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "adra_wiasrd_exits2009_with_acs"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Survey data files: Participant Tracking System (PTS) and Participant 18-month Follow-up Survey",
+            "identifier": "OASP-12-012:044-648",
+            "issued": "2019-06-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T18:39:48.911Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "YPD_PublicUse_R3",
-            "description": "Survey data files: Participant Tracking System (PTS) and Participant 18-month Follow-up Survey",
-            "modified": "2022-10-04T18:41:21.096Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-649",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2019-06-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13281,36 +13258,36 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "YPD_PublicUse_R12"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Survey data files: Participant Tracking System (PTS) and Participant 18-month Follow-up Survey",
+            "identifier": "OASP-12-012:044-649",
+            "issued": "2019-06-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T18:41:21.096Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "worker_survfile_nopii",
-            "description": "Survey data files: 2014-2015 telephone interviews with 8,503 adult workers across the U.S.",
-            "modified": "2022-10-04T18:46:29.459Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-647",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2016-11-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13319,106 +13296,106 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "YPD_PublicUse_R3"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Survey data files: 2014-2015 telephone interviews with 8,503 adult workers across the U.S.",
+            "identifier": "OASP-12-012:044-647",
+            "issued": "2016-11-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T18:46:29.459Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ccca_ruf_rev",
-            "description": "The Restricted Use File (RUF) for the Evaluation of the Cascades Job Corps College and Career Academy (CCCA) Pilot. Building on random assignment of applicants, the evaluation described the implementation of CCCA and its impacts.",
-            "modified": "2022-10-04T18:49:38.067Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-651",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Assistant Secretary for Policy"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "worker_survfile_nopii"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "The Restricted Use File (RUF) for the Evaluation of the Cascades Job Corps College and Career Academy (CCCA) Pilot. Building on random assignment of applicants, the evaluation described the implementation of CCCA and its impacts.",
+            "identifier": "OASP-12-012:044-651",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T18:49:38.067Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "etjraf_final",
-            "description": "This restricted-use data file presents early results from the Enhanced Transitional Jobs Demonstration (ETJD), which is using a rigorous random assignment research design to evaluate seven transitional jobs programs that targeted either individuals who had recently been released from prison, or parents who did not have custody of their children (\u201cnoncustodial\u201d parents), who owed child support, and who were unable to meet their obligations because they were unemployed.",
-            "modified": "2022-10-04T18:51:11.697Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-652",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Office of Assistant Secretary for Policy"
                 }
             },
+            "rights": "true",
+            "title": "ccca_ruf_rev"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "This restricted-use data file presents early results from the Enhanced Transitional Jobs Demonstration (ETJD), which is using a rigorous random assignment research design to evaluate seven transitional jobs programs that targeted either individuals who had recently been released from prison, or parents who did not have custody of their children (\u201cnoncustodial\u201d parents), who owed child support, and who were unable to meet their obligations because they were unemployed.",
+            "identifier": "OASP-12-012:044-652",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T18:51:11.697Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "YPD_PublicUse_All",
-            "description": "Survey data files: Participant Tracking System (PTS) and Participant 18-month Follow-up Survey",
-            "modified": "2022-10-04T18:43:53.792Z",
-            "accessLevel": "public",
-            "identifier": "OASP-12-012:044-650",
-            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "issued": "2019-06-01",
-            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13427,103 +13404,106 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "etjraf_final"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "description": "Survey data files: Participant Tracking System (PTS) and Participant 18-month Follow-up Survey",
+            "identifier": "OASP-12-012:044-650",
+            "issued": "2019-06-01",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/oasp/evaluation/publicusedata",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T18:43:53.792Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "odep_employer_survey_ruf",
-            "description": "The restricted use file for the Survey of Employer Policies on the Employment of People with Disabilities. The restricted use file does not include personally identifiable information, such as respondent name and address. The restricted use file is intended to be used only by DOL.",
-            "modified": "2022-10-04T18:56:25.076Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-653",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Assistant Secretary for Policy"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "YPD_PublicUse_All"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "The restricted use file for the Survey of Employer Policies on the Employment of People with Disabilities. The restricted use file does not include personally identifiable information, such as respondent name and address. The restricted use file is intended to be used only by DOL.",
+            "identifier": "OASP-12-012:044-653",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T18:56:25.076Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "th_swfi_grnt_surv_ruf",
-            "description": "The restricted use files for the surveys conducted for the Evaluation of the TechHire and Strengthening Working Families Initiative Grant Programs. The restricted use files do not include personally identifiable information (PII), such as respondent name and contact information. The restricted use file also does not include information that may pose a disclosure risk, such as employer name and other open-text answers. The restricted use files are intended to be used only by DOL.",
-            "modified": "2022-10-04T18:55:48.015Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-654",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Office of Assistant Secretary for Policy"
                 }
             },
+            "rights": "true",
+            "title": "odep_employer_survey_ruf"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "The restricted use files for the surveys conducted for the Evaluation of the TechHire and Strengthening Working Families Initiative Grant Programs. The restricted use files do not include personally identifiable information (PII), such as respondent name and contact information. The restricted use file also does not include information that may pose a disclosure risk, such as employer name and other open-text answers. The restricted use files are intended to be used only by DOL.",
+            "identifier": "OASP-12-012:044-654",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T18:55:48.015Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "th_swfi_prtn_surv_ruf",
-            "description": "The restricted use files for the surveys conducted for the Evaluation of the TechHire and Strengthening Working Families Initiative Grant Programs. The restricted use files do not include personally identifiable information (PII), such as respondent name and contact information. The restricted use file also does not include information that may pose a disclosure risk, such as employer name and other open-text answers. The restricted use files are intended to be used only by DOL.",
-            "modified": "2022-10-04T18:57:58.476Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-655",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13532,33 +13512,33 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "th_swfi_grnt_surv_ruf"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "The restricted use files for the surveys conducted for the Evaluation of the TechHire and Strengthening Working Families Initiative Grant Programs. The restricted use files do not include personally identifiable information (PII), such as respondent name and contact information. The restricted use file also does not include information that may pose a disclosure risk, such as employer name and other open-text answers. The restricted use files are intended to be used only by DOL.",
+            "identifier": "OASP-12-012:044-655",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T18:57:58.476Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "th_swfi_bif_ruf",
-            "description": "The restricted use files for the surveys conducted for the Evaluation of the TechHire and Strengthening Working Families Initiative Grant Programs. The restricted use files do not include personally identifiable information (PII), such as respondent name and contact information. The restricted use file also does not include information that may pose a disclosure risk, such as employer name and other open-text answers. The restricted use files are intended to be used only by DOL.",
-            "modified": "2022-10-04T19:00:48.786Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-656",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13567,33 +13547,33 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "th_swfi_prtn_surv_ruf"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "The restricted use files for the surveys conducted for the Evaluation of the TechHire and Strengthening Working Families Initiative Grant Programs. The restricted use files do not include personally identifiable information (PII), such as respondent name and contact information. The restricted use file also does not include information that may pose a disclosure risk, such as employer name and other open-text answers. The restricted use files are intended to be used only by DOL.",
+            "identifier": "OASP-12-012:044-656",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:00:48.786Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "th_swfi_6mo_surv_ruf",
-            "description": "The restricted use files for the surveys conducted for the Evaluation of the TechHire and Strengthening Working Families Initiative Grant Programs. The restricted use files do not include personally identifiable information (PII), such as respondent name and contact information. The restricted use file also does not include information that may pose a disclosure risk, such as employer name and other open-text answers. The restricted use files are intended to be used only by DOL.",
-            "modified": "2022-10-04T19:02:06.809Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-657",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13602,33 +13582,33 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "th_swfi_bif_ruf"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "The restricted use files for the surveys conducted for the Evaluation of the TechHire and Strengthening Working Families Initiative Grant Programs. The restricted use files do not include personally identifiable information (PII), such as respondent name and contact information. The restricted use file also does not include information that may pose a disclosure risk, such as employer name and other open-text answers. The restricted use files are intended to be used only by DOL.",
+            "identifier": "OASP-12-012:044-657",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:02:06.809Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "th_swfi_18mo_surv_ruf",
-            "description": "The restricted use files for the surveys conducted for the Evaluation of the TechHire and Strengthening Working Families Initiative Grant Programs. The restricted use files do not include personally identifiable information (PII), such as respondent name and contact information. The restricted use file also does not include information that may pose a disclosure risk, such as employer name and other open-text answers. The restricted use files are intended to be used only by DOL.",
-            "modified": "2022-10-04T19:05:20.326Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-658",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13637,33 +13617,33 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "th_swfi_6mo_surv_ruf"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "The restricted use files for the surveys conducted for the Evaluation of the TechHire and Strengthening Working Families Initiative Grant Programs. The restricted use files do not include personally identifiable information (PII), such as respondent name and contact information. The restricted use file also does not include information that may pose a disclosure risk, such as employer name and other open-text answers. The restricted use files are intended to be used only by DOL.",
+            "identifier": "OASP-12-012:044-658",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:05:20.326Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "th_swfi_prtn_surv_id_crosswalk",
-            "description": "The restricted use files for the surveys conducted for the Evaluation of the TechHire and Strengthening Working Families Initiative Grant Programs. The restricted use files do not include personally identifiable information (PII), such as respondent name and contact information. The restricted use file also does not include information that may pose a disclosure risk, such as employer name and other open-text answers. The restricted use files are intended to be used only by DOL.",
-            "modified": "2022-10-04T19:06:28.746Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-659",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13672,33 +13652,33 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "th_swfi_18mo_surv_ruf"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "The restricted use files for the surveys conducted for the Evaluation of the TechHire and Strengthening Working Families Initiative Grant Programs. The restricted use files do not include personally identifiable information (PII), such as respondent name and contact information. The restricted use file also does not include information that may pose a disclosure risk, such as employer name and other open-text answers. The restricted use files are intended to be used only by DOL.",
+            "identifier": "OASP-12-012:044-659",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:06:28.746Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "th_swfi_grnt_surv_id_crosswalk",
-            "description": "The restricted use files for the surveys conducted for the Evaluation of the TechHire and Strengthening Working Families Initiative Grant Programs. The restricted use files do not include personally identifiable information (PII), such as respondent name and contact information. The restricted use file also does not include information that may pose a disclosure risk, such as employer name and other open-text answers. The restricted use files are intended to be used only by DOL.",
-            "modified": "2022-10-04T19:07:23.437Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-660",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13707,33 +13687,33 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "th_swfi_prtn_surv_id_crosswalk"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "The restricted use files for the surveys conducted for the Evaluation of the TechHire and Strengthening Working Families Initiative Grant Programs. The restricted use files do not include personally identifiable information (PII), such as respondent name and contact information. The restricted use file also does not include information that may pose a disclosure risk, such as employer name and other open-text answers. The restricted use files are intended to be used only by DOL.",
+            "identifier": "OASP-12-012:044-660",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:07:23.437Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "WIA_ruf_30m",
-            "description": "The Restricted Use Files contains program administrative data, study intake information, and survey data used for the Workforce Investment Act (WIA) impact evaluation, along with the code by which these data can be used to replicate the study\u2019s estimation of the programs\u2019 impacts.",
-            "modified": "2022-10-04T19:08:26.959Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-661",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13742,33 +13722,33 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "th_swfi_grnt_surv_id_crosswalk"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "The Restricted Use Files contains program administrative data, study intake information, and survey data used for the Workforce Investment Act (WIA) impact evaluation, along with the code by which these data can be used to replicate the study\u2019s estimation of the programs\u2019 impacts.",
+            "identifier": "OASP-12-012:044-661",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:08:26.959Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "WIA_ruf_all",
-            "description": "The Restricted Use Files contains program administrative data, study intake information, and survey data used for the Workforce Investment Act (WIA) impact evaluation, along with the code by which these data can be used to replicate the study\u2019s estimation of the programs\u2019 impacts.",
-            "modified": "2022-10-04T19:10:00.097Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-662",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13777,103 +13757,103 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "WIA_ruf_30m"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "The Restricted Use Files contains program administrative data, study intake information, and survey data used for the Workforce Investment Act (WIA) impact evaluation, along with the code by which these data can be used to replicate the study\u2019s estimation of the programs\u2019 impacts.",
+            "identifier": "OASP-12-012:044-662",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:10:00.097Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "YCC_stu_baseline_survey_file",
-            "description": "Five restricted-use data files (RUFs) that were produced from data collected and used in the YCC impact study.",
-            "modified": "2022-10-04T19:12:54.344Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-663",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Assistant Secretary for Policy"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "WIA_ruf_all"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "Five restricted-use data files (RUFs) that were produced from data collected and used in the YCC impact study.",
+            "identifier": "OASP-12-012:044-663",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:12:54.344Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "YCC_stu_followup_survey_file",
-            "description": "Five restricted-use data files (RUFs) that were produced from data collected and used in the YCC impact study.",
-            "modified": "2022-10-04T19:14:21.321Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-664",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Office of Assistant Secretary for Policy"
                 }
             },
+            "rights": "true",
+            "title": "YCC_stu_baseline_survey_file"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "Five restricted-use data files (RUFs) that were produced from data collected and used in the YCC impact study.",
+            "identifier": "OASP-12-012:044-664",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:14:21.321Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "YCC_rct_analysis_file",
-            "description": "Five restricted-use data files (RUFs) that were produced from data collected and used in the YCC impact study.",
-            "modified": "2022-10-04T19:15:25.260Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-665",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13882,33 +13862,33 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "YCC_stu_followup_survey_file"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "Five restricted-use data files (RUFs) that were produced from data collected and used in the YCC impact study.",
+            "identifier": "OASP-12-012:044-665",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:15:25.260Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "YCC_qed_analysis_file",
-            "description": "Five restricted-use data files (RUFs) that were produced from data collected and used in the YCC impact study.",
-            "modified": "2022-10-04T19:16:16.184Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-666",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13917,33 +13897,33 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "YCC_rct_analysis_file"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "Five restricted-use data files (RUFs) that were produced from data collected and used in the YCC impact study.",
+            "identifier": "OASP-12-012:044-666",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:16:16.184Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "YCC_par_baseline_survey_file",
-            "description": "Five restricted-use data files (RUFs) that were produced from data collected and used in the YCC impact study.",
-            "modified": "2022-10-04T19:17:18.816Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-667",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13952,33 +13932,33 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "YCC_qed_analysis_file"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "Five restricted-use data files (RUFs) that were produced from data collected and used in the YCC impact study.",
+            "identifier": "OASP-12-012:044-667",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:17:18.816Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ybraf180625_final",
-            "description": "The data file includes variables needed to replicate findings from the interim and final impact reports from the YouthBuild Evaluation.",
-            "modified": "2022-10-04T19:19:03.289Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-668",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -13987,33 +13967,33 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "YCC_par_baseline_survey_file"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "The data file includes variables needed to replicate findings from the interim and final impact reports from the YouthBuild Evaluation.",
+            "identifier": "OASP-12-012:044-668",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:19:03.289Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "1 MAIN (Sections 0 4 5 6 7 8 9 10) v4 (stata 11)",
-            "description": "Restricted Use data from the ILAB Philippines study",
-            "modified": "2022-10-04T19:20:35.719Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-669",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -14022,33 +14002,33 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "ybraf180625_final"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "Restricted Use data from the ILAB Philippines study",
+            "identifier": "OASP-12-012:044-669",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:20:35.719Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2 INDIVIDUAL ( Sections 1 2 3 5) v4 (stata 11)",
-            "description": "Restricted Use data from the ILAB Philippines study",
-            "modified": "2022-10-04T19:21:38.180Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-670",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -14057,33 +14037,33 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "1 MAIN (Sections 0 4 5 6 7 8 9 10) v4 (stata 11)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "Restricted Use data from the ILAB Philippines study",
+            "identifier": "OASP-12-012:044-670",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:21:38.180Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "3 BUSINESS (Section 4) v4 (stata 11)",
-            "description": "Restricted Use data from the ILAB Philippines study",
-            "modified": "2022-10-04T19:22:32.446Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-671",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -14092,103 +14072,103 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "2 INDIVIDUAL ( Sections 1 2 3 5) v4 (stata 11)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "Restricted Use data from the ILAB Philippines study",
+            "identifier": "OASP-12-012:044-671",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:22:32.446Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "4 FARM (Section 6) v4 (stata 11)",
-            "description": "Restricted Use data from the ILAB Philippines study",
-            "modified": "2022-10-04T19:23:31.437Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-672",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
+                "name": "Office of Assistant Secretary for Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "3 BUSINESS (Section 4) v4 (stata 11)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "Restricted Use data from the ILAB Philippines study",
+            "identifier": "OASP-12-012:044-672",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:23:31.437Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "5 BACKYARD (Section 6) v4 (stata 11)",
-            "description": "Restricted Use data from the ILAB Philippines study",
-            "modified": "2022-10-04T19:24:19.610Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-673",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Assistant Secretary for Policy",
+                "name": "Office of the Assistant Secretary for Administration and Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "4 FARM (Section 6) v4 (stata 11)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "Restricted Use data from the ILAB Philippines study",
+            "identifier": "OASP-12-012:044-673",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:24:19.610Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "RTW_RUD",
-            "description": "The Restricted Use Dataset (RUD) for the Ready to Work (RTW) Partnership Grant Evaluation.",
-            "modified": "2022-10-04T19:25:15.127Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASP-12-012:044-674",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Assistant Secretary for Policy",
@@ -14197,114 +14177,128 @@
                     "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "5 BACKYARD (Section 6) v4 (stata 11)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CJ Krizan",
                 "hasEmail": "mailto:krizan.cornell.j@dol.gov"
             },
+            "description": "The Restricted Use Dataset (RUD) for the Ready to Work (RTW) Partnership Grant Evaluation.",
+            "identifier": "OASP-12-012:044-674",
             "keyword": [
                 "CEO",
                 "OASP"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-10-04T19:25:15.127Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Reentry Employment Opportunities (REO)  Joint Quarterly Narrative Report (QNR) (ETA-9179)",
-            "description": "Joint Quarterly Narrative Performance Report (ETA-9179) is used to collect qualitative information on grantee efforts, challenges, and outcomes.  The ETA-9179 allows grantees to provide a detailed account of all activities undertaken during the quarter including in-depth information on accomplishments, promising approaches, progress toward performance outcomes, and upcoming grant activities.",
-            "modified": "2022-12-20T00:00:00Z",
-            "accessLevel": "non-public",
-            "identifier": "ETA-5-012:008-444",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Employment and Training Administration"
+                "name": "Office of Assistant Secretary for Policy",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Department of Labor"
+                }
+            },
+            "rights": "true",
+            "title": "RTW_RUD"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jennifer Kemp",
                 "hasEmail": "mailto:kemp.jennifer.n@dol.gov"
             },
+            "description": "Joint Quarterly Narrative Performance Report (ETA-9179) is used to collect qualitative information on grantee efforts, challenges, and outcomes.  The ETA-9179 allows grantees to provide a detailed account of all activities undertaken during the quarter including in-depth information on accomplishments, promising approaches, progress toward performance outcomes, and upcoming grant activities.",
+            "identifier": "ETA-5-012:008-444",
             "keyword": [
                 "ETA",
                 "reemployment of justice-involved",
                 "reentry"
             ],
-            "bureauCode": [
-                "012:05"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-12-20T00:00:00Z",
             "programCode": [
                 "012:008"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Reemployment of Ex-Offenders (REO)  Youth Offender Quarterly Performance Report data (QPR)",
-            "description": "The Youth Offender QPR collects aggregate data on number of participants, characteristics of participants, and performance outcomes.",
-            "modified": "2022-12-20T00:00:00Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:008-443",
-            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
-            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "Reentry Employment Opportunities (REO)  Joint Quarterly Narrative Report (QNR) (ETA-9179)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jennifer Kemp",
                 "hasEmail": "mailto:kemp.jennifer.n@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
+            "description": "The Youth Offender QPR collects aggregate data on number of participants, characteristics of participants, and performance outcomes.",
+            "identifier": "ETA-5-012:008-443",
             "keyword": [
                 "ETA",
                 "ex offender",
                 "reemployment of ex offenders",
                 "reentry"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-12-20T00:00:00Z",
             "programCode": [
                 "012:008"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Reemployment of Ex-Offenders (REO) Prisoner Reentry Initiative Quarterly Performance Report data(QPR)",
-            "description": "The Reentry Employment Opportunities (REO) Youth QPR report collects aggregate data on number of participants, services provided, and performance outcomes. There is no individual data in the data set, only summary level quarterly data by individual grantee.",
-            "modified": "2024-09-27T15:10:39.658Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:008-442",
-            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
-            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "Reemployment of Ex-Offenders (REO)  Youth Offender Quarterly Performance Report data (QPR)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jennifer Kemp",
                 "hasEmail": "mailto:kemp.jennifer.n@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
+            "description": "The Reentry Employment Opportunities (REO) Youth QPR report collects aggregate data on number of participants, services provided, and performance outcomes. There is no individual data in the data set, only summary level quarterly data by individual grantee.",
+            "identifier": "ETA-5-012:008-442",
             "keyword": [
                 "ETA",
                 "adult",
@@ -14314,70 +14308,69 @@
                 "young adult",
                 "youth"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-27T15:10:39.658Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "YouthBuild Evaluation (Restricted Use File)",
-            "description": "YouthBuild is a \u201csecond chance\u201d program for young people. Targeted largely to high school dropouts, YouthBuild is a federally and privately funded program that provides construction-related training, educational services, counseling, and leadership development opportunities to low-income, out-of-school youth ages 16 to 24. The evaluation included 75 existing YouthBuild programs who received funding from DOL or the Corporation for National and Community Service in 2011. The evaluation included an impact analysis (with 72 sites), process study (all 75), and a cost analysis (58 sites).  Overall, the impact study includes 3,929 sample members. Three sites were unable to contribute sample members to the impact study; among the remaining sites, the study sample size varied considerably from 250 to 9. (Twenty-three sites have 25 or fewer study participants.) The main impact analysis drew on three waves of survey data and two administrative records sources and pooled data across all sites. A program features analysis used the extensive implementation research data to investigate how impacts might vary based on site-level characteristics.",
-            "modified": "2023-03-14T00:00:00Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:007-518",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "Reemployment of Ex-Offenders (REO) Prisoner Reentry Initiative Quarterly Performance Report data(QPR)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Wayne Gordon",
                 "hasEmail": "mailto:gordon.wayne@dol.gov"
             },
+            "description": "YouthBuild is a \u201csecond chance\u201d program for young people. Targeted largely to high school dropouts, YouthBuild is a federally and privately funded program that provides construction-related training, educational services, counseling, and leadership development opportunities to low-income, out-of-school youth ages 16 to 24. The evaluation included 75 existing YouthBuild programs who received funding from DOL or the Corporation for National and Community Service in 2011. The evaluation included an impact analysis (with 72 sites), process study (all 75), and a cost analysis (58 sites).  Overall, the impact study includes 3,929 sample members. Three sites were unable to contribute sample members to the impact study; among the remaining sites, the study sample size varied considerably from 250 to 9. (Twenty-three sites have 25 or fewer study participants.) The main impact analysis drew on three waves of survey data and two administrative records sources and pooled data across all sites. A program features analysis used the extensive implementation research data to investigate how impacts might vary based on site-level characteristics.",
+            "identifier": "ETA-5-012:007-518",
             "keyword": [
                 "ETA",
                 "evaluation",
                 "impact analysis",
                 "youthbuild"
             ],
-            "bureauCode": [
-                "012:05"
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-03-14T00:00:00Z",
             "programCode": [
                 "012:007"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Job Corps Program Data Set",
-            "description": "The Job Corps Program Data Set is collected and maintained by the Job Corps Data Center on all Job Corps centers, program participants, services, outcomes, costs, and other administrative information. ETA's Office of Job Corps creates various reports in aggregate from this data set that are publicly available on the www.jobcorps.gov website.",
-            "modified": "2024-09-27T15:08:01.522Z",
-            "accessLevel": "non-public",
-            "identifier": "ETA -5-012:009-522",
-            "describedBy": "https://www.jobcorps.gov/reports",
-            "landingPage": "https://www.jobcorps.gov/reports",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "YouthBuild Evaluation (Restricted Use File)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Shao Zhang",
                 "hasEmail": "mailto:Zhang.Shao@dol.gov"
             },
+            "describedBy": "https://www.jobcorps.gov/reports",
+            "description": "The Job Corps Program Data Set is collected and maintained by the Job Corps Data Center on all Job Corps centers, program participants, services, outcomes, costs, and other administrative information. ETA's Office of Job Corps creates various reports in aggregate from this data set that are publicly available on the www.jobcorps.gov website.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14385,6 +14378,7 @@
                     "title": "Job Corps Reports and Outcomes"
                 }
             ],
+            "identifier": "ETA -5-012:009-522",
             "keyword": [
                 "ETA",
                 "admissions",
@@ -14396,39 +14390,39 @@
                 "performance",
                 "student enrollment"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.jobcorps.gov/reports",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-27T15:08:01.522Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Employment and Training Administration"
+            },
+            "rights": "Not Available",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "Job Corps Program Data Set"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Unemployment Insurance Benefit Rights and Experience Data (ETA-218)",
-            "description": "Historical series of the State Unemployment Insurance (UI) Benefit Rights and Experience Reports (ETA-218) including information on claimant eligibility which is used for evaluating state benefit formulas as administered under state UI programs.",
-            "modified": "2024-03-29T16:40:51.736Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:013-466",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_218",
-            "rights": "TRUE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Employment and Training Administration"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
+            "description": "Historical series of the State Unemployment Insurance (UI) Benefit Rights and Experience Reports (ETA-218) including information on claimant eligibility which is used for evaluating state benefit formulas as administered under state UI programs.",
+            "identifier": "ETA-5-012:013-466",
             "keyword": [
                 "ETA",
                 "benefits",
@@ -14439,69 +14433,70 @@
                 "weeks claimed",
                 "weeks paid"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_218",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:40:51.736Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Self Employment Assistance (ETA-9161)",
-            "description": "Historical series of Self Employment Assistance reports (ETA-9161) in which states provide quarterly information on claimants that enter the self-employment assistance program.",
-            "modified": "2024-03-29T16:13:32.751Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-486",
-            "describedBy": "https://wdr.doleta.gov/directives/attach/ETAH/ETHand401_5th.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9161",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Unemployment Insurance Benefit Rights and Experience Data (ETA-218)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://wdr.doleta.gov/directives/attach/ETAH/ETHand401_5th.pdf",
+            "description": "Historical series of Self Employment Assistance reports (ETA-9161) in which states provide quarterly information on claimants that enter the self-employment assistance program.",
+            "identifier": "ETA-5-012:013-486",
             "keyword": [
                 "ETA",
                 "sea",
                 "self employment assistance"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9161",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:13:32.751Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Occupational Information Network (O*NET) Production Database data",
-            "description": "Comprehensive profile of occupational descriptors and characteristics for 923 O*NET-SOC occupations.  Includes, knowledge, skills, abilities, tasks, work activities and additional attributes.  Available as downloadable files, and web services/APIs.   See:  www.onetcenter.org",
-            "modified": "2023-05-23T00:00:00Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:018-459",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Self Employment Assistance (ETA-9161)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Steve Rietzke",
                 "hasEmail": "mailto:rietzke.steven@dol.gov"
             },
+            "description": "Comprehensive profile of occupational descriptors and characteristics for 923 O*NET-SOC occupations.  Includes, knowledge, skills, abilities, tasks, work activities and additional attributes.  Available as downloadable files, and web services/APIs.   See:  www.onetcenter.org",
+            "identifier": "ETA-5-012:018-459",
             "keyword": [
                 "ETA",
                 "abilities",
@@ -14510,34 +14505,34 @@
                 "skills",
                 "tasks"
             ],
-            "bureauCode": [
-                "012:05"
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-05-23T00:00:00Z",
             "programCode": [
                 "012:018"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Providing Public Workforce Services to Job Seekers: 30-month Impact Findings on the WIA Adult and Dislocated Worker Programs (WIA Gold)",
-            "description": "The WIA [Workforce Investment Act of 1998] Adult and Dislocated Worker Programs Gold Standard Evaluation, provides findings on participant outcomes 30-months after random assignment under the evaluation.  The evaluation began in 2008 and used a random assignment design to examine the impact of higher-tiered services provided by the Adult and Dislocated Worker programs in WIA, as implemented by 28 randomly selected local workforce investment areas (LWIAs) operating nationwide. The analysis describes the impact of different services provided under WIA core and intensive; and core, intensive and training. Researchers followed more than 34,000 study participants after random assignment collecting outcome data through follow-up surveys at 15 and 30 months and the National Directory of New Hires (an administrative database containing information on earnings and employment) at 36 months after random assignment.",
-            "modified": "2023-03-14T00:00:00Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:016-516",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Occupational Information Network (O*NET) Production Database data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Wayne Gordon",
                 "hasEmail": "mailto:gordon.wayne@dol.gov"
             },
+            "description": "The WIA [Workforce Investment Act of 1998] Adult and Dislocated Worker Programs Gold Standard Evaluation, provides findings on participant outcomes 30-months after random assignment under the evaluation.  The evaluation began in 2008 and used a random assignment design to examine the impact of higher-tiered services provided by the Adult and Dislocated Worker programs in WIA, as implemented by 28 randomly selected local workforce investment areas (LWIAs) operating nationwide. The analysis describes the impact of different services provided under WIA core and intensive; and core, intensive and training. Researchers followed more than 34,000 study participants after random assignment collecting outcome data through follow-up surveys at 15 and 30 months and the National Directory of New Hires (an administrative database containing information on earnings and employment) at 36 months after random assignment.",
+            "identifier": "ETA-5-012:016-516",
             "keyword": [
                 "ETA",
                 "adult dislocated worker grant",
@@ -14545,45 +14540,44 @@
                 "wia",
                 "workforce investment act"
             ],
-            "bureauCode": [
-                "012:05"
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-03-14T00:00:00Z",
             "programCode": [
                 "012:016"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Statutory Allotment Formula Results",
-            "description": "Statutory Allotment Formula Results are the annual results of completing the statutory formulas for the Workforce Innovation and Opportunity Act (WIOA) Adult, Youth, and Dislocated Worker programs; Wagner Peyser Employment Service program; and Senior Community Service Employment Program (SCSEP).  ETA prepares and posts the results of the formulas annually, and updates as required based on rescission of funds by Congress in future appropriations acts. The dataset includes dollar amounts by state/territory authorized to be obligated to grantees for the WIOA Title I Adult, Dislocated Worker, Youth, WIOA Title III Wagner-Peyser Employment Service and SCSEP programs. The data is posted in Excel and pdf formats on ETA's Budget website at https://www.dol.gov/agencies/eta/budget/formula/state.",
-            "modified": "2024-12-26T19:34:45.596Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:018-533",
-            "describedBy": "https://www.dol.gov/agencies/eta/budget/formula/state",
-            "describedByType": "text/html",
-            "landingPage": "https://www.dol.gov/agencies/eta/budget/formula/state",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "Providing Public Workforce Services to Job Seekers: 30-month Impact Findings on the WIA Adult and Dislocated Worker Programs (WIA Gold)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Anita Harvey",
                 "hasEmail": "mailto:harvey.anita@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/budget/formula/state",
+            "describedByType": "text/html",
+            "description": "Statutory Allotment Formula Results are the annual results of completing the statutory formulas for the Workforce Innovation and Opportunity Act (WIOA) Adult, Youth, and Dislocated Worker programs; Wagner Peyser Employment Service program; and Senior Community Service Employment Program (SCSEP).  ETA prepares and posts the results of the formulas annually, and updates as required based on rescission of funds by Congress in future appropriations acts. The dataset includes dollar amounts by state/territory authorized to be obligated to grantees for the WIOA Title I Adult, Dislocated Worker, Youth, WIOA Title III Wagner-Peyser Employment Service and SCSEP programs. The data is posted in Excel and pdf formats on ETA's Budget website at https://www.dol.gov/agencies/eta/budget/formula/state.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/eta/budget/formula/state",
-                    "title": "State Statutory Formula Funding",
-                    "description": "Data are provided for major ETA programs which use statutory formulas to determine the amount of grant funds each State (or outlying area) receives."
+                    "description": "Data are provided for major ETA programs which use statutory formulas to determine the amount of grant funds each State (or outlying area) receives.",
+                    "title": "State Statutory Formula Funding"
                 }
             ],
+            "identifier": "ETA-5-012:018-533",
             "keyword": [
                 "ETA",
                 "allotment formula data factors",
@@ -14604,36 +14598,36 @@
                 "workforce innovation and opportunity act",
                 "wp-es"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/eta/budget/formula/state",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-26T19:34:45.596Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "WIA Non-Experimental Net Impact Evaluation Dataset",
-            "description": "The evaluation employs administrative data from 12 states, covering approximately 160,000 WIA Adult, WIA Dislocated Worker and WIA Youth participants and nearly 3 million comparison group members. Focusing on participants who entered WIA programs between July 2003 and June 2005, the evaluation considers the impact for all those in the program, the impact for those receiving only Core or Intensive Services, and the incremental impact of Training Services. This dataset contains all of the information used to conduct the non-experimental evaluation estimates for the 1) WIA Client Treatment Group and 2) The Unemployment Insurance and Employment Service Client comparison group. The administrative data collected by IMPAQ for the \"Workforce Investment Act Non-Experimental Net Impact Evaluation\" project were received from state agencies in three segments: annual Workforce Investment Act Standardized Record Data (WIASRD) or closely related files, Unemployment Insurance data, and Unemployment Insurance Wage Record data. The analysis were conducted for twelve states; however, based on the data sharing agreements, the Public Use Data (PUD) set includes data for nine states only. Our agreement for use of these data required that the identity of those states was not revealed. As a result, all geographical identifiers were removed to preserve states' anonymity.",
-            "modified": "2023-03-14T00:00:00Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:016-519",
-            "describedBy": "https://www.dol.gov/agencies/eta/reports/wia-evaluation-dataset",
-            "landingPage": "https://www.dol.gov/agencies/eta/reports/wia-evaluation-dataset",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "true",
+            "title": "Statutory Allotment Formula Results"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Wayne Gordon",
                 "hasEmail": "mailto:gordon.wayne@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/reports/wia-evaluation-dataset",
+            "description": "The evaluation employs administrative data from 12 states, covering approximately 160,000 WIA Adult, WIA Dislocated Worker and WIA Youth participants and nearly 3 million comparison group members. Focusing on participants who entered WIA programs between July 2003 and June 2005, the evaluation considers the impact for all those in the program, the impact for those receiving only Core or Intensive Services, and the incremental impact of Training Services. This dataset contains all of the information used to conduct the non-experimental evaluation estimates for the 1) WIA Client Treatment Group and 2) The Unemployment Insurance and Employment Service Client comparison group. The administrative data collected by IMPAQ for the \"Workforce Investment Act Non-Experimental Net Impact Evaluation\" project were received from state agencies in three segments: annual Workforce Investment Act Standardized Record Data (WIASRD) or closely related files, Unemployment Insurance data, and Unemployment Insurance Wage Record data. The analysis were conducted for twelve states; however, based on the data sharing agreements, the Public Use Data (PUD) set includes data for nine states only. Our agreement for use of these data required that the identity of those states was not revealed. As a result, all geographical identifiers were removed to preserve states' anonymity.",
+            "identifier": "ETA-5-012:016-519",
             "keyword": [
                 "ETA",
                 "participant outcomes",
@@ -14641,70 +14635,70 @@
                 "wia non-expermental net impact",
                 "workforce system"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.dol.gov/agencies/eta/reports/wia-evaluation-dataset",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-03-14T00:00:00Z",
             "programCode": [
                 "012:016"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State/Federal Licensed Occupations data",
-            "description": "Dataset includes occupational licenses by state. Data is provided by the state. All licenses are coded to an O*NET-SOC code and by state. \n\nCareerOneStop.org web service available upon request.",
-            "modified": "2023-06-06T00:00:00Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:018-457",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "WIA Non-Experimental Net Impact Evaluation Dataset"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Steve Rietzke",
                 "hasEmail": "mailto:rietzke.steven@dol.gov"
             },
+            "description": "Dataset includes occupational licenses by state. Data is provided by the state. All licenses are coded to an O*NET-SOC code and by state. \n\nCareerOneStop.org web service available upon request.",
+            "identifier": "ETA-5-012:018-457",
             "keyword": [
                 "ETA",
                 "credentials",
                 "licensed occupations",
                 "licenses"
             ],
-            "bureauCode": [
-                "012:05"
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-06-06T00:00:00Z",
             "programCode": [
                 "012:018"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Historical Series of Combined Unemployment Insurance Wage Claim Activities (ETA-586)",
-            "description": "Historical series of Interstate Arrangement-Employment and Wages Reports (ETA-586) in which states provide data on claims filed under the interstate agreement for combining wages and employment.The dataset includes information on combined wage claims and benefit payment activities, and timelapse data on first payments and receipt of wage requests.",
-            "modified": "2024-03-29T16:22:38.081Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-479",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_586",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "State/Federal Licensed Occupations data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
+            "description": "Historical series of Interstate Arrangement-Employment and Wages Reports (ETA-586) in which states provide data on claims filed under the interstate agreement for combining wages and employment.The dataset includes information on combined wage claims and benefit payment activities, and timelapse data on first payments and receipt of wage requests.",
+            "identifier": "ETA-5-012:013-479",
             "keyword": [
                 "ETA",
                 "billing and reimbursement",
@@ -14712,36 +14706,36 @@
                 "first payment",
                 "time lapse"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_586",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:22:38.081Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Historical Series of Profiling and Reemployment Services (ETA-9048)",
-            "description": "Historical series of Profiling and Reemployment Services reports (ETA-9048) in which states provide quarterly information on the Worker Profiling and Reemployment Service activities of claimants who are profiled to assess their likelihood of exhausting benefits. Worker profiling allows for the targeting of reemployment services to those most in need. The data on this report is used for evaluation and monitoring of the Worker Profiling and Reemployment Services system on a national level.",
-            "modified": "2024-03-29T16:19:08.563Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-482",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9048",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Historical Series of Combined Unemployment Insurance Wage Claim Activities (ETA-586)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
+            "description": "Historical series of Profiling and Reemployment Services reports (ETA-9048) in which states provide quarterly information on the Worker Profiling and Reemployment Service activities of claimants who are profiled to assess their likelihood of exhausting benefits. Worker profiling allows for the targeting of reemployment services to those most in need. The data on this report is used for evaluation and monitoring of the Worker Profiling and Reemployment Services system on a national level.",
+            "identifier": "ETA-5-012:013-482",
             "keyword": [
                 "ETA",
                 "reemployment",
@@ -14749,43 +14743,43 @@
                 "worker profiling",
                 "wprs"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9048",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:19:08.563Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Comparison of State Unemployment Insurance (UI) Laws",
-            "description": "The Comparison of State Unemployment Insurance (UI) Laws is an annual report that provides state-by-state information on workers covered, benefit eligibility, methods of financing and other areas of interest in the UI program. It also includes information on the temporary disability programs operated in six states. The Comparison is published annually.",
-            "modified": "2024-12-26T19:07:41.464Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-500",
-            "landingPage": "https://oui.doleta.gov/unemploy/statelaws.asp#RecentStatelaw",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Historical Series of Profiling and Reemployment Services (ETA-9048)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daniel Hays",
                 "hasEmail": "mailto:hays.daniel@dol.gov"
             },
+            "description": "The Comparison of State Unemployment Insurance (UI) Laws is an annual report that provides state-by-state information on workers covered, benefit eligibility, methods of financing and other areas of interest in the UI program. It also includes information on the temporary disability programs operated in six states. The Comparison is published annually.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://oui.doleta.gov/unemploy/statelaws.asp#RecentStatelaw",
-                    "title": "Most Recent Comparison of State UI Laws",
-                    "description": "The Comparison of State Unemployment Insurance Laws provides state-by-state information on workers covered, benefit eligibility, methods of financing and other areas of interest in the UI program. It also includes information on the temporary disability programs operated in six states. The Comparison is published annually."
+                    "description": "The Comparison of State Unemployment Insurance Laws provides state-by-state information on workers covered, benefit eligibility, methods of financing and other areas of interest in the UI program. It also includes information on the temporary disability programs operated in six states. The Comparison is published annually.",
+                    "title": "Most Recent Comparison of State UI Laws"
                 }
             ],
+            "identifier": "ETA-5-012:013-500",
             "keyword": [
                 "ETA",
                 "benefit eligibility",
@@ -14793,186 +14787,186 @@
                 "state unemployment insurance laws",
                 "temporary disability programs"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/statelaws.asp#RecentStatelaw",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-26T19:07:41.464Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Most Recent Report on State Legislation",
-            "description": "This report summarizes amendments to state unemployment insurance laws and regulations recently enacted/promulgated in the various states.",
-            "modified": "2024-12-26T19:04:50.904Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-502",
-            "landingPage": "https://oui.doleta.gov/unemploy/statelaws.asp#RecentStatelaw",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Comparison of State Unemployment Insurance (UI) Laws"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daniel Hays",
                 "hasEmail": "mailto:hays.daniel@dol.gov"
             },
+            "description": "This report summarizes amendments to state unemployment insurance laws and regulations recently enacted/promulgated in the various states.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://oui.doleta.gov/unemploy/statelaws.asp#RecentStatelaw",
-                    "title": "Most Recent Report on State Legislation",
-                    "description": "This report summarizes amendments to state unemployment insurance laws and regulations recently enacted/promulgated in the various states."
+                    "description": "This report summarizes amendments to state unemployment insurance laws and regulations recently enacted/promulgated in the various states.",
+                    "title": "Most Recent Report on State Legislation"
                 }
             ],
+            "identifier": "ETA-5-012:013-502",
             "keyword": [
                 "ETA",
                 "state unemployment insurance laws"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/statelaws.asp#RecentStatelaw",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-26T19:04:50.904Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Apprenticeship Data and Statistics",
-            "description": "The Registered Apprenticeship data displayed in this resource is derived from several different sources with differing abilities to provide disaggregated data. The 25 federally-administered states and 16 federally-recognized State Apprenticeship Agencies (SAAs) use the Employment and Training Administration's Registered Apprenticeship Partners Information Database System (RAPIDS) to provide individual apprentice and sponsor data. This subset of data is referred to as RAPIDS data and can be disaggregated to provide additional specificity. The federal subset of that data (25 states plus national programs) is known as the Federal Workload. The remaining federally recognized SAAs and the U.S. Military Apprenticeship Program (USMAP) provide limited aggregate data on a quarterly basis that is then combined with RAPIDS data to provide a national data set on high-level metrics (apprentices and programs) but cannot generally be broken out in greater detail beyond the data provided here.",
-            "modified": "2023-03-14T00:00:00Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:017-535",
-            "describedBy": "https://www.apprenticeship.gov/sites/default/files/Apprentices%20by%20State%20Map%20Navigation_Last%20Updated_20221228.pdf",
-            "landingPage": "https://www.apprenticeship.gov/data-and-statistics",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Most Recent Report on State Legislation"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alex Jordan",
                 "hasEmail": "mailto:jordan.alexander@dol.gov"
             },
+            "describedBy": "https://www.apprenticeship.gov/sites/default/files/Apprentices%20by%20State%20Map%20Navigation_Last%20Updated_20221228.pdf",
+            "description": "The Registered Apprenticeship data displayed in this resource is derived from several different sources with differing abilities to provide disaggregated data. The 25 federally-administered states and 16 federally-recognized State Apprenticeship Agencies (SAAs) use the Employment and Training Administration's Registered Apprenticeship Partners Information Database System (RAPIDS) to provide individual apprentice and sponsor data. This subset of data is referred to as RAPIDS data and can be disaggregated to provide additional specificity. The federal subset of that data (25 states plus national programs) is known as the Federal Workload. The remaining federally recognized SAAs and the U.S. Military Apprenticeship Program (USMAP) provide limited aggregate data on a quarterly basis that is then combined with RAPIDS data to provide a national data set on high-level metrics (apprentices and programs) but cannot generally be broken out in greater detail beyond the data provided here.",
+            "identifier": "ETA-5-012:017-535",
             "keyword": [
                 "ETA",
                 "registered apprenticeship"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.apprenticeship.gov/data-and-statistics",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-03-14T00:00:00Z",
             "programCode": [
                 "012:017"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Employment and Training Administration"
+            },
+            "rights": "TRUE",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "Apprenticeship Data and Statistics"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "CW-1 Program Historical Data",
-            "description": "This dataset includes data the Employment and Training Administration's Office of Foreign Labor Certification (OFLC) collected from CW-1 applications during previous fiscal years. The CW-1 nonimmigrant visa program permits employers who meet program requirements to hire nonimmigrant workers temporarily in the Commonwealth of the Northern Mariana Island (CNMI or \"Commonwealth\") to perform services or labor based on the employer's need. The dataset includes information on employers, geography, and job details for participants in the CW-1 program. Historical CW-1 public disclosure data is available on the OFLC website in the Performance Data section. Data is available as Excel files in aggregate form at https://www.dol.gov/agencies/eta/foreign-labor/performance.",
-            "modified": "2023-05-15T00:00:00Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:015-530",
-            "describedBy": "https://www.dol.gov/agencies/eta/foreign-labor/performance",
-            "landingPage": "https://www.dol.gov/agencies/eta/foreign-labor/performance",
-            "rights": "TRUE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Employment and Training Administration"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rob Jordan",
                 "hasEmail": "mailto:jordan.rob@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/foreign-labor/performance",
+            "description": "This dataset includes data the Employment and Training Administration's Office of Foreign Labor Certification (OFLC) collected from CW-1 applications during previous fiscal years. The CW-1 nonimmigrant visa program permits employers who meet program requirements to hire nonimmigrant workers temporarily in the Commonwealth of the Northern Mariana Island (CNMI or \"Commonwealth\") to perform services or labor based on the employer's need. The dataset includes information on employers, geography, and job details for participants in the CW-1 program. Historical CW-1 public disclosure data is available on the OFLC website in the Performance Data section. Data is available as Excel files in aggregate form at https://www.dol.gov/agencies/eta/foreign-labor/performance.",
+            "identifier": "ETA-5-012:015-530",
             "keyword": [
                 "ETA",
                 "cw-1",
                 "oflc performance data"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.dol.gov/agencies/eta/foreign-labor/performance",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-05-15T00:00:00Z",
             "programCode": [
                 "012:015"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Employment and Training Administration"
+            },
+            "rights": "TRUE",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "CW-1 Program Historical Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Job Clubs data",
-            "description": "List of Job Club names, location, and contact information, including phone number and website link, where available.  Job Clubs provide networking opportunities for unemployed individuals and help creating a resume, completing a application, and writing a cover letter.\n\nCareerOneStop.org web service available upon request",
-            "modified": "2023-06-06T00:00:00Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:018-453",
-            "rights": "TRUE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Employment and Training Administration"
-            },
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Steve Rietzke",
                 "hasEmail": "mailto:rietzke.steven@dol.gov"
             },
+            "description": "List of Job Club names, location, and contact information, including phone number and website link, where available.  Job Clubs provide networking opportunities for unemployed individuals and help creating a resume, completing a application, and writing a cover letter.\n\nCareerOneStop.org web service available upon request",
+            "identifier": "ETA-5-012:018-453",
             "keyword": [
                 "job clubs"
             ],
-            "bureauCode": [
-                "012:05"
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-06-06T00:00:00Z",
             "programCode": [
                 "012:018"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Employment and Training Administration"
+            },
+            "rights": "TRUE",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "Job Clubs data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Unemployment Insurance Financial Transaction Data (ETA-2112)",
-            "description": "Historical series of Unemployment Insurance (UI) Financial Transaction Summary Reports (ETA-2112) in which states report monthly transactions summaries from state unemployment trust fund. The reports include the clearing account, the Unemployment Trust Fund Account (UTF) and the Benefit Payment Account.",
-            "modified": "2024-03-29T16:35:00.058Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:013-472",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_2112",
-            "rights": "TRUE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Employment and Training Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
```

